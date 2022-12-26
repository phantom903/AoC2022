snafu = {
  '=' : -2,
  '-' : -1,
  '0' : 0,
  '1' : 1,
  '2' : 2,
}

def fromSnafu(n):
  output = 0
  n = n[::-1]
  for i in range(len(n)):
    output += snafu[n[i]] * (5 ** i)
  return output

def toSnafu(n):
  if n == 0:
    return ''
  match n % 5 :
    case 0 | 1 | 2 :
      return toSnafu(n // 5) + str(n % 5)
    case 3:
      return toSnafu(1 + n // 5) + '='
    case 4:
      return toSnafu(1 + n // 5) + '-'

f = open('input/day25.txt').readlines()
print(toSnafu(sum([fromSnafu(line.strip()) for line in f])))