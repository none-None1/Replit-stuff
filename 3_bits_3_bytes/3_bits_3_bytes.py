# Modes:
#  "raw": Raw binary data
#  "hex": hex dump
#  "bin": binary number (0,1), spaces are allowed for readability
# Examples:
#  Quine: 41 14 88 (hex)
#  Truth Machine: 010 010 110 111 000 001 000 00n (bin)
#  where n is replaced with the input (0 or 1)
import sys

mode = 'raw'
try:
  mode = sys.argv[1]
except:
  pass
if mode not in 'raw hex bin':
  raise ValueError('Mode must be "raw" "hex" or "bin"')
code = input()
ip = 0
bits = []
if mode == 'raw':
  for i in code:
    bits += [(1 if int(j) else 0) for j in '{:08b}'.format(ord(i))]
if mode == 'hex':
  for i in [int(k, 16) for k in code.split()]:
    bits += [(1 if int(j) else 0) for j in '{:08b}'.format(i)]
if mode == 'bin':
  code = ''.join(filter(
      lambda x: x in '01',
      code))  # sometimes spaces are added for readability in binary mode
  for i in code:
    bits.append(1 if int(i) else 0)


def parse_command(code, ip):

  def getcmd(idx):
    return code[idx] * 4 + code[idx + 1] * 2 + code[idx + 2]

  c = getcmd(ip)
  if c in [0, 1]:
    return (c, )
  elif c != 6:
    return (c, getcmd(ip + 3))
  else:
    return (c, getcmd(ip + 3), getcmd(ip + 6))


def parse_byte(code, x):
  return code[x * 8] * 128 + code[x * 8 + 1] * 64 + code[
      x * 8 + 2] * 32 + code[x * 8 + 3] * 16 + code[x * 8 + 4] * 8 + code[
          x * 8 + 5] * 4 + code[x * 8 + 6] * 2 + code[x * 8 + 7]


def unparse_byte(code, x, inp):
  p, q = 128, x * 8
  while p:
    code[q] = (1 if inp & p else 0)
    p >>= 1
    q += 1


while 1:
  c = parse_command(bits, ip)
  if c[0] == 0:
    ip += 3
  elif c[0] == 1:
    break
  elif c[0] == 2:
    if c[1] < 3:
      sys.stdout.write(chr(parse_byte(bits, c[1])))
    ip += 6
  elif c[0] == 3:
    if c[1] < 3:
      unparse_byte(bits, c[1], ord(sys.stdin.read(1)))
    ip += 6
  elif c[0] == 4:
    val = bits[c[1] * 3] * 4 + bits[c[1] * 3 + 1] * 2 + bits[c[1] * 3 + 2]
    val = (val + 1) & 7
    bits[c[1] * 3], bits[c[1] * 3 + 1], bits[c[1] * 3 + 2] = (
        1 if val & 4 else 0), (1 if val & 2 else 0), (1 if val & 1 else 0)
    ip += 6
  elif c[0] == 5:
    ip = c[1] * 3
  elif c[0] == 6:
    if bits[c[1] * 3] * 4 + bits[c[1] * 3 + 1] * 2 + bits[c[1] * 3 + 2]:
      ip = c[2] * 3
    else:
      ip += 9
  else:
    val = bits[c[1] * 3] * 4 + bits[c[1] * 3 + 1] * 2 + bits[c[1] * 3 + 2]
    val = 7 - val
    bits[c[1] * 3], bits[c[1] * 3 + 1], bits[c[1] * 3 + 2] = (
        1 if val & 4 else 0), (1 if val & 2 else 0), (1 if val & 1 else 0)
    ip += 6
  ip %= 24
