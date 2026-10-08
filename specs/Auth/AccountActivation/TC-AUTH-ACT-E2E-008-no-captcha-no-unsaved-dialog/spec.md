---
id: TC-AUTH-ACT-E2E-008-no-captcha-no-unsaved-dialog
title: "Halaman Set Password Tanpa CAPTCHA dan Tanpa Dialog Unsaved Changes"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-57
  - TC-AUTH-ACT-58
  - TC-AUTH-ACT-59
coverage:
  web: automated
---

# Halaman Set Password Tanpa CAPTCHA dan Tanpa Dialog Unsaved Changes

## Prerequisites

- Konteks browser: spec berjalan di konteks browser baru tanpa sesi login (jendela privat), sesuai precondition "Tanpa login" semua TC di spec ini.
- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-008@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `ACT_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: reload halaman (F5); navigasi ke halaman lain di tab yang sama.
- TC-AUTH-ACT-57: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-57: User `Bayu Nugroho` (`bayunugroho+{runId}-008@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-57 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-58: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-58: User `Intan Wibowo` (`intanwibowo+{runId}-008@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-58 data: Password dan Confirm Password: `Aman#Sandi8`
- TC-AUTH-ACT-59: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-59: User `Yoga Yulianti` (`yogayulianti+{runId}-008@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-59 data: Password dan Confirm Password: `Aman#Sandi8`

## Test Steps

### TC-AUTH-ACT-58: Reload halaman setelah mengisi field tidak memunculkan dialog Unsaved Changes

1. Buka link aktivasi user `Intan Wibowo` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Ketik `Aman#Sandi8` di field Password dan Confirm Password
3. Reload halaman (F5)
4. Verifikasi Tidak ada dialog Unsaved Changes atau dialog native browser sebelum reload
5. Verifikasi Halaman memuat ulang dan `Auth > Account Activation > Set Password` tampil dengan field Password dan Confirm Password kosong

### TC-AUTH-ACT-59: Meninggalkan halaman setelah mengisi field tidak memunculkan dialog dan token tetap valid

6. Buka link aktivasi user `Yoga Yulianti` di browser → halaman `Auth > Account Activation > Set Password` tampil
7. Ketik `Aman#Sandi8` di field Password dan Confirm Password
8. Navigasi ke halaman lain di tab yang sama
9. Verifikasi Tidak ada dialog konfirmasi (Unsaved Changes) dan navigasi berlangsung langsung
10. Buka kembali link aktivasi yang sama
11. Verifikasi `Auth > Account Activation > Set Password` tampil kembali dengan field kosong (token tetap valid, tidak ada data yang tersimpan)
12. Verifikasi Token aktivasi user `Yoga Yulianti` tetap Active

### TC-AUTH-ACT-57: Halaman Set Password tidak menampilkan CAPTCHA dan submit tidak meminta verifikasi captcha

13. Buka link aktivasi user `Bayu Nugroho` di browser → halaman `Auth > Account Activation > Set Password` tampil
14. Verifikasi Tidak ada widget CAPTCHA pada halaman sebelum klik
15. Ketik nilai `Spectra.env.ACT_PASSWORD` di Password dan Confirm Password, lalu klik button "Set Password" tanpa interaksi tambahan
16. Verifikasi Tidak ada widget CAPTCHA pada halaman sesudah klik
17. Verifikasi Tidak ada pesan captcha belum diselesaikan; submit diproses dan `Auth > Account Activation > Activation Success` tampil
18. Verifikasi Status user `Bayu Nugroho` Activated dan token Consumed

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: TC-AUTH-ACT-58 dan 59 (tidak menyimpan data) dijalankan sebelum TC-AUTH-ACT-57 (aktivasi sukses yang meng-consume token), sesuai prinsip 3.
- Input `Aman#Sandi8` pada TC-AUTH-ACT-58 dan 59 tidak pernah di-submit, sehingga ditulis literal.
