---
id: TC-AUTH-LP-E2E-023-mfa-handoff-device-and-idle
title: "Handoff ke MFA karena Device Baru dan Idle Lebih dari 30 Hari"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-71
  - TC-AUTH-LP-72
  - TC-AUTH-LP-154
coverage:
  web: automated
---

# Handoff ke MFA karena Device Baru dan Idle Lebih dari 30 Hari

## Prerequisites

- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: akses ke kotak masuk email user subjek (mail-catcher atau mailbox uji) dari penguji; fixture BE untuk riwayat login web (pernah login di device lain, logout kurang dari 30 hari lalu), browser belum dikenal sebagai device terpercaya, dan logout terakhir di web lebih dari 30 hari lalu (TC-AUTH-LP-154); fixture BE agar versi Privacy Policy yang disetujui sama dengan versi aktif; jendela privat baru; reCAPTCHA mode uji di environment.
- Mode: FE+BE.
- TC-AUTH-LP-71: User `Wati Handayani` (`watihandayani+{runId}-023@qwertysystem.net`) berstatus Activated dan Active; sudah pernah login di device lain dan logout kurang dari 30 hari lalu; versi Privacy Policy terakhir yang disetujui sama dengan versi aktif; browser yang dipakai belum dikenal sebagai device terpercaya
- TC-AUTH-LP-71: User belum login (guest); browser web
- TC-AUTH-LP-71 data: Email `watihandayani+{runId}-023@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-72: User `Wati Handayani` sama seperti TC-AUTH-LP-71; kotak masuk email akun dapat dibuka penguji; browser belum dikenal sebagai device terpercaya (jendela privat baru)
- TC-AUTH-LP-72: User belum login (guest); browser web
- TC-AUTH-LP-72 data: Email `watihandayani+{runId}-023@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-154: User `Rina Septiani` (`rinaseptiani+{runId}-023@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; lokasi sama seperti login sebelumnya; logout terakhir di web lebih dari 30 hari lalu (fixture BE); versi Privacy Policy terakhir yang disetujui sama dengan versi aktif; kotak masuk email akun dapat dibuka penguji
- TC-AUTH-LP-154: User belum login (guest); browser web
- TC-AUTH-LP-154 data: Email `rinaseptiani+{runId}-023@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-71: Login dari device yang belum dikenal mengalihkan ke halaman MFA

1. Buka halaman Login with Password
2. Ketik email `watihandayani+{runId}-023@qwertysystem.net` di field Email
3. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi browser menuju halaman MFA
7. Verifikasi layar Confirm to Continue tidak tampil
8. Verifikasi browser tidak menuju Portal — Product Hub
9. Verifikasi sesi penuh belum dibuat

### TC-AUTH-LP-72: Email alert login tak biasa terkirim saat MFA dipicu oleh device baru

10. Catat jumlah email alert login tak biasa di kotak masuk `watihandayani+{runId}-023@qwertysystem.net` sebagai pembanding
11. Buka jendela privat baru (tanpa sesi login)
12. Buka halaman Login with Password
13. Ketik email `watihandayani+{runId}-023@qwertysystem.net` di field Email
14. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
15. Selesaikan reCAPTCHA
16. Klik [Log in]
17. Verifikasi browser menuju halaman MFA
18. Buka kotak masuk email `watihandayani+{runId}-023@qwertysystem.net`
19. Verifikasi email alert login tak biasa baru diterima di kotak masuk dibanding langkah 10
20. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-154: Login setelah idle 30 hari atau lebih menampilkan layar Confirm to Continue lalu halaman MFA setelah Continue

21. Catat jumlah email alert login tak biasa di kotak masuk `rinaseptiani+{runId}-023@qwertysystem.net` sebagai pembanding
22. Buka jendela privat baru (tanpa sesi login)
23. Buka halaman Login with Password
24. Ketik email `rinaseptiani+{runId}-023@qwertysystem.net` di field Email
25. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
26. Selesaikan reCAPTCHA
27. Klik [Log in]
28. Verifikasi layar Confirm to Continue tampil (kondisi Agreement logout terakhir ≥30 hari terpenuhi)
29. Verifikasi halaman MFA tidak tampil
30. Verifikasi Portal — Product Hub tidak tampil
31. Verifikasi sesi penuh belum dibuat
32. Centang checkbox persetujuan
33. Klik [Continue ➔]
34. Verifikasi browser menuju halaman MFA
35. Verifikasi browser tidak menuju Portal — Product Hub
36. Verifikasi sesi penuh belum dibuat
37. Buka kotak masuk email `rinaseptiani+{runId}-023@qwertysystem.net`
38. Verifikasi tidak ada email alert login tak biasa baru dibanding langkah 21

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah 10 dan 21 (pencatatan jumlah email pembanding) serta langkah 11 dan 22 (jendela privat baru) adalah langkah penghubung tanpa awalan `Verifikasi` (S-03); pembanding dibutuhkan karena Expected "email diterima" dan "tidak ada email" hanya dapat dibuktikan relatif terhadap kondisi sebelum aksi.
- TC-AUTH-LP-72 mengulang login TC-AUTH-LP-71 (Dependensi: TC-AUTH-LP-71); langkah disalin utuh (S-04). Login kedua ini juga memicu MFA tertunda yang tidak pernah dituntaskan; user di-seed per spec sehingga tidak berpengaruh ke spec lain.
- TC-AUTH-LP-124 (pencatatan Success belum ditulis saat MFA tertunda) diuji di spec absence `TC-AUTH-LP-E2E-043-absence-state-based`.
- Langkah 20 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA: TC-AUTH-LP-72 tidak menyebut isi email alert (dimiliki modul MFA) sehingga hanya penerimaan email yang diasersi. TC-AUTH-LP-154 menyebut "tidak ada email alert login tak biasa (idle bukan login tak biasa)" tetapi tidak menyebut apakah email dicek sebelum atau sesudah Continue; spec mengecek sesudah Continue seperti urutan langkah TC.
