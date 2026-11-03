---
id: TC-FA-RP-E2E-294-absence-log-aksi-ditolak-karena-state-tenant-2
title: "Absence log: aksi ditolak karena state tenant (2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-979
  - TC-FA-RP-980
  - TC-FA-RP-981
  - TC-FA-RP-982
coverage:
  web: automated
---

# Absence log: aksi ditolak karena state tenant (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Client Suspended` (Pre-setup #25), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_SUSPENDED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Env var yang dipakai: `FA_SUSPENDED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #25 (`Client Suspended`), #20 (sub-tab `Transfer` pada `IT Infrastructure` dengan Require Approval On, Approver Pandu Wijaya, aturan OR, Approval Scope `Both`), #39 (Detail Role `Manage Open API` terisi dengan Dimas Pranata dan Citra Lestari), #15 (Ahmad Fauzi), #18, dan #19 (Require Approval Off di semua node). Disiapkan lewat seeding di hook `before`.
- Kemampuan teknis: kemampuan baca jumlah entri (disediakan tim FE/BE, tanpa endpoint karangan, bagian 8b butir 10) untuk Changelog surface terkait, System Log aktor, dan Activity Log; baseline dicatat per TC sebelum aksi pemicu dan asersi memakai perbandingan dengan baseline, bukan angka absolut (S-12).
- State global: status `Client Suspended` tidak diubah; spec tidak mengubah data karena semua aksi ditolak.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-979: Client Suspended menolak Bulk Remove, tidak ada entri log

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Catat baseline jumlah entri Changelog Detail Role `Manage Open API`, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
3. Centang baris Dimas Pranata dan Citra Lestari
4. Klik `Bulk Action` > `Remove`
5. Klik `[Remove]`
6. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
7. Verifikasi jumlah entri Changelog Detail Role `Manage Open API`, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)
8. Klik `[Cancel]` pada dialog Bulk Remove

### TC-FA-RP-980: Client Suspended menolak Toggle Require Approval, tidak ada entri log

9. Tunggu toast lama hilang otomatis
10. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
11. Catat baseline jumlah entri Changelog Transaction Role, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
12. Aktifkan toggle
13. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
14. Verifikasi jumlah entri Changelog Transaction Role, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-981: Client Suspended menolak Radio aturan persetujuan, tidak ada entri log

15. Tunggu toast lama hilang otomatis
16. Klik sub-tab `Transfer` pada node `IT Infrastructure`
17. Catat baseline jumlah entri Changelog Transaction Role, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
18. Pilih radio `All approvers (AND)`
19. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
20. Verifikasi jumlah entri Changelog Transaction Role, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)

### TC-FA-RP-982: Client Suspended menolak Assign Role Transaksi, tidak ada entri log

21. Tunggu toast lama hilang otomatis
22. Klik sub-tab `Disposal` pada node `IT Infrastructure`
23. Catat baseline jumlah entri Changelog Transaction Role, System Log aktor, dan Activity Log lewat kemampuan baca jumlah entri
24. Klik `[+ Assign]` pada section Asset Admin
25. Centang Ahmad Fauzi
26. Klik `[Assign]`
27. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
28. Verifikasi jumlah entri Changelog Transaction Role, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri log baru)
29. Klik `[Cancel]` pada popup Assign

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-979 sampai TC-FA-RP-982).
- Kelas g (absence log): tiap TC punya aksi pemicu nyata, baseline sendiri (S-12), dan anchor positif sebelum asersi absence (bagian 8b butir 2). Pemicu berkelas lain (state tenant, permintaan langsung, dua sesi) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (`P-5` butir a). Anchor positif tiap blok adalah toast penolakan `Changes can't be saved while this workspace is suspended or expired.`.
- Pembagian TC lintas spec: klausa "tidak ada entri log" pada Expected c TC-FA-RP-979 sampai TC-FA-RP-982 diasersi di spec ini dengan aksi nyata dan baseline sendiri; klausa toast, state kontrol, dan tidak ada perubahan data diasersi di spec 279. Id TC tetap di `sourceTc` spec asal dan spec ini (S-05).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): pencatatan baseline jumlah entri; "Tunggu toast lama hilang otomatis" sebelum tiap toast baku yang sama diasersi lagi (R-12); membuka tab, Detail Role, node, dan sub-tab; mencentang kandidat; menutup popup dan dialog dengan `[Cancel]` (S-09).
- Temuan untuk QA:
  - Akun Total Control pada `Client Suspended` tidak tertulis di Pre-setup #1 sampai #11; email dan password disediakan tim FE (S-11).
  - Expected c TC-FA-RP-979 sampai TC-FA-RP-982 menyebut "entri log" tanpa surface; spec membandingkan Changelog surface yang disentuh aksi, System Log aktor, dan Activity Log terhadap baseline.
  - TC tidak menyebut apakah popup atau dialog tetap terbuka setelah penolakan; spec menutupnya dengan `[Cancel]` mengikuti pola penolakan lain di TC.
