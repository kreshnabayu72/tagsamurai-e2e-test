---
id: TC-FA-SU-E2E-250-tab-system-log-pagination-tooltip-icon-dan-download
title: "Tab System Log: Pagination, Tooltip Icon, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-758
  - TC-FA-SU-759
  - TC-FA-SU-763
coverage:
  web: automated
---

# Tab System Log: Pagination, Tooltip Icon, dan Download

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
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nilai sel, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-758: Pagination: page size, navigasi, dan kasus tepi

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab System Log
3. Verifikasi default 10 baris per halaman
4. Klik dropdown page size
5. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
6. Tutup dropdown page size dengan Esc
7. Isi nomor halaman `0`, tekan Enter
8. Verifikasi tabel tetap di halaman 1
9. Isi nomor halaman `-1`, tekan Enter
10. Verifikasi tabel tetap di halaman 1
11. Isi nomor halaman `999`, tekan Enter
12. Verifikasi tabel tetap di halaman 1
13. Isi nomor halaman `abc`, tekan Enter
14. Verifikasi tabel tetap di halaman 1
15. Ganti page size ke 25
16. Verifikasi tabel menampilkan halaman 1
17. Ganti page size kembali ke 10
18. Verifikasi tabel menampilkan halaman 1
19. Klik header Date satu kali
20. Verifikasi tabel menampilkan halaman 1
21. Ketik Search `Assign`, tekan Enter
22. Verifikasi tabel menampilkan halaman 1
23. Klik `(←)` pada kotak Search

### TC-FA-SU-759: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

24. Hover icon Download
25. Verifikasi tooltip ikon `Download`
26. Klik icon Download
27. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
28. Pilih `Download as CSV`
29. Verifikasi tidak ada toast sukses
30. Verifikasi file `System-Log-Budi-Santoso.csv` terunduh
31. Klik icon Download, pilih `Download as XLSX`
32. Verifikasi tidak ada toast sukses
33. Verifikasi file `System-Log-Budi-Santoso.xlsx` terunduh
34. Verifikasi CSV berencoding UTF-8 dengan BOM
35. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
36. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-763: Tooltip icon Table Tools dan header Actions

37. Hover icon Search
38. Verifikasi tooltip `Search`
39. Hover icon Filter
40. Verifikasi tooltip `Filter`
41. Hover icon Download
42. Verifikasi tooltip `Download`
43. Hover header kolom Actions (⋯)
44. Verifikasi tooltip `Column Visibility`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay dan dropdown page size (Esc), pembukaan dropdown page size sebelum asersi pilihannya, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (Ketik Search `Budi Santoso` di User List untuk menemukan baris target sebelum membuka Detail, R-16, butir 8b.13); User List memuat 25 pengguna pada 3 halaman sehingga posisi baris tidak diandalkan.
- TC-FA-SU-760 ada di spec 251, TC-FA-SU-761 di spec 373, TC-FA-SU-762 di spec 368, dan TC-FA-SU-764 di spec 364.
- Spec ini berjumlah 44 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) TC-FA-SU-758 mengisi nomor halaman `0`, `-1`, `999`, dan `abc`; spec mengikuti Langkah Uji dan Data Uji. Butir e (fixture hanya satu halaman, multi-halaman diuji di TC-FA-SU-359 dan TC-FA-SU-1057) adalah catatan tanpa langkah observasi sehingga tidak diasersi. Kata kunci Search `Assign` adalah pilihan spec. (3) Klausa Expected d TC-FA-SU-759 (BOM UTF-8, tanda kutip ganda, sheet `Sheet1`) adalah isi berkas (kelas f, binary buffer); spec menulisnya sebagai `Verifikasi` dengan kemampuan baca berkas dari tim FE. Mohon konfirmasi bila harus dipindah ke spec kelas f.
