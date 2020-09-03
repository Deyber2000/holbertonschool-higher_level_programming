#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    suma = 0
    top = len(sys.argv)
    for i in range(1, top):
        suma += int(sys.argv[i])
    print(suma)
