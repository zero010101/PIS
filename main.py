from itertools import zip_longest, cycle


def xor_crypt_string(data, key):
    xored = ''
    for x, y in zip_longest(data, cycle(key)):
        if not x:
            break
        xored += chr(ord(x) ^ ord(y))
    return xored


if __name__ == '__main__':
    result = xor_crypt_string('resolve conflict', 'key')
    print(result)

