---
id: TC-AUTH-OTP-E2E-005-akses-langsung-dan-redirect-sesi-aktif
title: "Akses Langsung ke Layar Login with OTP tanpa Sesi dan Pengalihan bagi Pengguna yang Sudah Login"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-73
  - TC-AUTH-OTP-74
  - TC-AUTH-OTP-06
  - TC-AUTH-OTP-75
  - TC-AUTH-OTP-76
coverage:
  web: automated
---

# Akses Langsung ke Layar Login with OTP tanpa Sesi dan Pengalihan bagi Pengguna yang Sudah Login

## Prerequisites

- Mode: FE+BE (web). Spec dimulai tanpa sesi login (TC-AUTH-OTP-73 dan 74 membutuhkan konteks bersih), lalu berganti ke sesi akun aktor pada TC-AUTH-OTP-06, 75, dan 76.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Sesi aktor dibuat lewat `seedSession` (API) pada langkah ganti akun yang eksplisit; tidak ada login lewat UI.
- Kemampuan teknis: konteks browser tanpa sesi (jendela privat) dan injeksi sesi akun aktor (`seedSession`) ke konteks jendela privat yang sama; seluruh langkah spec berjalan di satu jendela privat itu.
- Environment variable: `GS_TC_PASSWORD` (akun aktor). Tidak ada password atau token di spec atau fixture.
- Tidak ada data yang dibuat spec ini (semua layar dibuka lewat alamat langsung).
- State yang diubah: sesi web akun aktor. Hook `after` mengakhiri sesi aktor yang dibuat spec ini dan menutup jendela privat (tetap jalan walau spec gagal di tengah).

## Test Steps

### TC-AUTH-OTP-73: Membuka alamat layar Verify OTP langsung tanpa melalui Request OTP

1. Buka jendela privat baru (tanpa sesi login)
2. Buka alamat layar `Auth > Login with OTP > Verify OTP` langsung di tab baru pada jendela privat yang sama tanpa alur Request OTP
3. Verifikasi layar Verify OTP tidak tampil
4. Verifikasi browser dialihkan ke halaman `Auth > Login with OTP > Request OTP`
5. Verifikasi field Email kosong

### TC-AUTH-OTP-74: Membuka alamat layar Confirm to Continue langsung tanpa token pra-autentikasi

6. Buka alamat layar `Auth > Login with OTP > Confirm to Continue` langsung di tab baru pada jendela privat yang sama tanpa alur verifikasi OTP
7. Verifikasi layar Confirm to Continue tidak tampil
8. Verifikasi browser dialihkan ke halaman `Auth > Login with Password`
9. Verifikasi Title "Login with Password"

### Ganti akun: sesi akun aktor Total Control (Global Settings)

10. Buat sesi web aktif untuk akun aktor Total Control (Global Settings) di jendela privat yang sama lewat `seedSession` (sesi disuntikkan ke konteks jendela privat tersebut)

### TC-AUTH-OTP-06: Pengguna yang sudah login membuka halaman Request OTP dialihkan ke Portal — Product Hub

11. Buka halaman `Auth > Login with OTP > Request OTP` melalui alamat langsung di jendela privat yang sama
12. Verifikasi halaman Request OTP tidak ditampilkan
13. Verifikasi browser dialihkan ke halaman Portal — Product Hub

### TC-AUTH-OTP-75: Pengguna yang sudah login membuka alamat layar Verify OTP dialihkan ke Portal — Product Hub

14. Buka alamat layar `Auth > Login with OTP > Verify OTP` langsung di jendela privat yang sama
15. Verifikasi layar Verify OTP tidak tampil
16. Verifikasi browser dialihkan ke halaman Portal — Product Hub

### TC-AUTH-OTP-76: Pengguna yang sudah login membuka alamat layar Confirm to Continue dialihkan ke Portal — Product Hub

17. Buka alamat layar `Auth > Login with OTP > Confirm to Continue` langsung di jendela privat yang sama
18. Verifikasi layar Confirm to Continue tidak tampil
19. Verifikasi browser dialihkan ke halaman Portal — Product Hub

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Urutan TC di spec: 73, 74 (tanpa sesi), lalu 06, 75, 76 (dengan sesi). Urutan ini berbeda dari nomor TC sumber supaya ganti akun hanya terjadi sekali (bagian 3, aturan "beda akun, role, atau entity dipisah kecuali (b) ada Step ganti akun eksplisit").
- S-07: login aktor pertama biasanya di hook, tetapi TC-AUTH-OTP-73 dan 74 mensyaratkan tanpa sesi, sehingga sesi aktor dibuat pada langkah 10 yang eksplisit dan disuntikkan ke jendela privat yang sama; hook `after` mengakhirinya. Bagian setelah langkah 10 tetap bermakna walau bagian sebelumnya gagal.
- Langkah 1 membuka konteks bersih (jendela privat) karena precondition TC-AUTH-OTP-73 "Tanpa login"; ini langkah penghubung tanpa asersi (S-03).
- Temuan untuk QA:
  - TC-AUTH-OTP-73 dan 74 memakai "tab baru" tanpa menyebut bahwa konteks harus tanpa sesi; spec memakai jendela privat baru agar sesuai precondition, dan tetap memakai jendela itu setelah sesi aktor disuntikkan pada langkah 10.
  - TC-AUTH-OTP-06, 75, dan 76 memakai "Login sbg Role: Total Control" tanpa menyebut aplikasi tempat login; spec memakai akun Total Control Global Settings dari Pre-setup #1.
