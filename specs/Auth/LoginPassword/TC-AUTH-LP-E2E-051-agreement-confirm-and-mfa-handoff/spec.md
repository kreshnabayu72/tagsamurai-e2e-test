---
id: TC-AUTH-LP-E2E-051-agreement-confirm-and-mfa-handoff
title: "Konfirmasi Agreement ke Portal, Login Berikutnya, dan Handoff ke MFA"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-84
  - TC-AUTH-LP-85
  - TC-AUTH-LP-86
coverage:
  web: automated
---

# Konfirmasi Agreement ke Portal, Login Berikutnya, dan Handoff ke MFA

## Prerequisites

- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Versi Privacy Policy: seeding user selalu relatif terhadap versi aktif yang terbaca di hook `before` (versi yang disetujui user = versi sebelum versi aktif); nomor versi absolut tidak dipakai. Spec ini tidak mempublikasikan versi baru dan tidak mengubah versi aktif. Versi aktif tidak pernah dipulihkan oleh spec mana pun karena publish bersifat append-only dan immutable (tanpa restore, `ACPP-LOGIC-01` pada PRD Settings > Privacy Policy); suite berjalan serial.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: fixture BE agar versi terakhir yang disetujui user Hadi lebih lama dari versi Privacy Policy aktif; fixture BE untuk device terpercaya (tidak memicu MFA) pada user Hadi dan penandaan user Siti sebagai belum pernah login di web; jendela privat baru, serta kemampuan menutup semua jendela privat dan menghapus sesi browser terkait; reCAPTCHA mode uji di environment.
- Mode: FE+BE.
- TC-AUTH-LP-84: User `Hadi Gunawan` (`hadigunawan+{runId}-051@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA
- TC-AUTH-LP-84: User belum login (guest); browser web
- TC-AUTH-LP-84 data: Email `hadigunawan+{runId}-051@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-85: User `Hadi Gunawan` yang sama dengan TC-AUTH-LP-84, sudah menyetujui versi Privacy Policy aktif dan berada di Portal — Product Hub; tidak ada versi baru yang dipublikasikan sesudahnya
- TC-AUTH-LP-86: User `Siti Rahmawati` (`sitirahmawati+{runId}-051@qwertysystem.net`) berstatus Activated dan Active; belum pernah login di web
- TC-AUTH-LP-86: User belum login (guest); browser web
- TC-AUTH-LP-86 data: Email `sitirahmawati+{runId}-051@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-84: Centang checkbox dan klik [Continue ➔] melanjutkan ke Portal

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman Login with Password
3. Ketik email `hadigunawan+{runId}-051@qwertysystem.net` di field Email
4. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
5. Selesaikan reCAPTCHA
6. Klik [Log in] sampai layar Confirm to Continue tampil
7. Centang checkbox persetujuan
8. Klik [Continue ➔]
9. Verifikasi browser menuju Portal — Product Hub
10. Verifikasi layar Confirm to Continue tidak tampil lagi

### TC-AUTH-LP-85: Login berikutnya setelah menyetujui tidak menampilkan layar Confirm to Continue lagi

11. Logout dari Portal — Product Hub
12. Buka halaman Login with Password
13. Ketik email `hadigunawan+{runId}-051@qwertysystem.net` di field Email
14. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
15. Selesaikan reCAPTCHA
16. Klik [Log in]
17. Verifikasi layar Confirm to Continue tidak tampil
18. Verifikasi browser menuju Portal — Product Hub
19. Logout dari Portal — Product Hub
20. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-86: Setelah Continue dengan centang user yang memicu MFA diarahkan ke halaman MFA

21. Buka jendela privat baru (tanpa sesi login)
22. Buka halaman Login with Password
23. Ketik email `sitirahmawati+{runId}-051@qwertysystem.net` di field Email
24. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
25. Selesaikan reCAPTCHA
26. Klik [Log in] sampai layar Confirm to Continue tampil
27. Centang checkbox persetujuan
28. Klik [Continue ➔]
29. Verifikasi browser menuju halaman MFA
30. Verifikasi browser tidak menuju Portal — Product Hub
31. Verifikasi sesi penuh belum dibuat

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Pembagian spec: TC-AUTH-LP-102, 82, 83 (user Tono) ada di spec `TC-AUTH-LP-E2E-022-agreement-confirm-flow`; spec ini memuat TC-AUTH-LP-84, 85, 86 karena beda akun dengan data persetujuan sendiri-sendiri, dan bagian sesudahnya tidak lagi bermakna bila bagian sebelumnya gagal keras (layar Confirm to Continue tidak terbuka atau login gagal).
- Urutan memperhatikan state user: TC-AUTH-LP-84 lalu TC-AUTH-LP-85 memakai user Hadi yang sama (persetujuan dibuat di TC-AUTH-LP-84, dipakai di TC-AUTH-LP-85); dependensi TC-AUTH-LP-85 pada TC-AUTH-LP-84 dipenuhi dengan menyalin langkah, bukan dirujuk (S-04). TC-AUTH-LP-86 memakai user Siti sendiri dan diletakkan terakhir karena berujung di halaman MFA.
- Langkah buka jendela privat baru (langkah 1, 21), logout (langkah 11, 19), dan penutupan semua jendela privat beserta penghapusan sesi browser terkait (langkah 20) adalah langkah penghubung tanpa awalan `Verifikasi` (S-03; S-09); langkah 20 menjamin TC-AUTH-LP-86 mulai dari konteks browser bersih tanpa mengandalkan jendela privat baru saja.
- TC-AUTH-LP-86 berhenti di halaman MFA; pelengkapan MFA dimiliki modul MFA. TC-AUTH-LP-124 (tidak ada pencatatan Success pada langkah password saat MFA tertunda) diuji di spec `TC-AUTH-LP-E2E-043-absence-state-based`.
- Temuan untuk QA: Post Condition "persetujuan Privacy Policy tersimpan untuk versi aktif" pada TC-AUTH-LP-84 dan TC-AUTH-LP-86 tidak punya langkah observasi atau cara baca state di UI; spec tidak mengasersinya (S-01) dan tidak menambah langkah observasi sendiri. Persetujuan hanya teramati tidak langsung lewat TC-AUTH-LP-85 (layar Confirm to Continue tidak tampil pada login berikutnya) untuk user Hadi; untuk user Siti tidak ada pengamatan.
