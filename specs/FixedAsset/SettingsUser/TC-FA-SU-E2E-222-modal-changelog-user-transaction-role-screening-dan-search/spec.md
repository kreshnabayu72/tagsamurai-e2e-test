---
id: TC-FA-SU-E2E-222-modal-changelog-user-transaction-role-screening-dan-search
title: "Modal Changelog User > Transaction Role: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-671
  - TC-FA-SU-672
  - TC-FA-SU-673
  - TC-FA-SU-674
coverage:
  web: automated
---

# Modal Changelog User > Transaction Role: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Transaction Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By):
  - TR-1: `Damaged — Branch Surabaya — Monitoring & Report`; Modified By `Ahmad D`
  - TR-2: `Missing — Branch Surabaya — Approver`; Modified By `Ahmad D`
  - TR-3: `Disposal — Logistics Warehouse — Asset Admin`; Modified By `Lina M`
  - TR-4: `Disposal — Logistics Warehouse — Staff`; Modified By `Lina M`
  - TR-5: `Transfer — Finance & Accounting — Asset Admin`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-671: Screening Modal Changelog

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Transaction Role, lalu klik icon Changelog
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
17. Verifikasi default sort Date descending, urutan relatif baris seed (baris non-seed boleh menyisip menurut Date-nya): TR-1, TR-2, TR-3, TR-4, TR-5
18. Verifikasi footer pagination 10 data per halaman
19. Klik dropdown page size
20. Verifikasi pilihan page size 10, 25, 50, 100
21. Tekan Esc untuk menutup dropdown page size

### TC-FA-SU-672: Search kelas teks (Action, Field)

22. Ketik Search `Assign` (kolom Action), tekan Enter
23. Verifikasi keyword `Assign` (kolom Action) menyisakan TR-1, TR-2, TR-3, TR-4, TR-5 (5 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
24. Kosongkan isi kotak search, tekan Enter
25. Ketik Search `Group Manager` (kolom Field), tekan Enter
26. Verifikasi keyword `Group Manager` (kolom Field) menyisakan tidak ada baris (0 baris), empty state `No results found` tampil
27. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-673: Search kelas mixed (Old Value, New Value)

28. Ketik Search `Logistics` (kolom Old Value), tekan Enter
29. Verifikasi keyword `Logistics` (kolom Old Value) menyisakan TR-3, TR-4 (2 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
30. Kosongkan isi kotak search, tekan Enter
31. Ketik Search `Assigned` (kolom New Value), tekan Enter
32. Verifikasi keyword `Assigned` (kolom New Value) menyisakan TR-1, TR-2, TR-3, TR-4, TR-5 (5 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
33. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-674: Search kelas user (Modified By)

34. Ketik Search `Marlina` (kolom Modified By), tekan Enter
35. Verifikasi keyword `Marlina` (kolom Modified By) menyisakan TR-3, TR-4 (2 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
36. Kosongkan isi kotak search, tekan Enter
37. Klik icon ←

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Asersi baris seed pada Modal Changelog (audit trail permanen) ditulis relatif terhadap baris seed: urutan relatif dan jumlah baris seed, dengan baris non-seed yang memenuhi kriteria boleh menyisip atau ikut tampil (S-14), mengikuti kualifier Expected TC sumber.
- Spec ini berjumlah 37 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Asersi tambahan di luar Expected (S-03): empty state `No results found` pada asersi hasil 0 baris, sebagai anchor positif absence (bagian 8b butir 2).
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Filter Action `Assign` hanya menyisakan 3 baris (TC-FA-SU-684) sedangkan Search `Assign` menyisakan 5 baris (TC-FA-SU-672); selisih ini konsisten hanya bila Search juga mencocokkan kolom lain (mis. New Value `Assigned`, TC-FA-SU-673). Label "kolom Action" pada TC-FA-SU-672 menyiratkan pencocokan kolom Action saja. Spec mengikuti angka TC. (3) TC menulis hasil 0 baris tanpa menyebut empty state; spec menambahkan `Verifikasi` empty state `No results found` sebagai anchor positif asersi 0 baris (bagian 8b butir 2), mengacu pada Expected TC-FA-SU-676 butir a.
