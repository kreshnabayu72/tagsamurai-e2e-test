---
id: TC-FA-COA-E2E-055-download-tabel-isi-berkas-mengikuti-search-filter-sort-dan-kolom
title: "Download Tabel: Isi Berkas mengikuti Search, Filter, Sort, dan Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-84
  - TC-FA-COA-85
  - TC-FA-COA-86
  - TC-FA-COA-223
  - TC-FA-COA-224
  - TC-FA-COA-334
coverage:
  web: automated
---

# Download Tabel: Isi Berkas mengikuti Search, Filter, Sort, dan Kolom

## Prerequisites

- Mode: FE+BE (TC-86 memakai `Spectra.intercept()` untuk memaksa respons Download gagal di atas backend nyata).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Akun Pre-setup (hanya dibaca dan tidak diubah; kunci fixture `Fixture.settingsChartOfAccounts.<kunci>` ditetapkan tim FE):

  | Akun | Account Code | Kondisi |
  |---|---|---|
  | P1 | `5-6001` | Active, Last Used in Journal kosong |
  | P2 | `6-2001` | Active, Last Used in Journal `Aug 2026` |
  | P3 | `4-7001` | Inactive |
  | P4 | `1-1002` | Inactive, Last Used in Journal `Mar 2025` |
  | P5 | `CAP-6100` | Active |

- Kemampuan teknis: membaca isi berkas CSV dan XLSX yang terunduh (nama berkas, baris, kolom, nilai sel) dan mencegat respons Download; disediakan tim FE.
- State yang diubah spec: konfigurasi kolom (Used By disembunyikan pada langkah 19 sampai 21 dan 35 sampai 37, ditampilkan kembali pada langkah 27 dan 38 sampai 40). Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE). Filter dan Search dibersihkan di antara blok.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-84: Download CSV mengikuti Filter dan kolom visible

1. Klik ikon Filter, pilih Active = Active, lalu klik Apply
2. Verifikasi sedikitnya satu baris tampil di tabel
3. Klik ikon Download, lalu pilih `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas bernama `Chart-of-Accounts` terunduh
6. Verifikasi berkas hanya memuat baris Active (baris P1 ada, baris P3 tidak ada)
7. Verifikasi berkas hanya memuat kolom yang visible, termasuk Used By
8. Verifikasi Switch Status ditulis `Active`
9. Verifikasi Last Used in Journal ditulis periode `MMM YYYY` (baris P2 `Aug 2026`) dan sel kosong ditulis `-` (baris P1)

### TC-FA-COA-85: Download XLSX dengan hasil kosong

10. Klik `Clear all` pada filter aktif
11. Ketik Search `zzz`, tekan Enter
12. Verifikasi tabel menampilkan "No results found"
13. Klik ikon Download, lalu pilih `Download as XLSX`
14. Verifikasi berkas XLSX terunduh berisi baris header saja

### TC-FA-COA-86: Download gagal

15. Aktifkan intercept yang memaksa respons Download gagal
16. Klik ikon Download, lalu pilih `Download as CSV`
17. Verifikasi toast "Error, failed to download Chart-of-Accounts."
18. Lepas intercept

### TC-FA-COA-224: Download dengan nol baris

19. Klik header Actions ⋯ > `Setup Column...`
20. Hapus centang kolom Used By
21. Klik `[Save]`
22. Verifikasi tabel masih menampilkan "No results found" untuk Search `zzz`
23. Verifikasi tombol Download aktif
24. Klik ikon Download, lalu pilih `Download as CSV`
25. Verifikasi tidak ada toast
26. Verifikasi berkas CSV hanya berisi satu baris header berisi kolom yang visible (tanpa Used By)
27. Klik header Actions ⋯ > `Setup Column...`, centang kolom Used By, lalu klik `[Save]`

### TC-FA-COA-223: Download mengikuti Sort

28. Klik `(←)` pada kotak Search
29. Klik header Account Code dua kali (indikator ↓)
30. Klik ikon Download, lalu pilih `Download as CSV`
31. Verifikasi baris berkas berurutan Z-A menurut Account Code, sama dengan tabel
32. Klik header Account Code sekali lagi (kembali ke default)
33. Klik ikon Download, lalu pilih `Download as CSV`
34. Verifikasi baris berkas berurutan default Account Code A-Z

### TC-FA-COA-334: Download setelah hide lalu unhide kolom

35. Klik header Actions ⋯ > `Setup Column...`
36. Hapus centang kolom Used By
37. Klik `[Save]`
38. Klik header Actions ⋯ > `Setup Column...`
39. Centang kolom Used By
40. Klik `[Save]`
41. Klik ikon Download, lalu pilih `Download as CSV`
42. Verifikasi tidak ada toast sukses
43. Verifikasi berkas CSV memuat kolom Used By

## Notes

- Alasan spec di atas sekitar 35 langkah (43 langkah): semua blok satu tombol Download pada satu tabel, satu dataset, dan tiap TC memulai dari state bersih (filter, Search, dan kolom dipulihkan di antara blok); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-10: TC-84, TC-85, TC-223, TC-224, dan TC-334 mencampur asersi UI (tombol, toast, empty state) dengan isi berkas (kelas f) pada alur unduh yang sama; alur klik Download lalu membaca berkas tidak dapat dipisah dari asersi UI. Klausa isi berkas ditaruh setelah klausa UI dan `Verifikasi` isi berkas satu per klausa.
- P-5: TC-86 adalah satu objek uji ringan kelas b (respons Download dipaksa gagal) pada permukaan yang sama (Download); intercept dilepas pada langkah 18.
- Asersi absence toast pada langkah 4, 25, dan 42 diletakkan segera setelah pemicu (klik pilihan format) sebelum asersi berkas; berkas terunduh (langkah 5, 26, 43) menjadi bukti positif bahwa respons sudah diproses (8b.11).
- Langkah penghubung (S-03): langkah 1 dan 10 (Filter dipasang dan dibersihkan), langkah 11 dan 28 (Search `zzz` dibuat dan dikosongkan), langkah 19 sampai 21 (menyiapkan precondition c TC-224), langkah 27 (pemulihan Setup Column eksplisit, R-24 dan 8b.14), langkah 35 sampai 40 (hide lalu unhide, langkah TC-334).
- Temuan untuk QA:
  - TC-84 butir b ("hanya baris Active") tidak menyebut jumlah baris; spec mengasersi dengan baris pembanding P1 (ada) dan P3 (tidak ada).
  - TC-224 mensyaratkan Search `zzz` pada langkah 1 dengan state Used By disembunyikan sebagai precondition; spec mempertahankan Search `zzz` dari TC-85 (langkah 11) dan menyembunyikan Used By pada langkah 20 sampai 21.
  - TC-85 dan TC-86 tidak memuat Post Condition yang membutuhkan observasi.
