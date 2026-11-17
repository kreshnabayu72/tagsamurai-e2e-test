---
id: TC-FA-TDC-E2E-051-create-pilih-asset-type-land-building-non-building-mengatur-field-dan-opsi
title: "Create - Pilih Asset Type Land, Building, dan Non-building Mengatur Field dan Opsi"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-162
  - TC-FA-TDC-163
  - TC-FA-TDC-164
sourceRules: ["ST-08", "FI-01", "FI-02", "ST-10", "ST-09"]
smoke: []
dependsOn: []
trace:
  "ST-08": [4, 6, 8]
  "FI-01": [5, 6, 9]
  "FI-02": [15, 16, 17, 20]
  "ST-10": 17
  "ST-09": [18, 19, 24, 26]
coverage:
  web: automated
---

# Create - Pilih Asset Type Land, Building, dan Non-building Mengatur Field dan Opsi

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: tujuh class seed bawaan (`Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE) dalam keadaan belum diubah. Master Data Count Limit belum tercapai.
- Data Dinamis: tidak ada data yang disimpan (tidak ada Submit). Nilai yang dipilih atau diketik: Asset Type `Non-building`, `Building`, `Land`; Useful Life `8` dan `20`; Allowed Methods `Straight Line` dan `Declining Balance`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-162: Create - pilih Asset Type Land menonaktifkan dan mengosongkan Useful Life, Allowed Methods, dan rate

1. Klik `+ Class` di toolbar
2. Pilih Asset Type `Non-building`, isi Useful Life `8`, pilih Allowed Methods `Straight Line`
3. Ganti Asset Type menjadi `Land`
4. Verifikasi Useful Life dan Allowed Methods tampil tetapi Disabled dengan helper "Land is not depreciated."
5. Verifikasi nilai Useful Life dan Allowed Methods dikosongkan
6. Verifikasi rate Straight Line dan Declining Balance Disabled tanpa nilai
7. Ganti Asset Type kembali menjadi `Non-building`
8. Verifikasi Useful Life dan Allowed Methods enabled kembali
9. Verifikasi Useful Life dan Allowed Methods tetap kosong

### TC-FA-TDC-163: Create - pilih Asset Type Building menonaktifkan opsi Declining Balance dan melepas pilihan sebelumnya

10. Isi Useful Life `20`
11. Pilih Allowed Methods `Straight Line` dan `Declining Balance`
12. Ganti Asset Type menjadi `Building`
13. Buka dropdown Allowed Methods
14. Arahkan kursor ke opsi `Declining Balance`
15. Verifikasi pilihan `Declining Balance` dilepas otomatis
16. Verifikasi `Straight Line` tetap terpilih
17. Verifikasi rate Declining Balance dikosongkan dan disembunyikan
18. Verifikasi opsi `Declining Balance` tampil tetapi Disabled
19. Verifikasi tooltip "Declining balance does not apply to buildings." muncul saat hover
20. Verifikasi opsi `Straight Line` tetap enabled

### TC-FA-TDC-164: Create - ganti Asset Type dari Building ke Non-building mengaktifkan kembali opsi Declining Balance

21. Tutup dropdown Allowed Methods
22. Ganti Asset Type menjadi `Non-building`
23. Buka dropdown Allowed Methods
24. Verifikasi opsi `Declining Balance` enabled kembali dan dapat dipilih
25. Arahkan kursor ke opsi `Declining Balance`
26. Verifikasi tidak ada tooltip "Declining balance does not apply to buildings."
27. Tutup dropdown Allowed Methods
28. Klik `[Clear Field]`
29. Klik ikon ✕ pada Drawer

## Notes

- Langkah penghubung (S-03): langkah 10 dan 11 (mengisi ulang Useful Life dan Allowed Methods sebagai keadaan awal TC-FA-TDC-163 sesudah kembali ke `Non-building` kosong pada langkah 7), langkah 21 dan 27 (menutup dropdown), langkah 28 (`[Clear Field]` mengosongkan form; S-09), langkah 29 (menutup Drawer yang bersih).
- Langkah 22 memulai TC-FA-TDC-164 dari keadaan `Building` hasil TC-FA-TDC-163 (TC-FA-TDC-164 memulai dari `Building`, lalu `Non-building`); langkah 2 TC-FA-TDC-164 ("Pilih Asset Type `Building`") sudah terpenuhi oleh langkah 12.
- Asersi absence langkah 26 didahului anchor positif langkah 24 dan hover pada langkah 25 (8b.2).
- Pembagian TC lintas spec: perhitungan dan tampilan rate (TC-FA-TDC-165 sampai 172) ada di spec `TC-FA-TDC-E2E-052-create-rate-tampil-mengikuti-metode-read-only-dan-batas-seratus` dan `TC-FA-TDC-E2E-053-create-rate-bulat-pembulatan-dua-desimal-half-up-dan-useful-life-maksimum`.
- Temuan untuk QA:
  - TC-FA-TDC-162 Expected b menyebut rate Straight Line dan Declining Balance "Disabled tanpa nilai", sedangkan TC-FA-TDC-103 b.vii dan TC-FA-TDC-165/166 menyebut rate "tidak tampil" bila belum ada metode atau Useful Life. Spec mengikuti masing-masing TC apa adanya; perlu konfirmasi QA apakah rate pada Land tampil Disabled atau tersembunyi.
  - TC-FA-TDC-163 Expected c menyebut opsi "tampil tetapi Disabled" dan tooltip saat hover; spec menjalankan hover (langkah 14) sebelum asersi tooltip (langkah 19).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
