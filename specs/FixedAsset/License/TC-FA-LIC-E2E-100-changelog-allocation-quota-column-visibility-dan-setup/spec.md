---
id: TC-FA-LIC-E2E-100-changelog-allocation-quota-column-visibility-dan-setup
title: "Column Visibility dan Setup Column Modal Changelog Allocation Quota: Screening, Ceklis, dan Geser per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-349
  - TC-FA-LIC-350
  - TC-FA-LIC-351
  - TC-FA-LIC-352
coverage:
  web: automated
---

# Column Visibility dan Setup Column Modal Changelog Allocation Quota: Screening, Ceklis, dan Geser per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, pemulihan konfigurasi kolom): dinyatakan sekali di `suite.md`; spec ini merujuknya. Spec ini menyimpan konfigurasi Setup Column modal Changelog Allocation Quota; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`).
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Allocation Quota #27 (6 entri) lewat `Fixture.fixedAssetLicense.changelogAllocationQuota` (fixture belum ada, disediakan tim FE). Kolom default (urutan awal, semua tercentang): Date, Action, Group Name, Field, Old Value, New Value, Modified By.
- Tabel kolom Setup Column (dipakai langkah 14 sampai 23 dan 24 sampai 31): Date, Action, Group Name, Field, Old Value, New Value, Modified By.
- State yang diubah spec: konfigurasi kolom tersimpan (visibilitas dan urutan); visibilitas dipulihkan per iterasi pada TC-FA-LIC-351, urutan dipulihkan per iterasi lewat `[Reset to Default]` pada TC-FA-LIC-352, dan preferensi kolom dihapus di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-349: Screening overlay Column Visibility

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota
2. Klik header kolom Actions `⋯`
3. Verifikasi overlay (Quick Panel) menampilkan daftar kolom berurutan dengan checkbox dan drag handle: `Date`, `Action`, `Group Name`, `Field`, `Old Value`, `New Value`, `Modified By` (semuanya tercentang)
4. Verifikasi item `Setup Column...` di bagian bawah panel

### TC-FA-LIC-350: Screening popup Setup Column tiga zona

5. Klik `Setup Column...`
6. Verifikasi header: Title `Setup Column`
7. Verifikasi header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
8. Verifikasi header: tombol `(×)`
9. Verifikasi body: daftar kolom dengan checkbox, drag handle, dan ikon Pin
10. Verifikasi body: Live Preview tabel
11. Verifikasi footer: `[Reset to Default]`
12. Verifikasi footer: `[Save]`
13. Verifikasi tidak ada `[Cancel]`

### TC-FA-LIC-351: Ceklis dan unceklis per kolom Hideable Visible default

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 14 sampai 23):

14. Hilangkan centang kolom pada baris tabel di popup Setup Column
15. Verifikasi kolom hilang dari Live Preview
16. Klik `[Save]`
17. Verifikasi kolom hilang dari tabel
18. Muat ulang halaman (F5), buka tab Allocation Quota, klik ikon Changelog pada toolbar Level 1 Groups Quota
19. Verifikasi kolom tetap hilang setelah F5
20. Klik header kolom Actions `⋯`, klik `Setup Column...`
21. Centang kembali kolom pada baris tabel
22. Verifikasi kolom kembali tampil
23. Klik `[Save]`

### TC-FA-LIC-352: Geser (drag) per kolom Hideable Visible default

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 24 sampai 31):

24. Klik header kolom Actions `⋯`, klik `Setup Column...`
25. Seret kolom pada baris tabel ke posisi pertama
26. Verifikasi urutan kolom di Live Preview berubah sesuai seretan: kolom itu di posisi pertama
27. Klik `[Save]`
28. Verifikasi urutan kolom di tabel berubah sesuai seretan: kolom itu di posisi pertama
29. Muat ulang halaman (F5), buka tab Allocation Quota, klik ikon Changelog pada toolbar Level 1 Groups Quota
30. Verifikasi urutan kolom bertahan setelah F5: kolom itu di posisi pertama
31. Klik header kolom Actions `⋯`, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 18 dan 29 membuka kembali modal sesudah F5 (modal tidak bertahan); langkah 20, 24, dan 31 membuka popup Setup Column; langkah 21 dan 23 memulihkan visibilitas per iterasi dan langkah 31 memulihkan urutan per iterasi lewat `[Reset to Default]` (S-09). Langkah 5 melanjutkan overlay TC-FA-LIC-349.
- Langkah yang diulang per baris tabel kolom: langkah 14 sampai 23 (7 iterasi) dan langkah 24 sampai 31 (7 iterasi) (bagian 8b butir 7).
- Spec ini memuat 31 langkah nominal dan 13 + 70 + 56 = sekitar 139 langkah dengan ekspansi. Alasan: seluruh blok adalah Column Visibility dan Setup Column pada modal yang sama dengan dataset yang sama, dan berdiri sendiri; tiap iterasi memulihkan visibilitas atau urutan (`[Reset to Default]`) sehingga dimulai dari awal sehingga kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-351 langkah 3 menyebut "periksa tabel dan Live Preview" tanpa urutan; spec memeriksa Live Preview sebelum `[Save]` dan tabel sesudahnya.
  - TC-FA-LIC-352 hanya meminta seret ke posisi pertama untuk kolom `Date` yang sudah berada di posisi pertama; spec mengikuti TC dan tidak menambah asersi posisi awal.
