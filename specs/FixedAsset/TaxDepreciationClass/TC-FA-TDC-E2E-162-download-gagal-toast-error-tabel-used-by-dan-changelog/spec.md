---
id: TC-FA-TDC-E2E-162-download-gagal-toast-error-tabel-used-by-dan-changelog
title: "Download Gagal: Toast Error Tabel, Used By, dan Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-578
  - TC-FA-TDC-594
  - TC-FA-TDC-930
coverage:
  web: automated
---

# Download Gagal: Toast Error Tabel, Used By, dan Changelog

## Prerequisites

- Mode: FE+BE. Respons Download dipaksa gagal 500 lewat `Spectra.intercept()` di atas backend nyata (asersi memuat state tabel dan popup yang tetap); endpoint Download tidak disebut TC, PRD, atau LLD yang dibaca sehingga tidak dikarang (S-13), dan intercept dipasang pada permintaan Download yang dipicu klik `Download as CSV`. Intercept dilepas segera setelah toast diasersi pada tiap blok (S-09).
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData`: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Untuk TC-FA-TDC-594, NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18).
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons Download 500 pada tabel utama, popup Used By, dan popup Changelog; Overlay Download.
- State global yang diubah: tidak ada state server yang diubah; intercept dilepas pada langkah 6, 14, dan 22.

## Test Steps

### TC-FA-TDC-578: Download gagal menampilkan toast error tanpa ekstensi

1. Pasang intercept yang memaksa respons Download tabel utama gagal 500
2. Klik icon Download
3. Klik `Download as CSV`
4. Verifikasi muncul toast error: `Error, failed to download Tax-Depreciation-Class.`
5. Verifikasi tidak ada berkas terunduh
6. Lepas intercept
7. Verifikasi tabel tidak berubah: sembilan class Example Data tetap tampil dengan urutan sama seperti sebelum Download

### TC-FA-TDC-594: Download Used By gagal menampilkan toast error

8. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
9. Pasang intercept yang memaksa respons Download Used By gagal 500
10. Klik icon Download pada toolbar Popup
11. Klik `Download as CSV`
12. Verifikasi muncul toast error: `Error, failed to download Tax-Depreciation-Class-Used-By.`
13. Verifikasi Popup Used By tetap terbuka
14. Lepas intercept
15. Tutup Popup Used By

### TC-FA-TDC-930: Download gagal dari Popup Changelog menampilkan toast error dengan nama berkas Changelog-Tax-Depreciation-Class

16. Klik icon Changelog
17. Pasang intercept yang memaksa respons Download Popup Changelog gagal 500
18. Klik icon Download pada toolbar Popup
19. Klik `Download as CSV`
20. Verifikasi muncul toast error: `Error, failed to download Changelog-Tax-Depreciation-Class.`
21. Verifikasi tidak ada berkas terunduh
22. Lepas intercept
23. Verifikasi Popup Changelog tetap terbuka
24. Tutup Popup Changelog

## Notes

- Langkah penghubung (S-03): langkah 2 (membuka Overlay Download; TC langsung klik `Download as CSV`), langkah 15 dan 24 (menutup popup), langkah 6, 14, dan 22 (melepas intercept; S-09).
- Intercept dilepas sesudah `Verifikasi` toast karena toast membuktikan respons gagal sudah diproses; langkah 6 mendahului langkah 7, dan langkah 22 mendahului langkah 23, sedangkan asersi absence berkas (langkah 5 dan 21) memakai toast error sebagai anchor positif (8b.2). Toast dari blok sebelumnya dibiarkan hilang otomatis sebelum blok berikutnya diasersi karena teks toast tiap blok berbeda.
- Kelas b (fault injection) diwakili tiga TC dalam satu spec per kelas per modul (prinsip 13); pemicunya sama (respons 500 pada Download).
- Temuan untuk QA:
  - TC-FA-TDC-578 butir b "tabel tidak berubah" tidak mendefinisikan keadaan yang dibandingkan; spec mengasersi baris dan urutan tabel sebelum dan sesudah Download.
  - TC-FA-TDC-594 dan 930 butir "tidak ada berkas terunduh" hanya ada di TC-FA-TDC-578 dan 930; TC-FA-TDC-594 hanya mengasersi toast dan popup tetap terbuka.
  - TC tidak menyebut endpoint Download; kemampuan intercept tergantung nama endpoint yang diberikan tim FE.
  - Email akun Total Control tidak tertulis di TC.
