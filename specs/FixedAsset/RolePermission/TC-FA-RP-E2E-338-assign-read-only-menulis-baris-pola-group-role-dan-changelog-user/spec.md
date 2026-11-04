---
id: TC-FA-RP-E2E-338-assign-read-only-menulis-baris-pola-group-role-dan-changelog-user
title: "Assign Read Only ke user Standard menulis baris pola Group Role pada semua group dengan Read saja"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1170
coverage:
  web: automated
---

# Assign Read Only ke user Standard menulis baris pola Group Role pada semua group dengan Read saja

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (kolam pengguna Standard; Budi Setiawan sebagai target), #18 (pohon group dengan tujuh group), #24 (disebut Precondition TC; lihat Temuan untuk QA).
- Precondition TC (dipakai sebagai precondition, tidak diasersi): Budi Setiawan berstatus Standard tanpa penugasan Group Role, disiapkan lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Baseline Changelog: Changelog User > Group Role adalah audit trail permanen; jumlah entri dicatat sebelum `[Assign]` (langkah 7) dan tidak diasersi sebagai angka absolut (S-12).
- Pemulihan: Budi Setiawan dipulihkan ke state seed Standard di hook `after` (kemampuan disediakan tim FE/BE). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1170: Assign Read Only ke user Standard menulis baris pola Group Role pada semua group dengan Read saja

1. Buka Settings > User lewat sidebar
2. Ketik Search `Budi Setiawan`, tekan Enter
3. Klik Name `Budi Setiawan`
4. Klik Tab `Role`
5. Klik sub-tab `Group Role`
6. Klik ikon `[Changelog]`
7. Catat jumlah entri Changelog User > Group Role sebagai baseline
8. Tutup modal Changelog dengan `[×]`
9. Buka menu Settings > Role & Permission dari sidebar
10. Klik Tab `Read Only`
11. Klik `[+ Assign]` di Tab Read Only
12. Centang Budi Setiawan
13. Klik `[Assign]`
14. Verifikasi muncul toast sukses: `Success, Read Only has been assigned.`
15. Buka Tab System lalu Detail Role Group Role `Manage files`
16. Klik `All Groups`
17. Ketik Search `Budi Setiawan`, tekan Enter
18. Verifikasi baris Budi Setiawan tampil pada setiap group di pohon Pre-setup #18
19. Verifikasi Read baris Budi Setiawan pada setiap group aktif dan terkunci
20. Verifikasi Delete baris Budi Setiawan pada setiap group tidak aktif
21. Verifikasi Create dan Update baris Budi Setiawan pada setiap group menampilkan `—`
22. Buka Tab System lalu Detail Role `Manage asset & TAG`
23. Klik node `Dock 1`
24. Ketik Search `Budi Setiawan`, tekan Enter
25. Verifikasi baris Budi Setiawan tampil di `Dock 1`
26. Verifikasi baris Budi Setiawan di `Dock 1`: Read aktif
27. Verifikasi baris Budi Setiawan di `Dock 1`: Create, Update, dan Delete tidak aktif
28. Buka Settings > User lewat sidebar
29. Ketik Search `Budi Setiawan`, tekan Enter
30. Klik Name `Budi Setiawan`
31. Klik Tab `Role`
32. Klik sub-tab `Group Role`
33. Klik ikon `[Changelog]`
34. Verifikasi jumlah entri Changelog User > Group Role bertambah dari baseline langkah 7
35. Verifikasi modal Changelog: User > Group Role memuat entri `Assign (via Read Only)` per baris Role × Group

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 35 langkah.
- Langkah penghubung (S-03): langkah 1 sampai 8 (pencatatan baseline Changelog), 9, 10, 15, 16, 22, 23, 28 (pindah halaman, tab, Detail Role, dan node). Akun aktor pertama sudah login di hook `before` (S-07).
- Search untuk menemukan baris target (R-16): langkah 2, 17, 24, 29. Langkah 18 dan 25 membuktikan sedikitnya satu baris hasil Search tampil sebelum asersi "pada setiap group" (8b.2). Search tidak dibersihkan antar Detail Role karena tiap Detail Role dibuka dari Tab System sebagai halaman baru.
- Langkah 34 dan 35 membaca entri baru sebagai himpunan entri teratas sesudah selisih dari baseline dibuktikan, tanpa mengandalkan urutan di antara entri se-menit (S-14).
- Pembagian TC lintas spec: TC-FA-RP-1169 (Assign Total Control ke user Standard) ada di spec `TC-FA-RP-E2E-319-assign-total-control-dan-read-only-menulis-baris-pola-group-role`.
- Temuan untuk QA:
  - TC-FA-RP-1170 Precondition c menyebut Pre-setup #24, yang di Tabel Data Uji Pre-setup adalah `Company Changelog`, bukan data pengguna atau group; Budi Setiawan ada di Pre-setup #15. Spec mengikuti TC dan memakai Company Alpha (akun default suite) karena TC tidak menyebut client.
  - TC-FA-RP-1170 Expected d menyebut entri `Assign (via Read Only)` "per baris Role × Group" tanpa jumlah; spec tidak mengasersi jumlah entri tepat, hanya bahwa jumlah bertambah dari baseline dan entri `Assign (via Read Only)` ada.
  - TC-FA-RP-1170 Expected b menyebut Read "aktif terkunci saja (Delete tidak aktif; Create dan Update `—`)": spec memecahnya menjadi tiga `Verifikasi` (Read aktif terkunci, Delete tidak aktif, Create dan Update `—`).
  - TC-FA-RP-1170 langkah 5 tidak menyebut cara menuju Settings > User; spec memakai "Buka Settings > User lewat sidebar" (S-14).
