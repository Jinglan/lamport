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
    sk0 = []
    sk1 = []
    for i in range(256): sk0.append(hex(secrets.randbits(256)))
    for i in range(256): sk1.append(hex(secrets.randbits(256)))
    return sk0, sk1

# Generate a public key by hashing the secret keys
# Return two hashed arrays that constitute pubkey pairs
def gen_publicKey(secretKey):
    sk0, sk1 = secretKey
    pk0 = list(map(lambda i: hash(i), sk0))
    pk1 = list(map(lambda i: hash(i), sk1))
    return pk0, pk1

# Format a message correctly by turning it into 256 bits
def messageBits(rawMessage):
    return str(bitstring.BitArray(hash(rawMessage)).bin)

# Return a list of half of the secret keys based on the
# value at each index of the message
def signMessage(secretKey, message):
    # pull the two lists of secret keys out so we can 
    # iterate through them more easily
    sk0, sk1 = secretKey
    # create an empty list to store our signatures
    sigList = []
    # run through each digit of the message
    for i in range(256):
        if message[i] == '0':
            # if it's a 0 bit, use a secret key from sk0
            sigList.append(sk0[i])
        elif message[i]== '1':
            # if it's a 1 bit, use a secret key from sk1
            sigList.append(sk1[i])
    return sigList


# Validate the authenticity of the signatures
def validate(publicKey, signatures, message):
    # Pull two separate lists out of the publicKey parameter
    pk0, pk1 = publicKey
    # Iterate through each signature in the list of signatures
    for i, sig in enumerate(signatures):
        # If the bit at that index of the message is 0
        if message[i] == '0':
            # Check if the signature matches the public key
            # at that index from the list pk0
            if pk0[i] != hash(sig):
                return "This is invalid"
        # If the bit at that index of the message is 1
        elif message[i] == '1':
            # Check if the signature matche the public key
            # at that index from the list pk1
            if pk1[i] != hash(sig):
                return "This is invalid"
    return "This is valid"



# Check it out
secretKey = gen_secretKey()
publicKey = gen_publicKey(secretKey)
message = messageBits("my name is jing!")
signatures = signMessage(secretKey, message)
print (validate(publicKey, signatures, message))
# print(signatures)
