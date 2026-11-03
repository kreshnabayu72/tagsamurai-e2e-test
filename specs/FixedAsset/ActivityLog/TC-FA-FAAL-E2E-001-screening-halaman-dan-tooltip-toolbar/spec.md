---
id: TC-FA-FAAL-E2E-001-screening-halaman-dan-tooltip-toolbar
title: "Screening Halaman Activity Log dan Tooltip Toolbar Kedua Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-1
  - TC-FA-FAAL-2
coverage:
  web: automated
---

# Screening Halaman Activity Log dan Tooltip Toolbar Kedua Tab

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: tidak ada data log khusus yang diasersi; kedua tab hanya diamati strukturnya.
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-1: Screening halaman Activity Log dari menu sidebar

1. Buka Fixed Asset > Dashboard
2. Klik menu Reports & Logs di sidebar
3. Klik Activity Log
4. Verifikasi Breadcrumb tampil `Reports & Logs > Activity Log` sebagai satu breadcrumb untuk kedua tab
5. Verifikasi tidak ada segmen Breadcrumb yang bisa diklik (dua segmen)
6. Verifikasi tidak ada Page Title terpisah di bawah Breadcrumb
7. Verifikasi Tab tampil `Session | User Action`
8. Verifikasi tab Session aktif dan terbuka sebagai tab default
9. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb
10. Verifikasi Table Tools Tab Session tampil `Search | Filter | Download`
11. Verifikasi tabel tampil di bawah Toolbar
12. Verifikasi Pagination tampil di bawah tabel

### TC-FA-FAAL-2: Tooltip icon Toolbar dan header kolom Actions pada kedua tab

13. Arahkan kursor ke icon Search
14. Verifikasi tooltip `Search` tampil
15. Arahkan kursor ke icon Filter
16. Verifikasi tooltip `Filter` tampil
17. Arahkan kursor ke icon Download
18. Verifikasi tooltip `Download` tampil
19. Arahkan kursor ke header kolom Actions (⋯)
20. Verifikasi tooltip `Column Visibility` tampil
21. Klik tab User Action
22. Arahkan kursor ke icon Search
23. Verifikasi tooltip `Search` tampil
24. Arahkan kursor ke icon Filter
25. Verifikasi tooltip `Filter` tampil
26. Arahkan kursor ke icon Download
27. Verifikasi tooltip `Download` tampil
28. Arahkan kursor ke header kolom Actions (⋯)
29. Verifikasi tooltip `Column Visibility` tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (meninggalkan layar awal yang dibuka hook `beforeEach` suite ke Dashboard, karena precondition TC-FA-FAAL-1 menyebut Dashboard dan TC menguji navigasi sidebar).
- Tooltip pada langkah 14, 16, 18, 20, 23, 25, 27, 29 diasersi segera setelah kursor diarahkan sebelum elemen berikutnya disentuh (bagian 8b butir 5). Urutan tooltip pada Expected TC-FA-FAAL-2 ("berurutan") dipenuhi oleh urutan langkah.
- TC-FA-FAAL-3 dan TC-FA-FAAL-5 (screening dan urutan default Tab Session) ada di spec 063; TC-FA-FAAL-4, 6, 9, dan 261 ada di spec 002.
- Temuan untuk QA:
  - TC-FA-FAAL-2 langkah 5 ("ulangi langkah 1 sampai 4") ditulis ulang utuh pada langkah 22 sampai 29 (S-04).
