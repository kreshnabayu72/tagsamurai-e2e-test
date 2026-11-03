---
id: TC-FA-LIC-E2E-105-changelog-concurrent-user-column-visibility-dan-setup
title: "Column Visibility dan Setup Column Modal Changelog Concurrent User: Screening, Ceklis, dan Geser per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-576
  - TC-FA-LIC-577
  - TC-FA-LIC-578
  - TC-FA-LIC-579
coverage:
  web: automated
---

# Column Visibility dan Setup Column Modal Changelog Concurrent User: Screening, Ceklis, dan Geser per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, pemulihan konfigurasi kolom): dinyatakan sekali di `suite.md`; spec ini merujuknya. Spec ini menyimpan konfigurasi Setup Column modal Changelog Concurrent User; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`).
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Concurrent User #31 (4 entri) lewat `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE). Kolom default (urutan awal, semua tercentang): Date, Action, User Name, Field, Old Value, New Value, Modified By.
- Tabel kolom Setup Column (dipakai langkah 14 sampai 23 dan 24 sampai 30): Date, Action, User Name, Field, Old Value, New Value, Modified By.
- State yang diubah spec: konfigurasi kolom tersimpan (visibilitas dan urutan); visibilitas dipulihkan per iterasi pada TC-FA-LIC-578 dan urutan tersimpan dihapus di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-576: Screening overlay Column Visibility

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar
2. Klik header kolom Actions `⋯`
3. Verifikasi overlay (Quick Panel) menampilkan daftar kolom berurutan: `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi setiap kolom pada overlay memiliki checkbox dan drag handle
5. Verifikasi semua kolom pada overlay tercentang
6. Verifikasi item `Setup Column...` di bagian bawah panel

### TC-FA-LIC-577: Screening popup Setup Column tiga zona

7. Klik `Setup Column...`
8. Verifikasi header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `(×)`
9. Verifikasi body memuat daftar kolom dengan checkbox
10. Verifikasi body memuat drag handle
11. Verifikasi body memuat ikon Pin
12. Verifikasi body memuat Live Preview tabel
13. Verifikasi footer: `[Reset to Default]` dan `[Save]`; tidak ada `[Cancel]`

### TC-FA-LIC-578: Ceklis dan unceklis per kolom Hideable Visible default

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 14 sampai 23):

14. Hilangkan centang kolom pada baris tabel di popup Setup Column
15. Verifikasi kolom hilang dari Live Preview
16. Klik `[Save]`
17. Verifikasi kolom hilang dari tabel
18. Muat ulang halaman (F5), buka tab Concurrent User, klik ikon Changelog pada toolbar
19. Verifikasi kolom tetap hilang setelah F5
20. Klik header kolom Actions `⋯`, klik `Setup Column...`
21. Centang kembali kolom pada baris tabel
22. Verifikasi kolom kembali tampil
23. Klik `[Save]`

### TC-FA-LIC-579: Geser (drag) per kolom Hideable Visible default

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 24 sampai 30):

24. Klik header kolom Actions `⋯`, klik `Setup Column...`
25. Seret kolom pada baris tabel ke posisi pertama
26. Verifikasi urutan kolom di Live Preview berubah sesuai seretan
27. Klik `[Save]`
28. Verifikasi urutan kolom di tabel berubah sesuai seretan
29. Muat ulang halaman (F5), buka tab Concurrent User, klik ikon Changelog pada toolbar
30. Verifikasi urutan kolom bertahan setelah F5

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 18 dan 29 membuka kembali modal sesudah F5 (modal tidak bertahan); langkah 20 dan 24 membuka popup Setup Column; langkah 21 dan 23 memulihkan visibilitas per iterasi (S-09). Langkah 7 melanjutkan overlay TC-FA-LIC-576.
- Langkah yang diulang per baris tabel kolom: langkah 14 sampai 23 (7 iterasi) dan langkah 24 sampai 30 (7 iterasi) (bagian 8b butir 7).
- Spec ini memuat 30 langkah nominal dan sekitar 132 langkah dengan ekspansi. Alasan: seluruh blok adalah Column Visibility dan Setup Column pada modal yang sama dengan dataset yang sama, dan berdiri sendiri; tiap iterasi memulihkan visibilitas atau mengganti urutan dari awal sehingga kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-578 langkah 3 menyebut "periksa tabel dan Live Preview" tanpa urutan; spec memeriksa Live Preview sebelum `[Save]` dan tabel sesudahnya.
  - TC-FA-LIC-579 meminta seret ke posisi pertama untuk kolom `Date` yang sudah berada di posisi pertama; spec mengikuti TC dan tidak menambah asersi posisi awal.
