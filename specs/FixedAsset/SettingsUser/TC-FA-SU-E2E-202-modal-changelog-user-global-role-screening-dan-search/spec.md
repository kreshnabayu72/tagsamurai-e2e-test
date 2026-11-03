---
id: TC-FA-SU-E2E-202-modal-changelog-user-global-role-screening-dan-search
title: "Modal Changelog User > Global Role: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-607
  - TC-FA-SU-608
  - TC-FA-SU-609
  - TC-FA-SU-610
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Screening dan Search

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

### TC-FA-SU-607: Screening Modal Changelog

1. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
2. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil rata kanan
3. Hover icon Search
4. Verifikasi tooltip `Search`
5. Hover icon Filter
6. Verifikasi tooltip `Filter`
7. Hover icon Download
8. Verifikasi tooltip `Download`
9. Klik icon Search
10. Verifikasi placeholder Search `Search action, role, field, or value...`
11. Klik icon ←
12. Verifikasi kolom `Date (sortable) | Action (sortable) | Role Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯)`
13. Klik header kolom Column Visibility (⋯)
14. Verifikasi overlay Column Visibility tampil
15. Verifikasi sel body kolom Column Visibility (⋯) pada setiap baris kosong tanpa row action
16. Tekan Esc untuk menutup overlay
17. Verifikasi default sort Date descending, lima baris pertama: G-1, G-2, G-3, G-4, G-5
18. Verifikasi footer pagination 10 data per halaman
19. Klik dropdown page size
20. Verifikasi pilihan page size 10, 25, 50, 100
21. Tekan Esc untuk menutup dropdown page size

### TC-FA-SU-608: Search kelas teks (Action, Role Name, Field)

22. Ketik Search `Assign` (kolom Action), tekan Enter
23. Verifikasi keyword `Assign` (kolom Action) menyisakan G-1, G-2, G-3, G-5 (4 baris)
24. Kosongkan isi kotak search, tekan Enter
25. Ketik Search `Import` (kolom Role Name), tekan Enter
26. Verifikasi keyword `Import` (kolom Role Name) menyisakan G-3 (1 baris)
27. Kosongkan isi kotak search, tekan Enter
28. Ketik Search `Group Manager` (kolom Field), tekan Enter
29. Verifikasi keyword `Group Manager` (kolom Field) menyisakan tidak ada baris (0 baris), empty state `No results found` tampil
30. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-609: Search kelas mixed (Old Value, New Value)

31. Ketik Search `Logistics` (kolom Old Value), tekan Enter
32. Verifikasi keyword `Logistics` (kolom Old Value) menyisakan tidak ada baris (0 baris), empty state `No results found` tampil
33. Kosongkan isi kotak search, tekan Enter
34. Ketik Search `Assigned` (kolom New Value), tekan Enter
35. Verifikasi keyword `Assigned` (kolom New Value) menyisakan G-1, G-2, G-3, G-5 (4 baris)
36. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-610: Search kelas user (Modified By)

37. Ketik Search `Marlina` (kolom Modified By), tekan Enter
38. Verifikasi keyword `Marlina` (kolom Modified By) menyisakan G-1 (1 baris)
39. Kosongkan isi kotak search, tekan Enter
40. Klik icon ←

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Asersi tambahan di luar Expected (S-03): empty state `No results found` pada asersi hasil 0 baris, sebagai anchor positif absence (bagian 8b butir 2).
- Spec ini berjumlah 40 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) TC menulis hasil 0 baris tanpa menyebut empty state; spec menambahkan `Verifikasi` empty state `No results found` sebagai anchor positif asersi 0 baris (bagian 8b butir 2), mengacu pada Expected TC-FA-SU-580 butir a.
