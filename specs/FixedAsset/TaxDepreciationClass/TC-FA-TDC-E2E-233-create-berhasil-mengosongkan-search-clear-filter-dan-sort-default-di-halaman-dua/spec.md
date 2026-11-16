---
id: TC-FA-TDC-E2E-233-create-berhasil-mengosongkan-search-clear-filter-dan-sort-default-di-halaman-dua
title: "Create Berhasil Mengosongkan Search, Meng-clear Filter Panel, dan Memuat Ulang Tabel di Sort Default"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-110
sourceRules: ["F-FATDC-01.k12", "T-01", "ST-02", "FI-09", "§9.5#r1"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-01.k12": 9
  "T-01": 10
  "ST-02": 11
  "FI-09": [12, 13, 15]
  "§9.5#r1": 14
coverage:
  web: automated
---

# Create Berhasil Mengosongkan Search, Meng-clear Filter Panel, dan Memuat Ulang Tabel di Sort Default

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND (`Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE) ditambah class seed tambahan lewat API sehingga tabel memuat lebih dari 10 class dan `KHS-04` jatuh di halaman 2 pada sort default Class Code A-Z (kode class tambahan berurut A-Z sebelum `KHS-04`; kodenya ditetapkan tim FE karena precondition TC tidak menyebutnya). Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-04` belum ada; form valid: Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Name `Kelompok khusus uji 4`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`. Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec. Search `NB` dan Filter Asset Type `Non-building`.
- Pemulihan: hook `after` menghapus `KHS-04` dan class seed tambahan lewat API (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-FA-TDC-110: Create berhasil (Stay tidak dicentang) mengosongkan Search, meng-clear Filter Panel, dan memuat ulang tabel di sort default

1. Ketik Search `NB`, tekan Enter
2. Buka Filter Panel
3. Pilih Asset Type `Non-building` pada Filter Panel
4. Klik `[Apply]`
5. Klik sort pada kolom Class Name satu kali
6. Klik `+ Class` di toolbar
7. Isi form valid dengan Class Code `KHS-04` (Non-building, Useful Life `8`, Straight Line)
8. Klik `[Submit]`
9. Verifikasi Drawer menutup
10. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
11. Verifikasi baris `KHS-04` di-highlight sesaat
12. Verifikasi kotak Search kosong
13. Verifikasi chip filter aktif hilang (Filter Panel di-clear)
14. Verifikasi tabel di sort default Class Code A-Z
15. Verifikasi tabel menampilkan halaman yang memuat `KHS-04`

## Notes

- Langkah penghubung (S-03): tidak ada.
- Urutan Expected diasersi mengikuti urutan state (8b.5): highlight baris `KHS-04` (langkah 11) diasersi lebih dulu karena bersifat sesaat, sebelum asersi Search, Filter, sort, dan halaman.
- Pembagian TC lintas spec: TC-FA-TDC-110 ada di spec ini karena membutuhkan tabel lebih dari 10 class; TC Create sukses lain (TC-FA-TDC-105 sampai 109) ada di spec `TC-FA-TDC-E2E-041-create-class-sukses-non-building-building-dan-land` dan `TC-FA-TDC-E2E-042-create-sukses-varian-metode-straight-line-saja-dan-declining-balance-saja`.
- Langkah 1 sampai 5 memberi Search, Filter, dan sort sebagai state yang dikosongkan oleh Create; sort Class Name diklik satu kali sesuai TC (arah sort ditetapkan aplikasi).
- Temuan untuk QA:
  - Precondition d TC-FA-TDC-110 ("Tabel memuat > 10 class sehingga class baru berada di halaman 2") tidak menyebut kode class tambahan; spec mensyaratkan seed tambahan lewat API yang kodenya berurut sebelum `KHS-04`.
  - Langkah 7 mengikuti TC ("Isi form valid"); nilai Regulation Reference dan Class Name tidak ditulis TC, spec memakai nilai dasar TC-FA-TDC-105.
  - Post Condition TC-FA-TDC-110 ("Pilihan page size tidak berubah") tidak punya langkah observasi di TC; spec tidak mengasersinya (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
