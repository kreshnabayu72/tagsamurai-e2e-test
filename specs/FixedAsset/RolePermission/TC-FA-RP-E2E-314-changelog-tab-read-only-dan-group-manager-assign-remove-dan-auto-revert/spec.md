---
id: TC-FA-RP-E2E-314-changelog-tab-read-only-dan-group-manager-assign-remove-dan-auto-revert
title: "Changelog Tab Read Only dan Group Manager: Assign, Remove, dan Auto-Revert"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-798
  - TC-FA-RP-799
  - TC-FA-RP-800
  - TC-FA-RP-801
coverage:
  web: automated
---

# Changelog Tab Read Only dan Group Manager: Assign, Remove, dan Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #12 (target Read Only Maya Anggraeni), #13 (target Group Manager Kevin Susanto), #15 (kolam pengguna Standard: Ahmad Fauzi), #18 (pohon group), #24 (`Company Changelog`), #43 (seed Group Manager). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca modal Changelog lewat UI; waktu aksi dicatat sesudah aksi pemicu. Pemulihan Maya Anggraeni ke Read Only dan Ahmad Fauzi ke tanpa tingkat akses antar blok TC lewat seeding API (kemampuan disediakan tim FE/BE).
- State yang diubah dan pemulihannya: Tingkat akses Ahmad Fauzi dan Maya Anggraeni serta penugasan Group Manager Ahmad Fauzi diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-798: Changelog Tab Read Only: Assign

1. Klik Tab `Read Only`
2. Klik `[+ Assign]` di Tab `Read Only`
3. Centang Ahmad Fauzi lalu klik `[Assign]`, catat waktu sesudah `[Assign]`
4. Tunggu aksi selesai: popup Assign tertutup dan baris pengguna yang di-assign tampil di tabel
5. Klik ikon Changelog di toolbar Tab `Read Only`
6. Verifikasi Modal `Changelog: Role & Permission > Read Only` memuat entri terbaru: Action `Assign`; User Name `Ahmad Fauzi`; Field `Access Level`; Old Value `—`; New Value `Read Only`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
7. Tutup modal Changelog

### TC-FA-RP-799: Changelog Tab Read Only: Remove

8. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`
9. Klik `[Remove]`, catat waktu sesudah `[Remove]`
10. Tunggu aksi selesai: dialog Remove tertutup dan baris pengguna tidak lagi tampil di tabel
11. Klik ikon Changelog di toolbar Tab `Read Only`
12. Verifikasi Modal memuat entri terbaru: Action `Remove`; User Name `Maya Anggraeni`; Field `Access Level`; Old Value `Read Only`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
13. Tutup modal Changelog

### TC-FA-RP-800: Changelog Tab Read Only: Auto-Revert

14. Pulihkan Maya Anggraeni ke Read Only lewat seeding API, hingga tersimpan
15. Klik Tab `System` lalu buka Detail Role `Manage accounting`
16. Centang Create pada baris Maya Anggraeni
17. Klik `[Remove]` pada dialog, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
18. Klik segmen `System` pada Breadcrumb lalu klik Tab `Read Only`
19. Klik ikon Changelog di toolbar Tab `Read Only`
20. Verifikasi Modal memuat entri terbaru: Action `Auto-Revert`; User Name `Maya Anggraeni`; Field `Access Level`; Old Value `Read Only`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
21. Tutup modal Changelog

### TC-FA-RP-801: Changelog Tab Group Manager: Assign

22. Pulihkan Ahmad Fauzi ke tanpa tingkat akses lewat seeding API, hingga tersimpan
23. Klik Tab `Group Manager`
24. Klik `[+ Assign]` di Tab `Group Manager`
25. Pilih group `Data Center`, centang Ahmad Fauzi, klik `[Assign]`, catat waktu sesudah `[Assign]`
26. Tunggu aksi selesai: popup Assign tertutup dan baris Ahmad Fauzi tampil di tabel Group Manager
27. Klik ikon Changelog di toolbar Tab `Group Manager`
28. Verifikasi Modal `Changelog: Role & Permission > Group Manager` memuat entri terbaru: Action `Assign`; User Name — Group Name `Ahmad Fauzi — Data Center`; Field `Group Manager`; Old Value `—`; New Value `Assigned`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
29. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 29 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 4, 7, 10, 13, 15, 18, 21, 23, 26, 29. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 14, 22; tidak ada `Verifikasi`.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- Urutan TC dalam spec: TC-FA-RP-798, 799, 800, 801 (urutan nomor); Maya Anggraeni dan Ahmad Fauzi dipulihkan lewat seeding API antar blok karena TC-FA-RP-799 dan TC-FA-RP-800 sama-sama membutuhkan Maya Anggraeni berstatus Read Only dan TC-FA-RP-801 membutuhkan Ahmad Fauzi tanpa tingkat akses.
- TC-FA-RP-794 sampai TC-FA-RP-797 ada di spec 243; TC-FA-RP-802 sampai TC-FA-RP-805 ada di spec 244.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-800 langkah 3 menyebut "Klik Tab Read Only" dari Detail Role tanpa menyebut cara kembali; spec menambah klik segmen `System` pada Breadcrumb sebagai langkah penghubung.
  - TC-FA-RP-799 dan TC-FA-RP-800 memakai Maya Anggraeni berstatus Read Only (Pre-setup #12) pada precondition masing-masing; hasil satu TC meniadakan precondition TC lain, sehingga pemulihan lewat seeding API wajib antar blok.
