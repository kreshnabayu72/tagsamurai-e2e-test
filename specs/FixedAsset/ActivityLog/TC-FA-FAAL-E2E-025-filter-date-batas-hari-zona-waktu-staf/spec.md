---
id: TC-FA-FAAL-E2E-025-filter-date-batas-hari-zona-waktu-staf
title: "Filter Date pada Batas Hari, Zona Waktu Staf, dan Tie-Breaker Sort"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-76
  - TC-FA-FAAL-106
  - TC-FA-FAAL-128
  - TC-FA-FAAL-208
coverage:
  web: automated
---

# Filter Date pada Batas Hari, Zona Waktu Staf, dan Tie-Breaker Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control pada client Batas Waktu (Pre-setup #15) dengan General Settings Time Zone `Asia/Jakarta` (UTC+07:00), format tanggal `dd/MM/yy` dan `HH:mm`. Password lewat `Spectra.env.FA_TCBATAS_PASSWORD` (butir "Env var" di `suite.md`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun kedua (langkah 29): Read Only staf B (Pre-setup #10) `readOnlyStaffB_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_RO_STAFB_PASSWORD`, Date Format `M/d/yy`, Time Format `hh:mm a`, Time Zone `(UTC+00:00) UTC, Reykjavik, Accra`. Env var `FA_RO_STAFB_PASSWORD` didaftarkan tim FE (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: client Batas Waktu (Pre-setup #15). Tab Session BD-1 (UTC 2026-07-15 16:59:59), BD-2 (UTC 2026-07-15 17:00:00), BD-3 (UTC 2026-07-16 16:59:59), BD-4 (UTC 2026-07-16 17:00:00), serta BD-5 dan BD-6 bertimestamp sama persis dengan BD-5 ditulis lebih dulu dari BD-6 (BD-5 dan BD-6 berPosition sama). Tab User Action BD-U1 sampai BD-U4 dengan timestamp UTC yang sama seperti BD-1 sampai BD-4. Spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: muat ulang halaman (F5) pada langkah 17.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-76: Filter Date Tab Session pada batas hari dalam zona waktu staf

1. Verifikasi kolom Date BD-1 tampil `15/07/26, 23:59`
2. Verifikasi kolom Date BD-2 tampil `16/07/26, 00:00`
3. Verifikasi kolom Date BD-3 tampil `16/07/26, 23:59`
4. Verifikasi kolom Date BD-4 tampil `17/07/26, 00:00`
5. Klik icon Filter
6. Pilih tanggal mulai `16/07/26` dan tanggal akhir `16/07/26` pada field Date
7. Klik `[Apply]`
8. Verifikasi hanya BD-2 dan BD-3 tampil (00:00:00 hari mulai dan 23:59:59 hari akhir termasuk)
9. Verifikasi BD-1 dan BD-4 tidak tampil
10. Klik `[Clear Field]`
11. Klik `[Apply]`

### TC-FA-FAAL-106: Tie-breaker sort: timestamp sama dan nilai kosong

12. Verifikasi urutan default Newest First: BD-6 (ditulis lebih akhir) di atas BD-5
13. Klik header Position sekali
14. Verifikasi sort Position Ascending: BD-6 tetap di atas BD-5 (tie-breaker default sort)
15. Klik header Position sekali lagi
16. Verifikasi sort Position Descending: BD-6 tetap di atas BD-5 (tie-breaker default sort)
17. Muat ulang halaman (F5)
18. Verifikasi urutan identik setelah muat ulang: BD-6 di atas BD-5 (deterministik)

### TC-FA-FAAL-128: Filter Date Tab User Action pada batas hari dalam zona waktu staf

19. Klik tab User Action
20. Verifikasi kolom Date BD-U1 tampil `15/07/26, 23:59`
21. Verifikasi kolom Date BD-U2 tampil `16/07/26, 00:00`
22. Verifikasi kolom Date BD-U3 tampil `16/07/26, 23:59`
23. Verifikasi kolom Date BD-U4 tampil `17/07/26, 00:00`
24. Klik icon Filter
25. Pilih tanggal mulai `16/07/26` dan tanggal akhir `16/07/26` pada field Date
26. Klik `[Apply]`
27. Verifikasi hanya BD-U2 dan BD-U3 tampil

### TC-FA-FAAL-208: Filter Date dinilai dalam zona waktu staf yang login, bukan zona entitas atau UTC

28. Ganti akun: Logout dari akun Total Control
29. Login sebagai Read Only staf B (Pre-setup #10) dengan password `Spectra.env.FA_RO_STAFB_PASSWORD`
30. Buka Fixed Asset > Reports & Logs > Activity Log pada client Batas Waktu (Tab Session)
31. Klik icon Filter
32. Pilih tanggal mulai `7/16/26` dan tanggal akhir `7/16/26` pada field Date
33. Klik `[Apply]`
34. Verifikasi hanya BD-3 (`7/16/26, 04:59 PM`) dan BD-4 (`7/16/26, 05:00 PM`) tampil
35. Verifikasi BD-1 dan BD-2 tidak tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 10, 11, 28, 29, 30 (mengosongkan filter Date setelah TC-FA-FAAL-76, ganti akun, dan membuka layar untuk akun staf B). Ganti akun pada langkah 29 bersifat eksplisit (S-07); hook `after` mengembalikan sesi ke akun default suite.
- Penyimpangan urutan (S-10): TC-FA-FAAL-106 diletakkan sebelum TC-FA-FAAL-128 agar seluruh asersi Tab Session pada akun Total Control berurutan; TC-FA-FAAL-208 terakhir karena mengganti akun.
- Langkah 1 TC-FA-FAAL-76 ("Buka tab Session") dipenuhi hook `beforeEach` suite; TC-FA-FAAL-208 membuka layar sendiri karena sesudah ganti akun.
- Temuan untuk QA:
  - Email dan password akun Total Control untuk client Batas Waktu (#15) tidak tertulis di Pre-setup #1 sampai #10; disediakan tim FE.
  - Timestamp BD-5 dan BD-6 tidak tertulis di Pre-setup #15, sehingga posisi BD-1 sampai BD-4 serta BD-5 dan BD-6 pada halaman 1 tabel (urutan default Newest First) tidak dapat dipastikan (S-14); spec mengikuti TC dan mengandalkan seed tim FE/BE.
  - TC-FA-FAAL-106 langkah 2 ("Klik header Position sekali lalu dua kali") tidak menyebut arah sort tiap klik; spec memetakan klik pertama ke Ascending dan klik kedua ke Descending sesuai urutan di Expected b.
  - TC-FA-FAAL-106 judul menyebut "nilai kosong", sedangkan langkah dan Pre-setup menyebut BD-5 dan BD-6 berPosition sama; spec mengikuti langkah TC.
