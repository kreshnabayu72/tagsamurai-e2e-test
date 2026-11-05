---
id: TC-FA-RP-E2E-260-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-3
title: "Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-865
  - TC-FA-RP-1035
coverage:
  web: automated
---

# Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (3/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Akun ganti: Kevin Susanto (Pre-setup #13, Group Manager di `Data Center`) pada TC-FA-RP-1035. Email dan password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun login disediakan tim FE.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #3 (Rina Wulandari, Total Control kedua; seluruh Global Role CRUD penuh) dan #15 (Budi Santoso memegang `Manage Open API`) untuk TC-FA-RP-865; #13 (Kevin Susanto: Group Manager di `Data Center`; Group Role eksplisit seluruh capability CRUD penuh di `Data Center`; Group Role `Manage files` Read dan Delete di `Helpdesk`), #18 (pohon group Company Alpha), dan #19 (seed Role Transaksi pada `Data Center` dan `Rack A1`) untuk TC-FA-RP-1035.
- Kemampuan teknis: membaca jumlah notifikasi in-app akun Kevin Susanto sebelum aksi (baseline TC-FA-RP-1035 Expected d) disediakan tim FE/BE; tanpa endpoint karangan.
- Baseline audit trail (S-12): jumlah entri Changelog, System Log, dan Activity Log dicatat sebelum aksi lewat kemampuan baca yang disediakan tim FE/BE (UI atau fixture BE); asersi memakai selisih terhadap baseline, bukan angka absolut dan bukan posisi teratas.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-865: Bulk Remove menulis satu entri per baris berhasil dan Auto-Revert per user bertier

1. Catat baseline (aksi tanpa `Verifikasi`):
   - Detail Role `Manage Open API` > ikon Changelog di toolbar Detail Role: jumlah entri Action `Remove` untuk Rina Wulandari dan untuk Budi Santoso
   - Tab Total Control > ikon Changelog di toolbar: jumlah entri Action `Auto-Revert` untuk Rina Wulandari
2. Buka Tab System, lalu Detail Role `Manage Open API`
3. Centang baris Rina Wulandari dan Budi Santoso, klik `Bulk Action` > `Remove` lalu `[Remove]`
4. Tunggu aksi selesai: dialog tertutup
5. Klik ikon Changelog di toolbar Detail Role
6. Verifikasi modal memuat satu entri `Remove` baru untuk Rina Wulandari
7. Verifikasi modal memuat satu entri `Remove` baru untuk Budi Santoso
8. Tutup modal, lalu buka Tab Total Control
9. Klik ikon Changelog di toolbar Tab Total Control
10. Verifikasi Changelog Tab Total Control memuat satu entri `Auto-Revert` Total Control baru untuk Rina Wulandari (selisih satu terhadap baseline)

### TC-FA-RP-1035: Remove Group Manager yang menghapus baris pola GM: satu entri Remove (via Group Manager) per baris Group Role dan Role Transaksi di surface log yang berlaku, tanpa notifikasi tambahan

11. Catat baseline (aksi tanpa `Verifikasi`):
   - Tab Group Manager > ikon Changelog di toolbar: jumlah entri Action `Remove` Object `Group Manager` untuk Kevin Susanto di `Data Center`
   - Detail Role `Manage files` > `All Groups` > ikon Changelog di toolbar Detail Role: jumlah entri Action `Remove (via Group Manager)` untuk Kevin Susanto
   - Tab Transaction Role > node `Data Center` sub-tab `Disposal` > ikon Changelog pada baris sub-tab: jumlah entri Action `Remove (via Group Manager)` untuk Kevin Susanto
   - Settings > User > Detail Kevin Susanto > Changelog: User > Group Role dan Transaction Role: jumlah entri Action `Remove (via Group Manager)` pada tiap sub-tab
   - Settings > User > Detail Siti Rahmawati > Tab System Log: jumlah entri Action `Remove (via Group Manager)`
   - Activity Log FAMS (menu Activity Log): jumlah entri Action `Remove (via Group Manager)`
   - Jumlah notifikasi in-app akun Kevin Susanto
12. Buka Fixed Asset > Settings > Role & Permission > Tab Group Manager
13. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`, klik `[Remove]`
14. Tunggu aksi selesai: dialog tertutup
15. Klik ikon Changelog di toolbar Tab Group Manager
16. Verifikasi entri baru `Remove` Object `Group Manager` untuk `Kevin Susanto — Data Center` tercatat
17. Buka Tab System, Detail Role `Manage files`, lalu klik node `All Groups`
18. Klik ikon Changelog di toolbar Detail Role
19. Verifikasi Changelog Detail Role memuat satu entri baru `Remove (via Group Manager)` per baris pola Group Role Kevin Susanto di `Data Center` dan `Rack A1`, Object `Manage files — Kevin Susanto — Data Center`, Field `Access`, Old Value `Assigned`, New Value `—`, Modified By `Siti R`
20. Buka Tab Transaction Role, klik node `Data Center` lalu sub-tab `Disposal`
21. Klik ikon Changelog pada baris sub-tab `Disposal`
22. Verifikasi Changelog memuat satu entri baru `Remove (via Group Manager)` per baris pola Role Transaksi Kevin Susanto, Field `Asset Admin — Data Center` dan `Approver — Data Center` (juga `Rack A1`), Old Value `Kevin Susanto`, New Value `—`
23. Buka Settings > User > Detail Kevin Susanto > Changelog: User > Group Role
24. Verifikasi Changelog: User > Group Role memuat entri baru `Remove (via Group Manager)` yang sama per baris pola Group Role
25. Klik sub-tab Transaction Role pada Changelog: User
26. Verifikasi Changelog: User > Transaction Role memuat entri baru `Remove (via Group Manager)` yang sama per baris pola Role Transaksi
27. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
28. Verifikasi sedikitnya satu entri tampil di System Log
29. Verifikasi jumlah entri `Remove (via Group Manager)` di System Log sama dengan baseline (tidak ada entri per baris pola)
30. Buka Activity Log FAMS (menu Activity Log)
31. Verifikasi sedikitnya satu entri tampil di Activity Log
32. Verifikasi jumlah entri `Remove (via Group Manager)` di Activity Log sama dengan baseline (tidak ada entri per baris pola)
33. Ganti akun: logout dari Siti Rahmawati lalu login sebagai Kevin Susanto
34. Buka Overlay Notifikasi lonceng navbar
35. Verifikasi notifikasi baru `You are no longer Group Manager for Data Center` tampil
36. Verifikasi jumlah notifikasi baru akun Kevin Susanto terhadap baseline hanya satu (tidak ada notifikasi untuk baris pola)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 36 langkah. Di atas 35 langkah karena blok TC-FA-RP-1035 memuat baseline dan satu Verifikasi per permukaan log (Changelog Group Role dan Transaction Role, System Log, Activity Log) serta notifikasi; tidak ada pengulangan yang dapat diringkas. Melewati 35 karena blok TC-FA-RP-1035 memuat baseline dan satu Verifikasi per permukaan log (Changelog Group Role dan Transaction Role, System Log, Activity Log) serta notifikasi; tidak ada pengulangan yang dapat diringkas.
- Urutan blok: TC-FA-RP-865 (Bulk Remove, mencabut Total Control Rina Wulandari) lalu TC-FA-RP-1035 (Remove Group Manager); ganti akun ke Kevin Susanto memakai Step eksplisit pada akhir spec (S-07). Hook `after` mengembalikan sesi ke akun default suite dan memulihkan Pre-setup (Rina Wulandari, Budi Santoso, Kevin Susanto).
- Langkah penghubung (S-03): pencatatan baseline, pembukaan tab dan Detail Role, "Tunggu aksi selesai". Akun aktor pertama sudah login di hook `before` (S-07).
- Asersi "System Log dan Activity Log tidak memuat entri per baris pola" (TC-FA-RP-1035 butir e) ditulis sebagai kesamaan jumlah terhadap baseline dengan anchor positif (langkah 28 dan 31; bagian 8b butir 2). Asersi "tidak ada notifikasi untuk baris pola" (TC-FA-RP-1035) ditulis sebagai kesamaan jumlah terhadap baseline pada aksi yang sukses, segera sesudah pembukaan Overlay Notifikasi (bagian 8b butir 11); bukan kelas absence.
- Temuan untuk QA:
  - Akun login Kevin Susanto (TC-FA-RP-1035) tidak tertulis di Pre-setup TC (Pre-setup #13 hanya data target); email dan password disediakan tim FE.
  - TC-FA-RP-865 merujuk Pre-setup #24 (Company Changelog) di Precondition; spec berjalan di Company Alpha dengan baseline selisih. Budi Santoso memegang `Manage Open API` hanya tertulis eksplisit pada #39; spec men-seed penugasan itu. TC-FA-RP-865 tanpa Post Condition.
  - TC-FA-RP-1035 Expected b dan c menyebut satu entri `Remove (via Group Manager)` per baris pola tanpa jumlah baris pola; spec tidak menghitung angka absolut dan mengasersi satu entri per baris yang terhapus. Pre-setup #19 hanya dirujuk TC untuk Role Transaksi `Asset Admin` dan `Approver` Kevin Susanto di `Data Center` dan `Rack A1`; seed baris pola itu perlu dikonfirmasi tim FE/BE. Expected d menyebut "entri yang sama tampil per baris di Changelog: User" tanpa memisah sub-tab; spec memeriksa sub-tab Group Role dan Transaction Role (langkah 24 dan 26). Expected e (System Log dan Activity Log) tidak menyebut surface lain; diasersi sebagai kesamaan jumlah entri `Remove (via Group Manager)` terhadap baseline. TC-FA-RP-1035 tanpa Post Condition.
