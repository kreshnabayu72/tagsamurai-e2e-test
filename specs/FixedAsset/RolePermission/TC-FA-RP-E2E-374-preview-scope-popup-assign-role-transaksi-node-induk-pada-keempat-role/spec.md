---
id: TC-FA-RP-E2E-374-preview-scope-popup-assign-role-transaksi-node-induk-pada-keempat-role
title: "Preview scope popup Assign Role Transaksi pada node induk menampilkan node terpilih beserta seluruh descendant pada keempat role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1205
coverage:
  web: automated
---

# Preview scope popup Assign Role Transaksi pada node induk menampilkan node terpilih beserta seluruh descendant pada keempat role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`; `Head Office` > `Logistics Warehouse` > `Dock 1`), #19 (penugasan Role Transaksi `IT Infrastructure` sub-tab `Disposal`), dan #15 (pool pengguna Standard, sumber kandidat picker).
- Data Dinamis: tidak ada data yang dibuat spec. Spec tidak menyimpan penugasan apa pun (tanpa klik `[Assign]`); tidak ada pemulihan yang dibutuhkan.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1205: preview scope popup Assign Role Transaksi pada node `IT Infrastructure`

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Catat baseline jumlah di header tiap section Asset Admin, Monitoring & Report, Staff, dan Approver (aksi tanpa `Verifikasi`)
3. Klik `[+ Assign]` pada section Asset Admin
4. Verifikasi preview scope popup Asset Admin menampilkan `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk`
5. Verifikasi preview scope popup Asset Admin tidak memuat `Head Office`, `Logistics Warehouse`, dan `Dock 1`
6. Tutup popup lewat `[×]`
7. Klik `[+ Assign]` pada section Monitoring & Report
8. Verifikasi preview scope popup Monitoring & Report menampilkan `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk`
9. Verifikasi preview scope popup Monitoring & Report tidak memuat `Head Office`, `Logistics Warehouse`, dan `Dock 1`
10. Tutup popup lewat `[×]`
11. Klik `[+ Assign]` pada section Staff
12. Verifikasi preview scope popup Staff menampilkan `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk`
13. Verifikasi preview scope popup Staff tidak memuat `Head Office`, `Logistics Warehouse`, dan `Dock 1`
14. Tutup popup lewat `[×]`
15. Klik `[+ Assign]` pada section Approver
16. Verifikasi preview scope popup Approver menampilkan `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk`
17. Verifikasi preview scope popup Approver tidak memuat `Head Office`, `Logistics Warehouse`, dan `Dock 1`
18. Tutup popup lewat `[×]` tanpa klik `[Assign]`
19. Verifikasi jumlah di header section Asset Admin, Monitoring & Report, Staff, dan Approver sama dengan baseline langkah 2 (tidak ada penugasan tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 19 langkah.
- Langkah penghubung (S-03): langkah 1 (navigasi Tab, node, sub-tab), langkah 2 (baseline jumlah header, S-12), langkah 3, 7, 11, dan 15 (membuka popup, bagian dari langkah TC 2 dan 3), dan langkah 6, 10, 14, serta 18 (menutup popup). Langkah 4, 8, 12, dan 16 menjadi anchor positif atas asersi absence langkah 5, 9, 13, dan 17 (bagian 8b butir 2).
- Pada langkah 19 yang diasersi hanyalah jumlah header section terhadap baseline; TC Expected c ("tidak menyimpan penugasan apa pun") tidak menyebut surface pengamatnya, maka dipilih jumlah header tiap section pada node `IT Infrastructure` sub-tab `Disposal`.
- Temuan untuk QA:
  - PRD tidak memuat literal judul maupun locator preview scope; TC hanya meng-assert daftar node. Asersi spec hanya atas daftar node (himpunan, tanpa urutan; urutan node pada preview tidak ditetapkan). Usulan locator untuk tim FE (belum ada di PRD): `~aria-label` `Preview Scope` pada popup dan satu elemen per node di dalamnya.
  - NC-19 / Open Item #8 (penugasan Role Transaksi mencakup node beserta descendant) belum dikonfirmasi PM; Expected 1205.a dan 1205.b ditulis sesuai TC. Bila PM mengubah cakupan, spec ini usang.
  - Pre-setup #19 menyatakan hitungan header pada `IT Infrastructure` sub-tab `Disposal` hanya berlaku tanpa seed Group Manager; spec memakai baseline yang dicatat saat dijalankan, bukan angka tetap.
