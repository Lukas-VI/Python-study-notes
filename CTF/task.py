class LFSRStreamCipher:
    def __init__(self, key: int):
        if not (0 <= key < 2**16):
            raise ValueError("Key must be a 16-bit integer")
        self.state = key
        self.poly = 0b1010000000000101  # 反馈多项式: x^16 + x^14 + x^13 + x^11 + 1

    def lfsr_step(self) -> int:
        feedback = self.state & 1
        self.state >>= 1
        if feedback:
            self.state ^= self.poly
        return feedback

    def generate_keystream(self, length: int) -> bytes:
        keystream = bytearray()
        for _ in range(length):
            byte = 0
            for i in range(8):
                byte |= self.lfsr_step() << i
            keystream.append(byte)
        return bytes(keystream)

    def encrypt(self, plaintext: bytes) -> bytes:
        """使用密钥流加密"""
        keystream = self.generate_keystream(len(plaintext))
        return bytes(p ^ k for p, k in zip(plaintext, keystream))

    def decrypt(self, ciphertext: bytes) -> bytes:
        """使用密钥流解密（加密与解密是相同的）"""
        return self.encrypt(ciphertext)


key = 0b1101011010110101
cipher = LFSRStreamCipher(key)

flag = "bd8b802f4a05ed77abace36b6cf9adbe627d3632edff818c556120ad131b50dbedd0f4af4483"

ciphertext = cipher.encrypt(flag)



print("Ciphertext:", ciphertext.hex())



#bd8b802f4a05ed77abace36b6cf9adbe627d3632edff818c556120ad131b50dbedd0f4af4483

