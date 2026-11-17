---
id: TC-FA-TDC-E2E-245-konflik-d-09-d-08-apply-class-dihapus-dan-asset-class-berubah-antara-save-dan-apply
title: "Konflik D-09 dan D-08: Apply pada Class yang Dihapus dan Asset Class Berubah Antara Save dan Apply"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-282
  - TC-FA-TDC-291
sourceRules: ["T-13", "F-FATDC-02.k12b", "D-08", "FATDC-LOGIC-10b.3", "F-FATDC-02.k6c", "§8.4#r7", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "T-13": [9, 12]
  "F-FATDC-02.k12b": [10, 11]
  "D-08": [21, 22]
  "FATDC-LOGIC-10b.3": 21
  "F-FATDC-02.k6c": 23
  "§8.4#r7": 24
  "§4.2c#b1": 27
coverage:
  web: automated
---

# Konflik D-09 dan D-08: Apply pada Class yang Dihapus dan Asset Class Berubah Antara Save dan Apply

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu perubahan state (hapus class, ubah Tax Method Asset Class di modul Asset Class) dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk Used By lewat Asset Class pemakai), sesi API aktor, kendali jam sistem, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah versi dan jumlah entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- State global yang diubah: jam server dan jam browser diatur bersama ke `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00; Fiscal Year Start Januari); dipulihkan dengan langkah eksplisit (langkah 30) dan di hook `after` sebagai cadangan. Tax Method Asset Class `AC-SL3` dikembalikan ke Straight Line di hook `after`.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsV1` | `KHS-V1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, hanya satu versi (Current tanpa Effective From), Active, Used By 0, tanpa versi Scheduled |
| `khsV14` | `KHS-V14` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Used By 1 (Asset Class `AC-SL3 – Kendaraan Operasional` memakai Straight Line) |

- Suite berjalan serial (`parallel: false`) karena jam sistem global dan Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-282: Apply pada class yang sudah dihapus admin lain

1. Atur jam server dan jam browser ke `15 Okt 2026 10:00 WIB`
2. Ketik Search `KHS-V1`, tekan Enter
3. Klik link Class Code `KHS-V1`
4. Ganti Useful Life dari `8` menjadi `10`
5. Klik `[Save]` (dialog Save Changes D-09 terbuka)
6. Sesi B (sesi API): hapus class `KHS-V1` hingga class terhapus di server
7. Sesi A: pilih Effective From `Jan 2027` pada dialog D-09
8. Sesi A: klik `[Apply]`
9. Verifikasi muncul toast info: `This tax depreciation class is no longer available.`
10. Verifikasi Drawer tertutup
11. Verifikasi dialog D-09 tertutup
12. Verifikasi tabel disegarkan dan tidak memuat baris `KHS-V1`

### TC-FA-TDC-291: Asset Class berubah antara Save dan Apply, server menolak dengan D-08 yang sama

13. Ganti isi kotak search dengan `KHS-V14`, tekan Enter
14. Klik link Class Code `KHS-V14`
15. Lepas centang Allowed Methods `Declining Balance`
16. Klik `[Save]` (dialog Save Changes D-09 terbuka)
17. Sesi B (sesi API, modul Asset Class): ubah Tax Method `AC-SL3` menjadi Declining Balance hingga perubahan tersimpan
18. Catat baseline jumlah versi dan jumlah entri Changelog class `KHS-V14` lewat fixture BE
19. Sesi A: pilih Effective From `Jan 2027` pada dialog D-09
20. Sesi A: klik `[Apply]`
21. Verifikasi dialog D-08 muncul dengan teks `1 asset class uses Declining Balance. Change it first.`
22. Verifikasi dialog D-08 memuat bullet `• AC-SL3 – Kendaraan Operasional`
23. Verifikasi tidak ada versi baru: jumlah versi `KHS-V14` sama dengan baseline langkah 18
24. Verifikasi tidak ada entri log baru: jumlah entri Changelog class `KHS-V14` sama dengan baseline langkah 18
25. Klik `[OK]` pada dialog D-08
26. Klik ikon ✕ pada Drawer
27. Verifikasi dialog Unsaved Changes tampil
28. Klik `[Leave]`
29. Klik `(←)` pada kotak Search
30. Pulihkan jam server dan jam browser ke waktu semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 dan 30 (mengatur dan memulihkan jam), langkah 2 dan 13 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 18 (baseline, S-12), langkah 25 (menutup dialog D-08 dengan `[OK]`; Drawer tetap terbuka), langkah 26 sampai 28 (menutup Drawer dirty deterministik; S-08), langkah 29 (mengosongkan Search).
- Langkah 6 dan 17 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20).
- Langkah 12 (absence): toast info langkah 9 adalah respons server yang sudah diasersi dan menjadi anchor positif untuk hilangnya baris (8b.2).
- Langkah 23 dan 24 (absence): dialog D-08 langkah 21 adalah respons server yang sudah diasersi dan menjadi anchor positif; selisih terhadap baseline langkah 18 (S-12, S-05; dua-sesi diuji di spec ini, P-1).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-V1` dan `KHS-V14` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-282 Post Condition (tidak ada entri log) tidak punya langkah observasi di TC; tidak diasersi (S-01, S-05).
  - TC-FA-TDC-291 tidak menyebut tombol penutup dialog D-08; spec memakai `[OK]` seperti dialog D-08 pada TC lain.
  - Kolom Automation TC-FA-TDC-282 dan TC-FA-TDC-291 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
