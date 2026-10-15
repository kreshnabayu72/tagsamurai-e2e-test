---
id: TC-AUTH-OTP-E2E-048-status-client-suspended-dan-expired
title: "Login with OTP untuk User dari Client Berstatus Suspended dan Expired"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-151
  - TC-AUTH-OTP-152
coverage:
  web: automated
---

# Login with OTP untuk User dari Client Berstatus Suspended dan Expired

## Prerequisites

- Mode: FE+BE.
- Tanpa login pada langkah uji di jendela privat: Login with OTP berjalan di halaman publik tanpa sesi aktif.
- Akun aktor seeding: Total Control (Admin Console), pre-setup `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.AC_TC_PASSWORD`. Akun ini dipakai hook untuk membuat Client dan user, bukan oleh langkah uji.
- Akun pembaca log (precondition e TC-AUTH-OTP-151 dan 152): Total Control (Global Settings), Tabel Data Uji Pre-setup #1, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`; login di browser admin pada hook `before`. Akun ini harus dapat membaca log user dari Client lain tersebut, dan dipakai langkah uji untuk membuka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Environment variable: `AC_TC_PASSWORD`, `GS_TC_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji; fixture status subscription atau time-travel di environment uji untuk membuat term Client Expired dan memajukannya ke Archive saat cleanup (fixture belum ada). Jam yang diatur (konvensi bagian 6): hanya jam server, dan hanya di hook (`before` memajukan term Client ke Expired, `after` memajukannya ke Archive lalu memulihkan jam server); ini perhitungan status di server yang tidak diamati lewat countdown UI, sehingga jam browser tidak diubah, dan langkah uji tidak menggeser jam. Jam server tidak dipulihkan di `before` setelah term Expired terbentuk: jam tetap maju selama langkah uji dan baru dipulihkan di `after`. Suite berjalan serial (`parallel: false`) karena jam server digeser.
- Hook `before` (seeding API) membuat satu Client per baris tabel dengan suffix per run `+{runId}-048` dan satu user profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada) di Client itu, dengan term subscription Active. Client Suspended dibuat dengan suspend setelah user di-seed; Client Expired dibuat dengan memajukan term ke Expired. Baris teratas `Global Settings > Activity Log > Session` dan jumlah baris `Global Settings > User > Detail > User Log` user dicatat di hook sebagai baseline "baris baru" (S-12). Hook `after` membersihkan Client dan user yang dibuat: Unsuspend Client Suspended lebih dulu, lalu batalkan term Active atau majukan term Expired ke Archive, lalu hapus Client beserta user-nya; tetap jalan walau seeding gagal sebagian.
- Tabel "Dimensi yang diuji" (langkah dilakukan untuk setiap baris tabel):

| TC | Dimensi | User | Email |
|---|---|---|---|
| TC-AUTH-OTP-151 | Client status Suspended | `Ratna Maulana` | `ratnamaulana+{runId}-048@qwertysystem.net` |
| TC-AUTH-OTP-152 | Client status Expired | `Taufik Siregar` | `taufiksiregar+{runId}-048@qwertysystem.net` |

## Test Steps

### Client berstatus Suspended dan Expired (TC-AUTH-OTP-151 dan 152), lakukan untuk setiap baris tabel

1. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik email user baris tabel pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi toast sukses: "Success, the code has been sent."
6. Verifikasi tidak ada caption penolakan karena status Client pada langkah Request OTP
7. Ketik 6 digit kode OTP dari email pada kotak digit
8. Verifikasi Verify OTP berhasil
9. Verifikasi sesi dibuat untuk user baris tabel
10. Ganti konteks ke browser admin Total Control (Global Settings), buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk user baris tabel
11. Verifikasi entri baru Success `Login with OTP` ditulis untuk user baris tabel di `Global Settings > Activity Log > Session` maupun `Global Settings > User > Detail > User Log`
12. Tutup jendela privat

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness h (state tenant: Client Suspended dan Expired), dipisah dari E2E-042 (plan dan entitas) menurut prinsip 13h supaya kegagalan seeding Client Expired tidak menjatuhkan spec plan dan entitas. Langkah identik per baris tabel, hanya status Client yang berbeda; cara skrip menjalankan dua baris diputuskan di tahap script. Spec ini 12 langkah per putaran, dijalankan 2 kali.
- Penanganan Access Restricted (Suspended) dan gate status subscription (Expired) dimiliki session-management dan tidak diasersi di sini, sesuai Expected TC-AUTH-OTP-151 dan 152; keputusan NC-13 menyatakan Request dan Verify OTP tidak dipengaruhi status Client.
- Langkah penghubung (S-03): mengganti konteks ke browser admin dan menutup jendela privat ditulis sebagai aksi tanpa `Verifikasi`.
- Temuan untuk QA: (1) TC-AUTH-OTP-151 dan 152 menyatakan "sesi dibuat" tanpa menyebut layar tujuan (Portal — Product Hub atau layar Access Restricted) maupun cara mengamati sesi; spec tidak mengasersi layar tujuan karena dimiliki session-management, dan mekanisme pengamatan sesi ditentukan di tahap script. (2) Entri Success `Login with OTP` pada TC-AUTH-OTP-151 dan 152 muncul di Post Condition yang punya langkah observasi di TC (langkah 6, kedua surface log), sehingga diasersi di kedua surface.
