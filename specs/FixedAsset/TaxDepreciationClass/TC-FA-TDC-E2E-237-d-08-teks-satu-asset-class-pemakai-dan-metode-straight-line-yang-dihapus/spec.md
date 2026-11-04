---
id: TC-FA-TDC-E2E-237-d-08-teks-satu-asset-class-pemakai-dan-metode-straight-line-yang-dihapus
title: "Dialog D-08: Teks untuk Tepat Satu Asset Class Pemakai dan Penyebutan Straight Line sebagai Metode yang Dihapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-284
  - TC-FA-TDC-285
coverage:
  web: automated
---

# Dialog D-08: Teks untuk Tepat Satu Asset Class Pemakai dan Penyebutan Straight Line sebagai Metode yang Dihapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Non-building, Useful Life 8, Straight Line dan Declining Balance):

| TC | Class (Class Code bersuffix) | Keterangan |
|---|---|---|
| TC-284 | `KHS-V10-{runId}-237` | Used By 1: Asset Class `AC-DB3 – Compressor Workshop` memakai Declining Balance (disediakan tim FE/BE) |
| TC-285 | `KHS-V11-{runId}-237` | Used By 1: Asset Class `AC-SL2 – Mesin Bubut` memakai Straight Line (disediakan tim FE/BE) |

- Pencarian baris target memakai kata kunci `{runId}-237` yang menampilkan kedua class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-237`, tekan Enter

### TC-FA-TDC-284: Screening dialog D-08 untuk tepat satu Asset Class

2. Klik link Class Code `KHS-V10-{runId}-237` pada tabel
3. Lepas `Declining Balance` dari Allowed Methods
4. Klik `[Save]`
5. Verifikasi judul dialog adalah `Cannot Remove This Method`
6. Verifikasi teks `1 asset class uses Declining Balance. Change it first.`
7. Verifikasi satu bullet `• AC-DB3 – Compressor Workshop` tampil di bawah teks
8. Verifikasi footer memuat satu tombol `[OK]`
9. Verifikasi dialog Save Changes (Effective From) tidak tampil
10. Klik `[OK]` pada dialog D-08
11. Klik `[×]` pada Drawer Edit
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-FA-TDC-285: D-08 menyebut Straight Line bila metode yang dihapus adalah Straight Line

14. Klik link Class Code `KHS-V11-{runId}-237` pada tabel
15. Lepas `Straight Line` dari Allowed Methods
16. Klik `[Save]`
17. Verifikasi dialog D-08 dengan teks `1 asset class uses Straight Line. Change it first.`
18. Verifikasi bullet `• AC-SL2 – Mesin Bubut` tampil di bawah teks
19. Verifikasi dialog D-09 tidak muncul
20. Klik `[OK]` pada dialog D-08
21. Klik `[×]` pada Drawer Edit
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 10 sampai 13 dan 20 sampai 23 (menutup D-08 dan Drawer yang dirty lewat `[OK]`, `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08).
- Absence pada langkah 9 dan 19: anchor positif adalah dialog D-08 yang tampil (langkah 5 sampai 8 dan 17 sampai 18).
- TC-283, 286, 287 ada di spec 081; TC-288, 289, 290, 292 ada di spec 082.
- Temuan untuk QA:
  - TC-284 dan TC-285 tidak menyebut Fiscal Year Start dan tanggal sistem; tidak relevan untuk D-08 dan jam tidak diatur di spec ini.
  - TC-284 Expected d menyebut dialog "Save Changes (Effective From)" sedangkan TC-285 menyebut "dialog D-09"; keduanya dialog yang sama.
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-237` (S-12); batas panjang Class Code tidak tertulis di TC.
