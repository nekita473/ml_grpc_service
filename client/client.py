import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
import model_pb2, model_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = model_pb2_grpc.PredictionServiceStub(channel)

request = model_pb2.PredictRequest(feature1=0.7, feature2=1.4)
response = stub.Predict(request)
print("Prediction:", response.prediction, "Probability:", response.proba)