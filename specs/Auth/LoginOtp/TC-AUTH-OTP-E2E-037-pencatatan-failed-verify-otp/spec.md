---
id: TC-AUTH-OTP-E2E-037-pencatatan-failed-verify-otp
title: "Pencatatan Failed pada Verify OTP: Empty OTP dan Incorrect OTP"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-119
  - TC-AUTH-OTP-120
  - TC-AUTH-OTP-121
  - TC-AUTH-OTP-122
coverage:
  web: automated
---

# Pencatatan Failed pada Verify OTP: Empty OTP dan Incorrect OTP

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji; `Spectra.intercept()` untuk memaksa respons Verify OTP server error 500 pada TC-AUTH-OTP-119 (intercept parsial di atas backend nyata); percepatan jam server untuk melewati countdown Resend 60 detik pada TC-AUTH-OTP-121 (jam dipulihkan di hook `after`).
- Jam yang diatur (konvensi bagian 6): jam server dan jam browser (klien) dimajukan bersama, karena countdown Resend di UI berjalan di jam klien sehingga memajukan jam server saja tidak mengaktifkan [Resend code]. Hook `after` memulihkan kedua jam. Suite berjalan serial (`parallel: false`) karena jam server digeser.
- Hook `before` (seeding API) membuat user profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada) dengan suffix per run `+{runId}-037`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Jumlah baris awal tiap user di kedua surface log dicatat di hook:
  - TC-AUTH-OTP-119: `Anisa Puspita` (`anisapuspita+{runId}-037@qwertysystem.net`)
  - TC-AUTH-OTP-120: `Bagas Damayanti` (`bagasdamayanti+{runId}-037@qwertysystem.net`)
  - TC-AUTH-OTP-121: `Tiara Wibowo` (`tiarawibowo+{runId}-037@qwertysystem.net`)
  - TC-AUTH-OTP-122: `Rafi Wijaya` (`rafiwijaya+{runId}-037@qwertysystem.net`)
- Hook `after`: melepas intercept respons Verify OTP 500 bila masih terpasang, memulihkan jam server dan jam browser, dan menghapus keempat user.
- Kode salah adalah `000000` (sesuai TC-AUTH-OTP-120 dan TC-AUTH-OTP-122), berbeda dari kode di email.

## Test Steps

### TC-AUTH-OTP-119: Pencatatan Empty OTP pada Verify fallback sebelum 6 digit terisi

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `anisapuspita+{runId}-037@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Atur intercept respons Verify OTP menjadi server error 500
6. Ketik 6 digit kode OTP dari email pada kotak digit
7. Hapus digit terakhir sehingga 5 kotak terisi
8. Pulihkan respons Verify OTP menjadi normal (hapus intercept)
9. Klik button [Verify]
10. Ganti konteks ke browser admin Total Control (Global Settings), buka `Global Settings > Activity Log > Session`
11. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan kolom User `Anisa Puspita`, Activity `Login`, Status `Failed`, Note `Empty OTP`
12. Verifikasi kolom IP Address berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
13. Buka `Global Settings > User > Detail > User Log` untuk `Anisa Puspita`
14. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Empty OTP`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

### TC-AUTH-OTP-120: Pencatatan Incorrect OTP pada kode salah

15. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
16. Ketik `bagasdamayanti+{runId}-037@qwertysystem.net` pada field Email
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Request OTP]
19. Ketik 6 digit kode `000000` (berbeda dari kode di email)
20. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session`
21. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan kolom User `Bagas Damayanti`, Activity `Login`, Status `Failed`, Note `Incorrect OTP`
22. Verifikasi kolom IP Address berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
23. Buka `Global Settings > User > Detail > User Log` untuk `Bagas Damayanti`
24. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Incorrect OTP`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

### TC-AUTH-OTP-121: Pencatatan Incorrect OTP pada kode yang sudah diganti Resend meski benar dan belum 5 menit

25. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
26. Ketik `tiarawibowo+{runId}-037@qwertysystem.net` pada field Email
27. Centang widget reCAPTCHA "I'm not a robot"
28. Klik button [Request OTP]
29. Catat kode OTP pertama dari email
30. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
31. Klik [Resend code]
32. Ketik kode OTP pertama pada kotak digit
33. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session`
34. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan kolom User `Tiara Wibowo`, Activity `Login`, Status `Failed`, Note `Incorrect OTP`
35. Verifikasi kolom IP Address berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
36. Buka `Global Settings > User > Detail > User Log` untuk `Tiara Wibowo`
37. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Incorrect OTP`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

### TC-AUTH-OTP-122: Pencatatan Incorrect OTP pada percobaan ke-5 dan kode benar setelah 5 kali salah

38. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
39. Ketik `rafiwijaya+{runId}-037@qwertysystem.net` pada field Email
40. Centang widget reCAPTCHA "I'm not a robot"
41. Klik button [Request OTP]
42. Ketik 5 kali berturut-turut kode salah `000000`
43. Ketik 6 digit kode OTP benar dari email pada kotak digit
44. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session`
45. Verifikasi 6 baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Incorrect OTP` untuk user `Rafi Wijaya` (5 percobaan salah dan 1 percobaan kode benar yang ditolak)
46. Buka `Global Settings > User > Detail > User Log` untuk `Rafi Wijaya`
47. Verifikasi 6 baris baru yang sama dibanding baseline hook `before` dengan Activity, Status, dan Note identik

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini 47 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena empat blok TC berdiri sendiri (user terpisah per blok, jendela privat baru per blok), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan seluruh spec satu kelas (pencatatan Failed pada Verify OTP).
- Langkah penghubung (S-03): ganti konteks antara jendela privat dan browser admin, muat ulang Activity Log, dan intercept respons Verify OTP pada TC-AUTH-OTP-119 (pemicu kegagalan 5xx pada auto-submit agar fallback [Verify] muncul), ditulis sebagai aksi tanpa `Verifikasi`.
- Pengecualian P-2 (pemicu bukan objek uji): intercept respons 500 pada TC-AUTH-OTP-119 hanya memunculkan fallback [Verify] dan dilepas pada langkah 8; bukan objek asersi.
- Asersi absence untuk kegagalan 5xx auto-submit (tidak dicatat) berada di E2E-040 (TC-AUTH-OTP-131); spec ini hanya mengasersi satu baris `Empty OTP` hasil klik [Verify].
- Temuan untuk QA: TC-AUTH-OTP-119 tidak menyebut apakah auto-submit yang gagal 500 pada langkah 6 menimbulkan baris log; Expected hanya satu baris `Empty OTP` (konsisten dengan TC-AUTH-OTP-131). Caption layar Verify OTP untuk kode salah ("Invalid code") tidak diasersi di sini karena bukan bagian Expected TC pencatatan.
