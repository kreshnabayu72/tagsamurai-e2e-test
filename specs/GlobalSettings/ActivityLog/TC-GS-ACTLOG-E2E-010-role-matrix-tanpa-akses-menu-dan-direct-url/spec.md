---
id: TC-GS-ACTLOG-E2E-010-role-matrix-tanpa-akses-menu-dan-direct-url
title: "Role Matrix: Tanpa Akses Menu dan Direct URL"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-30
  - TC-GS-ACTLOG-31
  - TC-GS-ACTLOG-32
  - TC-GS-ACTLOG-33
  - TC-GS-ACTLOG-34
coverage:
  web: automated
---

# Role Matrix: Tanpa Akses Menu dan Direct URL

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Create-Only Brand, Full CRUD Brand, System Role, dan Admin Console See-All, serta akun Total Control Client A untuk halaman Global Settings > Role & Permission, dan halaman Portal, Global Settings > Role & Permission, Global Settings > Brand, serta menu Global Settings lain milik role itu (kemampuan disediakan tim FE/BE)
- Spec Role Matrix negatif (bagian 3a konvensi): role yang tidak berhak atas Activity Log, akun login berbeda per role, langkah tiap role berbeda sehingga ditulis per blok. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (Client A):

| TC | Role | Akun | Env var password | Menu pembanding |
|---|---|---|---|---|
| TC-GS-ACTLOG-30 (Role & Permission) | Total Control | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` | tidak dipakai |
| TC-GS-ACTLOG-30 (menu), TC-GS-ACTLOG-34 | Create-Only Brand (capability individual tanpa access level Total Control atau Read Only) | `createOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` | `Brand` |
| TC-GS-ACTLOG-31 | Full CRUD Brand (Create, Update, Delete, Read pada Brand tanpa access level) | `Fixture.activityLog.fullCrudBrand` (email ditetapkan tim FE) | `Spectra.env.GS_FULLCRUDBRAND_PASSWORD` (env baru) | `Brand` |
| TC-GS-ACTLOG-32 | System Role | `Fixture.activityLog.systemRole` (email ditetapkan tim FE) | `Spectra.env.GS_SYSTEMROLE_PASSWORD` (env baru) | menu Global Settings lain milik role itu, disediakan tim FE |
| TC-GS-ACTLOG-33 | Admin Console See-All (akses baca Admin Console tanpa access level Global Settings) | `Fixture.activityLog.adminConsoleSeeAll` (email ditetapkan tim FE) | `Spectra.env.GS_ACSEEALL_PASSWORD` (env baru) | menu Global Settings lain milik role itu, disediakan tim FE |

- Login Total Control di hook `before` (akun default suite). Ganti akun antar role ditulis sebagai langkah eksplisit; karena spec berakhir di akun Admin Console See-All, hook `after` mengembalikan sesi ke Total Control Client A (`GS_TC_PASSWORD`).
- Data Pre-setup (tetap di environment): kelima akun di atas; spec tidak membuat atau mengubah data. Tidak ada data Dinamis bersuffix `{runId}`.
- Kemampuan teknis (disediakan tim FE/BE): URL langsung tab Session dan tab User Action Activity Log (route per tab sesuai PRD Activity Log §4.2) dapat diketik di address bar.

## Test Steps

### TC-GS-ACTLOG-30: Pemegang capability tunggal (Create-Only Brand) tidak punya akses menu Activity Log

1. Buka Global Settings > Role & Permission sebagai Total Control, buka daftar capability yang dapat dipilih
2. Verifikasi capability `Brand` tampil pada daftar capability
3. Verifikasi Activity Log tidak muncul sebagai capability yang bisa dipilih pada Role & Permission
4. Logout, lalu login sebagai Create-Only Brand (`createOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_CREATE_PASSWORD`, lalu buka Global Settings dari Portal
5. Verifikasi menu `Brand` tampil pada menu Global Settings di sidebar
6. Verifikasi menu Activity Log tidak tampil (Hidden total) pada menu Global Settings di sidebar

### TC-GS-ACTLOG-34: Akses URL langsung oleh pemegang capability tanpa access level, kedua tab

7. Ketik URL tab Session Activity Log langsung di address bar
8. Verifikasi toast error `"You don't have permission to do this."` tampil pada tab Session
9. Verifikasi tidak ada baris log yang tampil pada tab Session
10. Verifikasi tidak ada pengalihan ke halaman unauthorized terpisah pada tab Session
11. Ketik URL tab User Action Activity Log langsung di address bar
12. Verifikasi toast error `"You don't have permission to do this."` tampil pada tab User Action
13. Verifikasi tidak ada baris log yang tampil pada tab User Action
14. Verifikasi tidak ada pengalihan ke halaman unauthorized terpisah pada tab User Action

### TC-GS-ACTLOG-31: Pemegang capability penuh pada satu modul (Full CRUD Brand) tidak punya akses menu Activity Log

15. Logout, lalu login sebagai Full CRUD Brand dengan `Spectra.env.GS_FULLCRUDBRAND_PASSWORD`, lalu buka Global Settings dari Portal
16. Verifikasi menu `Brand` tampil pada menu Global Settings di sidebar
17. Verifikasi menu Activity Log tidak tampil (Hidden total) pada menu Global Settings di sidebar

### TC-GS-ACTLOG-32: System Role tidak punya akses menu Activity Log

18. Logout, lalu login sebagai System Role dengan `Spectra.env.GS_SYSTEMROLE_PASSWORD`, lalu buka Global Settings dari Portal
19. Verifikasi menu pembanding role System Role (tabel Prerequisites) tampil pada menu Global Settings di sidebar
20. Verifikasi menu Activity Log tidak tampil (Hidden total) pada menu Global Settings di sidebar

### TC-GS-ACTLOG-33: Pemegang akses baca Admin Console tanpa access level Global Settings tidak punya akses Activity Log

21. Logout, lalu login sebagai Admin Console See-All dengan `Spectra.env.GS_ACSEEALL_PASSWORD`, lalu buka Global Settings dari Portal
22. Verifikasi menu pembanding role Admin Console See-All (tabel Prerequisites) tampil pada menu Global Settings di sidebar
23. Verifikasi menu Activity Log tidak tampil (Hidden) pada menu Global Settings di sidebar
24. Ketik URL tab Session Activity Log langsung di address bar
25. Verifikasi toast error `"You don't have permission to do this."` tampil
26. Verifikasi data log tidak tampil

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-30, 31, 32, 33, 34).
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-ACTLOG-34 langsung setelah TC-GS-ACTLOG-30 karena memakai akun Create-Only Brand yang sama, sehingga ganti akun hanya satu kali per role. Akun pertama di hook `before` adalah Total Control karena Expected Result b TC-GS-ACTLOG-30 diamati dari akun yang bisa membuka Role & Permission, lalu langkah 4 berganti ke Create-Only Brand.
- Spec Role Matrix negatif ditulis per blok role (bukan perulangan) karena langkah tiap role berbeda: capability, akun, dan ada atau tidaknya langkah URL langsung (K-17).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (membuka daftar capability di Role & Permission, tidak ada di Langkah Uji TC-GS-ACTLOG-30; ditambahkan karena Expected Result TC itu menyebut Activity Log tidak muncul sebagai capability dan butuh langkah observasi) dan langkah ganti akun 4, 15, 18, 21 (juga membuka Global Settings dari Portal, karena halaman awal sesudah login adalah Portal dan sidebar Global Settings baru ada sesudah itu).
- Anchor positif tambahan yang tidak ada di TC (S-03, bagian 8b butir 2): langkah 2 (capability `Brand` tampil pada daftar), langkah 5, 16, 19, 22 (menu pembanding tampil pada sidebar yang sama) supaya asersi "tidak muncul" atau "tidak tampil" bukan karena daftar atau sidebar belum termuat.
- Toast error pada langkah 8, 12, dan 25 muncul di request baca yang ditolak 403; asersi respons server langsung (defense-in-depth) bukan bagian spec ini.
- Spec Role Matrix (bagian 3a konvensi): kasus sidebar tersembunyi dan direct URL ditolak dikelompokkan sebagai spec negatif sendiri; `caseType` Negative mengikuti seluruh TC sumber (Security dipetakan ke Negative). Visibilitas dan Download untuk Total Control dan Read Only ada di spec `TC-GS-ACTLOG-E2E-009-role-matrix-visibilitas-dan-download-total-control-dan-read-only`.
- Temuan untuk QA:
  - TC-GS-ACTLOG-30 tidak punya langkah untuk mengamati daftar capability di Role & Permission padahal Expected Result menyebutnya, dan aktor precondition (Create-Only Brand) tidak dapat membuka Role & Permission; navigasi langkah 1 dilakukan sebagai Total Control.
  - TC-GS-ACTLOG-31, 32, dan 33 memakai akun yang belum ada di `.env.example` (Full CRUD Brand, System Role, Admin Console See-All): akun disediakan tim FE (Pre-setup TC baris 4 sampai 6: nama akun ditetapkan tim FE); env baru `GS_FULLCRUDBRAND_PASSWORD`, `GS_SYSTEMROLE_PASSWORD`, `GS_ACSEEALL_PASSWORD`.
  - Route URL tab Session dan User Action tidak ditulis literal di TC (hanya "URL tab ... langsung"); tim FE menyediakan route sesuai PRD §4.2.
  - Belum diverifikasi apakah `createOnly_automated_qaTeam1` (System Role: Create dan Read di suite Brand) sama dengan "Create-Only Brand capability individual tanpa access level".
  - Menu pembanding untuk role System Role dan Admin Console See-All tidak ditentukan di TC; ditetapkan tim FE.
