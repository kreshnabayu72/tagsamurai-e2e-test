---
id: TC-FA-TDC-E2E-259-pratinjau-angka-penyusutan-fiskal-dan-nilai-sisa-buku-d-09-menunggu-mesin-kalkulasi
title: "Pratinjau Dampak D-09 Menampilkan Angka Penyusutan Fiskal dan Nilai Sisa Buku Sebelum → Sesudah (Menunggu Mesin Kalkulasi, OI-03 b)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-253
coverage:
  web: unsupported
---

# Pratinjau Dampak D-09 Menampilkan Angka Penyusutan Fiskal dan Nilai Sisa Buku Sebelum → Sesudah (Menunggu Mesin Kalkulasi, OI-03 b)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Kemampuan teknis: mesin kalkulasi penyusutan fiskal tersedia dan Asset Class pemakai memiliki aset aktif dengan nilai perolehan terisi (Precondition e TC). Kemampuan ini disediakan tim FE/BE dan saat ini belum ada (OI-03 b); selama belum tersedia, spec tidak dapat dijalankan sehingga `coverage.web` bernilai `unsupported`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`):

| Class (Class Code bersuffix) | Used By | Keterangan |
|---|---|---|
| `KHS-V9-{runId}-259` | 3 | Non-building, Useful Life 8, Straight Line dan Declining Balance, Active, hanya satu versi Current tanpa Effective From; Asset Class pemakai `AC-DB1`, `AC-DB2`, `AC-SL1` dengan total 18 aset aktif bernilai perolehan terisi (disediakan tim FE/BE) |

- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-253: Pratinjau angka penyusutan fiskal dan nilai sisa buku [DEFERRED]

1. Ketik Search `{runId}-259`, tekan Enter
2. Klik link Class Code `KHS-V9-{runId}-259` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Verifikasi judul dialog adalah `Save Changes`
6. Pilih Effective From `Jan 2027`
7. Verifikasi baris `Fiscal depreciation, tax year 2027` menampilkan nilai sebelum → sesudah dalam mata uang dasar client
8. Verifikasi nilai pada baris `Fiscal depreciation, tax year 2027` dihitung mesin kalkulasi
9. Verifikasi baris `Fiscal book value at year end` menampilkan nilai sebelum → sesudah dalam mata uang dasar client
10. Verifikasi label tahun pada baris pertama berubah dari 2026 ke 2027 mengikuti Effective From
11. Klik `[Cancel]` pada dialog Save Changes
12. Klik `[×]` pada Drawer Edit
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`

## Notes

- TC-FA-TDC-253 berlabel [DEFERRED] (OI-03 b: angka penyusutan fiskal dan nilai sisa buku belum didefinisikan karena mesin kalkulasi belum ada). Spec memakai `coverage.web: unsupported` sampai OI-03 diputuskan.
- Saat OI-03 diputuskan: ganti `coverage.web` menjadi `automated`; ganti langkah 7 dan 9 dengan nilai pasti hasil mesin (sebelum dan sesudah) dan langkah 8 dengan asersi nilai itu bila TC memuatnya; isi kondisi mesin kalkulasi pada Prerequisites dari kemampuan fixture BE yang tersedia.
- Langkah 8 merekam klausa "dihitung mesin kalkulasi" pada Expected a TC; tidak ada cara mengamatinya di UI selain nilai, sehingga asersinya mengikuti nilai pada langkah 7 setelah mesin tersedia.
- Langkah penghubung (S-03): langkah 11 sampai 14 (menutup dialog Save Changes dan Drawer yang dirty lewat `[Cancel]`, `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08); langkah 1 (Search untuk menemukan baris target; R-16).
- Dialog D-09 tampil pada langkah 5 (anchor positif sebelum pilihan Effective From pada langkah 6).
- Temuan untuk QA:
  - TC-FA-TDC-253: Expected menyatakan "nilai pasti ditetapkan setelah mesin tersedia"; spec hanya mengasersi bentuk nilai (sebelum → sesudah, mata uang dasar client), bukan angka.
  - TC-FA-TDC-253 tidak menyebut email akun Total Control, company uji, maupun data Asset Class pemakai (`AC-DB1`, `AC-DB2`, `AC-SL1`, 18 aset aktif, nilai perolehan); disediakan tim FE/BE.
  - Kode class milik spec bersuffix `{runId}-259` (S-12); batas panjang Class Code tidak tertulis di TC, sehingga muat tidaknya Class Code bersuffix perlu dikonfirmasi.
  - Post Condition "Tidak ada data tersimpan" tidak punya langkah observasi di TC dan tidak diasersi (S-01).
