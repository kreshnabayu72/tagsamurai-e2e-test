---
id: TC-GS-ROLE-E2E-102-default-user-tetap-total-control-setelah-semua-total-control-lain-di-remove
title: "Default User Tetap Total Control Setelah Semua Total Control Lain Di-Remove"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-278
coverage:
  web: automated
---

# Default User Tetap Total Control Setelah Semua Total Control Lain Di-Remove

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (login di hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Akun kedua (ganti akun di langkah 4): Eko Prasetyo (Total Control kedua, Pre-setup #13), password `Spectra.env.GS_TC2_PASSWORD`. Akun ketiga (ganti akun di langkah 12): Budi Santoso (Default User, Pre-setup #2), `defaultUserGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_DEFAULT_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_DEFAULT_PASSWORD`. Email Eko Prasetyo disediakan tim FE.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`).
- Given (hook `before`, lewat API): Tab Total Control hanya berisi Budi Santoso (Default User), Ahmad Fauzi, dan Eko Prasetyo, sesuai Precondition TC-GS-ROLE-278. Total Control Pre-setup lain (Dewi Lestari, Pre-setup #3; Bayu Nugraha, Pre-setup #19; dan user lain yang menjadi Total Control akibat spec lain) dicabut dulu agar kondisi itu terpenuhi.
- Pemulihan (hook `after`, lewat API): Ahmad Fauzi dan Eko Prasetyo dikembalikan sebagai Total Control, begitu pula Total Control lain yang dicabut di Given (Dewi Lestari kembali Inactive; Bayu Nugraha kembali Temporary User dengan Temporary Until semula). Sesi dikembalikan ke akun default suite (Ahmad Fauzi, `GS_TC_PASSWORD`). Efek pada Modified By dan Last Updated dipulihkan sejauh dapat dipulihkan.
- Spec ini mencabut Total Control dari Ahmad Fauzi, aktor default seluruh suite, sehingga wajib berjalan sesudah spec lain. Suite berjalan serial (`parallel: false`) dan spec ini diletakkan paling akhir di antara spec yang memakai akun Ahmad Fauzi.
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): mengatur access level user Pre-setup lewat API untuk Given dan pemulihan; ganti akun tiga kali dalam satu spec; hover pada item overlay untuk membaca tooltip.

## Test Steps

### TC-GS-ROLE-278: Default User tetap Total Control setelah semua Total Control lain di-Remove

1. Verifikasi baris Budi Santoso, Ahmad Fauzi, dan Eko Prasetyo tampil di Tab Total Control
2. Verifikasi tidak ada baris Total Control lain di Tab Total Control
3. Logout
4. Login sebagai Eko Prasetyo
5. Buka Tab Total Control
6. Klik `(⋯)` baris Ahmad Fauzi
7. Klik `Remove`
8. Klik `[Remove]`
9. Verifikasi toast sukses `Success, Total Control has been removed.` tampil
10. Verifikasi baris Ahmad Fauzi tidak ada di Tab Total Control
11. Logout
12. Login sebagai Budi Santoso
13. Buka Tab Total Control
14. Klik `(⋯)` baris Eko Prasetyo
15. Klik `Remove`
16. Klik `[Remove]`
17. Verifikasi toast sukses `Success, Total Control has been removed.` tampil
18. Verifikasi baris Eko Prasetyo tidak ada di Tab Total Control
19. Verifikasi Tab Total Control hanya berisi Budi Santoso
20. Klik `(⋯)` baris Budi Santoso
21. Arahkan kursor ke `Remove`
22. Verifikasi `Remove` tampil disabled
23. Verifikasi tooltip `Default User cannot be modified.`
24. Tekan Esc untuk menutup overlay

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): ganti akun (langkah 3, 4, 11, 12), membuka Tab Total Control (langkah 5, 13), dan menutup overlay dengan Esc (langkah 24). Langkah 1 dan 2 memverifikasi Given (anchor positif sebelum aksi).
- TC-GS-ROLE-278 langkah 1 ("Login sbg Eko Prasetyo: Remove Total Control Ahmad Fauzi") dan langkah 2 ("Login sbg Budi Santoso: Remove Total Control Eko Prasetyo") dipetakan ke langkah 4 sampai 10 dan 12 sampai 18; langkah 3 TC ("Amati Tab Total Control") ke langkah 19 sampai 23. Aktor Ahmad Fauzi di Precondition hanya menjadi akun hook `before` dan akun yang dicabut.
- Expected c ("Remove Budi Santoso disabled") dicek lewat hover overlay `(⋯)` baris Budi Santoso; tooltip `Default User cannot be modified.` mengikuti spec 019.
- Temuan untuk QA:
  - TC-GS-ROLE-278 Precondition b menyebut Total Control hanya Budi, Ahmad, dan Eko, padahal Pre-setup memuat Total Control lain (Dewi Lestari, Bayu Nugraha); spec menyiapkannya sebagai Given dan memulihkannya di hook `after`.
  - TC-GS-ROLE-278 Expected a ("tanpa pemeriksaan jumlah") tidak menyebut toast; spec memverifikasi toast sukses `Success, Total Control has been removed.` mengikuti TC-GS-ROLE-87.
  - TC-GS-ROLE-278 Expected c tidak menyebut tooltip; teks tooltip diambil dari TC-GS-ROLE-42.
