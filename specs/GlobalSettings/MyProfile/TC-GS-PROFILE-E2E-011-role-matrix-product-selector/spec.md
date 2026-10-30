---
id: TC-GS-PROFILE-E2E-011-role-matrix-product-selector
title: "Role Matrix: Product Selector berpindah konteks produk per role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-51
  - TC-GS-PROFILE-56
  - TC-GS-PROFILE-61
  - TC-GS-PROFILE-66
coverage:
  web: automated
---

# Role Matrix: Product Selector berpindah konteks produk per role

## Prerequisites

- Mode: FE+BE.
- Spec Role Matrix (bagian 3a konvensi) positif: berpindah konteks produk berhasil untuk semua role. Tiga role pertama memakai langkah identik (perulangan); User Basic ditulis sebagai blok sendiri karena langkah dan app asalnya berbeda. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji untuk perulangan (langkah 1 sampai 7; urutan baris = urutan iterasi):

| Role | Pre-setup | Akun | Env var password |
|---|---|---|---|
| Total Control | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_PROFILE_TC_PASSWORD` |
| Read Only | #2 | Rina Pratiwi, `readOnlyProfile_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_PROFILE_RO_PASSWORD` |
| System Role | #3 | Dewi Lestari, `systemRoleProfile_automated_{namaCompany}@qwertysystem.net` (role individual "Manage user and role") | `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD` |

Role blok sendiri: User Basic, Pre-setup #4 Budi Santoso (`userBasicProfile_automated_{namaCompany}@qwertysystem.net`), 0 role individual, tanpa Access Level, App Access Fixed Asset saja (app asal Fixed Asset); password `Spectra.env.GS_PROFILE_BASIC_PASSWORD`.

- Ketiga role perulangan memiliki App Access Global Settings dan Fixed Asset, sehingga opsi Fixed Asset tersedia pada Product Selector.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #1) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Data Dinamis: tidak ada. Spec hanya membaca; konteks Product Selector kembali ke default saat My Profile dibuka ulang.

## Test Steps

### Berpindah ke Fixed Asset, per role (TC-GS-PROFILE-51, TC-GS-PROFILE-56, TC-GS-PROFILE-61)

1. Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 7): logout, lalu login sebagai role pada baris tabel dengan env var password pada baris itu
2. Buka My Profile dari account menu navbar
3. Klik `Viewing: [Product ▾]`
4. Pilih opsi Fixed Asset
5. Verifikasi Section Access & Status dirender ulang untuk konteks Fixed Asset
6. Verifikasi Product Selector menampilkan `Viewing: Fixed Asset`
7. Muat ulang halaman My Profile

### Role User Basic berpindah produk dua arah (TC-GS-PROFILE-66)

8. Logout, lalu login sebagai Pre-setup #4 (Budi Santoso) dengan `Spectra.env.GS_PROFILE_BASIC_PASSWORD`; User berada di Fixed Asset (app asal)
9. Buka My Profile dari account menu navbar
10. Verifikasi Product Selector menampilkan `Viewing: Fixed Asset` (default mengikuti app asal, S-04)
11. Klik `Viewing: [Product ▾]`
12. Pilih opsi Global Settings
13. Verifikasi Section Access & Status dirender ulang untuk konteks Global Settings
14. Verifikasi Product Selector menampilkan `Viewing: Global Settings`
15. Klik `Viewing: [Product ▾]`
16. Pilih opsi Fixed Asset
17. Verifikasi Section Access & Status dirender ulang untuk konteks Fixed Asset
18. Verifikasi Product Selector menampilkan `Viewing: Fixed Asset`

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-51, 56, 61, 66).
- Pengulangan: langkah 1 sampai 7 diulang untuk tiap baris tabel Role yang diuji (Total Control, Read Only, System Role). Langkah tiap role identik; parameter iterasi hanya akun. Langkah 1 pada iterasi Total Control mengulang login akun hook `before` supaya langkah perulangan tidak bersyarat.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 dan 8 adalah Step ganti akun; langkah 2 dan 9 membuka My Profile untuk akun baru; langkah 7 memuat ulang halaman supaya konteks Product Selector kembali ke default sebelum iterasi berikutnya (S-09).
- Spec berisi 18 langkah nominal dan sekitar 32 langkah setelah ekspansi (langkah 1 sampai 7 dikali 3 ditambah 11 langkah User Basic), di bawah smell 35 langkah.
- Temuan untuk QA: tidak ada.
