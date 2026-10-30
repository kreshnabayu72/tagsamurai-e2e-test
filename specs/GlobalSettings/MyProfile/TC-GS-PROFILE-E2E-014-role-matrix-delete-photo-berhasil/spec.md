---
id: TC-GS-PROFILE-E2E-014-role-matrix-delete-photo-berhasil
title: "Role Matrix: Delete Photo berhasil per role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-54
  - TC-GS-PROFILE-59
  - TC-GS-PROFILE-64
  - TC-GS-PROFILE-69
coverage:
  web: automated
---

# Role Matrix: Delete Photo berhasil per role

## Prerequisites

- Mode: FE+BE.
- Spec Role Matrix (bagian 3a konvensi) positif: Delete Photo berhasil untuk semua role. Langkah tiap role identik, hanya akun login dan inisial Avatar yang berbeda. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (langkah 1 sampai 9; urutan baris = urutan iterasi):

| Role | Pre-setup | Akun | Inisial Avatar | Env var password |
|---|---|---|---|---|
| Total Control | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net` | `AP` | `Spectra.env.GS_PROFILE_TC_PASSWORD` |
| Read Only | #2 | Rina Pratiwi, `readOnlyProfile_automated_{namaCompany}@qwertysystem.net` | `RP` | `Spectra.env.GS_PROFILE_RO_PASSWORD` |
| System Role | #3 | Dewi Lestari, `systemRoleProfile_automated_{namaCompany}@qwertysystem.net` (role individual "Manage user and role") | `DL` | `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD` |
| User Basic | #4 | Budi Santoso, `userBasicProfile_automated_{namaCompany}@qwertysystem.net` (0 role individual, App Access Fixed Asset saja) | `BS` | `Spectra.env.GS_PROFILE_BASIC_PASSWORD` |

- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #1) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Kemampuan teknis: fixture BE yang memasang foto profil aktif untuk akun aktor sebelum tiap iterasi (precondition TC-GS-PROFILE-54, 59, 64, dan 69 butir d); mekanisme disediakan tim FE/BE.
- State yang diubah: foto profil akun Pre-setup #1 sampai #4 dipasang lalu dihapus. Hook suite 7 hanya memulihkan foto Pre-setup #9 dan #10, sehingga spec ini memulihkan foto Pre-setup #1 sampai #4 ke keadaan awal lewat fixture pemulihan foto yang disediakan tim FE/BE: di langkah 9 tiap iterasi dan di hook `after` spec sebagai cadangan yang tidak berasumsi iterasi berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada.

## Test Steps

### Delete Photo berhasil, per role (TC-GS-PROFILE-54, TC-GS-PROFILE-59, TC-GS-PROFILE-64, TC-GS-PROFILE-69)

1. Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 9): logout, lalu login sebagai role pada baris tabel dengan env var password pada baris itu
2. Pasang foto profil aktif untuk akun pada baris tabel lewat fixture BE
3. Buka My Profile dari account menu navbar
4. Hover Avatar, lalu klik [Delete]
5. Klik [Remove] pada dialog `Remove Photo`
6. Verifikasi toast sukses: `Success, photo has been removed.`
7. Verifikasi Avatar kembali menampilkan inisial pada kolom Inisial Avatar baris tabel
8. Tunggu aksi selesai
9. Pulihkan foto akun pada baris tabel ke keadaan awal lewat fixture pemulihan foto hingga perubahan tersimpan

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-54, 59, 64, 69).
- Pengulangan: langkah 1 sampai 9 diulang untuk tiap baris tabel Role yang diuji (Total Control, Read Only, System Role, User Basic). Langkah tiap role identik; parameter iterasi hanya akun, env var password, dan inisial Avatar, tanpa langkah bersyarat. Langkah 1 pada iterasi Total Control mengulang login akun hook `before` supaya langkah perulangan tidak bersyarat.
- Spec berisi 9 langkah nominal dan 36 langkah setelah ekspansi (9 langkah dikali 4 role), di atas smell 35 langkah. Alasan: semua iterasi satu kelas (Role Matrix positif) dan satu topik aksi; langkah tiap role identik sehingga kegagalan satu role tidak membuat role lain kehilangan makna (bagian 3a konvensi).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 adalah Step ganti akun; langkah 2 memasang foto aktif (precondition TC) sebelum My Profile dibuka (langkah 3); langkah 8 menunggu aksi selesai sebelum pemulihan dan ganti akun (bagian 8b butir 8); langkah 9 memulihkan foto (R-08, S-09).
- Temuan untuk QA:
  - TC-GS-PROFILE-54, 59, 64, dan 69 mensyaratkan foto profil aktif lewat fixture BE (butir d), sedangkan Pre-setup #1 tertulis tanpa foto dan Pre-setup #2 sampai #4 tidak menyebut foto; spec menulis fixture pemasangan foto di Prerequisites.
  - TC-GS-PROFILE-54, 59, 64, dan 69 tidak memberi Expected untuk dialog `Remove Photo` yang muncul sebelum [Remove]; spec tidak mengasersi dialog itu.
