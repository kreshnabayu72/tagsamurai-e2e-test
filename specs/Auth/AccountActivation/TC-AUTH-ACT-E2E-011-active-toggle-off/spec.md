---
id: TC-AUTH-ACT-E2E-011-active-toggle-off
title: "Aktivasi pada User dengan Toggle Active OFF"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-72
  - TC-AUTH-ACT-89
  - TC-AUTH-ACT-109
  - TC-AUTH-ACT-126
coverage:
  web: automated
---

# Aktivasi pada User dengan Toggle Active OFF

## Prerequisites

- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Password user uji dari `Spectra.env.ACT_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-011` beserta link aktivasinya, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-ACT-89: `Siti Handayani` (`sitihandayani+{runId}-011@qwertysystem.net`), Pending Activation, token Active, toggle Active OFF
  - TC-AUTH-ACT-72: `Ayu Prakoso` (`ayuprakoso+{runId}-011@qwertysystem.net`), Pending Activation, token Active, toggle Active OFF
  - TC-AUTH-ACT-126: `Anisa Maharani` (`anisamaharani+{runId}-011@qwertysystem.net`), Pending Activation, token Active, toggle Active ON
  - TC-AUTH-ACT-109: `Wahyu Maharani` (`wahyumaharani+{runId}-011@qwertysystem.net`), sudah Activated dengan token Consumed; disiapkan sendiri oleh spec ini lewat API, link aktivasinya disimpan dari seeding.
- Perubahan toggle Active: `Siti Handayani` dan `Ayu Prakoso` di-seed dengan toggle OFF; `Anisa Maharani` di-deactivate di TC-AUTH-ACT-126; `Wahyu Maharani` di-deactivate lalu di-activate di TC-AUTH-ACT-109. Tidak ada user lain yang diubah.
- Kemampuan teknis: dua konteks browser (jendela privat publik dan browser admin).

## Test Steps

### TC-AUTH-ACT-89: Link milik user dengan toggle Active OFF tidak diperlakukan sebagai token tidak valid

1. Di jendela privat (tanpa sesi), buka link aktivasi user `Siti Handayani` → halaman `Auth > Account Activation > Set Password` tampil
2. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for sitihandayani+{runId}-011@qwertysystem.net."
3. Verifikasi Halaman Invalid Link tidak tampil

### TC-AUTH-ACT-72: User Pending Activation dengan toggle Active OFF tetap bisa membuka Set Password dan mengaktifkan akun

4. Di jendela privat, buka link aktivasi user `Ayu Prakoso`
5. Verifikasi `Auth > Account Activation > Set Password` tampil normal (tidak ada halaman Invalid Link)
6. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
7. Klik button "Set Password"
8. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated"
9. Verifikasi Status Activation user `Ayu Prakoso` Activated dan token Consumed; toggle Active tetap pada nilai sebelum aktivasi

### TC-AUTH-ACT-126: User dinonaktifkan (toggle Active OFF) saat form terbuka: submit tetap berhasil

10. Di jendela privat, buka link aktivasi user `Anisa Maharani` → halaman `Auth > Account Activation > Set Password` tampil
11. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
12. Ganti konteks ke browser admin: login sebagai akun aktor Total Control (Global Settings)
13. Matikan toggle Active user `Anisa Maharani` di `Global Settings > User > Login User` dan klik [Deactivate] pada dialog konfirmasi
14. Ganti konteks kembali ke jendela privat (tab form) dan klik button "Set Password"
15. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated"
16. Verifikasi Tidak ada halaman Invalid Link dan tidak ada toast error
17. Verifikasi Status Activation user `Anisa Maharani` Activated dan token Consumed; toggle Active tetap OFF

### TC-AUTH-ACT-109: Menonaktifkan lalu mengaktifkan kembali user setelah aktivasi tidak mengembalikan status ke Pending Activation

18. Ganti konteks ke browser admin. Pada `Global Settings > User > Login User`, matikan toggle Active user `Wahyu Maharani`, lalu klik [Deactivate] pada dialog konfirmasi
19. Nyalakan kembali toggle Active user `Wahyu Maharani`, lalu klik [Activate] pada dialog konfirmasi
20. Muat ulang `Global Settings > User > Login User` dan cari user `Wahyu Maharani`
21. Verifikasi user `Wahyu Maharani` tidak berbadge Pending Activation (status Activation tetap Activated)
22. Ganti konteks ke jendela privat, buka kembali link aktivasi user `Wahyu Maharani`
23. Verifikasi `Auth > Account Activation > Invalid Link` varian Used tampil (token tetap Consumed)
24. Verifikasi Status Activation user `Wahyu Maharani` tetap Activated

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Urutan: kasus publik (89, 72) dulu, lalu kasus yang butuh browser admin (126, 109), supaya ganti konteks minimal.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
