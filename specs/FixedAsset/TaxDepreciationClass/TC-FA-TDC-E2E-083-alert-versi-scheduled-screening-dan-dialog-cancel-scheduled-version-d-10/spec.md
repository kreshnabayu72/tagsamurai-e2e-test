---
id: TC-FA-TDC-E2E-083-alert-versi-scheduled-screening-dan-dialog-cancel-scheduled-version-d-10
title: "Alert Versi Scheduled pada Drawer Edit dan Screening Dialog Cancel Scheduled Version (D-10)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-294
  - TC-FA-TDC-295
  - TC-FA-TDC-296
  - TC-FA-TDC-297
coverage:
  web: automated
---

# Alert Versi Scheduled pada Drawer Edit dan Screening Dialog Cancel Scheduled Version (D-10)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; semua Active, Used By 0, satu versi Current tanpa Effective From dan satu versi Scheduled Effective From Jan 2027):

| TC | Class (Class Code bersuffix) | Isi |
|---|---|---|
| TC-294, 297 | `KHS-C1-{runId}-083` (Class Name `Kelompok cancel uji`) | Current Useful Life 8, Straight Line dan Declining Balance; Scheduled Jan 2027 Useful Life 10, Straight Line dan Declining Balance |
| TC-295 | `KHS-C2-{runId}-083` | Scheduled Jan 2027 Useful Life 16, Straight Line saja |
| TC-296 | `KHS-C3-{runId}-083` | Scheduled Jan 2027 Useful Life 10, Declining Balance saja |

- Tabel berisi tujuh class seed bawaan dan ketiga class di atas (10 baris pada satu halaman, page size default 10); baris `KHS-*` berada di halaman pertama sehingga dibuka tanpa Search. Class Name `KHS-C2` dan `KHS-C3` tidak disebut TC dan ditetapkan fixture.
- Kemampuan teknis: seeding class dengan versi Current dan Scheduled lewat API; mengamati teks Alert dan dialog.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-294: Screening Alert versi Scheduled (Straight Line dan Declining Balance)

1. Klik link Class Code `KHS-C1-{runId}-083` pada tabel
2. Amati bagian paling atas Drawer di atas field form
3. Verifikasi Alert severity info berada di bagian paling atas Drawer mode Edit, di atas field Regulation Reference
4. Verifikasi teks Alert: "Next version starts Jan 2027: 10 years, Straight Line 10%, Declining Balance 20%, Straight Line · Declining Balance."
5. Verifikasi tombol `[Cancel scheduled version]` tampil pada Alert
6. Klik `[×]` pada header Drawer

### TC-FA-TDC-295: Alert tanpa bagian Declining Balance

7. Klik link Class Code `KHS-C2-{runId}-083` pada tabel
8. Verifikasi teks Alert: "Next version starts Jan 2027: 16 years, Straight Line 6.25%, Straight Line."
9. Verifikasi bagian "Declining Balance [y]%" tidak ditulis pada teks Alert
10. Klik `[×]` pada header Drawer

### TC-FA-TDC-296: Alert tanpa bagian Straight Line

11. Klik link Class Code `KHS-C3-{runId}-083` pada tabel
12. Verifikasi teks Alert: "Next version starts Jan 2027: 10 years, Declining Balance 20%, Declining Balance."
13. Verifikasi bagian "Straight Line [x]%" tidak ditulis pada teks Alert
14. Klik `[×]` pada header Drawer

### TC-FA-TDC-297: Screening dialog Cancel Scheduled Version (D-10)

15. Klik link Class Code `KHS-C1-{runId}-083` pada tabel
16. Klik `[Cancel scheduled version]` pada Alert
17. Amati dialog dari atas ke bawah
18. Verifikasi header: judul dialog `Cancel Scheduled Version`
19. Verifikasi body (tanpa field), baris pertama: "• KHS-C1-{runId}-083 – Kelompok cancel uji"
20. Verifikasi body, baris kedua: "Effective From Jan 2027"
21. Verifikasi body, baris ketiga: "Are you sure you want to cancel this scheduled version?"
22. Verifikasi footer: tombol `[Back]` dan `[Cancel version]` (severity danger)
23. Klik `[Back]`
24. Klik `[×]` pada header Drawer

## Notes

- Langkah penghubung (S-03): langkah 6, 10, 14, 24 (menutup Drawer tanpa perubahan, sehingga tanpa dialog `Unsaved Changes`) dan langkah 23 (`[Back]` menutup dialog D-10 tanpa membatalkan versi, agar data uji tidak berubah).
- Langkah 2 dan 17 ("Amati") adalah langkah TC tanpa asersi; asersinya ada pada `Verifikasi` sesudahnya.
- Tiap class memakai satu pembukaan Drawer; baris `KHS-*` dibuka tanpa Search karena berada di halaman pertama urutan default Class Code A-Z (sebelum `LAND`).
- Pembatalan versi sungguhan (menekan `[Cancel version]`) tidak dilakukan di spec ini; ada di spec 084 sampai 086.
- Temuan untuk QA:
  - Class Code `KHS-C1`, `KHS-C2`, `KHS-C3` ditulis tanpa suffix di TC; spec memakai `-{runId}-083` (S-12), sehingga baris D-10 memuat Class Code bersuffix. Batas panjang Class Code tidak disebut TC.
  - Class Name `KHS-C2` dan `KHS-C3` tidak disebut TC.
  - Email akun Total Control tidak tertulis di TC.
