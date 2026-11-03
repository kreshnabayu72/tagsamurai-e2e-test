---
id: TC-AC-ACAL-E2E-046-snapshot-identitas-beku-pelaku-terhapus-dan-perubahan-nama
title: "Snapshot Identitas Beku, Pelaku Terhapus, dan Perubahan Nama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-140
  - TC-AC-ACAL-141
  - TC-AC-ACAL-142
coverage:
  web: automated
---

# Snapshot Identitas Beku, Pelaku Terhapus, dan Perubahan Nama

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); spec ini mengubah dan menghapus data user/admin dan dijalankan paling akhir bersama spec 045 (suite.md); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md). Untuk akun Total Control Distributor Alfa, hook before/after spec ini menyetel dan memulihkan flag seen yang sama (kemampuan disediakan tim FE/BE).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)):

| Akun | Email (Pre-setup TC) | Env var password |
|---|---|---|
| Total Control (Principal), akun hook `before` | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 1) | `Spectra.env.AC_TC_PASSWORD` |
| Total Control (Distributor Alfa) | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |

- Akses Global Settings: langkah 1 dan 15 membuka Global Settings > User, sehingga akun Total Control (Principal) harus dapat membuka Global Settings > User dan mengedit user serta admin; akses itu disediakan tim FE/BE.
- Login akun pertama (Total Control Principal) di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`; password user dan admin dinamis `Spectra.env.AC_DYN_PASSWORD`:
  - User `John Doe {runId}-046` (First Name `John`, Last Name `Doe {runId}-046`; singkatan `John D`), Position `Staff {runId}-046`, Division `Marketing {runId}-046`, staf Principal yang sudah membuka lalu menutup Admin Console (baris Session lama). Position `Supervisor {runId}-046` dan Division `Finance {runId}-046` sebagai nilai tujuan. Nilai bersuffix menggantikan `John Doe`, `Staff`, `Marketing`, `Supervisor`, dan `Finance` pada TC-AC-ACAL-140 supaya tidak bentrok dengan spec lain; hasil rename Last Name `Doe` menjadi `Doel` ditulis `Doel {runId}-046`.
  - Admin `Wulan Sari {runId}-046` (First Name `Wulan`, Last Name `Sari {runId}-046`) dengan capability mengedit Client, dan Client `Klien Wulan {runId}-046` dengan PIC Name awal `PIC Awal {runId}-046`. Hasil rename Last Name `Sari` menjadi `Pratiwi` ditulis `Pratiwi {runId}-046`.
  - Staf `Rudi {runId}-046` (First Name `Rudi`, Last Name `{runId}-046`; Partner Beta; menggantikan `Rudi` pada TC-AC-ACAL-142 supaya data yang dihapus milik spec), dibuat di hook `before` (dihapus pada langkah 28), Client `Karya Uji {runId}-046` milik Partner Beta; `Rudi {runId}-046` membuka lalu menutup Admin Console dan mengubah PIC Name client itu lewat sesi API di hook `before` (precondition TC-AC-ACAL-142).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua user, admin, Position, Division, dan Client dinamis di atas (atau nama hasil edit) bila masih ada, termasuk staf `Rudi {runId}-046` bila langkah 28 tidak sampai berjalan. Entri log tidak dapat dihapus; semua nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor (user dinamis membuka Admin Console, admin mengubah PIC Name Client, Principal menghapus staf); pembacaan jumlah baris Tab Session dan Tab User Action untuk nama `Rudi {runId}-046` lewat sesi API aktor Total Control Distributor Alfa sebagai baseline (S-12) tanpa sesi UI tambahan; baseline total tidak dipakai di TC lain karena nama bersuffix unik. Baseline `Rudi {runId}-046` tetap dibaca (bukan nol) karena baris sesi dan edit staf itu dibuat di hook `before` sebelum penghapusan.
- State global yang diubah: nama user `John Doe {runId}-046` dan admin `Wulan Sari {runId}-046` (data milik spec, dihapus di hook `after`) serta penghapusan staf `Rudi {runId}-046`; tidak ada data Pre-setup yang diubah.

## Test Steps

### TC-AC-ACAL-140: Snapshot identitas Tab Session tidak berubah setelah data user diubah

1. Buka Global Settings > User, ketik Search `John Doe {runId}-046`, tekan Enter, lalu buka form Edit pada baris itu
2. Ubah Last Name menjadi `Doel {runId}-046`, Position menjadi `Supervisor {runId}-046`, dan Division menjadi `Finance {runId}-046`
3. Klik [Save]
4. Tunggu aksi selesai: form Edit tertutup atau tombol [Save] aktif kembali
5. Pemicu API: `John Doel {runId}-046` membuka Admin Console hingga baris `Session started` baru tersimpan
6. Buka Admin Console > Activity Log > Session
7. Ketik Search `Staff {runId}-046`, tekan Enter
8. Verifikasi baris lama menampilkan User `John D`, Position `Staff {runId}-046`, dan Division `Marketing {runId}-046`
9. Ganti isi kotak search dengan `Supervisor {runId}-046`, tekan Enter
10. Verifikasi baris baru menampilkan User `John D`, Position `Supervisor {runId}-046`, dan Division `Finance {runId}-046`
11. Arahkan kursor ke sel User pada baris baru
12. Verifikasi tooltip menampilkan `John Doel {runId}-046`
13. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-141: Snapshot Modified By tidak berubah setelah nama admin diubah

14. Pemicu API: admin `Wulan Sari {runId}-046` mengubah PIC Name Client `Klien Wulan {runId}-046` menjadi `PIC 141a {runId}-046` hingga tersimpan
15. Buka Global Settings > User, ketik Search `Wulan Sari {runId}-046`, tekan Enter, lalu buka form Edit pada baris itu
16. Ubah Last Name menjadi `Pratiwi {runId}-046`
17. Klik [Save]
18. Tunggu aksi selesai: form Edit tertutup atau tombol [Save] aktif kembali
19. Pemicu API: admin `Wulan Pratiwi {runId}-046` mengubah PIC Name Client `Klien Wulan {runId}-046` menjadi `PIC 141b {runId}-046` hingga tersimpan
20. Buka Admin Console > Activity Log > User Action
21. Ketik Search `Klien Wulan {runId}-046`, tekan Enter
22. Arahkan kursor ke sel Modified By pada baris Field `PIC Name` New Value `PIC 141a {runId}-046`
23. Verifikasi tooltip pada baris lama menampilkan `Wulan Sari {runId}-046`
24. Arahkan kursor ke sel Modified By pada baris Field `PIC Name` New Value `PIC 141b {runId}-046`
25. Verifikasi tooltip pada baris baru menampilkan `Wulan Pratiwi {runId}-046`
26. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-142: Log tetap menampilkan pelaku yang sudah dihapus dan tetap ter-scope

27. Baca lewat sesi API aktor Total Control (Distributor Alfa) jumlah baris Tab Session dengan User `Rudi {runId}-046` sebagai baseline RS0 dan jumlah baris Tab User Action dengan Modified By `Rudi {runId}-046` sebagai baseline RU0
28. Pemicu API: Principal menghapus staf `Rudi {runId}-046` hingga tersimpan
29. Tunggu aksi selesai: penghapusan staf `Rudi {runId}-046` tersimpan
30. Ganti akun: logout, lalu login sebagai Total Control (Distributor Alfa) dengan `Spectra.env.AC_ALFA_TC_PASSWORD`
31. Buka Admin Console > Activity Log > Session
32. Ketik Search `Rudi {runId}-046`, tekan Enter
33. Verifikasi sedikitnya satu baris sesi staf `Rudi {runId}-046` tampil dengan nama staf itu (format nama singkat)
34. Verifikasi jumlah total hasil pada footer `Showing X–Y of Z entries` sama dengan baseline RS0, sehingga sesi `Rudi {runId}-046` tetap tampil untuk Distributor Alfa
35. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
36. Klik tab "User Action"
37. Ketik Search `Rudi {runId}-046`, tekan Enter
38. Verifikasi baris `Edit` oleh `Rudi {runId}-046` tampil dengan Modified By staf itu (format nama singkat)
39. Verifikasi jumlah total hasil pada footer `Showing X–Y of Z entries` sama dengan baseline RU0, sehingga baris Edit oleh `Rudi {runId}-046` tetap tampil
40. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-140, 141, 142).
- Urutan TC di spec sama dengan sumber; aksi yang menghapus data (hapus staf `Rudi {runId}-046`) ada di langkah 28, setelah semua kasus lain, dan TC-AC-ACAL-142 terakhir karena memakai Distributor Alfa sebagai pengamat.
- Spec 40 langkah, di atas smell 35. Alasan: seluruh TC satu topik (snapshot identitas log atas perubahan atau penghapusan data pelaku) dan satu permukaan; tiap blok TC berdiri sendiri dengan data bersuffix sendiri dan pelaku sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pelaku pada langkah 5, 14, 19, dan 28 memakai sesi API (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`): bukan konteks kedua, tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka modul sumber, form, dan menu (langkah 1, 6, 15, 20, 31, 36), mengisi dan menyimpan form sumber (langkah 2, 3, 16, 17), "Tunggu aksi selesai" (langkah 4, 18, 29; bagian 8b butir 8), pemicu lewat sesi API (langkah 5, 14, 19, 28), mengetik, mengganti isi, dan menutup Search (langkah 7, 9, 13, 21, 26, 32, 35, 37, 40), mengarahkan kursor (langkah 11, 22, 24), baseline (langkah 27), dan ganti akun (langkah 30). Search di GS > User (langkah 1 dan 15) menemukan baris target.
- Search `Staff {runId}-046` dan `Supervisor {runId}-046` (langkah 7 dan 9) membedakan baris lama dan baru pada Tab Session; TC mengidentifikasi keduanya lewat nilai Position yang berbeda.
- Asersi `Rudi {runId}-046` memakai baseline selisih (S-12): jumlah baris dibaca sebelum penghapusan (RS0, RU0) dan dibandingkan sesudahnya, sehingga asersi tidak bergantung pada angka mutlak.
- Temuan untuk QA:
  - TC-AC-ACAL-140 sampai 142 memakai nama literal (`John Doel`, `Wulan Pratiwi`, `Rudi`). Spec memakai nama bersuffix untuk `John Doe`, `Wulan Sari`, dan `Rudi` (target aksi tulis atau hapus milik spec); QA konfirmasi. Singkatan nama tampil `Rudi {runId}-046` di kolom User dan Modified By ditetapkan format nama singkat FE; spec tidak mengasersi inisial.
  - TC-AC-ACAL-140 tidak menyebut cara membedakan baris lama dan baru; spec memakai nilai Position. TC-AC-ACAL-141 tidak menyebut Client yang diedit dan field yang diubah; spec memakai Client dinamis dan PIC Name.
  - TC-AC-ACAL-142 Expected b menyebut "tetap tampil" tanpa jumlah; spec memakai baseline jumlah baris sebelum penghapusan. Capability admin dan staf untuk mengedit Client oleh `Rudi` tidak disebut TC; disediakan tim FE/BE.
  - Email Pre-setup memakai placeholder `{namaCompany}` password: `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`; `AC_ALFA_TC_PASSWORD`, `AC_DYN_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
