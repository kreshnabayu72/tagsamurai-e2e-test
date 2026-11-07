---
id: TC-FA-SU-E2E-232-modal-combined-changelog-user-screening-dan-search
title: "Modal Combined Changelog: User: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-703
  - TC-FA-SU-704
  - TC-FA-SU-705
  - TC-FA-SU-706
coverage:
  web: automated
---

# Modal Combined Changelog: User: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Modal Combined Changelog dibuka dari icon Changelog di Table Tools halaman User List dan memuat riwayat seluruh pengguna Client `FaUserMain`. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Combined Changelog (Pre-setup #27, 6 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | User Name | Field; Modified By dalam format `[First Name] [Last Initial]`):
  - C-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`; Modified By `Ahmad D`
  - C-2: `Deactivate` | `Doni Prasetyo` | `Status`; Modified By `Budi S`
  - C-3: `Edit Home Group` | `Budi Santoso` | `Home Group`; Modified By `Lina M`
  - C-4: `Edit` | `Gita Permata` | `Manage group — Finance & Accounting — Update`; Modified By `Ahmad D`
  - C-5: `Assign` | `Budi Santoso` | `Manage accounting`; Modified By `Ahmad D`
  - C-6: `Activate` | `Eka Wulandari` | `Status`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Combined Changelog dan tidak menambah entri.

## Test Steps

### TC-FA-SU-703: Screening Modal Combined Changelog: Table Tools, kolom, dan default sort

1. Klik icon Changelog di Table Tools halaman User List
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
12. Verifikasi kolom `Date (sortable) | Action (sortable) | User Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯)`
13. Klik header kolom Column Visibility (⋯)
14. Verifikasi overlay Column Visibility tampil
15. Verifikasi sel body kolom Column Visibility (⋯) pada setiap baris kosong tanpa row action
16. Tekan Esc untuk menutup overlay
17. Verifikasi default sort Date descending, urutan relatif baris seed (baris non-seed boleh menyisip): C-1, C-2, C-3, C-4, C-5
18. Verifikasi footer pagination 10 data per halaman
19. Klik dropdown page size
20. Verifikasi pilihan page size 10, 25, 50, 100
21. Tekan Esc untuk menutup dropdown page size

### TC-FA-SU-704: Search kelas teks (Action, User Name, Field)

22. Ketik Search `Resend` (kolom Action), tekan Enter
23. Verifikasi keyword `Resend` (kolom Action) menyisakan C-1 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
24. Kosongkan isi kotak search, tekan Enter
25. Ketik Search `Gita` (kolom User Name), tekan Enter
26. Verifikasi keyword `Gita` (kolom User Name) menyisakan C-4 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
27. Kosongkan isi kotak search, tekan Enter
28. Ketik Search `Home Group` (kolom Field), tekan Enter
29. Verifikasi keyword `Home Group` (kolom Field) menyisakan C-3 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
30. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-705: Search kelas mixed (Old Value, New Value)

31. Ketik Search `Logistics` (kolom Old Value), tekan Enter
32. Verifikasi keyword `Logistics` (kolom Old Value) menyisakan C-3 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
33. Kosongkan isi kotak search, tekan Enter
34. Ketik Search `Assigned` (kolom New Value), tekan Enter
35. Verifikasi keyword `Assigned` (kolom New Value) menyisakan C-5 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
36. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-706: Search kelas user (Modified By)

37. Ketik Search `Santoso` (kolom Modified By), tekan Enter
38. Verifikasi keyword `Santoso` (kolom Modified By) menyisakan C-2, C-3, C-5 (3 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
39. Kosongkan isi kotak search, tekan Enter
40. Klik icon ←

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 40 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) TC-FA-SU-706 memberi label kolom Modified By, tetapi kata kunci `Santoso` yang dicari juga mencocokkan kolom User Name (C-3 dan C-5 bernama `Budi Santoso`) sedangkan C-2 cocok lewat Modified By `Budi S` dengan nama lengkap; tampilan Modified By berformat `[First Name] [Last Initial]` sementara pencarian memakai nama lengkap. Spec mengikuti Expected tiga baris. (3) Nilai Old Value dan New Value baris seed tidak tertulis di Tabel Pre-setup selain yang dipakai TC-FA-SU-705 (Old Value C-3 memuat `Logistics`, New Value C-5 memuat `Assigned`).
