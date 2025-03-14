import bcrypt

class PasswordHandler:
    def encrypt(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        return hashed_password.decode('utf-8')

    def compare(self, password: str, encrypted_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), encrypted_password.encode('utf-8'))