---
id: TC-GS-USER-E2E-174-sinkron-custom-field-deactivated-import-create-dan-section-hidden
title: "Sinkron Custom Field Deactivated: Create Ditolak di Field, Import Tersimpan dan Tersembunyi, serta Section Custom Fields Hidden di Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1105
  - TC-GS-USER-1104
  - TC-GS-USER-1121
coverage:
  web: automated
---

# Sinkron Custom Field Deactivated: Create Ditolak di Field, Import Tersimpan dan Tersembunyi, serta Section Custom Fields Hidden di Detail

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor (sesi UI): Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Akun Admin B (Total Control kedua, sesi API `[API Admin B]`): disediakan tim FE (tidak ada di Tabel Pre-setup TC), kredensial `Spectra.env.GS_TC2_PASSWORD`. Sesi API hanya memicu perubahan state Custom Field, tanpa hasil yang diasersi di sesi itu. Klien HTTP untuk sesi API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD.
- Env var: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Pengecualian layar awal: langkah 17 membuka Import > User Login dan langkah 22 membuka kembali Global Settings > User > User List; User List tetap layar awal dari hook `beforeEach` suite.
- Data Pre-setup (Tabel Data Uji Pre-setup): Custom Field `Blood Type` (Dropdown A/B/O/AB), `Skills` (Multi-Dropdown Excel/SQL), `Emergency Phone` (Phone, Required) (No. 24); Division `Finance` (No. 23); produk `Fixed Asset` (No. 26); Dewi Lestari (No. 12) hanya dibaca di TC-GS-USER-1121.
- Data Dinamis: Login User `Budi Santoso {runId}-174` (First Name `Budi`, Last Name `Santoso {runId}-174`), email `budisantoso+{runId}-174@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`, Blood Type `AB`. Dibuat TC-GS-USER-1104 lewat commit Import dari draft Import User Login 1 baris berstatus `pending` dengan nilai itu (draft disediakan tim FE di hook `before` sesuai fixture draft Import `tc-import.md`; Custom Field `Blood Type` Active saat draft dibuat). Dihapus di hook `after`. TC-GS-USER-1105 memakai email yang sama pada form Create tetapi user tidak pernah dibuat.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, atau LLD): sesi API Admin B untuk menonaktifkan dan mengaktifkan Custom Field (satu Custom Field dan seluruh Custom Field client, dengan daftar Custom Field yang Active pada awal spec dicatat di hook `before`); seeding draft Import User Login; membaca jumlah Login User pada entitas lewat BE sebagai baseline (8b butir 10); polling commit Import dengan memuat ulang halaman setiap 5 detik, batas tunggu 2 menit (bagian 6 konvensi, idiom polling worker commit).
- State global yang diubah: status Active Custom Field `Blood Type` (dinonaktifkan di langkah 4 dan 15, diaktifkan kembali di langkah 12 dan 30) dan seluruh Custom Field client (dinonaktifkan di langkah 34, diaktifkan kembali di langkah 40). Efek pada data Pre-setup yang dipakai sebagai target aksi tulis: Last Updated dan entri Changelog Custom Field `Blood Type` serta Custom Field lain (hanya karena toggle; nilai opsi tidak berubah). Pemulihan: hook `after` mengaktifkan kembali semua Custom Field yang Active pada awal spec, menghapus `Budi Santoso {runId}-174` lewat API, dan menghapus draft Import sisa bila ada, tanpa mengandalkan langkah berhasil penuh.

## Test Steps

### Persiapan

1. Catat baseline jumlah user Login pada entitas (dibaca lewat BE) sebagai `{n0}`

### TC-GS-USER-1105: Create ditolak di field karena Custom Field Blood Type dinonaktifkan sesi lain sebelum Submit

2. Klik `[+ User]` di Table Tools
3. Isi First Name `Budi`, Last Name `Santoso {runId}-174`, Division `Finance`, Email `budisantoso+{runId}-174@qwertysystem.net`, pilih Access `Fixed Asset`, pilih Blood Type `AB`
4. [API Admin B] Nonaktifkan Custom Field `Blood Type` hingga perubahan tersimpan
5. Klik `[Submit]`
6. Verifikasi inline error Blood Type: "This blood type no longer exists. Please select another."
7. Verifikasi field Blood Type kosong
8. Verifikasi jumlah user Login pada entitas sama dengan `{n0}` (user tidak dibuat)
9. Klik `✕` pada header Popup Create
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`
12. [API Admin B] Aktifkan kembali Custom Field `Blood Type` hingga perubahan tersimpan

### TC-GS-USER-1104: Import, nilai Custom Field Deactivated tersimpan ke User baru, tersembunyi selama nonaktif, tampil saat diaktifkan

13. Klik Tab `Custom Field`
14. Klik icon Search, ketik `Blood Type`, tekan Enter
15. Matikan switch Active baris `Blood Type`, klik `[Deactivate]` pada dialog
16. Tunggu aksi selesai
17. Buka Import > User Login
18. Klik `[Import (1)]`
19. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
20. Verifikasi Banner Hasil Commit bertone success dengan teks "Success, record has been imported. Duplicate records were ignored."
21. Verifikasi baris draft `Budi Santoso {runId}-174` tidak berstatus `error`
22. Buka Global Settings > User > User List (sub-tab Login User)
23. Klik icon Search, ketik `Budi Santoso {runId}-174`, tekan Enter
24. Verifikasi baris `Budi Santoso {runId}-174` tampil di daftar Login User
25. Klik Name `Budi Santoso {runId}-174`
26. Verifikasi Breadcrumb `User > Detail` tampil
27. Klik header Section Custom Fields
28. Verifikasi Custom Field aktif lain `Skills` tampil di Section Custom Fields
29. Verifikasi Custom Field `Blood Type` tidak tampil di Section Custom Fields
30. [API Admin B] Aktifkan kembali Custom Field `Blood Type` hingga perubahan tersimpan
31. Muat ulang Detail user `Budi Santoso {runId}-174` (F5)
32. Klik header Section Custom Fields
33. Verifikasi Custom Field Blood Type tampil bernilai `AB`

### TC-GS-USER-1121: Section Custom Fields Hidden penuh bila tidak ada Custom Field aktif

34. [API Admin B] Nonaktifkan seluruh Custom Field client hingga perubahan tersimpan
35. Klik menu User di sidebar Global Settings
36. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
37. Klik Name `Dewi Lestari`
38. Verifikasi Breadcrumb `User > Detail` tampil
39. Verifikasi Section Custom Fields tidak tampil sama sekali (tanpa header kosong)
40. [API Admin B] Aktifkan kembali seluruh Custom Field yang dinonaktifkan pada langkah 34 hingga perubahan tersimpan

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas fungsional (sinkron Custom Field Deactivated ke Create, Import, dan Detail); tidak ada TC kelas harness. Pelaku kedua `[API Admin B]` hanya memicu perubahan state lewat sesi API (bukan konteks kedua UI), ditulis "... hingga ... tersimpan" (R-20).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah: TC-GS-USER-1105 lebih dulu (form Create dan Custom Field `Blood Type` Active, tidak membuat data), lalu TC-GS-USER-1104 (membuat user lewat Import), dan TC-GS-USER-1121 paling akhir karena menonaktifkan seluruh Custom Field client dan hanya membaca Detail (bagian 3 prinsip 5; S-10).
- Spec melewati sekitar 35 langkah (40 langkah). Alasan: tiga TC berada di satu kelas fungsional dan satu tema (Custom Field Deactivated memengaruhi Create, Import, dan Detail), tiap blok memulihkan state Custom Field sendiri (langkah 12, 30, 40) dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah banyak karena satu `Verifikasi` per klausa Expected (S-01), satu aksi per baris, dan polling commit Import.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline), langkah 9 sampai 11 (menutup form dirty secara deterministik; S-08), langkah 12, 30, dan 40 (memulihkan status Custom Field; Post Condition TC-GS-USER-1104 dan 1105), langkah 13 sampai 16 (menonaktifkan `Blood Type` lewat Tab Custom Field; langkah Uji 1 TC-GS-USER-1104; langkah 16 adalah "Tunggu aksi selesai" karena langkah berikutnya berpindah surface), langkah 17 sampai 19 (membuka Import, commit, dan polling commit; langkah 17 dan 22 membuka layar di luar layar awal), langkah 22 sampai 23 dan 36 sampai 37 (Search baris target dibuka lewat Search nama persis; 8b butir 12, R-16), langkah 27 dan 32 (membuka Section Custom Fields yang collapsed secara default), langkah 31 (F5), langkah 35 (kembali ke User List).
- Asersi tambahan di luar Expected TC: langkah 26 dan 38 (Breadcrumb `User > Detail` sebagai anchor positif bahwa Detail termuat); langkah 28 (Custom Field aktif lain `Skills` tampil sebagai anchor positif untuk absence `Blood Type` pada langkah 29; 8b butir 2). Langkah 8 mengasersi "User tidak dibuat" lewat jumlah user terhadap baseline `{n0}` (asersi jumlah dengan baseline, S-12, bukan spec absence kelas g).
- Pembagian TC lintas spec: Create dengan Custom Field Deactivated dan Detail user saat Custom Field berubah lainnya berada di spec 031, 151, dan 152; spec ini tidak memuatnya.
- Temuan untuk QA:
  - TC-GS-USER-1104 precondition c: fixture draft Import "mengikuti `tc-import.md`"; `tc-import.md` menyebut draft commit hanya dibuat di Client E (kontrak fixture R3), sedangkan TC ini mengubah Custom Field `Blood Type` di Global Settings akun aktor yang sama. Spec memakai draft Import User Login milik akun Total Control Client A yang disediakan tim FE; perlu dikonfirmasi tim FE apakah draft di Client E dan Custom Field di client yang sama dengan akun aktor.
  - TC-GS-USER-1104 Expected a ("baris tidak berstatus `error`") tidak menyebut apakah baris draft masih tampil setelah commit; spec mengasersi baris tidak berstatus `error` (perlu dikonfirmasi tim FE bagaimana baris diamati setelah commit).
  - TC-GS-USER-1104 langkah 5 ("Aktifkan kembali Custom Field") tidak menyebut tempat; spec memicunya lewat sesi API Admin B agar Detail di sesi aktor tetap terbuka sebelum F5.
  - TC-GS-USER-1104 Expected b ("Detail tidak menampilkan Custom Field Blood Type") tidak menyebut Section Custom Fields collapsed; spec membuka section dan mengasersi `Blood Type` tidak tampil dengan `Skills` sebagai pembanding. Tabel Pre-setup No. 24 menandai `Emergency Phone` sebagai Required; draft Import dan form Create TC tidak mengisinya, sehingga hasil commit bergantung konfigurasi entitas uji yang disediakan tim FE.
  - TC-GS-USER-1105 langkah 3 ("Di tab lain nonaktifkan Custom Field") tidak menyebut admin yang bertindak; spec memakai sesi API Admin B. Post Condition (Custom Field dipulihkan) tanpa Expected padanan; dikerjakan di langkah 12 sebagai langkah penghubung.
  - TC-GS-USER-1121 precondition c ("Seluruh Custom Field client dalam status Deactivated") tidak menyebut client dan cara menyiapkannya; spec menonaktifkan seluruh Custom Field client akun aktor sementara (langkah 34, dipulihkan di langkah 40 dan hook `after`) karena suite serial. Alternatif: client khusus tanpa Custom Field aktif disediakan tim FE; perlu keputusan.
  - Perubahan status Custom Field Pre-setup (`Blood Type`, `Skills`, `Emergency Phone`, dan Custom Field lain) adalah perubahan data Pre-setup bersama yang tidak dapat dimiliki spec (S-06): pemulihan dijamin kemampuan fixture yang disediakan tim FE/BE dan `suite.md` belum menyatakannya; perlu dinyatakan di `suite.md` sebelum status spec naik.
