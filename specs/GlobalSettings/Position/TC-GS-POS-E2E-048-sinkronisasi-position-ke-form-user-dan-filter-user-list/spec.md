---
id: TC-GS-POS-E2E-048-sinkronisasi-position-ke-form-user-dan-filter-user-list
title: "Sinkronisasi Position Baru, Rename, dan Terhapus ke Form User, Form Non-Login User, dan Filter User List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-256
  - TC-GS-POS-257
  - TC-GS-POS-258
  - TC-GS-POS-281
  - TC-GS-POS-301
coverage:
  web: automated
---

# Sinkronisasi Position Baru, Rename, dan Terhapus ke Form User, Form Non-Login User, dan Filter User List

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Spec ini tidak menguji navigasi sehingga langkah 1 langsung mengklik `[+ Position]`.
- Akun sesi kedua (hanya TC-GS-POS-281, sebagai pemicu penghapusan Position): Admin B Total Control (Andi Wijaya) `superAdminGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Pre-setup 2), kredensial `Spectra.env.GS_TC2_PASSWORD`, dibuka di konteks browser kedua pada langkah 62. Konteks kedua ditutup beserta sesi loginnya pada langkah 78.
- Data Pre-setup: tidak ada yang dipakai.
- Data Dinamis (suffix per run dan nomor spec; fixture baru `Fixture.position.syncSeed048`):
  - `Risk Officer {runId}-048`: dibuat lewat UI pada TC-GS-POS-256, diubah menjadi `Risk Analyst Lead {runId}-048` pada TC-GS-POS-257, lalu menjadi `Risk Analyst Head {runId}-048` pada TC-GS-POS-301.
  - `Risk Officer II {runId}-048` (bebas relasi, dihapus UI pada TC-GS-POS-258) dan `Risk Officer III {runId}-048` (bebas relasi, dihapus oleh Admin B pada TC-GS-POS-281): di-seed lewat API di hook `before`.
  - Division `Divisi Uji {runId}-048`: di-seed lewat API di hook `before` karena Division wajib diisi pada form Create User dan fixture Division tidak ada di Pre-setup TC Position.
  - User Login `Hendra Gunawan {runId}-048` (First Name `Hendra`, Last Name `Gunawan {runId}-048`, email `hendragunawan+{runId}-048@qwertysystem.net`, Division `Divisi Uji {runId}-048`, Position `Risk Officer {runId}-048`): dibuat lewat fixture BE pada langkah 15, sesudah Position itu ada.
  - Nilai field wajib Create User pada TC-GS-POS-281: First Name `Risk`, Last Name `Tester {runId}-048`, Email `risktester+{runId}-048@qwertysystem.net`, Division `Divisi Uji {runId}-048`; field wajib lain (mis. Access) memakai nilai bawaan form. User ini tidak berhasil dibuat.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user `Hendra Gunawan {runId}-048` dan user `Risk Tester {runId}-048` bila ada, semua Position bersuffix `{runId}-048`, dan Division `Divisi Uji {runId}-048`; tutup konteks browser kedua; kosongkan Search dan Filter tabel User List dan tabel Position.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: dua konteks browser dengan akun berbeda (langkah 62); fixture BE untuk membuat Division dan user Login; pembacaan opsi dropdown Position pada Popup Create User, Create Non-Login User, Edit User, dan Filter Panel User List (opsi dicari lewat kolom pencarian dropdown).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-256: Position baru tersedia di dropdown Position form User dan Non-Login User

1. Klik `[+ Position]`
2. Isi Position Name dengan `Risk Officer {runId}-048`
3. Klik `[Submit]`
4. Tunggu aksi selesai (modal tertutup)
5. Buka Global Settings > User, klik sub-tab User List
6. Klik `[+ User]`
7. Buka dropdown Position
8. Verifikasi opsi `Risk Officer {runId}-048` tersedia pada Popup Create User
9. Tutup dropdown Position, klik `✕` pada Popup Create User
10. Klik sub-tab Non-Login User
11. Klik `[+ Non-Login User]`
12. Buka dropdown Position
13. Verifikasi opsi `Risk Officer {runId}-048` tersedia pada Popup Create Non-Login User
14. Tutup dropdown Position, klik `✕` pada Popup Create Non-Login User

### Persiapan TC-GS-POS-257: user memakai Position

15. Buat user Login `Hendra Gunawan {runId}-048` dengan Position `Risk Officer {runId}-048` lewat fixture BE

### TC-GS-POS-257: Rename Position tercermin di dropdown dan data user yang memakainya

16. Buka Global Settings > User, klik sub-tab Position
17. Ketik Search `Risk Officer {runId}-048` pada tabel Position, tekan Enter
18. Klik `⋯` pada baris `Risk Officer {runId}-048`, pilih `Edit`
19. Ganti Position Name dengan `Risk Analyst Lead {runId}-048`
20. Klik `[Save]`
21. Tunggu aksi selesai (modal tertutup)
22. Buka Global Settings > User, klik sub-tab User List, ketik Search email `hendragunawan+{runId}-048@qwertysystem.net`, tekan Enter
23. Klik `⋯` pada baris `Hendra Gunawan {runId}-048`, pilih `Edit`
24. Verifikasi field Position menampilkan `Risk Analyst Lead {runId}-048`
25. Buka dropdown Position
26. Verifikasi dropdown Position memuat `Risk Analyst Lead {runId}-048`
27. Verifikasi dropdown tidak memuat opsi `Risk Officer {runId}-048`
28. Tutup dropdown Position
29. Klik `[Save]` pada Popup Edit User
30. Verifikasi Popup Edit User tertutup sesudah Save
31. Verifikasi tidak ada pesan error
32. Verifikasi Position user `Hendra Gunawan {runId}-048` pada tabel User List tetap `Risk Analyst Lead {runId}-048`

### TC-GS-POS-301: Rename Position tercermin di opsi Filter Position tabel User List

33. Buka Global Settings > User, klik sub-tab Position
34. Ketik Search `Risk Analyst Lead {runId}-048` pada tabel Position, tekan Enter
35. Klik `⋯` pada baris `Risk Analyst Lead {runId}-048`, pilih `Edit`
36. Ganti Position Name dengan `Risk Analyst Head {runId}-048`
37. Klik `[Save]`
38. Tunggu aksi selesai (modal tertutup)
39. Buka Global Settings > User, klik sub-tab User List, klik `(←)` pada kotak Search
40. Klik ikon Filter, buka dropdown Position
41. Verifikasi dropdown Position memuat `Risk Analyst Head {runId}-048`
42. Verifikasi dropdown Position tidak memuat `Risk Analyst Lead {runId}-048`
43. Pilih `Risk Analyst Head {runId}-048`
44. Klik `[Apply]`
45. Verifikasi tabel User List menampilkan `Hendra Gunawan {runId}-048`
46. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-GS-POS-258: Position terhapus hilang dari dropdown form User dan Non-Login User

47. Buka Global Settings > User, klik sub-tab Position
48. Ketik Search `Risk Officer II {runId}-048` pada tabel Position, tekan Enter
49. Klik `⋯` pada baris `Risk Officer II {runId}-048`, pilih `Delete`
50. Klik `[Delete]` pada dialog `Delete Position`
51. Tunggu aksi selesai (dialog tertutup)
52. Buka Global Settings > User, klik sub-tab User List, klik `[+ User]`, buka dropdown Position
53. Verifikasi dropdown Position memuat `Risk Analyst Head {runId}-048` pada Popup Create User
54. Verifikasi opsi `Risk Officer II {runId}-048` tidak ada pada Popup Create User
55. Tutup dropdown Position, klik `✕` pada Popup Create User
56. Klik sub-tab Non-Login User, klik `[+ Non-Login User]`, buka dropdown Position
57. Verifikasi dropdown Position memuat `Risk Analyst Head {runId}-048` pada Popup Create Non-Login User
58. Verifikasi opsi `Risk Officer II {runId}-048` tidak ada pada Popup Create Non-Login User
59. Tutup dropdown Position, klik `✕` pada Popup Create Non-Login User

### TC-GS-POS-281: Form User yang memilih Position yang baru dihapus ditolak dengan error field-level

60. Sesi Admin A: buka Global Settings > User, klik sub-tab User List, klik `[+ User]`
61. Isi field wajib (First Name `Risk`, Last Name `Tester {runId}-048`, Email `risktester+{runId}-048@qwertysystem.net`, Division `Divisi Uji {runId}-048`) dan pilih Position `Risk Officer III {runId}-048`
62. Ganti akun ke sesi Admin B: buka konteks browser kedua, login sebagai Admin B dengan `Spectra.env.GS_TC2_PASSWORD`, buka Global Settings > User, klik sub-tab Position
63. Sesi Admin B: ketik Search `Risk Officer III {runId}-048`, tekan Enter, klik `⋯` pada barisnya, pilih `Delete`, klik `[Delete]` pada dialog `Delete Position`
64. Tunggu aksi selesai (dialog tertutup)
65. Kembali ke sesi Admin A, klik `[Submit]`
66. Verifikasi error inline di bawah field Position: "This position no longer exists. Please select another."
67. Verifikasi field Position dikosongkan otomatis
68. Buka dropdown Position
69. Verifikasi opsi dropdown Position di-refresh
70. Verifikasi dropdown Position memuat `Risk Analyst Head {runId}-048`
71. Verifikasi dropdown Position tidak memuat `Risk Officer III {runId}-048`
72. Tutup dropdown Position
73. Verifikasi field lain (First Name, Last Name, Email, Division) tetap terisi
74. Verifikasi Popup Create User tetap terbuka
75. Klik `✕` pada Popup Create User
76. Verifikasi dialog `Unsaved Changes`
77. Klik `[Leave]`
78. Tutup konteks browser kedua dan hapus sesi loginnya

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Spec ini kelas lintas modul (Position ke form User, form Non-Login User, dan filter User List).
- Urutan TC di spec: 256, 257, 301, 258, 281. TC sumber berurutan 256, 257, 258, 281, 301; 301 dipindah ke sesudah 257 karena memakai record yang sama (`Risk Analyst Lead` menjadi `Risk Analyst Head`), dan aksi Delete (258) serta TC multi-konteks (281) dipindah ke akhir (prinsip 5).
- Langkah "Tunggu aksi selesai" (langkah 4, 21, 38, 51, 64) ditulis tanpa `Verifikasi`. Langkah 4, 21, dan 38 mengikuti `[Submit]` atau `[Save]`, dan langkah 51 mengikuti `[Delete]` pada dialog `Delete Position` (langkah 50); hasil aksi-aksi itu tidak diasersi langsung dan langkah berikutnya pindah surface (konvensi bagian 8b butir 8). Langkah 64 mengikuti penghapusan oleh Admin B sebelum akun diganti kembali ke Admin A: `[Submit]` Admin A (langkah 65) harus terjadi sesudah penghapusan selesai supaya Position sudah tidak ada.
- Asersi tambahan di luar Expected TC (anchor positif supaya asersi absence opsi dropdown tidak lulus karena dropdown belum dimuat; konvensi bagian 8b butir 2): langkah 26 (opsi `Risk Analyst Lead` pada Popup Edit User, sebelum absence langkah 27), langkah 53 dan 57 (opsi `Risk Analyst Head`, record hasil rename TC-GS-POS-301 yang masih ada, pada Popup Create User dan Popup Create Non-Login User sebelum absence langkah 54 dan 58), serta langkah 70 (opsi `Risk Analyst Head` sebelum absence langkah 71). Langkah 41 (Expected TC-GS-POS-301 a) sudah menjadi anchor untuk absence langkah 42.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16, 33, 47 (membuka tab Position), langkah 17, 34, 48 (mencari baris target), langkah 22 (mencari user `Hendra Gunawan {runId}-048` lewat Search email di User List), langkah 63 (Admin B mencari Position `Risk Officer III {runId}-048` di tabel Position sebelum menghapusnya), langkah 9, 14, 55, 59 (menutup dropdown dan popup Create yang tidak dirty dengan `✕`; dropdown hanya dibuka tanpa memilih opsi sehingga tidak ada dialog `Unsaved Changes`), langkah 15 (membuat user Hendra lewat fixture BE), langkah 28 (menutup dropdown), langkah 46 (mengosongkan Filter Position), langkah 72 (menutup dropdown), langkah 78 (menutup konteks kedua), dan langkah "Tunggu aksi selesai" (langkah 4, 21, 38, 51, 64).
- Nama pengguna `Hendra Gunawan` pada TC sumber diganti user milik spec bersuffix `Hendra Gunawan {runId}-048`; TC-GS-POS-257 dan 301 mengubah nama Position yang dipakai user itu, sehingga memakai user Pre-setup 17 akan mengubah data bersama (S-06).
- Konteks browser kedua pada TC-GS-POS-281 hanya berfungsi sebagai pemicu penghapusan Position oleh Admin B; objek asersi adalah form Admin A (P-2, pemicu bukan objek uji).
- Spec melewati sekitar 35 langkah (78 langkah). Seluruhnya satu akun utama, tanpa state global; blok TC-GS-POS-258 dan TC-GS-POS-281 memakai data seeding sendiri dan tetap bermakna bila blok lain gagal. Blok TC-GS-POS-256, 257, dan 301 berbagi satu record Position yang berantai.
- Temuan untuk QA:
  - TC-GS-POS-256 menyebut "Login User" dan "tombol create"; PRD menamai sub-tab "User List" dan tombolnya `[+ User]` dan `[+ Non-Login User]`. Spec memakai nama PRD.
  - TC-GS-POS-257 menyatakan `Risk Officer` dipakai user Login `Hendra Gunawan`, sedangkan Pre-setup 17 menempatkan `Hendra Gunawan` pada `Sales Coordinator` (Pre-setup 16). TC tidak menyebut cara menautkan `Risk Officer` ke user; spec membuat user milik spec lewat fixture BE (mekanisme disediakan tim FE/BE).
  - TC-GS-POS-257 Expected c ("Save Edit User sukses dengan Position yang sama") tidak menyebut teks toast, dan Save tanpa perubahan pada form Edit User mungkin diperlakukan sebagai No-Op; spec mengasersi popup tertutup tanpa error dan Position tetap, tanpa teks toast.
  - TC-GS-POS-281 tidak menyebut field wajib Create User; PRD User mewajibkan First Name, Last Name, Email, dan Division (V-01, V-02, V-05, V-09). Spec mengisi keempatnya.
  - TC-GS-POS-281 Post Condition "User tidak dibuat" tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-GS-POS-301 tidak menyebut keadaan Filter Panel tabel User List sesudah `[Apply]` dan tidak menyebut cara mengosongkan Filter Position; langkah 46 membuka Filter Panel dengan klik ikon Filter lalu `[Clear Field]` dan `[Apply]`. Status kotak Search tabel User List sesudah berpindah sub-tab dan kembali (langkah 39) juga tidak disebut TC maupun PRD; langkah 39 mengklik `(←)` pada kotak Search dengan asumsi kotak masih terbuka berisi Search email dari langkah 22.
  - TC-GS-POS-256 dan 258 tidak menyebut apakah dropdown Position pada Popup Create User dapat dicari; spec mencari opsi lewat kolom pencarian dropdown.
