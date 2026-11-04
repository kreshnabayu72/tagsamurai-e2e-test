---
id: TC-FA-TDC-E2E-126-konflik-d-13-esc-save-tanpa-ubah-class-code-dan-fokus
title: "Konflik D-13: Esc dan Fokus Dialog serta Save Tanpa Mengubah Class Code Tetap Berhasil"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-213
  - TC-FA-TDC-214
  - TC-FA-TDC-921
coverage:
  web: automated
---

# Konflik D-13: Esc dan Fokus Dialog serta Save Tanpa Mengubah Class Code Tetap Berhasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): fixture BE yang memajukan Last Posted Tax Year `KHS-D13` ke 2026 (menyerupai posting penyusutan fiskal J-03; kemampuan disediakan tim FE/BE). Sesi B tidak membuka UI dan hasilnya tidak diasersi.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk class berkunci), flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsD13` | `KHS-D13` | Non-building, Used By 0, Last Posted Tax Year kosong (Class Code belum terkunci), Class Name `Kelompok D13`, Active |

- `KHS-D13` diseed ulang lewat API sebelum blok TC-FA-TDC-214 (langkah 14) karena blok pertama sudah mengunci Class Code; Last Posted Tax Year dipulihkan ke kosong di hook `after`.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-213 dan TC-FA-TDC-921: Esc dan fokus ter-trap pada dialog D-13

1. Ketik Search `KHS-D13`, tekan Enter
2. Klik link Class Code `KHS-D13` (Drawer Edit; Class Code enabled)
3. Fixture BE (sesi B): majukan Last Posted Tax Year `KHS-D13` ke 2026 hingga tersimpan
4. Ganti Class Code menjadi `KHS-D13B`
5. Klik `[Save]`
6. Verifikasi dialog D-13 muncul
7. Tekan Tab berulang
8. Verifikasi fokus tetap di dalam dialog D-13 pada satu-satunya tombol `[OK]` dan tidak keluar ke halaman
9. Tekan Esc
10. Verifikasi dialog D-13 tertutup
11. Verifikasi Drawer memuat ulang status kunci: Class Code Disabled dengan ikon gembok
12. Verifikasi tidak ada yang tersimpan: Class Code pada Drawer tetap bernilai `KHS-D13`
13. Klik ikon ✕ pada Drawer

### TC-FA-TDC-214: Save yang tidak mengubah Class Code tetap berhasil walau kunci berubah saat Drawer terbuka

14. Pulihkan class `KHS-D13` lewat seeding API ke Class Code belum terkunci (Last Posted Tax Year kosong, Class Name `Kelompok D13`)
15. Klik link Class Code `KHS-D13`
16. Fixture BE (sesi B): majukan Last Posted Tax Year `KHS-D13` ke 2026 hingga tersimpan
17. Ganti Class Name menjadi `Kelompok D13 baru` tanpa mengubah Class Code
18. Klik `[Save]`
19. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
20. Verifikasi dialog D-13 tidak muncul
21. Verifikasi baris `KHS-D13` di tabel menampilkan Class Name `Kelompok D13 baru`
22. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC dalam satu alur: TC-FA-TDC-213 dan TC-FA-TDC-921 memiliki precondition dan langkah 1 sampai 3 yang identik, sehingga dijalankan sebagai satu alur dengan satu pembukaan dialog D-13. Expected TC-FA-TDC-921 a (fokus) pada langkah 8, Expected TC-FA-TDC-213 a (dialog tertutup, Drawer memuat ulang status kunci, tidak ada yang tersimpan) dan Expected TC-FA-TDC-921 b (Esc menutup dialog; Class Code tersimpan tetap `KHS-D13`) pada langkah 10 sampai 12. Urutan langkah mengikuti urutan state (8b.5).
- Langkah penghubung (S-03): langkah 1 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 13 (menutup Drawer yang bersih sesudah dimuat ulang), langkah 14 (membentuk precondition TC-FA-TDC-214), langkah 22 (mengosongkan Search).
- Langkah 20 (dialog D-13 tidak muncul): toast sukses langkah 19 adalah respons server yang sudah diasersi dan menjadi anchor positif (8b.2).
- Temuan untuk QA:
  - Email akun Total Control sesi A tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-D13` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-213 tidak menyebut nilai Class Code baru dan Class Name class; spec memakai `KHS-D13B` dan `Kelompok D13` seperti TC-FA-TDC-921.
  - TC-FA-TDC-213 Expected a "tidak ada yang tersimpan" tanpa cara pengamatan; spec mengamati nilai Class Code pada Drawer yang dimuat ulang (langkah 12).
  - TC-FA-TDC-921 Post Condition (tidak ada data berubah) dan TC-FA-TDC-214 tidak punya langkah observasi untuk entri log; tidak diasersi (S-01).
  - Kolom Automation TC-FA-TDC-213 dan TC-FA-TDC-214 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
