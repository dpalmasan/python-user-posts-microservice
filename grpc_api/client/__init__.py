import grpc
from grpc_api.auth import auth_pb2_grpc
from grpc_api.auth import auth_pb2


class AuthService:
    def __init__(self, uri="0.0.0.0:50051"):
        channel = grpc.insecure_channel(uri)
        self._stub = auth_pb2_grpc.AuthServiceStub(channel)

    def validate_token(self, token):
        request = auth_pb2.TokenRequest(token=token)
        res = self._stub.ValidateToken(request)
        return res.success
