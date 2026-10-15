---
id: TC-AUTH-MFA-E2E-049-rate-limit-ip-429
title: "Rate Limit IP (429) pada Verify Faktor-2 dan Kirim OTP"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-204
  - TC-AUTH-MFA-205
coverage:
  web: automated
---

# Rate Limit IP (429) pada Verify Faktor-2 dan Kirim OTP

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah counter IP rate limit (flood 20 request per endpoint pada IP uji); hook `after` memulihkan (mereset) counter IP rate limit.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password user `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-204: `Bayu Wijaya` (`bayuwijaya+{runId}-049@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, device browser uji B belum ada di daftar trusted device, Authenticator sudah terdaftar dengan secret yang dikenali aplikasi authenticator uji).
  - TC-AUTH-MFA-205: `Wulan Wijaya` (`wulanwijaya+{runId}-049@qwertysystem.net`), profil NEWDEV (Tabel Data Uji Pre-setup #4: seperti NEWDEVE, Authenticator belum terdaftar).
- Hook `after`: reset counter IP rate limit untuk endpoint `POST /v2/iam/auth/mfa/authenticator/verify` dan `POST /v2/iam/auth/mfa/otp/send` pada IP uji, lalu hapus kedua user. Hook ini tetap jalan walau spec gagal di tengah dan pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk kedua TC. Tiap TC dimulai di jendela privat baru (browser uji B, ID device belum dikenali). Pengecekan log memakai jendela sesi akun aktor Total Control (Global Settings) yang dibuka di hook `before` (kredensial `Spectra.env.GS_TC_PASSWORD`); jendela itu hanya membaca log dan tidak memicu request ke endpoint MFA yang di-flood.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - IP uji tunggal yang dipakai browser dan client HTTP bersama-sama, sehingga request flood dan request dari halaman dihitung pada counter IP yang sama.
  - Client HTTP untuk mengirim 20 request cepat ke `POST /v2/iam/auth/mfa/authenticator/verify` (field `preAuthToken`, `totpCode`, TC-AUTH-MFA-204) dan `POST /v2/iam/auth/mfa/otp/send` (field `preAuthToken`, TC-AUTH-MFA-205); nama endpoint dan field dari `auth/mfa/API/openapi.yaml`. Batas IP rate limit: 20 request per menit per IP dengan jendela tetap 1 menit, counter terpisah per endpoint, setiap request dihitung termasuk yang ditolak (`auth/_foundation/auth-foundation.md` §3.2).
  - Kemampuan me-reset counter IP rate limit di lingkungan uji (dipakai di hook `after`).
  - Mail-catcher lingkungan uji untuk menghitung email OTP (TC-AUTH-MFA-205; baseline jumlah email sebelum aksi).
  - Penanda waktu (baseline) Activity Log Session dan User Log yang dicatat sebelum flood, supaya asersi "tidak ada entri log baru" hanya membaca baris sesudah penanda dan dicari lewat email bersuffix (TC-AUTH-MFA-204, 205).
  - Seeding state BE per user: profil NEWDEVE tanpa ID device browser uji B di daftar trusted device dengan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji (`Bayu Wijaya`) dan profil NEWDEV tanpa ID device browser uji B di daftar trusted device (`Wulan Wijaya`); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk kode TOTP valid (TC-AUTH-MFA-204).
  - reCAPTCHA mode uji di environment.
- Pemulihan state global: counter IP rate limit di-reset di hook `after`. Spec tidak mengubah jam server, geo-IP, atau email service.

## Test Steps

### TC-AUTH-MFA-204: Verify faktor-2 melampaui IP rate limit ditolak dengan caption Too many requests

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `bayuwijaya+{runId}-049@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
8. Catat penanda waktu (baseline) Activity Log Session dan User Log sebelum flood
9. Kirim 20 request `POST /v2/iam/auth/mfa/authenticator/verify` (client HTTP) dari IP uji yang sama dalam 1 menit dengan `preAuthToken` berupa nilai acak tidak dikenal dan `totpCode` `000000`
10. Dalam jendela 1 menit yang sama, ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `bayuwijaya+{runId}-049@qwertysystem.net` pada kotak digit, lalu klik button [Login] (request ke-21)
11. Verifikasi Caption error di bawah kotak digit: "Too many requests. Please try again later."
12. Verifikasi Kotak digit tetap terisi (digit dipertahankan)
13. Verifikasi Tidak ada sesi yang dibuat (Portal — Product Hub tidak tampil)
14. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Bayu Wijaya` (email bersuffix `bayuwijaya+{runId}-049@qwertysystem.net`)
15. Verifikasi Tidak ada entri log baru untuk penolakan karena rate limit pada Activity Log Session sesudah penanda waktu
16. Buka `Global Settings > User > Detail > User Log` untuk `Bayu Wijaya` dan cari entri sesudah penanda waktu
17. Verifikasi Tidak ada entri log baru untuk penolakan karena rate limit pada User Log sesudah penanda waktu

### TC-AUTH-MFA-205: Kirim OTP faktor-2 melampaui IP rate limit ditolak tanpa email dan dengan caption Too many requests

18. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
19. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
20. Ketik `wulanwijaya+{runId}-049@qwertysystem.net` pada field Email
21. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
22. Centang widget reCAPTCHA "I'm not a robot"
23. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
24. Catat jumlah email OTP di mail-catcher `wulanwijaya+{runId}-049@qwertysystem.net` sebagai baseline
25. Catat penanda waktu (baseline) Activity Log Session dan User Log sebelum flood
26. Kirim 20 request pengiriman OTP `POST /v2/iam/auth/mfa/otp/send` (client HTTP) dari IP uji yang sama dalam 1 menit dengan `preAuthToken` berupa nilai acak tidak dikenal (semua dihitung)
27. Dalam jendela 1 menit yang sama, pilih opsi "OTP via email" pada halaman Choose Verification Method, lalu klik button [Login] (request ke-21)
28. Verifikasi Caption error pada halaman Choose Verification Method: "Too many requests. Please try again later."
29. Periksa mail-catcher lingkungan uji untuk `wulanwijaya+{runId}-049@qwertysystem.net`
30. Verifikasi Tidak ada email OTP baru di mail-catcher `wulanwijaya+{runId}-049@qwertysystem.net` (jumlah email OTP sama dengan baseline)
31. Verifikasi Halaman tidak berpindah (tetap Choose Verification Method)
32. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Wulan Wijaya` (email bersuffix `wulanwijaya+{runId}-049@qwertysystem.net`)
33. Verifikasi Tidak ada entri log baru untuk penolakan karena rate limit pada Activity Log Session sesudah penanda waktu
34. Buka `Global Settings > User > Detail > User Log` untuk `Wulan Wijaya` dan cari entri sesudah penanda waktu
35. Verifikasi Tidak ada entri log baru untuk penolakan karena rate limit pada User Log sesudah penanda waktu

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- `P-1`: asersi "tidak ada entri log" untuk penolakan karena rate limit (TC-AUTH-MFA-204 Expected c, TC-AUTH-MFA-205 Expected c) tetap di spec ini sebagai `Verifikasi` dengan baseline penanda waktu sebelum flood (S-12, S-05), karena konteksnya adalah counter IP rate limit yang baru dipenuhi flood pada TC yang sama (state berat). TC-AUTH-MFA-204 dan TC-AUTH-MFA-205 tidak masuk `sourceTc` spec absence `TC-AUTH-MFA-E2E-035-absence-pencatatan-log`.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal TC kedua, mencatat baseline jumlah email OTP dan penanda waktu log, pindah ke jendela sesi akun aktor dan membuka Activity Log serta User Log) bukan asersi tambahan (S-03).
- Temuan untuk QA: (1) TC-AUTH-MFA-204 dan TC-AUTH-MFA-205 tidak menyebut isi 20 request flood; spec memakai `preAuthToken` acak tidak dikenal (tetap dihitung oleh rate limit karena dicek sebelum lookup user) agar sesi pre-auth user uji dan batas 5 percobaan salah tidak terpakai sebelum request ke-21. (2) TC-AUTH-MFA-204 Precondition mencantumkan akun Total Control, tetapi Langkah Uji tidak membuka log dan tidak menyebut penanda waktu; TC-AUTH-MFA-205 tidak mencantumkan akun Total Control sama sekali. Spec memakai akun aktor hook untuk membaca Activity Log Session dan User Log dengan baseline penanda waktu sebelum flood, supaya Expected c kedua TC dapat diasersi. (3) TC-AUTH-MFA-204 Langkah 8 menyebut klik [Login] "dengan kode TOTP valid" tanpa langkah mengetik kode; spec menambah langkah mengetik 6 digit kode TOTP. (4) Kedua TC bergantung pada jendela tetap 1 menit sejak request pertama: langkah flood dan request ke-21 harus berjalan berurutan tanpa jeda. (5) TC-AUTH-MFA-204 Post Condition "Tidak ada entri log baru untuk penolakan" dan TC-AUTH-MFA-205 Post Condition "Tidak ada kode OTP baru" sama dengan Expected c dan Expected b, sehingga tidak ada asersi tambahan dari Post Condition. (6) Mekanisme seeding state BE per user (profil NEWDEV/NEWDEVE: trusted device, Authenticator dengan secret dikenal) belum ada di Pre-setup TC (#20/#21).
