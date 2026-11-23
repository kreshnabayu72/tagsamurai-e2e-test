---
id: TC-FA-DAMAGED-UI-114-dialog-mark-as-repaired-validasi-dan-submit
title: "Validasi dan Submit Dialog Mark as Repaired: Scan TAG belum dipindai, TAG bukan milik aset, After photo wajib, Repair note wajib dan maksimal 360 karakter, saving, toast, gagal 5xx, dan Unsaved Changes"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [FI-DMG-08, V-DMG-03, V-DMG-04, FLD-DMG-03, FLD-DMG-05, TS-DMG-05, "§4.2.4#p13", "§9.6#r5", "§9.4.4#r25", EB-FRM-4@repair-note, EB-FB-1@mark-as-repaired, EB-FB-2@cancel-mark-as-repaired, EB-FRM-1@mark-as-repaired, EB-FRM-2@mark-as-repaired, EB-ERR-1@mark-as-repaired, "§Aturan Logika Modul#r93", "§Aturan Logika Modul#r94", "§Aturan Logika Modul#r95", V-DMG-20, TS-DMG-12, EC-DMG-39, "§7.3#p1", "§4.2.4#p3", "§9.2#b18"]
smoke: []
dependsOn: []
trace:
  FI-DMG-08: [4]
  V-DMG-03: [8]
  V-DMG-04: [4]
  FLD-DMG-03: [4, 8]
  FLD-DMG-05: [12, 16, 19, 21, 23, 25]
  TS-DMG-05: [29, 35, 41, 47, 53, 58, 74]
  "§4.2.4#p13": [100, 108, 110]
  "§9.6#r5": [29, 30, 74, 117, 130]
  "§9.4.4#r25": [9]
  EB-FRM-4@repair-note: [19, 21]
  EB-FB-1@mark-as-repaired: [29, 74]
  EB-FB-2@cancel-mark-as-repaired: [5, 63, 95, 96]
  EB-FRM-1@mark-as-repaired: [67, 68, 70]
  EB-FRM-2@mark-as-repaired: [87, 88, 91, 92, 100, 101, 102, 104, 106]
  EB-ERR-1@mark-as-repaired: [74, 75, 76, 78, 82, 83, 84, 148, 149]
  "§Aturan Logika Modul#r93": [117, 124, 130, 146]
  "§Aturan Logika Modul#r94": [121, 139, 140]
  "§Aturan Logika Modul#r95": [121, 122, 123]
  V-DMG-20: [117, 118, 120]
  TS-DMG-12: [117, 130, 137, 146]
  EC-DMG-39: [117, 121, 130, 131, 147]
  "§7.3#p1": [130, 146]
  "§4.2.4#p3": [115, 117, 121]
  "§9.2#b18": [117]
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
  - DU-114-20: Storage penuh: usage ledger Storage client sama dengan kuota, `50.0 GB` dari `50.0 GB`.
  - DU-114-21: Storage melebihi kuota: usage ledger `51.2 GB`, kuota `50.0 GB`.
  - DU-114-22: Storage client tanpa baris ledger Storage: kuota `0.0 GB` dan usage `0.0 GB`.
- Kondisi:
  - K1: record DU-114-1 dengan setting DU-114-3; Scan TAG belum dipindai.
  - K2: record DU-114-1 dengan setting DU-114-3; hasil pindai adalah DU-114-6.
  - K3: record DU-114-1 dengan setting DU-114-3; hasil pindai adalah DU-114-5; respons simpan sukses.
  - K4: record DU-114-2 dengan setting DU-114-3; respons simpan sukses.
  - K5: record DU-114-2 dengan setting DU-114-4; pemilih foto `After photo` menerima berkas sumber di atas 1 MB dan memampatkan hasilnya otomatis menjadi tidak lebih dari 1 MB tanpa pesan error; respons simpan sukses.
  - K6: record DU-114-2 dengan setting DU-114-3; respons simpan lambat lalu sukses.
  - K7: record DU-114-2 dengan setting DU-114-3; respons simpan pertama gagal karena error server, respons berikutnya sukses.
  - K8: record DU-114-2 dengan setting DU-114-3; permintaan simpan melewati batas waktu.
  - K9: record DU-114-2 dengan setting DU-114-3; Repair note belum diisi.
  - K10: record DU-114-2 dengan setting DU-114-4; Storage penuh DU-114-20; respons simpan ditolak karena Storage penuh.
  - K11: record DU-114-2 dengan setting DU-114-3; Storage melebihi kuota DU-114-21; After photo opsional diisi; respons simpan ditolak karena Storage penuh.
  - K12: record DU-114-2 dengan setting DU-114-4; respons simpan pertama ditolak karena Storage penuh DU-114-20, respons berikutnya sukses (Storage dibebaskan).
  - K13: record DU-114-2 dengan setting DU-114-4; client tanpa baris ledger Storage DU-114-22; respons simpan ditolak karena Storage penuh.

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

### Storage penuh dengan After photo wajib: Submit ditolak dengan toast Error persisten
111. Tampilkan Dialog Mark as Repaired dengan kondisi K10
112. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
113. Pilih berkas foto `foto-sesudah.jpeg` pada pemilih foto `After photo*`
114. Klik `Apply` pada dialog `Adjust photo`
115. Verifikasi tombol `[Mark as Repaired]` tidak Disabled sebelum diklik
116. Klik `[Mark as Repaired]`
117. Verifikasi toast `Error, failed to mark asset as repaired. Storage is full (50.0 GB of 50.0 GB used).` tampil
118. Verifikasi tidak ada caption error di bawah pemilih foto `After photo*`
119. Waktu berlalu sampai 10 detik sejak toast tampil
120. Verifikasi toast `Error, failed to mark asset as repaired. Storage is full (50.0 GB of 50.0 GB used).` masih tampil
121. Verifikasi dialog Mark as Repaired tetap terbuka walau After photo wajib sudah terisi
122. Verifikasi isian `Repair note*` masih berisi `Layar diganti baru dan sudah diuji fungsi`
123. Verifikasi foto `foto-sesudah.jpeg` masih tampil pada pemilih foto `After photo*`
124. Verifikasi tombol `[Mark as Repaired]` aktif lagi

### Storage melebihi kuota dengan After photo opsional yang diisi
125. Tampilkan Dialog Mark as Repaired dengan kondisi K11
126. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
127. Pilih berkas foto `foto-sesudah.jpeg` pada pemilih foto `After photo`
128. Klik `Apply` pada dialog `Adjust photo`
129. Klik `[Mark as Repaired]`
130. Verifikasi toast `Error, failed to mark asset as repaired. Storage is full (51.2 GB of 50.0 GB used).` tampil
131. Verifikasi dialog Mark as Repaired tetap terbuka sesudah After photo opsional ditolak karena Storage penuh

### Submit ulang berhasil sesudah Storage dibebaskan
132. Tampilkan Dialog Mark as Repaired dengan kondisi K12
133. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
134. Pilih berkas foto `foto-sesudah.jpeg` pada pemilih foto `After photo*`
135. Klik `Apply` pada dialog `Adjust photo`
136. Klik `[Mark as Repaired]`
137. Verifikasi toast `Error, failed to mark asset as repaired. Storage is full (50.0 GB of 50.0 GB used).` tampil
138. Klik `[Mark as Repaired]`
139. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil sesudah Storage dibebaskan
140. Verifikasi dialog Mark as Repaired tertutup sesudah Storage dibebaskan

### Client tanpa baris ledger Storage dianggap berkuota 0: Submit ditolak
141. Tampilkan Dialog Mark as Repaired dengan kondisi K13
142. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
143. Pilih berkas foto `foto-sesudah.jpeg` pada pemilih foto `After photo*`
144. Klik `Apply` pada dialog `Adjust photo`
145. Klik `[Mark as Repaired]`
146. Verifikasi toast `Error, failed to mark asset as repaired. Storage is full (0.0 GB of 0.0 GB used).` tampil
147. Verifikasi dialog Mark as Repaired tetap terbuka walau After photo wajib sudah terisi
148. Verifikasi isian `Repair note*` masih berisi `Layar diganti baru dan sudah diuji fungsi`
149. Verifikasi tombol `[Mark as Repaired]` aktif lagi
