---
id: TC-FA-PREF-E2E-036-default-capitalization-threshold-validasi-batas-v-02-dan-v-03
title: "Default Capitalization Threshold: Nilai Minus, Batas 0, 16 Digit, 17 Digit, Validasi V-02 dan V-03"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-133
  - TC-FA-PREF-134
  - TC-FA-PREF-135
  - TC-FA-PREF-136
  - TC-FA-PREF-137
coverage:
  web: automated
---

# Default Capitalization Threshold: Nilai Minus, Batas 0, 16 Digit, 17 Digit, Validasi V-02 dan V-03

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth) dengan Preferences nilai awal PA-2 (Default Capitalization Threshold 5.000.000, tidak terkunci, semua setting wajib terisi) dan tiga Asset Class memakai threshold default (PA-16: IT Equipment, Vehicles, Furniture) untuk TC-FA-PREF-135.
- Format angka tetap platform: pemisah ribuan titik, pemisah desimal koma, mata uang Rupiah (PA-1).
- State yang diubah spec: Default Capitalization Threshold tersimpan menjadi 0 pada langkah 14 (TC-FA-PREF-135) dan entri Changelog Edit baru (audit trail permanen, tidak dipulihkan). Preferences dipulihkan ke PA-2 lewat seed pada langkah 16 dan di hook `after`.
- Kemampuan teknis: seed dan pemulihan Preferences lewat sesi API aktor (butir "Seed dan pemulihan lewat API" dan "Sesi API aktor" di `suite.md`), disediakan tim FE/BE.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-133: Default Capitalization Threshold -1 diterima di input dan langsung menampilkan caption V-02

1. Ganti isi CurrencyInput Default Capitalization Threshold dengan "-1"
2. Verifikasi input menampilkan "-1"
3. Verifikasi caption "Capitalization threshold must be 0 or more" tampil langsung tanpa menunggu Save
4. Klik `[Save changes]`
5. Verifikasi dialog "Save Changes" tidak tampil dan tidak ada toast
6. Verifikasi caption "Capitalization threshold must be 0 or more" tetap tampil
7. Klik `[Cancel]`

### TC-FA-PREF-134: Default Capitalization Threshold -0.01 (satu langkah di bawah 0) menampilkan caption V-02

8. Ganti isi CurrencyInput Default Capitalization Threshold dengan "-0.01"
9. Verifikasi caption "Capitalization threshold must be 0 or more" tampil langsung

### TC-FA-PREF-135: Default Capitalization Threshold 0 (tepat batas) diterima dan dapat disimpan

10. Ganti isi CurrencyInput Default Capitalization Threshold dengan "0"
11. Verifikasi tidak ada caption pada field
12. Klik `[Save changes]`
13. Verifikasi dialog "Save Changes" tampil dengan daftar bullet "3 asset classes use the default threshold.", pertanyaan "Are you sure you want to save these changes?", serta tombol `[Cancel]` (text, contrast) dan `[Save]`
14. Klik `[Save]` pada dialog
15. Verifikasi toast sukses "Success, accounting preferences have been saved."
16. Pulihkan Preferences ke nilai awal PA-2 lewat sesi API hingga tersimpan, lalu muat ulang halaman Preferences

### TC-FA-PREF-136: Default Capitalization Threshold 16 digit bulat (tepat batas) diterima tanpa caption

17. Ganti isi CurrencyInput Default Capitalization Threshold dengan "9999999999999999" (16 digit)
18. Verifikasi saat diketik input menampilkan "9.999.999.999.999.999"
19. Pindahkan fokus keluar dari input (blur)
20. Verifikasi setelah blur addon awalan "Rp" dan input "9.999.999.999.999.999,00"
21. Verifikasi tidak ada caption pada field

### TC-FA-PREF-137: Default Capitalization Threshold 17 digit bulat (satu di atas batas) menampilkan caption V-03

22. Ganti isi CurrencyInput Default Capitalization Threshold dengan "10000000000000000" (17 digit)
23. Verifikasi input menampilkan "10.000.000.000.000.000"
24. Verifikasi caption "Capitalization threshold is too large" tampil langsung tanpa menunggu Save
25. Klik `[Save changes]`
26. Verifikasi dialog "Save Changes" tidak tampil dan tidak ada toast
27. Verifikasi caption "Capitalization threshold is too large" tetap tampil
28. Klik `[Cancel]`

## Notes

- Urutan mengikuti nomor TC; satu-satunya Save yang berhasil (TC-FA-PREF-135) dipulihkan lewat seed (langkah 16) sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03): langkah 7 (`[Cancel]` membersihkan caption identik sebelum TC-FA-PREF-134; R-12), 16 (pemulihan seed dan muat ulang), dan 28 (`[Cancel]` agar spec tidak berakhir dengan form dirty; S-09). Langkah 1, 8, 10, 17, dan 22 mengganti isi field yang sudah berisi.
- Asersi absence dialog dan toast (langkah 5 dan 26) memakai caption yang tetap tampil (langkah 6 dan 27) sebagai anchor positif (8b.11).
- Temuan untuk QA:
  - Step 2 TC-FA-PREF-134 mengetik "-0.01" dengan titik sebagai pemisah desimal, sedangkan TC-FA-PREF-138, 139, dan 140 mengetik desimal dengan koma (format platform: desimal koma). Spec menyalin "-0.01" apa adanya; perlu dikonfirmasi apakah "-0,01" yang dimaksud.
  - Post Condition TC-FA-PREF-135 ("Default Capitalization Threshold tersimpan 0"; entri Changelog Field Default Capitalization Threshold, Old Value 5.000.000, New Value 0) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01). Data Dinamis DA-3 menyebut TC-FA-PREF-135 diverifikasi sebagai Post Condition, tetapi tidak ada langkah yang membacanya.
  - Post Condition TC-FA-PREF-133 dan 137 ("Tidak ada perubahan data Preferences tersimpan"; "Tidak ada entri log baru") tidak punya langkah observasi sehingga tidak diasersi (S-01).
