---
id: TC-FA-RP-E2E-380-approver-di-ancestor-tidak-mengubah-toggle-descendant
title: "Penugasan Approver di node ancestor tidak mengubah nilai toggle Require Approval node descendant"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1216
coverage:
  web: automated
---

# Penugasan Approver di node ancestor tidak mengubah nilai toggle Require Approval node descendant

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, bagian "Hook suite".
- Data Pre-setup (dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas belum ada, disediakan tim FE): #15 (Ahmad Fauzi, Active, Activated, tanpa penugasan Approver di `IT Infrastructure`), #18 (struktur group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`), dan #19 (penugasan Role Transaksi; Approver Pandu Wijaya pada `IT Infrastructure` sub-tab `Disposal`; Require Approval OFF di semua node).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: toggle `Require Approval for Disposal` di `IT Infrastructure` diaktifkan oleh langkah 3 dan Ahmad Fauzi ditugaskan Approver di `IT Infrastructure` sub-tab `Disposal` oleh langkah 7 (efek: Last Updated baris dan entri Changelog bertambah). Hook `after` mengembalikan toggle ke OFF dan melepas penugasan Ahmad Fauzi, sehingga state kembali ke Pre-setup #19; dijamin fixture backend yang disediakan tim FE/BE, tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1216: Approver di ancestor tidak mengubah toggle descendant

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` pada Sidebar Group Tree, lalu klik sub-tab `Disposal`
3. Aktifkan toggle `Require Approval for Disposal`
4. Verifikasi toggle `Require Approval for Disposal` pada `IT Infrastructure` ON
5. Klik `[+ Assign]` pada section Approver
6. Ketik Search `Ahmad Fauzi` pada popup, tekan Enter
7. Centang Ahmad Fauzi, lalu klik `[Assign]`
8. Verifikasi muncul toast sukses: `Success, Approver has been assigned.`
9. Klik node `Data Center`, lalu klik sub-tab `Disposal`
10. Verifikasi toggle `Require Approval for Disposal` pada `Data Center` tetap OFF
11. Verifikasi RadioGroup aturan tidak tampil pada `Data Center`
12. Klik node `Rack A1`, lalu klik sub-tab `Disposal`
13. Verifikasi toggle `Require Approval for Disposal` pada `Rack A1` tetap OFF
14. Verifikasi RadioGroup aturan tidak tampil pada `Rack A1`
15. Klik node `Helpdesk`, lalu klik sub-tab `Disposal`
16. Verifikasi toggle `Require Approval for Disposal` pada `Helpdesk` tetap OFF
17. Verifikasi RadioGroup aturan tidak tampil pada `Helpdesk`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 17 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): navigasi Tab, node, dan sub-tab (langkah 1, 2, 9, 12, 15) dan Search kandidat pada popup `[+ Assign]` (langkah 6; R-16, R-22: kandidat dicari lewat Search agar tidak bergantung pada halaman pertama picker). Tabel section Approver memuat kurang dari 10 baris (Pre-setup #19: header Approver 4 pada `IT Infrastructure`), sehingga baris target tidak butuh Search.
- Asersi absence RadioGroup (langkah 11, 14, 17) didahului asersi toggle OFF pada kartu Approval Rule node yang sama (langkah 10, 13, 16) sebagai anchor kartu termuat (bagian 8b butir 2). Langkah 4 dan 8 adalah anchor bahwa aktivasi dan Assign selesai sebelum node descendant dibuka.
- Pembagian TC lintas spec: TC-FA-RP-1216 hanya ada di spec ini. Pasangan Approver ancestor dihitung aktivasi ada di spec 379 (TC-FA-RP-1214).
- Temuan untuk QA:
  - NC-19 / Open Item #8 (menunggu PM): pelebaran penugasan dan Approver ancestor dihitung; TC-FA-RP-1216 meng-assert perilaku PRD saat ini (toggle per node, 07c).
  - NC-11: hak efektif Approver `IT Infrastructure` pada `Data Center`, `Rack A1`, dan `Helpdesk` tidak teramati di surface ini; spec hanya meng-assert toggle dan RadioGroup.
  - TC-FA-RP-1216 Expected c ditulis satu butir untuk tiga node; spec memecahnya satu `Verifikasi` per node dan per klausa (toggle OFF, RadioGroup tidak tampil).
  - TC-FA-RP-1216 tidak menulis Post Condition; pemulihan toggle dan penugasan Ahmad Fauzi ada di hook `after`.
