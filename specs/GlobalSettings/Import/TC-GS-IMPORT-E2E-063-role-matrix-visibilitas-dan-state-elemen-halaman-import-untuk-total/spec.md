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

- Login role pertama (Total Control) di hook `before`; role berikutnya lewat langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap role): D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter nilai sumber Brand pertama tabel D-41) dengan badge saran AI pada sel Brand Name baris #13; D-11 mock AI normal; D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk akun aktor pertama. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk ketiga akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

Untuk setiap role pada tabel "Role yang diuji" (langkah 1 sampai 28):

1. Ganti akun: login sebagai akun role pada baris tabel (role pertama sudah login di hook `before`)
2. Buka menu Import dari sidebar
3. Verifikasi Navigasi Menu Import tampil
4. Verifikasi keenam Sub-Tab (Brand, Measurement, Position, Division, User Login, User Non Login) tampil
5. Verifikasi `[Changelog]` tampil
6. Verifikasi pratinjau Staging Table tampil
7. Verifikasi `[Download Template]` tampil dan Enabled
8. Verifikasi `[Upload File]` tampil dan Enabled
9. Verifikasi toggle `Edit this page` tampil dan Enabled
10. Verifikasi `[Discard]` pada Unsaved Banner tampil dan Enabled
11. Verifikasi `[Import (12)]` tampil dan Enabled
12. Verifikasi kolom Checkbox tampil
13. Centang checkbox baris #1
14. Verifikasi Bulk Action Bar tampil
15. Klik `[Bulk Action ▾]` pada Bulk Action Bar
16. Verifikasi overlay Bulk Action memuat `[Delete]` Enabled
17. Klik `[×]` pada Bulk Action Bar
18. Verifikasi Error Summary Callout menampilkan `[View Data]` Enabled
19. Verifikasi Error Summary Callout menampilkan `[Delete All Rows]` Enabled
20. Klik `[⋯]` pada baris #1
21. Verifikasi menu `[⋯]` memuat Duplicate Enabled
22. Verifikasi menu `[⋯]` memuat Edit Enabled
23. Verifikasi menu `[⋯]` memuat Remove Enabled
24. Tekan Esc untuk menutup menu
25. Klik halaman 2 pada Pagination
26. Verifikasi badge saran AI pada sel Brand Name baris #13 menampilkan `[Accept]` Enabled
27. Verifikasi badge saran AI pada sel Brand Name baris #13 menampilkan `[Dismiss]` Enabled
28. Pulihkan draft Client A ke D-09 sesuai Kontrak Fixture R2 (hanya antar-role)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec Role Matrix (bagian 3a): satu daftar elemen untuk tiga role dengan hasil identik; langkah 1 sampai 28 diulang untuk tiap baris tabel (3 iterasi, ekspansi sekitar 84 langkah) karena langkah dan Expected identik antar-role; setiap iterasi berdiri sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ganti akun), langkah 2, 13, 15, 17, 20, 24, 25 (aksi menuju keadaan yang diasersi), langkah 28 (pemulihan draft).
- Urutan langkah mengikuti urutan state: elemen pada pembukaan halaman (langkah 3 sampai 12) lalu Bulk Action Bar, Callout, menu `⋯`, dan badge AI.
- Pembagian TC lintas spec: elemen Disabled dan Hidden untuk Read Only dan Import data (Read Only) (TC-GS-IMPORT-29 dan 30) ada di spec 064.
- Temuan untuk QA:
  - TC-GS-IMPORT-27, 28, dan 31 menggabungkan beberapa elemen dalam satu butir Expected (b sampai f); spec memecahnya per elemen sesuai S-01.
  - Post Condition TC-GS-IMPORT-27, 28, dan 31 bertanda "-".
