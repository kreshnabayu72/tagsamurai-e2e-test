---
id: TC-FA-MISS-UI-056-dialog-reject-report
title: "Dialog Reject Report: bullet aset, placeholder Reason, validasi kosong dan 360, Unsaved, toast, dan respons gagal"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§4.2.4#p11, §7.2#r7, §9.9#r7, §7.3#r7, §9.6#r3, §4.1#r6, EB-FRM-1@reject-report, EB-FRM-2@reject-report, EB-FRM-4@reject-report, EB-FRM-7@reject-report, EB-FB-1@reject, EB-ERR-1@reject]
smoke: []
dependsOn: []
trace:
  §4.2.4#p11: [3, 4, 5, 6, 11, 19]
  §7.2#r7: [2, 3, 4]
  §9.9#r7: [5, 7, 11, 16, 19, 21, 23, 25, 27, 29]
  §7.3#r7: [37, 41, 72]
  §9.6#r3: [41, 72]
  §4.1#r6: 4
  EB-FRM-1@reject-report: [33, 34, 37]
  EB-FRM-2@reject-report: [45, 48, 52, 54, 55, 57, 60]
  EB-FRM-4@reject-report: [19, 21, 23, 25, 27]
  EB-FRM-7@reject-report: [12, 62, 63, 64, 66, 68]
  EB-FB-1@reject: [41, 42, 72]
  EB-ERR-1@reject: [72, 73, 74, 75, 77, 78, 82, 83, 84, 85]
anchor: []
coverage:
  web: automated
---
# Dialog Reject Report: bullet aset, placeholder Reason, validasi kosong dan 360, Unsaved, toast, dan respons gagal

## Prerequisites
- Aktor: Aktor Missing pada Group aset.
- Layar awal: halaman Missing, tab Active, dialog Missing Log record terbuka.
- Komponen: Dialog Reject Report (D-MIS-04)
- Data:
  - DU-056-1: Aset `Hand Pallet Truck - 3`, Asset ID `HPT-2026-0003`, Group `Warehouse`, status record `Waiting for Confirmation`; bullet yang diharapkan `• Hand Pallet Truck`, dari Asset Name `Hand Pallet Truck`.
- Kondisi:
  - K1: dialog dibuka untuk aset DU-056-1; simpan berhasil.
  - K2: dialog dibuka untuk aset DU-056-1; simpan pertama gagal karena error server, simpan berikutnya berhasil.
  - K3: dialog dibuka untuk aset DU-056-1; simpan gagal karena timeout.
  - K4: dialog dibuka untuk aset DU-056-1; respons simpan belum diterima sampai langkah menyatakannya.


## Test Steps

### Tampilan awal dialog Reject Report
1. Tampilkan Dialog Reject Report dengan kondisi K1
2. Verifikasi judul dialog `Reject Report`
3. Verifikasi isi dialog memuat bullet `• Hand Pallet Truck` dan isian Reason
4. Verifikasi dialog memuat tombol `[Cancel]` dan `[Reject]`
5. Verifikasi Reason bertanda wajib
6. Verifikasi placeholder isian Reason `Enter reason`
7. Verifikasi isian Reason kosong

### Reason kosong ditolak saat Submit
8. Tampilkan Dialog Reject Report dengan kondisi K1
9. Kosongkan isian Reason
10. Klik `[Reject]`
11. Verifikasi caption error `Reason must not be empty` tampil di bawah isian Reason
12. Verifikasi isian Reason memiliki `aria-describedby` yang menunjuk ke caption error itu

### Reason berisi spasi saja ditolak sebagai kosong
13. Tampilkan Dialog Reject Report dengan kondisi K1
14. Isi Reason `   `
15. Klik `[Reject]`
16. Verifikasi caption error `Reason must not be empty` tampil di bawah isian Reason

### Batas panjang Reason
17. Tampilkan Dialog Reject Report dengan kondisi K1
18. Isi Reason `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke raZ` (361 karakter)
19. Verifikasi caption error `Max. 360 characters` tampil langsung saat teks melebihi batas
20. Ganti isi Reason dengan `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra` (360 karakter)
21. Verifikasi caption error `Max. 360 characters` tidak tampil
22. Ganti isi Reason dengan `Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum.` (360 karakter)
23. Verifikasi caption error `Max. 360 characters` tidak tampil
24. Ganti isi Reason dengan `Aset belum kembali ke rak  penyimpanan sejak inventarisasi akhir bulan  dan tidak ada catatan peminjaman  terbaru.  Aset belum kembali  ke rak penyimpanan sejak inventarisasi  akhir bulan dan tidak ada  catatan peminjaman terbaru.  Aset  belum kembali ke rak penyimpanan  sejak inventarisasi akhir bulan dan  tidak ada catatan peminjaman terbaru.   Aset belum.` (360 karakter)
25. Verifikasi caption error `Max. 360 characters` tidak tampil
26. Ganti isi Reason dengan `  Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra  `, yaitu teks batas maksimum yang diapit dua spasi di awal dan di akhir
27. Verifikasi caption error `Max. 360 characters` tidak tampil
28. Ganti isi Reason dengan `H`
29. Verifikasi isian Reason berisi `H`

### Simpan lambat: tombol dan kontrol terkunci
30. Tampilkan Dialog Reject Report dengan kondisi K4
31. Isi Reason `Aset sudah ditemukan di gudang oleh petugas lapangan`
32. Klik `[Reject]`
33. Verifikasi `[Reject]` tidak bisa diklik selama simpan berjalan
34. Verifikasi isian Reason, `[Cancel]`, dan `✕` tidak bisa dipakai selama simpan berjalan
35. Klik `[Reject]`
36. Respons simpan diterima
37. Verifikasi hanya satu toast `Success, report has been rejected.` tampil

### Simpan berhasil: toast reject
38. Tampilkan Dialog Reject Report dengan kondisi K1
39. Isi Reason `Aset sudah ditemukan di gudang oleh petugas lapangan`
40. Klik `[Reject]`
41. Verifikasi toast `Success, report has been rejected.` tampil
42. Verifikasi dialog Reject Report tertutup

### Form bersih ditutup dengan tombol silang
43. Tampilkan Dialog Reject Report dengan kondisi K1
44. Klik `✕` pada dialog
45. Verifikasi dialog Reject Report tertutup tanpa dialog Unsaved Changes

### Form bersih ditutup dengan Esc
46. Tampilkan Dialog Reject Report dengan kondisi K1
47. Tekan Esc
48. Verifikasi dialog Reject Report tertutup tanpa dialog Unsaved Changes

### Form kotor ditutup memunculkan Unsaved Changes
49. Tampilkan Dialog Reject Report dengan kondisi K1
50. Isi Reason `Aset sudah ditemukan di gudang oleh petugas lapangan`
51. Klik area backdrop di luar dialog
52. Verifikasi dialog Reject Report tetap terbuka dengan isian Reason `Aset sudah ditemukan di gudang oleh petugas lapangan`
53. Klik `✕` pada dialog
54. Verifikasi dialog `Unsaved Changes` tampil di atas dialog Reject Report dengan teks `You have unsaved changes. Are you sure you want to leave?`
55. Verifikasi dialog Unsaved Changes pada dialog Reject Report memuat tombol `[Leave]` dan `[Cancel]`
56. Tekan Esc
57. Verifikasi dialog Unsaved Changes tertutup dan dialog Reject Report tetap terbuka dengan isian Reason `Aset sudah ditemukan di gudang oleh petugas lapangan`
58. Tekan Esc
59. Klik `[Leave]`
60. Verifikasi dialog Reject Report tertutup

### Aksesibilitas dialog
61. Tampilkan Dialog Reject Report dengan kondisi K1
62. Verifikasi fokus berada di dalam dialog Reject Report
63. Verifikasi isian Reason memiliki `aria-required`
64. Verifikasi tombol `✕` pada dialog Reject Report memiliki label aksesibel `Close dialog`
65. Tekan Tab sepuluh kali berturut-turut
66. Verifikasi fokus tetap berada di dalam dialog Reject Report
67. Klik `✕` pada dialog
68. Verifikasi fokus kembali ke elemen pemicu dialog Reject Report

### Simpan gagal karena error server: isian dipertahankan dan submit ulang berhasil
69. Tampilkan Dialog Reject Report dengan kondisi K2
70. Isi Reason `Aset sudah ditemukan di gudang oleh petugas lapangan`
71. Klik `[Reject]`
72. Verifikasi toast `Error, failed to reject report.` tampil
73. Verifikasi dialog Reject Report tetap terbuka
74. Verifikasi isian Reason tetap berisi `Aset sudah ditemukan di gudang oleh petugas lapangan`
75. Verifikasi `[Reject]` aktif lagi
76. Klik `[Reject]`
77. Verifikasi toast `Success, report has been rejected.` tampil
78. Verifikasi dialog Reject Report tertutup

### Simpan gagal karena timeout
79. Tampilkan Dialog Reject Report dengan kondisi K3
80. Isi Reason `Aset sudah ditemukan di gudang oleh petugas lapangan`
81. Klik `[Reject]`
82. Verifikasi toast `Connection problem. Please try again.` tampil setelah simpan Reject Report
83. Verifikasi dialog Reject Report tetap terbuka
84. Verifikasi isian Reason tetap berisi `Aset sudah ditemukan di gudang oleh petugas lapangan`
85. Verifikasi `[Reject]` aktif lagi

