---
id: TC-FA-TDC-E2E-090-cancel-version-batas-tahun-pajak-dan-time-zone-entitas
title: "Cancel Version: Batas Tahun Pajak Dimulai Menurut Time Zone Entitas"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-307
  - TC-FA-TDC-308
  - TC-FA-TDC-309
  - TC-FA-TDC-310
coverage:
  web: automated
---

# Cancel Version: Batas Tahun Pajak Dimulai Menurut Time Zone Entitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Time Zone entitas Asia/Jakarta (UTC+07:00); Fiscal Year Start Januari. Batas tahun pajak Jan 2027 menurut Time Zone entitas adalah 31 Des 2026 17:00:00 UTC (1 Jan 2027 00:00 WIB).
- Kendali jam sistem (`suite.md`): jam server dan jam browser diatur bersama pada waktu absolut yang tertulis di langkah (bukan digeser relatif; bagian 6 konvensi); jam dipulihkan di hook `after`. Job J-02 ditahan (belum berjalan) sepanjang spec; penahanan job disediakan tim FE/BE (`suite.md`) dan dilepas di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`): class `KHS-C1-{runId}-090` (Class Name `Kelompok cancel uji`), Active, Used By 0, versi Current tanpa Effective From (Useful Life 8, Straight Line dan Declining Balance) dan satu versi Scheduled Effective From Jan 2027 (Useful Life 10, Straight Line dan Declining Balance). Tabel berisi tujuh class seed bawaan dan class itu; baris dibuka tanpa Search.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-307: Confirm ditolak server setelah tahun pajak versi dimulai

1. Atur jam server dan jam browser ke 31 Des 2026 16:30 UTC (31 Des 2026 23:30 WIB)
2. Klik link Class Code `KHS-C1-{runId}-090` pada tabel
3. Klik `[Cancel scheduled version]` pada Alert
4. Majukan jam server dan jam browser ke 31 Des 2026 17:05 UTC (1 Jan 2027 00:05 WIB) tanpa menjalankan J-02
5. Klik `[Cancel version]`
6. Verifikasi toast error "Error, failed to cancel scheduled version."
7. Verifikasi dialog D-10 tertutup
8. Verifikasi Drawer disegarkan: Alert tidak lagi menampilkan versi Jan 2027
9. Klik `[×]` pada header Drawer

### TC-FA-TDC-308: Setelah tahun pajak dimulai, Alert dan tombol Cancel tidak tersedia

10. Klik link Class Code `KHS-C1-{runId}-090` pada tabel
11. Verifikasi field Regulation Reference tampil pada Drawer Edit
12. Verifikasi Drawer Edit tidak menampilkan Alert untuk versi Jan 2027
13. Verifikasi tombol `[Cancel scheduled version]` tidak ada
14. Klik tautan View versions
15. Verifikasi baris "Jan 2027" tampil pada modal Versions
16. Verifikasi baris "Jan 2027" tidak memiliki tombol `[Cancel]`
17. Tutup modal Versions
18. Klik `[×]` pada header Drawer

### TC-FA-TDC-310: Cancel ditolak tepat setelah tahun pajak dimulai walau tanggal UTC masih 31 Des

19. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC (1 Jan 2027 00:00 WIB)
20. Klik link Class Code `KHS-C1-{runId}-090` pada tabel
21. Verifikasi field Regulation Reference tampil pada Drawer Edit
22. Verifikasi Alert tidak menampilkan versi Jan 2027
23. Verifikasi tombol `[Cancel scheduled version]` tidak ada
24. Klik `[×]` pada header Drawer

### TC-FA-TDC-309: Cancel masih dapat dilakukan satu menit sebelum tahun pajak dimulai

25. Atur jam server dan jam browser ke 31 Des 2026 16:59 UTC (31 Des 2026 23:59 WIB)
26. Klik link Class Code `KHS-C1-{runId}-090` pada tabel
27. Klik `[Cancel scheduled version]` pada Alert
28. Klik `[Cancel version]`
29. Verifikasi toast sukses "Success, scheduled version has been cancelled."
30. Klik tautan View versions
31. Verifikasi baris "Jan 2027" berstatus "Cancelled"
32. Tutup modal Versions
33. Klik `[×]` pada header Drawer

## Notes

- Urutan TC-307, 308, 310, 309 (TC-310 sebelum TC-309): TC-309 membatalkan versi Jan 2027 dan menghabiskan data uji, sehingga dijalankan terakhir (S-10); jam diatur absolut ulang pada tiap blok.
- Langkah penghubung (S-03): langkah 9, 18, 24, dan 33 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`), langkah 17 dan 32 (menutup modal Versions), dan langkah 1, 19, dan 25 (mengatur jam absolut; jam server dan jam browser bersama sesuai bagian 6).
- Langkah 4 memajukan jam server dan jam browser bersama; TC hanya menyebut jam server, dan penyetelan bersama dipilih mengikuti `suite.md`.
- Anchor positif untuk absence (8b.2): langkah 11 dan 21 (field Regulation Reference tampil) untuk langkah 12, 13, 22, 23; langkah 15 (baris "Jan 2027" tampil) untuk langkah 16.
- Langkah 7 dan 8: Expected "Dialog D-10 tertutup" dan "Drawer disegarkan: Alert tidak lagi menampilkan versi Jan 2027" diasersi setelah toast; absence Alert pada langkah 8 berpegang pada toast error (langkah 6) sebagai anchor respons server selesai.
- Post Condition TC-307 (tidak ada mutasi dan tidak ada entri log; versi Jan 2027 tidak berstatus Cancelled) tidak punya langkah observasi di TC; "versi Jan 2027 tidak berstatus Cancelled" diamati sebagian lewat langkah 15 dan 16 pada TC-308 (baris masih tampil tanpa tombol `[Cancel]`), entri log tidak diasersi (S-01).
- Temuan untuk QA:
  - TC-307 ditandai Manual Only "(d) dua sesi paralel", tetapi langkah TC hanya satu sesi dengan jam server dimajukan; spec menulis satu sesi dengan jam diatur absolut.
  - TC-307 langkah 3 hanya menyebut jam server; TC-308 dan 310 membutuhkan jam browser yang sinkron agar tanggal tampil konsisten.
  - TC-308 butir c ("baris Jan 2027 tidak memiliki tombol [Cancel]") bergantung baris "Jan 2027" masih tampil di modal Versions setelah tahun pajak dimulai; status baris itu (Scheduled atau lainnya) tidak disebut TC.
  - Post Condition TC-307 tanpa langkah observasi di TC.
  - Class Code `KHS-C1` tanpa suffix di TC; spec memakai `-{runId}-090` (S-12).
  - Email akun Total Control tidak tertulis di TC.
