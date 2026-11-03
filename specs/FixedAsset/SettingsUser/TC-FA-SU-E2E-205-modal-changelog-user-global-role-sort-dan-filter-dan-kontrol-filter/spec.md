---
id: TC-FA-SU-E2E-205-modal-changelog-user-global-role-sort-dan-filter-dan-kontrol-filter
title: "Modal Changelog User > Global Role: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-616
  - TC-FA-SU-617
  - TC-FA-SU-618
  - TC-FA-SU-619
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Sort dan Filter dan Kontrol Filter

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

### TC-FA-SU-616: Sort kelas mixed (Old Value, New Value)

1. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
2. Klik header Old Value satu kali
3. Verifikasi urutan lima baris pertama klik 1 ascending (↑): G-1, G-2, G-4, G-3, G-5
4. Klik header Old Value kedua kali
5. Verifikasi urutan lima baris pertama klik 2 descending (↓): G-3, G-5, G-4, G-1, G-2
6. Klik header Old Value ketiga kali
7. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: G-1, G-2, G-3, G-4, G-5
8. Klik header New Value satu kali
9. Verifikasi urutan lima baris pertama klik 1 ascending (↑): G-4, G-3, G-5, G-1, G-2
10. Klik header New Value kedua kali
11. Verifikasi urutan lima baris pertama klik 2 descending (↓): G-1, G-2, G-3, G-5, G-4
12. Klik header New Value ketiga kali
13. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: G-1, G-2, G-3, G-4, G-5

### TC-FA-SU-617: Sort kelas user (Modified By)

14. Klik header Modified By satu kali
15. Verifikasi urutan lima baris pertama klik 1 ascending (↑): G-2, G-3, G-4, G-5, G-1
16. Klik header Modified By kedua kali
17. Verifikasi urutan lima baris pertama klik 2 descending (↓): G-1, G-2, G-3, G-4, G-5
18. Klik header Modified By ketiga kali
19. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: G-1, G-2, G-3, G-4, G-5

### TC-FA-SU-618: Screening Filter Panel

20. Klik icon Filter
21. Verifikasi panel terbuka di bawah Table Tools
22. Verifikasi ikon Filter menjadi gelap
23. Hover icon Filter
24. Verifikasi tooltip `Filter`
25. Verifikasi field ke-1 adalah Date (date range picker) dengan placeholder `Select date`
26. Verifikasi field ke-2 adalah Action (multi-select searchable) dengan placeholder `All actions`
27. Verifikasi field ke-3 adalah Role Name (multi-select searchable) dengan placeholder `All roles`
28. Verifikasi field ke-4 adalah Field (multi-select searchable) dengan placeholder `All fields`
29. Verifikasi field ke-5 adalah Modified By (multi-select searchable) dengan placeholder `All users`
30. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
31. Verifikasi tidak ada badge titik pada ikon Filter selama belum ada filter ter-Apply

### TC-FA-SU-619: Filter kelas date (Date)

32. Pilih rentang 15/07/26 sampai 20/07/26 pada Date
33. Klik `[Apply]`
34. Verifikasi rentang inklusif 15/07/26 sampai 20/07/26 menyisakan G-4, G-5 (2 baris)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE.
