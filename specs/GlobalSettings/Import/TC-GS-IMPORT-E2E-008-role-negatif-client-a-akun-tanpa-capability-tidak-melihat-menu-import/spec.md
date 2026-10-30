---
id: TC-GS-IMPORT-E2E-008-role-negatif-client-a-akun-tanpa-capability-tidak-melihat-menu-import
title: "Role Negatif Client A: Akun Tanpa Capability Tidak Melihat Menu Import; Read Only dan Import data (Read Only) Tidak Dapat Memulai Sesi Edit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-26
  - TC-GS-IMPORT-595
  - TC-GS-IMPORT-596
coverage:
  web: automated
---

# Role Negatif Client A: Akun Tanpa Capability Tidak Melihat Menu Import; Read Only dan Import data (Read Only) Tidak Dapat Memulai Sesi Edit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor (Client A):
  - Tanpa Capability (Fajar Nugroho) `noCapability_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-26. Login sekali di hook `before` dengan `Spectra.env.GS_NOCAP_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Tabel "Role yang diuji" untuk TC-GS-IMPORT-595 dan 596 (langkah identik, hanya akun berbeda; login lewat langkah ganti akun eksplisit):

    | Role | Email | Env var password |
    |---|---|---|
    | Read Only Client A (Maya Putri) | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` (env baru) |
    | Import data (Read Only) Client A (Tono Hartono) | `importRead_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_IMPORTRO_PASSWORD` (env baru) |

  - Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: spec menguji menu Import dari sidebar dan route langsung sehingga membuka halaman lewat langkah sendiri.
- Data Dinamis: D-01 draft Brand 12 baris `pending` (`brand-12.csv`) pada Client A, disiapkan skrip fixture di hook `before` dan dipulihkan hook `beforeEach` (Kontrak Fixture R2). Spec hanya membaca draft, tidak mengubahnya.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk ketiga akun, lihat `suite.md`.
- Kemampuan teknis: membuka alamat route Import langsung lewat browser; skrip seed/reset draft (disediakan tim FE/BE); ganti akun.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-26: Akun tanpa kapabilitas Import tidak melihat menu Import

1. Perhatikan sidebar Global Settings (User berada di Global Settings)
2. Verifikasi item menu lain pada sidebar Global Settings tampil
3. Verifikasi menu Import tidak tampil di sidebar (Hidden)
4. Buka alamat route halaman Import langsung lewat browser
5. Perhatikan halaman dan toast
6. Verifikasi tampil toast error "You don't have permission to do this."
7. Verifikasi halaman tidak memuat data Staging Table
8. Verifikasi tidak ada pengalihan halaman

### TC-GS-IMPORT-595 dan TC-GS-IMPORT-596: Read Only dan Import data (Read Only) tidak dapat memulai sesi edit

Untuk setiap baris tabel "Role yang diuji" (langkah 9 sampai 33; Read Only Client A untuk TC-GS-IMPORT-595, lalu Import data (Read Only) Client A untuk TC-GS-IMPORT-596):

9. Ganti akun: logout dari akun sebelumnya, login sebagai role pada baris tabel dengan env var passwordnya
10. Buka menu Import dari sidebar
11. Klik sel Brand Name baris #1
12. Perhatikan tabel dan footer
13. Verifikasi sel Brand Name baris #1 tidak berubah menjadi input dan tidak ada sesi edit
14. Verifikasi footer tetap menampilkan `[Import (12)]` tanpa `[Cancel]` dan `[Save]`
15. Verifikasi kolom Actions tetap tampil
16. Klik `[⋯]` pada baris #1
17. Klik item Edit
18. Perhatikan tabel dan footer
19. Verifikasi baris #1 tidak berubah menjadi input dan tidak ada sesi edit
20. Verifikasi footer tetap menampilkan `[Import (12)]` tanpa `[Cancel]` dan `[Save]`
21. Verifikasi kolom Actions tetap tampil
22. Klik `[⋯]` pada baris #1
23. Klik item Duplicate
24. Perhatikan tabel dan footer
25. Verifikasi tidak ada baris hasil Duplicate dan tidak ada sesi edit
26. Verifikasi footer tetap menampilkan `[Import (12)]` tanpa `[Cancel]` dan `[Save]`
27. Verifikasi kolom Actions tetap tampil
28. Klik toggle `Edit this page`
29. Perhatikan tabel dan footer
30. Verifikasi toggle `Edit this page` tetap OFF dan tidak ada sesi edit
31. Verifikasi footer tetap menampilkan `[Import (12)]` tanpa `[Cancel]` dan `[Save]`
32. Verifikasi kolom Actions tetap tampil
33. Verifikasi Staging Metric Cards: Total Rows 12 (draft Brand tetap 12 baris `pending` tanpa perubahan)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Langkah 9 sampai 33 dijalankan dua kali (Read Only lalu Import data (Read Only)); ekspansi 25 langkah x 2 = 50 langkah, ditambah 8 langkah TC-GS-IMPORT-26 = 58 langkah. Parameter tiap iterasi ada di tabel "Role yang diuji"; nomor langkah yang diulang: 9 sampai 33 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: langkah per role identik (Role Matrix negatif, konvensi 3a) dan ekspansinya hanya mengulang blok homogen; kegagalan satu role tidak menghilangkan makna role lain.
- TC-GS-IMPORT-26 (akun Tanpa Capability) tidak digabung ke tabel karena langkahnya berbeda (menu tidak tampil dan route langsung); diletakkan lebih dulu karena akun pertama login di hook `before` (S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 5, 12, 18, 24, 29 (mengamati sesuai Langkah Uji TC), langkah 9 dan 10 (ganti akun dan buka menu). Langkah 2 adalah asersi tambahan sebagai anchor positif untuk absence menu Import (konvensi 8b butir 2) dan tidak ada di Expected TC-GS-IMPORT-26 (S-03). Langkah 33 adalah asersi Post Condition TC-GS-IMPORT-595/596 ("Draft tetap berisi 12 baris pending") yang punya padanan pada Staging Metric Cards yang sama dengan Expected.
- Temuan untuk QA:
  - Post Condition TC-GS-IMPORT-595 dan 596 ("Draft Brand tetap berisi 12 baris pending tanpa perubahan") diasersi lewat Staging Metric Cards Total Rows 12 saja; TC tidak memberi langkah observasi lain.
  - TC-GS-IMPORT-26 mensyaratkan Client A memiliki draft D-01 tetapi tidak mengasersi isinya; seed draft memakai skrip fixture yang disediakan tim FE/BE (S-13). Nama data literal Population tanpa suffix `{runId}`.
