---
id: TC-AUTH-LP-E2E-021-agreement-trigger-conditions
title: "Kondisi Pemicu Layar Confirm to Continue"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-78
  - TC-AUTH-LP-79
  - TC-AUTH-LP-80
coverage:
  web: automated
---

# Kondisi Pemicu Layar Confirm to Continue

## Prerequisites

- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: fixture BE untuk riwayat login web (belum pernah login; pernah login dan logout kurang dari 30 hari lalu), waktu logout terakhir di web 31 hari lalu, device terpercaya (tidak memicu MFA), dan versi Privacy Policy yang disetujui user lebih lama dari versi aktif (seeding relatif, lihat aturan State global Privacy Policy); jendela privat baru; reCAPTCHA mode uji di environment.
- Mode: FE+BE.
- State global Privacy Policy: publish bersifat append-only dan immutable tanpa restore (`ACPP-LOGIC-01`), sehingga versi aktif tidak dipulihkan dan naik pada setiap run; suite berjalan serial. Seeding user Agreement selalu relatif terhadap versi aktif saat hook `before` (versi yang disetujui user = versi sebelum versi aktif), tanpa nomor versi absolut.
- TC-AUTH-LP-78: User `Siti Rahmawati` (`sitirahmawati+{runId}-021@qwertysystem.net`) berstatus Activated dan Active; belum pernah login di web
- TC-AUTH-LP-78: User belum login (guest); browser web
- TC-AUTH-LP-78 data: Email `sitirahmawati+{runId}-021@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-79: User `Eko Saputra` (`ekosaputra+{runId}-021@qwertysystem.net`) berstatus Activated dan Active; logout terakhir di web 31 hari lalu (fixture BE)
- TC-AUTH-LP-79: User belum login (guest); browser web
- TC-AUTH-LP-79 data: Email `ekosaputra+{runId}-021@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-80: User `Tono Kurniawan` (`tonokurniawan+{runId}-021@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; pernah login dan logout kurang dari 30 hari lalu; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini
- TC-AUTH-LP-80: User belum login (guest); browser web
- TC-AUTH-LP-80 data: Email `tonokurniawan+{runId}-021@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-78: Login pertama di web menampilkan layar Confirm to Continue sebelum halaman MFA

1. Buka halaman Login with Password
2. Ketik email `sitirahmawati+{runId}-021@qwertysystem.net` di field Email
3. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi layar Confirm to Continue tampil
7. Verifikasi halaman MFA tidak tampil
8. Verifikasi field Email, field Password, dan Button [Log in] tidak tampil
9. Verifikasi browser tidak menuju Portal — Product Hub

### TC-AUTH-LP-79: Login setelah logout terakhir lebih dari 30 hari menampilkan layar Confirm to Continue

10. Buka jendela privat baru (tanpa sesi login)
11. Buka halaman Login with Password
12. Ketik email `ekosaputra+{runId}-021@qwertysystem.net` di field Email
13. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
14. Selesaikan reCAPTCHA
15. Klik [Log in]
16. Verifikasi layar Confirm to Continue tampil
17. Verifikasi halaman MFA tidak tampil
18. Verifikasi Portal — Product Hub tidak tampil
19. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-80: Versi Privacy Policy aktif lebih baru dari versi yang disetujui menampilkan layar Confirm to Continue

20. Buka jendela privat baru (tanpa sesi login)
21. Buka halaman Login with Password
22. Ketik email `tonokurniawan+{runId}-021@qwertysystem.net` di field Email
23. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
24. Selesaikan reCAPTCHA
25. Klik [Log in]
26. Verifikasi layar Confirm to Continue tampil
27. Verifikasi halaman MFA tidak tampil
28. Verifikasi Portal — Product Hub tidak tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Variasi pemicu dari topik yang sama berurutan (login pertama, idle lebih dari 30 hari, versi policy lebih baru). Tiap TC memakai user sendiri dan dimulai di jendela privat baru (langkah penghubung, S-03).
- Layar Confirm to Continue tiap TC ditinggalkan tanpa Continue; interaksi Continue diuji di spec `TC-AUTH-LP-E2E-022-agreement-confirm-flow`.
- Langkah 19 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA: tidak ada. Urutan Agreement mendahului MFA pada TC-AUTH-LP-78 dan TC-AUTH-LP-79 konsisten dengan TC-AUTH-LP-86 dan TC-AUTH-LP-154.
