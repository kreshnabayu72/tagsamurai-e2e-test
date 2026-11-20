---
id: TC-FA-TDC-E2E-163-popup-used-by-screening-dan-isi-kolom
title: "Popup Used By: Screening dan Isi Kolom"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-579
  - TC-FA-TDC-580
sourceRules: ["§4.1.6#p1", "§4.1.6#r1", "§4.1.6#r2", "§4.1.6#r3", "§4.8#r3", "§4.1.6#p2", "FATDC-LOGIC-11a", "§4.1.1#r16"]
smoke: []
dependsOn: []
trace:
  "§4.1.6#p1": [2, 3, 4, 5, 6, 7, 11]
  "§4.1.6#r1": [8, 9, 12]
  "§4.1.6#r2": [8, 9, 13]
  "§4.1.6#r3": [8, 9, 14]
  "§4.8#r3": 8
  "§4.1.6#p2": 10
  "FATDC-LOGIC-11a": 15
  "§4.1.1#r16": 15
coverage:
  web: automated
---

# Popup Used By: Screening dan Isi Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData` ditambah Asset Class pemakai:
  - Sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data (NB-1 Used By 5 dengan Class Name `Bukan bangunan – Kelompok 1`).
  - NB-1 (TC-FA-TDC-579 dan 580) dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18).
- Kemampuan teknis: tidak ada di luar `suite.md`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-579: Screening Popup Used By

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
2. Verifikasi Header: Title `Used By`
3. Verifikasi Header: satu baris teks polos `NB-1 – Bukan bangunan – Kelompok 1` di bawah judul
4. Verifikasi Header: ikon Close `(X)` tampil
5. Verifikasi Header: tidak ada tombol teks `[Close]`
6. Verifikasi Header: toolbar tabel memuat Search dan Download
7. Verifikasi Header: `Download` adalah aksi sekunder, bukan primary
8. Verifikasi Body: kolom berurutan `Asset Class`, `Tax Method`, `Asset Names`, dan `Column Visibility (⋯)`
9. Verifikasi Body: `Asset Class`, `Tax Method`, dan `Asset Names` sortable, sedangkan `Column Visibility (⋯)` unsortable (klik header membuka Overlay Column Visibility)
10. Verifikasi Body: 5 baris urut Asset Class A-Z: AC-01, AC-02, AC-03, AC-04, AC-05
11. Verifikasi Footer: Pagination dengan page size default 10

### TC-FA-TDC-580: Isi kolom Popup Used By: format Asset Class, Tax Method, dan Asset Names

12. Verifikasi Asset Class berformat `[Class Code] – [Class Name]`: `AC-01 – Mesin Produksi`, `AC-02 – Peralatan Kantor`, `AC-03 – Kendaraan Operasional`, `AC-04 – Komputer`, `AC-05 – Furnitur`
13. Verifikasi Tax Method: AC-01 `Straight Line`, AC-02 `Straight Line`, AC-03 `Declining Balance`, AC-04 `Declining Balance`, AC-05 `Straight Line`
14. Verifikasi Asset Names (integer): AC-01 `12`, AC-02 `30`, AC-03 `7`, AC-04 `25`, AC-05 `18`
15. Verifikasi jumlah baris tabel (5) sama dengan angka Used By `5` pada baris NB-1 di tabel utama
16. Tutup Popup Used By lewat ikon Close `(X)`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-579, 580. TC-FA-TDC-579 dan 580 memakai Popup Used By NB-1 yang sama sehingga dibuka sekali (langkah 1) dan ditutup sesudah TC-FA-TDC-580 (langkah 16); langkah TC "Klik angka `5`" TC-FA-TDC-580 dan "Amati 5 baris tabel" diwakili langkah 1 dan 12 sampai 14.
- Langkah penghubung (S-03): langkah 16 (menutup popup lewat ikon Close; TC tidak menyebut cara menutup).
- Asersi absence langkah 5 didahului anchor positif langkah 4 (ikon Close tampil pada header yang sama; 8b.2).
- Tabel utama memuat sembilan baris pada satu halaman; baris NB-1 tidak perlu dicari lewat Search (8b.13).
- Temuan untuk QA:
  - TC-FA-TDC-579 butir Header iv menyebut `Download` sebagai aksi sekunder tanpa cara observasi (gaya tombol); spec mengasersinya apa adanya.
  - Email akun Total Control tidak tertulis di TC.
