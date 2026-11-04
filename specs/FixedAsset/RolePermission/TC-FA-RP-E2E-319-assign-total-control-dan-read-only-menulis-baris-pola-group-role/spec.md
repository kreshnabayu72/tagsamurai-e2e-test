---
id: TC-FA-RP-E2E-319-assign-total-control-dan-read-only-menulis-baris-pola-group-role
title: "Assign Total Control ke user Standard menulis baris pola Group Role pada semua group dengan CRUD penuh sesuai kolom berlaku"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1169
coverage:
  web: automated
---

# Assign Total Control ke user Standard menulis baris pola Group Role pada semua group dengan CRUD penuh sesuai kolom berlaku

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (kolam pengguna Standard; Budi Setiawan sebagai target), #18 (pohon group dengan tujuh group: `Head Office`, `IT Infrastructure`, `Data Center`, `Rack A1`, `Helpdesk`, `Logistics Warehouse`, `Dock 1`), #24 (disebut Precondition TC; lihat Temuan untuk QA).
- Precondition TC (dipakai sebagai precondition, tidak diasersi): Budi Setiawan berstatus Standard tanpa penugasan Group Role, disiapkan lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Baseline: nilai kolom Users tiap baris Group Role di Tab System dicatat sebelum `[Assign]` (langkah 2) untuk asersi selisih bertambah 1.
- Pemulihan: Budi Setiawan dipulihkan ke state seed Standard (tanpa baris pola Group Role) di hook `after` (kemampuan disediakan tim FE/BE). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1169: Assign Total Control ke user Standard menulis baris pola Group Role pada semua group dengan CRUD penuh sesuai kolom berlaku

1. Klik Tab `System`
2. Catat nilai kolom Users tiap baris Group Role sebagai baseline
3. Klik Tab `Total Control`
4. Klik `[+ Assign]` di Tab Total Control
5. Centang Budi Setiawan
6. Klik `[Assign]`
7. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
8. Buka Tab System lalu Detail Role Group Role `Manage files`
9. Klik `All Groups`
10. Ketik Search `Budi Setiawan`, tekan Enter
11. Verifikasi baris Budi Setiawan tampil pada setiap group di pohon Pre-setup #18
12. Verifikasi baris Budi Setiawan pada setiap group: Read dan Delete aktif
13. Verifikasi Read baris Budi Setiawan terkunci
14. Verifikasi baris Budi Setiawan pada setiap group: Create dan Update menampilkan `—`
15. Buka Tab System lalu Detail Role `Manage asset license`
16. Klik `All Groups`
17. Ketik Search `Budi Setiawan`, tekan Enter
18. Verifikasi baris Budi Setiawan tampil pada setiap group di pohon Pre-setup #18
19. Verifikasi baris Budi Setiawan pada setiap group: Read dan Update aktif
20. Verifikasi baris Budi Setiawan pada setiap group: Create dan Delete menampilkan `—`
21. Buka Tab System lalu Detail Role `Manage asset & TAG`
22. Klik node `Dock 1`
23. Ketik Search `Budi Setiawan`, tekan Enter
24. Verifikasi baris Budi Setiawan tampil di `Dock 1`
25. Verifikasi baris Budi Setiawan di `Dock 1`: Create, Read, Update, dan Delete aktif
26. Buka Tab System
27. Verifikasi kolom Users tiap baris Group Role selain `Manage user & role` bertambah 1 dari baseline langkah 2 (dihitung per user, bukan per group)
28. Verifikasi kolom Users baris `Manage user & role` tidak berubah dari baseline langkah 2 (dikecualikan dari pola, `FARP-LOGIC-24`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 28 langkah.
- Langkah penghubung (S-03): langkah 1 dan 2 (pencatatan baseline), 3, 8, 9, 15, 16, 21, 22, 26 (pindah tab, Detail Role, dan node). Akun aktor pertama sudah login di hook `before` (S-07).
- Search untuk menemukan baris target (R-16): langkah 10, 17, 23. Search tidak dibersihkan antar Detail Role karena tiap Detail Role dibuka dari Tab System sebagai halaman baru; langkah 11, 18, dan 24 membuktikan sedikitnya satu baris hasil Search tampil sebelum asersi "pada setiap group" (8b.2).
- Pembagian TC lintas spec: TC-FA-RP-1170 (Assign Read Only ke user Standard) ada di spec `TC-FA-RP-E2E-338-assign-read-only-menulis-baris-pola-group-role-dan-changelog-user`.
- Post Condition TC-FA-RP-1169 (entri `Assign (via Total Control)` per baris tanpa notifikasi per baris, lihat TC-FA-RP-860) tidak punya langkah observasi di TC dan tidak diasersi; pencatatan lintas surface diasersi di spec `TC-FA-RP-E2E-258-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-1`.
- Temuan untuk QA:
  - TC-FA-RP-1169 Precondition c menyebut Pre-setup #24, yang di Tabel Data Uji Pre-setup adalah `Company Changelog` (log 25 entri campuran), bukan data pengguna atau group; Budi Setiawan ada di Pre-setup #15. Spec mengikuti TC dan memakai Company Alpha (akun default suite) karena TC tidak menyebut client; Changelog tidak diasersi di spec ini.
  - TC-FA-RP-1169 Expected b dan c menyebut "setiap group" tanpa daftar; spec mengasersi baris pada Detail Role dengan `All Groups` untuk tujuh group Pre-setup #18.
  - TC-FA-RP-1169 Expected d menyebut Create, Read, Update, Delete aktif di `Dock 1` untuk `Manage asset & TAG`, sementara Expected b dan c untuk role lain menyebut kolom berlaku berbeda per role; spec mengikuti TC per role.
  - TC-FA-RP-1169 Expected e tidak menyebut nilai baseline kolom Users; spec mencatat baseline sebelum `[Assign]` (kemampuan baca nilai UI).
