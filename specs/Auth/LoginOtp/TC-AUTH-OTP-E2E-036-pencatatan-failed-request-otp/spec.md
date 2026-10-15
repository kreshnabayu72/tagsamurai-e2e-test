---
id: TC-AUTH-OTP-E2E-036-pencatatan-failed-request-otp
title: "Pencatatan Failed pada Request OTP: Captcha not completed, Account is not activated, Account is inactive"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-116
  - TC-AUTH-OTP-117
  - TC-AUTH-OTP-118
coverage:
  web: automated
---

# Pencatatan Failed pada Request OTP: Captcha not completed, Account is not activated, Account is inactive

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API; Login with OTP tidak memakai password). Tidak ada password atau token di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); reCAPTCHA mode uji di environment.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-036`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Jumlah baris awal user baru di kedua surface log dicatat di hook sehingga "baris baru" dihitung terhadap kondisi awal itu (S-12):
  - TC-AUTH-OTP-116: `Galih Santoso` (`galihsantoso+{runId}-036@qwertysystem.net`), profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada)
  - TC-AUTH-OTP-117: `Citra Lestari` (`citralestari+{runId}-036@qwertysystem.net`), profil PENDING (Pending Activation, Active ON)
  - TC-AUTH-OTP-118: `Joko Wulandari` (`jokowulandari+{runId}-036@qwertysystem.net`), profil INACTIVE (Activated, Toggle Global Active OFF)
- Tanpa login pada konteks publik: halaman Login with OTP adalah halaman publik, tidak ada sesi aktif di jendela privat.

## Test Steps

### TC-AUTH-OTP-116: Pencatatan Captcha not completed pada Request OTP tanpa reCAPTCHA

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `galihsantoso+{runId}-036@qwertysystem.net` pada field Email
3. Biarkan widget reCAPTCHA tidak dicentang
4. Klik button [Request OTP]
5. Ganti konteks ke browser admin Total Control (Global Settings), buka `Global Settings > Activity Log > Session`
6. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan kolom User `Galih Santoso`, Activity `Login`, Status `Failed`, Note `Captcha not completed`
7. Verifikasi kolom IP Address pada baris itu berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
8. Buka `Global Settings > User > Detail > User Log` untuk `Galih Santoso`
9. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Captcha not completed`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

### TC-AUTH-OTP-117: Pencatatan Account is not activated pada Request OTP akun yang belum aktivasi

10. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
11. Ketik `citralestari+{runId}-036@qwertysystem.net` pada field Email
12. Centang widget reCAPTCHA "I'm not a robot"
13. Klik button [Request OTP]
14. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session`
15. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan kolom User `Citra Lestari`, Activity `Login`, Status `Failed`, Note `Account is not activated`
16. Verifikasi kolom IP Address pada baris itu berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
17. Buka `Global Settings > User > Detail > User Log` untuk `Citra Lestari`
18. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Account is not activated`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

### TC-AUTH-OTP-118: Pencatatan Account is inactive pada Request OTP akun yang inactive

19. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
20. Ketik `jokowulandari+{runId}-036@qwertysystem.net` pada field Email
21. Centang widget reCAPTCHA "I'm not a robot"
22. Klik button [Request OTP]
23. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session`
24. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan kolom User `Joko Wulandari`, Activity `Login`, Status `Failed`, Note `Account is inactive`
25. Verifikasi kolom IP Address pada baris itu berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
26. Buka `Global Settings > User > Detail > User Log` untuk `Joko Wulandari`
27. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Account is inactive`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Langkah penghubung (S-03): ganti konteks antara jendela privat dan browser admin, serta muat ulang Activity Log, ditulis sebagai aksi tanpa `Verifikasi`.
- Caption penolakan di layar Request OTP (reCAPTCHA, "Your account has not been activated", "Your account is inactive") tidak diasersi di spec ini karena bukan bagian Expected Result TC pencatatan; caption itu diasersi di spec fungsional validasi dan status akun. Spec ini hanya memuat sisi pencatatan.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA: TC-AUTH-OTP-116, 117, dan 118 tidak menyebut jumlah baris awal log; spec ini menghitung "baris baru" terhadap kondisi awal user hasil seeding (dicatat di hook).
