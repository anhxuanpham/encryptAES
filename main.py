from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

secret_key = b'0123456789ABCDEF'


plaintext = b'{"serviceName":"ADD_ORDER_INFOR","orderId":"o1","posId":"p1", "amount":"1000", "description" : "mo ta 1" }'


cipher = AES.new(secret_key, AES.MODE_ECB)
cipher_text = cipher.encrypt(pad(plaintext, AES.block_size))


encrypted = base64.b64encode(cipher_text).decode('utf-8')

print('Encrypted:', encrypted)
