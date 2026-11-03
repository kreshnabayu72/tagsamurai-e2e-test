---
id: TC-GS-NLU-E2E-008-role-matrix-visibilitas-menu-user-di-sidebar-dan-direct
title: "Role Matrix: visibilitas menu User di sidebar dan direct URL tanpa capability"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-29
  - TC-GS-NLU-30
  - TC-GS-NLU-31
  - TC-GS-NLU-32
  - TC-GS-NLU-33
coverage:
  web: automated
---

# Role Matrix: visibilitas menu User di sidebar dan direct URL tanpa capability

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-29 | Total Control | Siti Nurhaliza | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-NLU-30 | Read Only | Yudi Pratomo | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-NLU-31 | Manage user and role (Read-Only role: R saja) | Eko Prasetyo | `manageUserRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |
| TC-GS-NLU-32, 33 | Basic (Access Global Settings, tanpa tier dan tanpa role Manage user and role) | Gita Permata | `basicGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_BASIC_PASSWORD` |
- Login akun aktor pertama (Total Control) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk setiap akun aktor pada tabel sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup No. 9 sampai 13 hanya dibaca. Spec tidak membuat data dan tidak mengubah state global.
- Kemampuan teknis: URL halaman Global Settings > User (User List) disediakan tim FE; URL itu tidak tertulis di TC, PRD, atau LLD.
- Env var `GS_TC_PASSWORD`, `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, dan `GS_BASIC_PASSWORD` terdaftar di `executionConfig.environmentVariables`; password tidak ditulis di spec atau fixture. Email Pre-setup TC berpola `{namaCompany}` (lihat Temuan untuk QA).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-29: Menu User di sidebar tampil untuk Total Control

1. Verifikasi item `User` tampil di sidebar Global Settings
2. Verifikasi sub-tab `Non-Login User` tersedia di halaman User List

### TC-GS-NLU-30: Menu User di sidebar tampil untuk Read Only

3. Logout dari akun Total Control, lalu login sebagai Read Only (Yudi Pratomo, `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_RO_PASSWORD`)
4. Verifikasi item `User` tampil di sidebar Global Settings
5. Klik item `User` di sidebar Global Settings
6. Verifikasi sub-tab `Non-Login User` tersedia

### TC-GS-NLU-31: Menu User di sidebar tampil untuk pemegang Manage user and role (Read-Only role: R saja)

7. Logout dari akun Read Only, lalu login sebagai Manage user and role (Read-Only role: R saja) (Eko Prasetyo, `manageUserRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_READ_PASSWORD`)
8. Verifikasi item `User` tampil di sidebar Global Settings
9. Klik item `User` di sidebar Global Settings
10. Verifikasi sub-tab `Non-Login User` tersedia

### TC-GS-NLU-32: Menu User di sidebar Hidden untuk aktor tanpa capability dan bukan Total Control atau Read Only

11. Logout dari akun Manage user and role (Read-Only role: R saja), lalu login sebagai Basic (Access Global Settings, tanpa tier dan tanpa role Manage user and role) (Gita Permata, `basicGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_BASIC_PASSWORD`)
12. Verifikasi halaman utama aplikasi tampil
13. Verifikasi seluruh sidebar Global Settings tidak dirender sehingga item `User` dan sub-tab Non-Login User tidak dapat diakses

### TC-GS-NLU-33: Direct URL halaman User oleh aktor tanpa capability ditolak

14. Ketik URL halaman Global Settings > User langsung di address bar, tekan Enter
15. Verifikasi Toast error `"You don't have permission to do this."`
16. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tersembunyi
17. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
18. Verifikasi data Non-Login User tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 3, 5, 7, 9, 11 (membuka halaman User List lewat sidebar sesudah ganti akun, agar sub-tab dapat diamati).
- Spec Role Matrix visibilitas (bagian 3a konvensi): satu topik izin (menu User di sidebar dan direct URL), hasil berbeda per role; polaritas tampil dan Hidden dicampur. Ditulis per blok role karena langkah tiap role tidak identik (Basic tidak punya sidebar Global Settings) dan ganti akun menuntut langkah eksplisit; akun pertama login di hook `before` (S-07).
- Tidak ada aksi tulis; TC-GS-NLU-33 tidak mengirim request langsung, hanya navigasi address bar.
- Temuan untuk QA:
  - Email Pre-setup TC (No. 1 sampai 8) berpola `..._automated_{namaCompany}`, sedangkan komentar `.env.example` untuk `GS_RO_PASSWORD` dan `GS_READ_PASSWORD` mencantumkan email lain (`readOnly_automated_qaTeam1`, `readCapability_automated_qaTeam1`). Spec memakai email TC dan nama env yang sudah terdaftar; tim FE perlu memastikan satu nama env satu akun (R-07).
  - TC-GS-NLU-33 tidak menyebut URL persis halaman Global Settings > User; URL disediakan tim FE.
  - TC-GS-NLU-33 Expected b ("UI di-refresh sehingga elemen tidak berhak tersembunyi") tidak menyebut elemen mana; ditulis satu Verifikasi apa adanya.
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
