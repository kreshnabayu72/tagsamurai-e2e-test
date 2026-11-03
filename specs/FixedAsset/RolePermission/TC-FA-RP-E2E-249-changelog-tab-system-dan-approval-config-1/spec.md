---
id: TC-FA-RP-E2E-249-changelog-tab-system-dan-approval-config-1
title: "Changelog Tab System dan Approval Config (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-820
  - TC-FA-RP-821
  - TC-FA-RP-822
  - TC-FA-RP-823
  - TC-FA-RP-824
coverage:
  web: automated
---

# Changelog Tab System dan Approval Config (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #15 (kolam pengguna Standard: Budi Santoso), #18 (pohon group), #19 (seed Role Transaksi: Require Approval OFF di semua node), #20 (seed approval Transfer pada `IT Infrastructure`: Require Approval ON, Approver Pandu Wijaya, aturan OR, Approval Scope `Both`), #24 (`Company Changelog`), #39 (Detail Role `Manage files` dan `Manage Open API`). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca modal Changelog lewat UI; waktu aksi dicatat sesudah aksi pemicu. Precondition TC-FA-RP-824 (Approval Rule `Transfer` pada `IT Infrastructure` bernilai AND) dipenuhi oleh hasil TC-FA-RP-823.
- State yang diubah dan pemulihannya: Penugasan Budi Santoso pada `Manage Open API` dan `Manage files`, toggle Require Approval `Disposal` dan `Transfer`, serta Approval Rule `Transfer` pada `IT Infrastructure` diubah spec ini; dipulihkan ke Pre-setup #19 dan #20 di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-820: Changelog Tab System adalah superset lintas role dengan label kolom `Role — User`

1. Klik Tab `System` lalu buka Detail Role `Manage Open API`
2. Klik `[+ Assign]`
3. Centang Budi Santoso lalu klik `[Assign]`, lalu tunggu aksi selesai
4. Klik segmen `System` pada Breadcrumb lalu buka Detail Role `Manage files`
5. Pilih node `Data Center`
6. Klik `[+ Assign]`
7. Centang Budi Santoso lalu klik `[Assign]`, lalu tunggu aksi selesai
8. Klik segmen `System` pada Breadcrumb
9. Klik ikon Changelog di toolbar Tab `System`
10. Verifikasi Modal `Changelog: Role & Permission > System` memuat entri `Assign` `Manage Open API — Budi Santoso`
11. Verifikasi Modal yang sama memuat entri `Assign` `Manage files — Budi Santoso — Data Center`
12. Verifikasi kolom Object berlabel `Role — User`
13. Tutup modal Changelog

### TC-FA-RP-821: Changelog Approval Config: Require Approval Off ke On

14. Klik Tab `Transaction Role`
15. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
16. Aktifkan toggle `Require Approval for Disposal`, catat waktu sesudahnya
17. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
18. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Disposal` terbuka tanpa kolom Object
19. Verifikasi Modal memuat entri terbaru: Action `Edit`; Field `Require Approval — IT Infrastructure`; Old Value `Off`; New Value `On`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
20. Tutup modal Changelog

### TC-FA-RP-823: Changelog Approval Config: Approval Rule OR ke AND

21. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
22. Pilih radio `All approvers (AND)`, catat waktu sesudahnya
23. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
24. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Approval Rule — IT Infrastructure`; Old Value `OR`; New Value `AND`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
25. Tutup modal Changelog

### TC-FA-RP-824: Changelog Approval Config: Approval Rule AND ke OR

26. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
27. Pilih radio `Any approver (OR)`, catat waktu sesudahnya
28. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
29. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Approval Rule — IT Infrastructure`; Old Value `AND`; New Value `OR`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
30. Tutup modal Changelog

### TC-FA-RP-822: Changelog Approval Config: Require Approval On ke Off

31. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
32. Matikan toggle `Require Approval for Transfer`, catat waktu sesudahnya
33. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
34. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Require Approval — IT Infrastructure`; Old Value `On`; New Value `Off`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
35. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 35 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 4, 13, 14, 20, 25, 30, 35. Akun aktor pertama sudah login di hook `before` (S-07).
- Urutan TC: TC-FA-RP-820, 821, 823, 824, 822 (TC-FA-RP-822 terakhir): TC-FA-RP-822 mematikan Require Approval `Transfer`, sedangkan TC-FA-RP-823 dan TC-FA-RP-824 membutuhkan Require Approval `Transfer` ON dan hasil TC-FA-RP-823 menjadi precondition TC-FA-RP-824.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- TC-FA-RP-825 sampai TC-FA-RP-829 ada di spec 250.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-820 langkah 1 "Lakukan kedua Assign di Detail Role masing-masing" tidak merinci langkah Assign; spec menuliskannya sebagai langkah eksplisit di kedua Detail Role.
  - TC-FA-RP-821 mensyaratkan Approver pada `Disposal` di `IT Infrastructure` (Pre-setup #19: Pandu Wijaya) agar toggle dapat diaktifkan; TC tidak menyebut prasyarat itu.
