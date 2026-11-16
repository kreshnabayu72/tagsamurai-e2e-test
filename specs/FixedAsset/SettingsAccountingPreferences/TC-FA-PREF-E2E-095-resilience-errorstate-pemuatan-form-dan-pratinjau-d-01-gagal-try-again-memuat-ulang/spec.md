---
id: TC-FA-PREF-E2E-095-resilience-errorstate-pemuatan-form-dan-pratinjau-d-01-gagal-try-again-memuat-ulang
title: "Resilience ErrorState: Pemuatan Form dan Pratinjau D-01 Gagal, Try Again Memuat Ulang"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-74
  - TC-FA-PREF-75
  - TC-FA-PREF-205
  - TC-FA-PREF-206
sourceRules: ["ST-22", "ST-03", "§4.2b#b4", "F-FAPREF-01.k21d", "F-FAPREF-01.k21b", "T-01", "F-FAPREF-01.k22b", "ST-21", "PV-01"]
smoke: []
dependsOn: []
trace:
  "ST-22": [3, 14, 24]
  "ST-03": [3, 4]
  "§4.2b#b4": [14, 24, 26]
  "F-FAPREF-01.k21d": 15
  "F-FAPREF-01.k21b": 17
  "T-01": 18
  "F-FAPREF-01.k22b": 18
  "ST-21": 26
  "PV-01": 28
anchor: [8, 9]
coverage:
  web: automated
---

# Resilience ErrorState: Pemuatan Form dan Pratinjau D-01 Gagal, Try Again Memuat Ulang

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; asersi memuat state backend pada TC-FA-PREF-205).
- Kelas harness: b (fault injection, 5xx).
- Akun aktor: Total Control (Pre-setup PA-1 dan PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PA-2 untuk TC-FA-PREF-74 dan 75 dan PB-1 untuk TC-FA-PREF-205 dan 206 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date); akun Chart of Accounts PB-2; Asset Class IT Equipment, Vehicles, Furniture (PB-3; hasil dampak "2 asset classes use the default threshold."). Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang ke nilai awal PB-1 dilakukan lewat langkah penghubung (langkah 20).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk membalas permintaan pemuatan data Preferences dengan 5xx (langkah 1 sampai 7) dan permintaan hitungan dampak D-01 dengan 5xx (langkah 11 dan 21), serta menahan respons hitungan dampak sampai dilepas agar Shimmer teramati (langkah 21 sampai 27); intercept dilepas segera setelah pemicu selesai (S-09).
- State yang diubah spec: Default Capitalization Threshold tersimpan 10.000.000 pada TC-FA-PREF-205 (dipulihkan pada langkah 20 dan di hook `after`, tetap jalan bila spec gagal di tengah) dan form yang dirty (dikembalikan pada langkah 29 dan 30).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-74: Form menampilkan ErrorState dengan tombol Try Again saat pemuatan data gagal

1. Pasang intercept agar respons pemuatan data Preferences gagal (5xx)
2. Muat ulang halaman dengan F5
3. Verifikasi form menampilkan ErrorState "Unable to load this data." disertai tombol [Try Again]
4. Verifikasi SectionCard dan nilai setting tidak tampil

### TC-FA-PREF-75: Klik Try Again setelah pemuatan gagal memuat ulang form

5. Muat ulang halaman dengan F5 hingga ErrorState tampil (respons pemuatan tetap gagal 5xx)
6. Lepas intercept pemuatan sehingga respons pemuatan menjadi sukses
7. Klik [Try Again]
8. Verifikasi form dimuat ulang dan tampil dengan nilai tersimpan: Fiscal Year Start "January", First Accounting Period "March" "2026", Default Capitalization Threshold "Rp 5.000.000,00", In-service Date Source "Activation date"
9. Verifikasi ErrorState "Unable to load this data." hilang

### TC-FA-PREF-205: Area pratinjau D-01 menampilkan ErrorState saat hitungan gagal dimuat dan [Save] tetap dapat diklik

10. Seed ulang Preferences ke nilai awal PB-1 hingga tersimpan
11. Pasang intercept agar permintaan hitungan dampak dibalas 5xx
12. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
13. Klik [Save changes]
14. Verifikasi area pratinjau dampak pada dialog D-01 menampilkan ErrorState "Unable to load this data." dengan tombol [Try Again]
15. Verifikasi tombol [Save] pada dialog D-01 berstatus Enabled
16. Klik [Save] pada dialog D-01
17. Verifikasi dialog D-01 tertutup
18. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
19. Lepas intercept hitungan dampak
20. Pulihkan Preferences ke nilai awal PB-1 lewat seed hingga tersimpan

### TC-FA-PREF-206: Klik [Try Again] pada ErrorState D-01 memuat ulang hitungan dampak

21. Pasang intercept agar permintaan hitungan dampak pertama dibalas 5xx dan permintaan berikutnya ditahan sampai dilepas
22. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
23. Klik [Save changes]
24. Verifikasi ErrorState "Unable to load this data." tampil dengan tombol [Try Again] pada area pratinjau dialog D-01
25. Klik [Try Again] pada ErrorState di dialog D-01
26. Verifikasi area pratinjau menampilkan Shimmer
27. Lepas tahanan respons hitungan dampak
28. Verifikasi area pratinjau menampilkan bullet "2 asset classes use the default threshold."
29. Klik [Cancel] pada dialog D-01
30. Klik [Cancel] pada form Preferences

## Notes

- Langkah penghubung (S-03, S-09): langkah 5 (muat ulang agar ErrorState tampil sebagai precondition TC-FA-PREF-75), langkah 6 (melepas intercept pemuatan), langkah 10 dan 20 (seed ulang), langkah 19 dan 27 (melepas intercept dan tahanan respons), dan langkah 29 dan 30 (mengembalikan form dirty ke nilai tersimpan, tanpa Verifikasi). Langkah 26 diletakkan segera setelah klik [Try Again] dan sebelum tahanan respons dilepas (bagian 8b butir 5).
- Langkah 4 (absence "SectionCard dan nilai setting tidak tampil") memakai ErrorState pada langkah 3 sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-PREF-205 Post Condition ("Preferences company menyimpan Default Capitalization Threshold = 10.000.000") tidak punya langkah observasi di TC dan tidak diasersi (S-01); pemulihan nilai awal pada langkah 20.
  - TC-FA-PREF-206 Expected b menyebut "Shimmer lalu bullet"; Shimmer adalah state sementara sehingga spec menahan respons hitungan dampak lewat intercept agar teramati (bagian 8b butir 5 dan 11); kemampuan menahan respons disediakan tim FE. TC-FA-PREF-206 Post Condition ("Preferences company belum berubah") tidak diasersi karena tidak punya langkah observasi.
  - TC-FA-PREF-74 dan 75 memakai seri PA sedangkan TC-FA-PREF-205 dan 206 memakai seri PB; spec mengasumsikan nilai awal keduanya setara.
  - TC-FA-PREF-75 langkah 2 ("Buka Tab Preferences hingga ErrorState tampil") tidak menyebut cara memicu pemuatan ulang; spec memakai muat ulang halaman.
