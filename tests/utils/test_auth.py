from utils.auth import get_claims_from_token

TEST_JWT_TOKEN = (
    "eyJhbGciOiJSUzI1NiIsImtpZCI6IjRhYmFjY2Y1LTFiMTYtNGVjZi1hYTk4LWM3NTA5MWZm"
    "YWI1YyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgzMzQ3MTQsImlhdCI6MTY0ODMzNDQxNCw"
    "icm9sZSI6InJlZ3VsYXIiLCJ1c2VyX2lkIjoiNjIwNTVlN2M1MGMxNzhmYzMwOGJmNDQ5In0"
    ".Wm3Eq7W_oYZh6C8cl1Q7W1MILFnThGG_F1zwvPZD8A-QedNWVC2KPxfEFXIo7zNqw6mlGt2"
    "0tGxm0dU8OpsPBT12hrobpM4gMu0Eg6fddJ_RBvTlHVpNwfjLMcN_VNC1MBCo2Ca4osqApx0"
    "IAgpITKKpTOZON-65li9NyZk4c339QO8d4GeiWD2fIv5RgC-f355e27lgh6NFDC5PVAo91RE"
    "xu-2b3RABsy5scwIVWV-RoZraDwYNolKfWui-_RL4JZT2QpAiTfQbZ_gOm_WtgSuZ4ETpDeP"
    "z6cgDEDtUAdER6EF0XiNsoPhbygtR6HmLYNQMx2fOYnHDDlbrrBq7ow"
)


def test_get_claims_from_token():
    claims = get_claims_from_token(TEST_JWT_TOKEN)

    assert "user_id" in claims
    assert claims["user_id"] == "62055e7c50c178fc308bf449"
