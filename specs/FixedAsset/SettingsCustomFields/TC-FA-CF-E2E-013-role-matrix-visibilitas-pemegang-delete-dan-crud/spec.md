---
id: TC-FA-CF-E2E-013-role-matrix-visibilitas-pemegang-delete-dan-crud
title: "Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Delete, Create-Update-Delete)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-39
  - TC-FA-CF-40
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Delete, Create-Update-Delete)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Company Alpha, `{namaCompany}` = Company Alpha; capability Manage asset master data; password tidak ditulis di spec atau fixture):

| Role | Akun (Pre-setup) | Env password | Dipakai di langkah |
|---|---|---|---|
| Master-Delete (Delete dan Read) | #7 `masterDelete_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini | `Spectra.env.FA_MD_PASSWORD` | 1 sampai 13 |
| Master-Crud (Create, Read, Update, Delete) | #8 `masterCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MCRUD_PASSWORD` | 14 sampai 26 |

- Halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite untuk akun pertama; hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Nama env baru (`FA_MD_PASSWORD`, `FA_MCRUD_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12; dipakai: baris `Asset Serial Tag`, Active), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: hover.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk setiap akun aktor yang dipakai spec dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-39: Visibilitas elemen UI untuk pemegang Delete

1. Verifikasi menu dan tab tampil
2. Verifikasi tombol `[+ Custom Field]` Hidden
3. Buka menu row action baris `Asset Serial Tag`
4. Verifikasi row action `Delete` tampil
5. Verifikasi row action `Edit` Hidden
6. Tutup menu row action dengan menekan `Esc`
7. Arahkan kursor ke switch Active baris `Asset Serial Tag`
8. Verifikasi switch Active tampil Disabled dengan tooltip `You don't have permission to do this.`
9. Verifikasi checkbox baris tampil
10. Centang baris `Asset Serial Tag`
11. Verifikasi Bulk Action Bar memuat `[Delete]`
12. Verifikasi Bulk Action Bar tidak memuat `[Activate]` maupun `[Deactivate]`
13. Verifikasi toolbar Search, Download, dan Changelog tampil

### TC-FA-CF-40: Visibilitas elemen UI untuk pemegang Create, Update, dan Delete

14. Ganti akun: Logout dari akun Master-Delete
15. Login sebagai Master-Crud (Pre-setup #8) dengan `Spectra.env.FA_MCRUD_PASSWORD`
16. Buka Fixed Asset > Settings > Custom Fields (tab General)
17. Verifikasi menu dan tab tampil
18. Verifikasi tombol `[+ Custom Field]` tampil
19. Buka menu row action baris `Asset Serial Tag`
20. Verifikasi row action `Edit` dan `Delete` tampil
21. Tutup menu row action dengan menekan `Esc`
22. Verifikasi switch Active tampil Enabled
23. Verifikasi checkbox baris tampil
24. Centang baris `Asset Serial Tag`
25. Verifikasi Bulk Action Bar memuat `[Activate]`, `[Deactivate]`, dan `[Delete]` sesuai komposisi seleksi
26. Verifikasi toolbar Search, Download, dan Changelog tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec hanya membaca; subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`) dan hasil per role berbeda (bagian 3a, S-07). Title spec tidak memakai kata "Positif" atau "Negatif" karena memuat kedua polaritas.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 dan 6, 19 dan 21 (membuka dan menutup menu row action), langkah 7 (hover agar tooltip switch Disabled teramati), langkah 10 dan 24 (mencentang baris; Langkah Uji TC "Centang satu baris bila checkbox tampil"), serta langkah 14 sampai 16 (ganti akun, login, dan membuka halaman).
- Absence Hidden pada langkah 2, 5, dan 12 beranchor Verifikasi menu, tab, dan toolbar yang tampil pada blok yang sama (8b butir 2, elemen UI Role Matrix; langkah 12 beranchor langkah 11).
- Langkah 11 dan 12 memecah Expected e TC-FA-CF-39 menjadi dua klausa.
- Temuan untuk QA:
  - TC-FA-CF-40 Expected e menyebut tiga tombol bulk "sesuai komposisi seleksi" tanpa menyebut komposisi untuk seleksi satu baris Active (`Asset Serial Tag`); spec mengikuti teks TC dan komposisi yang tepat ditentukan penulis skrip dari PRD.
  - Post Condition dua TC kosong (`-`); tidak ada yang dicatat.
