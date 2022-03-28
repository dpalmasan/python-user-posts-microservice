from base64 import urlsafe_b64decode
from json import loads


def get_claims_from_token(jwt_token: str) -> dict:
    claims = jwt_token.split(".")[1]
    padding = "=" * (4 - len(claims) % 4)
    return loads(urlsafe_b64decode(f"{claims}{padding}"))
