secret_key="LOLOLOL_I_Am_So_Secret"
cookie_str=".eJw9jkFrwkAQhf9K2XMPyUbBCj2kbCINzEgkusxcRJtoHXelWItxxP_e0EMP7_J473vvbsqw2Zvp3TxtzdTUyafrbH3dSrvDZmEhnaRg8Qba7jaKY1xN-m0YvKyyg3Ys5Tfo6sU8ns360P5zSPOeI6Qs-xH75Zg9B7K1pVhF9uURpEjRLRP2iwNpKWgxQByWlCO75Q2aRSSpIjiWuYMry_E65I6khYIl5VkV0ZHlGY2oyROStwBKCcrAcasDRsjQV4Jap-xRSN6VXd4PzTBvPjJUyOa-DNgUr3_fv7pz3Jy608VML-ef7vEL7Ixbwg.Cu8Fqw.qyMHnQ_eZ8zsTK4EAqerR5fxSsM"
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
