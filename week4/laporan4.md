# Laporan Praktikum Week 4

## 4.2
Perbedaan utama:
- Perintah 1 & 2 pakai DNS server default (fe80::...), Perintah 3 pakai Google DNS (8.8.8.8).
- DNS default timeout 2 detik dan hanya mengembalikan IPv6 untuk www.mit.edu
- Google DNS cepat dan mengembalikan IPv4 + IPv6.

Dampak terhadap informasi:
- Informasi dari DNS default tidak lengkap (IPv4 hilang) → bisa salah sangka bahwa situs tidak punya IPv4
- DNS default lambat → menghambat akses internet
- Jika perangkat/app tidak support IPv6, koneksi ke www.mit.edu gagal padahal sebenarnya bisa pakai IPv4
![](../assest/image/week4.2.png)

## 4.4
1. Ya, pakai UDP.
2. Untuk port tujuan adalah 53 dan sumbernya adalah 58847.
![](../assest/image/week4.4.2.png)
3. IP tujuan: 192.168.0.1, DNS lokal: 192.168.0.1, Ya sama.
![](../assest/image/week4.4.3.png)
4. Type: A, tidak ada jawaban.
5. Ada 2
![](../assest/image/week4.4.5.png)
6. 
![](../assest/image/week4.4.6(1).png)
![](../assest/image/week4.4.6(2).png)
7. HOST tidak selalu mengirimkan permintaan DNS baru untuk mengakses suatu objek pada web, dikarenakan browser selalu menyimpan hasil dns pada cache.

## nslookup www.mit.edu
1. Port : 53
![](../assest/image/image1.png)
![](../assest/image/image2.png)
2. DNS lokal
![](../assest/image/image3.png)
3. Type: AAAA
![](../assest/image/image4.png)
4. Ada 4
- Sebuah nama alias yang mengarah ke www.mit.edu.edgekey.net
- Sebuah nama alias yang mengarah ke e9566.dscb.akamaiedge.net
- Sebuah alamat IPv6 (Type AAAA) dari server tujuan akhir tersebut, yaitu 2600:1417:6000:1be::255e
- Sebuah alamat IPv6 alternatif (Type AAAA) dari server tujuan akhir tersebut, yaitu 2600:1417:6000:1a3::255e
![](../assest/image/image5.png)
5. 
![](../assest/image/image6.png)

## nslookup -type=NS mit.edu
1. Sama 
![](../assest/image/image7.png)
2. Type: NS
![](../assest/image/image8.png)
3. 
![](../assest/image/image9.png)
4. 
![](../assest/image/image10.png)

## nslookup www.alit.or.kr bitsy.mit.edu
1. Tidak, itu mengarah ke IP mit.edu
![](../assest/image/image11.png)
![](../assest/image/image12.png)
2. Type : AAAA, Tidak mengandung jawaban
![](../assest/image/image13.png)
3. Tidak ada jawaban
4. 
![](../assest/image/image14.png)