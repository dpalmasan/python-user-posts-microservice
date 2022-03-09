from grpc_api.client import AuthService


# auth_service_client = AuthService()


class AuthServiceStub(AuthService):
    """Dummy Stub"""

    def __init__(self):
        self.token = ""

    def validate_token(self, token):
        return token != self.token


auth_service_client = AuthServiceStub()
