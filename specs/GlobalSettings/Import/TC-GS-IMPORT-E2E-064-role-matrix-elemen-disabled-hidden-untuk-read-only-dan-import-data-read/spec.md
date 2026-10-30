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

- Login role pertama (Read Only) di hook `before`; role kedua lewat langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap role): D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter nilai sumber Brand pertama tabel D-41) dengan badge saran AI pada sel Brand Name baris #13; D-11 mock AI normal; D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk akun aktor pertama. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

Untuk setiap role pada tabel "Role yang diuji" (langkah 1 sampai 34):

1. Ganti akun: login sebagai akun role pada baris tabel (role pertama sudah login di hook `before`)
2. Buka menu Import dari sidebar
3. Verifikasi Navigasi Menu Import tampil
4. Verifikasi keenam Sub-Tab (Brand, Measurement, Position, Division, User Login, User Non Login) tampil
5. Verifikasi `[Changelog]` tampil
6. Verifikasi pratinjau Staging Table tampil
7. Verifikasi `[Download Template]` Enabled
8. Verifikasi `[View Data]` pada Error Summary Callout Enabled
9. Verifikasi kolom Checkbox tidak dirender (Hidden)
10. Verifikasi Bulk Action Bar tidak tersedia
11. Hover `[Upload File]`
12. Verifikasi `[Upload File]` Disabled dengan tooltip "You don't have permission to do this."
13. Hover toggle `Edit this page`
14. Verifikasi toggle `Edit this page` Disabled dengan tooltip "You don't have permission to do this."
15. Klik `[⋯]` pada baris #1
16. Hover item Duplicate
17. Verifikasi item Duplicate pada menu `[⋯]` Disabled dengan tooltip "You don't have permission to do this."
18. Hover item Edit
19. Verifikasi item Edit pada menu `[⋯]` Disabled dengan tooltip "You don't have permission to do this."
20. Hover item Remove
21. Verifikasi item Remove pada menu `[⋯]` Disabled dengan tooltip "You don't have permission to do this."
22. Tekan Esc untuk menutup menu
23. Klik halaman 2 pada Pagination
24. Hover `[Accept]` pada badge saran AI baris #13
25. Verifikasi `[Accept]` pada badge saran AI baris #13 Disabled dengan tooltip "You don't have permission to do this."
26. Hover `[Dismiss]` pada badge saran AI baris #13
27. Verifikasi `[Dismiss]` pada badge saran AI baris #13 Disabled dengan tooltip "You don't have permission to do this."
28. Hover `[Delete All Rows]` pada Error Summary Callout
29. Verifikasi `[Delete All Rows]` pada Error Summary Callout Disabled dengan tooltip "You don't have permission to do this."
30. Hover `[Discard]` pada Unsaved Banner
31. Verifikasi `[Discard]` pada Unsaved Banner Disabled dengan tooltip "You don't have permission to do this."
32. Hover `[Import (12)]`
33. Verifikasi `[Import (12)]` Disabled dengan tooltip "You don't have permission to do this."
34. Pulihkan draft Client A ke D-09 sesuai Kontrak Fixture R2 (hanya antar-role)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec Role Matrix (bagian 3a): satu daftar elemen untuk dua role dengan hasil identik; langkah 1 sampai 34 diulang untuk tiap baris tabel (2 iterasi, ekspansi sekitar 68 langkah). Spec di atas smell 35 langkah; alasan: langkah identik antar-role dan tiap iterasi berdiri sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ganti akun), langkah 2, 15, 22, 23 (aksi menuju keadaan yang diasersi), langkah 34 (pemulihan draft).
- Hover pada langkah 11, 13, 16, 18, 20, 24, 26, 28, 30, 32 mendahului `Verifikasi` tooltip sesuai 8b butir 5 (state sementara diasersi sebelum langkah yang mengubahnya).
- Pembagian TC lintas spec: elemen Enabled untuk Total Control, Default User, dan Import data (Create) ada di spec 063.
- Temuan untuk QA:
  - TC-GS-IMPORT-29 dan 30 menggabungkan beberapa elemen dalam satu butir Expected (a sampai c); spec memecahnya per elemen sesuai S-01.
