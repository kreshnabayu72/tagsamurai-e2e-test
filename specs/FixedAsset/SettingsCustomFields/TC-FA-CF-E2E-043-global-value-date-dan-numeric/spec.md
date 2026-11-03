---
id: TC-FA-CF-E2E-043-global-value-date-dan-numeric
title: "Global Value Date dan Numeric: Tanggal Tidak Valid, Decimal Places, Batas 15 Digit, dan Nilai Negatif"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-132
  - TC-FA-CF-133
  - TC-FA-CF-134
  - TC-FA-CF-620
coverage:
  web: automated
---

# Global Value Date dan Numeric: Tanggal Tidak Valid, Decimal Places, Batas 15 Digit, dan Nilai Negatif

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Date Format General Settings `dd/MM/yy` (Pre-setup #11) dipakai untuk nilai tanggal `31/02/26`; format tidak diubah.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-043`): `Global Date {runId}-043` (Date, tidak tersimpan), `Global Numeric {runId}-043` (Numeric, Decimal Places 1, tidak tersimpan), `Global Numeric 16 {runId}-043` (Numeric, Decimal Places 2, tidak tersimpan), `Global Numeric 15 {runId}-043` (Numeric, Decimal Places 2, tersimpan), `Global Negative {runId}-043` (Numeric, Decimal Places 1, nilai `-5.5`, tersimpan). Nilai yang diketik: `31/02/26`, `12.55`, `1234567890123.45` (15 digit), `12345678901234.45` (16 digit), `-5.5`.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-043`.
- Kemampuan teknis: pengetikan nilai tanggal mentah ke input Date; pembukaan form Edit field.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [+ Custom Field]

### TC-FA-CF-132: Global Value Date dengan tanggal tidak valid ditolak

2. Isi Field Name `Global Date {runId}-043`, pilih Data Type `Date`, Scope `General`, Value Type `Global`
3. Ketik tanggal tidak valid `31/02/26` pada input Value
4. Klik [Submit]
5. Verifikasi pesan inline "Global date {runId}-043 must be a valid date" tampil pada input Value
6. Verifikasi Submit ditolak: modal tetap terbuka
7. Klik [Clear Field]

### TC-FA-CF-133: Global Value Numeric melebihi Decimal Places field ditolak

8. Isi Field Name `Global Numeric {runId}-043`, pilih Data Type `Numeric`, Scope `General`, Value Type `Global`, Decimal Places `1 (.0)`
9. Isi Value `12.55`
10. Klik [Submit]
11. Verifikasi pesan inline "Global numeric {runId}-043 must have at most 1 decimal place(s)" tampil pada input Value
12. Verifikasi Submit ditolak: modal tetap terbuka
13. Klik [Clear Field]

### TC-FA-CF-134: Global Value Numeric 15 digit termasuk desimal diterima dan 16 digit ditolak

14. Isi Field Name `Global Numeric 16 {runId}-043`, pilih Data Type `Numeric`, Scope `General`, Value Type `Global`, Decimal Places `2 (.00)`
15. Isi Value 16 digit `12345678901234.45`
16. Klik [Submit]
17. Verifikasi input ditolak dengan pesan inline pada input Value (teks pesan tidak diassert)
18. Verifikasi Submit tidak menyimpan field: modal tetap terbuka
19. Klik [Clear Field]
20. Isi Field Name `Global Numeric 15 {runId}-043`, pilih Data Type `Numeric`, Scope `General`, Value Type `Global`, Decimal Places `2 (.00)`
21. Isi Value 15 digit `1234567890123.45`
22. Klik [Submit]
23. Verifikasi Submit sukses: toast "Success, custom field has been created." tampil

### TC-FA-CF-620: Global Value Numeric negatif dengan tanda minus di depan diterima

24. Klik [+ Custom Field]
25. Isi Field Name `Global Negative {runId}-043`, pilih Data Type `Numeric`, Decimal Places `1 (.0)`, Scope `General`, Value Type `Global`
26. Tunggu toast lama hilang otomatis
27. Isi Value `-5.5`, lalu klik [Submit]
28. Verifikasi toast "Success, custom field has been created." tampil
29. Ketik Search `Global Negative {runId}-043`, tekan Enter
30. Klik row action `⋯` > `Edit` pada baris `Global Negative {runId}-043`
31. Verifikasi form Edit menampilkan Value `-5.5`
32. Klik `[✕]`

### Penutup: field yang ditolak tidak tersimpan

33. Ganti isi kotak search dengan `{runId}-043`, tekan Enter
34. Verifikasi tabel menampilkan tepat 2 baris: `Global Numeric 15 {runId}-043` dan `Global Negative {runId}-043` (field `Global Date`, `Global Numeric`, dan `Global Numeric 16` bersuffix `{runId}-043` tidak tersimpan)
35. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 132, 133, 134, 620 (urutan sumber 132, 133, 134, 620). Modal yang sama dipakai untuk kasus yang diblokir (langkah 1 sampai 23); [Clear Field] (langkah 7, 13, 19) mengosongkan modal tanpa menutupnya. Kasus sukses menutup modal sehingga TC-FA-CF-620 membuka modal baru (langkah 24).
- TC-FA-CF-134: bagian 16 digit (ditolak) dijalankan lebih dulu daripada bagian 15 digit (diterima) karena Submit sukses menutup modal. Penambahan satu digit dilakukan pada bagian bulat sehingga yang diuji batas jumlah digit, bukan Decimal Places.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7, 13, 19, 24, 29, 30 (Search dan pembukaan Edit untuk menemukan baris target, R-16), 32, 33, 35, serta pengisian form sebagai bagian langkah TC. Langkah 33 sampai 35 membuktikan lewat dua baris tersimpan sebagai anchor positif bahwa tiga field yang ditolak tidak muncul.
- Asersi "Submit sukses" pada TC-FA-CF-134 ditulis sebagai toast sukses baku `Success, custom field has been created.` (tertulis di TC-FA-CF-141, 143, dan 155); asersi tambahan itu dicatat sesuai S-03. "Submit ditolak" diamati lewat modal yang tetap terbuka.
- Teks pesan inline TC-FA-CF-132 dan TC-FA-CF-133 memuat nama field; karena nama field bersuffix `{runId}-043`, asersi memakai nama bersuffix yang sama (R-06).
- Langkah penghubung toast (S-03, R-22): langkah 26 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-134: Expected a menyebut "Pada 15 digit Submit sukses", tetapi Langkah Uji hanya mengklik [Submit] sesudah digit ke-16 ditambahkan; spec menambah Submit pada 15 digit (langkah 22) dan menguji 16 digit pada pembukaan terpisah. TC juga tidak menyebut posisi digit tambahan.
  - TC-FA-CF-620: pembukaan form Edit memakai pencarian nama field (langkah 29) karena TC tidak menyebut cara menemukan baris.
  - Nama field memakai suffix `{runId}-043` (S-12) sehingga tidak sama dengan `Global Date`, `Global Numeric`, dan `Global Negative` pada Data Uji TC.
