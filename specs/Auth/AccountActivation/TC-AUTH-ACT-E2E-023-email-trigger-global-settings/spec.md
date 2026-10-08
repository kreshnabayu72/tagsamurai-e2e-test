---
id: TC-AUTH-ACT-E2E-023-email-trigger-global-settings
title: "Activation Email dari Pembuatan User di Global Settings"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-11
  - TC-AUTH-ACT-13
  - TC-AUTH-ACT-14
  - TC-AUTH-ACT-15
  - TC-AUTH-ACT-16
coverage:
  web: automated
---

# Activation Email dari Pembuatan User di Global Settings

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: mail-catcher uji yang dapat dibaca spec (API inbox per alamat) untuk semua TC di spec ini; jendela privat (browser tanpa sesi) untuk membuka link aktivasi TC-AUTH-ACT-11.
- Akun aktor: login sbg Role: Total Control (Global Settings); kredensial diambil dari environment variable `GS_TC_PASSWORD` (`Spectra.env.GS_TC_PASSWORD`).
- Hook `before` (lewat API, email bersuffix per run): buat user Pending Activation dengan token Active sehingga Activation Email terkirim ke mail-catcher:
  - TC-AUTH-ACT-14: `Dimas Prakoso` (`dimasprakoso+{runId}-023@qwertysystem.net`).
  - TC-AUTH-ACT-15: `Lestari Puspita` (`lestaripuspita+{runId}-023@qwertysystem.net`).
  - TC-AUTH-ACT-16: `Bayu Hidayat` (`bayuhidayat+{runId}-023@qwertysystem.net`).
- Data yang dibuat lewat UI di spec: TC-AUTH-ACT-11 Name `Maya Kurniawan`, Email `mayakurniawan+{runId}-023@qwertysystem.net`; TC-AUTH-ACT-13 Name `Putri Rahmawati`, Email `putrirahmawati+{runId}-023@qwertysystem.net`.
- Hook `after`: hapus semua user yang dibuat spec ini (lewat API) dan kosongkan inbox mail-catcher untuk alamat bersuffix run ini.

## Test Steps

### TC-AUTH-ACT-11: Membuat user di Global Settings > User memicu Activation Email dan link aktivasi valid

1. Login sbg Role: Total Control (Global Settings) dan buka `Global Settings > User > Login User`
2. Klik button "+ User" → `Global Settings > User > Login User > Popup Create User` terbuka; isi Name `Maya Kurniawan`, Email `mayakurniawan+{runId}-023@qwertysystem.net` dan field wajib lain, lalu klik [Submit]
3. Verifikasi User `Maya Kurniawan` muncul pada tabel `Global Settings > User > Login User` dengan badge Pending Activation
4. Buka inbox `mayakurniawan+{runId}-023@qwertysystem.net` di mail-catcher dan baca email aktivasi yang diterima
5. Verifikasi Email dengan Subject "Activate your TAG Samurai account" diterima di inbox `mayakurniawan+{runId}-023@qwertysystem.net`
6. Salin link [Activate Account] dari email lalu buka di jendela privat baru (tanpa sesi Total Control)
7. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for mayakurniawan+{runId}-023@qwertysystem.net."
8. Verifikasi Token aktivasi user `Maya Kurniawan` Active dan status user Pending Activation

### TC-AUTH-ACT-13: Isi Activation Email sesuai template platform

9. Kembali ke `Global Settings > User > Login User`, buat user `Putri Rahmawati` melalui `Popup Create User` dengan Email `putrirahmawati+{runId}-023@qwertysystem.net`, lalu klik [Submit]
10. Buka email aktivasi yang diterima di inbox `putrirahmawati+{runId}-023@qwertysystem.net` dan baca isinya
11. Verifikasi Subject: "Activate your TAG Samurai account"
12. Verifikasi Body menyapa "Hi Putri Rahmawati," dengan nama lengkap user
13. Verifikasi Body memuat kalimat "An account has been created for you on TAG Samurai. Click the button below to set your password and activate your account."
14. Verifikasi Tersedia button [Activate Account]
15. Verifikasi Body memuat kalimat "This link is valid for 24 hours and can only be used once."
16. Verifikasi Body memuat link teks mentah dengan alamat yang sama dengan button [Activate Account] setelah kalimat "If the button doesn't work, click the link below or copy and paste it into your browser:"
17. Verifikasi Body memuat kalimat "To keep your data secure, please don't forward this email to anyone. If you didn't create this account, just ignore this email." dan penutup "— TAG Samurai"

### TC-AUTH-ACT-16: Greeting email memakai nama lengkap saat email dikirim, bukan nama setelah diubah

18. Buka email aktivasi yang diterima user `Bayu Hidayat` di inbox `bayuhidayat+{runId}-023@qwertysystem.net` dan baca greeting
19. Verifikasi Greeting "Hi Bayu Hidayat,"
20. Buka `Global Settings > User > Login User > Popup Edit User` untuk `Bayu Hidayat`, ubah Last Name menjadi `Baru` lalu klik [Save]
21. Verifikasi Nama user `Bayu Hidayat` pada Global Settings > User berubah
22. Buka kembali email aktivasi yang sama di inbox `bayuhidayat+{runId}-023@qwertysystem.net`
23. Verifikasi Greeting email yang sudah terkirim tetap "Hi Bayu Hidayat," (tidak berubah mengikuti nama baru); email yang sudah terkirim tidak berubah

### TC-AUTH-ACT-14: Klik [Activate Account] pada email membuka halaman Set Password

24. Logout dari Global Settings dan pastikan tidak ada sesi aktif di browser (halaman publik)
25. Buka email aktivasi user `Dimas Prakoso` di inbox `dimasprakoso+{runId}-023@qwertysystem.net`
26. Klik button [Activate Account]
27. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for dimasprakoso+{runId}-023@qwertysystem.net."
28. Verifikasi Tidak ada halaman Invalid Link yang tampil

### TC-AUTH-ACT-15: Link teks mentah pada email membuka halaman Set Password

29. Buka email aktivasi user `Lestari Puspita` di inbox `lestaripuspita+{runId}-023@qwertysystem.net`
30. Salin link teks mentah dari body email dan tempel di address bar browser, lalu buka
31. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for lestaripuspita+{runId}-023@qwertysystem.net."

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness d (mail-catcher).
- Urutan: TC yang memakai sesi admin (11, 13, 16) dijalankan dulu, lalu langkah logout sebelum TC publik (14, 15).
- Asersi "Auth tidak menambahkan entri pencatatan" dari TC-AUTH-ACT-11 dicakup di spec absence E2E-029 (bagian TC-AUTH-ACT-96) (kelas g), bukan di spec ini.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
