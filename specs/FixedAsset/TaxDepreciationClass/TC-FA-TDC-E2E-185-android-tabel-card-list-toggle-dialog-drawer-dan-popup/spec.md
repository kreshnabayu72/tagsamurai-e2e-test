---
id: TC-FA-TDC-E2E-185-android-tabel-card-list-toggle-dialog-drawer-dan-popup
title: "Android: Card List, Toggle Active, Dialog Bottom Sheet, Form Halaman Penuh, dan Popup Used By"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-660
  - TC-FA-TDC-661
  - TC-FA-TDC-663
  - TC-FA-TDC-664
  - TC-FA-TDC-665
sourceRules: ["§4.6#b1", "ST-27", "§4.6#b4", "D-03", "FATDC-LOGIC-08h", "§4.6#b2", "FLD-18", "§4.1.6#p1", "§4.6#b3"]
smoke: []
dependsOn: []
trace:
  "§4.6#b1": [1, 2, 3]
  "ST-27": 3
  "§4.6#b4": [5, 20]
  "D-03": 5
  "FATDC-LOGIC-08h": 7
  "§4.6#b2": [9, 10, 11, 12, 15, 16, 17]
  "FLD-18": 17
  "§4.1.6#p1": 20
  "§4.6#b3": 21
coverage:
  mobile: automated
---

# Android: Card List, Toggle Active, Dialog Bottom Sheet, Form Halaman Penuh, dan Popup Used By

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi native Android Fixed Asset di perangkat atau emulator Android (`coverage.mobile`), disediakan tim FE. Perangkat Android uji dipakai bersama sehingga spec berjalan serial (`parallel: false`, sesuai `suite.md`).
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini pada aplikasi Android; layar Settings > Accounting > Tax Depreciation Class dibuka hook `before` spec ini (hook `beforeEach` suite membuka halaman web, bukan aplikasi native). Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite dan seeding mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-1 `Bukan bangunan – Kelompok 1`, Asset Type `Non-building`, Active On, Used By `5`; NB-OLD Active Off, nama `Kelompok khusus lama`; BLD-NP memiliki satu versi Scheduled. Kesembilan card tampil pada satu daftar. NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18). Data Dinamis: tidak ada.
- State global yang diubah: tidak ada (form Edit dan form Create ditutup tanpa perubahan, dialog Activate dibatalkan).

## Test Steps

### TC-FA-TDC-660: Tabel menjadi card list

1. Verifikasi daftar berupa card list (bukan tabel)
2. Verifikasi card NB-1: toggle Active On, judul `NB-1`, Class Name `Bukan bangunan – Kelompok 1`, Asset Type `Non-building`, Used By `5`
3. Verifikasi card NB-OLD: toggle Active Off

### TC-FA-TDC-661: Tap toggle Active membuka dialog sebagai bottom sheet

4. Tap toggle Active pada card NB-OLD
5. Verifikasi bottom sheet `Activate Tax Depreciation Class` tampil dengan bullet `NB-OLD – Kelompok khusus lama`, teks `Are you sure you want to activate it?`, tombol `Cancel` dan `Activate`
6. Tap `Cancel` pada bottom sheet
7. Verifikasi toggle NB-OLD tetap Off

### TC-FA-TDC-663: Drawer mode Edit menjadi halaman penuh tanpa tab

8. Tap judul card BLD-NP (Class Code) untuk membuka form Edit
9. Verifikasi form tampil sebagai halaman penuh tanpa tab
10. Verifikasi Alert versi Scheduled berada di bagian atas halaman
11. Verifikasi field disusun satu kolom
12. Verifikasi footer `[Clear Field]` dan `[Save]` tetap terlihat di bawah halaman
13. Kembali ke daftar Tax Depreciation Class tanpa mengubah field

### TC-FA-TDC-664: Form Create menjadi halaman penuh dengan footer tetap terlihat

14. Tap `+ Class`
15. Verifikasi form tampil sebagai halaman penuh tanpa tab
16. Verifikasi field disusun satu kolom
17. Verifikasi footer menampilkan checkbox `Stay on this form after submitting`, `[Clear Field]`, dan `[Submit]` yang tetap terlihat di bawah halaman
18. Kembali ke daftar Tax Depreciation Class tanpa mengisi field

### TC-FA-TDC-665: Popup Used By menjadi bottom sheet dengan card list

19. Tap angka Used By `5` pada card NB-1
20. Verifikasi bottom sheet `Used By` tampil
21. Verifikasi isi bottom sheet berupa card list Asset Class (bukan tabel)
22. Tutup bottom sheet `Used By`

## Notes

- Langkah penghubung (S-03): langkah 13 dan 18 (kembali ke daftar dari form yang tidak diubah; tidak ada dialog `Unsaved Changes`), langkah 22 (menutup bottom sheet).
- Urutan TC dalam spec: TC-FA-TDC-660, 661, 663, 664, lalu 665; TC-FA-TDC-662 dan TC-FA-TDC-668 (akun Read Only) ada di spec 186.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-663 dan TC-FA-TDC-664 tidak menyebut cara kembali ke daftar dari halaman penuh (tombol kembali perangkat atau tombol di header); spec menulis "kembali ke daftar" tanpa mekanisme.
  - TC-FA-TDC-665 tidak menyebut isi card list Asset Class selain bahwa bukan tabel; spec hanya mengasersi bentuk card list.
  - Seluruh TC Android ditandai `Manual Only` karena framework web tidak dapat mengotomasi aplikasi native; spec tetap ditulis dengan `coverage.mobile: automated` untuk eksekusi di perangkat Android lewat TestSpectra mobile (kemampuan disediakan tim FE).
