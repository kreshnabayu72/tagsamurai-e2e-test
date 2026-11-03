---
id: TC-FA-RP-E2E-315-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-4
title: "Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (4/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-861
  - TC-FA-RP-863
  - TC-FA-RP-864
  - TC-FA-RP-874
coverage:
  web: automated
---

# Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (4/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, tanpa tingkat akses), #18 (pohon group Company Alpha, termasuk `Data Center` dan `Helpdesk`), #19 (seed Role Transaksi Disposal pada `IT Infrastructure`), #3 (Rina Wulandari, Total Control kedua; seluruh Global Role CRUD penuh; TC-FA-RP-861), dan #39 (Detail Role `Manage files` terisi; Budi Santoso di `Helpdesk`; TC-FA-RP-874).
- Baseline audit trail (S-12): jumlah entri Changelog, System Log, dan Activity Log dicatat sebelum aksi lewat kemampuan baca yang disediakan tim FE/BE (UI atau fixture BE); asersi memakai selisih terhadap baseline, bukan angka absolut dan bukan posisi teratas.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Entri Assign Budi Santoso di `Helpdesk` (dasar asersi TC-FA-RP-874) dibuat spec ini lewat sesi API aktor (`suite.md` bagian "Hook suite") sebelum group dihapus, sehingga tidak bergantung pada riwayat tenant; TC-FA-RP-874 merujuk Pre-setup #24 di Precondition, sedangkan spec berjalan di Company Alpha.
- Pemulihan di hook `after`: Rina Wulandari dikembalikan sebagai Total Control kedua dan group `Helpdesk` beserta penugasannya dipulihkan (aturan pemulihan fixture destruktif pada Catatan TC).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-863: Assign Group Manager tercatat di Changelog: User

1. Pulihkan Ahmad Fauzi ke state Precondition (tanpa tingkat akses, tanpa Group Manager) lewat seeding API hingga tersimpan
2. Catat baseline (aksi tanpa `Verifikasi`): Settings > User > Detail Ahmad Fauzi > Changelog: User, jumlah entri Assign Group Manager untuk `Data Center`
3. Buka Fixed Asset > Settings > Role & Permission > Tab Group Manager
4. Klik `[+ Assign]` di Tab Group Manager
5. Pilih group `Data Center`, centang Ahmad Fauzi, klik `[Assign]`
6. Tunggu aksi selesai: popup tertutup
7. Buka Settings > User > Detail Ahmad Fauzi > Changelog: User
8. Verifikasi entri baru Assign Group Manager untuk `Data Center` tampil di Changelog: User (selisih terhadap baseline)

### TC-FA-RP-864: Assign Role Transaksi tercatat di Changelog: User > Transaction Role

9. Pulihkan Ahmad Fauzi ke state Precondition (tanpa tingkat akses, tanpa Group Manager, tanpa Role Transaksi) lewat seeding API hingga tersimpan
10. Catat baseline (aksi tanpa `Verifikasi`): Settings > User > Detail Ahmad Fauzi > Changelog: User > Transaction Role, jumlah entri Assign Transaction Role `Disposal` `Asset Admin` pada `IT Infrastructure`
11. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
12. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
13. Klik `[+ Assign]` pada section Asset Admin, centang Ahmad Fauzi, klik `[Assign]`
14. Tunggu aksi selesai: popup tertutup
15. Buka Settings > User > Detail Ahmad Fauzi > Changelog: User > Transaction Role
16. Verifikasi entri baru Assign Transaction Role `Disposal` `Asset Admin` pada `IT Infrastructure` tampil (selisih terhadap baseline)

### TC-FA-RP-861: Auto-Revert tercatat di Changelog: User terlepas origin edit

17. Catat baseline (aksi tanpa `Verifikasi`): Settings > User > Detail Rina Wulandari > Changelog: User, jumlah entri Action `Auto-Revert` Field `Access Level` dan jumlah entri Action `Edit` Field `Delete` untuk `Manage accounting`
18. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage accounting`
19. Hapus centang Delete pada baris Rina Wulandari lalu klik `[Remove]` pada dialog
20. Tunggu aksi selesai: perubahan tersimpan
21. Buka Settings > User > Detail Rina Wulandari > Changelog: User
22. Verifikasi entri baru Action `Auto-Revert` Field `Access Level` `Total Control` ke `—` tampil (selisih terhadap baseline)
23. Verifikasi entri baru Action `Edit` Field `Delete` pada Global Role `Manage accounting` tampil (selisih terhadap baseline)
24. Pulihkan Rina Wulandari sebagai Total Control kedua dengan seluruh Global Role CRUD penuh lewat seeding API hingga tersimpan

### TC-FA-RP-874: Entri log menyimpan nama group saat itu setelah group dihapus

25. Lepas penugasan Budi Santoso di `Helpdesk` pada Group Role `Manage files` lalu tetapkan ulang lewat sesi API aktor (Siti Rahmawati), hingga tersimpan, sehingga entri Assign Budi Santoso untuk `Helpdesk` tercatat sebelum group dihapus
26. Catat baseline (aksi tanpa `Verifikasi`): Detail Role `Manage files` > ikon Changelog di toolbar Detail Role, jumlah entri Action `Remove (Group Deleted)` untuk `Helpdesk`
27. Hapus group `Helpdesk` di Settings > Groups
28. Tunggu aksi selesai: group terhapus
29. Buka Tab System, lalu Detail Role `Manage files`
30. Klik ikon Changelog di toolbar Detail Role
31. Verifikasi entri Assign Budi Santoso yang dibuat pada langkah penugasan ulang sebelum group dihapus tetap menyebut `Helpdesk`
32. Verifikasi entri baru `Remove (Group Deleted)` tampil (selisih terhadap baseline)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 32 langkah.
- Urutan blok: TC-FA-RP-863, 864, 861, 874 menaruh aksi yang mencabut atau menghapus data di akhir (S-10); TC-FA-RP-874 (hapus group) terakhir. Pemulihan Rina Wulandari dan group `Helpdesk` dilakukan hook `after`.
- Langkah penghubung (S-03): pencatatan baseline, pemulihan Ahmad Fauzi lewat seeding API di antara blok TC, pembukaan tab dan Detail Role, "Tunggu aksi selesai", dan pemulihan lewat seeding API. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding lewat sesi API aktor (S-04, S-09): langkah 25 membuat entri Assign Budi Santoso untuk `Helpdesk` sebelum group dihapus; tanpa `Verifikasi`. Entri itulah yang diasersi tetap menyebut `Helpdesk` pada langkah 31.
- Temuan untuk QA:
  - TC-FA-RP-863 dan 864 tidak menyebut Modified By; spec tidak mengasersinya. TC-FA-RP-874 tidak menyebut Modified By dan tidak merinci Post Condition pemulihan group selain rujukan ke Catatan TC (ditangani hook `after`).
  - TC-FA-RP-861 Expected menempatkan entri `Edit` Delete di Changelog: User tanpa menyebut sub-tab (Global Role); spec membaca aggregate sesuai TC.
  - TC-FA-RP-874 merujuk Pre-setup #24 (Company Changelog) di Precondition; spec berjalan di Company Alpha dengan baseline selisih. Post Condition TC-FA-RP-861, 863, dan 864 kosong; tidak ada yang diasersi.
