---
id: TC-FA-CF-E2E-012-role-matrix-visibilitas-pemegang-read-create-update
title: "Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Read, Create, Update)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-36
  - TC-FA-CF-37
  - TC-FA-CF-38
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Read, Create, Update)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Company Alpha, `{namaCompany}` = Company Alpha; capability Manage asset master data; password tidak ditulis di spec atau fixture):

| Role | Akun (Pre-setup) | Env password | Dipakai di langkah |
|---|---|---|---|
| Master-Read (Read saja) | #4 `masterRead_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini | `Spectra.env.FA_MR_PASSWORD` | 1 sampai 7 |
| Master-Create (Create dan Read) | #5 `masterCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MC_PASSWORD` | 8 sampai 17 |
| Master-Update (Update dan Read) | #6 `masterUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MU_PASSWORD` | 18 sampai 32 |

- Halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite untuk akun pertama; hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Nama env baru (`FA_MR_PASSWORD`, `FA_MC_PASSWORD`, `FA_MU_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12; dipakai: baris `Asset Serial Tag`, Active), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: hover.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk setiap akun aktor yang dipakai spec dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-36: Visibilitas elemen UI untuk pemegang Read saja

1. Verifikasi menu dan tab tampil
2. Verifikasi tombol `[+ Custom Field]` Hidden
3. Verifikasi row action `Edit` dan `Delete` Hidden
4. Arahkan kursor ke switch Active baris `Asset Serial Tag`
5. Verifikasi switch Active tampil Disabled dengan tooltip `You don't have permission to do this.`
6. Verifikasi kolom Checkbox baris dan Bulk Action Bar Hidden
7. Verifikasi toolbar Search, Download, dan Changelog tampil

### TC-FA-CF-37: Visibilitas elemen UI untuk pemegang Create

8. Ganti akun: Logout dari akun Master-Read
9. Login sebagai Master-Create (Pre-setup #5) dengan `Spectra.env.FA_MC_PASSWORD`
10. Buka Fixed Asset > Settings > Custom Fields (tab General)
11. Verifikasi menu dan tab tampil
12. Verifikasi tombol `[+ Custom Field]` tampil
13. Verifikasi row action `Edit` dan `Delete` Hidden
14. Arahkan kursor ke switch Active baris `Asset Serial Tag`
15. Verifikasi switch Active tampil Disabled dengan tooltip `You don't have permission to do this.`
16. Verifikasi kolom Checkbox baris dan Bulk Action Bar Hidden
17. Verifikasi toolbar Search, Download, dan Changelog tampil

### TC-FA-CF-38: Visibilitas elemen UI untuk pemegang Update

18. Ganti akun: Logout dari akun Master-Create
19. Login sebagai Master-Update (Pre-setup #6) dengan `Spectra.env.FA_MU_PASSWORD`
20. Buka Fixed Asset > Settings > Custom Fields (tab General)
21. Verifikasi menu dan tab tampil
22. Verifikasi tombol `[+ Custom Field]` Hidden
23. Buka menu row action baris `Asset Serial Tag`
24. Verifikasi row action `Edit` tampil
25. Verifikasi row action `Delete` Hidden
26. Tutup menu row action dengan menekan `Esc`
27. Verifikasi switch Active tampil Enabled
28. Verifikasi checkbox baris tampil
29. Centang baris `Asset Serial Tag`
30. Verifikasi Bulk Action Bar memuat `[Activate]`/`[Deactivate]` sesuai komposisi seleksi
31. Verifikasi Bulk Action Bar tidak memuat `[Delete]`
32. Verifikasi toolbar Search, Download, dan Changelog tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec hanya membaca; subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`) dan hasil per role berbeda (bagian 3a, S-07). Title spec tidak memakai kata "Positif" atau "Negatif" karena memuat kedua polaritas.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4, 14 (hover agar tooltip switch Disabled teramati), langkah 8 sampai 10 dan 18 sampai 20 (ganti akun, login, dan membuka halaman), langkah 23 dan 26 (membuka dan menutup menu row action), dan langkah 29 (mencentang baris; Langkah Uji TC "Centang satu baris bila checkbox tampil"). Pada blok Master-Read dan Master-Create tidak ada baris yang dicentang karena kolom Checkbox Hidden.
- Absence Hidden pada langkah 2, 3, 6, 13, 16, 22, 25, dan 31 beranchor Verifikasi menu, tab, dan toolbar yang tampil pada blok yang sama (8b butir 2, elemen UI Role Matrix; langkah 31 beranchor langkah 30).
- Langkah 24 dan 25 memecah Expected c TC-FA-CF-38 ("Edit tampil dan Delete Hidden") menjadi dua klausa; langkah 30 dan 31 memecah Expected e.
- Temuan untuk QA:
  - TC-FA-CF-38 Expected e menyebut Bulk Action Bar memuat `[Activate]`/`[Deactivate]` "sesuai komposisi seleksi" tanpa menyebut tombol yang tampil untuk seleksi satu baris Active (`Asset Serial Tag`); spec mengikuti teks TC dan tombol yang tepat ditentukan penulis skrip dari PRD.
  - Post Condition tiga TC kosong (`-`); tidak ada yang dicatat.
