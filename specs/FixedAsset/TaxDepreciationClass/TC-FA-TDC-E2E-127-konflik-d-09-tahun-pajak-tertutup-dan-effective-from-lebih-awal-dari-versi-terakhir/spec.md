---
id: TC-FA-TDC-E2E-127-konflik-d-09-tahun-pajak-tertutup-dan-effective-from-lebih-awal-dari-versi-terakhir
title: "Konflik D-09: Tahun Pajak yang Baru Ditutup dan Effective From Lebih Awal dari Versi Terakhir yang Baru Dibentuk"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-263
  - TC-FA-TDC-264
coverage:
  web: automated
---

# Konflik D-09: Tahun Pajak yang Baru Ditutup dan Effective From Lebih Awal dari Versi Terakhir yang Baru Dibentuk

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`) atau fixture BE untuk data Accounting Period. Sesi B hanya memicu perubahan state dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk periode Accounting Period Closed/Open dan versi Scheduled), sesi API aktor, kendali jam sistem, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah versi class lewat fixture BE (disediakan tim FE/BE).
- State global yang diubah: jam server dan jam browser diatur bersama ke `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00; Fiscal Year Start Januari) dan Accounting Period tahun pajak 2026 diubah menjadi Closed pada TC-FA-TDC-263; dipulihkan dengan langkah eksplisit (langkah 16 dan 29) dan di hook `after` sebagai cadangan.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsV1` | `KHS-V1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, hanya satu versi (Current tanpa Effective From), Active, Used By 0, tanpa versi Scheduled |
| `periode2026` | Accounting Period tahun pajak 2026 | seluruh 12 periode berstatus Open |

- `KHS-V1` dan periode 2026 dipulihkan ke keadaan awal (langkah 16) di antara dua blok.
- Suite berjalan serial (`parallel: false`) karena jam sistem, Accounting Period, dan Class Code seed bersifat global atau literal.

## Test Steps

### TC-FA-TDC-263: Memilih tahun pajak yang baru ditutup setelah dialog dibuka menampilkan caption V-21

1. Atur jam server dan jam browser ke `15 Okt 2026 10:00 WIB`
2. Ketik Search `KHS-V1`, tekan Enter
3. Klik link Class Code `KHS-V1`
4. Ganti Useful Life dari `8` menjadi `10`
5. Klik `[Save]` (dialog Save Changes D-09 terbuka)
6. Sesi B (fixture BE): ubah seluruh 12 periode tahun pajak 2026 menjadi Closed hingga tersimpan
7. Sesi A: pilih Effective From `Jan 2027` pada dialog D-09
8. Sesi A: pilih kembali Effective From `Jan 2026`
9. Verifikasi caption `Tax year 2026 is closed. Choose a later tax year.` muncul pada Effective From
10. Klik `[Apply]`
11. Verifikasi tidak ada versi baru: jumlah versi `KHS-V1` lewat fixture BE tetap 1
12. Tekan Esc untuk menutup dialog D-09
13. Klik ikon ✕ pada Drawer
14. Verifikasi dialog Unsaved Changes tampil
15. Klik `[Leave]`
16. Pulihkan seluruh periode tahun pajak 2026 ke Open dan class `KHS-V1` ke nilai awal lewat seeding API

### TC-FA-TDC-264: Memilih Effective From lebih awal dari versi terakhir yang baru dibentuk menampilkan caption V-22

17. Klik link Class Code `KHS-V1`
18. Ganti Useful Life dari `8` menjadi `10`
19. Klik `[Save]` (dialog Save Changes D-09 terbuka dengan opsi mulai `Jan 2026`)
20. Sesi B (sesi API): buat versi Scheduled Effective From `Jan 2028` pada `KHS-V1` hingga versi tersimpan
21. Sesi A: pilih Effective From `Jan 2027`
22. Verifikasi caption `Effective from must not be earlier than Jan 2028` muncul pada Effective From
23. Verifikasi tidak ada versi baru dari sesi A: jumlah versi `KHS-V1` lewat fixture BE tetap 2 (versi Current awal dan versi Scheduled `Jan 2028` dari sesi B)
24. Tekan Esc untuk menutup dialog D-09
25. Klik ikon ✕ pada Drawer
26. Verifikasi dialog Unsaved Changes tampil
27. Klik `[Leave]`
28. Klik `(←)` pada kotak Search
29. Pulihkan jam server dan jam browser ke waktu semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 dan 29 (mengatur dan memulihkan jam), langkah 2 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 12 dan 24 (menutup dialog D-09 dengan Esc), langkah 13 sampai 15 dan 25 sampai 27 (menutup Drawer dirty deterministik; S-08), langkah 16 (membentuk precondition TC-FA-TDC-264), langkah 28 (mengosongkan Search). Langkah 17 memakai Search langkah 2 yang masih aktif.
- Langkah 20 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ... tersimpan" (R-20). Langkah 6 memakai fixture BE karena perubahan Accounting Period tidak tersedia di UI modul ini (data uji TC).
- Langkah 10 (klik `[Apply]`) tidak ada di langkah TC; ditambahkan agar Expected b TC-FA-TDC-263 ("tombol `[Apply]` tidak menyimpan versi pada nilai itu") dapat diasersi lewat langkah 11 (S-03, S-15). Caption langkah 9 menjadi anchor positif bahwa dialog sudah memuat status tahun pajak terbaru (8b.2).
- Langkah 23 (Expected b TC-FA-TDC-264, tidak ada versi baru dari sesi A): jumlah versi dibaca lewat fixture BE, dengan caption langkah 22 sebagai anchor positif.
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-V1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-263 Expected b menyebut tombol `[Apply]` "tidak menyimpan versi pada nilai itu" tetapi langkah TC tidak mengklik `[Apply]`; spec menambah klik `[Apply]` (langkah 10). Apakah dialog tetap terbuka setelah klik tidak disebut TC; spec menutupnya dengan Esc (langkah 12).
  - TC-FA-TDC-263 dan TC-FA-TDC-264 Post Condition (tidak ada data tersimpan) tidak punya langkah observasi selain jumlah versi pada langkah 11 dan 23; tidak ada asersi log (S-01).
  - TC-FA-TDC-263 menyebut Select tidak menawarkan tahun tertutup (NC-18); caption muncul hanya karena pilihan `Jan 2026` sudah ada di dialog sebelum periode ditutup.
  - Kolom Automation TC-FA-TDC-263 dan TC-FA-TDC-264 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
