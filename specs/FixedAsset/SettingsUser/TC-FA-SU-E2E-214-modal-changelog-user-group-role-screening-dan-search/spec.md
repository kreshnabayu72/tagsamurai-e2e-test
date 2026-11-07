---
id: TC-FA-SU-E2E-214-modal-changelog-user-group-role-screening-dan-search
title: "Modal Changelog User > Group Role: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-639
  - TC-FA-SU-640
  - TC-FA-SU-641
  - TC-FA-SU-642
coverage:
  web: automated
---

# Modal Changelog User > Group Role: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Group Role (Pre-setup #27, 4 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By):
  - GR-1: `Manage files — Branch Surabaya`; Modified By `Lina M`
  - GR-2: `Manage files — IT Infrastructure`; Modified By `Ahmad D`
  - GR-3: `Group Manager — IT Infrastructure`; Modified By `Ahmad D`
  - GR-4: `Manage group — IT Infrastructure — Update`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-639: Screening Modal Changelog

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Group Role, lalu klik icon Changelog
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
12. Verifikasi kolom `Date (sortable) | Action (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯)`
13. Klik header kolom Column Visibility (⋯)
14. Verifikasi overlay Column Visibility tampil
15. Verifikasi sel body kolom Column Visibility (⋯) pada setiap baris kosong tanpa row action
16. Tekan Esc untuk menutup overlay
17. Verifikasi default sort Date descending: urutan relatif baris seed menurut Date seed dari terbaru ke terlama (baris non-seed boleh menyisip menurut Date-nya): GR-1, GR-2, GR-3, GR-4
18. Verifikasi footer pagination 10 data per halaman
19. Klik dropdown page size
20. Verifikasi pilihan page size 10, 25, 50, 100
21. Tekan Esc untuk menutup dropdown page size

### TC-FA-SU-640: Search kelas teks (Action, Field)

22. Ketik Search `Assign` (kolom Action), tekan Enter
23. Verifikasi keyword `Assign` (kolom Action) menyisakan GR-1, GR-2, GR-3 (3 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
24. Kosongkan isi kotak search, tekan Enter
25. Ketik Search `Group Manager` (kolom Field), tekan Enter
26. Verifikasi keyword `Group Manager` (kolom Field) menyisakan GR-3 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
27. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-641: Search kelas mixed (Old Value, New Value)

28. Ketik Search `Logistics` (kolom Old Value), tekan Enter
29. Verifikasi keyword `Logistics` (kolom Old Value) menyisakan tidak ada baris (0 baris), empty state `No results found` tampil
30. Kosongkan isi kotak search, tekan Enter
31. Ketik Search `Assigned` (kolom New Value), tekan Enter
32. Verifikasi keyword `Assigned` (kolom New Value) menyisakan GR-1, GR-2, GR-3 (3 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
33. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-642: Search kelas user (Modified By)

34. Ketik Search `Marlina` (kolom Modified By), tekan Enter
35. Verifikasi keyword `Marlina` (kolom Modified By) menyisakan GR-1 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
36. Kosongkan isi kotak search, tekan Enter
37. Klik icon ←

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Asersi baris seed pada Modal Changelog (audit trail permanen) ditulis relatif terhadap baris seed: urutan relatif dan jumlah baris seed, dengan baris non-seed yang memenuhi kriteria boleh menyisip atau ikut tampil (S-14), mengikuti kualifier Expected TC sumber.
- Spec ini berjumlah 37 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Asersi tambahan di luar Expected (S-03): empty state `No results found` pada asersi hasil 0 baris, sebagai anchor positif absence (bagian 8b butir 2).
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Filter Action `Assign` hanya menyisakan 1 baris (TC-FA-SU-652) sedangkan Search `Assign` menyisakan 3 baris (TC-FA-SU-640); selisih ini konsisten hanya bila Search juga mencocokkan kolom lain (mis. New Value `Assigned`, TC-FA-SU-641). Label "kolom Action" pada TC-FA-SU-640 menyiratkan pencocokan kolom Action saja. Spec mengikuti angka TC. (3) TC menulis hasil 0 baris tanpa menyebut empty state; spec menambahkan `Verifikasi` empty state `No results found` sebagai anchor positif asersi 0 baris (bagian 8b butir 2), mengacu pada Expected TC-FA-SU-644 butir a.
