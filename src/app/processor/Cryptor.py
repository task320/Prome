import hashlib, binascii

class Cryptor:
    @staticmethod
    def output_sha256(user_id, password):
        dk = hashlib.pbkdf2_hmac('sha256', 
                                password.encode(), 
                                user_id.encode(), 
                                100000)
        return binascii.hexlify(dk).decode()
    
