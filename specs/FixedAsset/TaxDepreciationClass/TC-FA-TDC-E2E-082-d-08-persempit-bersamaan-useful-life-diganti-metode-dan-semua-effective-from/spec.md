---
id: TC-FA-TDC-E2E-082-d-08-persempit-bersamaan-useful-life-diganti-metode-dan-semua-effective-from
title: "Guard Persempit D-08: Bersamaan dengan Useful Life Diubah, Mengganti Metode, Metode Tidak Dipakai Tidak Diblokir, dan Berlaku untuk Semua Effective From"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-288
  - TC-FA-TDC-289
  - TC-FA-TDC-290
  - TC-FA-TDC-292
sourceRules: ["D-08", "E-FATDC-17", "F-FATDC-02.k6c", "§4.2c#b1", "D-09", "FI-04"]
smoke: []
dependsOn: []
trace:
  "D-08": [6, 10, 20, 21, 31]
  "E-FATDC-17": [7, 11]
  "F-FATDC-02.k6c": [8, 9, 22]
  "§4.2c#b1": [14, 25, 34]
  "D-09": 30
  "FI-04": 30
coverage:
  web: automated
---

# Guard Persempit D-08: Bersamaan dengan Useful Life Diubah, Mengganti Metode, Metode Tidak Dipakai Tidak Diblokir, dan Berlaku untuk Semua Effective From

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Kemampuan teknis: pembacaan versi dan nilai class lewat fixture BE (untuk asersi "tidak ada versi baru" dan "tidak ada data tersimpan"; disediakan tim FE/BE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; semua Non-building, Useful Life 8, Active, satu versi):

| TC | Class (Class Code bersuffix) | Allowed Methods | Used By |
|---|---|---|---|
| TC-288, 292 | `KHS-V8-{runId}-082` | Straight Line dan Declining Balance | 2: Asset Class `AC-DB1 – Pompa Air Gudang` dan `AC-DB2 – Genset Pabrik` keduanya memakai Declining Balance |
| TC-289 | `KHS-V12-{runId}-082` | Declining Balance saja | 1: Asset Class `AC-DB4 – Traktor Kebun` memakai Declining Balance |
| TC-290 | `KHS-V13-{runId}-082` | Straight Line dan Declining Balance | 2: kedua Asset Class memakai Straight Line |

  Asset Class pemakai disediakan tim FE/BE.
- Pencarian baris target memakai kata kunci `{runId}-082` yang menampilkan ketiga class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-082`, tekan Enter

### TC-FA-TDC-288 dan TC-FA-TDC-292: Mempersempit bersamaan dengan Useful Life diubah tetap diblokir D-08; guard dievaluasi saat Save

2. Klik link Class Code `KHS-V8-{runId}-082` pada tabel
3. Ganti Useful Life menjadi `10`
4. Lepas `Declining Balance` dari Allowed Methods
5. Klik `[Save]`
6. Verifikasi dialog D-08 muncul
7. Verifikasi dialog D-09 tidak muncul
8. Verifikasi tidak ada versi baru pada class `KHS-V8-{runId}-082` (dibaca lewat fixture BE)
9. Verifikasi tidak ada data tersimpan pada class `KHS-V8-{runId}-082`: Useful Life dan Allowed Methods tetap nilai awal (dibaca lewat fixture BE)
10. Verifikasi dialog D-08 muncul sebelum pilihan Effective From apa pun tersedia
11. Verifikasi dialog D-09 tidak ditampilkan sehingga versi Scheduled masa depan tidak dapat dibentuk
12. Klik `[OK]` pada dialog D-08
13. Klik `[×]` pada Drawer Edit
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`

### TC-FA-TDC-289: Mengganti Allowed Methods dari Declining Balance saja ke Straight Line saja diblokir bila Declining Balance dipakai

16. Klik link Class Code `KHS-V12-{runId}-082` pada tabel
17. Lepas `Declining Balance` dari Allowed Methods
18. Pilih `Straight Line` pada Allowed Methods
19. Klik `[Save]`
20. Verifikasi dialog D-08 dengan teks `1 asset class uses Declining Balance. Change it first.`
21. Verifikasi bullet `• AC-DB4 – Traktor Kebun` tampil di bawah teks
22. Verifikasi tidak ada data tersimpan pada class `KHS-V12-{runId}-082`: Allowed Methods tetap `Declining Balance` saja (dibaca lewat fixture BE)
23. Klik `[OK]` pada dialog D-08
24. Klik `[×]` pada Drawer Edit
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`

### TC-FA-TDC-290: Mempersempit metode yang tidak dipakai Asset Class mana pun tidak diblokir

27. Klik link Class Code `KHS-V13-{runId}-082` pada tabel
28. Lepas `Declining Balance` dari Allowed Methods
29. Klik `[Save]`
30. Verifikasi dialog D-09 muncul dengan blok pratinjau dampak (Used By lebih dari 0)
31. Verifikasi dialog D-08 tidak muncul
32. Klik `[Cancel]` pada dialog Save Changes
33. Klik `[×]` pada Drawer Edit
34. Verifikasi dialog `Unsaved Changes` tampil
35. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 12 sampai 15, 23 sampai 26, dan 32 sampai 35 (menutup dialog dan Drawer yang dirty lewat `[OK]` atau `[Cancel]`, `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08).
- TC-292 (Expected: D-08 muncul sebelum pilihan Effective From apa pun, D-09 tidak ditampilkan) memakai keadaan yang sama dengan TC-288 (class `KHS-V8`, `Declining Balance` dilepas, `[Save]` diklik); Useful Life `10` pada form tidak memengaruhi guard. Langkah 10 dan 11 mengamati keadaan itu dan langkah 2 sampai 5 tidak diulang untuk TC-292.
- Absence pada langkah 7: anchor positif adalah dialog D-08 yang tampil (langkah 6). Absence pada langkah 31: anchor positif adalah dialog D-09 yang tampil (langkah 30).
- TC-283, 286, 287 ada di spec 081; TC-284 dan TC-285 ada di spec 237.
- Temuan untuk QA:
  - TC-288, 289, 290 tidak menyebut tanggal sistem uji; tidak relevan untuk D-08 dan jam tetap dari state global spec ini.
  - TC-292 Data Uji yang memuat tanggal Effective From `Jan 2031` (tidak sempat dipilih) tidak punya padanan langkah; spec tidak memilih Effective From karena dialog Save Changes tidak tampil.
  - TC-288 dan TC-289 Expected "tidak ada data tersimpan" dan "tidak ada versi baru" tidak punya langkah observasi di TC; diasersi lewat fixture BE karena ada di Expected.
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-082` (S-12); batas panjang Class Code tidak tertulis di TC.
