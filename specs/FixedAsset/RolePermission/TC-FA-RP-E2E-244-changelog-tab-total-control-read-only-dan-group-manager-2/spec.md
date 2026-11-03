---
id: TC-FA-RP-E2E-244-changelog-tab-total-control-read-only-dan-group-manager-2
title: "Changelog Tab Total Control, Read Only, dan Group Manager (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-802
  - TC-FA-RP-803
  - TC-FA-RP-804
  - TC-FA-RP-805
coverage:
  web: automated
---

# Changelog Tab Total Control, Read Only, dan Group Manager (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #13 (target Group Manager Kevin Susanto: Group Manager di `Data Center`), #18 (pohon group), #24 (`Company Changelog`), #43 (seed Group Manager: Fajar Nugroho, Kevin Susanto, dan Lina Marlina). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca modal Changelog lewat UI; waktu aksi dicatat sesudah aksi pemicu. Pemulihan penugasan Kevin Susanto (Group Manager di `Data Center`, serta `Helpdesk` bagi TC-FA-RP-804) dan group `Data Center` lewat seeding API antar blok TC (kemampuan disediakan tim FE/BE).
- State yang diubah dan pemulihannya: Penugasan Group Manager Kevin Susanto, Group Role Kevin Susanto pada `Manage group`, dan group `Data Center` diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-802: Changelog Tab Group Manager: Remove

1. Klik Tab `Group Manager`
2. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`
3. Klik `[Remove]`, catat waktu sesudah `[Remove]`
4. Tunggu aksi selesai: dialog Remove tertutup dan baris pengguna tidak lagi tampil di tabel
5. Klik ikon Changelog di toolbar Tab `Group Manager`
6. Verifikasi Modal `Changelog: Role & Permission > Group Manager` memuat entri terbaru: Action `Remove`; User Name — Group Name `Kevin Susanto — Data Center`; Field `Group Manager`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
7. Tutup modal Changelog

### TC-FA-RP-803: Changelog Tab Group Manager: Auto-Revert

8. Pulihkan penugasan Group Manager Kevin Susanto di `Data Center` lewat seeding API, hingga tersimpan
9. Klik Tab `System` lalu buka Detail Role `Manage group`
10. Pilih node `Data Center`
11. Hapus centang Delete pada baris Kevin Susanto
12. Klik `[Remove]`, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
13. Klik segmen `System` pada Breadcrumb lalu klik Tab `Group Manager`
14. Klik ikon Changelog di toolbar Tab `Group Manager`
15. Verifikasi Modal `Changelog: Role & Permission > Group Manager` memuat entri terbaru: Action `Auto-Revert`; User Name — Group Name `Kevin Susanto — Data Center`; Field `Group Manager`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
16. Tutup modal Changelog

### TC-FA-RP-804: Changelog Tab Group Manager: pelepasan GM saat Assign Total Control dicatat Remove per group

17. Pulihkan penugasan Group Manager Kevin Susanto di `Data Center` dan `Helpdesk` lewat seeding API, hingga tersimpan
18. Klik Tab `Total Control`
19. Klik `[+ Assign]` di Tab `Total Control`
20. Centang Kevin Susanto lalu klik `[Assign]`, catat waktu sesudah `[Assign]`
21. Tunggu aksi selesai: popup Assign tertutup dan baris pengguna yang di-assign tampil di tabel
22. Klik Tab `Group Manager`
23. Klik ikon Changelog di toolbar Tab `Group Manager`
24. Verifikasi Modal `Changelog: Role & Permission > Group Manager` memuat entri terbaru: Action `Remove`; User Name — Group Name `Kevin Susanto — Data Center`; Field `Group Manager`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
25. Verifikasi Modal memuat entri baru kedua: Action `Remove`; User Name — Group Name `Kevin Susanto — Helpdesk`; Field `Group Manager`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
26. Tutup modal Changelog

### TC-FA-RP-805: Changelog Tab Group Manager: Remove (Group Deleted) saat group dihapus

27. Pulihkan Kevin Susanto ke Pre-setup #43 (bukan Total Control, Group Manager di `Data Center`) lewat seeding API, hingga tersimpan
28. Buka Settings > Groups
29. Hapus group `Data Center` (konfirmasi dialog `Delete Group`), catat waktu sesudah konfirmasi, lalu tunggu aksi selesai
30. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Group Manager`
31. Klik ikon Changelog di toolbar Tab `Group Manager`
32. Verifikasi Modal memuat entri terbaru: Action `Remove (Group Deleted)`; User Name — Group Name `Kevin Susanto — Data Center`; Field `Group Manager`; Old Value `Assigned`; New Value `—`; Modified By `Siti R` (admin yang menghapus Group); Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
33. Tutup modal Changelog
34. Pulihkan group `Data Center` lewat seeding API, hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 34 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 4, 7, 9, 13, 16, 18, 21, 26, 28, 30, 33. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 8, 17, 27, 34; tidak ada `Verifikasi`.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- Urutan TC: TC-FA-RP-802, 803, 804, 805 (urutan nomor); pemulihan Kevin Susanto antar blok lewat seeding API karena tiap TC mengonsumsi penugasan Group Manager yang sama.
- TC-FA-RP-794 sampai TC-FA-RP-801 ada di spec 243 dan spec 314.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-804 precondition d menyebut Kevin Susanto Group Manager di `Data Center` dan `Helpdesk`; Pre-setup #38 memuat keduanya, Pre-setup #43 hanya `Data Center`; spec memenuhinya lewat seeding API.
  - TC-FA-RP-805 Expected menyebut Modified By `Siti R` "admin yang menghapus Group" tanpa menyebut akun penghapus; spec menghapus group lewat sesi UI aktor (Siti Rahmawati).
  - TC-FA-RP-804 Expected "entri terbaru ... dan entri terbaru ..." tidak menyebut urutan kedua entri; spec tidak mengasersi urutannya.
  - Post Condition TC-FA-RP-805 (pemulihan group) tidak punya langkah observasi dan tidak diasersi.
