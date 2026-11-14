---
id: TC-FA-DAMAGED-UI-114-dialog-mark-as-repaired-validasi-dan-submit
title: "Validasi dan Submit Dialog Mark as Repaired: Scan TAG belum dipindai, TAG bukan milik aset, After photo wajib, Repair note wajib dan maksimal 360 karakter, saving, toast, gagal 5xx, dan Unsaved Changes"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [FI-DMG-08, V-DMG-03, V-DMG-04, "§9.9#r3", "§9.9#r5", TS-DMG-05, "§4.2.4#p12", "§9.6#r5", "§9.4.4#r24", EB-FRM-4@repair-note, EB-FB-1@mark-as-repaired, EB-FB-2@cancel-mark-as-repaired, EB-FRM-1@mark-as-repaired, EB-FRM-2@mark-as-repaired, EB-ERR-1@mark-as-repaired]
smoke: []
dependsOn: []
trace:
  FI-DMG-08: [4]
  V-DMG-03: [8]
  V-DMG-04: [4]
  "§9.9#r3": [4, 8]
  "§9.9#r5": [12, 16, 19, 21, 23, 25]
  TS-DMG-05: [29, 35, 41, 47, 53, 58, 74]
  "§4.2.4#p12": [100, 108, 110]
  "§9.6#r5": [29, 30, 74]
  "§9.4.4#r24": [9]
  EB-FRM-4@repair-note: [19, 21]
  EB-FB-1@mark-as-repaired: [29, 74]
  EB-FB-2@cancel-mark-as-repaired: [5, 63, 95, 96]
  EB-FRM-1@mark-as-repaired: [67, 68, 70]
  EB-FRM-2@mark-as-repaired: [87, 88, 91, 92, 100, 101, 102, 104, 106]
  EB-ERR-1@mark-as-repaired: [74, 75, 76, 78, 82, 83, 84]
anchor: [62]
coverage:
  web: automated
---

# Validasi dan Submit Dialog Mark as Repaired: Scan TAG belum dipindai, TAG bukan milik aset, After photo wajib, Repair note wajib dan maksimal 360 karakter, saving, toast, gagal 5xx, dan Unsaved Changes

## Prerequisites
- Aktor: Aktor Damaged pada Group aset.
- Layar awal: Dialog Mark as Repaired belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Mark as Repaired (D-DMG-02)
- Data:
  - DU-114-1: record `Damaged` untuk aset `Laptop Dell Latitude 5420 - 6`, Asset ID `LPT-2026-0006`, Group `Head Office`, memiliki TAG RFID.
  - DU-114-2: record `Damaged` untuk aset `Toyota Avanza - 2`, Asset ID `VEH-2026-0002`, Group `Head Office`, tanpa TAG.
  - DU-114-3: setting After photo required bernilai `OFF`.
  - DU-114-4: setting After photo required bernilai `ON`.
  - DU-114-5: hasil pindai TAG milik aset DU-114-1, TAG `RFID-LPT-0006`.
  - DU-114-6: hasil pindai TAG bukan milik aset DU-114-1, TAG `RFID-CHR-0031`.
  - DU-114-7: Repair note dibiarkan kosong.
  - DU-114-8: Repair note berisi tiga spasi saja.
  - DU-114-9: Repair note sepanjang 360 karakter.
  - DU-114-10: Repair note sepanjang 361 karakter.
  - DU-114-11: Repair note sepanjang 360 karakter dengan spasi ganda di antara kata.
  - DU-114-12: Repair note sepanjang 360 karakter dengan huruf beraksen dan satu karakter non-BMP.
  - DU-114-13: berkas After photo JPEG `foto-sesudah.jpeg`, ukuran 512 KB.
  - DU-114-14: berkas After photo PNG `foto-sesudah.png`, ukuran 1 MB.
  - DU-114-15: berkas `catatan-servis.pdf`.
  - DU-114-16: berkas After photo JPEG `foto-sesudah-besar.jpeg`, ukuran 2 MB.
  - DU-114-17: After photo tidak dipilih saat setting OFF.
  - DU-114-18: After photo tidak dipilih saat setting ON.
  - DU-114-19: pengisian valid lengkap: Repair note `Layar diganti baru dan sudah diuji fungsi` dengan Scan TAG `RFID-LPT-0006` untuk aset ber-TAG.
- Kondisi:
  - K1: record DU-114-1 dengan setting DU-114-3; Scan TAG belum dipindai.
  - K2: record DU-114-1 dengan setting DU-114-3; hasil pindai adalah DU-114-6.
  - K3: record DU-114-1 dengan setting DU-114-3; hasil pindai adalah DU-114-5; respons simpan sukses.
  - K4: record DU-114-2 dengan setting DU-114-3; respons simpan sukses.
  - K5: record DU-114-2 dengan setting DU-114-4; respons simpan sukses.
  - K6: record DU-114-2 dengan setting DU-114-3; respons simpan lambat lalu sukses.
  - K7: record DU-114-2 dengan setting DU-114-3; respons simpan pertama gagal karena error server, respons berikutnya sukses.
  - K8: record DU-114-2 dengan setting DU-114-3; permintaan simpan melewati batas waktu.
  - K9: record DU-114-2 dengan setting DU-114-3; Repair note belum diisi.

## Test Steps

### Scan TAG wajib dipindai sebelum submit
1. Tampilkan Dialog Mark as Repaired dengan kondisi K1
2. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
3. Klik `[Mark as Repaired]`
4. Verifikasi caption `Scan TAG must not be empty` tampil pada bagian `Scan TAG*`
5. Verifikasi tidak ada toast yang tampil sesudah submit ditolak

### TAG yang dipindai bukan milik aset ditolak
6. Tampilkan Dialog Mark as Repaired dengan kondisi K2
7. Klik `[Scan TAG]`
8. Verifikasi pesan `This TAG doesn't belong to [Asset Name].` tampil dengan `[Asset Name]` berisi `Laptop Dell Latitude 5420 - 6`
9. Verifikasi tidak ada toast sukses yang tampil sesudah TAG ditolak

### Repair note kosong ditolak
10. Tampilkan Dialog Mark as Repaired dengan kondisi K4
11. Klik `[Mark as Repaired]` tanpa mengisi Repair note
12. Verifikasi caption `Repair note must not be empty` tampil di bawah isian `Repair note*`

### Repair note yang hanya berisi spasi diperlakukan kosong
13. Tampilkan Dialog Mark as Repaired dengan kondisi K4
14. Isi `Repair note*` dengan tiga spasi (`   `)
15. Klik `[Mark as Repaired]`
16. Verifikasi caption `Repair note must not be empty` tampil di bawah isian `Repair note*` yang hanya berisi spasi

### Batas 360 karakter pada Repair note
17. Tampilkan Dialog Mark as Repaired dengan kondisi K4
18. Isi `Repair note*` dengan `Panel layar diganti dengan unit baru dari pemasok resmi, konektor daya dibersihkan, lalu perangkat diuji menyala selama dua jam tanpa gangguan sebelum diserahkan kembali ke pemegang. Panel layar diganti dengan unit baru dari pemasok resmi, konektor daya dibersihkan, lalu perangkat diuji menyala selama dua jam tanpa gangguan sebelum diserahkan kembali ke pemeg` (361 karakter)
19. Verifikasi pesan `Max. 360 characters` tampil di bawah isian `Repair note*` tanpa menunggu submit
20. Ganti isi `Repair note*` dengan `Panel layar diganti dengan unit baru dari pemasok resmi, konektor daya dibersihkan, lalu perangkat diuji menyala selama dua jam tanpa gangguan sebelum diserahkan kembali ke pemegang. Panel layar diganti dengan unit baru dari pemasok resmi, konektor daya dibersihkan, lalu perangkat diuji menyala selama dua jam tanpa gangguan sebelum diserahkan kembali ke peme` (360 karakter)
21. Verifikasi pesan `Max. 360 characters` pada `Repair note*` tidak tampil lagi
22. Ganti isi `Repair note*` dengan `Panel  layar  diganti  dengan  unit  baru  dari  pemasok  resmi,  konektor  daya  dibersihkan,  lalu  perangkat  diuji  menyala  selama  dua  jam  tanpa  gangguan  sebelum  diserahkan  kembali  ke  pemegang.    Panel  layar  diganti  dengan  unit  baru  dari  pemasok  resmi,  konektor  daya  dibersihkan,  lalu  perangkat  diuji  menyala  selama  dua  jam  ta` (360 karakter)
23. Verifikasi pesan `Max. 360 characters` pada `Repair note*` tidak tampil untuk teks ber-spasi ganda
24. Ganti isi `Repair note*` dengan `Lénsa kaméra Cañon diganti oleh teknisi Ünit Perawatan Jakarta 𝒜 dan mekanisme fokus dikalibrasi ulang, kemudian perangkat diuji mengambil foto aset di gudang pusat tanpa gangguan selama satu jam penuh sebelum dikembalikan ke rak peminjaman karyawan lapangan, dengan catatan servis dilampirkan pada berkas perawatan. Lénsa kaméra Cañon diganti oleh teknisi Üni` (360 karakter)
25. Verifikasi pesan `Max. 360 characters` pada `Repair note*` tidak tampil untuk teks beraksen dan non-BMP

### Submit sukses aset tanpa TAG dan tanpa After photo
26. Tampilkan Dialog Mark as Repaired dengan kondisi K4
27. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
28. Klik `[Mark as Repaired]`
29. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil
30. Verifikasi dialog Mark as Repaired tertutup sesudah simpan sukses

### Submit sukses aset ber-TAG yang sudah terverifikasi
31. Tampilkan Dialog Mark as Repaired dengan kondisi K3
32. Klik `[Scan TAG]`
33. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
34. Klik `[Mark as Repaired]`
35. Verifikasi toast `Success, Laptop Dell Latitude 5420 - 6 has been marked as repaired.` tampil

### Submit sukses dengan After photo JPEG di bawah 1 MB
36. Tampilkan Dialog Mark as Repaired dengan kondisi K5
37. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
38. Pilih berkas foto `foto-sesudah.jpeg` pada pemilih foto `After photo`
39. Klik `Apply` pada dialog `Adjust photo`
40. Klik `[Mark as Repaired]`
41. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil sesudah After photo JPEG dipilih

### Submit sukses dengan After photo PNG tepat 1 MB
42. Tampilkan Dialog Mark as Repaired dengan kondisi K5
43. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
44. Pilih berkas foto `foto-sesudah.png` pada pemilih foto `After photo`
45. Klik `Apply` pada dialog `Adjust photo`
46. Klik `[Mark as Repaired]`
47. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil sesudah After photo PNG 1 MB dipilih

### Submit sukses dengan After photo JPEG di atas 1 MB
48. Tampilkan Dialog Mark as Repaired dengan kondisi K5
49. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
50. Pilih berkas foto `foto-sesudah-besar.jpeg` pada pemilih foto `After photo`
51. Klik `Apply` pada dialog `Adjust photo`
52. Klik `[Mark as Repaired]`
53. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil sesudah After photo JPEG 2 MB dipilih

### Berkas PDF disaring dan After photo opsional dibiarkan kosong
54. Tampilkan Dialog Mark as Repaired dengan kondisi K4
55. Pilih berkas `catatan-servis.pdf` pada pemilih foto `After photo`
56. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
57. Klik `[Mark as Repaired]`
58. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil tanpa After photo

### After photo wajib yang kosong memblok submit tanpa toast
59. Tampilkan Dialog Mark as Repaired dengan kondisi K5
60. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
61. Klik `[Mark as Repaired]`
62. Verifikasi dialog Mark as Repaired tetap terbuka sesudah submit tanpa After photo
63. Verifikasi tidak ada toast yang tampil sesudah submit tanpa After photo ditolak

### Saving state selama simpan berjalan
64. Tampilkan Dialog Mark as Repaired dengan kondisi K6
65. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
66. Klik `[Mark as Repaired]`
67. Verifikasi tombol `[Mark as Repaired]` berada dalam saving state dan tidak bisa diklik
68. Verifikasi tombol `✕`, tombol `[Cancel]`, isian `Repair note*`, dan pemilih foto `After photo` pada dialog Mark as Repaired tidak bisa dioperasikan selama simpan berjalan
69. Klik `[Mark as Repaired]` sekali lagi
70. Verifikasi hanya satu permintaan simpan Mark as Repaired yang terkirim

### Gagal 5xx lalu berhasil sesudah pulih
71. Tampilkan Dialog Mark as Repaired dengan kondisi K7
72. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
73. Klik `[Mark as Repaired]`
74. Verifikasi toast `Error, failed to mark asset as repaired.` tampil
75. Verifikasi dialog Mark as Repaired tetap terbuka sesudah simpan gagal dengan isian `Repair note*` berisi `Layar diganti baru dan sudah diuji fungsi`
76. Verifikasi tombol `[Mark as Repaired]` aktif lagi sesudah simpan gagal
77. Klik `[Mark as Repaired]`
78. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil pada pengiriman ulang

### Timeout pada simpan
79. Tampilkan Dialog Mark as Repaired dengan kondisi K8
80. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
81. Klik `[Mark as Repaired]`
82. Verifikasi toast `Connection problem. Please try again.` tampil untuk simpan Mark as Repaired yang melewati batas waktu
83. Verifikasi dialog Mark as Repaired tetap terbuka sesudah timeout dengan isian `Repair note*` berisi `Layar diganti baru dan sudah diuji fungsi`
84. Verifikasi tombol `[Mark as Repaired]` aktif lagi sesudah timeout

### Menutup form bersih dengan tombol tutup
85. Tampilkan Dialog Mark as Repaired dengan kondisi K9
86. Klik `✕` pada dialog
87. Verifikasi dialog Mark as Repaired tertutup
88. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil sesudah dialog Mark as Repaired ditutup

### Menutup form bersih dengan Esc
89. Tampilkan Dialog Mark as Repaired dengan kondisi K9
90. Tekan `Esc`
91. Verifikasi dialog Mark as Repaired tertutup oleh `Esc`
92. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil sesudah `Esc` pada form bersih

### Cancel pada form bersih tidak memunculkan toast
93. Tampilkan Dialog Mark as Repaired dengan kondisi K9
94. Klik `[Cancel]`
95. Verifikasi dialog Mark as Repaired tertutup oleh `[Cancel]`
96. Verifikasi tidak ada toast yang tampil sesudah `[Cancel]`

### Menutup form kotor memunculkan dialog Unsaved Changes
97. Tampilkan Dialog Mark as Repaired dengan kondisi K9
98. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
99. Klik `✕` pada dialog
100. Verifikasi dialog `Unsaved Changes` tampil di atas dialog Mark as Repaired
101. Verifikasi dialog `Unsaved Changes` pada Mark as Repaired memuat pesan `You have unsaved changes. Are you sure you want to leave?`
102. Verifikasi dialog `Unsaved Changes` pada Mark as Repaired memuat tombol `[Leave]` dan `[Cancel]`
103. Klik `[Cancel]` pada dialog `Unsaved Changes`
104. Verifikasi dialog `Unsaved Changes` tertutup dan dialog Mark as Repaired tetap terbuka dengan isian `Repair note*` berisi `Layar diganti baru dan sudah diuji fungsi`
105. Klik area backdrop di luar dialog Mark as Repaired
106. Verifikasi dialog Mark as Repaired tetap terbuka setelah klik backdrop dengan isian `Repair note*` berisi `Layar diganti baru dan sudah diuji fungsi`, dan dialog `Unsaved Changes` tidak tampil
107. Tekan `Esc`
108. Verifikasi dialog `Unsaved Changes` tampil sesudah `Esc` pada form Mark as Repaired yang terisi
109. Klik `[Leave]`
110. Verifikasi dialog Mark as Repaired tertutup sesudah `[Leave]`
