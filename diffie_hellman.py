# Private key - public key generation
# Diffie hellman style.
# Maths : https://www.youtube.com/watch?v=Yjrfm_oRO0w
# Given private keys a,b
#     public key g
# a,b range 1-n
# n is the number one the circular verification


class KeyHandler(object):
    def __init__(self, privKey, pubKey, n):
        self.privKey = privKey
        self.pubKey = pubKey
        self.n = n


    def compute(self):
        return pow(self.pubKey, self.privKey, self.n)


    def verifyKey(self, combinedKey):
        return pow(combinedKey, self.privKey, self.n)

def main():
    n = 100000

    #   private keys
    a = 3426158395
    b = 3479502846

    #   public key
    g = 6748390294

    print('Public Key:'), g
    print('Private Key a:'), a
    print('Private Key b:'), b
    print('Verification Circle n:'), n

    #Object Creation

    _keyHandler1 = KeyHandler(a, g, n)
    _keyHandler2 = KeyHandler(b, g, n)

    #Combine Public private key

    ag = _keyHandler1.compute()
    bg = _keyHandler2.compute()

    print('Private a and Public'), ag
    print('Private b and Public'), bg

    #Verify Combined Key

    agb = _keyHandler1.verifyKey(bg)
    bga = _keyHandler2.verifyKey(ag)

    print('Combined agb'), agb
    print('Combined bga'), bga


if __name__ == '__main__':
    main()
