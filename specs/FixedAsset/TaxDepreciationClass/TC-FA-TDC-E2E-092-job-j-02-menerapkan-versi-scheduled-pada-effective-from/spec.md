---
id: TC-FA-TDC-E2E-092-job-j-02-menerapkan-versi-scheduled-pada-effective-from
title: "Job J-02: Menerapkan Versi Scheduled Menjadi Current pada 00:00 Effective From Menurut Time Zone Entitas"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-343
  - TC-FA-TDC-344
  - TC-FA-TDC-345
  - TC-FA-TDC-346
coverage:
  web: automated
---

# Job J-02: Menerapkan Versi Scheduled Menjadi Current pada 00:00 Effective From Menurut Time Zone Entitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Time Zone entitas Asia/Jakarta (UTC+07:00). Job J-02 dijalankan oleh scheduler harian; tick scheduler J-02 dijalankan eksplisit di langkah (kemampuan penahanan dan penjalanan job disediakan tim FE/BE, `suite.md`).
- Kendali jam sistem (`suite.md`): jam server dan jam browser diatur bersama pada waktu absolut yang tertulis di langkah (batas Jan 2027 menurut Time Zone entitas adalah 31 Des 2026 17:00:00 UTC; langkah 1 memakai 16:59:59 UTC dan langkah 7, 19, 26 memakai 17:00:00 UTC); jam dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; semua Active, Used By 0, versi Current tanpa Effective From):

| TC | Class (Class Code bersuffix) | Isi |
|---|---|---|
| TC-343, 344 | `KHS-J1-{runId}-092` | Current Useful Life 8; Scheduled Jan 2027 Useful Life 10; keduanya Straight Line dan Declining Balance |
| TC-345 | `KHS-J2-{runId}-092` | Current Useful Life 8; Scheduled Jan 2027 (Useful Life 10) dan Jan 2028 (Useful Life 12); Straight Line dan Declining Balance |
| TC-346 | `KHS-J3-{runId}-092` | Current Useful Life 8; Scheduled Jan 2027 (Useful Life 10) yang kemudian dibatalkan (Cancelled) |

- Tabel berisi tujuh class seed bawaan dan ketiga class di atas; baris `KHS-*` berada di halaman pertama sehingga dibuka tanpa Search.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-343: Versi Scheduled belum berlaku satu detik sebelum 00:00

1. Atur jam server dan jam browser ke 31 Des 2026 16:59:59 UTC (31 Des 2026 23:59:59 WIB) lalu jalankan tick scheduler J-02
2. Muat ulang halaman; baca baris `KHS-J1-{runId}-092`
3. Verifikasi baris `KHS-J1-{runId}-092`: Useful Life (years) "8", Effective From "—"
4. Klik link Class Code `KHS-J1-{runId}-092` pada tabel
5. Verifikasi Alert versi Scheduled tetap tampil dengan teks "Next version starts Jan 2027: 10 years, Straight Line 10%, Declining Balance 20%, Straight Line · Declining Balance."
6. Klik `[×]` pada header Drawer

### TC-FA-TDC-344: J-02 menjadikan versi Scheduled Current pada 00:00 Effective From

7. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC (1 Jan 2027 00:00:00 WIB) lalu jalankan tick scheduler J-02
8. Muat ulang halaman; baca baris `KHS-J1-{runId}-092` dan arahkan kursor ke sel Effective From
9. Verifikasi baris: Useful Life (years) "10", Straight Line Rate "10%", Declining Balance Rate "20%", Effective From "Jan 2027"
10. Verifikasi tidak ada toast
11. Verifikasi tooltip "Next version starts ..." tidak ada lagi pada sel Effective From
12. Klik link Class Code `KHS-J1-{runId}-092` pada tabel
13. Verifikasi Drawer Edit: Effective From read-only "Jan 2027"
14. Verifikasi Alert versi Scheduled tidak tampil
15. Klik tautan View versions
16. Verifikasi modal Versions: "Jan 2027" berstatus "Current"; "—" berstatus "Past"
17. Tutup modal Versions
18. Klik `[×]` pada header Drawer

### TC-FA-TDC-345: J-02 pada dua versi Scheduled

19. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC lalu jalankan tick scheduler J-02
20. Muat ulang halaman; arahkan kursor ke sel Effective From baris `KHS-J2-{runId}-092`
21. Verifikasi baris `KHS-J2-{runId}-092`: Effective From "Jan 2027"
22. Verifikasi tooltip sel Effective From: "Next version starts Jan 2028."
23. Klik link Class Code `KHS-J2-{runId}-092` pada tabel
24. Verifikasi Alert: "Next version starts Jan 2028: 12 years, Straight Line 8.33%, Declining Balance 16.67%, Straight Line · Declining Balance."
25. Klik `[×]` pada header Drawer

### TC-FA-TDC-346: Versi Cancelled tidak diterapkan J-02

26. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC lalu jalankan tick scheduler J-02
27. Muat ulang halaman; baca baris `KHS-J3-{runId}-092`
28. Verifikasi baris `KHS-J3-{runId}-092`: Useful Life (years) "8", Effective From "—"
29. Klik link Class Code `KHS-J3-{runId}-092` pada tabel
30. Klik tautan View versions
31. Verifikasi modal Versions: "Jan 2027" tetap "Cancelled"; "—" tetap "Current"
32. Tutup modal Versions
33. Klik `[×]` pada header Drawer

## Notes

- Langkah penghubung (S-03): langkah 6, 18, 25, dan 33 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`), dan langkah 17 dan 32 (menutup modal Versions). Langkah 2, 8, 20, 27 menggabungkan muat ulang dan "baca/arahkan kursor" seperti langkah TC.
- Anchor positif untuk absence (8b.2): langkah 9 (baris `KHS-J1` termuat) untuk langkah 10 dan 11; langkah 13 (Effective From read-only tampil) untuk langkah 14.
- Langkah 7, 19, dan 26 mengatur jam absolut yang sama; jam tidak diperiksa antar blok karena tiap blok menyetel ulang. Class `KHS-J1` pada TC-343 dan 344 adalah class yang sama (TC-343 sebelum batas, TC-344 pada batas).
- Post Condition TC-343 ("tidak ada entri L-08"), TC-344 (satu entri L-08 Modified By System), dan TC-346 ("tidak ada entri L-08") tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan L-08 ada di spec 096.
- Temuan untuk QA:
  - TC-343 Expected: tidak ada Expected untuk toast; TC-344 butir a memuat "tidak ada toast" yang berpegang pada tampilan setelah muat ulang (toast hanya sementara).
  - Post Condition TC-343, TC-344, dan TC-346 tanpa langkah observasi di TC.
  - TC-343 sampai 346 memakai `KHS-J1`, `KHS-J2`, `KHS-J3` tanpa suffix; spec memakai `-{runId}-092` (S-12).
  - TC-345 dan TC-346 tidak menyebut tanggal sistem uji; spec memakai jam absolut dari langkah.
  - Email akun Total Control tidak tertulis di TC.
