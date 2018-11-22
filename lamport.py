#Jinglan Wang

from hashlib import sha256
import secrets
import bitstring
import binascii

# Make it easy to hash things, encoded in the right way
def hash(data):
    return sha256(data.encode('utf-8')).digest()

# Generate two lists each with 256 elements, each element 256 bits in length
# Return two lists of secret keys
def gen_secretKey():
    sk0, sk1 = []
    for i in range(256): sk0.append(hex(secrets.randbits(256)))
    for i in range(256): sk1.append(hex(secrets.randbits(256)))
    return sk0, sk1

# Generate a public key by hashing the secret keys
# Return two hashed arrays that constitute pubkey pairs
def gen_publicKey(secretKey):
    sk0, sk1 = privkey
    pk0 = list(map(lambda i: hash(i), sk0))
    pk1 = list(map(lambda i: hash(i), sk1))
    return pk0, pk1

# Format a message correctly by turning it into 256 bits
def messageBits(rawMessage):
    return str(bitstring.BitArray(hash(message)).bin)

# Return a list of half of the secret keys based on the
# value at each index of the message
def signMessage(secretKey, message):
    sk0, sk1 = secretKey
    sigList = []
    for i in range(256):
        if message[i] == '0':
            sigList.append(sk0[i])
        elif message[i]== '1':
            sigList.append(sk1[i])
    return sigList


# Validating the sigatures... it looks like you reveal your secretkeys!???!!
def validate(publicKey, signatures, message):
    for i in range(signatures):
        if 



# Check it out
secretKey = gen_secretKey()
publicKey = gen_publicKey(secretKey)
rawMessage = "my name is jing!"
signatures = signMessage(secretKey, message)

print(signatures)