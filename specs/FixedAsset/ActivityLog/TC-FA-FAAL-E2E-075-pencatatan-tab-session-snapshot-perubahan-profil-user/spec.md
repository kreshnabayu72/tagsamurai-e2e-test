---
id: TC-FA-FAAL-E2E-075-pencatatan-tab-session-snapshot-perubahan-profil-user
title: "Pencatatan Tab Session: Baris Lama Tidak Berubah Setelah Profil User Diubah"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-220
  - TC-FA-FAAL-284
coverage:
  web: automated
---

# Pencatatan Tab Session: Baris Lama Tidak Berubah Setelah Profil User Diubah

## Prerequisites

- Mode: FE+BE.
- Akun observer dan aktor: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, tab Session).
- Data Tab Session SS-01 sampai SS-11 (Pre-setup #11): SS-01 adalah baris John Doe (Position `Staff`, Division `Marketing`) dan SS-07 adalah baris Dewi Lestari (Employee ID `EMP005`, Position `Staff`, Division `Marketing`); dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE).
- Pelaku (Pre-setup #16), email dari `Fixture.activity-log.<kunci>.email` (fixture belum ada, disediakan tim FE):
  - John Doe: App Access Fixed Asset dan seat subscription tersedia; password `Spectra.env.FA_JOHNDOE_PASSWORD`. Tanggal baris SS-01 dari `Fixture.activity-log.ss01.date`.
  - Dewi Lestari: user aktif dengan Employee ID `EMP005`, Position `Staff`, Division `Marketing`. User ini dihapus oleh langkah 14; tim FE/BE menyediakannya kembali sebagai data milik spec ini di hook `before` (baris SS-07 tetap dari Pre-setup #11).
  - Env var `FA_JOHNDOE_PASSWORD` terdaftar di butir "Env var" `suite.md` (R-07). Password tidak ditulis di spec atau fixture.
- Kemampuan teknis disediakan tim BE/FE: sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk John Doe dan Admin Alpha, termasuk mengubah Position dan Division, mengganti nama dan Employee ID, menonaktifkan, dan menghapus user di Global Settings > User.
- State yang diubah dan pemulihannya: Position dan Division John Doe dikembalikan ke `Staff` dan `Marketing` pada langkah 12 dan di hook `after`; Dewi Lestari dihapus pada langkah 14 dan disediakan ulang di hook `before` run berikutnya; sesi-produk John Doe ditutup di hook `after`.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun observer.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-220: Baris Tab Session adalah snapshot, perubahan profil user tidak mengubah baris lama

1. Catat Z0 dari teks `Showing X–Y of Z entries` di Tab Session, lalu Admin Total Control (sesi API aktor, Admin Alpha) mengubah Position John Doe menjadi `Supervisor` dan Division menjadi `Finance` di Global Settings > User hingga tersimpan
2. Pelaku John Doe (sesi API aktor) login dengan password dan membuka produk Fixed Asset lagi hingga Session started tersimpan
3. Verifikasi teks `Showing X–Y of Z entries` di Tab Session menjadi Z1 dengan Z1 = Z0 + 1
4. Klik icon Filter
5. Verifikasi dropdown Position memuat `Staff` dan `Supervisor`
6. Verifikasi dropdown Division memuat `Marketing` dan `Finance`
7. Pilih `Staff` pada field Position, `Marketing` pada field Division, dan rentang Date baris SS-01 (`Fixture.activity-log.ss01.date`), klik `[Apply]`
8. Verifikasi baris SS-01 tampil dengan Position `Staff` dan Division `Marketing`
9. Klik icon Filter, ganti pilihan menjadi `Supervisor` pada field Position, `Finance` pada field Division, dan rentang Date hari ini, klik `[Apply]`
10. Verifikasi baris baru John Doe tampil dengan Position `Supervisor` dan Division `Finance`
11. Klik menu `Activity Log` pada sidebar Reports & Logs (mereset Search, Filter, dan Sort)
12. Pulihkan Position John Doe ke `Staff` dan Division ke `Marketing` lewat sesi API aktor hingga tersimpan

### TC-FA-FAAL-284: Baris Tab Session tidak berubah setelah user diganti nama, Employee ID diubah, dinonaktifkan, dan dihapus

13. Admin Total Control (sesi API aktor, Admin Alpha) mengubah nama Dewi Lestari menjadi `Dewi Anggraini` dan Employee ID `EMP005` menjadi `EMP105` di Global Settings > User hingga tersimpan
14. Admin Total Control (sesi API aktor, Admin Alpha) menonaktifkan lalu menghapus pengguna tersebut hingga tersimpan
15. Ketik Search `Lestari`, tekan Enter
16. Verifikasi hasil Search `Lestari` menampilkan baris SS-07
17. Verifikasi baris SS-07 tampil dengan User `Dewi L` dan Employee ID `EMP005`
18. Arahkan kursor ke User pada baris SS-07
19. Verifikasi hover User baris SS-07 menampilkan `Dewi Lestari`
20. Ganti isi kotak search dengan `Anggraini`, tekan Enter
21. Verifikasi state `No results found` tampil
22. Klik `(←)` pada kotak Search
23. Klik icon Filter dan buka dropdown User
24. Verifikasi dropdown User memuat `Dewi Lestari`
25. Verifikasi dropdown User tidak memuat `Dewi Anggraini`
26. Klik menu `Activity Log` pada sidebar Reports & Logs (mereset Search, Filter, dan Sort)

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan Verifikasi TC-FA-FAAL-220 mengikuti state Filter (bagian 8b butir 5): total Z0 + 1 (langkah 3, Expected butir b) dibaca sebelum Filter dipakai; dropdown (langkah 5 dan 6, Expected butir c) dicek sebelum Filter menemukan baris (langkah 8, butir a; langkah 10, butir b). Urutan Verifikasi TC-FA-FAAL-284 mengikuti Search: baris SS-07 ditemukan lewat Search `Lestari` (langkah 15 sampai 19, butir c dan a), lalu keyword `Anggraini` (langkah 20 dan 21, butir c), lalu dropdown (langkah 23 sampai 25, butir b).
- Langkah penghubung (S-03): langkah 1 dan 2 (pencatatan Z0, pemicu perubahan profil dan sesi baru), langkah 7 dan 9 memakai Filter Date supaya baris SS-01 dan baris baru berada di halaman teramati (S-14), langkah 11, 22, dan 26 (reset dan pengosongan Search), langkah 12 (pemulihan), langkah 13 dan 14 (pemicu perubahan user lewat sesi API aktor).
- Search `Lestari` pada langkah 15 dan Search `Anggraini` pada langkah 20 adalah langkah penghubung untuk menemukan baris target sekaligus Expected TC-FA-FAAL-284 butir c (R-16).
- Anchor absence langkah 25 adalah Verifikasi langkah 24 pada dropdown yang sama; anchor `No results found` langkah 21 adalah state hasil Search (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAL-220 tidak menyebut cara menemukan baris SS-01 di antara baris John Doe lain pada Tab Session yang tumbuh; spec memakai Filter Date dengan tanggal seeding SS-01 dari fixture (S-14).
  - Baris log immutable, jadi baris John Doe dengan Position `Supervisor` dan Division `Finance` bertambah tiap run; asersi langkah 10 memakai rentang Date hari ini dan tidak dapat memakai nama bersuffix karena nilai berasal dari TC.
  - TC-FA-FAAL-284 memakai Dewi Lestari yang juga muncul sebagai target di TC-FA-FAAL-230; user dihapus di langkah 14; spec 058 menyeed Dewi Lestari sendiri di hook `before`, sehingga tiap spec menyediakan datanya sendiri dan tidak bergantung urutan.
  - TC-FA-FAAL-284 menyebut "Search `Anggraini` lalu `Lestari`" sedangkan spec memakai urutan sebaliknya untuk menemukan SS-07 lebih dulu; hasil asersi sama.
  - Email dan password John Doe tidak tertulis di Pre-setup TC; email disediakan tim FE dan env var password mengikuti `suite.md`.
