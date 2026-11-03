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
3. Klik `[Force Logout]` pada sesi Budi Santoso
4. Klik `[Confirm Logout]`
5. Verifikasi server menolak dengan `403 Forbidden`
6. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
7. Verifikasi tidak ada redirect
8. Verifikasi dialog `Force Logout User` (D-FALIC-01) ditutup dan tidak dibuka kembali (tanpa retry pada dialog yang sama)
9. Verifikasi daftar sesi dan `Online Users` di-refresh
10. Verifikasi tampilan baca tidak berubah
11. Verifikasi tidak ada perubahan data: sesi Budi Santoso tetap aktif lewat fixture BE

### TC-FA-LIC-448: Entitas Suspended/Expired: Edit Allocation ditolak 403 dengan toast baku (Suspended)

12. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
13. Klik `[Edit]` pada `Divisi IT`
14. Isi New Allocated Quota `120`
15. Klik `[Save]`
16. Verifikasi server menolak dengan `403 Forbidden`
17. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
18. Verifikasi tidak ada redirect
19. Verifikasi modal Edit Allocation ditutup dan input `120` dibuang tanpa retry pada modal yang sama
20. Klik `[Edit]` pada `Divisi IT` lagi
21. Verifikasi modal Edit Allocation menampilkan nilai tersimpan 100
22. Tutup modal Edit Allocation dengan `[×]`
23. Verifikasi Section 1 dan Section 2 Tab Allocation Quota di-refresh
24. Verifikasi tampilan baca tidak berubah
25. Verifikasi tidak ada perubahan data: Allocated Quota Divisi IT tetap 100 lewat fixture BE

### TC-FA-LIC-449: Entitas Suspended/Expired: Remove Allocation ditolak 403 dengan toast baku (Suspended)

26. Klik `[Edit]` pada `Divisi IT`
27. Klik `[Clear Field]`
28. Klik `[Save]`
29. Verifikasi server menolak dengan `403 Forbidden`
30. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
31. Verifikasi tidak ada redirect
32. Verifikasi modal Edit Allocation ditutup dan input kosong dibuang tanpa retry pada modal yang sama
33. Klik `[Edit]` pada `Divisi IT` lagi
34. Verifikasi modal Edit Allocation menampilkan nilai tersimpan 100
35. Tutup modal Edit Allocation dengan `[×]`
36. Verifikasi Section 1 dan Section 2 Tab Allocation Quota di-refresh
37. Verifikasi tampilan baca tidak berubah
38. Verifikasi tidak ada perubahan data: Allocated Quota Divisi IT tetap 100 lewat fixture BE

### Client Expired

39. Ganti akun: Logout
40. Login sebagai Total Control client Expired Pre-setup #18 (`Spectra.env.FA_EXPIRED_TC_PASSWORD`)
41. Ubah status Client menjadi Expired lewat fixture BE (sesi aktor sudah dibuka sebelum status berubah)

### TC-FA-LIC-447: Entitas Suspended/Expired: Force Logout ditolak 403 dengan toast baku (Expired)

42. Buka License > Concurrent User
43. Klik `[Force Logout]` pada sesi Budi Santoso
44. Klik `[Confirm Logout]`
45. Verifikasi server menolak dengan `403 Forbidden`
46. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
47. Verifikasi tidak ada redirect
48. Verifikasi dialog `Force Logout User` (D-FALIC-01) ditutup dan tidak dibuka kembali (tanpa retry pada dialog yang sama)
49. Verifikasi daftar sesi dan `Online Users` di-refresh
50. Verifikasi tampilan baca tidak berubah
51. Verifikasi tidak ada perubahan data: sesi Budi Santoso tetap aktif lewat fixture BE

### TC-FA-LIC-448: Entitas Suspended/Expired: Edit Allocation ditolak 403 dengan toast baku (Expired)

52. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
53. Klik `[Edit]` pada `Divisi IT`
54. Isi New Allocated Quota `120`
55. Klik `[Save]`
56. Verifikasi server menolak dengan `403 Forbidden`
57. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
58. Verifikasi tidak ada redirect
59. Verifikasi modal Edit Allocation ditutup dan input `120` dibuang tanpa retry pada modal yang sama
60. Klik `[Edit]` pada `Divisi IT` lagi
61. Verifikasi modal Edit Allocation menampilkan nilai tersimpan 100
62. Tutup modal Edit Allocation dengan `[×]`
63. Verifikasi Section 1 dan Section 2 Tab Allocation Quota di-refresh
64. Verifikasi tampilan baca tidak berubah
65. Verifikasi tidak ada perubahan data: Allocated Quota Divisi IT tetap 100 lewat fixture BE

### TC-FA-LIC-449: Entitas Suspended/Expired: Remove Allocation ditolak 403 dengan toast baku (Expired)

66. Klik `[Edit]` pada `Divisi IT`
67. Klik `[Clear Field]`
68. Klik `[Save]`
69. Verifikasi server menolak dengan `403 Forbidden`
70. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
71. Verifikasi tidak ada redirect
72. Verifikasi modal Edit Allocation ditutup dan input kosong dibuang tanpa retry pada modal yang sama
73. Klik `[Edit]` pada `Divisi IT` lagi
74. Verifikasi modal Edit Allocation menampilkan nilai tersimpan 100
75. Tutup modal Edit Allocation dengan `[×]`
76. Verifikasi Section 1 dan Section 2 Tab Allocation Quota di-refresh
77. Verifikasi tampilan baca tidak berubah
78. Verifikasi tidak ada perubahan data: Allocated Quota Divisi IT tetap 100 lewat fixture BE

## Notes

- Spec kelas h (state tenant, bagian 3 prinsip 13); perubahan status Client oleh fixture BE hanya memicu kondisi yang diuji.
- Langkah penghubung (aksi tanpa `Verifikasi`): ubah status Client (langkah 1 dan 41), ganti akun (langkah 39 dan 40), "Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`", dan "Tutup modal Edit Allocation dengan `[×]`" setelah memverifikasi nilai tersimpan (modal tidak dirty).
- Spec di atas 35 langkah (78 langkah): alasan dipertahankan, TC-FA-LIC-447, 448, dan 449 menurut Precondition TC dijalankan dua kali (client Suspended lalu client Expired), tiap client memuat tiga blok aksi tulis yang berbagi state yang sama, dan penolakan tiap aksi berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok client Expired mengulang blok client Suspended dengan akun dan fixture berbeda (langkah 42 sampai 78 mengulang langkah 2 sampai 38).
- Temuan untuk QA:
  - TC-FA-LIC-447, 448, dan 449 menulis precondition login Total Control Pre-setup #1, sedangkan Pre-setup #18 adalah dua client lain dengan akun sendiri; spec mengikuti Pre-setup #18 (akun Suspended dan Expired).
  - Kontrak fixture pengubah status Client tidak tertulis di TC; disediakan tim FE/BE.
