---
id: TC-FA-TDC-E2E-234-create-tombol-clear-field-mengosongkan-semua-field-tanpa-menutup-drawer
title: "Create - Tombol Clear Field Mengosongkan Semua Field Tanpa Menutup Drawer"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-113
coverage:
  web: automated
---

# Create - Tombol Clear Field Mengosongkan Semua Field Tanpa Menutup Drawer

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: tujuh class seed bawaan (`Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE) dalam keadaan belum diubah. Master Data Count Limit belum tercapai.
- Data Dinamis: tidak ada data yang disimpan (tidak ada Submit). Nilai yang diketik: Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Code `KHS-07`, Class Name `Kelompok uji validasi`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-113: Tombol Clear Field pada Drawer Create mengosongkan semua field tanpa menutup Drawer

1. Klik `+ Class` di toolbar
2. Isi semua field: Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `KHS-07`, Class Name `Kelompok uji validasi`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`
3. Kosongkan Class Name
4. Klik di luar field Class Name agar caption error tampil (tanpa Submit)
5. Centang checkbox "Stay on this form after submitting"
6. Klik `[Clear Field]`
7. Verifikasi field Regulation Reference kosong
8. Verifikasi field Class Code kosong
9. Verifikasi field Class Name kosong
10. Verifikasi Asset Type kembali ke placeholder "Select asset type"
11. Verifikasi field Useful Life kosong
12. Verifikasi Allowed Methods kembali ke placeholder "Select allowed methods"
13. Verifikasi caption error dihapus
14. Verifikasi border merah dihapus
15. Verifikasi Drawer tetap terbuka
16. Verifikasi fokus berada di field Regulation Reference
17. Verifikasi tidak ada dialog konfirmasi apa pun yang muncul
18. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang
19. Tutup Drawer dengan klik ikon ✕

## Notes

- Langkah penghubung (S-03): langkah 19 (menutup Drawer yang bersih).
- Langkah 3 dan 4 mengikuti TC ("Kosongkan Class Name lalu klik di luar field agar caption error tampil"); langkah 13 dan 14 ditulis per klausa karena caption dan border adalah klausa berbeda (S-01).
- Asersi absence langkah 17 didahului anchor positif langkah 15 (Drawer masih terbuka pada permukaan yang sama; 8b.2).
- Pembagian TC lintas spec: tidak ada; TC-FA-TDC-113 hanya ada di spec ini. Create dengan checkbox Stay (TC-FA-TDC-111 dan 112) ada di spec `TC-FA-TDC-E2E-043-create-stay-on-form-checkbox-default-dan-dipertahankan`.
- Temuan untuk QA:
  - Langkah 2 mengikuti TC ("Isi semua field"); nilai Regulation Reference dan Class Name tidak ditulis TC, spec memakai nilai dasar yang dipakai TC validasi lain.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
