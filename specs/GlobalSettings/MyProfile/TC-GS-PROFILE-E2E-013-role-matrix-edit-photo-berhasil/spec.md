---
id: TC-GS-PROFILE-E2E-013-role-matrix-edit-photo-berhasil
title: "Role Matrix: Edit Photo berhasil per role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-53
  - TC-GS-PROFILE-58
  - TC-GS-PROFILE-63
  - TC-GS-PROFILE-68
coverage:
  web: automated
---

# Role Matrix: Edit Photo berhasil per role

## Prerequisites

- Mode: FE+BE.
- Spec Role Matrix (bagian 3a konvensi) positif: Edit Photo berhasil untuk semua role. Langkah tiap role identik, hanya akun login yang berbeda. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (langkah 1 sampai 8; urutan baris = urutan iterasi):

| Role | Pre-setup | Akun | Env var password |
|---|---|---|---|
| Total Control | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net` (tanpa foto) | `Spectra.env.GS_PROFILE_TC_PASSWORD` |
| Read Only | #2 | Rina Pratiwi, `readOnlyProfile_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_PROFILE_RO_PASSWORD` |
| System Role | #3 | Dewi Lestari, `systemRoleProfile_automated_{namaCompany}@qwertysystem.net` (role individual "Manage user and role") | `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD` |
| User Basic | #4 | Budi Santoso, `userBasicProfile_automated_{namaCompany}@qwertysystem.net` (0 role individual, App Access Fixed Asset saja) | `Spectra.env.GS_PROFILE_BASIC_PASSWORD` |

- File uji: `valid-photo.png` (Pre-setup #17, 200 KB).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #1) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Kemampuan teknis: memilih file pada file picker native browser (`valid-photo.png`) setelah [Edit] diklik.
- State yang diubah: foto profil akun Pre-setup #1 sampai #4 berubah menjadi `valid-photo.png`. Hook suite 7 hanya memulihkan foto Pre-setup #9 dan #10, sehingga spec ini memulihkan foto Pre-setup #1 sampai #4 ke keadaan awal lewat fixture pemulihan foto yang disediakan tim FE/BE: di langkah 8 tiap iterasi dan di hook `after` spec sebagai cadangan yang tidak berasumsi iterasi berhasil penuh. Foto baru menambah pemakaian Storage Client; efek ledger dipulihkan oleh fixture itu. Suite berjalan serial (`parallel: false`).
- Data Dinamis: Foto baru hasil Edit Photo (Data Dinamis #1) dipulihkan ke keadaan awal Pre-setup di langkah 8.

## Test Steps

### Edit Photo berhasil, per role (TC-GS-PROFILE-53, TC-GS-PROFILE-58, TC-GS-PROFILE-63, TC-GS-PROFILE-68)

1. Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 8): logout, lalu login sebagai role pada baris tabel dengan env var password pada baris itu
2. Buka My Profile dari account menu navbar
3. Hover Avatar, lalu klik [Edit]
4. Pilih file `valid-photo.png` pada file picker
5. Verifikasi toast sukses: `Success, photo has been updated.`
6. Verifikasi Avatar menampilkan foto baru
7. Tunggu aksi selesai
8. Pulihkan foto akun pada baris tabel ke keadaan awal lewat fixture pemulihan foto hingga perubahan tersimpan

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-53, 58, 63, 68).
- Pengulangan: langkah 1 sampai 8 diulang untuk tiap baris tabel Role yang diuji (Total Control, Read Only, System Role, User Basic). Langkah tiap role identik; parameter iterasi hanya akun dan env var password, tanpa langkah bersyarat. Langkah 1 pada iterasi Total Control mengulang login akun hook `before` supaya langkah perulangan tidak bersyarat.
- Spec berisi 8 langkah nominal dan 32 langkah setelah ekspansi (8 langkah dikali 4 role), di bawah smell 35 langkah.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 adalah Step ganti akun; langkah 2 membuka My Profile untuk akun baru; langkah 7 menunggu aksi selesai sebelum fixture memulihkan foto dan akun berganti (bagian 8b butir 8); langkah 8 memulihkan foto (R-08, S-09).
- Temuan untuk QA:
  - TC-GS-PROFILE-53, 58, 63, dan 68 tidak menyebut kondisi foto awal Pre-setup #2 sampai #4; spec memakai kondisi awal yang dipulihkan fixture.
