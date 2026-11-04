---
id: TC-FA-TDC-E2E-128-konflik-cancel-version-versi-berubah-atau-class-dihapus
title: "Konflik Cancel Version: Versi Sudah Dibatalkan Sesi Lain atau Class Dihapus Sesi Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-306
  - TC-FA-TDC-311
coverage:
  web: automated
---

# Konflik Cancel Version: Versi Sudah Dibatalkan Sesi Lain atau Class Dihapus Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu perubahan state (batalkan versi, hapus class) dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk versi Scheduled), sesi API aktor, kendali jam sistem, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- State global yang diubah: jam server dan jam browser diatur bersama ke `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00; Fiscal Year Start Januari); dipulihkan dengan langkah eksplisit (langkah 20) dan di hook `after` sebagai cadangan.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsC1` | `KHS-C1` | Class Name `Kelompok cancel uji`; versi Current tanpa Effective From (Useful Life `8`, Straight Line dan Declining Balance) dan satu versi Scheduled Effective From `Jan 2027` (Useful Life `10`, Straight Line dan Declining Balance), Used By 0 |

- `KHS-C1` diseed ulang lewat API di antara dua blok (langkah 11) karena TC-FA-TDC-306 membatalkan versi Scheduled dan TC-FA-TDC-311 menghapus class.
- Suite berjalan serial (`parallel: false`) karena jam sistem global dan Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-306: Cancel pada versi yang sudah tidak Scheduled saat Confirm

1. Atur jam server dan jam browser ke `15 Okt 2026 10:00 WIB`
2. Ketik Search `KHS-C1`, tekan Enter
3. Klik link Class Code `KHS-C1`
4. Klik `[Cancel scheduled version]` (dialog D-10 terbuka)
5. Sesi B (sesi API): batalkan versi Scheduled `Jan 2027` pada `KHS-C1` hingga pembatalan tersimpan
6. Sesi A: klik `[Cancel version]`
7. Verifikasi muncul toast error: `Error, failed to cancel scheduled version.`
8. Verifikasi dialog D-10 tertutup
9. Verifikasi Drawer sesi A disegarkan: Alert versi Scheduled hilang
10. Klik ikon ✕ pada Drawer

### TC-FA-TDC-311: Cancel version pada class yang sudah dihapus admin lain

11. Pulihkan class `KHS-C1` lewat seeding API ke nilai awal (versi Current dan versi Scheduled `Jan 2027`)
12. Klik link Class Code `KHS-C1`
13. Klik `[Cancel scheduled version]` (dialog D-10 terbuka)
14. Sesi B (sesi API): hapus class `KHS-C1` hingga class terhapus di server
15. Sesi A: klik `[Cancel version]`
16. Verifikasi muncul toast info: `This tax depreciation class is no longer available.`
17. Verifikasi Drawer tertutup
18. Verifikasi tabel disegarkan dan tidak memuat baris `KHS-C1`
19. Klik `(←)` pada kotak Search
20. Pulihkan jam server dan jam browser ke waktu semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 dan 20 (mengatur dan memulihkan jam), langkah 2 (Search agar baris target ada di halaman teramati; R-16, 8b.13; langkah 12 memakai Search yang masih aktif), langkah 10 (menutup Drawer yang bersih), langkah 11 (membentuk precondition TC-FA-TDC-311), langkah 19 (mengosongkan Search).
- Langkah 5 dan 14 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20).
- Langkah 9 (absence, Alert versi Scheduled hilang): toast error langkah 7 adalah respons server yang sudah diasersi dan menjadi anchor positif (8b.2). Langkah 18 (baris hilang): toast info langkah 16 menjadi anchor.
- Langkah 8 dan 17 mengasersi penutupan dialog dan Drawer setelah toast; penutupan terjadi sebelum atau bersamaan dengan toast sehingga urutan Verifikasi mengikuti urutan Expected TC (8b.5).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-C1` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-306 Post Condition (tidak ada mutasi tambahan; hanya satu entri L-09 dari sesi B) dan TC-FA-TDC-311 Post Condition (tidak ada entri log) tidak punya langkah observasi di TC; tidak diasersi (S-01, S-05).
  - Kolom Automation TC-FA-TDC-306 dan TC-FA-TDC-311 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
