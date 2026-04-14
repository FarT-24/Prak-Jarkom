# Laporan Praktikum Week 5

## 5.2
1. 4 (Source Port, Destination Port, Lenght, Checksum)
![](../assest/image/week5(1,%203).png)
2. Setiap field pada header UDP memiliki panjang 2 byte, sehingga total panjang header UDP adalah 8 byte.
3. Berdasarkan hasil analisis pada Wireshark, nilai Length menunjukkan total panjang paket UDP yang mencakup header dan payload. Misalnya, jika nilai Length adalah 58 byte, maka 8 byte merupakan header UDP dan sisanya merupakan data. Hal ini membuktikan bahwa field Length menyatakan total ukuran segmen UDP. ( 58 - 8 = 50)
![](../assest/image/week5(1,%203).png)
4. Field Length pada UDP memiliki ukuran 2 byte sehingga nilai maksimumnya adalah 65535 byte. Karena header UDP memiliki panjang tetap sebesar 8 byte, maka maksimum payload yang dapat dikirim adalah 65535 dikurangi 8, yaitu sebesar 65527 byte.
5. 2^16 - 1 = 65535. Nomor port terbesar adalah 65535.
6. Nomor protokol UDP adalah: Desimal: 17, Heksadesimal: 0x11
![](../assest/image/week5(6).png)
7. Pada paket balasan, nomor port sumber dan tujuan saling bertukar dibandingkan dengan paket permintaan. Hal ini menunjukkan bahwa balasan dikirim kembali ke port asal pengirim.
![](../assest/image/week5(7.1).png)
![](../assest/image/week5(7.2).png)