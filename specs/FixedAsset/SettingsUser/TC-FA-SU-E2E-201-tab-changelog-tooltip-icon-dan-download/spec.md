---
id: TC-FA-SU-E2E-201-tab-changelog-tooltip-icon-dan-download
title: "Tab Changelog: Tooltip Icon dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-601
  - TC-FA-SU-602
  - TC-FA-SU-605
coverage:
  web: automated
---

# Tab Changelog: Tooltip Icon dan Download

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
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nilai sel, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-601: Download format CSV dan XLSX, nama file, tanpa toast sukses

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
3. Hover icon Download
4. Verifikasi tooltip ikon `Download`
5. Klik icon Download
6. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
7. Pilih `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi file `Changelog-Budi-Santoso.csv` terunduh
10. Klik icon Download, pilih `Download as XLSX`
11. Verifikasi tidak ada toast sukses
12. Verifikasi file `Changelog-Budi-Santoso.xlsx` terunduh
13. Verifikasi CSV berencoding UTF-8 dengan BOM
14. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
15. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-602: Cakupan baris dan kolom Download

16. Klik icon Download, pilih `Download as CSV`
17. Verifikasi berkas memuat seluruh baris (bukan hanya halaman aktif)
18. Verifikasi urutan baris pada berkas mengikuti sort aktif
19. Ketik Search `Home`, tekan Enter
20. Klik icon Filter
21. Buka dropdown Modified By, centang `Lina M`
22. Klik `[Apply]`
23. Klik icon Download, pilih `Download as CSV`
24. Verifikasi berkas hanya memuat baris yang cocok dengan Search dan Filter (irisan Search `Home` dan Filter Modified By `Lina M`)
25. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
26. Klik header Column Visibility (⋯), hilangkan centang Old Value
27. Klik icon Download, pilih `Download as CSV`
28. Verifikasi tidak ada toast peringatan
29. Verifikasi kolom Old Value tidak ikut berkas
30. Klik header Column Visibility (⋯), centang kembali Old Value
31. Klik icon Download, pilih `Download as CSV`
32. Verifikasi kolom Old Value ikut kembali pada berkas
33. Ketik Search `zzzz` (tidak ada hasil), tekan Enter
34. Klik icon Download, pilih `Download as CSV`
35. Verifikasi tidak ada toast
36. Verifikasi berkas terunduh
37. Verifikasi berkas hanya memuat baris header kolom yang visible
38. Klik `(←)` pada kotak Search

### TC-FA-SU-605: Tooltip icon Table Tools dan header Actions

39. Hover icon Search
40. Verifikasi tooltip `Search`
41. Hover icon Filter
42. Verifikasi tooltip `Filter`
43. Hover icon Download
44. Verifikasi tooltip `Download`
45. Hover header kolom Actions (⋯)
46. Verifikasi tooltip `Column Visibility`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- Spec ini berjumlah 46 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) Klausa Expected d (BOM UTF-8, tanda kutip ganda, sheet `Sheet1`) adalah isi berkas (kelas f, binary buffer) sedangkan penempatan awal menaruhnya di spec fungsional bersama nama berkas; spec menulisnya sebagai `Verifikasi` dengan kemampuan baca berkas dari tim FE. Mohon konfirmasi bila harus dipindah ke spec kelas f. (2) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (3) TC-FA-SU-602 tidak menyebut nilai Search dan Filter; spec memilih Search `Home`, Filter Modified By `Lina M`, dan keyword tanpa hasil `zzzz`.
