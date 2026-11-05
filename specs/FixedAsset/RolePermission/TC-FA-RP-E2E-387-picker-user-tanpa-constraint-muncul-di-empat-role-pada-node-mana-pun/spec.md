---
id: TC-FA-RP-E2E-387-picker-user-tanpa-constraint-muncul-di-empat-role-pada-node-mana-pun
title: "Picker Role Transaksi: user tanpa constraint muncul di keempat role pada node mana pun"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1226
coverage:
  web: automated
---

# Picker Role Transaksi: user tanpa constraint muncul di keempat role pada node mana pun

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Indra Kusuma, tanpa Home Group; Active, Activated), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`; `Head Office` > `Logistics Warehouse` > `Dock 1`), dan #19 (penugasan Role Transaksi `IT Infrastructure` sub-tab `Disposal`).
- Kemampuan teknis (disediakan tim FE/BE lewat fixture BE, tanpa endpoint karangan): seeding precondition TC di hook `before` berupa Indra Kusuma tanpa penugasan Role Transaksi pada node mana pun (penugasan yang tersisa dicabut; dipakai sebagai precondition TC, tidak diasersi), serta pemulihan Pre-setup #17 dan #19 ke kondisi Tabel Data Uji Pre-setup TC di hook `after` sebagai cadangan.
- Data Dinamis: tidak ada data yang dibuat spec. Spec tidak menyimpan penugasan apa pun (tanpa klik `[Assign]`); tidak ada state yang berubah selain pembukaan dan penutupan popup.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture. Spec ini tidak login sebagai Indra Kusuma.

## Test Steps

### TC-FA-RP-1226: User tanpa Home Group constraint muncul di picker keempat role Role Transaksi pada node mana pun

1. Klik Tab `Transaction Role`, klik node `Rack A1` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Ketik Search `Indra Kusuma`, tekan Enter
4. Verifikasi Indra Kusuma ada di daftar picker section Asset Admin `Rack A1`
5. Tutup popup Assign lewat `[×]`
6. Klik `[+ Assign]` pada section Monitoring & Report
7. Ketik Search `Indra Kusuma`, tekan Enter
8. Verifikasi Indra Kusuma ada di daftar picker section Monitoring & Report `Rack A1`
9. Tutup popup Assign lewat `[×]`
10. Klik `[+ Assign]` pada section Staff
11. Ketik Search `Indra Kusuma`, tekan Enter
12. Verifikasi Indra Kusuma ada di daftar picker section Staff `Rack A1`
13. Tutup popup Assign lewat `[×]`
14. Klik `[+ Assign]` pada section Approver
15. Ketik Search `Indra Kusuma`, tekan Enter
16. Verifikasi Indra Kusuma ada di daftar picker section Approver `Rack A1`
17. Tutup popup Assign lewat `[×]`
18. Klik node `Dock 1` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
19. Klik `[+ Assign]` pada section Asset Admin
20. Ketik Search `Indra Kusuma`, tekan Enter
21. Verifikasi Indra Kusuma ada di daftar picker section Asset Admin `Dock 1` (user tanpa constraint eligible di group mana pun)
22. Tutup popup Assign lewat `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 22 langkah.
- Langkah penghubung (S-03): langkah 1 dan 18 (navigasi Tab, node, sub-tab), langkah 2, 6, 10, 14, dan 19 (membuka popup Assign pada tiap section), dan langkah 5, 9, 13, 17, dan 22 (menutup popup, S-09). Langkah 3, 7, 11, 15, dan 20 adalah Search nama kandidat di Table User Picker yang dapat memuat lebih dari satu halaman (R-16, R-22).
- Expected a TC ("keempat section di `Rack A1`") dipecah satu `Verifikasi` per section (langkah 4, 8, 12, dan 16) agar tiap section dapat gagal sendiri (S-01). Seluruh asersi spec ini presence; tidak ada asersi absence atau log (S-05, bagian 8b butir 2 tidak terpicu).
- Temuan untuk QA:
  - NC-20 / Open Item #9 (menunggu PM): arah gate Home Group sebagai constraint belum dikonfirmasi PM; TC-FA-RP-1226 menyatakan user tanpa constraint eligible di group mana pun, dan bila PM menetapkan lain Expected 1226.a dan 1226.b usang.
  - TC-FA-RP-1226 tidak memuat asersi preview scope popup dan PRD tidak memuat locator preview scope; spec tidak mengasersinya.
  - Email Indra Kusuma tidak tertulis di Pre-setup #17 dan tidak dipakai login oleh spec ini; spec tidak membutuhkan env password untuknya.
  - Precondition TC-FA-RP-1226 ("tanpa penugasan Role Transaksi") tidak menyebut cara membentuknya; spec menetapkannya lewat fixture BE yang disediakan tim FE/BE (kemampuan seeding dan pemulihan Pre-setup #17 belum punya nama di Pre-setup).
  - TC-FA-RP-1226 langkah 3 ("ulangi pada section Monitoring & Report, Staff, dan Approver") tidak menyebut node; spec memakai `Rack A1` seperti langkah 1 dan 2, sesuai Expected a.
  - Post Condition TC-FA-RP-1226 kosong ("-").
