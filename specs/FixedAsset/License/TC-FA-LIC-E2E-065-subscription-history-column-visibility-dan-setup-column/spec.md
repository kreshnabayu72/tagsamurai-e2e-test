---
id: TC-FA-LIC-E2E-065-subscription-history-column-visibility-dan-setup-column
title: "Subscription History: Overlay Column Visibility, Popup Setup Column, serta Ceklis dan Geser per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-206
  - TC-FA-LIC-207
  - TC-FA-LIC-208
  - TC-FA-LIC-209
coverage:
  web: automated
---
# Subscription History: Overlay Column Visibility, Popup Setup Column, serta Ceklis dan Geser per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Pemulihan konfigurasi kolom: konfigurasi Setup Column atau Column Visibility yang disimpan spec ini didaftarkan di `suite.md`; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Daftar kolom Hideable Visible default (parameter langkah 17 sampai 29 dan 30 sampai 37): `Subscription ID`, `Plan`, `Type`, `Status`, `Start Date`, `End Date`, `Plan Owner` (tujuh kolom). Untuk kolom `Subscription ID` yang sudah berada di posisi pertama, langkah seret ke posisi pertama tidak mengubah urutan.
- Kemampuan teknis (disediakan tim FE): seret-dan-lepas baris kolom pada popup Setup Column, pembacaan Live Preview tabel di popup itu, dan muat ulang halaman (F5).
- State yang diubah dan dipulihkan: visibilitas dan urutan kolom Setup Column (setiap iterasi memulihkannya pada langkah 29 dan 37; didaftarkan di `suite.md`).

## Test Steps

1. Klik sub-tab `Subscription History`

### TC-FA-LIC-206: Screening overlay Column Visibility

2. Klik header kolom Actions `⋯`
3. Verifikasi overlay menampilkan daftar kolom berurutan: `Subscription ID`, `Plan`, `Type`, `Status`, `Start Date`, `End Date`, `Plan Owner`
4. Verifikasi tiap kolom pada daftar memiliki checkbox tercentang dan drag handle
5. Verifikasi item `Setup Column...` di bagian bawah panel
6. Tutup overlay Column Visibility

### TC-FA-LIC-207: Screening Popup Setup Column

7. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
8. Verifikasi Title header popup `Setup Column`
9. Verifikasi deskripsi header `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
10. Verifikasi tombol `(×)` pada header
11. Verifikasi body memuat daftar kolom dengan checkbox, drag handle, dan ikon Pin
12. Verifikasi body memuat Live Preview tabel
13. Verifikasi footer memuat `[Reset to Default]`
14. Verifikasi footer memuat `[Save]`
15. Verifikasi footer tidak memuat `[Cancel]`
16. Klik `(×)` untuk menutup popup

### TC-FA-LIC-208: Ceklis dan unceklis per kolom

Untuk setiap kolom pada daftar kolom (langkah 17 sampai 29):

17. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
18. Hilangkan centang kolom
19. Verifikasi kolom hilang dari Live Preview
20. Klik `[Save]`
21. Verifikasi sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel
22. Verifikasi kolom hilang dari tabel
23. Muat ulang halaman (F5)
24. Verifikasi sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel
25. Verifikasi kolom tetap hilang dari tabel
26. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
27. Centang kembali kolom
28. Verifikasi kolom kembali tampil di Live Preview
29. Klik `[Save]`

### TC-FA-LIC-209: Geser (drag) per kolom

Untuk setiap kolom pada daftar kolom (langkah 30 sampai 37):

30. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
31. Seret kolom ke posisi pertama
32. Verifikasi urutan kolom di Live Preview berubah sesuai seretan
33. Klik `[Save]`
34. Verifikasi urutan kolom di tabel berubah sesuai seretan
35. Muat ulang halaman (F5)
36. Verifikasi urutan kolom di tabel bertahan sesuai seretan
37. Klik header kolom Actions `⋯`, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (37 langkah nominal; 163 langkah setelah ekspansi). Alasan: seluruh blok satu topik (Column Visibility dan Setup Column Subscription History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri, dan langkah 17 sampai 29 serta 30 sampai 37 diulang per kolom (tujuh iterasi) dengan parameter di daftar kolom `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 6 dan 16 (menutup overlay dan popup), langkah 29 (memulihkan kolom; S-09), dan langkah 37 (memulihkan urutan kolom lewat `[Reset to Default]` lalu `[Save]`; S-09).
- Asersi di luar Expected TC (S-03; 8b.2): `Verifikasi` "sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel" pada langkah 21 dan 24 mendahului asersi kolom hilang (anchor positif supaya tabel yang belum termuat tidak meloloskan absence).
- Temuan untuk QA:
  - TC-FA-LIC-209 meminta seret kolom `Subscription ID` ke posisi pertama padahal kolom itu sudah pertama; hasil "urutan berubah sesuai seretan" tidak memiliki perubahan yang teramati untuk iterasi itu.
  - TC-FA-LIC-208 menulis "tampilkan kembali" tanpa menyebut `Verifikasi` tabel setelah `[Save]` ulang; spec mengasersi kembali tampil di Live Preview (Expected TC: "kembali tampil saat dicentang ulang") dan menyimpan ulang sebagai pemulihan.
  - TC-FA-LIC-206, 207, 208, dan 209 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
