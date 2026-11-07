---
id: TC-FA-SU-E2E-277-tab-user-log-sub-tab-assignment-screening-dan-search
title: "Tab User Log sub-tab Assignment: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-838
  - TC-FA-SU-839
  - TC-FA-SU-840
  - TC-FA-SU-841
coverage:
  web: automated
---

# Tab User Log sub-tab Assignment: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Assignment Budi Santoso (Pre-setup #30, 5 baris; urutan default Date descending). Label baris = `Activity|Transaction ID`; alias dipakai langkah:
  - A-1: `Unassigned|ASG-20260618-0089`, Date `30/06/26`, PIC `Eka W` (keyword `Wulandari`)
  - A-2: `Assigned|ASG-20260625-0102`, Name `Lemari`, PIC `Ahmad D`
  - A-3: `Assigned|ASG-20260618-0089`, PIC `Eka W` (keyword `Wulandari`)
  - A-4: `Assigned|ASG-20260512-0067`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
  - A-5: `Assigned|ASG-20260505-0045`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-838: Screening Table Tools, kolom, dan default sort

1. Ketik Search `Budi Santoso`, tekan Enter, buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Assignment
2. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil rata kanan
3. Hover icon Search
4. Verifikasi tooltip `Search`
5. Hover icon Filter
6. Verifikasi tooltip `Filter`
7. Hover icon Download
8. Verifikasi tooltip `Download`
9. Klik icon Search
10. Verifikasi placeholder Search `Search transaction ID, name, or PIC...`
11. Klik icon ←
12. Verifikasi kolom `Date (sortable) | Activity (unsortable) | Transaction ID (sortable) | Name (sortable) | PIC (sortable) | Column Visibility (⋯)`
13. Klik header kolom Column Visibility (⋯)
14. Verifikasi overlay Column Visibility tampil
15. Verifikasi sedikitnya satu baris tampil pada tabel
16. Verifikasi sel body kolom Column Visibility (⋯) pada setiap baris kosong tanpa row action
17. Tekan Esc untuk menutup overlay
18. Verifikasi default sort Date descending, lima baris pertama: A-1, A-2, A-3, A-4, A-5
19. Verifikasi footer pagination 10 data per halaman
20. Klik dropdown page size
21. Verifikasi pilihan page size 10, 25, 50, 100
22. Tekan Esc untuk menutup dropdown page size

### TC-FA-SU-839: Search kelas enum: kolom Activity

23. Ketik Search `Unassigned` (kolom Activity), tekan Enter
24. Verifikasi keyword `Unassigned` (kolom Activity) menyisakan A-1 (`Unassigned|ASG-20260618-0089`; 1 baris)
25. Kosongkan isi kotak search, tekan Enter
26. Klik icon ←

### TC-FA-SU-840: Search kelas teks: kolom Transaction ID, Name

27. Ketik Search `0067` (kolom Transaction ID), tekan Enter
28. Verifikasi keyword `0067` (kolom Transaction ID) menyisakan A-4 (`Assigned|ASG-20260512-0067`; 1 baris)
29. Kosongkan isi kotak search, tekan Enter
30. Ketik Search `Lemari` (kolom Name), tekan Enter
31. Verifikasi keyword `Lemari` (kolom Name) menyisakan A-2 (`Assigned|ASG-20260625-0102`; 1 baris)
32. Kosongkan isi kotak search, tekan Enter
33. Klik icon ←

### TC-FA-SU-841: Search kelas user: kolom PIC

34. Ketik Search `Wulandari` (kolom PIC), tekan Enter
35. Verifikasi keyword `Wulandari` (kolom PIC) menyisakan A-1, A-3 (2 baris)
36. Kosongkan isi kotak search, tekan Enter
37. Klik icon ←

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung pencarian baris (S-03, R-16, bagian 8b butir 13): langkah 1 mencari pengguna lewat Search nama persis `Budi Santoso` (nama Pre-setup) sebelum membuka Detail, karena User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman) sehingga spec tidak mengandalkan posisi baris di halaman.
- Langkah 15 (`Verifikasi sedikitnya satu baris tampil pada tabel`) adalah asersi tambahan di luar Expected TC dan dicatat di sini (S-03): pembanding generik sebelum asersi universal "setiap baris" pada kolom Column Visibility (bagian 8b butir 2).
- Langkah 20 (`Klik dropdown page size`) dan langkah 22 (`Tekan Esc untuk menutup dropdown page size`) mengikuti Langkah Uji TC (klik dropdown page size, amati pilihan, tutup dengan Esc) sehingga pilihan page size diasersi saat dropdown terbuka.
- Spec ini berjumlah 37 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- TC-FA-SU-838 diverifikasi pada level screening; overlay Column Visibility diverifikasi lengkap di spec 281 (TC-FA-SU-857), spec ini hanya membukanya dan mengasersi body kolom kosong.
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-841: keyword `Wulandari` tidak dipetakan ke nilai kolom PIC; spec mengikuti TC dan mengasumsikan A-1 dan A-3 ber-PIC `Eka W` (opsi DISTINCT PIC pada TC-FA-SU-852 hanya `Ahmad D` dan `Eka W`). TC-FA-SU-838 menyebut Name hanya untuk A-2 (`Lemari`); nama baris lain tidak tertulis di Pre-setup TC.
