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
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, pemulihan konfigurasi kolom): dinyatakan sekali di `suite.md`; spec ini merujuknya. Spec ini menyimpan konfigurasi Setup Column modal Changelog Concurrent User; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`).
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Concurrent User #31 (4 entri) lewat `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE). Kolom default (urutan awal, semua tercentang): Date, Action, User Name, Field, Old Value, New Value, Modified By.
- Tabel kolom Setup Column (dipakai langkah 20 sampai 32 dan 33 sampai 40): Date, Action, User Name, Field, Old Value, New Value, Modified By.
- Kemampuan teknis: seret-dan-lepas (drag and drop) item pada daftar kolom popup Setup Column (langkah 34), disediakan tim FE.
- State yang diubah spec: konfigurasi kolom tersimpan (visibilitas dan urutan); visibilitas dipulihkan per iterasi pada TC-FA-LIC-578, urutan dipulihkan per iterasi lewat `[Reset to Default]` lalu `[Save]` pada TC-FA-LIC-579, dan preferensi kolom dihapus di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-576: Screening overlay Column Visibility

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar
2. Klik header kolom Actions `⋯`
3. Verifikasi overlay (Quick Panel) menampilkan daftar kolom berurutan: `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi setiap kolom pada overlay memiliki checkbox
5. Verifikasi setiap kolom pada overlay memiliki drag handle
6. Verifikasi semua kolom pada overlay tercentang
7. Verifikasi item `Setup Column...` di bagian bawah panel

### TC-FA-LIC-577: Screening popup Setup Column tiga zona

8. Klik `Setup Column...`
9. Verifikasi header: Title `Setup Column`
10. Verifikasi header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi header: tombol `(×)`
12. Verifikasi body memuat daftar kolom dengan checkbox
13. Verifikasi body memuat drag handle
14. Verifikasi body memuat ikon Pin
15. Verifikasi body memuat Live Preview tabel
16. Verifikasi footer: `[Reset to Default]`
17. Verifikasi footer: `[Save]`
18. Verifikasi tidak ada `[Cancel]`
19. Klik `(×)` pada popup Setup Column

### TC-FA-LIC-578: Ceklis dan unceklis per kolom Hideable Visible default

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 20 sampai 32):

20. Klik header kolom Actions `⋯`, klik `Setup Column...`
21. Hilangkan centang kolom pada baris tabel di popup Setup Column
22. Verifikasi kolom hilang dari Live Preview
23. Klik `[Save]`
24. Verifikasi sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel
25. Verifikasi kolom hilang dari tabel
26. Muat ulang halaman (F5), buka tab Concurrent User, klik ikon Changelog pada toolbar
27. Verifikasi sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel
28. Verifikasi kolom tetap hilang setelah F5
29. Klik header kolom Actions `⋯`, klik `Setup Column...`
30. Centang kembali kolom pada baris tabel
31. Verifikasi kolom kembali tampil
32. Klik `[Save]`

### TC-FA-LIC-579: Geser (drag) per kolom Hideable Visible default

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 33 sampai 40):

33. Klik header kolom Actions `⋯`, klik `Setup Column...`
34. Seret kolom pada baris tabel ke posisi pertama
35. Verifikasi urutan kolom di Live Preview berubah sesuai seretan
36. Klik `[Save]`
37. Verifikasi urutan kolom di tabel berubah sesuai seretan
38. Muat ulang halaman (F5), buka tab Concurrent User, klik ikon Changelog pada toolbar
39. Verifikasi urutan kolom bertahan setelah F5
40. Klik header kolom Actions `⋯`, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 19 menutup popup Setup Column dari TC-FA-LIC-577 supaya tiap iterasi TC-FA-LIC-578 dimulai dari popup tertutup; langkah 26 dan 38 membuka kembali modal sesudah F5 (modal tidak bertahan); langkah 20, 29, 33, dan 40 membuka popup Setup Column; langkah 30 dan 32 memulihkan visibilitas per iterasi; langkah 40 memulihkan urutan kolom per iterasi lewat `[Reset to Default]` lalu `[Save]` (S-03, S-09, bagian 8b butir 14). Langkah 8 melanjutkan overlay TC-FA-LIC-576.
- Langkah yang diulang per baris tabel kolom: langkah 20 sampai 32 (7 iterasi) dan langkah 33 sampai 40 (7 iterasi) (bagian 8b butir 7).
- Asersi di luar Expected TC (S-03; 8b.2): `Verifikasi` "sedikitnya satu kolom lain (selain kolom iterasi) tampil di tabel" pada langkah 24 dan 27 mendahului asersi kolom hilang dari tabel dan kolom tetap hilang setelah F5 (anchor positif supaya tabel yang belum termuat tidak meloloskan absence).
- Spec di atas 35 langkah (40 langkah nominal dan 19 + 91 + 56 = sekitar 166 langkah dengan ekspansi). Alasan: seluruh blok adalah Column Visibility dan Setup Column pada modal yang sama dengan dataset yang sama, dan berdiri sendiri; tiap iterasi memulihkan visibilitas atau mengembalikan urutan ke default sehingga dimulai dari awal sehingga kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-578 langkah 3 menyebut "periksa tabel dan Live Preview" tanpa urutan; spec memeriksa Live Preview sebelum `[Save]` dan tabel sesudahnya.
  - TC-FA-LIC-579 meminta seret ke posisi pertama untuk kolom `Date` yang sudah berada di posisi pertama; spec mengikuti TC dan tidak menambah asersi posisi awal.
