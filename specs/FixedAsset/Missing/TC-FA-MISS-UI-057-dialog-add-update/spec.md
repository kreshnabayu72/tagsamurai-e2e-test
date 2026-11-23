---
id: TC-FA-MISS-UI-057-dialog-add-update
title: "Dialog Add Update: header record dengan badge dan penanda, placeholder Update, validasi kosong dan 360, Unsaved, toast, dan respons gagal"
layer: ui-client
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: [§4.2.4#p13, §7.2#r8, §9.9#r8, §9.2#b65, §9.4.2#r32, §9.4.4#r29, §7.3#r9, §9.6#r5, §4.1#r6, EB-FRM-1@add-update, EB-FRM-2@add-update, EB-FRM-4@add-update, EB-FRM-7@add-update, EB-FB-1@add-update, EB-ERR-1@add-update]
smoke: []
dependsOn: []
trace:
  §4.2.4#p13: [3, 4, 5, 6, 7, 8, 9, 12, 13, 17]
  §7.2#r8: [2, 7]
  §9.9#r8: [8, 10, 17, 24, 27, 29, 31, 33, 35, 37]
  §9.2#b65: [17, 19, 20, 24, 27]
  §9.4.2#r32: [17, 19, 20, 27]
  §9.4.4#r29: [17, 19, 20, 27]
  §7.3#r9: [45, 49, 80]
  §9.6#r5: [41, 45, 49, 80]
  §4.1#r6: [4, 7]
  EB-FRM-1@add-update: [41, 42, 45]
  EB-FRM-2@add-update: [53, 56, 60, 62, 63, 65, 68]
  EB-FRM-4@add-update: [27, 29, 31, 33, 35]
  EB-FRM-7@add-update: [18, 70, 71, 72, 74, 76]
  EB-FB-1@add-update: [49, 50, 80]
  EB-ERR-1@add-update: [80, 81, 82, 83, 85, 86, 90, 91, 92, 93]
anchor: []
coverage:
  web: automated
---
# Dialog Add Update: header record dengan badge dan penanda, placeholder Update, validasi kosong dan 360, Unsaved, toast, dan respons gagal

## Prerequisites
- Aktor: Aktor Missing pada Group aset.
- Layar awal: halaman Missing, tab Active, dialog Missing Log record terbuka.
- Komponen: Dialog Add Update (D-MIS-05)
- Data:
  - DU-057-1: Record `Laptop Lenovo ThinkPad T14 - 4`, Asset ID `LPT-2026-0004`, status record `Missing`, penanda `Long missing`.
  - DU-057-2: Record `Toyota Innova - 2`, Asset ID `VEH-2026-0002`, status record `Missing`, tanpa penanda.
- Kondisi:
  - K1: dialog dibuka untuk record DU-057-1; simpan berhasil.
  - K2: dialog dibuka untuk record DU-057-2.
  - K3: dialog dibuka untuk record DU-057-1; simpan pertama gagal karena error server, simpan berikutnya berhasil.
  - K4: dialog dibuka untuk record DU-057-1; simpan gagal karena timeout.
  - K5: dialog dibuka untuk record DU-057-1; respons simpan belum diterima sampai langkah menyatakannya.


## Test Steps

### Tampilan awal dialog Add Update pada record dengan penanda Long missing
1. Tampilkan Dialog Add Update dengan kondisi K1
2. Verifikasi judul dialog `Add Update`
3. Verifikasi header menampilkan nama `Laptop Lenovo ThinkPad T14 - 4` dan Asset ID `LPT-2026-0004`
4. Verifikasi header menampilkan badge status record `Missing`
5. Verifikasi header menampilkan penanda `Long missing`
6. Verifikasi dialog hanya memuat satu isian, yaitu Update, tanpa lampiran
7. Verifikasi dialog memuat tombol `[Cancel]` dan `[Add Update]`
8. Verifikasi Update bertanda wajib
9. Verifikasi placeholder isian Update `Enter update`
10. Verifikasi isian Update kosong

### Record tanpa penanda Long missing
11. Tampilkan Dialog Add Update dengan kondisi K2
12. Verifikasi header menampilkan badge status record `Missing`
13. Verifikasi header tidak menampilkan penanda `Long missing`

### Update kosong ditolak saat Submit
14. Tampilkan Dialog Add Update dengan kondisi K1
15. Kosongkan isian Update
16. Klik `[Add Update]`
17. Verifikasi caption error `Update must not be empty` tampil di bawah isian Update
18. Verifikasi isian Update memiliki `aria-describedby` yang menunjuk ke caption error itu
19. Verifikasi dialog Add Update tetap terbuka
20. Verifikasi toast `Success, update has been added.` tidak tampil

### Update berisi spasi saja ditolak sebagai kosong
21. Tampilkan Dialog Add Update dengan kondisi K1
22. Isi Update `   `
23. Klik `[Add Update]`
24. Verifikasi caption error `Update must not be empty` tampil di bawah isian Update

### Batas panjang Update
25. Tampilkan Dialog Add Update dengan kondisi K1
26. Isi Update `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke raZ` (361 karakter)
27. Verifikasi caption error `Max. 360 characters` tampil langsung saat teks melebihi batas
28. Ganti isi Update dengan `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra` (360 karakter)
29. Verifikasi caption error `Max. 360 characters` tidak tampil
30. Ganti isi Update dengan `Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum.` (360 karakter)
31. Verifikasi caption error `Max. 360 characters` tidak tampil
32. Ganti isi Update dengan `Aset belum kembali ke rak  penyimpanan sejak inventarisasi akhir bulan  dan tidak ada catatan peminjaman  terbaru.  Aset belum kembali  ke rak penyimpanan sejak inventarisasi  akhir bulan dan tidak ada  catatan peminjaman terbaru.  Aset  belum kembali ke rak penyimpanan  sejak inventarisasi akhir bulan dan  tidak ada catatan peminjaman terbaru.   Aset belum.` (360 karakter)
33. Verifikasi caption error `Max. 360 characters` tidak tampil
34. Ganti isi Update dengan `  Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra  `, yaitu teks batas maksimum yang diapit dua spasi di awal dan di akhir
35. Verifikasi caption error `Max. 360 characters` tidak tampil
36. Ganti isi Update dengan `H`
37. Verifikasi isian Update berisi `H`

### Simpan lambat: tombol dan kontrol terkunci
38. Tampilkan Dialog Add Update dengan kondisi K5
39. Isi Update `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
40. Klik `[Add Update]`
41. Verifikasi `[Add Update]` tidak bisa diklik selama simpan berjalan
42. Verifikasi isian Update, `[Cancel]`, dan `✕` tidak bisa dipakai selama simpan berjalan
43. Klik `[Add Update]`
44. Respons simpan diterima
45. Verifikasi hanya satu toast `Success, update has been added.` tampil

### Simpan berhasil: toast Add Update
46. Tampilkan Dialog Add Update dengan kondisi K1
47. Isi Update `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
48. Klik `[Add Update]`
49. Verifikasi toast `Success, update has been added.` tampil
50. Verifikasi dialog Add Update tertutup

### Form bersih ditutup dengan tombol silang
51. Tampilkan Dialog Add Update dengan kondisi K1
52. Klik `✕` pada dialog
53. Verifikasi dialog Add Update tertutup tanpa dialog Unsaved Changes

### Form bersih ditutup dengan Esc
54. Tampilkan Dialog Add Update dengan kondisi K1
55. Tekan Esc
56. Verifikasi dialog Add Update tertutup tanpa dialog Unsaved Changes

### Form kotor ditutup memunculkan Unsaved Changes
57. Tampilkan Dialog Add Update dengan kondisi K1
58. Isi Update `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
59. Klik area backdrop di luar dialog
60. Verifikasi dialog Add Update tetap terbuka dengan isian Update `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
61. Klik `✕` pada dialog
62. Verifikasi dialog `Unsaved Changes` tampil di atas dialog Add Update dengan teks `You have unsaved changes. Are you sure you want to leave?`
63. Verifikasi dialog Unsaved Changes pada dialog Add Update memuat tombol `[Leave]` dan `[Cancel]`
64. Tekan Esc
65. Verifikasi dialog Unsaved Changes tertutup dan dialog Add Update tetap terbuka dengan isian Update `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
66. Tekan Esc
67. Klik `[Leave]`
68. Verifikasi dialog Add Update tertutup

### Aksesibilitas dialog
69. Tampilkan Dialog Add Update dengan kondisi K1
70. Verifikasi fokus berada di dalam dialog Add Update
71. Verifikasi isian Update memiliki `aria-required`
72. Verifikasi tombol `✕` pada dialog Add Update memiliki label aksesibel `Close dialog`
73. Tekan Tab sepuluh kali berturut-turut
74. Verifikasi fokus tetap berada di dalam dialog Add Update
75. Klik `✕` pada dialog
76. Verifikasi fokus kembali ke elemen pemicu dialog Add Update

### Simpan gagal karena error server: isian dipertahankan dan submit ulang berhasil
77. Tampilkan Dialog Add Update dengan kondisi K3
78. Isi Update `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
79. Klik `[Add Update]`
80. Verifikasi toast `Error, failed to add update.` tampil
81. Verifikasi dialog Add Update tetap terbuka
82. Verifikasi isian Update tetap berisi `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
83. Verifikasi `[Add Update]` aktif lagi
84. Klik `[Add Update]`
85. Verifikasi toast `Success, update has been added.` tampil
86. Verifikasi dialog Add Update tertutup

### Simpan gagal karena timeout
87. Tampilkan Dialog Add Update dengan kondisi K4
88. Isi Update `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
89. Klik `[Add Update]`
90. Verifikasi toast `Connection problem. Please try again.` tampil setelah simpan Add Update
91. Verifikasi dialog Add Update tetap terbuka
92. Verifikasi isian Update tetap berisi `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset`
93. Verifikasi `[Add Update]` aktif lagi

