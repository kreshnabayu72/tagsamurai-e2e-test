---
id: TC-FA-FAAC-E2E-081-mode-create-draft-asset-name-screening-dan-pemilihan-draft
title: "Mode Create: Screening Tab Asset Names, Dialog Assign, dan Pemilihan Draft Asset Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-254
  - TC-FA-FAAC-255
  - TC-FA-FAAC-256
  - TC-FA-FAAC-657
coverage:
  web: automated
---

# Mode Create: Screening Tab Asset Names, Dialog Assign, dan Pemilihan Draft Asset Name

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Name tanpa Asset Class: Forklift 3T (6 aset aktif), Laptop Standard (120 aset aktif), Pallet Jack Electric (0 aset aktif); Asset Name "Delivery Van" ter-assign ke 'Vehicles'. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; kemampuan baca BE untuk jumlah Asset Name tanpa Asset Class dan jumlah Asset Class.
- State global: tidak ada yang diubah (form Create dibuang lewat [Leave]).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Baca jumlah Asset Name tanpa Asset Class sebagai baseline

### TC-FA-FAAC-254: Tab Asset Names pada Halaman Detail mode Add Asset Class Enabled

2. Klik tombol "+ Asset Class"
3. Klik tab "Asset Names"
4. Verifikasi tab "Asset Names" Enabled dan dapat dibuka pada mode Add Asset Class (bukan Disabled)
5. Verifikasi tombol "+ Assign Asset Names" tampil dan Enabled

### TC-FA-FAAC-657: Judul dialog Assign Asset Names pada mode Add Asset Class tanpa nama kelas

6. Klik tombol "+ Assign Asset Names"
7. Verifikasi judul dialog berbunyi "Assign Asset Names" tanpa bagian "to [Class Name]" karena Asset Class belum disimpan

### TC-FA-FAAC-255: Dialog Assign pada mode Add Asset Class tanpa kolom Current Class dan tanpa checkbox Without asset class only

8. Verifikasi kolom tabel picker: Asset Name, Category, Label, Assets
9. Verifikasi tidak ada kolom Current Class
10. Verifikasi checkbox "Without asset class only" tidak ada pada toolbar
11. Verifikasi kandidat hanya Asset Name tanpa Asset Class: "Forklift 3T", "Laptop Standard", dan "Pallet Jack Electric" tampil
12. Verifikasi "Delivery Van" (sudah di Vehicles) tidak tampil

### TC-FA-FAAC-256: Memilih Asset Name melalui Assign Asset Names pada mode Add Asset Class menahannya sebagai draft

13. Centang "Forklift 3T" dan "Laptop Standard"
14. Klik [Assign]
15. Verifikasi dialog Assign menutup
16. Verifikasi "Forklift 3T" dan "Laptop Standard" tampil pada daftar draft tab Asset Names
17. Klik breadcrumb "Asset Class"
18. Verifikasi dialog Unsaved Changes tampil
19. Klik [Leave]
20. Verifikasi jumlah Asset Name tanpa Asset Class sama dengan baseline langkah 1 (kedua Asset Name masih terhitung pada banner Asset Name tanpa Asset Class; belum ter-assign ke Asset Class mana pun)

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan TC dalam spec: 254, 657, 255, 256 (screening tab dan dialog pada form Create yang sama; TC-256 menutup form dirty di akhir).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name seed dipakai apa adanya; spec tidak men-submit Asset Class sehingga tidak ada Asset Name yang ter-assign.
- Langkah penghubung (S-03): langkah 1 (baseline S-12), 17 sampai 19 (menutup form dirty sesuai S-08).
- Langkah 5 dan 8 menjadi anchor positif bagi asersi absence langkah 9 sampai 12 (bagian 8b butir 2).
- Temuan untuk QA: format banner Asset Name tanpa Asset Class tidak disebut TC-256; spec mengasersi jumlah dari kemampuan baca BE.
