---
id: TC-GS-PROFILE-E2E-012-role-matrix-change-password-berhasil
title: "Role Matrix: Change Password berhasil per role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-52
  - TC-GS-PROFILE-57
  - TC-GS-PROFILE-62
  - TC-GS-PROFILE-67
coverage:
  web: automated
---

# Role Matrix: Change Password berhasil per role

## Prerequisites

- Mode: FE+BE.
- Spec Role Matrix (bagian 3a konvensi) positif: Change Password berhasil untuk semua role. Langkah tiap role identik, hanya akun login yang berbeda. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (langkah 1 sampai 10; urutan baris = urutan iterasi):

| Role | Pre-setup | Akun | Env var password aktif (Current Password) |
|---|---|---|---|
| Total Control | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_PROFILE_TC_PASSWORD` |
| Read Only | #2 | Rina Pratiwi, `readOnlyProfile_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_PROFILE_RO_PASSWORD` |
| System Role | #3 | Dewi Lestari, `systemRoleProfile_automated_{namaCompany}@qwertysystem.net` (role individual "Manage user and role") | `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD` |
| User Basic | #4 | Budi Santoso, `userBasicProfile_automated_{namaCompany}@qwertysystem.net` (0 role individual, App Access Fixed Asset saja) | `Spectra.env.GS_PROFILE_BASIC_PASSWORD` |

- Password baru untuk New Password dan Confirm New Password: `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3, nilai `N3wPassw0rd!`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #1) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- State global yang diubah: password akun Pre-setup #1 sampai #4 berubah menjadi `N3wPassw0rd!`. Hook suite 7 hanya memulihkan password Pre-setup #7, #18, dan #24, sehingga spec ini memulihkan password Pre-setup #1 sampai #4 ke nilai awal (env var tabel di atas) lewat fixture pemulihan password yang disediakan tim FE/BE: di langkah 10 tiap iterasi, dan di hook `after` spec sebagai cadangan yang tidak berasumsi iterasi berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada selain password baru di atas.

## Test Steps

### Change Password berhasil, per role (TC-GS-PROFILE-52, TC-GS-PROFILE-57, TC-GS-PROFILE-62, TC-GS-PROFILE-67)

1. Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 10): logout, lalu login sebagai role pada baris tabel dengan env var password pada baris itu
2. Buka My Profile dari account menu navbar
3. Klik [Change Password]
4. Isi Current Password dengan password aktif akun pada baris tabel
5. Isi New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
6. Isi Confirm New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
7. Klik [Save]
8. Verifikasi toast sukses: `Success, your password has been updated.`
9. Verifikasi modal Change Password tertutup
10. Pulihkan password akun pada baris tabel ke nilai awal lewat fixture pemulihan password hingga perubahan tersimpan

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-52, 57, 62, 67).
- Pengulangan: langkah 1 sampai 10 diulang untuk tiap baris tabel Role yang diuji (Total Control, Read Only, System Role, User Basic). Langkah tiap role identik; parameter iterasi hanya akun dan env var password, tanpa langkah bersyarat. Langkah 1 pada iterasi Total Control mengulang login akun hook `before` supaya langkah perulangan tidak bersyarat.
- Spec berisi 10 langkah nominal dan sekitar 40 langkah setelah ekspansi (10 langkah dikali 4 role), di atas smell 35 langkah. Alasan: semua iterasi satu kelas (Role Matrix positif) dan satu topik aksi; langkah tiap role identik sehingga kegagalan satu role tidak membuat role lain kehilangan makna (bagian 3a konvensi).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 adalah Step ganti akun; langkah 2 membuka My Profile untuk akun baru; langkah 10 memulihkan password (R-08, S-09).
- Form Change Password tertutup oleh sukses [Save], sehingga tidak ada form dirty di akhir iterasi.
- Temuan untuk QA:
  - Post Condition TC-GS-PROFILE-52, 57, 62, dan 67 ("Password akun berubah menjadi `N3wPassw0rd!`") tidak punya langkah observasi di TC dan tidak diasersi di spec ini (S-01).
  - TC-GS-PROFILE-52, 57, 62, dan 67 menulis Precondition "Login sbg Role: ..." dan Current Password "password aktif akun" tanpa nilai; spec memakai env var per akun Pre-setup #1 sampai #4.
