from itertools import zip_longest, cycle


def xor_crypt_string(data, key):
    xored = ''
    for x, y in zip_longest, cycle:
        if not x:
	    break
	xored += chr(ord(x) ^ ord(y))
    return xored

if __name__ == '__main__':
    print(xor_crypt_string('hello', 'key'))
