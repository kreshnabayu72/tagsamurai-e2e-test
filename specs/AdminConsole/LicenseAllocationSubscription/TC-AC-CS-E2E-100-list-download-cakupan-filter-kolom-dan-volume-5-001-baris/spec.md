---
id: TC-AC-CS-E2E-100-list-download-cakupan-filter-kolom-dan-volume-5-001-baris
title: "List Download: Cakupan, Filter, Kolom, dan Volume 5.001 Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-383
  - TC-AC-CS-384
  - TC-AC-CS-385
  - TC-AC-CS-386
  - TC-AC-CS-388
  - TC-AC-CS-392
coverage:
  web: automated
---

# List Download: Cakupan, Filter, Kolom, dan Volume 5.001 Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #82 (120 baris term di tab Current dan 60 baris di tab History; Plan Owner PT Maju Bersama dan CV Karya Mandiri) bersifat baca-saja; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data seed Pre-setup #83 (5.001 baris term di tab History) dipasang oleh fixture backend (disediakan tim FE/BE) sebagai langkah penghubung sebelum TC-AC-CS-392 dan dihapus di hook `after`; selama blok itu tab History Principal berisi 5.001 baris, sehingga blok TC-AC-CS-385 (60 baris History dari #82) berjalan sebelum #83 dipasang. Efek: baris History Principal.
- Kemampuan membaca berkas unduhan (nama berkas, jumlah baris data, nama kolom header) disediakan tim FE; isi sel hanya diasersi di spec 101 (kelas binary buffer).
- Nilai input uji: Search `Sejahtera`, Filter Status `Active`; Search tanpa hasil `zzzzqqq`.
- Kelas volume data (e): dataset 120 baris Current, 60 baris History, dan 5.001 baris History.

## Test Steps

### TC-AC-CS-383: Download tanpa filter mengekspor seluruh baris tab aktif

1. Klik ikon Download lalu pilih `Download as CSV`
2. Verifikasi berkas `Client-Subscription-Current.csv` terunduh dengan 120 baris data (seluruh halaman, bukan 10 baris tampilan)
3. Verifikasi berkas hanya memuat baris tab `Current`
4. Verifikasi tidak ada toast sukses

### TC-AC-CS-384: Download mengikuti Search dan Filter yang aktif

5. Ketik Search `Sejahtera`, tekan Enter
6. Klik ikon Filter di toolbar, pilih Status `Active`, lalu klik `[Apply]`
7. Klik ikon Download lalu pilih `Download as XLSX`
8. Verifikasi berkas `Client-Subscription-Current.xlsx` hanya berisi baris yang memuat `Sejahtera` dan berstatus Active
9. Verifikasi ekstensi berkas mengikuti pilihan XLSX
10. Klik `(←)` pada kotak Search, lalu klik ikon Filter, `[Clear Field]`, dan `[Apply]`

### TC-AC-CS-386: Kolom yang disembunyikan tidak ikut diekspor dan kembali ikut saat ditampilkan

11. Hilangkan centang kolom `Product` lewat overlay Column Visibility
12. Klik ikon Download lalu pilih `Download as CSV`
13. Verifikasi berkas tidak memuat kolom Product
14. Verifikasi tidak ada toast peringatan
15. Centang kembali kolom `Product` lewat overlay Column Visibility
16. Klik ikon Download lalu pilih `Download as CSV`
17. Verifikasi berkas memuat kembali kolom Product

### TC-AC-CS-388: Download dengan nol baris menghasilkan berkas hanya berisi header

18. Ketik Search `zzzzqqq`, tekan Enter
19. Verifikasi tombol Download tetap aktif
20. Klik ikon Download lalu pilih `Download as CSV`
21. Verifikasi berkas hanya berisi baris header kolom yang visible tanpa baris data
22. Verifikasi tidak ada toast
23. Klik `(←)` pada kotak Search

### TC-AC-CS-385: Download tab History memakai filename tab History

24. Klik tab `History`
25. Klik ikon Download lalu pilih `Download as CSV`
26. Verifikasi berkas bernama `Client-Subscription-History.csv`
27. Verifikasi isi berkas hanya baris tab `History` (60 baris data)

### TC-AC-CS-392: Download lebih dari 5.000 baris memakai loading screen tanpa job background

28. Pasang seed Pre-setup #83 lewat fixture backend, lalu muat ulang tab `History`
29. Klik ikon Download lalu pilih `Download as CSV`
30. Verifikasi loading screen tampil sampai berkas siap
31. Verifikasi berkas terunduh langsung setelah loading screen selesai
32. Verifikasi tidak ada job background maupun notifikasi in-app
33. Verifikasi berkas memuat 5.001 baris data

## Notes

- TC-AC-CS-389, 390, 391, dan 472 (isi sel berkas) dicakup spec lain suite ini.
- Seluruh blok satu topik (Download List) dengan harness dan dataset volume yang sama (kelas e) dan berdiri sendiri. Urutan blok: TC-AC-CS-388 sebelum TC-AC-CS-385 karena memakai tab `Current`, dan TC-AC-CS-385 sebelum TC-AC-CS-392 karena seed #83 mengganti isi tab `History`.
- Langkah penghubung (S-03): langkah membersihkan Search dan Filter di akhir blok TC-AC-CS-384 dan TC-AC-CS-388 (`(←)`, `[Clear Field]`, `[Apply]`).
- Asersi absence toast dan notifikasi (TC-AC-CS-383, 386, 388, 392) mengikuti bagian 8b butir 11: klik Download menjadi pemicu dan `Verifikasi` berkas terunduh menjadi anchor positif; pada TC-AC-CS-392 `Verifikasi` berkas terunduh diletakkan sebelum asersi absence notifikasi. Ini bukan absence log (S-05).
- Temuan untuk QA:
  - TC-AC-CS-392 Expected b ("Tidak ada job background maupun notifikasi in-app") tidak menyebut cara mengamati job background; spec hanya mengamati notifikasi in-app dan indikator job pada UI.
  - Pre-setup #83 (5.001 baris History) dan #82 (60 baris History, TC-AC-CS-385) menempati tab `History` yang sama sehingga tidak dapat aktif bersamaan; spec memasang #83 sebagai langkah penghubung sesudah blok TC-AC-CS-385.
  - TC-AC-CS-384 Expected a mensyaratkan isi sel (Client memuat `Sejahtera`, Status Active); spec mengasersinya dengan kemampuan baca berkas tanpa membahas format sel (format sel dicakup spec lain suite ini).
