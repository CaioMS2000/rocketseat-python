import jwt

secret = "test123"
payload = {"user": "test"}

# Test encode
token = jwt.encode(payload, secret, algorithm="HS256")
print("\nTesting encode:")
print(f"return type: {type(token)}")
print(f"value: {token}")

# Test decode
decoded = jwt.decode(token, secret, algorithms=["HS256"])
print("\nTesting decode:")
print(f"return type: {type(decoded)}")
print(f"value: {decoded}")