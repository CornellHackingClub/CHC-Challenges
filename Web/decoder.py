secret_key="LOLOLOL_I_Am_So_Secret"
cookie_str=".eJw9js1qwzAQhF-l6NxDpMSQBnoI2BYO7AoX2UJ7KUn8K0ehpCmJFfLuFT30MJdh5pt5sPy079nmwV4ObMPKxZC2orwdXNOh_hDA1xwEzhCabh8wwXp9P5yit9yJqI5c_g2hfmPPV_Y5Nv8cSmkib4MysEKXCRTVDHo3KknO6vKGPlui6-9kqplcv7KmuFkNHPVWxNyEsh4hMiD0CTjyZAoeOTGPgzL5QBInSrdCyXwidww25A40jqCPnHxxp7RYgYEEJQ2oT6NKe67iBkmbgK9jp1womS2Uqd7_vn-1F78_t-cr21wvP-3zF7TfWtU.Cv47Xg.x-pfHw6xTU-GzgmKfaXfDylF1go"
def decode_flask_cookie(secret_key, cookie_str):
    import hashlib
    from itsdangerous import URLSafeTimedSerializer
    from flask.sessions import TaggedJSONSerializer
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)

print decode_flask_cookie(secret_key, cookie_str)
