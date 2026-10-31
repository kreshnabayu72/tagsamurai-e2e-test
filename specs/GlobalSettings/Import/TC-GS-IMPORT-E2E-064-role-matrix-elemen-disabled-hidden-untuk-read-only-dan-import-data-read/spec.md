---
id: TC-GS-IMPORT-E2E-064-role-matrix-elemen-disabled-hidden-untuk-read-only-dan-import-data-read
title: "Role Matrix: Elemen Disabled dan Hidden untuk Read Only dan Import data (Read Only) pada Halaman Import"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-29
  - TC-GS-IMPORT-30
coverage:
  web: automated
---

# Role Matrix: Elemen Disabled dan Hidden untuk Read Only dan Import data (Read Only) pada Halaman Import

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Role yang diuji (Client A; langkah identik, hanya akun login yang berbeda):

| Role | Akun | Password (env) | TC |
|---|---|---|---|
| Read Only Client A | Maya Putri `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` | TC-GS-IMPORT-29 |
| Import data (Read Only) Client A | Tono Hartono `importRead_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_IMPORTRO_PASSWORD` | TC-GS-IMPORT-30 |

- Kedua role login lewat langkah ganti akun (langkah 2) dari akun default suite (Total Control Client A). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A): D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter nilai sumber Brand pertama tabel D-41) dengan badge saran AI pada sel Brand Name baris #13, dipulihkan oleh hook `beforeEach` suite sebagai draft dasar; D-11 mock AI normal; D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil, disiapkan oleh langkah 1.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun default suite; kedua role masuk lewat langkah 2. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

1. Seed D-76 varian 1 pada draft D-09 Client A lewat skrip fixture (mundurkan `created_at` 25 jam)

Untuk setiap role pada tabel "Role yang diuji" (langkah 2 sampai 34):

2. Ganti akun: login sebagai akun role pada baris tabel
3. Buka menu Import dari sidebar
4. Verifikasi Navigasi Menu Import tampil
5. Verifikasi keenam Sub-Tab (Brand, Measurement, Position, Division, User Login, User Non Login) tampil
6. Verifikasi `[Changelog]` tampil
7. Verifikasi pratinjau Staging Table tampil
8. Verifikasi `[Download Template]` Enabled
9. Verifikasi `[View Data]` pada Error Summary Callout Enabled
10. Verifikasi kolom Checkbox tidak dirender (Hidden)
11. Verifikasi Bulk Action Bar tidak tersedia
12. Hover `[Upload File]`
13. Verifikasi `[Upload File]` Disabled dengan tooltip "You don't have permission to do this."
14. Hover toggle `Edit this page`
15. Verifikasi toggle `Edit this page` Disabled dengan tooltip "You don't have permission to do this."
16. Klik `[⋯]` pada baris #1
17. Hover item Duplicate
18. Verifikasi item Duplicate pada menu `[⋯]` Disabled dengan tooltip "You don't have permission to do this."
19. Hover item Edit
20. Verifikasi item Edit pada menu `[⋯]` Disabled dengan tooltip "You don't have permission to do this."
21. Hover item Remove
22. Verifikasi item Remove pada menu `[⋯]` Disabled dengan tooltip "You don't have permission to do this."
23. Tekan Esc untuk menutup menu
24. Klik halaman 2 pada Pagination
25. Hover `[Accept]` pada badge saran AI baris #13
26. Verifikasi `[Accept]` pada badge saran AI baris #13 Disabled dengan tooltip "You don't have permission to do this."
27. Hover `[Dismiss]` pada badge saran AI baris #13
28. Verifikasi `[Dismiss]` pada badge saran AI baris #13 Disabled dengan tooltip "You don't have permission to do this."
29. Hover `[Delete All Rows]` pada Error Summary Callout
30. Verifikasi `[Delete All Rows]` pada Error Summary Callout Disabled dengan tooltip "You don't have permission to do this."
31. Hover `[Discard]` pada Unsaved Banner
32. Verifikasi `[Discard]` pada Unsaved Banner Disabled dengan tooltip "You don't have permission to do this."
33. Hover `[Import (12)]`
34. Verifikasi `[Import (12)]` Disabled dengan tooltip "You don't have permission to do this."

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec Role Matrix (bagian 3a): satu daftar elemen untuk dua role dengan hasil identik; langkah 1 dijalankan sekali, langkah 2 sampai 34 diulang untuk tiap baris tabel (2 iterasi, ekspansi 67 langkah). Spec di atas smell 35 langkah; alasan: langkah identik antar-role dan tiap iterasi berdiri sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (seed fixture), langkah 2 (ganti akun), langkah 3, 16, 23, 24 (aksi menuju keadaan yang diasersi). Tidak ada langkah pemulihan antar-role: tidak ada langkah yang mengubah draft (hover, Esc, dan Pagination hanya mengubah tampilan), dan langkah 2 memuat sesi baru tiap iterasi.
- Hover pada langkah 12, 14, 17, 19, 21, 25, 27, 29, 31, 33 mendahului `Verifikasi` tooltip sesuai 8b butir 5 (state sementara diasersi sebelum langkah yang mengubahnya).
- Pembagian TC lintas spec: elemen Enabled untuk Total Control, Default User, dan Import data (Create) ada di spec 063.
- Temuan untuk QA:
  - TC-GS-IMPORT-29 dan 30 menggabungkan beberapa elemen dalam satu butir Expected (a sampai c); spec memecahnya per elemen sesuai S-01.
