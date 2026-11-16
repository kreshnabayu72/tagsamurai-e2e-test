---
id: TC-FA-TDC-E2E-173-popup-changelog-download-nama-berkas-dan-filter-aktif
title: "Popup Changelog Download: Overlay, Nama Berkas, dan Filter Aktif"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-615
  - TC-FA-TDC-616
  - TC-FA-TDC-617
  - TC-FA-TDC-618
sourceRules: ["§5#b8", "§[F-FATDC-12] Download#b1", "§4.1.1#p8", "§4.1.1#r26", "§4.1.1#r43", "§4.1.1#r44"]
smoke: []
dependsOn: []
trace:
  "§5#b8": [5, 7, 12]
  "§[F-FATDC-12] Download#b1": [7, 12, 21, 22]
  "§4.1.1#p8": 21
  "§4.1.1#r26": 22
  "§4.1.1#r43": [22, 23]
  "§4.1.1#r44": [22, 23]
anchor: [3, 4, 8, 13]
coverage:
  web: automated
---

# Popup Changelog Download: Overlay, Nama Berkas, dan Filter Aktif

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD, termasuk dua entri Edit untuk NB-4. Format tanggal General Settings `dd/MM/yy HH:mm`. Data Dinamis: tidak ada.
- Data uji TC-FA-TDC-618: Action `Edit`; Keyword `NB-4`.
- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); menangkap berkas unduhan CSV dan XLSX serta membuka isinya (nama berkas, daftar sheet, baris header, jumlah baris data); kemampuan membuka berkas disediakan tim FE.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-615: Screening Overlay Download pada Popup Changelog

1. Klik icon Changelog
2. Klik icon Download pada toolbar Popup
3. Verifikasi Overlay tampil menempel pada icon Download di toolbar Popup
4. Verifikasi Overlay tampil tanpa backdrop
5. Verifikasi Overlay memuat dua opsi `Download as CSV` dan `Download as XLSX`

### TC-FA-TDC-616: Download CSV dari Popup Changelog

6. Klik `Download as CSV`
7. Verifikasi berkas `Changelog-Tax-Depreciation-Class.csv` terunduh
8. Verifikasi Popup Changelog tetap terbuka

### TC-FA-TDC-617: Download XLSX dari Popup Changelog

9. Klik icon Download pada toolbar Popup
10. Klik `Download as XLSX`
11. Buka berkas
12. Verifikasi berkas `Changelog-Tax-Depreciation-Class.xlsx` terunduh
13. Verifikasi berkas memiliki satu sheet bernama `Sheet1`

### TC-FA-TDC-618: Download dengan Search dan Filter aktif

14. Klik icon Filter pada toolbar Popup
15. Pilih Action `Edit`
16. Klik `[Apply]`
17. Ketik Search `NB-4`, tekan Enter
18. Klik icon Download pada toolbar Popup
19. Klik `Download as CSV`
20. Buka berkas
21. Verifikasi berkas memuat baris header
22. Verifikasi berkas memuat tepat 2 baris data
23. Verifikasi kedua baris data adalah dua entri Edit untuk NB-4
24. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah 2 TC-FA-TDC-616 ("Klik icon Download") tidak diulang karena Overlay Download masih terbuka dari langkah 2 dan opsi langsung diklik pada langkah 6. Langkah 1 TC-FA-TDC-616, TC-FA-TDC-617, dan TC-FA-TDC-618 ("Klik icon Changelog") tidak diulang karena Popup Changelog tetap terbuka sejak langkah 1.
- Kelas f (binary buffer): spec ini mengasersi nama berkas, daftar sheet, baris header, dan jumlah baris data (asersi fungsional menurut prinsip 13f). Nilai sel tidak diasersi; satu-satunya asersi keanggotaan baris adalah langkah 23 (kolom Action dan Class Code dua baris hasil).
- Langkah penghubung (S-03): langkah 24 (menutup Popup Changelog, yang membuang Filter dan Search Popup).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-616, TC-FA-TDC-617, dan TC-FA-TDC-618 tidak menyebut cara membuka atau membaca berkas unduhan; mekanismenya disediakan tim FE (S-13).
  - TC-FA-TDC-618 tidak menyebut nama kolom baris header berkas; spec hanya mengasersi keberadaan baris header.
  - TC-FA-TDC-618 tidak menyatakan bahwa menutup Popup membuang Filter dan Search Popup; spec mengasumsikannya untuk membersihkan state.
