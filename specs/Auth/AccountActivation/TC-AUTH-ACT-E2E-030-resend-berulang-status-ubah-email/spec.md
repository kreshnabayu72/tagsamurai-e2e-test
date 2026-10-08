---
id: TC-AUTH-ACT-E2E-030-resend-berulang-status-ubah-email
title: "Resend Berulang, Status Setelah Resend, dan Perubahan Email User Pending Activation"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-102
  - TC-AUTH-ACT-103
  - TC-AUTH-ACT-104
coverage:
  web: automated
---

# Resend Berulang, Status Setelah Resend, dan Perubahan Email User Pending Activation

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: mail-catcher uji yang dapat dibaca spec (API inbox per alamat); jendela privat (browser tanpa sesi) untuk membuka link aktivasi.
- Akun aktor: login sbg Role: Total Control (Global Settings); kredensial diambil dari environment variable `GS_TC_PASSWORD` (`Spectra.env.GS_TC_PASSWORD`).
- Hook `before` (lewat API, email bersuffix per run): buat user Pending Activation dengan token Active, Activation Email pertama terkirim ke mail-catcher; cooldown Resend ditunggu eksplisit di langkah sebelum tiap Resend:
  - TC-AUTH-ACT-102: `Bayu Susanto` (`bayususanto+{runId}-030@qwertysystem.net`).
  - TC-AUTH-ACT-103: `Intan Sulistyo` (`intansulistyo+{runId}-030@qwertysystem.net`).
  - TC-AUTH-ACT-104: `Yoga Basuki` (`yogabasuki+{runId}-030@qwertysystem.net`); email baru `yogabasukibaru+{runId}-030@qwertysystem.net` belum dipakai user lain.
- Hook `after`: hapus semua user yang dibuat spec ini.
- Semua TC: login sbg Role: Total Control (Global Settings) di browser admin; link aktivasi dibuka di jendela privat.

## Test Steps

### TC-AUTH-ACT-102: Dua kali Resend berturut-turut hanya menyisakan token terakhir yang valid

1. Di browser admin, login sbg Role: Total Control (Global Settings). Ambil link dari email pertama user `Bayu Susanto` (link A)
2. Tunggu cooldown Resend Activation Email (60 detik) sejak email terakhir dikirim untuk user `Bayu Susanto`
3. Di browser admin, klik Resend Activation Email untuk `Bayu Susanto`, lalu ambil link dari email kedua (link B)
4. Tunggu cooldown Resend Activation Email (60 detik) sejak email terakhir dikirim untuk user `Bayu Susanto`
5. Klik Resend Activation Email lagi, lalu ambil link dari email ketiga (link C)
6. Di jendela privat baru (tanpa sesi admin), buka link A
7. Verifikasi Link A menampilkan `Auth > Account Activation > Invalid Link` varian Expired
8. Di jendela privat yang sama, buka link B
9. Verifikasi Link B menampilkan `Auth > Account Activation > Invalid Link` varian Expired
10. Di jendela privat yang sama, buka link C
11. Verifikasi Link C menampilkan `Auth > Account Activation > Set Password` dengan Subtitle "Set a password to log in for bayususanto+{runId}-030@qwertysystem.net."
12. Verifikasi Hanya token C yang Active; token A dan B Superseded

### TC-AUTH-ACT-103: Resend Activation Email tidak mengubah status user dari Pending Activation

13. Di browser admin, pada `Global Settings > User > Login User`, klik row action Resend Activation Email untuk user `Intan Sulistyo`
14. Muat ulang `Global Settings > User > Login User` dan cari user `Intan Sulistyo`
15. Verifikasi User `Intan Sulistyo` tetap berbadge Pending Activation pada tabel (status tidak berubah akibat Resend)
16. Verifikasi Status user `Intan Sulistyo` tetap Pending Activation

### TC-AUTH-ACT-104: Mengubah email user Pending Activation memicu pengiriman ulang dan membuat link lama invalid

17. Ambil link aktivasi dari email pertama user `Yoga Basuki` (link A)
18. Di browser admin, pada `Global Settings > User > Login User`, buka `Popup Edit User` untuk `Yoga Basuki`, ubah Email menjadi `yogabasukibaru+{runId}-030@qwertysystem.net` lalu klik [Save]
19. Ambil link aktivasi dari email baru yang tiba di `yogabasukibaru+{runId}-030@qwertysystem.net` (link B)
20. Di jendela privat baru (tanpa sesi admin), buka link A
21. Verifikasi `Auth > Account Activation > Invalid Link` varian Expired tampil untuk link A
22. Di jendela privat yang sama, buka link B
23. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for yogabasukibaru+{runId}-030@qwertysystem.net."
24. Verifikasi Token A user `Yoga Basuki` Superseded dan token B Active; status user tetap Pending Activation

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness d (mail-catcher). Dipisah dari E2E-026 supaya kedua spec di bawah batas smell sekitar 35 langkah; tiap TC memakai user sendiri.
- Setiap link aktivasi dibuka di jendela privat tanpa sesi admin; browser admin dipakai untuk Resend dan Edit User.
- caseType Edge mengikuti alur dominan (TC-AUTH-ACT-102 dan TC-AUTH-ACT-104 Edge Case); priority High dari TC-AUTH-ACT-102 (P1).
- Spec ini 25 langkah.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
