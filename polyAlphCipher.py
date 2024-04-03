import random

class PolyAlphaCipher:
    def __init__(self):
        self.P2C = {}
        self.C2P = {}

    def print_poly(self, poly):
        for row in poly:
            print(''.join(row))
        print()

    def swap_col(self, alpha, idx1, idx2):
        for i in range(len(alpha)):
            alpha[i][idx1], alpha[i][idx2] = alpha[i][idx2], alpha[i][idx1]

    def swap_row(self, alpha, idx1, idx2):
        alpha[idx1], alpha[idx2] = alpha[idx2], alpha[idx1]

    def generate_poly(self, alphabet):
        size = len(alphabet)
        chars = list(alphabet)

        for i in chars:
            self.P2C[i] = {}
            for j in chars:
                self.P2C[i][j] = 'a'  # Placeholder, will be replaced

        alphabets = [list(alphabet[i:] + alphabet[:i]) for i in range(size)]

        for _ in range(size ** 2):
            idx1, idx2 = random.sample(range(size), 2)
            self.swap_row(alphabets, idx1, idx2)

        for _ in range(size ** 2):
            idx1, idx2 = random.sample(range(size), 2)
            self.swap_col(alphabets, idx1, idx2)

        for i, P in enumerate(chars):
            for j, K in enumerate(chars):
                self.P2C[P][K] = alphabets[i][j]

        for P in self.P2C:
            for K in self.P2C[P]:
                C = self.P2C[P][K]
                if C not in self.C2P:
                    self.C2P[C] = {}
                self.C2P[C][K] = P

    def encrypt(self, plain_text, key):
        # Placeholder for encryption logic
        P = list(plain_text)
        K = list(key)
        cipherText = ""
        for i, e in enumerate(P):
            if e in self.P2C and K[i % len(K)] in self.P2C[e]:
                cipherText += self.P2C[e][K[i % len(K)]] 
            else:
                cipherText += e
        return cipherText

    def decrypt(self, cipher_text, key):
        # Placeholder for decryption logic
        C = list(cipher_text)
        K = list(key)
        plainText = ""
        for i, e in enumerate(C):
            if e in self.C2P and K[i % len(K)] in self.C2P[e]:
                plainText += self.C2P[e][K[i % len(K)]] 
            else:
                plainText += e
        return plainText

# Usage example
pac = PolyAlphaCipher()
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \t"
pac.generate_poly(alphabet)

plain_text = "The Quick Brown Fox Jumps Over The Lazy Dog And Does Other Quick Things AS Well Just Because"
key = "CesarAdrianReynaSoftwareDeveloper"
encrypted_text = pac.encrypt(plain_text, key)
decrypted_text = pac.decrypt(encrypted_text, key)
print("Encrypted: ", encrypted_text)
print("Decrypted: ", decrypted_text)


## Refrence Material
## https://chat.openai.com/share/99e7cff7-08c4-4a40-a782-1bdf6a3ac077
