---
id: TC-FA-SU-E2E-194-tab-changelog-screening-dan-search
title: "Tab Changelog: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-575
  - TC-FA-SU-576
  - TC-FA-SU-577
  - TC-FA-SU-578
coverage:
  web: automated
---

# Tab Changelog: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By dalam format `[First Name] [Last Initial]`):
  - T-1: Field `Manage files — IT Infrastructure`, Modified By `Ahmad D`
  - T-2: Field `Manage group — IT Infrastructure — Delete`, Modified By `Ahmad D`
  - T-3: Field `Manage group — IT Infrastructure — Update`, Modified By `Ahmad D`
  - T-4: Field `Home Group`, Modified By `Lina M`
  - T-5: Field `Manage asset master data — Delete`, Modified By `Ahmad D`
  - T-6: Field `Manage accounting`, Modified By `Ahmad D`
  - T-7: Field `Status`, Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-575: Screening Tab Changelog

1. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
2. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil rata kanan
3. Hover icon Search
4. Verifikasi tooltip `Search`
5. Hover icon Filter
6. Verifikasi tooltip `Filter`
7. Hover icon Download
8. Verifikasi tooltip `Download`
9. Klik icon Search
10. Verifikasi placeholder Search `Search action, field, or value...`
11. Klik icon ←
12. Verifikasi kolom `Date (sortable) | Action (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯)`
13. Klik header kolom Column Visibility (⋯)
14. Verifikasi overlay Column Visibility tampil
15. Verifikasi sel body kolom Column Visibility (⋯) pada setiap baris kosong tanpa row action
16. Tekan Esc untuk menutup overlay
17. Verifikasi default sort Date descending, lima baris pertama: T-1, T-2, T-3, T-4, T-5
18. Verifikasi footer pagination 10 data per halaman
19. Klik dropdown page size
20. Verifikasi pilihan page size 10, 25, 50, 100
21. Tekan Esc untuk menutup dropdown page size

### TC-FA-SU-576: Search kelas teks (Action, Field)

22. Ketik Search `Home` (kolom Action), tekan Enter
23. Verifikasi keyword `Home` (kolom Action) menyisakan `Home Group` (T-4; 1 baris)
24. Kosongkan isi kotak search, tekan Enter
25. Ketik Search `Manage files` (kolom Field), tekan Enter
26. Verifikasi keyword `Manage files` (kolom Field) menyisakan `Manage files — IT Infrastructure` (T-1; 1 baris)
27. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-577: Search kelas mixed (Old Value, New Value)

28. Ketik Search `Logistics` (kolom Old Value), tekan Enter
29. Verifikasi keyword `Logistics` (kolom Old Value) menyisakan `Home Group` (T-4; 1 baris)
30. Kosongkan isi kotak search, tekan Enter
31. Ketik Search `Assigned` (kolom New Value), tekan Enter
32. Verifikasi keyword `Assigned` (kolom New Value) menyisakan `Manage files — IT Infrastructure`, `Manage accounting` (T-1, T-6; 2 baris)
33. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-578: Search kelas user (Modified By)

34. Ketik Search `Marlina` (kolom Modified By), tekan Enter
35. Verifikasi keyword `Marlina` (kolom Modified By) menyisakan `Home Group` (T-4; 1 baris)
36. Kosongkan isi kotak search, tekan Enter
37. Klik icon ←

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 37 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Expected b TC-FA-SU-575 menyebut header Column Visibility membuka overlay; overlay diverifikasi di spec 199 (TC-FA-SU-594), spec ini hanya membukanya dan mengasersi body kolom kosong.
