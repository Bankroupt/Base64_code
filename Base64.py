#!/usr/bin/env python3
import sys
import base64
import argparse

def texto_a_base64(text: str) -> str:
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def de_base64_a_texto(b64: str) -> str:
    return base64.b64decode(b64.encode('utf-8')).decode('utf-8')

def main():
    p = argparse.ArgumentParser(description="Codificador de texto Base64 Desarrollado por Rafael Loor D.")
    p.add_argument('-c', '--codif', help='texto a Base64', metavar='text')
    p.add_argument('-d', '--decod', help='base64 a texto', metavar='base64')
    p.add_argument('-f', '--file', help='leer primer linea desde archivo', metavar='ruta')
    args = p.parse_args()

    if args.file:
        data = open(args.file, 'rb').read()
        try:
            decoded = base64.b64decode(data)
            print("El texto es: " + decoded.decode('utf-8'))
        except Exception:
            print("El cicrado queda asi: " + base64.b64encode(data).decode('utf-8'))
        return

    if args.codif:
        print(texto_a_base64(args.codif))
    elif args.decod:
        print(de_base64_a_texto(args.decod))
    else:
        raw = sys.stdin.read()
        raw = raw.strip()
        try:
            decoded = base64.b64decode(raw, validate=True)
            print(decoded.decode('utf-8'))
        except Exception:
            print(texto_a_base64(raw))

if __name__ == '__main__':
    main()
