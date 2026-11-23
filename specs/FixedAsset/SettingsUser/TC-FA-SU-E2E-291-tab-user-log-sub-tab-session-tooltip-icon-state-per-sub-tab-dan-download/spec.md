---
id: TC-FA-SU-E2E-291-tab-user-log-sub-tab-session-tooltip-icon-state-per-sub-tab-dan-download
title: "Tab User Log sub-tab Session: Tooltip Icon, State per Sub-tab, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-888
  - TC-FA-SU-892
  - TC-FA-SU-894
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Tooltip Icon, State per Sub-tab, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Session Budi Santoso (Pre-setup #30, 9 baris; urutan default Date descending). Label baris = `Date|Note` (kolom Activity bernilai `Session`, kolom Status bernilai `—`); alias dipakai langkah:
  - S-1: `16/07/26 08:12|Session started`
  - S-2: `15/07/26 20:30|Session ended`
  - S-3: `15/07/26 08:00|Session started`
  - S-4: `14/07/26 08:40|Session ended`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-5: `14/07/26 08:05|Session started`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-6: `13/07/26 17:05|Session ended`
  - S-7: `13/07/26 08:10|Session started`
  - S-8: `12/07/26 17:15|Session ended`
  - S-9: `12/07/26 08:02|Session started`
- Seed Tab User Log sub-tab Assignment Budi Santoso (dipakai sebagai sub-tab pembanding pada TC-FA-SU-894; hasilnya tidak diasersi) (Pre-setup #30, 5 baris; urutan default Date descending). Label baris = `Activity|Transaction ID`; alias dipakai langkah:
  - A-1: `Unassigned|ASG-20260618-0089`, Date `30/06/26`, PIC `Eka W` (keyword `Wulandari`)
  - A-2: `Handed over|ASG-20260625-0102`, Name `Lemari`, PIC `Ahmad D`
  - A-3: `Handed over|ASG-20260618-0089`, PIC `Eka W` (keyword `Wulandari`)
  - A-4: `Handed over|ASG-20260512-0067`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
  - A-5: `Handed over|ASG-20260505-0045`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-888: Download: format CSV dan XLSX, nama file, dan tanpa toast sukses

1. Ketik Search `Budi Santoso`, tekan Enter, klik nama Budi Santoso, lalu klik tab User Log, sub-tab Session
2. Hover icon Download
3. Verifikasi tooltip ikon `Download`
4. Klik icon Download
5. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `User-Log-Budi-Santoso.csv` terunduh
9. Klik icon Download, pilih `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `User-Log-Budi-Santoso.xlsx` terunduh
12. Verifikasi CSV berencoding UTF-8 dengan BOM
13. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
14. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-892: Tooltip icon Table Tools dan header Actions

15. Hover icon Search
16. Verifikasi tooltip `Search`
17. Hover icon Filter
18. Verifikasi tooltip `Filter`
19. Hover icon Download
20. Verifikasi tooltip `Download`
21. Hover header kolom Actions (⋯)
22. Verifikasi tooltip `Column Visibility`

### TC-FA-SU-894: State sub-tab dipertahankan per sub-tab

23. Ketik Search `ended`, tekan Enter
24. Klik icon Filter, pilih rentang 12/07/26 sampai 13/07/26 pada Date
25. Klik `[Apply]`
26. Klik header Note satu kali
27. Ganti page size ke 25
28. Pindah ke sub-tab Assignment
29. Ketik Search `Unassigned`, tekan Enter
30. Klik header Date satu kali
31. Kembali ke sub-tab Session
32. Verifikasi Search `ended` sub-tab Session dipulihkan
33. Verifikasi Filter Date sub-tab Session dipulihkan
34. Verifikasi Sort Note sub-tab Session dipulihkan
35. Verifikasi page size 25 sub-tab Session dipulihkan
36. Verifikasi state sub-tab Session tidak memengaruhi sub-tab Assignment (Search `Unassigned` dan Sort Date sub-tab Assignment tetap)
37. Klik Back breadcrumb ke List, buka Detail pengguna Budi Santoso lagi, klik tab User Log, sub-tab Session
38. Verifikasi state sub-tab Session (Search, Filter, Sort, page size) dipulihkan setelah Back breadcrumb
39. Tekan F5 pada halaman Detail
40. Verifikasi state sub-tab Session dipulihkan setelah refresh F5
41. Klik menu Settings > User pada sidebar, ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso lagi, klik tab User Log, sub-tab Session
42. Verifikasi state sub-tab Session kembali ke default setelah keluar lewat menu sidebar

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung tambahan (S-03, R-16, bagian 8b butir 13): langkah 1 dan 41 mengetik Search `Budi Santoso` lalu Enter supaya baris Budi Santoso tampil di User List (25 baris) sebelum nama diklik (langkah 41 "ketik Search" karena sesudah menu sidebar kotak Search kosong).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 42 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC-FA-SU-888: klausa BOM UTF-8, tanda kutip ganda, dan sheet `Sheet1` adalah isi berkas (kelas f); spec menulisnya sebagai `Verifikasi` dengan kemampuan baca berkas dari tim FE. TC-FA-SU-894: Langkah Uji 2 menyebut "kontrol berbeda" pada sub-tab lain tanpa nilai; spec memakai Search `Unassigned` dan Sort Date pada sub-tab Assignment, dan nomor halaman aktif tidak diuji (fixture satu halaman).
