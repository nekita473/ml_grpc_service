import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
from grpc_reflection.v1alpha import reflection
from concurrent import futures
import model_pb2, model_pb2_grpc
import joblib, pandas as pd


class PredictionService(model_pb2_grpc.PredictionServiceServicer):
    def __init__(self):
        model_path = os.environ.get('MODEL_PATH')
        if model_path is None:
            raise ValueError('MODEL_PATH variable is not set')
        self.model = joblib.load(model_path)

        self.model_version = os.environ.get('MODEL_VERSION')
        if self.model_version is None:
            raise ValueError('MODEL_PATH variable is not set')

    def Predict(self, request, context):
        df = pd.DataFrame([{
            "feature1": request.feature1,
            "feature2": request.feature2
        }])
        pred = self.model.predict(df)[0]
        proba = self.model.predict_proba(df)[0][1]
        return model_pb2.PredictResponse(prediction=str(pred), proba=str(proba))

    def Health(self, request, context):
        return model_pb2.HealthResponse(status="ok", model_version=self.model_version)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    model_pb2_grpc.add_PredictionServiceServicer_to_server(PredictionService(), server)

    SERVICE_NAMES = (
        model_pb2.DESCRIPTOR.services_by_name['PredictionService'].full_name,
        # reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()