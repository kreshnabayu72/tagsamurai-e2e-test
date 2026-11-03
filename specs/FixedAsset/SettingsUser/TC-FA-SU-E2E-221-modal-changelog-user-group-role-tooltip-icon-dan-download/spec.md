---
id: TC-FA-SU-E2E-221-modal-changelog-user-group-role-tooltip-icon-dan-download
title: "Modal Changelog User > Group Role: Tooltip Icon dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-665
  - TC-FA-SU-666
  - TC-FA-SU-669
coverage:
  web: automated
---

# Modal Changelog User > Group Role: Tooltip Icon dan Download

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
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nilai sel, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-665: Download format CSV dan XLSX, nama file, tanpa toast sukses

1. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Group Role, lalu klik icon Changelog
2. Hover icon Download
3. Verifikasi tooltip ikon `Download`
4. Klik icon Download
5. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `Changelog-Budi-Santoso-Group-Role.csv` terunduh
9. Klik icon Download, pilih `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `Changelog-Budi-Santoso-Group-Role.xlsx` terunduh
12. Verifikasi CSV berencoding UTF-8 dengan BOM
13. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
14. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-666: Cakupan baris dan kolom Download

15. Klik icon Download, pilih `Download as CSV`
16. Verifikasi berkas memuat seluruh baris (bukan hanya halaman aktif)
17. Verifikasi urutan baris pada berkas mengikuti sort aktif
18. Ketik Search `Assign`, tekan Enter
19. Klik icon Filter
20. Buka dropdown Modified By, centang `Ahmad D`
21. Klik `[Apply]`
22. Klik icon Download, pilih `Download as CSV`
23. Verifikasi berkas hanya memuat baris yang cocok dengan Search dan Filter (irisan Search `Assign` dan Filter Modified By `Ahmad D`)
24. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
25. Klik header Column Visibility (⋯), hilangkan centang Old Value
26. Klik icon Download, pilih `Download as CSV`
27. Verifikasi tidak ada toast peringatan
28. Verifikasi kolom Old Value tidak ikut berkas
29. Klik header Column Visibility (⋯), centang kembali Old Value
30. Klik icon Download, pilih `Download as CSV`
31. Verifikasi kolom Old Value ikut kembali pada berkas
32. Ketik Search `zzzz` (tidak ada hasil), tekan Enter
33. Klik icon Download, pilih `Download as CSV`
34. Verifikasi tidak ada toast
35. Verifikasi berkas terunduh
36. Verifikasi berkas hanya memuat baris header kolom yang visible
37. Klik `(←)` pada kotak Search

### TC-FA-SU-669: Tooltip icon Table Tools dan header Actions

38. Hover icon Search
39. Verifikasi tooltip `Search`
40. Hover icon Filter
41. Verifikasi tooltip `Filter`
42. Hover icon Download
43. Verifikasi tooltip `Download`
44. Hover header kolom Actions (⋯)
45. Verifikasi tooltip `Column Visibility`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- TC-FA-SU-667 (transformasi data Download) ada di spec 372 dan TC-FA-SU-668 (Download gagal) ada di spec 367; TC-FA-SU-670 (empty state, loading, dan error load) ada di spec 363.
- Spec ini berjumlah 45 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) Klausa Expected d TC-FA-SU-665 (BOM UTF-8, tanda kutip ganda, sheet `Sheet1`) adalah isi berkas (kelas f, binary buffer); spec menulisnya sebagai `Verifikasi` bersama nama berkas dengan kemampuan baca berkas dari tim FE. Mohon konfirmasi bila harus dipindah ke spec kelas f. (2) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (3) Search `Assign` dan Filter Modified By `Ahmad D` pada TC-FA-SU-666 tidak disertai daftar baris hasil; spec mengasersi irisan kedua kontrol tanpa menyebut baris tertentu.
