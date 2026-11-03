---
id: TC-FA-SU-E2E-240-modal-combined-changelog-user-pagination-tooltip-icon-dan-download
title: "Modal Combined Changelog: User: Pagination, Tooltip Icon, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-728
  - TC-FA-SU-729
  - TC-FA-SU-733
coverage:
  web: automated
---

# Modal Combined Changelog: User: Pagination, Tooltip Icon, dan Download

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
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nilai sel, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-728: Pagination: page size, navigasi, dan kasus tepi

1. Klik icon Changelog di Table Tools halaman User List
2. Verifikasi default 10 baris per halaman
3. Klik dropdown page size
4. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
5. Tekan Esc untuk menutup dropdown page size
6. Isi nomor halaman `0`, tekan Enter
7. Verifikasi tabel tetap di halaman 1
8. Isi nomor halaman `-1`, tekan Enter
9. Verifikasi tabel tetap di halaman 1
10. Isi nomor halaman `999`, tekan Enter
11. Verifikasi tabel tetap di halaman 1
12. Isi nomor halaman `abc`, tekan Enter
13. Verifikasi tabel tetap di halaman 1
14. Ganti page size ke 25
15. Verifikasi tabel menampilkan halaman 1
16. Ganti page size kembali ke 10
17. Verifikasi tabel menampilkan halaman 1
18. Klik header Date satu kali
19. Verifikasi tabel menampilkan halaman 1
20. Ketik Search `Assign`, tekan Enter
21. Verifikasi tabel menampilkan halaman 1
22. Klik `(←)` pada kotak Search

### TC-FA-SU-729: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

23. Hover icon Download
24. Verifikasi tooltip ikon `Download`
25. Klik icon Download
26. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
27. Pilih `Download as CSV`
28. Verifikasi tidak ada toast sukses
29. Verifikasi file `Changelog-User.csv` terunduh
30. Klik icon Download, pilih `Download as XLSX`
31. Verifikasi tidak ada toast sukses
32. Verifikasi file `Changelog-User.xlsx` terunduh
33. Verifikasi CSV berencoding UTF-8 dengan BOM
34. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
35. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-733: Tooltip icon Table Tools dan header Actions

36. Hover icon Search
37. Verifikasi tooltip `Search`
38. Hover icon Filter
39. Verifikasi tooltip `Filter`
40. Hover icon Download
41. Verifikasi tooltip `Download`
42. Hover header kolom Actions (⋯)
43. Verifikasi tooltip `Column Visibility`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pembukaan dan penutupan dropdown page size, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- TC-FA-SU-730 ada di spec 241, TC-FA-SU-731 di spec 373, TC-FA-SU-732 di spec 368, dan TC-FA-SU-734 di spec 375.
- Spec ini berjumlah 43 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) Butir e (fixture hanya satu halaman, multi-halaman diuji di TC-FA-SU-359 dan TC-FA-SU-1057) adalah catatan tanpa langkah observasi sehingga tidak diasersi. Kata kunci Search `Assign` adalah pilihan spec. (3) Klausa Expected d TC-FA-SU-729 (BOM UTF-8, tanda kutip ganda, sheet `Sheet1`) adalah isi berkas (kelas f, binary buffer); spec menulisnya sebagai `Verifikasi` dengan kemampuan baca berkas dari tim FE. Mohon konfirmasi bila harus dipindah ke spec kelas f.
