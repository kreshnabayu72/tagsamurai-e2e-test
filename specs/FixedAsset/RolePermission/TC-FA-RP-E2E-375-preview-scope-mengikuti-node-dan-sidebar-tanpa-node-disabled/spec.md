---
id: TC-FA-RP-E2E-375-preview-scope-mengikuti-node-dan-sidebar-tanpa-node-disabled
title: "Preview scope mengikuti node terpilih dan Sidebar Group Tree tanpa node disabled walau ancestor atau descendant memegang penugasan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1206
  - TC-FA-RP-1207
coverage:
  web: automated
---

# Preview scope mengikuti node terpilih dan Sidebar Group Tree tanpa node disabled walau ancestor atau descendant memegang penugasan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon Group), #19 (Nadia Putri Asset Admin di `IT Infrastructure` sub-tab `Disposal`), dan #15 (Ahmad Fauzi, pool pengguna Standard).
- Kondisi awal yang di-seed di hook `before` (precondition TC-FA-RP-1207, tidak diasersi): Ahmad Fauzi Asset Admin di `Rack A1` sub-tab `Disposal`. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec. Spec tidak mengklik `[Assign]`.
- State yang diubah dan pemulihannya: hook `before` menambah baris Ahmad Fauzi di `Rack A1`; hook `after` mencabut baris itu (tidak berasumsi seeding berhasil penuh) sehingga Pre-setup #19 kembali ke kondisi Tabel Data Uji Pre-setup TC. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1206: preview scope mengikuti node terpilih

1. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Verifikasi preview scope node `Data Center` menampilkan `Data Center` dan `Rack A1`
4. Tutup popup lewat `[×]`
5. Klik node `Rack A1` di Sidebar Group Tree
6. Klik `[+ Assign]` pada section Approver
7. Verifikasi preview scope node `Rack A1` hanya menampilkan `Rack A1` (tanpa descendant)
8. Verifikasi preview scope node `Rack A1` tidak memuat `Data Center`
9. Tutup popup lewat `[×]`
10. Klik node `Helpdesk` di Sidebar Group Tree
11. Klik `[+ Assign]` pada section Staff
12. Verifikasi preview scope node `Helpdesk` hanya menampilkan `Helpdesk`
13. Verifikasi preview scope node `Helpdesk` tidak memuat sibling `Data Center`
14. Tutup popup lewat `[×]`

### TC-FA-RP-1207: Sidebar Group Tree tanpa node disabled

15. Verifikasi Sidebar Group Tree pada Tab `Transaction Role` memuat node `Head Office`, `IT Infrastructure`, `Data Center`, `Rack A1`, `Helpdesk`, `Logistics Warehouse`, dan `Dock 1`
16. Verifikasi tidak ada node bergaya disabled pada Sidebar Group Tree
17. Klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
18. Verifikasi node `IT Infrastructure` terpilih dan panel Role Transaksi node itu termuat
19. Verifikasi section Asset Admin, Monitoring & Report, Staff, dan Approver tampil pada node `IT Infrastructure`
20. Verifikasi `[+ Assign]` Enabled pada keempat section node `IT Infrastructure`
21. Klik node `Data Center`, lalu klik sub-tab `Disposal`
22. Verifikasi node `Data Center` terpilih dan panel Role Transaksi node itu termuat
23. Verifikasi section Asset Admin, Monitoring & Report, Staff, dan Approver tampil pada node `Data Center`
24. Verifikasi `[+ Assign]` Enabled pada keempat section node `Data Center`
25. Klik node `Rack A1`, lalu klik sub-tab `Disposal`
26. Verifikasi node `Rack A1` terpilih dan panel Role Transaksi node itu termuat
27. Verifikasi section Asset Admin, Monitoring & Report, Staff, dan Approver tampil pada node `Rack A1`
28. Verifikasi `[+ Assign]` Enabled pada keempat section node `Rack A1`
29. Klik node `Helpdesk`, lalu klik sub-tab `Disposal`
30. Verifikasi node `Helpdesk` terpilih dan panel Role Transaksi node itu termuat
31. Verifikasi section Asset Admin, Monitoring & Report, Staff, dan Approver tampil pada node `Helpdesk`
32. Verifikasi `[+ Assign]` Enabled pada keempat section node `Helpdesk`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 32 langkah (di bawah ambang sekitar 35).
- Langkah penghubung (S-03): langkah 1, 5, 10, 17, 21, 25, dan 29 (navigasi Tab, node, sub-tab); langkah 2, 6, dan 11 (membuka popup, bagian dari langkah TC 1206); langkah 4, 9, dan 14 (menutup popup).
- Asersi tambahan yang tidak ada di TC (S-03, bagian 8b butir 2): langkah 8 dan 13 menegaskan "hanya" (ancestor `Data Center` dan sibling tidak ikut; langkah 3, 7, dan 12 menjadi anchor positif), langkah 15 menjadi anchor positif atas asersi absence node disabled langkah 16, dan langkah 18, 22, 26, 30 membuktikan node dapat diklik (Expected 1207.a "seluruh node dapat diklik"). Langkah 13 diambil dari Expected 1206.c.
- Cara baca Expected 1207: a dipetakan ke langkah 16 (tidak ada node bergaya disabled, termasuk node yang ancestor atau descendant-nya memegang penugasan) dan langkah 18, 22, 26, 30 (dapat diklik); b dipetakan ke langkah 19, 20, 23, 24, 27, 28, 31, 32 (satu `Verifikasi` untuk keempat section dan satu untuk keempat `[+ Assign]` per node).
- Temuan untuk QA:
  - PRD tidak memuat literal judul maupun locator preview scope; asersi hanya atas daftar node (himpunan, tanpa urutan). Usulan locator untuk tim FE (belum ada di PRD): `~aria-label` `Preview Scope` pada popup dan satu elemen per node di dalamnya.
  - NC-19 / Open Item #8 (penugasan mencakup node beserta descendant) belum dikonfirmasi PM; bila cakupan berubah, Expected 1206.a dan 1206.c usang.
  - TC-FA-RP-1206 langkah 2 dan 3 menyebut klik node tanpa menyebut sub-tab; spec mengandalkan sub-tab `Disposal` tetap aktif setelah klik node berikutnya.
  - Gaya "disabled" node tidak punya locator atau definisi visual di PRD; asersi langkah 16 memakai state disabled dari Page Object yang disediakan tim FE.
