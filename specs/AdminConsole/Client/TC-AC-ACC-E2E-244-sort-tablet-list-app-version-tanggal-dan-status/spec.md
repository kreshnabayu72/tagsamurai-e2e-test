---
id: TC-AC-ACC-E2E-244-sort-tablet-list-app-version-tanggal-dan-status
title: "Sort Tablet List: Default Device Name, App Version Semantic, Enrolled Date, Last Active, dan Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-845
  - TC-AC-ACC-846
coverage:
  web: automated
---

# Sort Tablet List: Default Device Name, App Version Semantic, Enrolled Date, Last Active, dan Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): C-DTL-1 "PT Uji Tabel Detail" dengan Station "Gerbang Uji" berisi tiga Tablet: "Tablet Uji 1" (App Version 2.10.0, Enrolled Date 05 Jan 2026, Last Active 08 Jul 2026 09:00, Status Active); "Tablet Uji 2" (2.9.1, 12 Feb 2026, 07 Jul 2026 18:00, Inactive); "Tablet Uji 3" (2.9.0, 03 Nov 2025, 01 Mar 2026 10:00, Active). Urutan default Tablet List: Device Name A-Z. Setiap kolom yang diurutkan punya sedikitnya dua nilai distinct.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Uji Tabel Detail" di List Client, tekan Enter, klik Company Name "PT Uji Tabel Detail", lalu klik Tab Asset Control
2. Klik baris Station "Gerbang Uji" untuk membuka Tablet List

### TC-AC-ACC-845: Sort Tablet List: default Device Name A-Z dan App Version semantic

3. Verifikasi urutan awal: Tablet Uji 1, Tablet Uji 2, Tablet Uji 3
4. Klik header App Version
5. Verifikasi urutan: Tablet Uji 3 (2.9.0), Tablet Uji 2 (2.9.1), Tablet Uji 1 (2.10.0)
6. Klik header App Version lagi
7. Verifikasi urutan: Tablet Uji 1 (2.10.0), Tablet Uji 2 (2.9.1), Tablet Uji 3 (2.9.0)
8. Klik header Device Name
9. Verifikasi urutan: Tablet Uji 1, Tablet Uji 2, Tablet Uji 3
10. Klik header Device Name lagi
11. Verifikasi urutan: Tablet Uji 3, Tablet Uji 2, Tablet Uji 1

### TC-AC-ACC-846: Sort Tablet List kolom Enrolled Date, Last Active, dan Status

12. Klik header Enrolled Date
13. Verifikasi Oldest First: Tablet Uji 3, Tablet Uji 1, Tablet Uji 2
14. Klik header Enrolled Date lagi
15. Verifikasi Newest First: Tablet Uji 2, Tablet Uji 1, Tablet Uji 3
16. Klik header Last Active
17. Verifikasi Oldest First: Tablet Uji 3, Tablet Uji 2, Tablet Uji 1
18. Klik header Last Active lagi
19. Verifikasi Newest First: Tablet Uji 1, Tablet Uji 2, Tablet Uji 3
20. Klik header Status
21. Verifikasi Tablet Uji 1 dan Tablet Uji 3 (Active) pada posisi 1 dan 2, lalu Tablet Uji 2 (Inactive) pada posisi 3
22. Klik header Status lagi
23. Verifikasi Tablet Uji 2 (Inactive) pada posisi 1, lalu Tablet Uji 1 dan Tablet Uji 3 (Active) pada posisi 2 dan 3

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client) dan langkah 2 (expand row Station agar Tablet List teramati).
- Temuan untuk QA:
  - TC-AC-ACC-845 Expected a tidak menyebut apakah urutan awal diurutkan oleh default Device Name A-Z atau oleh seed; spec mengikuti Expected.
  - TC-AC-ACC-846 Expected e dan f tidak menentukan urutan antar dua Tablet Active (Tablet Uji 1 dan Tablet Uji 3); tidak diasersi.
