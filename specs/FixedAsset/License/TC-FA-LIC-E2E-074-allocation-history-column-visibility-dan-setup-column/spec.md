---
id: TC-FA-LIC-E2E-074-allocation-history-column-visibility-dan-setup-column
title: "Allocation History: Overlay Column Visibility, Popup Setup Column, serta Ceklis dan Geser per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-249
  - TC-FA-LIC-250
  - TC-FA-LIC-251
  - TC-FA-LIC-252
coverage:
  web: automated
---
# Allocation History: Overlay Column Visibility, Popup Setup Column, serta Ceklis dan Geser per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Pemulihan konfigurasi kolom: konfigurasi Setup Column atau Column Visibility yang disimpan spec ini didaftarkan di `suite.md`; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Daftar kolom Hideable Visible default (parameter langkah 16 sampai 26 dan 27 sampai 34): `Allocation ID`, `Subscription ID`, `License Type`, `Quantity`, `Status`, `Date`, `End Date`, `Plan Owner`, `Last Updated` (sembilan kolom). Untuk kolom `Allocation ID` yang sudah berada di posisi pertama, langkah seret ke posisi pertama tidak mengubah urutan.
- State yang diubah dan dipulihkan: visibilitas dan urutan kolom Setup Column (setiap iterasi memulihkannya pada langkah 26 dan 34; didaftarkan di `suite.md`).

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-249: Screening overlay Column Visibility

2. Klik header kolom Actions `⋯`
3. Verifikasi overlay menampilkan daftar kolom berurutan: `Allocation ID`, `Subscription ID`, `License Type`, `Quantity`, `Status`, `Date`, `End Date`, `Plan Owner`, `Last Updated`
4. Verifikasi tiap kolom pada daftar memiliki checkbox tercentang dan drag handle
5. Verifikasi item `Setup Column...` di bagian bawah panel
6. Tutup overlay Column Visibility

### TC-FA-LIC-250: Screening Popup Setup Column

7. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
8. Verifikasi Title header popup `Setup Column`
9. Verifikasi deskripsi header `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
10. Verifikasi tombol `(×)` pada header
11. Verifikasi body memuat daftar kolom dengan checkbox, drag handle, dan ikon Pin
12. Verifikasi body memuat Live Preview tabel
13. Verifikasi footer memuat `[Reset to Default]` dan `[Save]`
14. Verifikasi footer tidak memuat `[Cancel]`
15. Klik `(×)` untuk menutup popup

### TC-FA-LIC-251: Ceklis dan unceklis per kolom

Untuk setiap kolom pada daftar kolom (langkah 16 sampai 26):

16. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
17. Hilangkan centang kolom
18. Verifikasi kolom hilang dari Live Preview
19. Klik `[Save]`
20. Verifikasi kolom hilang dari tabel
21. Muat ulang halaman (F5), lalu klik sub-tab `Allocation History`
22. Verifikasi kolom tetap hilang dari tabel
23. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
24. Centang kembali kolom
25. Verifikasi kolom kembali tampil di Live Preview
26. Klik `[Save]`

### TC-FA-LIC-252: Geser (drag) per kolom

Untuk setiap kolom pada daftar kolom (langkah 27 sampai 34):

27. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
28. Seret kolom ke posisi pertama
29. Verifikasi urutan kolom di Live Preview berubah sesuai seretan
30. Klik `[Save]`
31. Verifikasi urutan kolom di tabel berubah sesuai seretan
32. Muat ulang halaman (F5), lalu klik sub-tab `Allocation History`
33. Verifikasi urutan kolom di tabel bertahan sesuai seretan
34. Klik header kolom Actions `⋯`, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (34 langkah nominal; 186 langkah setelah ekspansi). Alasan: seluruh blok satu topik (Column Visibility dan Setup Column Allocation History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri, dan langkah 16 sampai 26 serta 27 sampai 34 diulang per kolom (sembilan iterasi) dengan parameter di daftar kolom `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 6 dan 15 (menutup overlay dan popup), langkah 21 dan 32 (klik sub-tab sesudah muat ulang agar sub-tab aktif deterministik), langkah 26 (memulihkan kolom; S-09), dan langkah 34 (memulihkan urutan kolom lewat `[Reset to Default]` lalu `[Save]`; S-09).
- Temuan untuk QA:
  - TC-FA-LIC-252 meminta seret kolom `Allocation ID` ke posisi pertama padahal kolom itu sudah pertama; hasil "urutan berubah sesuai seretan" tidak memiliki perubahan yang teramati untuk iterasi itu.
  - TC-FA-LIC-251 menulis "tampilkan kembali" tanpa menyebut `Verifikasi` tabel setelah `[Save]` ulang; spec mengasersi kembali tampil di Live Preview (Expected TC: "kembali tampil saat dicentang ulang") dan menyimpan ulang sebagai pemulihan.
  - TC-FA-LIC-249, 250, 251, dan 252 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
