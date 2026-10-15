---
id: TC-AUTH-OTP-E2E-039-pencatatan-success-dan-struktur-log
title: "Pencatatan Success Login with OTP dan Struktur Kolom Surface Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-127
  - TC-AUTH-OTP-128
  - TC-AUTH-OTP-136
  - TC-AUTH-OTP-137
coverage:
  web: automated
---

# Pencatatan Success Login with OTP dan Struktur Kolom Surface Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji. TC-AUTH-OTP-136 mengasersi Device / Browser `Chrome on Windows`: browser dan OS pada environment run harus Chrome di Windows.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-039`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Jumlah baris awal tiap user di kedua surface log dicatat di hook:
  - TC-AUTH-OTP-127: `Irfan Hidayati` (`irfanhidayati+{runId}-039@qwertysystem.net`), profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada; Agreement dan MFA tidak terpicu)
  - TC-AUTH-OTP-128: `Sinta Anggraini` (`sintaanggraini+{runId}-039@qwertysystem.net`), profil POLICY (seperti BASE, tetapi Principal sudah mempublish versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu)
  - TC-AUTH-OTP-136: `Dewi Lubis` (`dewilubis+{runId}-039@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-137: `Rizky Suryani` (`rizkysuryani+{runId}-039@qwertysystem.net`) dan `Nur Hidayati` (`nurhidayati+{runId}-039@qwertysystem.net`), keduanya profil BASE
- Konfigurasi: akun Principal di atas menerbitkan versi Privacy Policy terbaru sebelum `Sinta Anggraini` di-seed (hook `before`). Urutan hook `before`: Principal lebih dulu menerbitkan versi Privacy Policy, lalu user profil BASE di-seed dengan persetujuan versi terbaru dan user profil POLICY di-seed dengan persetujuan versi sebelumnya. Versi yang diterbitkan adalah state global yang tidak ditarik kembali oleh hook `after`; suite berjalan serial (`parallel: false`).
- Kode salah adalah `000000` (sesuai TC-AUTH-OTP-136 dan TC-AUTH-OTP-137), berbeda dari kode di email.

## Test Steps

### TC-AUTH-OTP-127: Pencatatan Login with OTP Success pada login tanpa Agreement dan MFA

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `irfanhidayati+{runId}-039@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ketik 6 digit kode OTP dari email pada kotak digit
6. Ganti konteks ke browser admin Total Control (Global Settings), buka `Global Settings > Activity Log > Session`
7. Verifikasi tepat satu baris baru dengan kolom User `Irfan Hidayati`, Activity `Login`, Status `Success`, Note `Login with OTP`
8. Verifikasi kolom IP Address berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
9. Buka `Global Settings > User > Detail > User Log` untuk `Irfan Hidayati`
10. Verifikasi tepat satu baris baru dengan Activity `Login`, Status `Success`, Note `Login with OTP`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

### TC-AUTH-OTP-128: Login with OTP Success dicatat sekali setelah Agreement dikonfirmasi

11. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
12. Ketik `sintaanggraini+{runId}-039@qwertysystem.net` pada field Email
13. Centang widget reCAPTCHA "I'm not a robot"
14. Klik button [Request OTP]
15. Ketik 6 digit kode OTP dari email pada kotak digit
16. Ganti konteks ke jendela privat, centang checkbox "I have read and agree to the Privacy Policy *"
17. Klik button [Continue ➔]
18. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Sinta Anggraini`
19. Verifikasi di `Global Settings > Activity Log > Session` tepat satu baris baru dengan kolom User `Sinta Anggraini`, Activity `Login`, Status `Success`, Note `Login with OTP`
20. Verifikasi kolom IP Address berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
21. Verifikasi di `Global Settings > User > Detail > User Log` tepat satu baris baru dengan Activity `Login`, Status `Success`, Note `Login with OTP`, serta IP Address dan Device / Browser yang sama dengan baris di Activity Log Session

### TC-AUTH-OTP-136: Struktur kolom surface log untuk percobaan Login with OTP

22. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
23. Ketik `dewilubis+{runId}-039@qwertysystem.net` pada field Email
24. Centang widget reCAPTCHA "I'm not a robot"
25. Klik button [Request OTP]
26. Ketik 6 digit kode `000000` (berbeda dari kode di email)
27. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session` lalu `Global Settings > User > Detail > User Log` untuk `Dewi Lubis`
28. Verifikasi header kolom `Global Settings > Activity Log > Session` berurutan: Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address | Device / Browser
29. Verifikasi header kolom `Global Settings > User > Detail > User Log` berurutan: Date | Activity | Status | Note | IP Address | Device / Browser
30. Verifikasi baris terbaru berisi Activity `Login`, Status `Failed`, Note `Incorrect OTP` pada kedua surface
31. Verifikasi kolom Device / Browser pada baris terbaru berisi `Chrome on Windows` dan kolom IP Address berisi alamat IP browser uji

### TC-AUTH-OTP-137: Satu percobaan menghasilkan satu entri per surface dan tidak ada entri untuk user lain

32. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
33. Ketik `rizkysuryani+{runId}-039@qwertysystem.net` pada field Email
34. Centang widget reCAPTCHA "I'm not a robot"
35. Klik button [Request OTP]
36. Ketik 6 digit kode `000000` (berbeda dari kode di email)
37. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session`
38. Verifikasi tepat satu baris baru Failed `Incorrect OTP` untuk user `Rizky Suryani` di `Global Settings > Activity Log > Session`
39. Buka `Global Settings > User > Detail > User Log` untuk `Rizky Suryani`
40. Verifikasi tepat satu baris baru Failed `Incorrect OTP` di User Log milik `Rizky Suryani`
41. Buka `Global Settings > User > Detail > User Log` untuk `Nur Hidayati`
42. Verifikasi tidak ada baris baru di User Log milik `Nur Hidayati`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini 42 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena empat blok TC berdiri sendiri (user terpisah per blok, jendela privat baru per blok), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan seluruh spec satu kelas (struktur dan pencatatan surface log).
- Langkah penghubung (S-03): ganti konteks antara jendela privat dan browser admin serta muat ulang kedua surface log ditulis sebagai aksi tanpa `Verifikasi`. Asersi absence TC-AUTH-OTP-128 (butir a: tidak ada baris Success sebelum Continue; butir d: tidak ada baris Note lain untuk konfirmasi Agreement) dipindah ke E2E-040 Bagian D (S-05, prinsip 13g); spec ini hanya memuat butir b dan c (tepat satu baris Success di kedua surface log), dan pembagian ini dicatat juga di Notes E2E-040. Baseline jumlah baris `Sinta Anggraini` dicatat di hook `before` (S-12).
- Login with OTP Success yang dicatat sekali di titik final setelah MFA tuntas (TC-AUTH-OTP-129) ada di spec handoff MFA; Failed yang tidak dicatat (absence) ada di E2E-040.
- Temuan untuk QA: TC-AUTH-OTP-136 mengasersi nilai `Chrome on Windows`, yang bergantung pada browser dan OS runner; bila runner bukan Chrome di Windows asersi ini gagal tanpa ada cacat aplikasi. Nama tampilan user seeding mengikuti TC dan sama di setiap run (hanya email yang bersuffix), dan `Sinta Anggraini` juga dipakai spec E2E-040; baris Activity Log Session dikenali lewat nama sehingga bisa tertukar bila ada user lain bernama sama (TC tidak memberi nama unik). Selain itu Expected TC-AUTH-OTP-137 tidak menyebut baris Success/Failed lain untuk `Nur Hidayati`; spec membaca "tidak ada entri untuk user lain" sebagai tidak ada baris baru sama sekali.
