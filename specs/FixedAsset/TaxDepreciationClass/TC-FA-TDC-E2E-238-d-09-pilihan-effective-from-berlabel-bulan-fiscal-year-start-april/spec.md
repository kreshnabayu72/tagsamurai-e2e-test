---
id: TC-FA-TDC-E2E-238-d-09-pilihan-effective-from-berlabel-bulan-fiscal-year-start-april
title: "Pilihan Effective From pada D-09 Berlabel Bulan Fiscal Year Start Non-Januari (April)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-258
coverage:
  web: automated
---

# Pilihan Effective From pada D-09 Berlabel Bulan Fiscal Year Start Non-Januari (April)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global (diubah spec ini, dipulihkan di hook `after`): Fiscal Year Start diatur ke April (Settings > Accounting > Preferences, disediakan lewat API oleh tim FE/BE) dan jam sistem uji diatur ke `15 Feb 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta; jam server dan browser bersama) di hook `before`. Tahun pajak berjalan dimulai April 2025. Hook `after` memulihkan Fiscal Year Start ke Januari dan jam ke nilai semula.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`):

| TC | Class (Class Code bersuffix) | Keterangan |
|---|---|---|
| TC-258 | `KHS-V1-{runId}-238` | Non-building, Useful Life 8, Straight Line dan Declining Balance, Active, Used By 0, satu versi Current tanpa Effective From, tanpa versi Scheduled |

- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-258: Pilihan Effective From berlabel bulan Fiscal Year Start April

1. Ketik Search `KHS-V1-{runId}-238`, tekan Enter
2. Klik link Class Code `KHS-V1-{runId}-238` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Klik Select Effective From
6. Verifikasi tahun pajak berjalan dimulai `Apr 2025` dan nilai awal terpilih adalah `Apr 2025`
7. Verifikasi daftar opsi: `Apr 2025`, `Apr 2026`, `Apr 2027`, `Apr 2028`, `Apr 2029`, `Apr 2030` (enam opsi)
8. Verifikasi label pada baris pratinjau tahun pajak mengikuti tahun kalender awal tahun pajak (opsi `Apr 2025` menjadi tahun 2025)
9. Klik opsi `Apr 2025`
10. Klik `[Cancel]` pada dialog Save Changes
11. Klik `[×]` pada Drawer Edit
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 9 (memilih kembali opsi awal agar daftar opsi tertutup tanpa mengubah pilihan), langkah 10 sampai 13 (menutup dialog dan Drawer yang dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08).
- TC-258 ada di spec ini; pilihan Effective From dengan Fiscal Year Start Januari ada di spec 072 (TC-256 dan TC-257).
- Temuan untuk QA:
  - TC-258 Expected c menyebut "label pada baris pratinjau tahun pajak", tetapi Precondition d menetapkan class `KHS-V1` dengan Used By 0, sedangkan TC-248 menyatakan blok pratinjau dampak tidak tampil untuk Used By 0. Langkah 8 mengikuti Expected TC dan tidak dapat dipenuhi pada data Precondition TC; QA perlu menetapkan class ber-Used By lebih dari 0 atau menghapus klausa itu.
  - TC-258 tidak menyebut cara mengubah Fiscal Year Start dan tanggal sistem; disediakan tim FE/BE (S-13).
  - TC-258 tidak menyebut email akun Total Control maupun company uji; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-238` (S-12); batas panjang Class Code tidak tertulis di TC.
