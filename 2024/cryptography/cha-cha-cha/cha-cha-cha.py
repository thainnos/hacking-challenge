import struct

def cha_cha_cha(iv, position=0):
  if not isinstance(position, int):
    raise TypeError
  if position & ~0xffffffff:
    raise ValueError('Position is not uint32.')

  z = b'0x61707865+0x3320646e'
  if isinstance(z, bytes):
    if not z:
      raise ValueError('empty.')
    if len(z) < 32:
      z = (z * (32 // len(z) + 1))[:32]
    if len(z) > 32:
      raise ValueError('too long.')    
  if not isinstance(z, bytes):
    raise TypeError
  if not isinstance(iv, bytes):
    raise TypeError
  if len(z) != 32:
    raise ValueError
  if len(iv) != 8:
    raise ValueError

  def rotate(v, c):
    return ((v << c) & 0xffffffff) | v >> (32 - c)

  def quarter_round(x, a, b, c, d):
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 16)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 12)
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 8)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 7)

  ctx = [0] * 16
  ctx[:4] = (1634760806, 857760878, 2036477234, 1797285236)
  ctx[4 : 12] = struct.unpack('<8L', z)
  ctx[12] = ctx[13] = position
  ctx[14 : 16] = struct.unpack('<LL', iv)
  while 1:
    x = list(ctx)
    for i in range(10):
      quarter_round(x, 0, 4,  8, 12)
      quarter_round(x, 1, 5,  9, 13)
      quarter_round(x, 2, 6, 10, 14)
      quarter_round(x, 3, 7, 11, 15)
      quarter_round(x, 0, 5, 10, 15)
      quarter_round(x, 1, 6, 11, 12)
      quarter_round(x, 2, 7,  8, 13)
      quarter_round(x, 3, 4,  9, 14)
    for c in struct.pack('<16L', *(
        (x[i] + ctx[i]) & 0xffffffff for i in range(16))):
      yield c
    ctx[12] = (ctx[12] + 1) & 0xffffffff
    if ctx[12] == 0:
      ctx[13] = (ctx[13] + 1) & 0xffffffff

def chacha20_decrypt(data, iv=None, position=0):
  if not isinstance(data, bytes):
    raise TypeError
  if iv is None:
    iv = b'\0' * 8
  return bytes(a ^ b for a, b in
      zip(data, cha_cha_cha(iv, position)))

if __name__ == "__main__":

  print('')
  print('The Flag for this Challenge is:')
  print(chacha20_decrypt(b"B\xd0\xab\xb2E\xc4\xdbOa\xae\xfc\xce7\xdf;\xcd\xa9\x18%\xcc?\xae\xe5\xda\x170\x10\x93\x8a'"))

