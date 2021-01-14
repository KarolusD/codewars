import hashlib

def pass_hash(str):
    result=hashlib.md5(str.encode())
    return result.hexdigest()


print("Basic tests")
print(pass_hash('password') == '5f4dcc3b5aa765d61d8327deb882cf99');
print(pass_hash('abc123') == 'e99a18c428cb38d5f260853678922e03');