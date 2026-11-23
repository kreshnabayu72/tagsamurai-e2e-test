---
id: TC-AUTH-OTP-E2E-016-verify-sukses-tanpa-gate
title: "Verify OTP Berhasil Langsung ke Product Hub tanpa Agreement dan MFA"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-10
  - TC-AUTH-OTP-48
  - TC-AUTH-OTP-100
  - TC-AUTH-OTP-197
coverage:
  web: automated
---

# Verify OTP Berhasil Langsung ke Product Hub tanpa Agreement dan MFA

## Prerequisites

- Mode: FE+BE.
- Tidak ada akun aktor. Browser tanpa sesi login (halaman Login with OTP adalah halaman publik).
- Environment variable: `OTP_PASSWORD` (password user uji yang dipasang saat seeding; tidak ada password atau token di spec atau fixture). Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-016`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir sehingga bukan login pertama dan device dikenal, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-10: `Agus Wijaya` (`aguswijaya+{runId}-016@qwertysystem.net`), role di Global Settings: Read Only
  - TC-AUTH-OTP-48: `Sinta Pratama` (`sintapratama+{runId}-016@qwertysystem.net`)
  - TC-AUTH-OTP-100: `Agus Nugroho` (`agusnugroho+{runId}-016@qwertysystem.net`)
  - TC-AUTH-OTP-197: `Andi Purnama` (`andipurnama+{runId}-016@qwertysystem.net`)
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji di environment (centang tanpa tantangan); pengamatan permintaan jaringan browser (TC-AUTH-OTP-100: tidak ada permintaan konfirmasi Agreement; TC-AUTH-OTP-197: isi payload request Verify OTP).
- State yang berubah: keempat TC diakhiri dengan login sukses; langkah logout dari Portal — Product Hub ada di antara TC dan hook `after` menutup sesi yang tersisa.

## Test Steps

### TC-AUTH-OTP-10: Halaman Login with OTP dapat dipakai tanpa gate role atau capability oleh pengguna dengan role Read Only

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Verifikasi halaman Request OTP tampil tanpa pesan izin akses
3. Ketik `aguswijaya+{runId}-016@qwertysystem.net` pada field Email
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Request OTP]
6. Verifikasi toast sukses "Success, the code has been sent." tampil
7. Verifikasi halaman Verify OTP terbuka
8. Ketik 6 digit kode dari email (mail-catcher `aguswijaya+{runId}-016@qwertysystem.net`) pada kotak digit
9. Verifikasi browser dialihkan ke Portal — Product Hub
10. Verifikasi sesi aktif untuk `Agus Wijaya`

### TC-AUTH-OTP-48: Verify OTP dengan kode benar tanpa Agreement dan MFA membuat sesi dan masuk Product Hub

11. Logout dari Portal — Product Hub dan buka halaman `Auth > Login with OTP > Request OTP`
12. Ketik `sintapratama+{runId}-016@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
13. Ketik 6 digit kode OTP dari email (mail-catcher `sintapratama+{runId}-016@qwertysystem.net`) pada kotak digit
14. Verifikasi verifikasi berjalan otomatis pada digit ke-6 tanpa ada button [Verify] yang diklik
15. Verifikasi layar Confirm to Continue tidak tampil
16. Verifikasi halaman MFA tidak tampil
17. Verifikasi browser dialihkan ke Portal — Product Hub
18. Verifikasi sesi aktif untuk `Sinta Pratama`

### TC-AUTH-OTP-100: Tanpa kondisi Agreement layar Confirm to Continue dilewati total

19. Logout dari Portal — Product Hub dan buka halaman `Auth > Login with OTP > Request OTP`
20. Ketik `agusnugroho+{runId}-016@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
21. Ketik 6 digit kode OTP dari email (mail-catcher `agusnugroho+{runId}-016@qwertysystem.net`) pada kotak digit
22. Verifikasi layar Confirm to Continue tidak tampil sama sekali
23. Verifikasi tidak ada permintaan konfirmasi Agreement yang dikirim
24. Verifikasi browser dialihkan ke Portal — Product Hub
25. Verifikasi sesi aktif untuk `Agus Nugroho`

### TC-AUTH-OTP-197: Verify OTP di web tidak meminta reCAPTCHA atau attestation pada sesi Request yang diterima

26. Logout dari Portal — Product Hub dan buka halaman `Auth > Login with OTP > Request OTP`
27. Ketik `andipurnama+{runId}-016@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
28. Verifikasi halaman Verify OTP tidak menampilkan widget reCAPTCHA
29. Ketik 6 digit kode OTP dari email (mail-catcher `andipurnama+{runId}-016@qwertysystem.net`) pada kotak digit
30. Verifikasi payload request Verify OTP tidak memuat `recaptchaToken` maupun `integrityToken`
31. Verifikasi Verify diterima tanpa meminta centang reCAPTCHA: browser dialihkan ke Portal — Product Hub
32. Verifikasi sesi aktif untuk `Andi Purnama`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 11, 19, dan 26 adalah langkah penghubung antar-TC (S-03, S-09): logout dari sesi hasil TC sebelumnya lalu buka ulang halaman Request OTP agar konteks bersih. Langkah 12, 20, dan 27 menggabungkan ketik email, centang reCAPTCHA, dan klik [Request OTP] menjadi satu baris karena persis sama dengan prasyarat TC.
- TC-AUTH-OTP-48 dan TC-AUTH-OTP-100 hampir identik (login BASE sampai Product Hub); keduanya dipertahankan karena Expected-nya berbeda (verifikasi otomatis tanpa klik dan tidak ada MFA pada TC-AUTH-OTP-48, tidak ada permintaan konfirmasi Agreement pada TC-AUTH-OTP-100).
- Temuan untuk QA: (1) TC-AUTH-OTP-10 menyebut "role di Global Settings: Read Only" tetapi tidak menyebut cara menyiapkan role itu pada user seeding; spec memakai seeding API dengan role Read Only. (2) TC-AUTH-OTP-100 butir a "tidak ada permintaan konfirmasi Agreement yang dikirim" memerlukan pengamatan permintaan jaringan yang tidak disebut di TC. (3) Post Condition TC-AUTH-OTP-48 b (kode berstatus terpakai) dan c (entri Success `Login with OTP` di Activity Log Session dan User Log) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini; kode terpakai diuji di spec defense-in-depth (TC-AUTH-OTP-155) dan pencatatan Success di spec pencatatan Success (TC-AUTH-OTP-127). (4) TC-AUTH-OTP-197 langkah 7 memeriksa payload request Verify lewat developer tools (`Manual Only` di TC sumber); spec memakai pengamatan permintaan jaringan browser (Prerequisites) agar dapat diotomasi.
