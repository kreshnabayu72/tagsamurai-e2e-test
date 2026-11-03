---
id: TC-AC-ACHA-E2E-044-download-isi-berkas-csv-xlsx
title: "Isi Berkas Download CSV dan XLSX pada List Device Allocation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-360
  - TC-AC-ACHA-361
  - TC-AC-ACHA-397
coverage:
  web: automated
---

# Isi Berkas Download CSV dan XLSX pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (nama env tercantum di daftar env var `suite.md`, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-6: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Data Dinamis: TC-AC-ACHA-361 membuat satu alokasi baru lewat sesi API aktor (pengirim PT ABC, jalur langsung, Category NFC, Client `PT Manufaktur Unggul`, Quantity `1`, Payment Free) dengan Notes `Kirim, cepat "uji"`, baris baru, lalu `baris dua {runId}-044`; Allocation ID baru ditangkap dari respons pembuatan (Dynamic Reference) dan dipakai mengenali baris di berkas. Alokasi ini tidak dapat dihapus lewat UI; seed dipulihkan ke Seed List 30 baris lewat fixture API yang disediakan tim FE/BE di hook `after`.
- Data uji TC-AC-ACHA-360 (baris Seed List yang diperiksa di berkas XLSX):

  | Baris | Dipakai untuk | Nilai di Seed List |
  |---|---|---|
  | `HALC-20260903-00004` | Category, Status, Quantity, Cost, Paid From, Payment, Last Updated, Allocated By | RFID Object TAG, Completed, Quantity `5,000`, Cost `$12,500.00`, Paid From `PT ABC (Principal)`, Payment Wallet, Last Updated `03/09/26 23:00`, Allocated By `Hendra W` (Hendra Wibowo) |
  | `HALC-20260902-00003` | Nilai kosong Notes, Paid From, Cost; Payment `Free` | Pengirim PT ABC (Principal), Notes `—`, Payment Free, Paid From `—`, Cost `—` |
  | `HALC-20260901-00003` | Nilai kosong Type dan Notes | NFC, Type `—`, Notes `—` |

- Kemampuan teknis (disediakan tim FE): browser mengunduh berkas ke folder uji yang dikosongkan sebelum tiap unduhan; membaca isi berkas CSV (byte awal untuk BOM, pemisah, pembungkus tanda kutip) dan XLSX (nilai dan tipe sel, nama sheet); sesi API aktor (login API password akun aktor, bukan sesi web; dinyatakan di `suite.md`) untuk membuat alokasi; mengubah Date Format dan Time Format di Global Settings > General Settings (akun aktor memiliki akses ke halaman itu).
- State global yang diubah: Date Format General Settings diubah menjadi `dd MMM yy` dan Time Format `HH:mm` di TC-AC-ACHA-397; dipulihkan ke `dd/MM/yy` dan 24 jam (Pre-setup #1) di langkah pemulihan akhir dan di hook `after` suite. Kolom Notes, Payment, Paid From, dan Cost ditampilkan di awal spec dan disembunyikan kembali di pemulihan akhir.
- Preferensi kolom tabel (Setup Column) tersimpan di browser; hook `after` suite menghapusnya (kemampuan disediakan tim FE, didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Persiapan kolom

1. Klik ikon `⋯` pada header kolom terakhir
2. Centang kolom Notes, Payment, Paid From, dan Cost di overlay Column Visibility
3. Tutup overlay Column Visibility

### TC-AC-ACHA-360: Transformasi isi berkas per tipe kolom

4. Klik ikon Download
5. Klik `Download as XLSX`
6. Buka berkas XLSX
7. Periksa baris `HALC-20260903-00004`, `HALC-20260902-00003`, dan `HALC-20260901-00003` (baris dengan Notes kosong)
8. Verifikasi Category baris `HALC-20260903-00004` ditulis hierarki penuh dari root (`TAG > RFID`)
9. Verifikasi Status ditulis label teks tanpa warna (baris `HALC-20260903-00004`: `Completed`)
10. Verifikasi Quantity baris `HALC-20260903-00004` ditulis sel angka `5000` (tanpa pemisah ribuan)
11. Verifikasi Cost baris `HALC-20260903-00004` ditulis sel angka `12500` (nilai numerik asli, tanpa pemisah ribuan dan tanpa simbol `$`)
12. Verifikasi nilai kosong Type baris `HALC-20260901-00003` ditulis `-` (hyphen tunggal), bukan blank atau `—`
13. Verifikasi nilai kosong Notes baris `HALC-20260901-00003` ditulis `-` (hyphen tunggal), bukan blank atau `—`
14. Verifikasi nilai kosong Paid From baris `HALC-20260902-00003` ditulis `-` (hyphen tunggal), bukan blank atau `—`
15. Verifikasi nilai kosong Cost baris `HALC-20260902-00003` ditulis `-` (hyphen tunggal), bukan blank atau `—`
16. Verifikasi Paid From baris `HALC-20260903-00004` ditulis `PT ABC (Principal)`
17. Verifikasi Payment baris `HALC-20260903-00004` ditulis `Wallet` sesuai pengirim
18. Verifikasi Payment baris `HALC-20260902-00003` ditulis `Free` sesuai pengirim
19. Verifikasi Last Updated baris `HALC-20260903-00004` ditulis `03/09/26 23:00` sesuai Date Format dan Time Format General Settings
20. Verifikasi Allocated By baris `HALC-20260903-00004` ditulis `Hendra W`, bukan nama lengkap `Hendra Wibowo`

### TC-AC-ACHA-361: Aturan teknis CSV dan XLSX

21. Buat alokasi dengan Notes `Kirim, cepat "uji"`, baris baru, dan `baris dua {runId}-044` lewat sesi API aktor hingga alokasi tersimpan; Allocation ID baru ditangkap
22. Muat ulang halaman (F5)
23. Klik ikon Download
24. Klik `Download as CSV`
25. Buka berkas CSV dengan editor teks
26. Verifikasi CSV berencoding UTF-8 dengan BOM
27. Verifikasi CSV memakai pemisah koma
28. Verifikasi nilai Notes baris alokasi baru (dikenali dari Allocation ID) dibungkus tanda kutip ganda
29. Verifikasi tanda kutip di dalam nilai Notes baris alokasi baru digandakan
30. Klik ikon Download
31. Klik `Download as XLSX`
32. Buka berkas XLSX
33. Verifikasi XLSX memuat satu sheet bernama `Sheet1`

### TC-AC-ACHA-397: Export mengikuti General Settings

34. Ubah Date Format menjadi `dd MMM yy` dan Time Format `HH:mm` di Global Settings > General Settings, simpan
35. Buka Allocation > Device Allocation
36. Klik ikon Download
37. Klik `Download as CSV`
38. Buka berkas CSV
39. Verifikasi Last Updated baris `HALC-20260909-00003` memuat tanggal `09 Sep 26` (format General Settings, bukan format ISO)
40. Verifikasi Last Updated baris `HALC-20260909-00003` memuat waktu `19:00` (format General Settings, bukan format ISO)

### Pemulihan state

41. Ubah Date Format menjadi `dd/MM/yy` dan Time Format ke 24 jam di Global Settings > General Settings, simpan (Pre-setup #1)
42. Buka Allocation > Device Allocation
43. Klik ikon `⋯` pada header kolom terakhir
44. Hilangkan centang kolom Notes, Payment, Paid From, dan Cost di overlay Column Visibility
45. Tutup overlay Column Visibility

## Notes

- Ukuran spec (di atas 35 langkah): tiga TC isi berkas satu topik memakai satu dataset; tiap kolom dan baris yang diharapkan menjadi `Verifikasi` sendiri (S-01), ditambah persiapan dan pemulihan kolom serta format tanggal.
- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-7 dan 7a). Seluruh TC primer spec ini (TC-AC-ACHA-360, 361, 397) dikerjakan di sini. Spec ini kelas f (binary buffer, konvensi bagian 3 prinsip 13f): isi berkas CSV dan XLSX dipisah dari asersi nama berkas, header, dan jumlah baris di spec 043. TC-AC-ACHA-397 (format tanggal waktu pada berkas) ada di sini; TC-AC-ACHA-392 sampai 396 dan 398 (format tanggal pada surface lain) ada di spec 050.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): persiapan dan pemulihan kolom lewat overlay Column Visibility; muat ulang halaman sesudah pembuatan alokasi lewat API (supaya baris baru ada di tabel); pembukaan berkas unduhan; pemulihan Date Format dan Time Format. Pelaku pembuat alokasi memakai sesi API aktor (bukan konteks UI kedua) sehingga tidak memakai `P-2`.
- Baris TC-AC-ACHA-360: TC menyebut "baris dengan Notes kosong" tanpa ID; spec memakai `HALC-20260901-00003` (Type dan Notes kosong) untuk nilai kosong Type dan Notes, dan `HALC-20260902-00003` untuk Paid From dan Cost kosong serta Payment `Free`. Asersi tambahan (S-03): nilai Last Updated `03/09/26 23:00` dan Status `Completed` diambil dari Seed List untuk baris `HALC-20260903-00004`.
- Temuan untuk QA:
  - TC-AC-ACHA-397 langkah uji kedua menulis "Klik `[Download]` dan pilih `CSV`", sedangkan TC-AC-ACHA-357 menulis ikon Download dengan opsi `Download as CSV`; spec memakai ikon Download dan `Download as CSV`.
  - TC-AC-ACHA-397 mengubah Date Format dan Time Format di Global Settings > General Settings tanpa menyebut label field atau tombol simpan; spec menulis aksi tingkat tinggi (tim FE melengkapi selector) dan memulihkannya ke Pre-setup #1 di akhir spec.
  - TC-AC-ACHA-361 langkah uji pertama ("Buat alokasi dengan Notes ...") tidak menyebut Category, Client, atau Quantity; spec memakai nilai minimal lewat sesi API aktor dan menambah akhiran `{runId}-044` pada baris kedua Notes agar unik per run.
