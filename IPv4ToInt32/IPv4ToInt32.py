# https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/train/python
def ip_to_int32_v2(ip):
    ip_octets = ip.split('.')
    ip_binary_octets = [f'{int(x):08b}' for x in ip_octets]
    ip_binary = ''.join(ip_binary_octets)

    return int(ip_binary, 2)


# shorter version
def ip_to_int32(ip):
    return int(''.join(f'{int(x):08b}' for x in ip.split('.')), 2)


print(ip_to_int32("128.114.17.104") == 2154959208,
      "wrong integer for ip: 128.114.17.104")
print(ip_to_int32("0.0.0.0") == 0, "wrong integer for ip: 0.0.0.0")
print(ip_to_int32("128.32.10.1") == 2149583361,
      "wrong integer for ip: 128.32.10.1")
