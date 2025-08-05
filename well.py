import random

angka_random = random.randint(1, 100)
ronde = 0
max_ronde = 5

print("TEBAK ANGKA")
print("SAYA MEMILIH SEBUAH ANGKA, DARI 1 - 100")
print("TUGAS ANDA ADALAH MENEBAKNYA", + str(max_ronde), + "kesempatan!")

while(ronde < max_ronde):
tebakan = int(input("tebakan kamu: ")
ronde += 1

     if (tebakan user < angka_random):
        print("alamak kecilnya")
     elif (tebakan user > angka_random):
         print("terlalu besar sir")
     else:
        print("TEBAKAN BENAR SIR")
        exit(0)
  print("SISA KESEMPATAN: " +str(max_ronde - ronde))
  
  print("yahh, kesempatanmu habis, tolol sih nebak angka doang gabisa")
  print("nih angka randomnya =>" + str(angka_random))
  
  #NOTE PROJECT INI TERINSPIRASI DARI BANG ARWILDO