# Private key - public key generation
# Diffie-Hellman style.
# Maths : https://www.youtube.com/watch?v=Yjrfm_oRO0w
# Given private keys a,b
#     public key g
# Modulo size n


class KeyHandler(object):
    def __init__(self, priv_key, pub_key, n):
        self.privKey = priv_key
        self.pubKey = pub_key
        self.n = n

    def compute(self):
        return pow(self.pubKey, self.privKey, self.n)

    def verify_key(self, combined_key):
        return pow(combined_key, self.privKey, self.n)


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

#   Object Creation

    _keyHandler1 = KeyHandler(a, g, n)
    _keyHandler2 = KeyHandler(b, g, n)

#   Combine Public private key

    ag = _keyHandler1.compute()
    bg = _keyHandler2.compute()

    print('Private a and Public'), ag
    print('Private b and Public'), bg

#   Verify Combined Key

    agb = _keyHandler1.verify_key(bg)
    bga = _keyHandler2.verify_key(ag)

    print('Combined agb'), agb
    print('Combined bga'), bga


if __name__ == '__main__':
    main()
