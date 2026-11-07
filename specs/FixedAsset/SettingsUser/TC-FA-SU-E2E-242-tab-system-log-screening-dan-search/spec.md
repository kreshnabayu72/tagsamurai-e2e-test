---
id: TC-FA-SU-E2E-242-tab-system-log-screening-dan-search
title: "Tab System Log: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-735
  - TC-FA-SU-736
  - TC-FA-SU-737
coverage:
  web: automated
---

# Tab System Log: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan System Log (#28). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab System Log Budi Santoso (Pre-setup #28, 7 baris; urutan default Date descending; kolom Name berisi target perubahan). Alias baris yang dipakai langkah (Action | Name | Field):
  - S-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`
  - S-2: `Auto-Revert` | `Oscar Pranata` | `Group Manager — IT Infrastructure`
  - S-3: `Edit` | `Oscar Pranata` | `Manage group — IT Infrastructure — Update`
  - S-4: `Assign` | `Lina Marlina` | `Access Level`
  - S-5: `Assign` | `Eka Wulandari` | `Manage group — Finance & Accounting`
  - S-6: `Assign` | `Eka Wulandari` | `Manage accounting`
  - S-7: `Activate` | `Eka Wulandari` | `Status`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed System Log #28 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface System Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-735: Screening Tab System Log: Table Tools, kolom, dan default sort

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso dan klik tab System Log
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
12. Verifikasi kolom `Date (sortable) | Action (sortable) | Object (sortable) | Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Column Visibility (⋯)`
13. Klik header kolom Column Visibility (⋯)
14. Verifikasi overlay Column Visibility tampil
15. Verifikasi sel body kolom Column Visibility (⋯) pada setiap baris kosong tanpa row action
16. Tekan Esc untuk menutup overlay
17. Verifikasi default sort Date descending, urutan relatif baris seed (baris non-seed boleh menyisip): S-1, S-2, S-3, S-4, S-5
18. Verifikasi footer pagination 10 data per halaman
19. Klik dropdown page size
20. Verifikasi pilihan page size 10, 25, 50, 100
21. Tekan Esc untuk menutup dropdown page size

### TC-FA-SU-736: Search kelas teks (Action, Object, Name, Field)

22. Ketik Search `Revert` (kolom Action), tekan Enter
23. Verifikasi keyword `Revert` (kolom Action) menyisakan S-2 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
24. Kosongkan isi kotak search, tekan Enter
25. Ketik Search `Global Role` (kolom Object), tekan Enter
26. Verifikasi keyword `Global Role` (kolom Object) menyisakan S-6 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
27. Kosongkan isi kotak search, tekan Enter
28. Ketik Search `Hana` (kolom Name), tekan Enter
29. Verifikasi keyword `Hana` (kolom Name) menyisakan S-1 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
30. Kosongkan isi kotak search, tekan Enter
31. Ketik Search `Access Level` (kolom Field), tekan Enter
32. Verifikasi keyword `Access Level` (kolom Field) menyisakan S-4 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
33. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-737: Search kelas mixed (Old Value, New Value)

34. Ketik Search `Inactive` (kolom Old Value), tekan Enter
35. Verifikasi keyword `Inactive` (kolom Old Value) menyisakan S-3, S-7 (2 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
36. Kosongkan isi kotak search, tekan Enter
37. Ketik Search `Total Control` (kolom New Value), tekan Enter
38. Verifikasi keyword `Total Control` (kolom New Value) menyisakan S-4 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
39. Kosongkan isi kotak search, tekan Enter
40. Klik icon ←

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail pada langkah 1 didahului Search `Budi Santoso` lalu Enter untuk menemukan baris target (R-16, butir 8b.9 dan 8b.13); User List memuat 25 pengguna pada 3 halaman sehingga posisi baris tidak diandalkan.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 40 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) Nilai kolom Object per baris seed tidak tertulis di Pre-setup selain yang dipakai TC-FA-SU-736 (S-6 memiliki Object `Global Role`); opsi Object yang disebut TC-FA-SU-746 adalah `Global Role`, `Group Manager`, `Group Role`, `Total Control`, `User`. Nilai Old Value dan New Value baris seed hanya diketahui dari TC-FA-SU-737 (S-3 dan S-7 memuat `Inactive`, S-4 memuat `Total Control`).
