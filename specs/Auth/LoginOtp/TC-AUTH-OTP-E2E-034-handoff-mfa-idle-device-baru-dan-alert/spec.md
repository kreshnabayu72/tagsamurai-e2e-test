---
id: TC-AUTH-OTP-E2E-034-handoff-mfa-idle-device-baru-dan-alert
title: "Handoff ke MFA untuk Idle 30 Hari, Device Baru, dan Email Alert Login Tak Biasa"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-98
  - TC-AUTH-OTP-113
  - TC-AUTH-OTP-114
  - TC-AUTH-OTP-174
coverage:
  web: automated
---

# Handoff ke MFA untuk Idle 30 Hari, Device Baru, dan Email Alert Login Tak Biasa

## Prerequisites

- Mode: FE+BE (backend nyata; sesi dan email alert dibuktikan lewat perilaku UI dan mail-catcher).
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy sebelum semua user di-seed (profil IDLE, POLNEW, dan NEWDEV), bukan oleh langkah uji.
- Environment variable: `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Tidak ada password, token, atau secret TOTP di spec atau fixture.
- Hook `before`: Principal menerbitkan versi Privacy Policy terbaru lebih dulu, baru kemudian semua user di bawah ini (termasuk `Taufik Purnama` profil NEWDEV) di-seed. Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-034`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - Profil IDLE (Activated, Active ON; logout web terakhir 31 hari yang lalu, diatur lewat seed data waktu; Authenticator sudah terdaftar; Agreement dan MFA terpicu):
    - TC-AUTH-OTP-98: `Rizky Tanjung` (`rizkytanjung+{runId}-034@qwertysystem.net`)
    - TC-AUTH-OTP-113: `Ratna Prasetyo` (`ratnaprasetyo+{runId}-034@qwertysystem.net`)
  - Profil POLNEW (seperti POLICY, yaitu Principal sudah mempublish versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user, tetapi login dari browser/device yang belum dikenali; Authenticator sudah terdaftar; Agreement dan MFA terpicu sekaligus):
    - TC-AUTH-OTP-174: `Fikri Wibowo` (`fikriwibowo+{runId}-034@qwertysystem.net`)
  - Profil NEWDEV (seperti BASE, tetapi login dari browser/device yang belum dikenali; Authenticator sudah terdaftar; hanya MFA terpicu):
    - TC-AUTH-OTP-114: `Taufik Purnama` (`taufikpurnama+{runId}-034@qwertysystem.net`)
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP dan email alert login tak biasa; klien HTTP yang mengirim permintaan Verify OTP langsung ke server tanpa melalui UI dengan email dan kode OTP yang sudah dipakai (TC-AUTH-OTP-98); seed data waktu logout terakhir 31 hari yang lalu (profil IDLE) dan seed device belum dikenali (profil NEWDEV dan POLNEW); Principal dengan hak publish Privacy Policy sehingga versi baru sudah terpublikasi sebelum profil POLNEW dipakai; reCAPTCHA mode uji. Isi email alert dimiliki modul `mfa`; spec ini hanya memverifikasi kehadiran dan jumlahnya.
- Konfigurasi: akun Principal di atas menerbitkan versi Privacy Policy terbaru sebelum semua user (`Rizky Tanjung`, `Ratna Prasetyo`, `Fikri Wibowo`, dan `Taufik Purnama`) di-seed (hook `before`). Versi yang diterbitkan adalah state global yang tidak ditarik kembali oleh hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AUTH-OTP-98: Idle lebih dari 30 hari memicu layar Confirm to Continue setelah OTP benar

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `rizkytanjung+{runId}-034@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ketik 6 digit kode OTP dari email pada kotak digit
6. Kirim permintaan Verify OTP langsung ke server dengan email `rizkytanjung+{runId}-034@qwertysystem.net` dan kode OTP yang sama yang dipakai pada langkah 5
7. Verifikasi layar Confirm to Continue tampil dengan Title "Confirm to Continue" (kondisi idle lebih dari 30 hari)
8. Buka Portal — Product Hub langsung di tab lain
9. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login
10. Verifikasi permintaan Verify OTP langsung pada langkah 6 ditolak server
11. Verifikasi tidak ada sesi yang dibuat

### TC-AUTH-OTP-113: Idle 30 hari: Agreement lalu langsung verifikasi Authenticator tanpa pilihan metode

12. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `ratnaprasetyo+{runId}-034@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Klik button [Request OTP]
16. Ketik 6 digit kode OTP dari email pada kotak digit
17. Centang checkbox "I have read and agree to the Privacy Policy *"
18. Klik button [Continue ➔]
19. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code` (Authenticator sudah terdaftar)
20. Verifikasi halaman "Choose verification method" tidak tampil dan tidak ada opsi OTP via email
21. Buka Portal — Product Hub langsung di tab lain
22. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login

### TC-AUTH-OTP-174: Agreement dan login tak biasa terpicu bersamaan: email alert terkirim setelah Agreement dikonfirmasi

23. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
24. Ketik `fikriwibowo+{runId}-034@qwertysystem.net` pada field Email
25. Centang widget reCAPTCHA "I'm not a robot"
26. Klik button [Request OTP]
27. Ketik 6 digit kode OTP dari email pada kotak digit
28. Verifikasi layar Confirm to Continue tampil
29. Buka email alert login tak biasa di mail-catcher `fikriwibowo+{runId}-034@qwertysystem.net` sebelum Continue
30. Verifikasi belum ada email alert login tak biasa di mail-catcher
31. Kembali ke layar Confirm to Continue, centang checkbox "I have read and agree to the Privacy Policy *"
32. Klik button [Continue ➔]
33. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code`
34. Buka kembali mail-catcher `fikriwibowo+{runId}-034@qwertysystem.net`
35. Verifikasi tepat satu email alert login tak biasa diterima

### TC-AUTH-OTP-114: Login tak biasa tanpa Agreement: langsung verifikasi Authenticator dan email alert terkirim

36. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
37. Ketik `taufikpurnama+{runId}-034@qwertysystem.net` pada field Email
38. Centang widget reCAPTCHA "I'm not a robot"
39. Klik button [Request OTP]
40. Ketik 6 digit kode OTP dari email pada kotak digit
41. Verifikasi layar Confirm to Continue tidak tampil
42. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code` tanpa halaman pilihan metode
43. Verifikasi email alert login tak biasa diterima di mail-catcher `taufikpurnama+{runId}-034@qwertysystem.net` (isi email dimiliki modul mfa)
44. Buka Portal — Product Hub langsung di tab lain
45. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini melebihi sekitar 35 langkah karena memuat empat TC dengan login penuh masing-masing; tiap TC memakai user dan jendela privat sendiri sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec ini berhenti di halaman MFA; penyelesaian faktor-2 dan pencatatan Success di titik final dicakup `TC-AUTH-OTP-E2E-033-handoff-mfa-first-login-dan-final`.
- Urutan TC di dalam spec berbeda dari urutan TC sumber (98, 113, 114, 174): TC profil IDLE dikelompokkan berurutan, lalu profil POLNEW (Agreement dan MFA), lalu NEWDEV (hanya MFA), sehingga urutan di spec menjadi 98, 113, 174, 114, supaya variasi topik sejenis berurutan (prinsip 3, S-10).
- Urutan verifikasi TC-AUTH-OTP-174 Expected a: layar Confirm to Continue diverifikasi lebih dulu (langkah 28), baru mail-catcher dibuka (langkah 29) dan email alert diverifikasi belum ada, supaya verifikasi layar tidak dilakukan saat konteks berada di mail-catcher. Langkah 29 dan langkah 34 (membuka mail-catcher) mengikuti langkah 6 dan 9 di TC sumber; langkah 31 adalah langkah penghubung kembali ke layar Confirm to Continue (S-03).
- Pengecualian P-2 (pemicu bukan objek uji): langkah 6 memutar ulang kode yang sudah terpakai langsung ke server hanya sebagai langkah observasi Expected c dan Post Condition a TC-AUTH-OTP-98 ("kode OTP berstatus terpakai"), bukan sebagai objek uji replay (kelas a).
- Temuan untuk QA:
  - TC-AUTH-OTP-98 langkah 6 mengirim Verify OTP langsung dengan kode terpakai saat user berada di layar Confirm to Continue. Penolakan server pada keadaan itu diasumsikan; di PRD baru terbukti untuk kode terpakai setelah login sukses (TC-AUTH-OTP-155). Mohon QA mengonfirmasi bahwa PRD juga menetapkannya pada keadaan Confirm to Continue.
  - TC-AUTH-OTP-98 (`Manual Only` di TC sumber) membutuhkan profil IDLE dengan waktu logout terakhir 31 hari yang lalu; kebutuhan seed ini dicatat di Prerequisites sebagai kemampuan teknis, bukan alasan mengeluarkan TC dari spec.
  - TC-AUTH-OTP-174 Expected a menyebut "belum ada email alert" sebelum Continue tetapi tidak menyebut cara memastikan bahwa email tidak datang terlambat; spec memeriksa sekali sebelum Continue sesuai TC.
  - TC-AUTH-OTP-174 Post Condition a (persetujuan Privacy Policy tersimpan) dan b (sesi penuh belum dibuat sampai faktor-2 selesai) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi untuk keduanya (S-01). Mohon QA menambah langkah observasinya di TC-174 bila diinginkan.
  - TC-AUTH-OTP-113 dan TC-AUTH-OTP-114 Post Condition (Success belum ditulis) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi untuk keduanya (S-01). Mohon QA menambah langkah observasinya di TC.
