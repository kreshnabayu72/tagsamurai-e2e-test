---
id: TC-FA-TDC-E2E-094-hari-ini-menurut-time-zone-entitas-bukan-utc-dan-versi-pertama
title: "Hari Ini Menurut Time Zone Entitas Menentukan Versi Current atau Scheduled dan Versi Pertama Tidak Mengunci Fiscal Year Start"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-350
  - TC-FA-TDC-351
  - TC-FA-TDC-352
sourceRules: ["§11.2#r6", "E-FATDC-20", "FLD-01", "§4.1.2#r1", "ST-30", "§9.5#r10", "FATDC-LOGIC-04w"]
smoke: []
dependsOn: []
trace:
  "§11.2#r6": [4, 5]
  "E-FATDC-20": [14, 26]
  "FLD-01": 16
  "§4.1.2#r1": 16
  "ST-30": 17
  "§9.5#r10": 22
  "FATDC-LOGIC-04w": [22, 26]
coverage:
  web: automated
---

# Hari Ini Menurut Time Zone Entitas Menentukan Versi Current atau Scheduled dan Versi Pertama Tidak Mengunci Fiscal Year Start

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Time Zone entitas Asia/Jakarta (UTC+07:00); Fiscal Year Start Januari (awal spec, dipulihkan di hook `after`).
- Kendali jam sistem (`suite.md`): jam server dan jam browser diatur bersama pada waktu absolut: langkah 1 pada `15 Okt 2026 10:00 WIB`, langkah 8 pada `1 Jan 2027 09:00 WIB` (1 Jan 2027 02:00 UTC), langkah 19 pada `31 Des 2026 18:00 UTC` (1 Jan 2027 01:00 WIB); jam dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Active, Used By 0, satu versi Current tanpa Effective From, Useful Life 8): `KHS-P1-{runId}-094` (TC-350) dan `KHS-P2-{runId}-094` (TC-351). Company hanya memiliki class dengan versi pertama tanpa Effective From (tujuh class seed bawaan dan kedua class itu) saat TC-352 dijalankan (precondition d TC-352). Baris `KHS-*` berada di halaman pertama sehingga dibuka tanpa Search.
- Kemampuan teknis: mengubah Fiscal Year Start di Settings > Accounting > Preferences (modul tetangga; UI dan label sesuai TC); seeding class lewat API.
- State global yang diubah: jam server dan browser, Fiscal Year Start (dikembalikan ke Januari pada langkah 6, sebelum versi ber-Effective From terbentuk, karena Fiscal Year Start terkunci setelah ada versi ber-Effective From), serta versi ber-Effective From milik class spec (dihapus lewat seeding API di hook `after`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-352: Versi pertama tanpa Effective From tidak mengunci Fiscal Year Start

1. Atur jam server dan jam browser ke 15 Okt 2026 03:00 UTC (15 Okt 2026 10:00 WIB)
2. Klik tab `Preferences` pada tab bar Accounting
3. Ubah Fiscal Year Start menjadi April, klik `[Save changes]`
4. Verifikasi Fiscal Year Start berisi April
5. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tidak tampil
6. Ubah Fiscal Year Start kembali menjadi Januari, klik `[Save changes]`
7. Klik tab `Tax Depreciation Class` pada tab bar Accounting

### TC-FA-TDC-350: Apply dengan Effective From sama dengan hari ini langsung Current

8. Atur jam server dan jam browser ke 1 Jan 2027 02:00 UTC (1 Jan 2027 09:00 WIB)
9. Klik link Class Code `KHS-P1-{runId}-094` pada tabel
10. Ganti Useful Life menjadi `10`, klik `[Save]`
11. Pilih Effective From "Jan 2027" lalu klik `[Apply]`
12. Tunggu aksi selesai
13. Muat ulang halaman; baca baris `KHS-P1-{runId}-094`
14. Verifikasi baris `KHS-P1-{runId}-094`: Useful Life (years) "10", Effective From "Jan 2027" (versi langsung Current)
15. Klik link Class Code `KHS-P1-{runId}-094` pada tabel
16. Verifikasi field Regulation Reference tampil pada Drawer Edit
17. Verifikasi Alert versi Scheduled tidak tampil
18. Klik `[×]` pada header Drawer

### TC-FA-TDC-351: Hari ini menurut Time Zone entitas, bukan UTC

19. Atur jam server dan jam browser ke 31 Des 2026 18:00 UTC (1 Jan 2027 01:00 WIB)
20. Klik link Class Code `KHS-P2-{runId}-094` pada tabel
21. Ganti Useful Life menjadi `10`, klik `[Save]`
22. Verifikasi nilai awal Select Effective From pada dialog D-09: "Jan 2027" (tahun pajak berjalan menurut Time Zone entitas dimulai Jan 2027)
23. Pilih Effective From "Jan 2027" lalu klik `[Apply]`
24. Tunggu aksi selesai
25. Muat ulang halaman; baca baris `KHS-P2-{runId}-094`
26. Verifikasi baris `KHS-P2-{runId}-094`: Useful Life (years) "10", Effective From "Jan 2027" (Current, bukan Scheduled)

## Notes

- Urutan TC-352, 350, 351 (TC-352 pertama): TC-352 mensyaratkan company hanya memiliki versi pertama tanpa Effective From, dan Fiscal Year Start tidak dapat diubah lagi setelah TC-350 dan TC-351 membentuk versi ber-Effective From. Fiscal Year Start dikembalikan ke Januari pada langkah 6 agar TC-350 dan TC-351 berjalan pada Fiscal Year Start Januari.
- Langkah penghubung (S-03): langkah 1, 8, dan 19 (mengatur jam absolut), langkah 2 dan 7 (pindah tab), langkah 6 (memulihkan Fiscal Year Start), langkah 12 dan 24 ("Tunggu aksi selesai", 8b.8; hasil Apply tidak diasersi TC langsung), langkah 13 dan 25 (muat ulang dan baca baris), dan langkah 18 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Langkah 16 adalah anchor positif untuk absence Alert pada langkah 17 (8b.2).
- Langkah 22 menjalankan klausa "nilai awal Effective From 'Jan 2027'" pada Expected TC-351 butir a sebagai nilai awal pilihan pada dialog D-09 (TC tidak menyebut tempat mengamatinya).
- Post Condition TC-352 ("Fiscal Year Start tersimpan April") tidak punya langkah observasi di TC; langkah 4 mengasersi nilai field setelah `[Save changes]` sebagai makna "perubahan diterima" pada Expected TC-352.
- Temuan untuk QA:
  - TC-352 Expected "Perubahan Fiscal Year Start diterima" tanpa indikator yang teramati (toast atau state); spec memakai nilai field April dan absennya caption.
  - TC-350 dan TC-351 tidak menyebut tempat mengamati "tahun pajak berjalan" selain Expected; TC-351 Expected a tidak punya langkah.
  - TC-352 dan TC-350/351 saling bergantung pada Fiscal Year Start dan versi ber-Effective From; urutan di spec mengikuti kebutuhan itu.
  - Class Code `KHS-P1` dan `KHS-P2` tanpa suffix di TC; spec memakai `-{runId}-094` (S-12).
  - Email akun Total Control tidak tertulis di TC.
