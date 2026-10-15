---
id: TC-AUTH-OTP-E2E-038-pencatatan-failed-consent-dan-email-changed
title: "Pencatatan Failed: Account is inactive saat Verify, OTP invalid — email changed, dan Consent not given"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-124
  - TC-AUTH-OTP-125
  - TC-AUTH-OTP-126
coverage:
  web: automated
---

# Pencatatan Failed: Account is inactive saat Verify, OTP invalid — email changed, dan Consent not given

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`. Akun ini juga dipakai langkah uji untuk mematikan Toggle Active user (TC-AUTH-OTP-124).
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-038`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Jumlah baris awal tiap user di kedua surface log dicatat di hook:
  - TC-AUTH-OTP-124: `Surya Fitriani` (`suryafitriani+{runId}-038@qwertysystem.net`), profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada)
  - TC-AUTH-OTP-125: `Nadia Susanti` (`nadiasusanti+{runId}-038@qwertysystem.net`) dan `Teguh Lubis` (`teguhlubis+{runId}-038@qwertysystem.net`), keduanya profil BASE
  - TC-AUTH-OTP-126: `Laras Suryani` (`larassuryani+{runId}-038@qwertysystem.net`), profil POLICY (seperti BASE, tetapi Principal sudah mempublish versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu)
- Konfigurasi: akun Principal di atas menerbitkan versi Privacy Policy terbaru sebelum `Laras Suryani` di-seed (hook `before`). Urutan hook `before`: Principal lebih dulu menerbitkan versi Privacy Policy, lalu user profil BASE di-seed dengan persetujuan versi terbaru dan user profil POLICY di-seed dengan persetujuan versi sebelumnya. Versi yang diterbitkan adalah state global yang tidak ditarik kembali oleh hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AUTH-OTP-124: Pencatatan Account is inactive pada Verify OTP setelah akun dinonaktifkan

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `suryafitriani+{runId}-038@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ganti konteks ke browser admin Total Control (Global Settings), matikan Toggle Active untuk `Surya Fitriani` di `Global Settings > User`
6. Ganti konteks ke jendela privat, ketik 6 digit kode OTP dari email pada kotak digit
7. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session`
8. Verifikasi tepat satu baris baru dengan kolom User `Surya Fitriani`, Activity `Login`, Status `Failed`, Note `Account is inactive`
9. Verifikasi kolom IP Address berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
10. Buka `Global Settings > User > Detail > User Log` untuk `Surya Fitriani`
11. Verifikasi tepat satu baris baru dengan Activity `Login`, Status `Failed`, Note `Account is inactive`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

### TC-AUTH-OTP-125: Pencatatan OTP invalid — email changed pada kode dari email sebelumnya

12. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `nadiasusanti+{runId}-038@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Klik button [Request OTP]
16. Catat kode OTP dari email `nadiasusanti+{runId}-038@qwertysystem.net`
17. Klik tautan [Edit email]
18. Ubah email menjadi `teguhlubis+{runId}-038@qwertysystem.net`, centang widget reCAPTCHA "I'm not a robot", klik button [Request OTP]
19. Ketik kode OTP milik `nadiasusanti+{runId}-038@qwertysystem.net` pada halaman Verify OTP `teguhlubis+{runId}-038@qwertysystem.net`
20. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session`
21. Verifikasi tepat satu baris baru Activity `Login`, Status `Failed`, Note `OTP invalid — email changed` pada user `Teguh Lubis` (pemilik email di layar Verify)
22. Buka `Global Settings > User > Detail > User Log` untuk `Teguh Lubis`
23. Verifikasi tepat satu baris baru Activity `Login`, Status `Failed`, Note `OTP invalid — email changed`
24. Buka `Global Settings > User > Detail > User Log` untuk `Nadia Susanti`
25. Verifikasi tidak ada baris baru di User Log `Nadia Susanti`

### TC-AUTH-OTP-126: Pencatatan Consent not given satu kali per klik Continue tanpa centang yang ditolak server

26. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
27. Ketik `larassuryani+{runId}-038@qwertysystem.net` pada field Email
28. Centang widget reCAPTCHA "I'm not a robot"
29. Klik button [Request OTP]
30. Ketik 6 digit kode OTP dari email pada kotak digit
31. Klik button [Continue ➔] tanpa mencentang checkbox
32. Klik button [Continue ➔] sekali lagi tanpa mencentang checkbox
33. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session`
34. Verifikasi tepat 2 baris baru Activity `Login`, Status `Failed`, Note `Consent not given` untuk user `Laras Suryani` (satu per klik)
35. Buka `Global Settings > User > Detail > User Log` untuk `Laras Suryani`
36. Verifikasi 2 baris yang sama dengan Activity, Status, dan Note identik

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini 36 langkah, di sekitar batas smell sekitar 35 langkah (prinsip 13); tiga blok TC berdiri sendiri (user dan jendela privat terpisah per blok) dan seluruh spec satu kelas (pencatatan Failed).
- Langkah penghubung (S-03): ganti konteks antara jendela privat dan browser admin, muat ulang Activity Log, dan klik [Edit email] untuk mengganti email pada TC-AUTH-OTP-125, ditulis sebagai aksi tanpa `Verifikasi`.
- Caption layar (misalnya "Invalid code" pada kode dari email lain, caption Consent not given pada layar Confirm to Continue) tidak diasersi di spec ini karena bukan bagian Expected Result TC pencatatan; caption diasersi di spec fungsional verify dan Agreement Gate.
- Temuan untuk QA: Label button `[Continue ➔]` pada TC-AUTH-OTP-126 memakai glyph, sedangkan NC-17 menetapkan ikon dekoratif tidak di-assert pada tautan; spec mengikuti teks TC untuk button.
