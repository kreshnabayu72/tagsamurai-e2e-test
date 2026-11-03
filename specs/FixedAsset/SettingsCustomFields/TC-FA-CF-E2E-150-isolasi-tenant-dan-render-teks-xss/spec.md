---
id: TC-FA-CF-E2E-150-isolasi-tenant-dan-render-teks-xss
title: "Isolasi Tenant dan Render Teks untuk Payload Skrip atau Markup"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-562
  - TC-FA-CF-563
  - TC-FA-CF-564
coverage:
  web: automated
---

# Isolasi Tenant dan Render Teks untuk Payload Skrip atau Markup

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11 dan #12) dan Company Beta terpisah dengan Total Control Beta dan field `Beta Field` (Pre-setup #11). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE). Spec hanya membaca data Beta.
- Data Dinamis (bersuffix, S-12): field `<script>alert(1)</script> {runId}-150` (Text), field `Inj Dropdown {runId}-150` (Dropdown dengan opsi `<img src=x onerror=alert(1)>` dan Placeholder `' OR 1=1 --`), Field Name request Edit ditolak `Cross Edit {runId}-150`. Cleanup di hook `after`: hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-150`.
- Kemampuan teknis: klien HTTP dengan token Company Alpha; fixture BE untuk membaca field Company Beta; kemampuan baca Modal Changelog, System Log aktor, dan Activity Log dengan Search nama field (TC tidak menyebut path System Log aktor dan Activity Log; disediakan tim FE).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-562: request ke field milik company lain

1. Kirim request Edit langsung dengan token Company Alpha untuk id field `Beta Field` milik Company Beta, dengan Field Name `Cross Edit {runId}-150`
2. Verifikasi server menolak request Edit
3. Kirim request Delete langsung dengan token Company Alpha untuk id field `Beta Field` milik Company Beta
4. Verifikasi server menolak request Delete
5. Verifikasi field `Beta Field` Company Beta tidak berubah dan masih ada (dibaca lewat fixture BE)
6. Verifikasi daftar custom field Company Alpha memuat sedikitnya satu baris
7. Ketik Search `Beta Field`, tekan Enter
8. Verifikasi daftar Company Alpha tidak memuat field `Beta Field` (empty state `No results found`)
9. Klik `(←)` pada kotak Search

### TC-FA-CF-563: Field Name berisi payload skrip

10. Klik `[+ Custom Field]`
11. Isi Field Name `<script>alert(1)</script> {runId}-150` dan Data Type `Text`, lalu klik `[Submit]`
12. Ketik Search `<script>alert(1)</script> {runId}-150`, tekan Enter
13. Verifikasi nama field pada baris tabel tampil sebagai teks apa adanya tanpa mengeksekusi skrip
14. Klik row action `⋯` > `Delete` pada baris itu
15. Verifikasi nama field pada dialog Delete tampil sebagai teks apa adanya tanpa mengeksekusi skrip
16. Klik `[Cancel]`
17. Klik row action `⋯` > `Edit` pada baris itu
18. Verifikasi nama field pada modal Edit tampil sebagai teks apa adanya tanpa mengeksekusi skrip
19. Klik icon close `[✕]`
20. Klik icon Changelog di toolbar
21. Ketik Search `<script>alert(1)</script> {runId}-150` pada Changelog, tekan Enter
22. Verifikasi nama field pada Modal Changelog tampil sebagai teks apa adanya tanpa mengeksekusi skrip
23. Tutup Modal Changelog
24. Buka System Log aktor, ketik Search `<script>alert(1)</script> {runId}-150`, tekan Enter
25. Verifikasi nama field pada System Log aktor tampil sebagai teks apa adanya tanpa mengeksekusi skrip
26. Tutup System Log aktor
27. Buka Activity Log, ketik Search `<script>alert(1)</script> {runId}-150`, tekan Enter
28. Verifikasi nama field pada Activity Log tampil sebagai teks apa adanya tanpa mengeksekusi skrip
29. Tutup Activity Log
30. Klik `(←)` pada kotak Search

### TC-FA-CF-564: nama opsi, Placeholder, dan Search berisi markup atau SQL

31. Klik `[+ Custom Field]`
32. Isi Field Name `Inj Dropdown {runId}-150` dan Data Type `Dropdown`
33. Tambah opsi `<img src=x onerror=alert(1)>` dan isi Placeholder `' OR 1=1 --`, lalu klik `[Submit]`
34. Ketik Search `Inj Dropdown {runId}-150`, tekan Enter
35. Verifikasi Placeholder pada baris tabel tampil sebagai teks apa adanya `' OR 1=1 --`
36. Klik row action `⋯` > `Edit` pada baris itu
37. Verifikasi opsi `<img src=x onerror=alert(1)>` pada modal Edit tampil sebagai teks apa adanya
38. Klik icon close `[✕]`
39. Ganti isi kotak search dengan `' OR 1=1 --`, tekan Enter
40. Verifikasi pencarian dicocokkan sebagai teks biasa: baris `Inj Dropdown {runId}-150` ditemukan
41. Verifikasi pencarian tanpa efek injeksi: tabel tidak menampilkan seluruh baris Pre-setup
42. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 42 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kelas a, defense-in-depth tanpa harness eksternal), berdiri sendiri, dan 12 langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi`) yang tidak dihitung (bagian 3), sehingga sisa 30 langkah.
- K-1: TC-FA-CF-562 (kelas a) memiliki Expected respons API dan tetap di spec FE+BE ini; langkah 1 sampai 5 hanya mengasersi penolakan server dan state data lewat fixture BE (bagian 8b butir 1).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 9, 12, 21, 24, 27, 30, 34, 39, dan 42 (Search dan membersihkannya, R-16), langkah 16, 19, dan 38 (menutup dialog dan modal tanpa mengubah isi sehingga tidak muncul `Unsaved Changes`), pembukaan dan penutupan Modal Changelog, System Log aktor, dan Activity Log. Langkah 6 adalah pembanding generik sebelum asersi absence di langkah 8 (bagian 8b butir 2).
- Field Name TC-FA-CF-563 diberi suffix `{runId}-150` setelah payload supaya Data Dinamis unik (S-12) dan payload tetap utuh.
- Temuan untuk QA:
  - TC-FA-CF-562 menyebut "Server menolak" tanpa kode status; spec mengasersi penolakan tanpa kode.
  - TC-FA-CF-564 Expected b ("Pencarian dicocokkan sebagai teks biasa tanpa efek injeksi") tidak menyebut hasil yang diharapkan; spec mengasersi baris field ditemukan lewat Placeholder dan tabel tidak menampilkan seluruh baris. Kolom Placeholder sebagai kolom yang dicari Search tidak dinyatakan pada TC.
  - TC-FA-CF-564 tidak menyebut tempat opsi `<img src=x onerror=alert(1)>` diamati; spec memakai modal Edit.
