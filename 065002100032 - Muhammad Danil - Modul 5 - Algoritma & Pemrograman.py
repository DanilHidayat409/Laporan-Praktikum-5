# -*- coding: utf-8 -*-
"""
@Hari/Tanggal : 20212410
@Nama : Muhammad Danil Hidayat
@NIM : 065002100032
@Judul : Laporan Praktikum 5 
"""

print("Selamat Datang")
print("umur 1 : gratis ")
print("umur 12 kebawah : $ 14.00")
print("umur 13 sampai 34 : $ 18.00")
print("umur 35 sampai 66 : $ 23.00")

ulang = 0
nomor = 0
jumlah= 0


while ulang == 0:
    nomor += 1
    x = int(input("masukkan umur: "))
    
    if x == int("-1"): 
        break
    
    else: 
        
        if x == 1: 
            jumlah += 0
            print("ini gratis")
            print("jumlah",jumlah)
            
        elif x <= 12:
            jumlah += 14.00
            print("$ 14.00")
            print("jumlah",jumlah)
    
            
        elif(x >= 13 and x <= 34) :
            jumlah += 18.00 
            print("$ 18.00")
            print("jumlah: ",jumlah)
            
        elif(x >= 35 and x <= 66) :
            jumlah += 23.00
            print("$ 23.00")
            print("jumlah: ",jumlah)
        
        else :
            print("saya tidak mengerti")
            jumlah = 0 
        
uang = int(input("Masukkan uang nya: "))
        
if uang == jumlah:
            print("uang kamu pas")
   
elif uang < jumlah:
            print("uang kamu kurang")
    
elif uang > jumlah:
            uang -= jumlah
            print("kembalian nya",uang)