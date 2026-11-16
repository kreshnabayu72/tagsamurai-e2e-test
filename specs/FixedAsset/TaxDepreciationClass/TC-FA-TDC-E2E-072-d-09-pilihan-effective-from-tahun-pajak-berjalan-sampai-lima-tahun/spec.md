---
id: TC-FA-TDC-E2E-072-d-09-pilihan-effective-from-tahun-pajak-berjalan-sampai-lima-tahun
title: "Pilihan Effective From pada D-09: Tahun Pajak Berjalan sampai Lima Tahun Setelahnya dan Mulai dari Versi Terakhir Bertanggal"
layer: ui-e2e
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-256
  - TC-FA-TDC-257
sourceRules: ["FATDC-LOGIC-04af", "FATDC-LOGIC-04f.4", "FATDC-LOGIC-04t", "E-FATDC-77", "§4.2c#b1", "V-22"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04af": [6, 8, 19, 20]
  "FATDC-LOGIC-04f.4": 6
  "FATDC-LOGIC-04t": [7, 18]
  "E-FATDC-77": 8
  "§4.2c#b1": [12, 24]
  "V-22": 20
coverage:
  web: automated
---

# Pilihan Effective From pada D-09: Tahun Pajak Berjalan sampai Lima Tahun Setelahnya dan Mulai dari Versi Terakhir Bertanggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`. Tahun pajak berjalan 2026.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Non-building, Useful Life 8, Active, Used By 0):

| TC | Class (Class Code bersuffix) | Versi | Keterangan |
|---|---|---|---|
| TC-256 | `KHS-V1-{runId}-072` | satu versi Current tanpa Effective From, tanpa versi Scheduled | Straight Line dan Declining Balance |
| TC-257 | `KHS-V2-{runId}-072` | versi Current tanpa Effective From dan versi Scheduled Effective From Jan 2027 (Useful Life 10) | Straight Line dan Declining Balance |

- Pencarian baris target memakai kata kunci `{runId}-072` yang menampilkan kedua class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-072`, tekan Enter

### TC-FA-TDC-256: Pilihan Effective From tahun pajak berjalan sampai 5 tahun setelahnya (tanpa versi bertanggal)

2. Klik link Class Code `KHS-V1-{runId}-072` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Klik Select Effective From
6. Verifikasi daftar opsi berurutan: `Jan 2026`, `Jan 2027`, `Jan 2028`, `Jan 2029`, `Jan 2030`, `Jan 2031` (enam opsi)
7. Verifikasi nilai awal terpilih `Jan 2026`
8. Verifikasi tidak ada opsi sebelum `Jan 2026` maupun sesudah `Jan 2031`
9. Klik opsi `Jan 2026`
10. Klik `[Cancel]` pada dialog Save Changes
11. Klik `[×]` pada Drawer Edit
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-FA-TDC-257: Pilihan Effective From dimulai dari tahun pajak versi terakhir yang bertanggal

14. Klik link Class Code `KHS-V2-{runId}-072` pada tabel
15. Ganti Useful Life menjadi `12`
16. Klik `[Save]`
17. Klik Select Effective From
18. Verifikasi nilai awal terpilih `Jan 2027`
19. Verifikasi daftar opsi: `Jan 2027`, `Jan 2028`, `Jan 2029`, `Jan 2030`, `Jan 2031` (lima opsi)
20. Verifikasi opsi `Jan 2026` tidak ada
21. Klik opsi `Jan 2027`
22. Klik `[Cancel]` pada dialog Save Changes
23. Klik `[×]` pada Drawer Edit
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 9 dan 21 (memilih kembali opsi awal agar daftar opsi tertutup tanpa mengubah pilihan), langkah 10 sampai 13 dan 22 sampai 25 (menutup dialog dan Drawer yang dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08).
- Absence pada langkah 8 dan 20: anchor positif adalah daftar opsi yang tampil (langkah 6 dan 19).
- Pilihan Effective From dengan Fiscal Year Start April diuji di spec 238 (TC-258), karena membutuhkan Fiscal Year Start dan tanggal sistem berbeda.
- Temuan untuk QA:
  - TC-256 dan TC-257 tidak menyebut email akun Total Control maupun company uji; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-072` (S-12); batas panjang Class Code tidak tertulis di TC.
  - TC-256 dan TC-257 tidak menyebut bahwa daftar opsi ditutup sebelum dialog dibatalkan; spec menutupnya dengan memilih kembali opsi awal.
