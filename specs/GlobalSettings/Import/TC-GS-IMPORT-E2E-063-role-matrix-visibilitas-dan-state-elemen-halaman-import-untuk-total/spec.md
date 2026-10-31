---
id: TC-GS-IMPORT-E2E-063-role-matrix-visibilitas-dan-state-elemen-halaman-import-untuk-total
title: "Role Matrix: Visibilitas dan State Elemen Halaman Import untuk Total Control, Default User, dan Import data (Create)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-27
  - TC-GS-IMPORT-28
  - TC-GS-IMPORT-31
coverage:
  web: automated
---

# Role Matrix: Visibilitas dan State Elemen Halaman Import untuk Total Control, Default User, dan Import data (Create)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Role yang diuji (Client A; langkah identik untuk semua role, hanya akun login yang berbeda):

| Role | Akun | Password (env) | TC |
|---|---|---|---|
| Total Control | Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` | TC-GS-IMPORT-27 |
| Default User Client A | Wahyu Nugraha `defaultUser_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DU_PASSWORD` | TC-GS-IMPORT-28 |
| Import data (Create) Client A | Rina Marlina `importCreate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_IMPORTCREATE_PASSWORD` | TC-GS-IMPORT-31 |

- Semua role, termasuk Total Control pada iterasi pertama, masuk lewat langkah 2 (ganti akun) sehingga iterasi tidak bersyarat. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A, disiapkan oleh langkah 1 dan dipulihkan oleh langkah 29 di akhir tiap iterasi lewat skrip fixture): D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter nilai sumber Brand pertama tabel D-41) dengan badge saran AI pada sel Brand Name baris #13; D-11 mock AI normal; D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk akun aktor pertama. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk ketiga akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

1. Pulihkan draft Client A ke D-09 sesuai Kontrak Fixture R2 dengan D-76 varian 1 (`created_at` dimundurkan 25 jam) lewat skrip fixture

Untuk setiap role pada tabel "Role yang diuji" (langkah 2 sampai 29):

2. Ganti akun: login sebagai akun role pada baris tabel
3. Buka menu Import dari sidebar
4. Verifikasi Navigasi Menu Import tampil
5. Verifikasi keenam Sub-Tab (Brand, Measurement, Position, Division, User Login, User Non Login) tampil
6. Verifikasi `[Changelog]` tampil
7. Verifikasi pratinjau Staging Table tampil
8. Verifikasi `[Download Template]` tampil dan Enabled
9. Verifikasi `[Upload File]` tampil dan Enabled
10. Verifikasi toggle `Edit this page` tampil dan Enabled
11. Verifikasi `[Discard]` pada Unsaved Banner tampil dan Enabled
12. Verifikasi `[Import (12)]` tampil dan Enabled
13. Verifikasi kolom Checkbox tampil
14. Centang checkbox baris #1
15. Verifikasi Bulk Action Bar tampil
16. Klik `[Bulk Action ▾]` pada Bulk Action Bar
17. Verifikasi overlay Bulk Action memuat `[Delete]` Enabled
18. Klik `[×]` pada Bulk Action Bar
19. Verifikasi Error Summary Callout menampilkan `[View Data]` Enabled
20. Verifikasi Error Summary Callout menampilkan `[Delete All Rows]` Enabled
21. Klik `[⋯]` pada baris #1
22. Verifikasi menu `[⋯]` memuat Duplicate Enabled
23. Verifikasi menu `[⋯]` memuat Edit Enabled
24. Verifikasi menu `[⋯]` memuat Remove Enabled
25. Tekan Esc untuk menutup menu
26. Klik halaman 2 pada Pagination
27. Verifikasi badge saran AI pada sel Brand Name baris #13 menampilkan `[Accept]` Enabled
28. Verifikasi badge saran AI pada sel Brand Name baris #13 menampilkan `[Dismiss]` Enabled
29. Pulihkan draft Client A ke D-09 sesuai Kontrak Fixture R2 dengan D-76 varian 1 (`created_at` dimundurkan 25 jam) lewat skrip fixture

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec Role Matrix (bagian 3a): satu daftar elemen untuk tiga role dengan hasil identik; langkah 2 sampai 29 diulang untuk tiap baris tabel (3 iterasi, ekspansi 85 langkah: langkah 1 ditambah 3 kali 28) karena langkah dan Expected identik antar-role; setiap iterasi berdiri sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (seed draft D-09 dan D-76 varian 1), langkah 2 (ganti akun), langkah 3, 14, 16, 18, 21, 25, 26 (aksi menuju keadaan yang diasersi), langkah 29 (pemulihan draft pada akhir tiap iterasi, tanpa pengecualian untuk role terakhir).
- Urutan langkah mengikuti urutan state: elemen pada pembukaan halaman (langkah 4 sampai 13) lalu Bulk Action Bar, Callout, menu `⋯`, dan badge AI.
- Pembagian TC lintas spec: elemen Disabled dan Hidden untuk Read Only dan Import data (Read Only) (TC-GS-IMPORT-29 dan 30) ada di spec 064.
- Temuan untuk QA:
  - TC-GS-IMPORT-27, 28, dan 31 menggabungkan beberapa elemen dalam satu butir Expected (b sampai f); spec memecahnya per elemen sesuai S-01.
  - Post Condition TC-GS-IMPORT-27, 28, dan 31 bertanda "-".
