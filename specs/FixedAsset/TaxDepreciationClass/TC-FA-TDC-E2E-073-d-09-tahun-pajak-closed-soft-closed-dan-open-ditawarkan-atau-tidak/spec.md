---
id: TC-FA-TDC-E2E-073-d-09-tahun-pajak-closed-soft-closed-dan-open-ditawarkan-atau-tidak
title: "Pilihan Effective From pada D-09: Tahun Pajak Seluruh Periode Closed Tidak Ditawarkan, Soft Closed dan Open Tetap Ditawarkan"
layer: ui-e2e
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-259
  - TC-FA-TDC-260
  - TC-FA-TDC-261
sourceRules: ["FATDC-LOGIC-04af", "FATDC-LOGIC-04ag", "FATDC-LOGIC-04e", "FATDC-LOGIC-04t", "V-20", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04af": [6, 7, 13, 20]
  "FATDC-LOGIC-04ag": 6
  "FATDC-LOGIC-04e": [7, 13, 20]
  "FATDC-LOGIC-04t": [8, 14, 21]
  "V-20": 15
  "§4.2c#b1": 24
coverage:
  web: automated
---

# Pilihan Effective From pada D-09: Tahun Pajak Seluruh Periode Closed Tidak Ditawarkan, Soft Closed dan Open Tetap Ditawarkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global (diubah spec ini, dipulihkan di hook `after` dan di langkah 26): jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00), Fiscal Year Start Januari, dan status periode Accounting Period tahun pajak 2026 dan 2027. Status periode diatur lewat fixture BE Accounting Period (aksi Period Close belum tersedia di UI; disediakan tim FE/BE). Hook `before` menyetel keadaan TC-259; hook `after` memulihkan status periode ke keadaan semula.
  - TC-259: periode 2026 Jan sampai Des seluruhnya Closed; periode 2027 seluruhnya Open.
  - TC-260: periode 2026 Jan sampai Nov Closed, Des Soft Closed.
  - TC-261: periode 2026 Jan sampai Nov Closed, Des Open.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`):

| TC | Class (Class Code bersuffix) | Keterangan |
|---|---|---|
| TC-259, 260, 261 | `KHS-V1-{runId}-073` | Non-building, Useful Life 8, Straight Line dan Declining Balance, Active, Used By 0, satu versi Current tanpa Effective From, tanpa versi Scheduled |

- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-259: Tahun pajak seluruh periode Closed tidak ditawarkan

1. Ketik Search `KHS-V1-{runId}-073`, tekan Enter
2. Klik link Class Code `KHS-V1-{runId}-073` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Klik Select Effective From
6. Verifikasi daftar opsi: `Jan 2027`, `Jan 2028`, `Jan 2029`, `Jan 2030`, `Jan 2031`
7. Verifikasi opsi `Jan 2026` tidak ditawarkan
8. Verifikasi nilai awal terpilih `Jan 2027` (opsi pertama yang ditawarkan), bukan kosong dan bukan `Jan 2026`
9. Klik `[Cancel]` pada dialog Save Changes

### TC-FA-TDC-260: Tahun pajak dengan satu periode Soft Closed tetap ditawarkan

10. Ubah status periode tahun pajak 2026 menjadi Jan sampai Nov Closed dan Des Soft Closed lewat fixture BE hingga tersimpan
11. Klik `[Save]`
12. Klik Select Effective From
13. Verifikasi opsi `Jan 2026` ditawarkan
14. Verifikasi nilai awal terpilih `Jan 2026`
15. Verifikasi tidak ada caption error pada Effective From
16. Klik `[Cancel]` pada dialog Save Changes

### TC-FA-TDC-261: Tahun pajak dengan satu periode Open tetap ditawarkan

17. Ubah status periode Des 2026 menjadi Open lewat fixture BE hingga tersimpan
18. Klik `[Save]`
19. Klik Select Effective From
20. Verifikasi opsi `Jan 2026` ditawarkan
21. Verifikasi nilai awal terpilih `Jan 2026`
22. Klik `[Cancel]` pada dialog Save Changes
23. Klik `[×]` pada Drawer Edit
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik `[Leave]`
26. Pulihkan status periode Accounting Period tahun pajak 2026 dan 2027 ke keadaan semula lewat fixture BE hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 9, 16, dan 22 (menutup dialog Save Changes dengan `[Cancel]` agar status periode dapat diubah dan dialog dibuka ulang), langkah 10 dan 17 (mengatur status periode untuk TC berikutnya; pelaku lewat fixture BE, R-20), langkah 23 sampai 25 (menutup Drawer yang dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08), langkah 26 (pemulihan state global).
- Ketiga TC memakai satu class dan satu sesi Drawer Edit yang dibuka pada langkah 2 sampai 4 (Useful Life `10`); langkah 1 sampai 3 tiap TC berikutnya identik dengan keadaan yang sudah terbentuk, dan dialog Save Changes dibuka ulang dengan `[Save]` agar pilihan Effective From dihitung dari status periode terbaru.
- Absence pada langkah 7: anchor positif adalah daftar opsi (langkah 6). Absence pada langkah 15: anchor positif adalah opsi dan nilai awal (langkah 13 dan 14).
- Temuan untuk QA:
  - TC-259, 260, 261 tidak menyebut cara mengubah status periode selain "data uji" (aksi Period Close belum tersedia); disediakan tim FE/BE (S-13).
  - TC-259, 260, 261 tidak menyebut email akun Total Control maupun company uji; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-073` (S-12); batas panjang Class Code tidak tertulis di TC.
