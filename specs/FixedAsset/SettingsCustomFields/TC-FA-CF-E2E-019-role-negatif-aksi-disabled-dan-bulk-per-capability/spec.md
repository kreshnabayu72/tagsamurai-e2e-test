---
id: TC-FA-CF-E2E-019-role-negatif-aksi-disabled-dan-bulk-per-capability
title: "Role Negatif: Switch Disabled Read Only dan Tombol Bulk per Capability"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-48
  - TC-FA-CF-50
coverage:
  web: automated
---

# Role Negatif: Switch Disabled Read Only dan Tombol Bulk per Capability

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Company Alpha, `{namaCompany}` = Company Alpha; password tidak ditulis di spec atau fixture):

| Role | Akun (Pre-setup) | Env password | Dipakai di langkah |
|---|---|---|---|
| Read Only | #3 `readOnly_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini | `Spectra.env.FA_RO_PASSWORD` | 1 sampai 6 |
| Master-Update (Update dan Read) | #6 `masterUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MU_PASSWORD` | 8 sampai 12 |

- Halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite untuk akun pertama; hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Nama env baru (`FA_RO_PASSWORD`, `FA_MU_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12; dipakai: `Asset Serial Tag` Active dan `Depreciated Ratio` Inactive), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: hover; fokus keyboard (Tab).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk setiap akun aktor yang dipakai spec dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-48: Switch Disabled bagi Read Only menampilkan tooltip izin

1. Arahkan kursor ke switch Active baris `Asset Serial Tag`
2. Verifikasi switch tetap tampil (visible) namun berstatus disabled
3. Verifikasi tooltip `You don't have permission to do this.` tampil saat hover
4. Pindahkan kursor keluar dari switch lalu pindahkan fokus keyboard ke switch yang sama
5. Verifikasi tooltip `You don't have permission to do this.` tampil saat fokus keyboard
6. Klik switch Active baris `Asset Serial Tag`
7. Verifikasi switch tidak dapat digeser dan tetap pada posisi ON

### TC-FA-CF-50: Pemegang Update memisah tombol bulk menurut capability pada seleksi campuran

8. Ganti akun: Logout dari akun Read Only
9. Login sebagai Master-Update (Pre-setup #6) dengan `Spectra.env.FA_MU_PASSWORD` dan buka Fixed Asset > Settings > Custom Fields (tab General)
10. Centang baris `Asset Serial Tag` (Active) dan `Depreciated Ratio` (Inactive)
11. Verifikasi tombol `[Activate]` dan `[Deactivate]` tampil bersamaan pada Bulk Action Bar
12. Verifikasi tombol `[Delete]` Hidden pada Bulk Action Bar bagi pemegang Update

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec negatif per topik aksi tidak tersedia atau dibatasi per capability (bagian 3a); subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 48 (Read Only, akun pertama di hook `before`) lalu 50 (Master-Update setelah Ganti akun, langkah 8 dan 9; S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (melepas hover dan memindah fokus keyboard supaya tooltip fokus teramati terpisah dari hover), langkah 6 (mencoba menggeser switch agar Expected c TC-FA-CF-48 teramati), dan langkah 10 (mencentang dua baris sesuai Langkah Uji TC).
- Langkah 7 mengasersi "Switch tidak dapat digeser" sebagai switch tetap pada posisi ON setelah klik (Expected c TC-FA-CF-48); Langkah Uji TC tidak memuat langkah klik, sehingga langkah 6 ditambahkan sebagai langkah penghubung.
- Langkah 12 (absence `[Delete]`) beranchor langkah 11 (bar tampil dengan tombol lain).
- Temuan untuk QA:
  - TC-FA-CF-48 Expected c ("Switch tidak dapat digeser") tidak punya langkah klik di Langkah Uji; spec menambahkan klik sebagai langkah penghubung untuk membuat asersi teramati.
  - TC-FA-CF-50 Langkah Uji menyebut keadaan `Depreciated Ratio` Inactive tetapi tidak menyatakan Pre-setup; spec memakai baseline Pre-setup #12.
