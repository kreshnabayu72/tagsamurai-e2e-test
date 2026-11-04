---
id: TC-FA-LIC-E2E-035-state-tenant-client-suspended-expired-menolak-force-logout-dan-edit
title: "State Tenant: Client Suspended Menolak Force Logout, Edit, dan Remove Allocation"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-447
  - TC-FA-LIC-448
  - TC-FA-LIC-449
coverage:
  web: automated
---

# State Tenant: Client Suspended Menolak Force Logout, Edit, dan Remove Allocation

## Prerequisites

- Mode: FE+BE.
- Dua client (Pre-setup #18), tiap TC dijalankan dua kali sesuai Precondition TC:

| Client | Akun Total Control | Kredensial | Fixture |
|---|---|---|---|
| Suspended | `totalControlSuspended_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_SUSPENDED_TC_PASSWORD` | `Fixture.fixedAssetLicense.clientSuspended` |
| Expired | `totalControlExpired_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_EXPIRED_TC_PASSWORD` | `Fixture.fixedAssetLicense.clientExpired` |

- Nama env `FA_SUSPENDED_TC_PASSWORD` dan `FA_EXPIRED_TC_PASSWORD` baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Login akun pertama (Suspended) di hook `before` spec ini sebelum status Client berubah; halaman dibuka hook `beforeEach` suite. Akun Expired diganti dengan langkah eksplisit (Logout, login); sesinya dibuka sebelum status client Expired berubah. Hook `after` memulihkan status kedua client dan mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup #18: tiap client memakai data kuota dan hierarki seperti Pre-setup #12 (Divisi IT beralokasi 100) dan sesi Budi Santoso aktif; status Client diubah menjadi Suspended atau Expired lewat fixture BE setelah sesi aktor dibuka; disediakan tim FE/BE.
- State global: status kedua client dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah). Suite serial (`parallel: false`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### Client Suspended

1. Ubah status Client menjadi Suspended lewat fixture BE (sesi aktor sudah dibuka sebelum status berubah)

### TC-FA-LIC-447: Entitas Suspended/Expired: Force Logout ditolak 403 dengan toast baku (Suspended)

2. Buka License > Concurrent User
3. Ketik Search `Budi Santoso`, tekan Enter
4. Klik `[Force Logout]` pada sesi Budi Santoso
5. Klik `[Confirm Logout]`
6. Verifikasi server menolak dengan `403 Forbidden`
7. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
8. Verifikasi tidak ada redirect
9. Verifikasi dialog `Force Logout User` (D-FALIC-01) ditutup dan tidak dibuka kembali (tanpa retry pada dialog yang sama)
10. Verifikasi daftar sesi dan `Online Users` di-refresh
11. Verifikasi tampilan baca tidak berubah
12. Verifikasi tidak ada perubahan data: sesi Budi Santoso tetap aktif lewat fixture BE
13. Klik `(←)` pada kotak Search

### TC-FA-LIC-448: Entitas Suspended/Expired: Edit Allocation ditolak 403 dengan toast baku (Suspended)

14. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
15. Klik `[Edit]` pada `Divisi IT`
16. Isi New Allocated Quota `120`
17. Klik `[Save]`
18. Verifikasi server menolak dengan `403 Forbidden`
19. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
20. Verifikasi tidak ada redirect
21. Verifikasi modal Edit Allocation ditutup dan input `120` dibuang tanpa retry pada modal yang sama
22. Klik `[Edit]` pada `Divisi IT` lagi
23. Verifikasi modal Edit Allocation menampilkan nilai tersimpan 100
24. Tutup modal Edit Allocation dengan `[×]`
25. Verifikasi Section 1 dan Section 2 Tab Allocation Quota di-refresh
26. Verifikasi tampilan baca tidak berubah
27. Verifikasi tidak ada perubahan data: Allocated Quota Divisi IT tetap 100 lewat fixture BE

### TC-FA-LIC-449: Entitas Suspended/Expired: Remove Allocation ditolak 403 dengan toast baku (Suspended)

28. Klik `[Edit]` pada `Divisi IT`
29. Klik `[Clear Field]`
30. Klik `[Save]`
31. Verifikasi server menolak dengan `403 Forbidden`
32. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
33. Verifikasi tidak ada redirect
34. Verifikasi modal Edit Allocation ditutup dan input kosong dibuang tanpa retry pada modal yang sama
35. Klik `[Edit]` pada `Divisi IT` lagi
36. Verifikasi modal Edit Allocation menampilkan nilai tersimpan 100
37. Tutup modal Edit Allocation dengan `[×]`
38. Verifikasi Section 1 dan Section 2 Tab Allocation Quota di-refresh
39. Verifikasi tampilan baca tidak berubah
40. Verifikasi tidak ada perubahan data: Allocated Quota Divisi IT tetap 100 lewat fixture BE

### Client Expired

41. Ganti akun: Logout
42. Login sebagai Total Control client Expired Pre-setup #18 (`Spectra.env.FA_EXPIRED_TC_PASSWORD`)
43. Ubah status Client menjadi Expired lewat fixture BE (sesi aktor sudah dibuka sebelum status berubah)

### TC-FA-LIC-447: Entitas Suspended/Expired: Force Logout ditolak 403 dengan toast baku (Expired)

44. Buka License > Concurrent User
45. Ketik Search `Budi Santoso`, tekan Enter
46. Klik `[Force Logout]` pada sesi Budi Santoso
47. Klik `[Confirm Logout]`
48. Verifikasi server menolak dengan `403 Forbidden`
49. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
50. Verifikasi tidak ada redirect
51. Verifikasi dialog `Force Logout User` (D-FALIC-01) ditutup dan tidak dibuka kembali (tanpa retry pada dialog yang sama)
52. Verifikasi daftar sesi dan `Online Users` di-refresh
53. Verifikasi tampilan baca tidak berubah
54. Verifikasi tidak ada perubahan data: sesi Budi Santoso tetap aktif lewat fixture BE
55. Klik `(←)` pada kotak Search

### TC-FA-LIC-448: Entitas Suspended/Expired: Edit Allocation ditolak 403 dengan toast baku (Expired)

56. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
57. Klik `[Edit]` pada `Divisi IT`
58. Isi New Allocated Quota `120`
59. Klik `[Save]`
60. Verifikasi server menolak dengan `403 Forbidden`
61. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
62. Verifikasi tidak ada redirect
63. Verifikasi modal Edit Allocation ditutup dan input `120` dibuang tanpa retry pada modal yang sama
64. Klik `[Edit]` pada `Divisi IT` lagi
65. Verifikasi modal Edit Allocation menampilkan nilai tersimpan 100
66. Tutup modal Edit Allocation dengan `[×]`
67. Verifikasi Section 1 dan Section 2 Tab Allocation Quota di-refresh
68. Verifikasi tampilan baca tidak berubah
69. Verifikasi tidak ada perubahan data: Allocated Quota Divisi IT tetap 100 lewat fixture BE

### TC-FA-LIC-449: Entitas Suspended/Expired: Remove Allocation ditolak 403 dengan toast baku (Expired)

70. Klik `[Edit]` pada `Divisi IT`
71. Klik `[Clear Field]`
72. Klik `[Save]`
73. Verifikasi server menolak dengan `403 Forbidden`
74. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
75. Verifikasi tidak ada redirect
76. Verifikasi modal Edit Allocation ditutup dan input kosong dibuang tanpa retry pada modal yang sama
77. Klik `[Edit]` pada `Divisi IT` lagi
78. Verifikasi modal Edit Allocation menampilkan nilai tersimpan 100
79. Tutup modal Edit Allocation dengan `[×]`
80. Verifikasi Section 1 dan Section 2 Tab Allocation Quota di-refresh
81. Verifikasi tampilan baca tidak berubah
82. Verifikasi tidak ada perubahan data: Allocated Quota Divisi IT tetap 100 lewat fixture BE

## Notes

- Spec kelas h (state tenant, bagian 3 prinsip 13); perubahan status Client oleh fixture BE hanya memicu kondisi yang diuji.
- Search `Budi Santoso` sebelum `[Force Logout]` dan `(←)` sesudah blok TC-FA-LIC-447 adalah langkah penghubung (tabel Active Sessions dapat memuat lebih dari satu halaman; 8b.13, R-16, S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): ubah status Client (langkah 1 dan 43), ganti akun (langkah 41 dan 42), "Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`", dan "Tutup modal Edit Allocation dengan `[×]`" setelah memverifikasi nilai tersimpan (modal tidak dirty).
- Spec di atas 35 langkah (82 langkah): alasan dipertahankan, TC-FA-LIC-447, 448, dan 449 menurut Precondition TC dijalankan dua kali (client Suspended lalu client Expired), tiap client memuat tiga blok aksi tulis yang berbagi state yang sama, dan penolakan tiap aksi berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok client Expired mengulang blok client Suspended dengan akun dan fixture berbeda (langkah 44 sampai 82 mengulang langkah 2 sampai 40).
- Temuan untuk QA:
  - TC-FA-LIC-447, 448, dan 449 menulis precondition login Total Control Pre-setup #1, sedangkan Pre-setup #18 adalah dua client lain dengan akun sendiri; spec mengikuti Pre-setup #18 (akun Suspended dan Expired).
  - Kontrak fixture pengubah status Client tidak tertulis di TC; disediakan tim FE/BE.
