---
id: TC-GS-ROLE-E2E-114-landing-page-user-seluruh-role-inactive-retained
title: "Landing Page User yang Seluruh Role-nya Inactive-Retained"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-332
coverage:
  web: automated
---

# Landing Page User yang Seluruh Role-nya Inactive-Retained

## Prerequisites

- Mode: FE+BE. Suite `parallel: false` karena spec mengubah state user Pre-setup bersama dan berganti akun.
- Akun hook `before`: Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Ahmad Fauzi dipakai hanya untuk menyiapkan Given lewat sesi API dan menjadi akun default suite yang dipulihkan di hook `after`.
- Akun uji: Lutfi Hakim (Pre-setup #20: Active, tanpa access level, satu-satunya baris role `Manage files` inactive-retained, Access Global Settings dicentang). Email dan kredensial disediakan tim FE (Tabel Pre-setup TC tidak memuat email; lihat Temuan untuk QA). Login ke akun ini adalah objek uji (Expected a) dan ditulis sebagai langkah ganti akun di Test Steps. Nilai identitas user mengacu fixture `Fixture.role.*` yang dibuat di tahap script (berkas belum ada).
- Given (hook `before`): `Lutfi Hakim` dipastikan berada di state di atas. Mekanisme menyiapkan baris role inactive-retained per user disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): sesi dipulihkan ke akun default suite (Logout `Lutfi Hakim`) dan `Lutfi Hakim` dikembalikan ke state Given. Efek pada Pre-setup: tidak ada perubahan data; entri log bersifat immutable.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun UI yang dipakai suite, termasuk akun target; spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-332: Landing page untuk user yang seluruh role-nya inactive-retained

1. Ganti akun: Logout dari akun Ahmad Fauzi
2. Login sebagai `Lutfi Hakim`
3. Buka card Global Settings di Portal
4. Verifikasi aplikasi Global Settings terbuka (tidak redirect ke Portal)
5. Verifikasi area konten menampilkan illustration, teks `You don't have access to any menu yet.`, dan subtext `Contact your administrator to get access.`
6. Verifikasi sidebar kosong: seluruh menu modul Global Settings tidak tampil, termasuk File Manager
7. Verifikasi tidak tampil `Unable to load this data.` maupun `[Try Again]`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional. Satu TC sumber.
- Langkah 1 dan 2 adalah ganti akun eksplisit: login `Lutfi Hakim` adalah objek uji (Expected a "Login sukses"), sehingga tidak dilakukan di hook `before`.
- Urutan langkah mengikuti urutan state (bagian 8b butir 5): area konten (langkah 5) diasersi lebih dulu dan menjadi anchor positif bagi absence menu sidebar (langkah 6) dan absence pesan error (langkah 7), karena sidebar tidak punya item menu lain sebagai pembanding.
- Langkah penghubung (aksi tanpa `Verifikasi`): ganti akun (langkah 1 dan 2) dan membuka card Global Settings (langkah 3).
- Temuan untuk QA:
  - Email dan kredensial akun `Lutfi Hakim` tidak ada di Tabel Pre-setup TC; ditulis "disediakan tim FE".
  - Kolom Precondition TC-GS-ROLE-332 terpotong ("Role Lutfi Hakim (Pre-setup #20), tanpa acces..."); spec memperlakukannya sebagai login sebagai `Lutfi Hakim` tanpa access level.
  - Mekanisme menyiapkan baris role inactive-retained per user (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-ROLE-332 Langkah Uji "Buka card Global Settings di Portal" mengasumsikan landing di Portal; Expected a menyebut "tidak redirect ke Portal"; spec mengikuti keduanya.
