---
id: TC-FA-LIC-E2E-059-download-riwayat-subscription-dan-allocation-cakupan
title: "Download Riwayat Subscription dan Allocation: Cakupan Seluruh Baris, Mengikuti Search, dan Kolom yang Disembunyikan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-222
  - TC-FA-LIC-223
  - TC-FA-LIC-226
  - TC-FA-LIC-227
coverage:
  web: automated
---

# Download Riwayat Subscription dan Allocation: Cakupan Seluruh Baris, Mengikuti Search, dan Kolom yang Disembunyikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (hanya dibaca): 4 term Subscription (SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001) dan 6 alokasi (LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001), lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE).
- Data Dinamis (milik spec, dibuat di hook `before` oleh fixture BE yang disediakan tim FE/BE, dihapus di hook `after`):
  - 25 baris Subscription History tambahan: 22 baris dengan Plan Owner `PT Uji Lain {runId}-059` dan 3 baris dengan Plan Owner `PT Uji Tiga {runId}-059`. Total baris Subscription History 29 (4 + 25). Search `PT Uji Tiga {runId}-059` menyisakan tepat 3 baris (kata kunci dipilih spec karena TC hanya menulis "Search/Filter yang menyisakan 3 baris").
  - 25 baris Allocation History tambahan dengan pola yang sama (22 baris `PT Uji Lain {runId}-059`, 3 baris `PT Uji Tiga {runId}-059`). Total baris Allocation History 31 (6 + 25).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV dan XLSX (nama berkas, baris header, jumlah baris); berkas tiap unduhan ditangkap ke direktori bersih; pemulihan preferensi kolom di browser di hook `after`.
- State yang diubah dan dipulihkan: Search tiap tabel (dibersihkan pada langkah 13 dan 34) dan visibilitas kolom `Plan Owner` (dipulihkan pada langkah 18 dan 39).

## Test Steps

### TC-FA-LIC-222: Cakupan seluruh baris Subscription History

1. Klik sub-tab `Subscription History`
2. Klik ikon Download pada toolbar tabel, lalu pilih `Download as CSV` (tanpa Search dan Filter)
3. Verifikasi tidak ada toast sukses
4. Verifikasi berkas `License-Subscription-History.csv` terunduh
5. Buka isi berkas yang terunduh
6. Verifikasi berkas memuat seluruh 29 baris data (bukan hanya 10 baris halaman aktif)
7. Ketik Search `PT Uji Tiga {runId}-059`, tekan Enter
8. Verifikasi tabel menampilkan tiga baris
9. Klik ikon Download pada toolbar tabel, lalu pilih `Download as CSV`
10. Verifikasi tidak ada toast sukses
11. Buka isi berkas yang terunduh
12. Verifikasi berkas kedua hanya memuat tiga baris yang cocok dengan Search
13. Klik `(←)` pada kotak Search

### TC-FA-LIC-223: Kolom yang disembunyikan pada Subscription History

14. Klik header kolom Actions `⋯`, hilangkan centang `Plan Owner`, lalu tutup overlay
15. Klik ikon Download pada toolbar tabel, pilih `Download as XLSX`, lalu buka berkas yang terunduh
16. Verifikasi berkas memuat kolom `Subscription ID`, `Plan`, `Type`, `Status`, `Start Date`, dan `End Date`
17. Verifikasi berkas `License-Subscription-History.xlsx` tidak memuat kolom `Plan Owner`
18. Klik header kolom Actions `⋯`, centang kembali `Plan Owner`, lalu tutup overlay
19. Klik ikon Download pada toolbar tabel, pilih `Download as CSV`, lalu buka berkas yang terunduh
20. Verifikasi berkas `License-Subscription-History.csv` memuat kolom `Plan Owner`
21. Verifikasi ekstensi berkas mengikuti pilihan format (`.xlsx` untuk `Download as XLSX`, `.csv` untuk `Download as CSV`)

### TC-FA-LIC-226: Cakupan seluruh baris Allocation History

22. Klik sub-tab `Allocation History`
23. Klik ikon Download pada toolbar tabel, lalu pilih `Download as CSV` (tanpa Search dan Filter)
24. Verifikasi tidak ada toast sukses
25. Verifikasi berkas `License-Allocation-History.csv` terunduh
26. Buka isi berkas yang terunduh
27. Verifikasi berkas memuat seluruh 31 baris data (bukan hanya 10 baris halaman aktif)
28. Ketik Search `PT Uji Tiga {runId}-059`, tekan Enter
29. Verifikasi tabel menampilkan tiga baris
30. Klik ikon Download pada toolbar tabel, lalu pilih `Download as CSV`
31. Verifikasi tidak ada toast sukses
32. Buka isi berkas yang terunduh
33. Verifikasi berkas kedua hanya memuat tiga baris yang cocok dengan Search
34. Klik `(←)` pada kotak Search

### TC-FA-LIC-227: Kolom yang disembunyikan pada Allocation History

35. Klik header kolom Actions `⋯`, hilangkan centang `Plan Owner`, lalu tutup overlay
36. Klik ikon Download pada toolbar tabel, pilih `Download as XLSX`, lalu buka berkas yang terunduh
37. Verifikasi berkas memuat kolom `Allocation ID`, `Subscription ID`, `License Type`, `Quantity`, `Status`, `Date`, `End Date`, dan `Last Updated`
38. Verifikasi berkas `License-Allocation-History.xlsx` tidak memuat kolom `Plan Owner`
39. Klik header kolom Actions `⋯`, centang kembali `Plan Owner`, lalu tutup overlay
40. Klik ikon Download pada toolbar tabel, pilih `Download as CSV`, lalu buka berkas yang terunduh
41. Verifikasi berkas `License-Allocation-History.csv` memuat kolom `Plan Owner`
42. Verifikasi ekstensi berkas mengikuti pilihan format (`.xlsx` untuk `Download as XLSX`, `.csv` untuk `Download as CSV`)

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (42 langkah). Alasan: seluruh blok satu kelas harness (fungsional Download riwayat) dan dua tabel dengan pola identik (Subscription History dan Allocation History) yang masing-masing berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tiap Verifikasi sesuai satu klausa Expected TC (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 22 (klik sub-tab sebagai aksi deterministik), langkah 5, 11, 15, 19, 26, 32, 36, dan 40 (membuka isi berkas), langkah 13 dan 34 (pemulihan Search; S-09), langkah 14, 18, 35, dan 39 (menyembunyikan atau memulihkan kolom `Plan Owner` serta menutup overlay Column Visibility).
- Absence state sementara (bagian 8b butir 11 dan 5): toast sukses diasersi segera setelah pemicu dan sebelum asersi berkas (langkah 3, 10, 24, dan 31); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 4, 6, 12, 25, 27, dan 33).
- Asersi di luar Expected TC (S-03): langkah 16 dan 37 (berkas memuat kolom lain) adalah anchor positif untuk asersi absence kolom `Plan Owner` pada langkah 17 dan 38 (bagian 8b butir 2); langkah 8 dan 29 (tabel menampilkan tiga baris) membuktikan Search menyisakan tiga baris sebelum berkas kedua diasersi.
- Temuan untuk QA:
  - TC-FA-LIC-222 dan TC-FA-LIC-226 menulis "Search/Filter yang menyisakan 3 baris" tanpa menyebut kata kunci dan data; spec merancang 25 baris tambahan dengan Plan Owner `PT Uji Tiga {runId}-059` untuk 3 baris yang disisakan.
  - TC-FA-LIC-222 dan TC-FA-LIC-226 menulis "ditambah 25 baris fixture" tanpa menyebut isi baris; mekanisme seeding disediakan tim FE/BE (S-13).
  - Kasus "nol baris tetap unduh header" ada di spec 060 (TC-FA-LIC-224 dan TC-FA-LIC-228).
  - TC-FA-LIC-222, 223, 226, dan 227 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
