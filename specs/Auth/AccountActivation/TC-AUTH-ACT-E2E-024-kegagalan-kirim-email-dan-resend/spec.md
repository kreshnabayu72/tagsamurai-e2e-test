---
id: TC-AUTH-ACT-E2E-024-kegagalan-kirim-email-dan-resend
title: "Kegagalan Pengiriman Activation Email dan Pemulihan lewat Resend"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-17
  - TC-AUTH-ACT-18
coverage:
  web: automated
---

# Kegagalan Pengiriman Activation Email dan Pemulihan lewat Resend

## Prerequisites

- Mode: FE+BE (kegagalan di sisi penyedia email tidak bisa di-intercept di browser, sesuai bagian 6 konvensi).
- Kemampuan teknis: mail-catcher uji yang dapat dibaca spec (API inbox per alamat) dan akses konfigurasi mail-catcher untuk memblokir koneksi email provider uji.
- Akun aktor: login sbg Role: Total Control (Global Settings); kredensial diambil dari environment variable `GS_TC_PASSWORD` (`Spectra.env.GS_TC_PASSWORD`).
- Data yang dibuat lewat UI di spec: Name `Intan Ramadhan`, Email `intanramadhan+{runId}-024@qwertysystem.net`. TC-AUTH-ACT-18 memakai user yang dibuat di TC-AUTH-ACT-17 dalam spec ini.
- Hook `after`: pulihkan koneksi email provider uji ke kondisi normal dan hapus user `Intan Ramadhan`. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-ACT-17: Pengiriman Activation Email gagal tidak membatalkan pembuatan user dan tidak ada retry otomatis

1. Aktifkan simulasi kegagalan pengiriman email dengan memblokir koneksi ke email provider uji
2. Login sbg Role: Total Control (Global Settings), buat user `Intan Ramadhan` melalui `Global Settings > User > Login User > Popup Create User` dengan Email `intanramadhan+{runId}-024@qwertysystem.net`
3. Verifikasi User `Intan Ramadhan` tetap muncul pada tabel `Global Settings > User > Login User` dengan badge Pending Activation (pembuatan user tidak dibatalkan)
4. Tunggu 15 menit dan periksa inbox `intanramadhan+{runId}-024@qwertysystem.net` di mail-catcher serta notifikasi admin
5. Verifikasi Tidak ada Activation Email yang tiba selama 15 menit (tidak ada retry otomatis)
6. Verifikasi Tidak ada notifikasi dari Auth kepada admin tentang kegagalan pengiriman
7. Verifikasi Status user `Intan Ramadhan` Pending Activation dan token aktivasi tetap Active

### TC-AUTH-ACT-18: Resend Activation Email memulihkan aktivasi setelah pengiriman awal gagal

8. Pulihkan email provider uji ke kondisi normal
9. Buka `Global Settings > User > Login User` dan klik row action Resend Activation Email untuk user `Intan Ramadhan`
10. Verifikasi Toast sukses: "Success, activation email has been sent."
11. Buka inbox `intanramadhan+{runId}-024@qwertysystem.net` di mail-catcher dan baca email aktivasi terbaru
12. Verifikasi Email aktivasi baru diterima
13. Buka jendela privat baru (tanpa sesi admin), lalu buka link [Activate Account] dari email tersebut di jendela itu
14. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for intanramadhan+{runId}-024@qwertysystem.net."

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness d (mail-catcher dengan failure injection pada email provider uji). Fault injection di sini dijalankan lewat konfigurasi mail-catcher, bukan intercept browser.
- Dari dua alternatif pemicu di TC sumber (blokir koneksi atau alamat bounce), spec memakai blokir koneksi supaya pemicunya pasti.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
