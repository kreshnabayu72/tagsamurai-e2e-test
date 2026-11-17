---
id: TC-FA-TDC-E2E-070-d-09-screening-dialog-save-changes-dan-pratinjau-dampak
title: "Screening Dialog Save Changes D-09 dan Pratinjau Dampak Jumlah Asset Class dan Aset Aktif"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-248
  - TC-FA-TDC-249
  - TC-FA-TDC-250
sourceRules: ["D-09", "FLD-15", "FATDC-LOGIC-04t", "FATDC-LOGIC-05e", "§4.2c#b1", "FATDC-LOGIC-05a", "FATDC-LOGIC-05b.1", "FATDC-LOGIC-05b.2", "FATDC-LOGIC-05b.3", "FATDC-LOGIC-05b.4", "§Aturan Logika Modul#p14"]
smoke: []
dependsOn: []
trace:
  "D-09": [5, 9, 17, 21]
  "FLD-15": [5, 6, 17, 18]
  "FATDC-LOGIC-04t": [7, 19]
  "FATDC-LOGIC-05e": 8
  "§4.2c#b1": [12, 26]
  "FATDC-LOGIC-05a": 20
  "FATDC-LOGIC-05b.1": [20, 22]
  "FATDC-LOGIC-05b.2": [20, 23]
  "FATDC-LOGIC-05b.3": 20
  "FATDC-LOGIC-05b.4": 20
  "§Aturan Logika Modul#p14": [22, 23]
coverage:
  web: automated
---

# Screening Dialog Save Changes D-09 dan Pratinjau Dampak Jumlah Asset Class dan Aset Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; semua Non-building, Useful Life 8, Straight Line dan Declining Balance, Active, satu versi Current tanpa Effective From, tanpa versi Scheduled):

| TC | Class (Class Code bersuffix) | Used By | Keterangan |
|---|---|---|---|
| TC-248 | `KHS-V1-{runId}-070` | 0 | tanpa Asset Class pemakai |
| TC-249, 250 | `KHS-V9-{runId}-070` | 3 | Asset Class pemakai `AC-DB1`, `AC-DB2`, `AC-SL1` dengan total 18 aset aktif (disediakan tim FE/BE) |

- Pencarian baris target memakai kata kunci `{runId}-070` yang menampilkan kedua class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-248: Screening D-09 untuk class dengan Used By 0

1. Ketik Search `{runId}-070`, tekan Enter
2. Klik link Class Code `KHS-V1-{runId}-070` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Verifikasi judul dialog adalah `Save Changes`
6. Verifikasi label `Effective From *` tampil di atas kontrol Select tahun pajak
7. Verifikasi Select tahun pajak terisi nilai awal `Jan 2026`
8. Verifikasi blok pratinjau dampak tidak tampil
9. Verifikasi footer memuat tombol `[Cancel]` dan `[Apply]`
10. Klik `[Cancel]` pada dialog Save Changes
11. Klik `[×]` pada Drawer Edit
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-FA-TDC-249: Screening D-09 untuk class dengan Used By lebih dari 0

14. Klik link Class Code `KHS-V9-{runId}-070` pada tabel
15. Ganti Useful Life menjadi `10`
16. Klik `[Save]`
17. Verifikasi judul dialog adalah `Save Changes`
18. Verifikasi label `Effective From *` tampil di atas Select tahun pajak
19. Verifikasi Select tahun pajak terisi nilai awal `Jan 2026`
20. Verifikasi blok pratinjau dampak read-only tampil dengan empat baris berlabel `Asset classes affected`, `Active assets affected`, `Fiscal depreciation, tax year 2026`, `Fiscal book value at year end`
21. Verifikasi footer memuat tombol `[Cancel]` dan `[Apply]`

### TC-FA-TDC-250: Pratinjau jumlah Asset Class dan aset aktif terdampak

22. Verifikasi baris `Asset classes affected` bernilai `3`
23. Verifikasi baris `Active assets affected` bernilai `18`

24. Klik `[Cancel]` pada dialog Save Changes
25. Klik `[×]` pada Drawer Edit
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 10 sampai 13 dan 24 sampai 27 (menutup dialog Save Changes dan Drawer yang dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08), langkah 1 (Search untuk menemukan baris target; R-16).
- TC-250 melanjutkan dialog Save Changes class `KHS-V9-{runId}-070` yang sudah terbuka pada TC-249; langkah 1 sampai 3 TC-250 identik dengan keadaan yang sudah terbentuk (class sama, Useful Life `10`, `[Save]` diklik).
- Absence pada langkah 8: anchor positif adalah langkah 5 sampai 7 (dialog dan Select tampil).
- Temuan untuk QA:
  - TC-248 sampai 250 tidak menyebut email akun Total Control, company uji, maupun data Asset Class pemakai (`AC-DB1`, `AC-DB2`, `AC-SL1`, 18 aset aktif); disediakan tim FE/BE.
  - TC-249 menyebut empat baris berlabel pada pratinjau tetapi tidak menyebut nilai default tiap baris; hanya TC-250 yang menyebut nilai `3` dan `18`.
  - Kode class milik spec bersuffix `{runId}-070` (S-12); batas panjang Class Code tidak tertulis di TC, sehingga muat tidaknya Class Code bersuffix perlu dikonfirmasi.
  - Post Condition "Tidak ada data tersimpan" (TC-248, 249) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
