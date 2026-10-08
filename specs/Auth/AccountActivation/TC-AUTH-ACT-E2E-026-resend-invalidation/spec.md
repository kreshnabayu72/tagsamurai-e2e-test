---
id: TC-AUTH-ACT-E2E-026-resend-invalidation
title: "Resend Activation Email Menggantikan Link Lama: Single dan Bulk Resend"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-85
  - TC-AUTH-ACT-99
  - TC-AUTH-ACT-101
coverage:
  web: automated
---

# Resend Activation Email Menggantikan Link Lama: Single dan Bulk Resend

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: mail-catcher uji yang dapat dibaca spec (API inbox per alamat); jendela privat (browser tanpa sesi) untuk membuka link aktivasi.
- Akun aktor: login sbg Role: Total Control (Global Settings); kredensial diambil dari environment variable `GS_TC_PASSWORD` (`Spectra.env.GS_TC_PASSWORD`).
- Hook `before` (lewat API, email bersuffix per run): buat user Pending Activation dengan token Active, Activation Email pertama terkirim ke mail-catcher; cooldown Resend ditunggu eksplisit di langkah sebelum tiap Resend:
  - TC-AUTH-ACT-85: `Anisa Susanto` (`anisasusanto+{runId}-026@qwertysystem.net`); lalu tunggu cooldown Resend (60 detik) dan lakukan Resend lewat API sehingga token A Superseded dan token B Active (kurang dari 24 jam sejak token A diterbitkan).
  - TC-AUTH-ACT-99: `Fajar Mulyadi` (`fajarmulyadi+{runId}-026@qwertysystem.net`).
  - TC-AUTH-ACT-101: `Dimas Kusuma` (`dimaskusuma+{runId}-026@qwertysystem.net`) dan `Lestari Anggraini` (`lestarianggraini+{runId}-026@qwertysystem.net`).
- Hook `after`: hapus semua user yang dibuat spec ini.
- TC-AUTH-ACT-85: tanpa login (halaman publik). TC-AUTH-ACT-99 dan TC-AUTH-ACT-101: login sbg Role: Total Control (Global Settings).

## Test Steps

### TC-AUTH-ACT-85: Link lama setelah Resend menampilkan halaman Invalid Link varian Expired walau belum 24 jam

1. Di jendela privat baru (tanpa sesi admin), buka link lama (token A) user `Anisa Susanto` yang sudah di-supersede oleh Resend, kurang dari 24 jam sejak diterbitkan
2. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil: Title "Activation Link Expired", Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
3. Verifikasi Tidak ada button CTA (tidak ada "Go to Login") pada halaman dan form Set Password tidak ditampilkan
4. Verifikasi Tampilan identik dengan link yang expired (tidak dibedakan antara superseded dan expired)

### TC-AUTH-ACT-99: Resend Activation Email dari Global Settings > User membuat link lama invalid dan link baru valid

5. Di browser admin, login sbg Role: Total Control (Global Settings). Ambil link aktivasi dari email pertama user `Fajar Mulyadi` (link A)
6. Tunggu cooldown Resend Activation Email (60 detik) sejak email terakhir dikirim untuk user `Fajar Mulyadi`
7. Pada `Global Settings > User > Login User`, klik row action Resend Activation Email untuk user `Fajar Mulyadi`
8. Verifikasi Toast sukses: "Success, activation email has been sent."
9. Ambil link aktivasi dari email baru (link B)
10. Di jendela privat baru (tanpa sesi admin), buka link A
11. Verifikasi `Auth > Account Activation > Invalid Link` varian Expired tampil (Title "Activation Link Expired") untuk link A walau belum 24 jam
12. Di jendela privat yang sama, buka link B
13. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for fajarmulyadi+{runId}-026@qwertysystem.net." untuk link B
14. Verifikasi Token A user `Fajar Mulyadi` Superseded dan token B Active; status user tetap Pending Activation

### TC-AUTH-ACT-101: Bulk Resend Activation Email dari Global Settings > User membuat link lama kedua user invalid

15. Ambil link aktivasi dari email pertama user `Dimas Kusuma` (link A1) dan user `Lestari Anggraini` (link A2)
16. Tunggu cooldown Resend Activation Email (60 detik) sejak email terakhir dikirim untuk user `Dimas Kusuma` dan `Lestari Anggraini`
17. Di browser admin, pada `Global Settings > User > Login User`, centang user `Dimas Kusuma` dan `Lestari Anggraini`, buka Bulk Action, pilih Resend Activation Email
18. Ambil link baru untuk masing-masing user (B1 dan B2)
19. Di jendela privat baru (tanpa sesi admin), buka A1
20. Verifikasi A1 menampilkan `Auth > Account Activation > Invalid Link` varian Expired
21. Di jendela privat yang sama, buka A2
22. Verifikasi A2 menampilkan `Auth > Account Activation > Invalid Link` varian Expired
23. Di jendela privat yang sama, buka B1
24. Verifikasi B1 menampilkan `Auth > Account Activation > Set Password` dengan Subtitle "Set a password to log in for dimaskusuma+{runId}-026@qwertysystem.net."
25. Di jendela privat yang sama, buka B2
26. Verifikasi B2 menampilkan `Auth > Account Activation > Set Password` dengan Subtitle "Set a password to log in for lestarianggraini+{runId}-026@qwertysystem.net."
27. Verifikasi Token lama kedua user Superseded dan token baru Active

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness d (mail-catcher). TC-AUTH-ACT-123 (multi-konteks) dipindah ke E2E-021.
- TC-AUTH-ACT-102, 103, dan 104 (Resend berulang, status setelah Resend, perubahan email) dipisah ke E2E-030 supaya spec tidak melewati batas smell; tiap TC memakai user sendiri, jadi tidak ada data bersama.
- TC-AUTH-ACT-105 tetap di E2E-027: TC itu butuh time-travel (Resend pada T0 + 23 jam), dan link-nya diambil lewat API seeding di sana, sehingga 026 tetap satu harness (mail-catcher) dan 027 tetap satu harness (time-travel).
- Setiap link aktivasi dibuka di jendela privat tanpa sesi admin; browser admin dipakai untuk Resend.
- Spec ini 27 langkah.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
