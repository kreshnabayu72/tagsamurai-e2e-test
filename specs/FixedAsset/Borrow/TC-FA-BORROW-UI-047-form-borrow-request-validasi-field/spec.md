---
id: TC-FA-BORROW-UI-047-form-borrow-request-validasi-field
title: "Validasi Borrower, Duration, Purpose, dan Note di form Borrow Request sebelum Submit"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FI-BRW-04", "FI-BRW-05", "FI-BRW-06", "FI-BRW-07", "FI-BRW-08", "FI-BRW-09", "FI-BRW-10", "FI-BRW-17", "FI-BRW-18", "FI-BRW-19", "FLD-BRW-02", "FLD-BRW-03", "FLD-BRW-04", "V-BRW-07", "V-BRW-16", "V-BRW-20", "§9.5#r10", "EB-FRM-4@form-borrow-request"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-04": [2, 3]
  "FI-BRW-05": 4
  "FI-BRW-06": 6
  "FI-BRW-07": 9
  "FI-BRW-08": 13
  "FI-BRW-09": 16
  "FI-BRW-10": [17, 19, 20]
  "FI-BRW-17": 24
  "FI-BRW-18": 25
  "FI-BRW-19": [36, 37, 38, 41]
  "FLD-BRW-02": [24, 29, 36, 77, 81]
  "FLD-BRW-03": [46, 50, 53, 57, 61, 66]
  "FLD-BRW-04": [70, 73]
  "V-BRW-07": 38
  "V-BRW-16": [24, 36, 77, 81]
  "V-BRW-20": [37, 46, 53]
  "§9.5#r10": [50, 53, 70, 73]
  "EB-FRM-4@form-borrow-request": [50, 53, 70, 73]
anchor: [8, 15, 28, 45, 49, 56, 60, 65, 69]
coverage:
  web: automated
---
# Validasi Borrower, Duration, Purpose, dan Note di form Borrow Request sebelum Submit

## Prerequisites
- Aktor: Aktor Borrow dalam cakupan Group `Head Office`.
- Layar awal: halaman Borrow Request.
- Komponen: Form Borrow Request
- Data:
  - DU-047-1: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Max Duration `3 days`, satuan Duration `days`, Duration dan Purpose kosong.
  - DU-047-2: Aset `Camera Sony A7 IV - 1`, Asset ID `CAM-2026-0001`, Group `Head Office`, Max Duration `4 hours`, satuan Duration `hours`, Duration dan Purpose kosong.
  - DU-047-3: Aset `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Group `Head Office`, Max Duration `8 hours`, satuan efektif `hours`; Draft menyimpan Duration `3` pada satuan lama `days`, dan Purpose `Rapat koordinasi vendor`.
  - DU-047-18: Karyawan `Budi Setiawan`, Position `Staff`, Division `Finance`, aktif, Borrower pada Draft DU-047-3.
  - DU-047-19: Isian Duration `0` untuk baris DU-047-1, di bawah batas bawah `1`.
  - DU-047-20: Isian Duration `3` untuk baris DU-047-1, tepat di Max Duration `3 days`.
- Kondisi:
  - K1: form Borrow Request baru, Borrower belum dipilih, berisi baris aset DU-047-1 dan DU-047-2 yang baru ditambahkan.
  - K2: Draft dibuka dengan Borrower DU-047-18 dan Purpose baris DU-047-3 sudah terisi, berisi baris aset DU-047-3 yang satuan efektifnya sudah berubah dari `days` menjadi `hours` sejak Draft disimpan.
  - K3: form Borrow Request baru tanpa baris aset dan tanpa Borrower.

## Test Steps

### Duration berupa input angka dengan satuan tetap per aset
1. Tampilkan Form Borrow Request dengan kondisi K1
2. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10` dan baris `Camera Sony A7 IV - 1` masing-masing berupa input angka tanpa pilihan cepat
3. Verifikasi input Duration baris `Laptop Dell Latitude 5420 - 10` memuat satuan `days` sesuai Duration unit aset itu
4. Verifikasi input Duration baris `Camera Sony A7 IV - 1` memuat satuan `hours` pada form yang sama dengan baris bersatuan `days`
5. Isi Duration baris `Laptop Dell Latitude 5420 - 10` dengan `2`
6. Verifikasi satuan `days` tetap tampil di samping input Duration baris `Laptop Dell Latitude 5420 - 10` yang berisi `2`, dan satuan `hours` di samping input baris `Camera Sony A7 IV - 1`

### Aset yang baru ditambahkan mulai dengan Duration dan Purpose kosong
7. Tampilkan Form Borrow Request dengan kondisi K1
8. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan baris `Camera Sony A7 IV - 1` tampil pada tabel aset
9. Verifikasi Duration dan Purpose baris `Laptop Dell Latitude 5420 - 10` dan baris `Camera Sony A7 IV - 1` kosong
10. Centang baris `Laptop Dell Latitude 5420 - 10`
11. Centang baris `Camera Sony A7 IV - 1`
12. Buka menu aksi pada bar bulk
13. Verifikasi aksi `Set Duration & Purpose` tersedia untuk menyamakan Duration dan Purpose baris tercentang

### Satuan efektif aset berubah mengosongkan Duration tersimpan
14. Tampilkan Form Borrow Request dengan kondisi K2
15. Verifikasi baris `Meeting Mic Set - 2` tampil pada tabel aset
16. Verifikasi Duration baris `Meeting Mic Set - 2` kosong dengan satuan `hours`
17. Verifikasi Duration baris `Meeting Mic Set - 2` tidak memuat `3` yang tersimpan pada satuan lama
18. Klik `[Submit]`
19. Verifikasi caption `Enter a duration of at least 1` tampil di bawah Duration baris `Meeting Mic Set - 2`
20. Verifikasi dialog `Submit Borrow` tidak tampil sehingga Submit diblokir sampai Duration terisi

### Duration yang melewati Max duration aset dijepit ke batas
21. Tampilkan Form Borrow Request dengan kondisi K1
22. Isi Duration baris `Laptop Dell Latitude 5420 - 10` dengan `5`
23. Pindahkan fokus keluar dari field Duration baris `Laptop Dell Latitude 5420 - 10`
24. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10` berisi `3` sesuai Max Duration `3 days` aset itu[^drift-1]
25. Verifikasi form tidak menampilkan banner ringkasan maupun aksi cepat

### Duration menolak karakter selain angka
26. Tampilkan Form Borrow Request dengan kondisi K1
27. Isi Duration baris `Laptop Dell Latitude 5420 - 10` dengan `abc`
28. Verifikasi satuan `days` tetap tampil di samping input Duration baris `Laptop Dell Latitude 5420 - 10`
29. Verifikasi field Duration baris `Laptop Dell Latitude 5420 - 10` tetap kosong

### Isian wajib yang kosong menampilkan error setelah Submit
30. Tampilkan Form Borrow Request dengan kondisi K1
31. Isi Duration baris `Laptop Dell Latitude 5420 - 10` dengan `2`
32. Kosongkan field Duration baris `Laptop Dell Latitude 5420 - 10`
33. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Rapat evaluasi bulanan`
34. Kosongkan field Purpose baris `Laptop Dell Latitude 5420 - 10`
35. Klik `[Submit]`
36. Verifikasi caption `Enter a duration of at least 1` tampil di bawah Duration baris `Laptop Dell Latitude 5420 - 10`
37. Verifikasi caption `Purpose must not be empty` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10`
38. Verifikasi caption `You must pick a borrower` tampil di bawah field Borrower

### Aset wajib ada saat Submit
39. Tampilkan Form Borrow Request dengan kondisi K3
40. Klik `[Submit]`
41. Verifikasi caption `You must pick an asset` tampil pada tabel aset

### Purpose yang hanya berisi spasi dianggap kosong
42. Tampilkan Form Borrow Request dengan kondisi K1
43. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `   ` (tiga spasi)
44. Klik `[Submit]`
45. Verifikasi caption `Enter a duration of at least 1` tampil di bawah Duration baris `Laptop Dell Latitude 5420 - 10`
46. Verifikasi caption `Purpose must not be empty` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` karena isian hanya spasi dianggap kosong

### Purpose tepat di batas 120 karakter diterima
47. Tampilkan Form Borrow Request dengan kondisi K1
48. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Peminjaman laptop untuk presentasi hasil audit aset kepada manajemen cabang selama kunjungan ke kantor perwakilan Banten` (120 karakter)
49. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 10` berisi teks yang diisi
50. Verifikasi caption `Max. 120 characters` tidak tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10`

### Purpose satu karakter di atas batas ditolak
51. Tampilkan Form Borrow Request dengan kondisi K1
52. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Peminjaman laptop untuk presentasi hasil audit aset kepada manajemen cabang selama kunjungan ke kantor perwakilan Bandung` (121 karakter)
53. Verifikasi caption `Max. 120 characters` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10`

### Spasi di awal dan akhir Purpose tidak ikut dihitung
54. Tampilkan Form Borrow Request dengan kondisi K1
55. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan teks 120 karakter yang diapit dua spasi di awal dan di akhir: `  Peminjaman laptop untuk presentasi hasil audit aset kepada manajemen cabang selama kunjungan ke kantor perwakilan Banten  `
56. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 10` berisi teks yang diisi
57. Verifikasi caption `Max. 120 characters` tidak tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` karena spasi di awal dan akhir tidak dihitung

### Spasi di tengah Purpose dihitung penuh
58. Tampilkan Form Borrow Request dengan kondisi K1
59. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Peminjaman  laptop  untuk presentasi hasil audit aset kepada manajemen cabang selama kunjungan ke kantor cabang Makassar` (120 karakter)
60. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 10` berisi teks yang diisi
61. Verifikasi caption `Max. 120 characters` tidak tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` karena spasi di tengah dihitung penuh sampai tepat 120 karakter

### Purpose yang diapit spasi tetap valid
62. Tampilkan Form Borrow Request dengan kondisi K1
63. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `  Pinjam untuk presentasi  `
64. Klik `[Submit]`
65. Verifikasi caption `Enter a duration of at least 1` tampil di bawah Duration baris `Laptop Dell Latitude 5420 - 10`
66. Verifikasi caption `Purpose must not be empty` tidak tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10`

### Note tepat di batas 360 karakter diterima
67. Tampilkan Form Borrow Request dengan kondisi K1
68. Isi Note dengan `Aset dipakai tim audit internal untuk verifikasi fisik di gudang pusat dan beberapa kantor cabang, harap disiapkan lengkap dengan charger dan tas pelindung. Mohon cek kondisi fisik sebelum diserahkan kepada peminjam dan didokumentasikan dengan foto singkat untuk arsip. Pengembalian dilakukan paling telat menurut batas durasi yang disepakati bersama oleh tim.` (360 karakter)
69. Verifikasi field Note berisi teks yang diisi
70. Verifikasi caption `Max. 360 characters` tidak tampil di bawah Note

### Note satu karakter di atas batas ditolak
71. Tampilkan Form Borrow Request dengan kondisi K1
72. Isi Note dengan `Aset dipakai tim audit internal untuk verifikasi fisik di gudang pusat dan beberapa kantor cabang, harap disiapkan lengkap dengan charger dan tas pelindung. Mohon cek kondisi fisik sebelum diserahkan kepada peminjam dan didokumentasikan dengan foto singkat untuk arsip. Pengembalian dilakukan paling telat menurut batas durasi yang disepakati bersama oleh tim.!` (361 karakter)
73. Verifikasi caption `Max. 360 characters` tampil di bawah Note

### Duration `0` dijepit ke batas bawah 1
74. Tampilkan Form Borrow Request dengan kondisi K1
75. Isi Duration baris `Laptop Dell Latitude 5420 - 10` dengan `0`
76. Pindahkan fokus keluar dari field Duration baris `Laptop Dell Latitude 5420 - 10`
77. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10` berisi `1` sesuai batas bawah Duration `1`[^drift-2]

### Duration tepat di Max duration aset diterima
78. Tampilkan Form Borrow Request dengan kondisi K1
79. Isi Duration baris `Laptop Dell Latitude 5420 - 10` dengan `3`
80. Pindahkan fokus keluar dari field Duration baris `Laptop Dell Latitude 5420 - 10`
81. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10` berisi `3` karena tepat di Max Duration `3 days` aset itu

[^drift-1]: Drift PRD vs kontrak komponen. PRD §6 V-BRW-16 dan §9.9 FLD-BRW-02: caption `Max. [Limit] [Unit] for [Category]` tampil langsung di bawah field Duration saat Duration melewati Max duration aset. Kontrak komponen `NumberInput#1`: min dan max adalah rentang, saat blur atau Enter nilai dijepit ke batas terdekat; `NumberInput#15`: tidak ada pesan rentang dan tidak ada invalid state untuk nilai di luar min/max. Diasersi: kontrak, karena field Duration dirender NumberInput (SB-7).

[^drift-2]: Drift PRD vs kontrak komponen. PRD §6 V-BRW-16 dan §9.9 FLD-BRW-02: Duration bilangan bulat `1` sampai Max duration aset, dengan caption `Enter a duration of at least 1` langsung di bawah field untuk nilai di bawah batas. Kontrak komponen `NumberInput#1`: min dan max adalah rentang, saat blur atau Enter nilai di bawah min dijepit ke min; `NumberInput#15`: tidak ada pesan rentang dan tidak ada invalid state untuk nilai di luar min/max. Diasersi: kontrak, karena field Duration dirender NumberInput (SB-7).
