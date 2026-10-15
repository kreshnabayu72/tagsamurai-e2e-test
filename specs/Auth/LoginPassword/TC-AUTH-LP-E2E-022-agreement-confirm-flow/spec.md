---
id: TC-AUTH-LP-E2E-022-agreement-confirm-flow
title: "Interaksi dan Konfirmasi pada Layar Confirm to Continue"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-102
  - TC-AUTH-LP-82
  - TC-AUTH-LP-83
coverage:
  web: automated
---

# Interaksi dan Konfirmasi pada Layar Confirm to Continue

## Prerequisites

- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Versi Privacy Policy: seeding user selalu relatif terhadap versi aktif yang terbaca di hook `before` (versi yang disetujui user = versi sebelum versi aktif); nomor versi absolut tidak dipakai. Spec ini tidak mempublikasikan versi baru dan tidak mengubah versi aktif. Versi aktif tidak pernah dipulihkan oleh spec mana pun karena publish bersifat append-only dan immutable (tanpa restore, `ACPP-LOGIC-01` pada PRD Settings > Privacy Policy); suite berjalan serial.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: fixture BE agar versi terakhir yang disetujui user subjek lebih lama dari versi Privacy Policy aktif; fixture BE untuk device terpercaya (tidak memicu MFA); jendela privat baru; reCAPTCHA mode uji di environment.
- Mode: FE+BE.
- TC-AUTH-LP-102: User `Tono Kurniawan` (`tonokurniawan+{runId}-022@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya
- TC-AUTH-LP-102: User belum login (guest); browser web
- TC-AUTH-LP-102 data: Email `tonokurniawan+{runId}-022@qwertysystem.net`; Password salah nilai `Spectra.env.LP_PASSWORD_WRONG`; Password benar nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-82: User `Tono Kurniawan` (`tonokurniawan+{runId}-022@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui (persetujuan belum tersimpan); device terpercaya; tidak memicu MFA
- TC-AUTH-LP-82: User belum login (guest); browser web
- TC-AUTH-LP-82 data: Email `tonokurniawan+{runId}-022@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-83: User dan data sama seperti TC-AUTH-LP-82 (jendela privat baru)

## Test Steps

### TC-AUTH-LP-102: Alert pesan server hilang saat respons berikutnya membuka layar lain

1. Buka halaman Login with Password
2. Ketik email `tonokurniawan+{runId}-022@qwertysystem.net` di field Email
3. Ketik password nilai `Spectra.env.LP_PASSWORD_WRONG` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
7. Ketik ulang password nilai `Spectra.env.LP_PASSWORD` di field Password
8. Selesaikan reCAPTCHA
9. Klik [Log in]
10. Verifikasi layar Confirm to Continue tampil
11. Verifikasi Alert Danger dari percobaan sebelumnya tidak tampil

### TC-AUTH-LP-82: Klik [Continue ➔] tanpa mencentang checkbox

12. Buka jendela privat baru (tanpa sesi login)
13. Buka halaman Login with Password
14. Ketik email `tonokurniawan+{runId}-022@qwertysystem.net` di field Email
15. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
16. Selesaikan reCAPTCHA
17. Klik [Log in] sampai layar Confirm to Continue tampil
18. Biarkan checkbox unchecked, klik [Continue ➔]
19. Verifikasi checkbox berstatus invalid (severity danger)
20. Verifikasi caption "You need to agree to the Privacy Policy to continue" tampil di bawah checkbox
21. Verifikasi Button [Continue ➔] tetap enabled
22. Verifikasi layar Confirm to Continue tetap terbuka
23. Verifikasi browser tidak menuju Portal — Product Hub
24. Verifikasi browser tidak menuju halaman MFA
25. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-83: Mencentang checkbox dan klik [Continue ➔] setelah penolakan berhasil melanjutkan login

26. Buka jendela privat baru (tanpa sesi login)
27. Buka halaman Login with Password
28. Ketik email `tonokurniawan+{runId}-022@qwertysystem.net` di field Email
29. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
30. Selesaikan reCAPTCHA
31. Klik [Log in] sampai layar Confirm to Continue tampil
32. Klik [Continue ➔] tanpa mencentang checkbox
33. Verifikasi caption "You need to agree to the Privacy Policy to continue" tampil
34. Centang checkbox persetujuan
35. Verifikasi caption "You need to agree to the Privacy Policy to continue" tidak tampil lagi
36. Klik [Continue ➔]
37. Verifikasi browser menuju Portal — Product Hub
38. Logout dari Portal — Product Hub

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Pemisahan spec: kasus konfirmasi Agreement dibagi menurut akun. Spec ini memuat user Tono (TC-AUTH-LP-102, 82, 83); TC-AUTH-LP-84, 85 (Hadi) dan 86 (Siti) ada di spec `TC-AUTH-LP-E2E-051-agreement-confirm-and-mfa-handoff`. Alasannya: beda akun dengan data persetujuan sendiri-sendiri, dan bagian sesudahnya tidak lagi bermakna bila bagian sebelumnya gagal keras (layar Confirm to Continue tidak terbuka atau login gagal).
- Urutan memperhatikan state user: TC-AUTH-LP-102 dijalankan paling awal karena meninggalkan layar tanpa persetujuan; TC-AUTH-LP-82 dan TC-AUTH-LP-83 memakai user yang sama (persetujuan baru tersimpan di TC-AUTH-LP-83). Dependensi TC-AUTH-LP-83 pada TC-AUTH-LP-82 dipenuhi dengan menyalin langkah, bukan dirujuk (S-04).
- Langkah buka jendela privat baru (langkah 12, 26) dan logout (langkah 38) adalah langkah penghubung tanpa awalan `Verifikasi` (S-03; S-09).
- TC-AUTH-LP-82 dan TC-AUTH-LP-114 (pencatatan "Consent not given" di log) dibagi: pencatatan log diuji di spec `TC-AUTH-LP-E2E-038-log-success-and-consent`; spec ini hanya asersi UI.
- TC-AUTH-LP-148 (klik ganda [Continue ➔]) diuji di spec `TC-AUTH-LP-E2E-032-double-submit`.
- Langkah 25 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA: Post Condition "persetujuan Privacy Policy tersimpan untuk versi aktif" pada TC-AUTH-LP-83 tidak punya langkah observasi di TC, jadi spec tidak mengasersinya (S-01); TC tidak menyebut cara membaca state persetujuan, perlu Expected padanan atau langkah observasi dari tim QA.
