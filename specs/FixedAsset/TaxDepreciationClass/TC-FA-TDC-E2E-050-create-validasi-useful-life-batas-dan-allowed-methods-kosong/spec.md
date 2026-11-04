---
id: TC-FA-TDC-E2E-050-create-validasi-useful-life-batas-dan-allowed-methods-kosong
title: "Create - Validasi Batas Useful Life dan Allowed Methods Kosong"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-157
  - TC-FA-TDC-158
  - TC-FA-TDC-159
coverage:
  web: automated
---

# Create - Validasi Batas Useful Life dan Allowed Methods Kosong

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai.
- Data Dinamis: tidak ada data yang disimpan (Submit diblokir validasi). Data Uji dasar: Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Code `KHS-M1` (literal TC; Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; seeding idempotent, suite serial, kode berbeda antar spec), Class Name `Kelompok uji validasi`, Asset Type `Non-building`, Useful Life `8`; Allowed Methods belum dipilih. Nilai Useful Life uji: `0`, `101`, `150`, `1.5`, `1`, `100`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-157: Create - Useful Life di luar 1-100 atau bukan bilangan bulat ditolak saat mengetik

1. Klik `+ Class` di toolbar
2. Ketik `0` pada Useful Life
3. Verifikasi caption "Useful life must be between 1 and 100 years" muncul segera (`0`)
4. Ganti isi Useful Life dengan `101`
5. Verifikasi caption "Useful life must be between 1 and 100 years" muncul segera (`101`)
6. Ganti isi Useful Life dengan `150`
7. Verifikasi caption "Useful life must be between 1 and 100 years" muncul segera (`150`)
8. Ganti isi Useful Life dengan `1.5`
9. Verifikasi caption "Useful life must be between 1 and 100 years" muncul segera (`1.5`)

### TC-FA-TDC-158: Create - Useful Life 1 dan 100 diterima sebagai batas bawah dan atas

10. Ganti isi Useful Life dengan `1`
11. Verifikasi tidak ada caption error pada Useful Life (`1`)
12. Ganti isi Useful Life dengan `100`
13. Verifikasi tidak ada caption error pada Useful Life (`100`)

### TC-FA-TDC-159: Create - Allowed Methods kosong pada Asset Type Non-building ditolak

14. Klik `[Clear Field]`
15. Isi field lain sesuai Data Uji; biarkan Allowed Methods belum dipilih
16. Klik `[Submit]`
17. Verifikasi caption "Allowed methods must not be empty" muncul pada Allowed Methods
18. Verifikasi Drawer tetap terbuka
19. Verifikasi tabel di belakang Drawer tetap berisi 7 class seed tanpa baris baru (tidak ada data tersimpan)
20. Klik `[Clear Field]`
21. Klik ikon ✕ pada Drawer

## Notes

- Langkah penghubung (S-03): langkah 14 dan 20 (`[Clear Field]` mengosongkan form dan caption sebelum kasus berikutnya atau sebelum menutup Drawer; S-09), langkah 4, 6, 8, 10, dan 12 ("Ganti isi" Useful Life menggantikan nilai sebelumnya), langkah 21 (menutup Drawer yang bersih).
- Satu pembukaan Drawer dipakai untuk TC-FA-TDC-157 dan TC-FA-TDC-158 (kasus tanpa submit); TC-FA-TDC-159 menutup dengan Submit yang diblokir (prinsip 3).
- Asersi absence langkah 11 dan 13 didahului anchor positif: caption error pada Useful Life tampil pada langkah 9 sebelumnya di Drawer yang sama (8b.2).
- Pembagian TC lintas spec: validasi Useful Life kosong (TC-FA-TDC-156) ada di spec `TC-FA-TDC-E2E-049-create-validasi-regulation-reference-asset-type-dan-useful-life-kosong`.
- Temuan untuk QA:
  - TC-FA-TDC-157 menguji `1.5` pada field Number input; perilaku browser pada input angka desimal tidak disebut TC, spec mengasersi caption sesuai Expected d.
  - Post Condition TC-FA-TDC-157, 158, dan 159 ("Tidak ada data berubah dan tidak ada entri log") tidak punya langkah observasi di TC; spec mengasersi data lewat jumlah baris tabel pada Expected b TC-FA-TDC-159 dan tidak mengasersi entri log (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
