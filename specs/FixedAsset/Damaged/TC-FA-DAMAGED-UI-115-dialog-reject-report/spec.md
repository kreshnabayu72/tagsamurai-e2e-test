---
id: TC-FA-DAMAGED-UI-115-dialog-reject-report
title: "Dialog Reject Report: bullet nama aset, Reason wajib dan maksimal 360 karakter, tombol, saving, toast, gagal 5xx, Unsaved Changes, dan aksesibilitas"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [D-DMG-04, "§4.2.4#p4", "§4.4#r6", FLD-DMG-06, TS-DMG-04, "§4.2.4#p12", "§9.6#r3", EB-FRM-4@reason, EB-FB-1@reject, EB-FB-2@cancel-reject-report, EB-FRM-1@reject-report, EB-FRM-2@reject-report, EB-FRM-7@reject-report, EB-ERR-1@reject-report]
smoke: []
dependsOn: []
trace:
  D-DMG-04: [2, 3, 5, 6, 7]
  "§4.2.4#p4": [2, 3, 4, 5, 6, 7]
  "§4.4#r6": [2]
  FLD-DMG-06: [10, 14, 17, 19, 21, 23]
  TS-DMG-04: [27, 39]
  "§4.2.4#p12": [65, 73, 75]
  "§9.6#r3": [27, 28, 39]
  EB-FRM-4@reason: [17, 19]
  EB-FB-1@reject: [27, 39]
  EB-FB-2@cancel-reject-report: [60, 61]
  EB-FRM-1@reject-report: [32, 33, 35]
  EB-FRM-2@reject-report: [52, 53, 56, 57, 65, 66, 67, 69, 71]
  EB-FRM-7@reject-report: [77, 78, 79, 81, 83, 85]
  EB-ERR-1@reject-report: [39, 40, 41, 43, 47, 48, 49]
anchor: []
coverage:
  web: automated
---

# Dialog Reject Report: bullet nama aset, Reason wajib dan maksimal 360 karakter, tombol, saving, toast, gagal 5xx, Unsaved Changes, dan aksesibilitas

## Prerequisites
- Aktor: Aktor Damaged pada Group aset.
- Layar awal: Dialog Reject Report belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Reject Report (D-DMG-04)
- Data:
  - DU-115-1: laporan `Waiting for Confirmation` atas aset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`.
  - DU-115-2: Reason dibiarkan kosong.
  - DU-115-3: Reason berisi tiga spasi saja.
  - DU-115-4: Reason sepanjang 360 karakter.
  - DU-115-5: Reason sepanjang 361 karakter.
  - DU-115-6: Reason sepanjang 360 karakter dengan spasi ganda di antara kata.
  - DU-115-7: Reason sepanjang 360 karakter dengan huruf beraksen dan satu karakter non-BMP.
  - DU-115-8: pengisian valid lengkap: Reason `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`.
- Kondisi:
  - K1: laporan DU-115-1 ditampilkan di dialog; respons simpan sukses.
  - K2: laporan DU-115-1; respons simpan lambat lalu sukses.
  - K3: laporan DU-115-1; respons simpan pertama gagal karena error server, respons berikutnya sukses.
  - K4: laporan DU-115-1; permintaan simpan melewati batas waktu.
  - K5: laporan DU-115-1; Reason belum diisi.

## Test Steps

### Isi dialog Reject Report
1. Tampilkan Dialog Reject Report dengan kondisi K1
2. Verifikasi judul dialog `Reject Report`
3. Verifikasi nama aset `Laptop Dell Latitude 5420 - 4` tampil sebagai butir daftar
4. Verifikasi daftar aset hanya memuat satu butir
5. Verifikasi isian `Reason*` tampil dengan placeholder `Enter reason`
6. Verifikasi tombol `[Cancel]` tampil pada dialog Reject Report
7. Verifikasi tombol `[Reject]` tampil pada dialog Reject Report

### Reason kosong ditolak
8. Tampilkan Dialog Reject Report dengan kondisi K1
9. Klik `[Reject]` tanpa mengisi Reason
10. Verifikasi caption `Reason must not be empty` tampil di bawah isian `Reason*`

### Reason yang hanya berisi spasi diperlakukan kosong
11. Tampilkan Dialog Reject Report dengan kondisi K1
12. Isi `Reason*` dengan tiga spasi (`   `)
13. Klik `[Reject]`
14. Verifikasi caption `Reason must not be empty` tampil di bawah isian `Reason*` yang hanya berisi spasi

### Batas 360 karakter pada Reason
15. Tampilkan Dialog Reject Report dengan kondisi K1
16. Isi `Reason*` dengan `Laporan ditolak karena foto yang dilampirkan memperlihatkan perangkat lain dan bukan aset yang dimaksud, sehingga kerusakan pada aset ini tidak dapat diverifikasi oleh admin aset pada saat peninjauan laporan. Laporan ditolak karena foto yang dilampirkan memperlihatkan perangkat lain dan bukan aset yang dimaksud, sehingga kerusakan pada aset ini tidak dapat di` (361 karakter)
17. Verifikasi pesan `Max. 360 characters` tampil di bawah isian `Reason*` tanpa menunggu submit
18. Ganti isi `Reason*` dengan `Laporan ditolak karena foto yang dilampirkan memperlihatkan perangkat lain dan bukan aset yang dimaksud, sehingga kerusakan pada aset ini tidak dapat diverifikasi oleh admin aset pada saat peninjauan laporan. Laporan ditolak karena foto yang dilampirkan memperlihatkan perangkat lain dan bukan aset yang dimaksud, sehingga kerusakan pada aset ini tidak dapat d` (360 karakter)
19. Verifikasi pesan `Max. 360 characters` pada `Reason*` tidak tampil lagi
20. Ganti isi `Reason*` dengan `Laporan  ditolak  karena  foto  yang  dilampirkan  memperlihatkan  perangkat  lain  dan  bukan  aset  yang  dimaksud,  sehingga  kerusakan  pada  aset  ini  tidak  dapat  diverifikasi  oleh  admin  aset  pada  saat  peninjauan  laporan.    Laporan  ditolak  karena  foto  yang  dilampirkan  memperlihatkan  perangkat  lain  dan  bukan  aset  yang  dimaksud,  s` (360 karakter)
21. Verifikasi pesan `Max. 360 characters` pada `Reason*` tidak tampil untuk teks ber-spasi ganda
22. Ganti isi `Reason*` dengan `Laporan ditolak karena lensa kaméra Cañon pada foto bukan milik Ünit Gudang Pusat Jakarta 𝒜 dan nomor seri pada badan perangkat tidak cocok dengan data aset, sehingga laporan tidak dapat dilanjutkan sampai pelapor melampirkan foto yang benar dan keterangan kerusakan yang lebih jelas bagi admin aset di lokasi. Laporan ditolak karena lensa kaméra Cañon pada fo` (360 karakter)
23. Verifikasi pesan `Max. 360 characters` pada `Reason*` tidak tampil untuk teks beraksen dan non-BMP

### Submit sukses menampilkan toast
24. Tampilkan Dialog Reject Report dengan kondisi K1
25. Isi `Reason*` dengan `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
26. Klik `[Reject]`
27. Verifikasi toast `Success, report has been rejected.` tampil
28. Verifikasi dialog Reject Report tertutup sesudah simpan sukses

### Saving state selama simpan berjalan
29. Tampilkan Dialog Reject Report dengan kondisi K2
30. Isi `Reason*` dengan `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
31. Klik `[Reject]`
32. Verifikasi tombol `[Reject]` berada dalam saving state dan tidak bisa diklik
33. Verifikasi tombol `✕`, tombol `[Cancel]`, dan isian `Reason*` pada dialog Reject Report tidak bisa dioperasikan selama simpan berjalan
34. Klik `[Reject]` sekali lagi
35. Verifikasi hanya satu permintaan simpan Reject Report yang terkirim

### Gagal 5xx lalu berhasil sesudah pulih
36. Tampilkan Dialog Reject Report dengan kondisi K3
37. Isi `Reason*` dengan `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
38. Klik `[Reject]`
39. Verifikasi toast `Error, failed to reject report.` tampil
40. Verifikasi dialog Reject Report tetap terbuka sesudah simpan gagal dengan isian `Reason*` berisi `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
41. Verifikasi tombol `[Reject]` aktif lagi sesudah simpan gagal
42. Klik `[Reject]`
43. Verifikasi toast `Success, report has been rejected.` tampil pada pengiriman ulang

### Timeout pada simpan
44. Tampilkan Dialog Reject Report dengan kondisi K4
45. Isi `Reason*` dengan `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
46. Klik `[Reject]`
47. Verifikasi toast `Connection problem. Please try again.` tampil untuk simpan Reject Report yang melewati batas waktu
48. Verifikasi dialog Reject Report tetap terbuka sesudah timeout dengan isian `Reason*` berisi `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
49. Verifikasi tombol `[Reject]` aktif lagi sesudah timeout

### Menutup form bersih dengan tombol tutup
50. Tampilkan Dialog Reject Report dengan kondisi K5
51. Klik `✕` pada dialog
52. Verifikasi dialog Reject Report tertutup
53. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil sesudah dialog Reject Report ditutup

### Menutup form bersih dengan Esc
54. Tampilkan Dialog Reject Report dengan kondisi K5
55. Tekan `Esc`
56. Verifikasi dialog Reject Report tertutup oleh `Esc`
57. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil sesudah `Esc` pada Reject Report yang bersih

### Cancel pada form bersih tidak memunculkan toast
58. Tampilkan Dialog Reject Report dengan kondisi K5
59. Klik `[Cancel]`
60. Verifikasi dialog Reject Report tertutup oleh `[Cancel]`
61. Verifikasi tidak ada toast yang tampil sesudah `[Cancel]` pada Reject Report

### Menutup form kotor memunculkan dialog Unsaved Changes
62. Tampilkan Dialog Reject Report dengan kondisi K5
63. Isi `Reason*` dengan `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
64. Klik `✕` pada dialog
65. Verifikasi dialog `Unsaved Changes` tampil di atas dialog Reject Report
66. Verifikasi dialog `Unsaved Changes` pada Reject Report memuat pesan `You have unsaved changes. Are you sure you want to leave?`
67. Verifikasi dialog `Unsaved Changes` pada Reject Report memuat tombol `[Leave]` dan `[Cancel]`
68. Klik `[Cancel]` pada dialog `Unsaved Changes`
69. Verifikasi dialog `Unsaved Changes` tertutup dan dialog Reject Report tetap terbuka dengan isian `Reason*` berisi `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
70. Klik area backdrop di luar dialog Reject Report
71. Verifikasi dialog Reject Report tetap terbuka setelah klik backdrop dengan isian `Reason*` berisi `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`, dan dialog `Unsaved Changes` tidak tampil
72. Tekan `Esc`
73. Verifikasi dialog `Unsaved Changes` tampil sesudah `Esc` pada form Reject Report yang terisi
74. Klik `[Leave]`
75. Verifikasi dialog Reject Report tertutup sesudah `[Leave]`

### Aksesibilitas dialog
76. Tampilkan Dialog Reject Report dengan kondisi K5
77. Verifikasi fokus berada pada elemen di dalam dialog Reject Report
78. Verifikasi isian `Reason*` pada dialog Reject Report memiliki penanda wajib untuk teknologi bantu
79. Verifikasi tombol tutup dialog Reject Report memiliki nama aksesibel `Close dialog`
80. Tekan `Tab` sebanyak 8 kali
81. Verifikasi fokus tetap berada pada elemen di dalam dialog Reject Report
82. Klik `[Reject]`
83. Verifikasi pesan error di bawah isian `Reason*` terhubung sebagai deskripsi aksesibel isian itu
84. Klik `[Cancel]`
85. Verifikasi fokus kembali ke elemen yang membuka dialog Reject Report
