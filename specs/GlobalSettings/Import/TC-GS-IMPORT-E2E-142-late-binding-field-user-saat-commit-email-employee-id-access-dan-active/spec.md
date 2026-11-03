---
id: TC-GS-IMPORT-E2E-142-late-binding-field-user-saat-commit-email-employee-id-access-dan-active
title: "Late-binding field User saat commit: Email, Employee ID, Access, dan Active Period menjadi tidak valid"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-396
  - TC-GS-IMPORT-397
  - TC-GS-IMPORT-398
  - TC-GS-IMPORT-399
  - TC-GS-IMPORT-400
coverage:
  web: automated
---

# Late-binding field User saat commit: Email, Employee ID, Access, dan Active Period menjadi tidak valid

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua: Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, hanya lewat sesi API sebagai pemicu perubahan state (P-2); tidak ada asersi di sesi itu. Pemicu produk memakai fixture Admin Console (lihat kemampuan teknis).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > User Login (Client E); perpindahan Sub-Tab atau halaman lain ditulis sebagai langkah.
- Data Dinamis (draft lewat fixture `Fixture.import.lateBindingUser142`, fixture baru; nama literal dari Data Dinamis karena asersi bergantung pada nama dan jumlah): D-54 (user-login-commit-8.csv, 8 baris `pending`: Rizky Pratama EMP-5001, Sinta Maharani Active Period H+30, Doni Kurniawan, Eka Putri, Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata); D-55 (user-non-login-commit-5.csv, 5 baris `pending`: Joko Santoso, Kartika Dewi Active Period H+30, Lukman Hakim, Maya Sari, Nanda Wijaya). Produk organisasi Client E: Global Settings dan Fixed Asset.
- Kemampuan teknis (disediakan tim FE/BE): skrip reset Client E sesuai D-47 (hapus User Login dan User Non Login hasil commit, hapus Login User buatan Admin kedua, hapus draft dan hasil commit terakhir, pulihkan produk organisasi Fixed Asset); permintaan buat Login User atas nama Admin kedua Client E lewat klien HTTP; fixture Admin Console untuk mencabut produk Fixed Asset dari organisasi Client E; fixture Active Period baris staging (NC-08) yang mengatur tanggal Active Period baris staging ke hari ini menurut zona waktu Client E.
- State global: produk organisasi Client E dicabut sementara pada TC-GS-IMPORT-398 dan dipulihkan oleh reset D-47 dan hook `after`; Client E dimutasi lalu direset. Suite Import berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 dan pulihkan state yang diubah spec (lihat kemampuan teknis).

## Test Steps

### TC-GS-IMPORT-396: Email menjadi bentrok tepat saat commit menghasilkan error

1. Reset Client E ke tanpa draft (D-47), siapkan draft User Login 8 baris dari user-login-commit-8.csv (D-54, Email `indah.permata@example.com` pada baris #8) lewat fixture
2. Muat ulang halaman Import > User Login dan tunggu Staging Table termuat
3. Verifikasi footer menampilkan `[Import (8)]` Enabled
4. Buat Login User dengan Email `indah.permata@example.com` di halaman User > User List > Login User atas nama Admin kedua Client E lewat sesi API hingga tersimpan
5. Pada halaman yang sama (tanpa memuat ulang) klik [Import (8)]
6. Tunggu aksi selesai (permintaan mendapat respons)
7. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
8. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
9. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Indah Permata (kolom # bernilai 1)
10. Verifikasi Error Summary Callout memuat "Email already exists"
11. Verifikasi Error Summary Callout menampilkan badge "1 row"
12. Buka halaman User > User List > Login User
13. Atur Rows per page 100
14. Verifikasi halaman User > User List > Login User Client E memuat 7 user baru dari baris #1-#7

### TC-GS-IMPORT-397: Employee ID menjadi bentrok tepat saat commit menghasilkan error

15. Reset Client E ke tanpa draft (D-47), siapkan draft User Login 8 baris dari user-login-commit-8.csv (D-54, Employee ID `EMP-5001` pada baris #1) lewat fixture
16. Buka Import > User Login dan tunggu Staging Table termuat
17. Verifikasi footer menampilkan `[Import (8)]` Enabled
18. Buat Login User dengan Employee ID `EMP-5001` di halaman User > User List > Login User atas nama Admin kedua Client E lewat sesi API hingga tersimpan
19. Pada halaman yang sama (tanpa memuat ulang) klik [Import (8)]
20. Tunggu aksi selesai (permintaan mendapat respons)
21. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
22. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
23. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Rizky Pratama (kolom # bernilai 1)
24. Verifikasi Error Summary Callout memuat "Employee ID already exists"
25. Verifikasi Error Summary Callout menampilkan badge "1 row"
26. Buka halaman User > User List > Login User
27. Atur Rows per page 100
28. Verifikasi halaman User > User List > Login User Client E memuat 7 user baru dari baris #2-#8

### TC-GS-IMPORT-398: Access menjadi tidak valid saat commit (produk tidak lagi tersedia) menghasilkan error

29. Reset Client E ke tanpa draft (D-47), siapkan draft User Login 8 baris dari user-login-commit-8.csv (D-54, Access `Fixed Asset` pada baris #1, #3, #5, #7 dan `Global Settings` saja pada baris #2, #4, #6, #8) lewat fixture
30. Buka Import > User Login dan tunggu Staging Table termuat
31. Verifikasi footer menampilkan `[Import (8)]` Enabled
32. Hapus produk Fixed Asset dari organisasi Client E lewat fixture Admin Console (atas nama administrator Admin Console)
33. Pada halaman yang sama (tanpa memuat ulang) klik [Import (8)]
34. Tunggu aksi selesai (permintaan mendapat respons)
35. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
36. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 4 errors remain." tampil
37. Verifikasi Staging Table menampilkan 4 baris berstatus `error`: Rizky Pratama, Doni Kurniawan, Fajar Hidayat, Hendra Gunawan (Access memuat `Fixed Asset`)
38. Verifikasi Error Summary Callout memuat "Access must only contain the following values: Global Settings"
39. Verifikasi Error Summary Callout menampilkan badge "4 rows"
40. Buka halaman User > User List > Login User
41. Atur Rows per page 100
42. Verifikasi halaman User > User List > Login User Client E memuat 4 user baru: Sinta Maharani, Eka Putri, Gita Savitri, Indah Permata

### TC-GS-IMPORT-399: Active Period menjadi tidak valid saat commit (tanggal sudah lewat) menghasilkan error

43. Reset Client E ke tanpa draft (D-47), siapkan draft User Login 8 baris dari user-login-commit-8.csv (D-54, Active Period baris #2 H+30) lewat fixture
44. Atur Active Period baris #2 (Sinta Maharani) menjadi tanggal hari ini menurut zona waktu Client E lewat fixture data staging hingga tersimpan (tanpa membuka Staging Table)
45. Buka Import > User Login
46. Klik [Import (8)]
47. Tunggu aksi selesai (permintaan mendapat respons)
48. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
49. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
50. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Sinta Maharani (kolom # bernilai 1)
51. Verifikasi Error Summary Callout memuat "Active Period: Please select a future date."
52. Verifikasi Error Summary Callout menampilkan badge "1 row"
53. Buka halaman User > User List > Login User
54. Atur Rows per page 100
55. Verifikasi halaman User > User List > Login User Client E memuat 7 user baru
56. Verifikasi user Sinta Maharani tidak ada

### TC-GS-IMPORT-400: Active Period menjadi tidak valid saat commit pada User Non Login

57. Reset Client E ke tanpa draft (D-47), siapkan draft User Non Login 5 baris dari user-non-login-commit-5.csv (D-55, Active Period baris #2 H+30) lewat fixture
58. Atur Active Period baris #2 (Kartika Dewi) menjadi tanggal hari ini menurut zona waktu Client E lewat fixture data staging hingga tersimpan (tanpa membuka Staging Table)
59. Buka Import > User Non Login
60. Klik [Import (5)]
61. Tunggu aksi selesai (permintaan mendapat respons)
62. Muat ulang halaman Import > User Non Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
63. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
64. Verifikasi Staging Table menampilkan 1 baris berstatus `error`: Kartika Dewi (kolom # bernilai 1)
65. Verifikasi Error Summary Callout memuat "Active Period: Please select a future date."
66. Verifikasi Error Summary Callout menampilkan badge "1 row"
67. Buka halaman User > User List > Non-Login User
68. Verifikasi halaman User > User List > Non-Login User Client E memuat 4 user baru
69. Verifikasi user Kartika Dewi tidak ada

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (396 sampai 400) dipertahankan; User Non Login (TC-GS-IMPORT-400) terakhir karena berbeda Sub-Tab.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah pertama tiap blok (reset Client E dan penyiapan draft karena Precondition tiap TC mensyaratkan Client E direset sebelum TC), langkah pemicu (Admin kedua, fixture Admin Console, atau fixture Active Period), langkah menunggu aksi selesai sesudah klik [Import (N)], langkah menunggu commit, langkah pindah halaman dan Rows per page 100.
- P-2: Admin kedua Client E dan fixture Admin Console hanya memicu perubahan state dan bukan objek asersi.
- Anchor positif untuk absence: daftar user baru diverifikasi lebih dulu di blok yang sama sebelum verifikasi user tertentu tidak ada.
- Spec melewati sekitar 35 langkah. Alasan: lima blok TC homogen (satu objek uji: field User menjadi tidak valid tepat saat commit) yang berdiri sendiri, masing-masing mereset Client E; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pola halaman basi (late-binding saat commit, TC-GS-IMPORT-396..398): halaman Import dimuat dan Staging Table dibaca sebelum pemicu, lalu `[Import (N)]` diklik pada halaman yang sama tanpa dimuat ulang, dengan N dari sebelum pemicu. Referensi, duplikat, dan opsi dievaluasi ulang saat commit selain saat pembacaan Staging Table (PRD `import.md` baris 994, 1164, 1195). `Verifikasi` footer `[Import (N)]` sebelum pemicu adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan draft sudah dibaca pada halaman itu.
- Temuan untuk QA:
  - TC-GS-IMPORT-396 sampai 400: Post Condition (draft berisi baris `error`; record User baru tersimpan; Login User buatan Admin kedua ada; produk organisasi hanya Global Settings) sebagian teramati lewat Expected; sisanya tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-GS-IMPORT-398: akun pelaku fixture Admin Console tidak tertulis di Pre-setup TC; ditulis "fixture Admin Console disediakan tim FE".
  - TC-GS-IMPORT-399 dan 400: "tanggal hari ini menurut zona waktu Client E" bergantung waktu saat run (dekat tengah malam batas zona waktu berbeda dari UTC); TC tidak menyebut jam server atau zona yang dipakai fixture.
  - TC-GS-IMPORT-396 sampai 400: nama user, Email, dan Employee ID D-54 dan D-55 literal tanpa suffix per run karena asersi bergantung pada nilai; pengecualian S-12 untuk data ini belum dinyatakan di konvensi, dipertahankan dengan reset D-47 dan suite serial.
