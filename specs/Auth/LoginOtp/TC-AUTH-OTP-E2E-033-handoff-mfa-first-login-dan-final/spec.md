---
id: TC-AUTH-OTP-E2E-033-handoff-mfa-first-login-dan-final
title: "Handoff ke MFA Authenticator setelah Agreement dan Pencatatan Success di Titik Final"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-112
  - TC-AUTH-OTP-115
  - TC-AUTH-OTP-129
coverage:
  web: automated
---

# Handoff ke MFA Authenticator setelah Agreement dan Pencatatan Success di Titik Final

## Prerequisites

- Mode: FE+BE (backend nyata; sesi dan log dibuktikan lewat perilaku UI dan log Global Settings).
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Tidak ada password, token, atau secret TOTP di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`; `OTP_PASSWORD` (password user uji yang dipasang saat seeding; tidak dipakai langkah uji); `OTP_TOTP_SECRET_IDLE` (secret TOTP Authenticator `Wulan Harahap`, profil IDLE, TC-AUTH-OTP-115) dan `OTP_TOTP_SECRET_NEWDEV` (secret TOTP Authenticator `Doni Gunawan`, profil NEWDEV, TC-AUTH-OTP-129), dengan pola nama `OTP_TOTP_SECRET_<PROFIL>`. Hook `before` mendaftarkan Authenticator kedua user dengan secret itu; kode TOTP dihitung dari secret saat langkah dijalankan.
- Hook `before` membuka browser admin dan login sebagai akun aktor Total Control (Global Settings); langkah uji hanya berpindah konteks ke browser itu (TC-AUTH-OTP-129). Hook `after` mengembalikan sesi admin ke akun default suite.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-033`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - Profil FIRST (Activated, Active ON; belum pernah menyelesaikan login di platform web; Authenticator belum terdaftar; Agreement dan MFA terpicu):
    - TC-AUTH-OTP-112: `Eko Handayani` (`ekohandayani+{runId}-033@qwertysystem.net`)
  - Profil IDLE (Activated, Active ON; logout web terakhir 31 hari yang lalu; Authenticator sudah terdaftar; Agreement dan MFA terpicu; waktu logout terakhir diatur lewat seed data):
    - TC-AUTH-OTP-115: `Wulan Harahap` (`wulanharahap+{runId}-033@qwertysystem.net`)
  - Profil NEWDEV (seperti BASE, tetapi login dari browser/device yang belum dikenali; Authenticator sudah terdaftar; hanya MFA terpicu):
    - TC-AUTH-OTP-129: `Doni Gunawan` (`donigunawan+{runId}-033@qwertysystem.net`)
- Baseline log: hook `before` mencatat jumlah baris `Doni Gunawan` di `Global Settings > Activity Log > Session` dan di `Global Settings > User > Detail > User Log`; "tidak ada baris Success" dan "tepat satu baris baru" pada langkah 35 sampai 45 dihitung terhadap baseline itu (S-12).
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP; aplikasi authenticator uji (TOTP) yang menghasilkan kode valid untuk `Wulan Harahap` dan `Doni Gunawan`; seed data waktu logout terakhir 31 hari yang lalu; seed device belum dikenali; dua konteks browser (browser admin dan jendela privat publik); reCAPTCHA mode uji.
- Tidak ada state global yang diubah spec ini.

## Test Steps

### TC-AUTH-OTP-112: Login pertama: Agreement lalu langsung faktor-2 Authenticator tanpa pilihan metode

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `ekohandayani+{runId}-033@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ketik 6 digit kode OTP dari email pada kotak digit
6. Centang checkbox "I have read and agree to the Privacy Policy *"
7. Klik button [Continue ➔]
8. Verifikasi browser berpindah ke halaman MFA `Set up authenticator app` (Authenticator belum terdaftar)
9. Verifikasi halaman "Choose verification method" tidak tampil dan tidak ada opsi OTP via email
10. Buka Portal — Product Hub langsung di tab lain
11. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login

### TC-AUTH-OTP-115: Alur lengkap OTP, Confirm to Continue, Authenticator, lalu Product Hub

12. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `wulanharahap+{runId}-033@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Klik button [Request OTP]
16. Ketik 6 digit kode OTP dari email pada kotak digit
17. Verifikasi layar Confirm to Continue tampil setelah Verify OTP
18. Centang checkbox "I have read and agree to the Privacy Policy *"
19. Klik button [Continue ➔]
20. Verifikasi halaman MFA `Enter authenticator code` tampil setelah Confirm to Continue
21. Verifikasi button CTA pada halaman MFA `Enter authenticator code` berlabel "Login"
22. Ketik kode TOTP yang valid dari aplikasi authenticator uji (dihitung dari secret `Spectra.env.OTP_TOTP_SECRET_IDLE`)
23. Klik button [Login]
24. Verifikasi browser dialihkan ke Portal — Product Hub
25. Verifikasi sesi aktif untuk `Wulan Harahap`
26. Verifikasi urutan layar yang dilalui: Verify OTP, Confirm to Continue, Enter authenticator code, Portal — Product Hub
27. Verifikasi tidak ada layar yang meminta OTP email sebagai faktor kedua
28. Logout dari Portal — Product Hub

### TC-AUTH-OTP-129: Login with OTP Success dicatat sekali di titik final setelah MFA tuntas

29. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
30. Ketik `donigunawan+{runId}-033@qwertysystem.net` pada field Email
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Request OTP]
33. Ketik 6 digit kode OTP dari email pada kotak digit; halaman publik berpindah ke halaman MFA `Enter authenticator code`
34. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` untuk `Doni Gunawan`
35. Verifikasi sebelum faktor-2 selesai tidak ada baris Success `Login with OTP` untuk percobaan ini di `Global Settings > Activity Log > Session` dibanding baseline hook `before`
36. Buka `Global Settings > User > Detail > User Log` untuk `Doni Gunawan`
37. Verifikasi sebelum faktor-2 selesai tidak ada baris Success `Login with OTP` untuk percobaan ini di `Global Settings > User > Detail > User Log` dibanding baseline hook `before`
38. Ganti konteks kembali ke jendela publik pada halaman MFA `Enter authenticator code`
39. Ketik kode TOTP yang valid dari aplikasi authenticator uji (dihitung dari secret `Spectra.env.OTP_TOTP_SECRET_NEWDEV`)
40. Klik button [Login] dan selesaikan login
41. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan segarkan halaman
42. Verifikasi tepat satu baris baru dibanding baseline hook `before` di `Global Settings > Activity Log > Session` dengan kolom User `Doni Gunawan`, Activity `Login`, Status `Success`, Note `Login with OTP`
43. Verifikasi kolom IP Address pada baris itu berisi alamat IP browser uji dan kolom Device / Browser berisi browser dan OS uji dalam format "[Browser] on [OS]"
44. Buka `Global Settings > User > Detail > User Log` untuk `Doni Gunawan` dan segarkan halaman
45. Verifikasi tepat satu baris baru dibanding baseline hook `before` di `Global Settings > User > Detail > User Log` dengan Activity `Login`, Status `Success`, Note `Login with OTP`
46. Verifikasi IP Address dan Device / Browser pada baris itu sama dengan baris di Activity Log Session

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini melebihi sekitar 35 langkah karena memuat tiga TC dengan login penuh masing-masing, ditambah faktor-2 TOTP; tiap TC memakai user dan jendela privat sendiri sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Halaman MFA dan isi email dimiliki modul `mfa`; spec ini hanya memverifikasi handoff dari login-otp.
- Pengecualian P-1 (state berat): asersi absence TC-AUTH-OTP-129 Expected a ("Sebelum faktor-2 selesai: tidak ada baris Success `Login with OTP` untuk percobaan ini di `Global Settings > Activity Log > Session` maupun `Global Settings > User > Detail > User Log`") tetap di spec ini (langkah 34 sampai 37) dan tidak dipindah ke spec absence E2E-040, karena bergantung pada state MFA yang baru dibangun: pemeriksaan harus dilakukan saat sesi berhenti di halaman MFA, sebelum TOTP dimasukkan, lalu urutan dilanjutkan ke Expected b dan c di titik final.
- Langkah 28 (logout) dan langkah 41 (ganti konteks ke browser admin) adalah langkah penghubung (S-03, S-07). Langkah 34 dan 36 (ganti konteks dan buka log) serta langkah 38 (kembali ke halaman MFA) adalah penghubung untuk pemeriksaan di tengah alur MFA.
- Langkah 17 dan 20 (memverifikasi layar Confirm to Continue dan halaman MFA `Enter authenticator code` tampil pada titik masing-masing) diturunkan dari Expected c TC-AUTH-OTP-115 (urutan layar yang dilalui: Verify OTP, Confirm to Continue, Enter authenticator code, Portal — Product Hub); langkah 26 mengasersi urutan itu secara keseluruhan.
- Langkah 33: TC sumber (langkah 5 dan 6) menulis halaman MFA tampil sebagai kelanjutan mengetik kode OTP; spec menulisnya sebagai keterangan pada langkah mengetik kode dan tidak menambah `Verifikasi` untuk halaman itu.
- Temuan untuk QA:
  - TC-AUTH-OTP-129 Expected a (sebelum faktor-2 selesai tidak ada baris Success) bergantung pada urutan waktu: TC langkah 6 membuka log di tengah alur MFA; spec ini mengikuti urutan itu (langkah 34 sampai 37) dan memeriksa log lagi sesudah faktor-2 selesai.
  - TC-AUTH-OTP-112 Post Condition a (persetujuan Privacy Policy tersimpan) dan b (Success belum ditulis) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi untuk keduanya.
  - TC-AUTH-OTP-115 Post Condition b (entri Success `Login with OTP` ditulis tepat satu kali di titik final) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi (S-01). Post Condition a (sesi web aktif) tercakup oleh Expected b. Pencatatan Success di titik final dicakup TC-AUTH-OTP-129. Mohon QA menambah langkah observasi log di TC-115 bila diinginkan.
