---
id: TC-FA-TDC-E2E-165-popup-used-by-menutup-dan-hanya-dibuka-dari-angka-lebih-dari-nol
title: "Popup Used By: Menutup dan Hanya Dibuka dari Angka Lebih dari Nol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-589
  - TC-FA-TDC-590
coverage:
  web: automated
---

# Popup Used By: Menutup dan Hanya Dibuka dari Angka Lebih dari Nol

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData` ditambah pemakai NB-1: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data (NB-1 Used By 5, NB-4 Used By 0); NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18).
- Kemampuan teknis: klik area gelap di luar popup (backdrop); tombol Esc.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-589: Menutup Popup Used By: ikon Close dan Esc; klik backdrop tidak menutup

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
2. Klik area gelap di luar Popup
3. Verifikasi Popup tetap terbuka setelah klik backdrop
4. Klik ikon Close `(X)`
5. Verifikasi Popup tertutup setelah klik ikon Close
6. Klik angka `5` pada baris NB-1 untuk membuka kembali Popup Used By
7. Tekan Esc
8. Verifikasi Popup tertutup setelah Esc

### TC-FA-TDC-590: Popup Used By hanya dibuka dari angka lebih dari 0

9. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
10. Verifikasi angka `5` membuka Popup Used By
11. Tutup Popup Used By lewat ikon Close `(X)`
12. Klik angka `0` pada baris NB-4
13. Verifikasi angka `0` tidak membuka Popup

## Notes

- Langkah penghubung (S-03): langkah 11 (menutup popup; TC menulis "Tutup Popup" tanpa cara). Tabel utama memuat sembilan baris pada satu halaman; baris NB-1 dan NB-4 tidak perlu dicari lewat Search (8b.13).
- Asersi absence langkah 13 didahului anchor positif langkah 10 (angka lain pada tabel yang sama membuka Popup; 8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-590 butir b "angka `0` tidak membuka Popup" tidak memberi jeda atau langkah observasi selain klik; spec mengasersinya segera setelah klik.
  - Email akun Total Control tidak tertulis di TC.
