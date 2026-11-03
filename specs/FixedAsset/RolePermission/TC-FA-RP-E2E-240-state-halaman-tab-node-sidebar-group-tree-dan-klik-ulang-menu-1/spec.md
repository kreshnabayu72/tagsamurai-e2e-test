---
id: TC-FA-RP-E2E-240-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-1
title: "State halaman: tab, node Sidebar Group Tree, dan klik ulang menu (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-787
  - TC-FA-RP-788
  - TC-FA-RP-789
  - TC-FA-RP-790
coverage:
  web: automated
---

# State halaman: tab, node Sidebar Group Tree, dan klik ulang menu (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #15 (kolam pengguna Standard), #18 (pohon group), #19 (seed Role Transaksi), #36, #37, dan #38 (data Tab Total Control, Read Only, dan Group Manager), #43 (seed Group Manager). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Muat ulang halaman (F5) dan klik Breadcrumb; tidak ada pembacaan state backend.
- State yang diubah dan pemulihannya: Tidak ada state backend yang diubah; Search yang diketik hanya state UI.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-787: State Search tiap tab disimpan sendiri selama di halaman

1. Ketik Search `rina` di Tab `Total Control`, tekan Enter
2. Klik Tab `Read Only`
3. Ketik Search `dewi`, tekan Enter
4. Klik Tab `Total Control`
5. Verifikasi sedikitnya satu baris tampil di Tab `Total Control`
6. Verifikasi Tab `Total Control` masih tersaring `rina` (baris Rina Wulandari tampil)
7. Klik Tab `Read Only`
8. Verifikasi sedikitnya satu baris tampil di Tab `Read Only`
9. Verifikasi Tab `Read Only` masih tersaring `dewi` (baris Dewi Anggraini tampil)
10. Verifikasi Search satu tab tidak memengaruhi tab lain (Tab `Total Control` tetap `rina`, Tab `Read Only` tetap `dewi`)

### TC-FA-RP-788: Tab aktif dipertahankan setelah F5

11. Klik Tab `System`
12. Muat ulang halaman (F5)
13. Verifikasi Tab `System` tetap aktif
14. Verifikasi Breadcrumb `Settings > Role & Permission > System`

### TC-FA-RP-789: Node Sidebar Group Tree dipertahankan setelah F5 dan setelah Back dari Detail Role

15. Klik Tab `Group Manager`
16. Klik node `Data Center`
17. Muat ulang halaman (F5)
18. Verifikasi Tab `Group Manager` tetap aktif
19. Verifikasi node `Data Center` terpilih
20. Klik Tab `System`
21. Buka Detail Role `Manage files`
22. Klik segmen `System` pada Breadcrumb
23. Klik Tab `Group Manager`
24. Verifikasi Tab `Group Manager` masih memakai node `Data Center`

### TC-FA-RP-790: Node Sidebar Group Tree disimpan sendiri oleh Tab Group Manager dan Tab Transaction Role

25. Klik node `Data Center` pada Tab `Group Manager`
26. Klik Tab `Transaction Role`
27. Verifikasi Tab `Transaction Role` memulai pada node `All Groups`
28. Klik node `Helpdesk`
29. Klik Tab `Group Manager`
30. Verifikasi Tab `Group Manager` masih memakai node `Data Center`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 30 langkah.
- Temuan untuk QA:
  - TC-FA-RP-789 langkah 3 menyebut Back dari Detail Role lewat segmen `System` pada Breadcrumb; spec mengikuti Breadcrumb dan tidak memakai tombol Back browser.
  - TC-FA-RP-787 Expected a dan b menyebut tab "masih tersaring"; spec menulis pembanding baris tampil dan baris hasil yang disebut Pre-setup (Rina Wulandari, Dewi Anggraini) karena TC tidak merinci baris yang tampil.
