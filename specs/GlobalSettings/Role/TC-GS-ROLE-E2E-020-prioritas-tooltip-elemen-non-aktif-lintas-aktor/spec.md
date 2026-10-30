---
id: TC-GS-ROLE-E2E-020-prioritas-tooltip-elemen-non-aktif-lintas-aktor
title: "Role Matrix: Prioritas Tooltip Elemen Non-Aktif pada Baris Default User Lintas Aktor"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-44
  - TC-GS-ROLE-45
  - TC-GS-ROLE-46
coverage:
  web: automated
---

# Role Matrix: Prioritas Tooltip Elemen Non-Aktif pada Baris Default User Lintas Aktor

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data; hanya hover dan membuka overlay.
- Langkah tiap aktor berbeda (Detail saja, Detail lalu Tab Total Control, dan dua elemen Detail), sehingga spec ditulis sebagai blok per aktor. Login aktor pertama (Siti Nurhaliza) dilakukan di hook `before`; aktor berikutnya memakai langkah ganti akun eksplisit. Password tidak ditulis di spec atau fixture.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-44 | Read Only (Active, punya baris Manage TAG) | Siti Nurhaliza | disediakan tim FE | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-ROLE-45 | Total Control, Default User | Budi Santoso | `defaultUserGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_DEFAULT_PASSWORD` |
| TC-GS-ROLE-46 | Manage user and role C/R/U/D (punya baris Manage TAG) | Hendra Wijaya | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` |

- Environment variable: `GS_RO_PASSWORD`, `GS_DEFAULT_PASSWORD`; env baru `GS_ROLE_MANAGE_CRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE).
- Data Pre-setup (hanya dibaca): Budi Santoso (Default User, Pre-setup #2) punya baris di Detail "Manage TAG" dan di Tab Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Hook `after`: mengembalikan sesi ke akun default suite (Ahmad Fauzi, `GS_TC_PASSWORD`) karena spec berakhir di akun Hendra Wijaya.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: mengarahkan kursor ke checkbox disabled dan ke item overlay untuk membaca tooltip.

## Test Steps

### TC-GS-ROLE-44: Prioritas tooltip, aktor Read Only pada baris Default User

1. Buka Detail "Manage TAG"
2. Arahkan kursor ke checkbox Update baris Budi Santoso
3. Verifikasi tooltip `Read Only access cannot modify data.`

### TC-GS-ROLE-45: Prioritas tooltip, Default User melihat barisnya sendiri

4. Logout, lalu login sebagai Budi Santoso (Default User)
5. Buka Detail "Manage TAG"
6. Arahkan kursor ke checkbox Update baris Budi Santoso
7. Verifikasi checkbox Update baris Budi Santoso disabled
8. Verifikasi tooltip `Default User cannot be modified.`
9. Arahkan kursor ke checkbox Remove baris Budi Santoso
10. Verifikasi checkbox Remove baris Budi Santoso disabled
11. Verifikasi tooltip `Default User cannot be modified.`
12. Arahkan kursor ke checkbox seleksi baris Budi Santoso
13. Verifikasi checkbox seleksi baris Budi Santoso disabled
14. Verifikasi tooltip `Default User cannot be modified.`
15. Buka Tab Total Control
16. Buka overlay (⋯) baris Budi Santoso
17. Arahkan kursor ke Remove
18. Verifikasi Remove disabled
19. Verifikasi tooltip `Default User cannot be modified.`
20. Tekan Esc untuk menutup overlay

### TC-GS-ROLE-46: Prioritas tooltip, aktor Manage user and role C/R/U/D pada Default User

21. Logout, lalu login sebagai Hendra Wijaya
22. Buka Detail "Manage TAG"
23. Arahkan kursor ke checkbox Update baris Budi Santoso
24. Verifikasi tooltip `Default User cannot be modified.`
25. Arahkan kursor ke checkbox Remove baris Budi Santoso
26. Verifikasi tooltip `Default User cannot be modified.`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): logout lalu login ke aktor berikutnya (langkah 4 dan 21), membuka Tab Total Control (langkah 15), dan menutup overlay dengan Esc (langkah 20).
- Expected TC-GS-ROLE-44 dan TC-GS-ROLE-46 menyebut teks tooltip yang tidak boleh muncul ("Default User cannot be modified." pada aktor Read Only; "You don't have permission to edit." pada aktor Manage user and role); asersi teks tooltip persis pada langkah 3, 24, dan 26 sudah memastikan teks lain tidak tampil, sehingga tidak ada `Verifikasi` negatif terpisah.
- Pembagian TC lintas spec: TC-GS-ROLE-41, 42, 43 (guard Default User dan diri sendiri) ada di spec 019; TC-GS-ROLE-47, 48 ada di spec 021.
- Temuan untuk QA:
  - TC-GS-ROLE-45 langkah 2 ("hover Remove baris Budi Santoso" di Tab Total Control) tidak menyebut overlay; spec membuka overlay `(⋯)` mengikuti TC-GS-ROLE-42 karena Remove Tab Total Control berada di overlay.
  - TC-GS-ROLE-46 Expected tidak menyebut apakah checkbox Update dan Remove disabled; spec hanya memverifikasi teks tooltip.
