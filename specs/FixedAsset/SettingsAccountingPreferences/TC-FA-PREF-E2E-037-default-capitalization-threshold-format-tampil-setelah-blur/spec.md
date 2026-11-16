---
id: TC-FA-PREF-E2E-037-default-capitalization-threshold-format-tampil-setelah-blur
title: "Default Capitalization Threshold: Format Tampil Setelah Blur, Desimal, dan Digit Desimal Ketiga Diblok"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-138
  - TC-FA-PREF-139
  - TC-FA-PREF-140
  - TC-FA-PREF-141
sourceRules: ["FAPREF-LOGIC-03e", "V-02", "V-03"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-03e": [2, 4, 8, 13, 16, 18]
  "V-02": [5, 9]
  "V-03": [11, 14]
coverage:
  web: automated
---

# Default Capitalization Threshold: Format Tampil Setelah Blur, Desimal, dan Digit Desimal Ketiga Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth) dengan Preferences nilai awal PA-2 (Default Capitalization Threshold 5.000.000, tidak terkunci, semua setting wajib terisi). Format angka tetap platform: pemisah ribuan titik, pemisah desimal koma, mata uang Rupiah (PA-1).
- State yang diubah spec: tidak ada Save; form dikembalikan ke nilai tersimpan pada langkah 19.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-138: Dua desimal ditampilkan dengan pemisah ribuan, simbol mata uang, dan dua desimal setelah blur

1. Ganti isi CurrencyInput Default Capitalization Threshold dengan "1234,56"
2. Verifikasi saat diketik input menampilkan "1.234,56"
3. Pindahkan fokus keluar dari input (blur)
4. Verifikasi setelah blur addon awalan "Rp" dan input "1.234,56"
5. Verifikasi tidak ada caption pada field

### TC-FA-PREF-139: Digit desimal ketiga diblok di input tanpa caption

6. Ganti isi CurrencyInput Default Capitalization Threshold dengan "1234,56"
7. Ketik digit "7" setelah "1234,56"
8. Verifikasi input tetap menampilkan "1.234,56" (digit ketiga tidak masuk)
9. Verifikasi tidak ada caption pada field

### TC-FA-PREF-140: 16 digit bulat dengan dua desimal (nilai maksimum) diterima

10. Ganti isi CurrencyInput Default Capitalization Threshold dengan "9999999999999999,99"
11. Verifikasi saat diketik input menampilkan "9.999.999.999.999.999,99"
12. Pindahkan fokus keluar dari input (blur)
13. Verifikasi setelah blur addon awalan "Rp" dan input "9.999.999.999.999.999,99"
14. Verifikasi tidak ada caption pada field

### TC-FA-PREF-141: Nominal tanpa desimal ditampilkan dengan simbol mata uang, pemisah ribuan, dan dua desimal setelah blur

15. Ganti isi CurrencyInput Default Capitalization Threshold dengan "5000000"
16. Verifikasi saat diketik input menampilkan "5.000.000"
17. Pindahkan fokus keluar dari input (blur)
18. Verifikasi setelah blur addon awalan "Rp" dan input "5.000.000,00"
19. Klik `[Cancel]`

## Notes

- Kasus tanpa submit: satu pembukaan halaman dan field diganti isinya di antara kasus (bagian 3, halaman yang sama dipakai berulang).
- Langkah penghubung (S-03): langkah 19 (`[Cancel]` mengembalikan form ke nilai tersimpan agar spec tidak berakhir dirty; S-09). Langkah 1, 6, 10, dan 15 mengganti isi field yang sudah berisi.
- Nilai yang diketik pada langkah 6 sama dengan langkah 1 (disalin utuh dari TC; S-04); langkah 7 mengetik digit ketiga sesudahnya.
- Temuan untuk QA:
  - TC-FA-PREF-138 mengetik "1234,56" dan TC-FA-PREF-134 (spec 036) mengetik "-0.01" dengan titik sebagai pemisah desimal; konsistensi pemisah desimal pada Data Uji perlu dikonfirmasi.
  - TC-FA-PREF-139 menyebut Data Uji `1234,567` tetapi Langkah hanya mengetik digit "7" setelah "1234,56"; spec mengikuti Langkah.
