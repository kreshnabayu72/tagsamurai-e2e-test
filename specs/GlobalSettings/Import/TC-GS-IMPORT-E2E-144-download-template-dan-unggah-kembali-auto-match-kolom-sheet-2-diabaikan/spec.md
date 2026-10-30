---
id: TC-GS-IMPORT-E2E-144-download-template-dan-unggah-kembali-auto-match-kolom-sheet-2-diabaikan
title: "Download Template dan unggah kembali: auto-match kolom, Sheet 2 diabaikan, dan tidak membuat draft (Client B)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-455
  - TC-GS-IMPORT-456
  - TC-GS-IMPORT-457
coverage:
  web: automated
---

# Download Template dan unggah kembali: auto-match kolom, Sheet 2 diabaikan, dan tidak membuat draft (Client B)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand (Client B); perpindahan Sub-Tab ditulis sebagai langkah.
- Data: Client B tanpa draft pada keadaan awal (Kontrak Fixture R1) dan tanpa data master. Berkas upload adalah berkas hasil unduhan `Template-Import-Measurement.xlsx` dan `Template-Import-Brand.xlsx` (Sheet 1 berisi header dan 3 baris contoh; Sheet 2 berisi petunjuk kolom `Column`, `Data Type`, `Description`, `Constraint`, `Example`); tidak ada fixture berkas tersendiri.
- Kemampuan teknis (disediakan tim FE/BE): runner meneruskan berkas hasil unduhan ke input upload; skrip reset draft Client B (R1) untuk Tab Measurement dan Tab Brand.
- State global: tidak ada yang diubah selain draft Client B (direset) dan flag Guided Tooltip (dipulihkan hook suite `after`). Suite Import berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft Brand dan Measurement Client B ke tanpa draft.

## Test Steps

### TC-GS-IMPORT-457: Download Template tidak membuat draft atau mengubah state halaman

1. Reset draft Brand Client B ke tanpa draft lewat fixture (R1), lalu muat ulang halaman Import > Brand
2. Klik `[Download Template]` pada state belum ada draft
3. Tunggu berkas template terunduh
4. Verifikasi halaman tetap menampilkan Dropzone
5. Verifikasi tidak ada Unsaved Banner
6. Verifikasi kartu Total Rows 0
7. Verifikasi `[Import (0)]` Disabled
8. Muat ulang halaman
9. Verifikasi halaman masih menampilkan Dropzone
10. Verifikasi tidak ada Unsaved Banner (tidak ada draft tersimpan)

### TC-GS-IMPORT-455: Template yang diunduh dapat diunggah kembali dan auto-match Unit Name dan Symbol

11. Klik Sub-Tab Measurement
12. Klik `[Download Template]` di Tab Measurement
13. Tunggu berkas `Template-Import-Measurement.xlsx` terunduh
14. Klik `[Upload File]` dan pilih berkas `Template-Import-Measurement.xlsx` yang terunduh tanpa mengubah isi
15. Verifikasi Modal Column Mapping `Column Mapping: Measurement` terbuka
16. Verifikasi dropdown `Unit Name` terisi otomatis dengan kolom berkas bernama sama
17. Verifikasi dropdown `Symbol` terisi otomatis dengan kolom berkas bernama sama
18. Verifikasi tidak ada Error Banner pada Modal Column Mapping
19. Klik [Confirm Mapping]
20. Verifikasi modal tertutup
21. Verifikasi toast sukses "Success, row has been added."
22. Verifikasi Staging Table menampilkan 3 baris `pending` (Kilogram/kg, Meter/m, Piece/pcs)
23. Verifikasi Row # bernilai 1 sampai 3
24. Reset draft Measurement Client B ke tanpa draft lewat fixture, lalu klik Sub-Tab Brand

### TC-GS-IMPORT-456: Sheet 2 pada template yang diunggah kembali diabaikan

25. Klik `[Download Template]` di Tab Brand
26. Tunggu berkas `Template-Import-Brand.xlsx` terunduh
27. Klik `[Upload File]` dan pilih berkas `Template-Import-Brand.xlsx` yang terunduh tanpa mengubah isi
28. Buka dropdown File Column `Brand Name` pada Modal Column Mapping
29. Verifikasi dropdown File Column hanya menawarkan `No Column` dan `Brand Name` (header Sheet 1)
30. Verifikasi dropdown File Column tidak menawarkan opsi dari Sheet 2 (`Column`, `Data Type`, `Description`, `Constraint`, `Example`)
31. Klik [Confirm Mapping]
32. Verifikasi Staging Table memuat tepat 3 baris `Acme Corp`, `Lenovo`, dan `Zebra Technologies`
33. Verifikasi tidak ada baris bernilai teks Sheet 2
34. Reset draft Brand Client B ke tanpa draft lewat fixture

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan dalam spec: TC-GS-IMPORT-457, 455, 456. TC-GS-IMPORT-457 (tanpa membuat draft) dikerjakan lebih dulu karena butuh state belum ada draft pada Tab Brand dan aksi yang membuat draft (TC-GS-IMPORT-455 dan 456) ditaruh sesudahnya (prinsip 2 dan 3 bagian 3); urutan TC sumber (455, 456, 457) diubah karena alasan itu.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah reset draft (awal blok TC-GS-IMPORT-457 sesuai Precondition c, serta akhir blok TC-GS-IMPORT-455 dan 456 untuk memberi state belum ada draft pada blok berikutnya), langkah memilih Sub-Tab, dan langkah menunggu berkas terunduh. Reset draft dilakukan lewat fixture (R1), bukan lewat langkah UI yang tidak ada di TC.
- Pembagian TC lintas spec: Download Template untuk Client A dan Client G berada di spec lain; TC-GS-IMPORT-455, 456, dan 457 memakai Client B sehingga ditaruh bersama di spec ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-455 dan 456: isi berkas template (3 baris contoh: Kilogram/kg, Meter/m, Piece/pcs untuk Measurement; Acme Corp, Lenovo, Zebra Technologies untuk Brand) dan nama kolom Sheet 2 tidak ada di Data Dinamis atau Pre-setup; hanya di Expected TC.
  - TC-GS-IMPORT-455: Expected b menulis toast sukses "Success, row has been added."; spec mengikuti TC.
  - TC-GS-IMPORT-455, 456, dan 457: kolom Post Condition kosong ("-"); tidak ada Post Condition yang diasersi.
  - TC-GS-IMPORT-457: Expected a menyebut "kartu Total Rows 0 dan `[Import (0)]` Disabled" pada state belum ada draft; PRD §7.1 menampilkan Dropzone pada state ini sehingga keberadaan kartu tidak jelas (temuan serupa pada TC-GS-IMPORT-195).
  - TC-GS-IMPORT-455 dan 456: tidak ada Expected tentang toast atau berkas terunduh; spec hanya menunggu berkas terunduh sebagai langkah penghubung, bukan asersi.
