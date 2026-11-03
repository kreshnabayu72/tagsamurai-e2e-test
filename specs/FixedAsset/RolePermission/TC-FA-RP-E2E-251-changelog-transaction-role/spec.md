---
id: TC-FA-RP-E2E-251-changelog-transaction-role
title: "Changelog Transaction Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-830
  - TC-FA-RP-831
  - TC-FA-RP-832
  - TC-FA-RP-833
coverage:
  web: automated
---

# Changelog Transaction Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi), #18 (pohon group), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Monitoring & Report Oscar Pratama, Staff Putri Wulandari, Approver Pandu Wijaya), #24 (`Company Changelog`). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca modal Changelog lewat UI; waktu aksi dicatat sesudah aksi pemicu. Penghapusan group `IT Infrastructure` beserta subtree lewat UI Settings > Groups dan pemulihannya (group beserta Pre-setup #19) lewat seeding API (kemampuan disediakan tim FE/BE).
- State yang diubah dan pemulihannya: Penugasan Role Transaksi `Disposal` pada `IT Infrastructure` dan group `IT Infrastructure` beserta subtree diubah spec ini; dipulihkan ke Pre-setup #18 dan #19 di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-832: Changelog Transaction Role: Remove (Group Deleted)

1. Buka Settings > Groups
2. Hapus group `IT Infrastructure` beserta subtree-nya (konfirmasi dialog `Delete Group`), catat waktu sesudah konfirmasi, lalu tunggu aksi selesai
3. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
4. Klik sub-tab `Disposal`
5. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
6. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Disposal` memuat entri terbaru: Action `Remove (Group Deleted)`; Field `Asset Admin — IT Infrastructure`; Old Value `Nadia Putri`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
7. Tutup modal Changelog
8. Pulihkan group `IT Infrastructure` beserta subtree dan Pre-setup #19 lewat seeding API, hingga tersimpan

### TC-FA-RP-830: Changelog Transaction Role: Assign Role Transaksi

9. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
10. Klik `[+ Assign]` pada section Asset Admin
11. Centang Ahmad Fauzi lalu klik `[Assign]`, catat waktu sesudah `[Assign]`
12. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
13. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Disposal` memuat entri terbaru: Action `Assign`; Field `Asset Admin — IT Infrastructure`; Old Value `—`; New Value `Ahmad Fauzi`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
14. Tutup modal Changelog

### TC-FA-RP-831: Changelog Transaction Role: Remove Role Transaksi

15. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
16. Klik `[⋯]` baris Putri Wulandari lalu `Remove`
17. Klik `[Remove]`, catat waktu sesudah `[Remove]`
18. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
19. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Disposal` memuat entri terbaru: Action `Remove`; Field `Staff — IT Infrastructure`; Old Value `Putri Wulandari`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
20. Tutup modal Changelog

### TC-FA-RP-833: Changelog Transaction Role: penggantian role karena naik tangga dicatat dua entri Remove lalu Assign

21. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
22. Klik `[+ Assign]` pada section Asset Admin
23. Centang Oscar Pratama (Monitoring & Report) lalu klik `[Assign]`, catat waktu sesudah `[Assign]`
24. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
25. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Disposal` memuat entri `Remove` untuk Oscar Pratama: Field `Monitoring & Report — IT Infrastructure`; Old Value `Oscar Pratama`; New Value `—`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
26. Verifikasi Modal memuat entri `Assign` berikutnya untuk Oscar Pratama: Field `Asset Admin — IT Infrastructure`; Old Value `—`; New Value `Oscar Pratama`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
27. Verifikasi Modal tidak memuat entri `Edit` untuk Oscar Pratama pada waktu aksi
28. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 28 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 3, 7, 14, 20, 28. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 8; tidak ada `Verifikasi`.
- Urutan TC: TC-FA-RP-832, 830, 831, 833 (TC-FA-RP-832 lebih dulu): TC-FA-RP-832 mengasersi Old Value `Nadia Putri` pada Asset Admin Pre-setup #19, sehingga dijalankan sebelum TC-FA-RP-830 dan TC-FA-RP-833 menambah penugasan Asset Admin; group dan Pre-setup #19 dipulihkan lewat seeding API sesudah TC-FA-RP-832.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- Asersi absence `Edit` pada TC-FA-RP-833 didahului entri `Remove` dan `Assign` pada modal yang sama (butir 8b.2).
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-832 Expected menyebut Old Value `Nadia Putri` pada Field `Asset Admin`; Role Transaksi bisa berisi lebih dari satu pemegang Asset Admin (Pre-setup #40 menyebut tiga), sehingga TC tidak menentukan entri mana yang "terbaru"; spec memakai Pre-setup #19 (Nadia Putri satu-satunya Asset Admin) dan menjalankan TC ini lebih dulu.
  - TC-FA-RP-832 dan 833 tidak menyebut judul section untuk Oscar Pratama selain `Monitoring & Report`; spec mengikuti Field TC.
  - Post Condition TC-FA-RP-832 (pemulihan group) tidak punya langkah observasi dan tidak diasersi.
