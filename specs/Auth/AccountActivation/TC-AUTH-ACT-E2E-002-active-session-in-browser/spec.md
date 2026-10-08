---
id: TC-AUTH-ACT-E2E-002-active-session-in-browser
title: "Link Aktivasi dan Go to Login saat Browser Memiliki Sesi Login Aktif"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-10
  - TC-AUTH-ACT-78
coverage:
  web: automated
---

# Link Aktivasi dan Go to Login saat Browser Memiliki Sesi Login Aktif

## Prerequisites

- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-002@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `ACT_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: satu konteks browser yang sudah memegang sesi login akun aktor (dari hook `before`); link aktivasi dibuka di browser yang sama.
- TC-AUTH-ACT-10: Browser memiliki sesi login aktif milik akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), login di hook `before` dengan kredensial `Spectra.env.GS_TC_PASSWORD`
- TC-AUTH-ACT-10: User `Hendra Santoso` (`hendrasantoso+{runId}-002@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-10 data: Link aktivasi user `Hendra Santoso`
- TC-AUTH-ACT-78: Browser memiliki sesi login aktif milik akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), login di hook `before` dengan kredensial `Spectra.env.GS_TC_PASSWORD`
- TC-AUTH-ACT-78: User `Kirana Kusuma` (`kiranakusuma+{runId}-002@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-78 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`

## Test Steps

### TC-AUTH-ACT-10: Link valid dibuka di browser yang sedang memiliki sesi login aktif

1. Pada browser yang sama, buka link aktivasi user `Hendra Santoso`
2. Verifikasi `Auth > Account Activation > Set Password` tampil normal untuk user `Hendra Santoso` tanpa redirect ke beranda sesi aktif
3. Verifikasi Sesi login aktif milik user lain tidak berubah (tetap login)
4. Verifikasi Token aktivasi tetap Active dan status user tetap Pending Activation
5. Verifikasi Sesi login aktif di browser tidak berubah

### TC-AUTH-ACT-78: Go to Login saat browser memiliki sesi login aktif milik user lain

6. Buka link aktivasi user `Kirana Kusuma` di browser → halaman `Auth > Account Activation > Set Password` tampil
7. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan nilai `Spectra.env.ACT_PASSWORD` di field Confirm Password
8. Klik button "Set Password"
9. Klik CTA "Go to Login"
10. Verifikasi halaman Login with Password selalu tampil
11. Verifikasi Sesi login aktif milik user lain di browser tidak diperiksa dan tidak berubah (tetap login)
12. Verifikasi Status user `Kirana Kusuma` Activated; sesi login aktif di browser tidak berubah

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Akun aktor admin Global Settings login di browser yang sama sebelum link dibuka.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
