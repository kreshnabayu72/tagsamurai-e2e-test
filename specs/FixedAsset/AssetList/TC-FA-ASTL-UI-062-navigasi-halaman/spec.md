---
id: TC-FA-ASTL-UI-062-navigasi-halaman
title: "Paginasi, breadcrumb, dan guided tooltip halaman Assets"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.1#p2", "§4.2.1#p3", "§4.2.1#p4", "§4.4#b1", "§4.7Step1", "§4.7Step2", "§4.7Step3", "§5#r2", "EB-TBL-7@tabel-all-assets", "EB-TBL-10", "EB-TBL-11"]
smoke: []
dependsOn: []
trace:
  "§4.2.1#p2": [2, 3, 5]
  "§4.2.1#p3": 2
  "§4.2.1#p4": [8, 9]
  "§4.4#b1": [40, 41, 42]
  "§4.7Step1": 44
  "§4.7Step2": 47
  "§4.7Step3": 52
  "§5#r2": [11, 13, 16, 31, 33, 38]
  "EB-TBL-7@tabel-all-assets": [18, 22, 24, 26, 28]
  "EB-TBL-10": [44, 45, 47, 49, 52, 53, 55, 58, 60, 62, 64, 66]
  "EB-TBL-11": [2, 5, 7]
anchor: [57]
coverage:
  web: automated
---
# Paginasi, breadcrumb, dan guided tooltip halaman Assets

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Halaman Assets
- Data:
  - DU-062-1: Tiga puluh lima aset: Name `Aset Paginasi 1` sampai `Aset Paginasi 35`, Status `Available`.
- Kondisi:
  - K1: tab `Assets` memuat DU-062-1 dengan ukuran halaman bawaan, dan Guided Tooltip halaman ini sudah pernah diselesaikan.
  - K2: seperti K1, tetapi ini kunjungan pertama dan Guided Tooltip belum pernah diselesaikan maupun dilewati.
  - K3: seperti K2, tetapi walkthrough sebelumnya ditutup tanpa diselesaikan sehingga flag belum disetel.
  - K4: state daftar yang tersimpan berisi Search `Aset Paginasi`, sort kolom Name naik, dan halaman 2, dengan DU-062-1 sebagai data.

## Test Steps

### Breadcrumb dan pembungkus area
1. Tampilkan Halaman Assets dengan kondisi K1
2. Verifikasi breadcrumb menampilkan `Assets > All Assets`
3. Verifikasi tidak ada heading halaman terpisah selain breadcrumb
4. Klik segmen `Assets` pada breadcrumb
5. Verifikasi halaman tetap pada tab `Assets` tanpa berpindah
6. Klik segmen `All Assets` pada breadcrumb
7. Verifikasi halaman tetap pada tab `Assets` tanpa berpindah
8. Verifikasi baris kartu status, toolbar, dan tabel tampil bersama pada area tabel
9. Verifikasi Sidebar Group tampil di sisi kanan area tabel

### Ukuran halaman bawaan dan pilihannya
10. Tampilkan Halaman Assets dengan kondisi K1
11. Verifikasi ukuran halaman bernilai `10` dan tabel memuat `Aset Paginasi 1`
12. Buka pilihan ukuran halaman
13. Verifikasi pilihan ukuran halaman `10`, `25`, `50`, dan `100` tampil

### Ganti ukuran halaman dan sort, serta nomor halaman tidak valid
14. Tampilkan Halaman Assets dengan kondisi K1
15. Klik halaman 3
16. Verifikasi halaman 3 aktif
17. Pilih ukuran halaman `25`
18. Verifikasi halaman 1 aktif
19. Pilih ukuran halaman `10`
20. Klik halaman 2
21. Klik header kolom Name
22. Verifikasi halaman 2 tetap aktif
23. Isi nomor halaman `abc`
24. Verifikasi halaman 2 tetap aktif
25. Isi nomor halaman `99`
26. Verifikasi halaman 4 aktif sebagai halaman terakhir
27. Isi nomor halaman `0`
28. Verifikasi halaman 1 aktif

### Search dan Apply mengembalikan ke halaman 1
29. Tampilkan Halaman Assets dengan kondisi K1
30. Klik halaman 3
31. Verifikasi halaman 3 aktif
32. Ketik Search `Aset Paginasi`, tekan Enter
33. Verifikasi halaman 1 aktif
34. Klik halaman 3
35. Klik ikon Filter
36. Pilih `Available` pada field Status
37. Klik `[Apply]`
38. Verifikasi halaman 1 aktif

### State daftar dipulihkan saat halaman dibuka kembali
39. Tampilkan Halaman Assets dengan kondisi K4
40. Verifikasi kotak Search terisi `Aset Paginasi`
41. Verifikasi indikator sort naik `↑` aktif pada kolom Name
42. Verifikasi halaman 2 aktif

### Guided Tooltip kunjungan pertama
43. Tampilkan Halaman Assets dengan kondisi K2
44. Verifikasi Guided Tooltip tampil otomatis pada langkah 1 dengan judul `Status cards` dan teks `Click a card to filter assets by status.`, dan baris kartu status disorot
45. Verifikasi tombol `[Skip]` dan `[Next]` tampil dan tombol `[Back]` tidak tampil
46. Klik `[Next]`
47. Verifikasi langkah 2 tampil dengan judul `Filter` dan teks `Narrow down the list to find specific assets.`, dan tombol Filter disorot
48. Klik `[Back]`
49. Verifikasi langkah 1 tampil dengan judul `Status cards`
50. Klik `[Next]`
51. Klik `[Next]`
52. Verifikasi langkah 3 tampil dengan judul `Setup Column` dan teks `Choose which columns to show and drag to reorder them.`, dan menu kolom (`⋯` pada header) disorot
53. Verifikasi tombol `[Done]` menggantikan `[Next]`
54. Klik `[Done]`
55. Verifikasi Guided Tooltip tertutup

### Guided Tooltip tidak muncul lagi dan dapat diputar ulang
56. Tampilkan Halaman Assets dengan kondisi K1
57. Verifikasi tabel memuat `Aset Paginasi 1`
58. Verifikasi Guided Tooltip tidak tampil otomatis
59. Klik tombol `[?]` di sebelah kanan breadcrumb
60. Verifikasi langkah 1 tampil dengan judul `Status cards`
61. Klik `[Skip]`
62. Verifikasi Guided Tooltip tertutup

### Guided Tooltip yang ditutup tanpa selesai muncul lagi
63. Tampilkan Halaman Assets dengan kondisi K3
64. Verifikasi Guided Tooltip tampil otomatis pada langkah 1 dengan judul `Status cards`
65. Tutup walkthrough tanpa menekan `[Done]` maupun `[Skip]`
66. Verifikasi tidak ada penanda selesai atau dilewati yang disetel, dan Guided Tooltip tampil lagi otomatis pada langkah 1 saat Halaman Assets dibuka kembali dengan kondisi K3
