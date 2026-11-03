---
id: TC-FA-SU-E2E-204-modal-changelog-user-global-role-search-dan-sort
title: "Modal Changelog User > Global Role: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-613
  - TC-FA-SU-614
  - TC-FA-SU-615
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Global Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | Role Name | Field; Modified By):
  - G-1: `Remove` | `Manage global license` | `Manage global license`; Modified By `Lina M`
  - G-2: `Remove (via Total Control)` | `Manage global license` | `Access`; Modified By `Ahmad D`
  - G-3: `Assign (via Total Control)` | `Import Data` | `Access`; Modified By `Ahmad D`
  - G-4: `Edit` | `Manage asset master data` | `Manage asset master data — Delete`; Modified By `Ahmad D`
  - G-5: `Assign` | `Manage accounting` | `Manage accounting`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-613: Search terikat visibilitas kolom Action

1. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
2. Ketik Search `Assign`, tekan Enter
3. Verifikasi sebelum hide: keyword `Assign` menyisakan G-1, G-2, G-3, G-5 (4 baris)
4. Klik header Column Visibility (⋯), hilangkan centang Action
5. Ganti isi kotak search dengan `Assign`, tekan Enter
6. Verifikasi setelah kolom Action di-hide: keyword yang sama menyisakan G-1, G-2, G-3, G-5 (4 baris)
7. Klik header Column Visibility (⋯), centang kembali Action
8. Ganti isi kotak search dengan `Assign`, tekan Enter
9. Verifikasi setelah kolom Action di-unhide: hasil kembali G-1, G-2, G-3, G-5 (4 baris)
10. Klik `(←)` pada kotak Search

### TC-FA-SU-614: Sort kelas date (Date)

11. Klik header Date satu kali
12. Verifikasi urutan lima baris pertama klik 1 ascending (↑): G-5, G-4, G-3, G-2, G-1
13. Klik header Date kedua kali
14. Verifikasi urutan lima baris pertama klik 2 descending (↓): G-1, G-2, G-3, G-4, G-5
15. Klik header Date ketiga kali
16. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: G-1, G-2, G-3, G-4, G-5

### TC-FA-SU-615: Sort kelas teks (Action, Role Name, Field)

17. Klik header Action satu kali
18. Verifikasi urutan lima baris pertama klik 1 ascending (↑): G-5, G-3, G-4, G-1, G-2
19. Klik header Action kedua kali
20. Verifikasi urutan lima baris pertama klik 2 descending (↓): G-2, G-1, G-4, G-3, G-5
21. Klik header Action ketiga kali
22. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: G-1, G-2, G-3, G-4, G-5
23. Klik header Role Name satu kali
24. Verifikasi urutan lima baris pertama klik 1 ascending (↑): G-3, G-5, G-4, G-1, G-2
25. Klik header Role Name kedua kali
26. Verifikasi urutan lima baris pertama klik 2 descending (↓): G-1, G-2, G-4, G-5, G-3
27. Klik header Role Name ketiga kali
28. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: G-1, G-2, G-3, G-4, G-5
29. Klik header Field satu kali
30. Verifikasi urutan lima baris pertama klik 1 ascending (↑): G-2, G-3, G-5, G-4, G-1
31. Klik header Field kedua kali
32. Verifikasi urutan lima baris pertama klik 2 descending (↓): G-1, G-4, G-5, G-2, G-3
33. Klik header Field ketiga kali
34. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: G-1, G-2, G-3, G-4, G-5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14).
