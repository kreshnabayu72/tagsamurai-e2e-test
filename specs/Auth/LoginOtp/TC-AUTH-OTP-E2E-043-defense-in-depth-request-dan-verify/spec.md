---
id: TC-AUTH-OTP-E2E-043-defense-in-depth-request-dan-verify
title: "Defense-in-Depth: Payload Script, Klaim Mobile Tanpa Bukti, Resend Sebelum Cooldown, Token Diubah, dan Kode Terpakai"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-157
  - TC-AUTH-OTP-154
  - TC-AUTH-OTP-84
  - TC-AUTH-OTP-161
  - TC-AUTH-OTP-155
coverage:
  web: automated
---

# Defense-in-Depth: Payload Script, Klaim Mobile Tanpa Bukti, Resend Sebelum Cooldown, Token Diubah, dan Kode Terpakai

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: klien HTTP untuk mengirim request langsung ke server (melewati UI yang menonaktifkan tombol): Request OTP dan Resend lewat `/v2/iam/auth/otp/request` serta Verify OTP lewat `/v2/iam/auth/otp/verify` sesuai `auth/login-otp/API/openapi.yaml`; endpoint Confirm Agreement (TC-AUTH-OTP-161) hanya dirujuk sebagai target preAuthToken di openapi.yaml:745 tanpa path item, sehingga path-nya ditentukan di tahap script (lihat Temuan untuk QA butir 6); kemampuan mengamati sesi yang dibuat untuk satu user (daftar atau jumlah sesi per user lewat API sesi atau DB lingkungan uji; bentuk pastinya ditentukan di tahap script, lihat Temuan untuk QA butir 5) untuk Expected TC-AUTH-OTP-161 a dan TC-AUTH-OTP-155 a; pembacaan token pra-autentikasi dari respons Verify OTP pada TC-AUTH-OTP-161 untuk diubah satu karakter; dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit dan memeriksa tidak ada email terkirim; reCAPTCHA mode uji. Tidak ada jam yang digeser: TC-AUTH-OTP-84 memakai waktu nyata (permintaan Resend langsung dikirim pada detik ke-10 setelah Request OTP).
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-043`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Jumlah baris awal tiap user di kedua surface log dicatat di hook:
  - TC-AUTH-OTP-154: `Wulan Cahyono` (`wulancahyono+{runId}-043@qwertysystem.net`), profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada)
  - TC-AUTH-OTP-84: `Rafi Mulyadi` (`rafimulyadi+{runId}-043@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-161: `Tiara Halim` (`tiarahalim+{runId}-043@qwertysystem.net`), profil POLICY (seperti BASE, tetapi Principal sudah mempublish versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu)
  - TC-AUTH-OTP-155: `Galih Kusuma` (`galihkusuma+{runId}-043@qwertysystem.net`), profil BASE
- TC-AUTH-OTP-157 tidak memakai user: payload `<script>alert(1)</script>@qwertysystem.net` tidak terdaftar di Global Settings > User.
- Konfigurasi: akun Principal di atas menerbitkan versi Privacy Policy terbaru sebelum `Tiara Halim` di-seed (hook `before`). Urutan hook `before`: Principal lebih dulu menerbitkan versi Privacy Policy, lalu user profil BASE di-seed dengan persetujuan versi terbaru dan user profil POLICY di-seed dengan persetujuan versi sebelumnya. Versi yang diterbitkan adalah state global yang tidak ditarik kembali oleh hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AUTH-OTP-157: Payload script pada field Email tidak dieksekusi

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `<script>alert(1)</script>@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi caption error di bawah field Email: "Email is not registered yet"
6. Verifikasi tidak ada dialog atau skrip yang dieksekusi di halaman
7. Verifikasi teks payload tidak dirender sebagai HTML
8. Verifikasi tidak ada email OTP terkirim di mail-catcher untuk alamat payload

### TC-AUTH-OTP-154: Permintaan yang mengaku mobile tanpa bukti klien valid diperlakukan sebagai web dan wajib reCAPTCHA

9. Kirim permintaan Request OTP langsung ke server dengan email `wulancahyono+{runId}-043@qwertysystem.net`, platform `mobile`, tanpa token reCAPTCHA dan tanpa token attestation mobile yang valid
10. Verifikasi permintaan ditolak karena tidak ada token attestation mobile yang valid sehingga diperlakukan sebagai web dan wajib token reCAPTCHA (kosong)
11. Verifikasi tidak ada email OTP terkirim di mail-catcher untuk `wulancahyono+{runId}-043@qwertysystem.net`
12. Di browser admin, buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Wulan Cahyono`
13. Verifikasi entri Failed dengan Note "Captcha not completed" ditulis sebagai baris baru dibanding baseline hook `before` untuk `Wulan Cahyono` (baseline dicatat per user) di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`

### TC-AUTH-OTP-84: Resend yang dikirim langsung ke server sebelum cooldown selesai ditolak

14. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
15. Ketik `rafimulyadi+{runId}-043@qwertysystem.net` pada field Email
16. Centang widget reCAPTCHA "I'm not a robot"
17. Klik button [Request OTP]
18. Pada detik ke-10 setelah Request OTP (sebelum 60 detik berlalu), kirim permintaan Resend langsung ke server (melewati UI yang menonaktifkan tombol)
19. Verifikasi permintaan ditolak server
20. Verifikasi area Resend tetap pada state cooldown
21. Verifikasi tidak ada toast maupun caption baru
22. Verifikasi tidak ada email OTP kedua yang terkirim di mail-catcher untuk `rafimulyadi+{runId}-043@qwertysystem.net`

### TC-AUTH-OTP-161: Token pra-autentikasi yang diubah atau tidak dikenal tidak dapat dipakai mengonfirmasi Agreement

23. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
24. Ketik `tiarahalim+{runId}-043@qwertysystem.net` pada field Email
25. Centang widget reCAPTCHA "I'm not a robot"
26. Klik button [Request OTP]
27. Ketik 6 digit kode OTP dari email pada kotak digit
28. Kirim permintaan konfirmasi Agreement langsung ke server dengan token pra-autentikasi yang nilainya diubah satu karakter dan agreementAccepted bernilai setuju
29. Verifikasi permintaan ditolak server
30. Verifikasi tidak ada sesi yang dibuat untuk `Tiara Halim`
31. Pada layar Confirm to Continue yang masih terbuka, centang checkbox "I have read and agree to the Privacy Policy *"
32. Klik button [Continue ➔]
33. Verifikasi token asli masih berlaku: browser dialihkan ke Portal — Product Hub
34. Verifikasi sesi aktif untuk `Tiara Halim`

### TC-AUTH-OTP-155: Kode OTP yang sudah dipakai ditolak saat dikirim ulang langsung ke server

35. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
36. Ketik `galihkusuma+{runId}-043@qwertysystem.net` pada field Email
37. Centang widget reCAPTCHA "I'm not a robot"
38. Klik button [Request OTP]
39. Ketik 6 digit kode OTP dari email pada kotak digit
40. Logout dari Portal — Product Hub
41. Kirim permintaan Verify OTP langsung ke server dengan email `galihkusuma+{runId}-043@qwertysystem.net` dan kode OTP yang sudah dipakai tadi
42. Verifikasi permintaan ditolak server
43. Verifikasi tidak ada sesi baru yang dibuat untuk `Galih Kusuma`
44. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Galih Kusuma`
45. Verifikasi di kedua surface log terdapat tepat satu baris Success `Login with OTP` (login pertama)
46. Verifikasi di kedua surface log terdapat tepat satu baris Failed `Incorrect OTP` (percobaan kode terpakai)

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness a (defense-in-depth: manipulasi token, request langsung ke server). Spec ini 46 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena lima blok TC berdiri sendiri (user dan jendela privat terpisah per blok) dan seluruh spec satu kelas.
- TC defense-in-depth yang bergantung kuota Resend habis (TC-AUTH-OTP-162, 163, 171, 178) ada di E2E-044 karena butuh state berat (5 kali Resend); TC-AUTH-OTP-153, 156, 160, dan 172 hanya-BE.
- Pembagian asersi absence (S-05): asersi "tidak ada entri log baru" pada TC-AUTH-OTP-157 (Expected d) dipindah ke E2E-047 (prinsip 13g); blok TC-AUTH-OTP-157 spec ini hanya memuat asersi fungsional (caption, tidak ada skrip dieksekusi, tidak ada email OTP). Pembagian TC dicatat juga di Notes E2E-047.
- Urutan TC di dalam spec berbeda dari nomor TC: TC-AUTH-OTP-157 (tanpa user) dan TC-AUTH-OTP-154 (tanpa login) di awal, lalu TC-AUTH-OTP-84, TC-AUTH-OTP-161, dan TC-AUTH-OTP-155 yang menyelesaikan login di akhir (S-10).
- Langkah penghubung (S-03): ganti konteks antara jendela privat dan browser admin, serta logout dari Product Hub pada langkah 40 (TC-AUTH-OTP-155 langkah 6), ditulis sebagai aksi tanpa `Verifikasi`.
- Temuan untuk QA: (1) TC-AUTH-OTP-154 tidak menyebut bentuk "token attestation tidak valid" (kosong, rusak, atau kedaluwarsa); spec mengikuti TC dengan "tanpa token attestation mobile yang valid". (2) Expected TC-AUTH-OTP-84 tidak menyebut kode error atau status HTTP penolakan; spec hanya mengasersi perilaku yang terlihat (cooldown tetap, tanpa toast atau caption, tanpa email kedua). (3) TC-AUTH-OTP-157 memakai alamat `<script>alert(1)</script>@qwertysystem.net` dan mengharapkan caption "Email is not registered yet", padahal alamat itu belum tentu lolos cek format; urutan evaluasi format lalu lookup tidak dijelaskan di TC. (4) TC-AUTH-OTP-155 Expected a tidak menyebut caption layar; asersi hanya pada penolakan dan jumlah baris log. (5) Expected TC-AUTH-OTP-161 a dan TC-AUTH-OTP-155 a ("tidak ada sesi yang dibuat") tidak menyebut mekanisme pengamatan sesi; spec memerlukan kemampuan membaca sesi per user (API sesi atau DB) tanpa menyebut endpoint karena tidak tertulis di TC, PRD, atau OpenAPI modul ini. Post Condition TC-AUTH-OTP-155 a ("hanya satu sesi hasil login pertama yang pernah dibuat dari kode tersebut") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); hanya Expected a (tidak ada sesi baru) yang diasersi. (6) Endpoint Confirm Agreement tidak punya path item di openapi.yaml modul ini; path hanya dirujuk sebagai target preAuthToken di openapi.yaml:745. Yang punya path item adalah `/v2/iam/auth/otp/request` (melayani Request OTP dan Resend) dan `/v2/iam/auth/otp/verify` (melayani Verify). TC-AUTH-OTP-161 menyebut "permintaan konfirmasi Agreement langsung ke server" tanpa path, dan spec tidak mengarang endpoint.
