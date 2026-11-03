---
id: TC-AC-RP-E2E-089-modal-changelog-screening-per-varian
title: "Modal Changelog: Screening Lima Varian (Total Control, Read Only, GM, System, Detail Role)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-293
  - TC-AC-RP-294
  - TC-AC-RP-295
  - TC-AC-RP-296
  - TC-AC-RP-297
coverage:
  web: automated
---

# Modal Changelog: Screening Lima Varian (Total Control, Read Only, GM, System, Detail Role)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #15 (penugasan peran individual), dan #18 (riwayat Changelog seed).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis bersuffix `+{runId}-<NNN>` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-293: Screening Modal Changelog varian Total Control

1. Klik ikon Changelog
2. Verifikasi Title "Changelog: Role & Permission > Total Control"
3. Verifikasi Toolbar memuat Search (placeholder "Search action, user, or value..."), Filter, dan Download
4. Verifikasi kolom Date, Action, User Name, Field, Old Value, New Value, Modified By, dan header `⋯` tanpa row action
5. Verifikasi urutan kolom Date Newest First
6. Verifikasi Pagination default 10
7. Tutup modal Changelog

### TC-AC-RP-294: Screening Modal Changelog varian Read Only

8. Klik tab `Read Only`
9. Klik ikon Changelog
10. Verifikasi Title "Changelog: Role & Permission > Read Only"
11. Verifikasi Toolbar memuat Search (placeholder "Search action, user, or value..."), Filter, dan Download
12. Verifikasi kolom Date, Action, User Name, Field, Old Value, New Value, Modified By, dan header `⋯` tanpa row action
13. Verifikasi urutan kolom Date Newest First
14. Verifikasi Pagination default 10
15. Tutup modal Changelog

### TC-AC-RP-295: Screening Modal Changelog varian Group Manager

16. Klik tab `Group Manager`
17. Klik ikon Changelog
18. Verifikasi Title "Changelog: Role & Permission > Group Manager"
19. Verifikasi Toolbar memuat Search (placeholder "Search action, user, group, or value..."), Filter, dan Download
20. Verifikasi kolom Date, Action, User Name — Group Name, Field, Old Value, New Value, Modified By, dan header `⋯` tanpa row action
21. Verifikasi urutan kolom Date Newest First
22. Verifikasi Pagination default 10
23. Tutup modal Changelog

### TC-AC-RP-296: Screening Modal Changelog varian System

24. Klik tab `System`
25. Klik ikon Changelog
26. Verifikasi Title "Changelog: Role & Permission > System"
27. Verifikasi Toolbar memuat Search (placeholder "Search action, role, user, or value..."), Filter, dan Download
28. Verifikasi kolom Date, Action, Role — User, Field, Old Value, New Value, Modified By, dan header `⋯` tanpa row action
29. Verifikasi urutan kolom Date Newest First
30. Verifikasi Pagination default 10
31. Tutup modal Changelog

### TC-AC-RP-297: Screening Modal Changelog varian Detail Role

32. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
33. Klik ikon Changelog
34. Verifikasi Title "Changelog: Role & Permission > Manage device master data"
35. Verifikasi Toolbar memuat Search (placeholder "Search action, user, or value..."), Filter, dan Download
36. Verifikasi kolom Date, Action, Role Name — User, Field, Old Value, New Value, Modified By, dan header `⋯` tanpa row action
37. Verifikasi urutan kolom Date Newest First
38. Verifikasi Pagination default 10

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 7, 15, 23, 31.
- Expected b TC-AC-RP-293 sampai 297 (Toolbar Search, Filter, Download) ditulis satu Verifikasi per varian karena daftar elemen toolbar disebut utuh dalam satu butir (S-01); Expected c diuraikan menjadi daftar kolom, urutan Date, dan Pagination.
- Modal terakhir (TC-AC-RP-297) tidak ditutup karena hook `beforeEach` suite membuka ulang halaman untuk spec berikutnya.
- Alasan sekitar 35 langkah (38 langkah): lima blok screening satu kelas fungsional pada modal Changelog yang sama, tiap blok berdiri sendiri (varian, tab, dan data berbeda), dan kegagalan satu varian tidak membuat varian lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-RP-297 Expected a menulis Title "Changelog: Role & Permission > Manage device master data"; PRD §4.2j memakai nama role; spec mengikuti TC.
