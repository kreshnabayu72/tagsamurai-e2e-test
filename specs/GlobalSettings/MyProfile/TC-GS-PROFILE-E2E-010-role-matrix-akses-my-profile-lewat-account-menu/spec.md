---
id: TC-GS-PROFILE-E2E-010-role-matrix-akses-my-profile-lewat-account-menu
title: "Role Matrix: akses My Profile lewat account menu navbar per role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-50
  - TC-GS-PROFILE-55
  - TC-GS-PROFILE-60
  - TC-GS-PROFILE-65
  - TC-GS-PROFILE-70
coverage:
  web: automated
---

# Role Matrix: akses My Profile lewat account menu navbar per role

## Prerequisites

- Mode: FE+BE.
- Spec Role Matrix (bagian 3a konvensi) positif: aksi membuka My Profile berhasil untuk semua role. Spec ditulis per blok role karena langkah tiap role berbeda (app asal dan asersi tambahan User Basic) dan ganti akun menuntut Step eksplisit. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (urutan baris = urutan blok):

| Role | Pre-setup | Akun | Kondisi data | Env var password |
|---|---|---|---|---|
| Total Control | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net` | App Access Global Settings, Fixed Asset, Admin Console | `Spectra.env.GS_PROFILE_TC_PASSWORD` |
| Read Only | #2 | Rina Pratiwi, `readOnlyProfile_automated_{namaCompany}@qwertysystem.net` | App Access Global Settings dan Fixed Asset | `Spectra.env.GS_PROFILE_RO_PASSWORD` |
| System Role | #3 | Dewi Lestari, `systemRoleProfile_automated_{namaCompany}@qwertysystem.net` | tanpa Access Level, role individual "Manage user and role", App Access Global Settings dan Fixed Asset | `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD` |
| User Basic | #4 | Budi Santoso, `userBasicProfile_automated_{namaCompany}@qwertysystem.net` | 0 role individual, tanpa Access Level, App Access Fixed Asset saja (app asal Fixed Asset) | `Spectra.env.GS_PROFILE_BASIC_PASSWORD` |

- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #1) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Data Dinamis: tidak ada. Spec hanya membaca dan tidak mengubah state.

## Test Steps

### Role Total Control (TC-GS-PROFILE-50)

1. Buka halaman Global Settings selain My Profile
2. Klik icon Profile di navbar
3. Klik item `My Profile` di account menu
4. Verifikasi halaman My Profile terbuka dengan Header, Section Identity, Section Access & Status, dan Section Custom Field milik Andi Pratama

### Role Read Only (TC-GS-PROFILE-55)

5. Logout, lalu login sebagai Pre-setup #2 (Rina Pratiwi) dengan `Spectra.env.GS_PROFILE_RO_PASSWORD`
6. Klik icon Profile di navbar
7. Klik item `My Profile` di account menu
8. Verifikasi halaman My Profile terbuka dengan Header, Section Identity, Section Access & Status, dan Section Custom Field milik Rina Pratiwi

### Role System Role (TC-GS-PROFILE-60)

9. Logout, lalu login sebagai Pre-setup #3 (Dewi Lestari) dengan `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD`
10. Klik icon Profile di navbar
11. Klik item `My Profile` di account menu
12. Verifikasi halaman My Profile terbuka dengan Header, Section Identity, Section Access & Status, dan Section Custom Field milik Dewi Lestari

### Role User Basic (TC-GS-PROFILE-65, TC-GS-PROFILE-70)

13. Logout, lalu login sebagai Pre-setup #4 (Budi Santoso) dengan `Spectra.env.GS_PROFILE_BASIC_PASSWORD`; User berada di Fixed Asset (app asal)
14. Verifikasi sedikitnya satu item menu Fixed Asset tampil pada sidebar
15. Verifikasi item sidebar Global Settings Hidden untuk User Basic
16. Klik icon Profile di navbar
17. Klik item `My Profile` di account menu
18. Verifikasi halaman My Profile terbuka dengan Header, Section Identity, Section Access & Status, dan Section Custom Field milik Budi Santoso
19. Verifikasi Product Selector menampilkan `Viewing: Fixed Asset`

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-50, 55, 60, 65, 70).
- Spec ditulis per blok role (bagian 3a konvensi, keputusan 2026-10-30): ganti akun menuntut Step eksplisit dan akun pertama login di hook `before`; tiap blok tetap bermakna walau blok sebelumnya gagal.
- TC-GS-PROFILE-65 dan TC-GS-PROFILE-70 memakai akun Pre-setup #4 dalam satu kunjungan: langkah 15 adalah Expected a TC-GS-PROFILE-70; langkah 18 sekaligus Expected a TC-GS-PROFILE-65 dan Expected b TC-GS-PROFILE-70 (halaman My Profile terbuka); langkah 19 adalah Expected b TC-GS-PROFILE-65.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 membuka halaman Global Settings selain My Profile supaya pembukaan lewat account menu bermakna (hook `beforeEach` sudah membuka My Profile); langkah 5, 9, dan 13 adalah Step ganti akun.
- Judul TC-GS-PROFILE-50, 55, dan 60 menyebut "item `My Profile` ada di account menu"; item itu dibuktikan lewat klik pada langkah 3, 7, dan 11 dan tidak diasersi terpisah karena Expected TC hanya memuat halaman terbuka (S-02).
- Asersi `Hidden` sidebar (langkah 15) didahului `Verifikasi` item sidebar lain tampil (langkah 14) sebagai anchor.
- Temuan untuk QA:
  - TC-GS-PROFILE-50, 55, 60, dan 65 tidak menyebut halaman asal dan Expected tentang item `My Profile` di account menu hanya ada pada judul; spec membuktikan item lewat klik.
  - TC-GS-PROFILE-70 tidak menyebut item sidebar lain yang tampil sebagai anchor absence; spec memakai item menu Fixed Asset secara umum.
