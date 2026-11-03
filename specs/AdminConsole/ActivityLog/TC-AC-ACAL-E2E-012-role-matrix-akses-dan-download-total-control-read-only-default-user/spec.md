---
id: TC-AC-ACAL-E2E-012-role-matrix-akses-dan-download-total-control-read-only-default-user
title: "Role Matrix: Akses, Toolbar, dan Download Total Control, Read Only, Default User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-25
  - TC-AC-ACAL-26
  - TC-AC-ACAL-27
coverage:
  web: automated
---

# Role Matrix: Akses, Toolbar, dan Download Total Control, Read Only, Default User

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); hook suite (flag Guided Tooltip, pemulihan preferensi Setup Column, kemampuan sesi API aktor) dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md). Untuk akun Read Only dan Default User, hook before/after spec ini menyetel dan memulihkan flag yang sama (kemampuan disediakan tim FE/BE).
- Spec Role Matrix positif (bagian 3a konvensi). Password tidak ditulis di spec atau fixture; dari nama env AC_* di bawah hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; nama lain adalah usulan tim FE (Pre-setup TC tidak menyebut env; lihat Temuan untuk QA).

Role yang diuji (Principal), urutan baris = urutan blok:

| Role | Email (Pre-setup TC) | Env var password |
|---|---|---|
| Total Control (Principal) | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 1) | `Spectra.env.AC_TC_PASSWORD` |
| Read Only (Principal) | `readOnlyAdminConsolePrincipal_automated_{namaCompany}@qwertysystem.net` (No 2) | `Spectra.env.AC_RO_PASSWORD` |
| Default User | `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 3) | `Spectra.env.AC_DU_PASSWORD` |

- Login akun pertama (Total Control Principal) di hook `before` spec ini; halaman Admin Console > Activity Log dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (tetap di environment): hanya tiga akun pada tabel di atas dan data log kedua tab (Pre-setup No 9 dan 10) agar tabel tidak kosong. Tidak ada Data Dinamis.
- Kemampuan teknis (disediakan tim FE): penangkapan berkas unduhan browser untuk langkah Download (nama berkas diasersi, isi berkas tidak).
- Jam server dan jam browser tidak diatur.

## Test Steps

### TC-AC-ACAL-25: Total Control, menu, kedua tab, toolbar, Setup Column, dan Download

1. Verifikasi menu Activity Log tampil (Show) pada sidebar Admin Console
2. Verifikasi tab Session tampil dengan Search, Filter, Download, Sort, dan Pagination aktif
3. Klik header `⋯` pada tab Session
4. Verifikasi Overlay Column Visibility terbuka pada tab Session
5. Tutup Overlay Column Visibility
6. Klik icon Download, pilih `Download as CSV`
7. Verifikasi tidak ada toast yang tampil setelah klik Download tab Session
8. Verifikasi berkas `Activity-Log-Session.csv` terunduh
9. Klik tab "User Action"
10. Verifikasi tab User Action tampil dengan Search, Filter, Download, Sort, dan Pagination aktif
11. Klik header `⋯` pada tab User Action
12. Verifikasi Overlay Column Visibility terbuka pada tab User Action
13. Tutup Overlay Column Visibility
14. Klik icon Download, pilih `Download as CSV`
15. Verifikasi tidak ada toast yang tampil setelah klik Download tab User Action
16. Verifikasi berkas `Activity-Log-User-Action.csv` terunduh

### TC-AC-ACAL-26: Read Only, akses UI identik Total Control dan Download berhasil

17. Ganti akun: logout, lalu login sebagai Read Only (Principal) dengan `Spectra.env.AC_RO_PASSWORD`
18. Verifikasi menu Activity Log tampil (Show) pada sidebar Admin Console
19. Klik menu Activity Log di sidebar Admin Console
20. Verifikasi tab Session tampil dengan Search, Filter, Download, Sort, Pagination, dan Setup Column aktif, tanpa state Disabled
21. Klik tab "User Action"
22. Verifikasi tab User Action tampil dengan Search, Filter, Download, Sort, Pagination, dan Setup Column aktif, tanpa state Disabled
23. Klik header `⋯` pada tab User Action
24. Verifikasi Overlay Column Visibility terbuka pada tab User Action
25. Tutup Overlay Column Visibility
26. Klik icon Download, pilih `Download as XLSX`
27. Verifikasi tidak ada toast yang tampil setelah klik Download
28. Verifikasi berkas `Activity-Log-User-Action.xlsx` terunduh

### TC-AC-ACAL-27: Default User, akses setara Total Control

29. Ganti akun: logout, lalu login sebagai Default User dengan `Spectra.env.AC_DU_PASSWORD`
30. Verifikasi menu Activity Log tampil (Show) pada sidebar Admin Console
31. Klik menu Activity Log di sidebar Admin Console
32. Verifikasi tab Session dan tab User Action tampil
33. Verifikasi toolbar tab Session tampil dengan Search, Filter, dan Download
34. Klik tab "User Action"
35. Verifikasi toolbar tab User Action tampil dengan Search, Filter, dan Download
36. Klik tab "Session"
37. Klik icon Download, pilih `Download as CSV`
38. Verifikasi berkas `Activity-Log-Session.csv` terunduh

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-25, 26, 27).
- Spec ditulis per blok role (bagian 3a konvensi, `[KEPUTUSAN 2026-10-30]`): langkah ketiga TC berbeda per role (format dan tab Download berbeda, Setup Column hanya diuji di TC-AC-ACAL-25 dan 26), dan ganti akun menuntut Step eksplisit; akun pertama login di hook `before`.
- Spec 38 langkah, di atas smell 35. Alasan: seluruh blok satu topik (akses baca per role pada halaman yang sama) dan satu kelas harness; tiap blok role berdiri sendiri setelah Step ganti akun, sehingga kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup Overlay Column Visibility (langkah 5, 13, 25), membuka menu dan tab (langkah 9, 19, 21, 31, 34, 36), dan ganti akun (langkah 17 dan 29).
- Perbandingan TC-AC-ACAL-26 "identik Total Control" ditulis sebagai `Verifikasi` hasil per langkah pada Read Only (aktif tanpa Disabled) dan bukan sebagai perbandingan antar role.
- Absence toast diasersi tepat sesudah klik Download dan sebelum asersi berkas terunduh (state sementara; bagian 8b butir 11).
- Isi berkas unduhan tidak diasersi (hanya nama berkas yang terunduh sesuai Expected).
- Temuan untuk QA:
  - Email Pre-setup memakai placeholder `{namaCompany}`; nilai ditetapkan tim FE. `AC_TC_PASSWORD` terdaftar di `.env.example` dan `spectra.config.ts`; `AC_RO_PASSWORD` dan `AC_DU_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
  - TC-AC-ACAL-25 Expected b menyebut "Kedua tab Show" dan toolbar aktif tetapi tidak menyebut Setup Column di Expected tab; Setup Column hanya diamati lewat Overlay Column Visibility (Expected c).
  - TC-AC-ACAL-26 Expected b ("tidak ada state Disabled") dan TC-AC-ACAL-27 Expected b ("toolbar") tidak menyebut daftar elemen yang tepat; spec memakai daftar Search, Filter, Download, Sort, Pagination (Setup Column untuk Read Only) mengikuti TC-AC-ACAL-25.
  - Cara menutup Overlay Column Visibility tidak ditulis di TC; spec menulis "Tutup" sebagai langkah penghubung dan tahap script menetapkan caranya.
