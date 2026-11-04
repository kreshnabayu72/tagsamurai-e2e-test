---
id: TC-FA-TDC-E2E-002-loading-dan-kegagalan-muat-tabel
title: "Loading dan Kegagalan Muat Tabel Tax Depreciation Class"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-5
  - TC-FA-TDC-6
  - TC-FA-TDC-7
coverage:
  web: automated
---

# Loading dan Kegagalan Muat Tabel Tax Depreciation Class

## Prerequisites

- Mode: FE+BE. Respons data tabel dimanipulasi lewat `Spectra.intercept()` di atas backend nyata; asersi atas baris seed yang tampil memuat state server, sehingga spec bukan `Mode: mock`.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND dalam keadaan belum diubah. Data Dinamis: tidak ada.
- Kemampuan teknis: `Spectra.intercept()` atas request data tabel Tax Depreciation Class (endpoint ditetapkan tim FE dari sumber modul; tidak dikarang di spec) untuk (a) menunda respons 3 detik dan menahannya sampai dilepas, (b) mengembalikan respons 500, dan (c) mengembalikan 500 pada percobaan pertama lalu respons normal pada percobaan berikutnya, dengan penundaan singkat pada respons kedua supaya Shimmer teramati (lihat Temuan untuk QA). Intercept dilepas segera setelah blok TC selesai (S-09).
- State global yang diubah: hanya intercept jaringan pada sesi browser; dilepas di hook `after` sebagai cadangan.

## Test Steps

### TC-FA-TDC-5: Loading tabel saat data dimuat

1. Pasang intercept: respons data tabel ditahan sampai dilepas (delay 3 detik)
2. Buka halaman utama aplikasi Fixed Asset
3. Klik menu sidebar `Accounting`
4. Klik tab `Tax Depreciation Class`
5. Verifikasi area tabel menampilkan Loading component (Shimmer) selama data dimuat
6. Lepas tahanan respons
7. Verifikasi baris data tampil
8. Verifikasi Shimmer hilang

### TC-FA-TDC-6: Tampilan error saat data tabel gagal dimuat

9. Pasang intercept: respons data tabel dipaksa gagal 500
10. Buka halaman utama aplikasi Fixed Asset
11. Klik menu sidebar `Accounting`
12. Klik tab `Tax Depreciation Class`
13. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]` (satu unit state error)
14. Verifikasi teks `No tax depreciation class` tidak tampil
15. Lepas intercept

### TC-FA-TDC-7: Try Again memuat ulang data tabel setelah gagal dimuat

16. Pasang intercept: respons data tabel gagal 500 pada percobaan pertama, lalu normal (200) pada percobaan berikutnya
17. Buka halaman utama aplikasi Fixed Asset
18. Klik menu sidebar `Accounting`
19. Klik tab `Tax Depreciation Class`
20. Klik tombol `[Try Again]`
21. Verifikasi Shimmer tampil sebentar
22. Verifikasi 7 baris seed tampil
23. Verifikasi teks `Unable to load this data.` hilang
24. Lepas intercept

## Notes

- Langkah penghubung (S-03): langkah 2, 10, dan 17 (membuka halaman utama aplikasi Fixed Asset sebelum klik sidebar, supaya pemuatan data tabel terjadi sesudah intercept dipasang), langkah 6, 15, dan 24 (melepas intercept; S-09), serta langkah 1, 9, dan 16 (memasang intercept sebagai kebutuhan Pre-setup TC, tidak diasersi).
- TC-FA-TDC-5 hanya menahan respons untuk mengamati state UI (Shimmer) dan bukan kelas fault injection; spec ini kelas b karena TC-FA-TDC-6 dan TC-FA-TDC-7 memaksa kegagalan 500. Urutan TC-FA-TDC-5 lebih dulu karena kasus tanpa kegagalan paksa dijalankan sebelum yang memaksa kegagalan.
- Asersi absence langkah 8 dan 14 didahului anchor positif langkah 7 dan 13; asersi absence langkah 23 didahului anchor langkah 22 (butir 8b.2). Langkah 8 diletakkan sesudah langkah 6 dan 7 karena toast atau state hasil belum dapat dinilai selama respons ditahan (8b.11).
- Temuan untuk QA:
  - TC-FA-TDC-7 Expected a menyebut Shimmer "tampil sebentar" tanpa menyebut penahanan respons kedua; supaya Shimmer teramati (8b.5) spec menahan respons kedua sebentar sebagai kemampuan intercept. Perlu konfirmasi QA.
  - Endpoint dan pola URL request data tabel tidak tertulis di TC; ditetapkan tim FE di tahap script (S-13).
  - Email akun Total Control tidak tertulis di TC.
