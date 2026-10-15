---
id: TC-AUTH-RST-E2E-040-log-request-resend
title: "Pencatatan Request dan Resend pada Activity Log Session dan User Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-94
  - TC-AUTH-RST-95
  - TC-AUTH-RST-96
  - TC-AUTH-RST-97
coverage:
  web: automated
---

# Pencatatan Request dan Resend pada Activity Log Session dan User Log

## Prerequisites

- Mode: FE+BE (dengan fixture BE untuk counter per email).
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dengan password aktif `Spectra.env.RST_PASSWORD`. Counter per email diatur lewat fixture BE. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: fixture BE untuk counter per email dan cooldown; reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Global Settings > Activity Log > Session dan Global Settings > User > Detail > User Log); pengaturan jam server dan jam browser bersama (cooldown ditegakkan di server, countdown [Resend email] berjalan di jam klien).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: jam server dan jam browser. Suite berjalan serial (`parallel: false`). Pemulihan: kedua jam dipulihkan di hook `after` (tetap berjalan walau spec gagal di tengah).
- TC-AUTH-RST-94, 95, 96, 97: aksi dilakukan oleh guest (browser web); admin pengamat log pada jendela terpisah.
- TC-AUTH-RST-94: User `Budi Santoso` (`budisantoso+{runId}-040a@qwertysystem.net`) Active.
- TC-AUTH-RST-95: User `Tono Kurniawan` (`tonokurniawan+{runId}-040b@qwertysystem.net`) Inactive.
- TC-AUTH-RST-96: User `Fajar Nugroho` (`fajarnugroho+{runId}-040c@qwertysystem.net`) Active dengan 5 percobaan dalam 24 jam dan cooldown sudah lewat.
- TC-AUTH-RST-97: User `Gita Nugroho` (`gitanugroho+{runId}-040d@qwertysystem.net`) Active dengan 4 percobaan dalam 24 jam dan cooldown sudah lewat.

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA)

### TC-AUTH-RST-94: Request sukses tercatat Success / Password reset requested

2. Pindah ke jendela admin, buka Global Settings > Activity Log > Session lalu terapkan Filter Activity = "Reset Password"
3. Buka Global Settings > User > Detail > User Log untuk user "Budi Santoso" lalu catat jumlah baris kedua surface sebagai baseline B1
4. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `budisantoso+{runId}-040a@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
5. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Budi Santoso"
6. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B1
7. Verifikasi entri baru pada kedua surface: Activity `Reset Password`, Status Success, Note `Password reset requested` (dicari berdasarkan Note dan email user, bukan posisi teratas)
8. Verifikasi kedua entri memuat Date, IP Address, dan Device / Browser yang terisi

### TC-AUTH-RST-95: Request akun Inactive tercatat Failed / Account is inactive

9. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password", buka User Log untuk user "Tono Kurniawan", lalu catat jumlah baris kedua surface sebagai baseline B2
10. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `tonokurniawan+{runId}-040b@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
11. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Tono Kurniawan"
12. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B2
13. Verifikasi entri baru pada kedua surface: Activity `Reset Password`, Status Failed, Note `Account is inactive` (dicari berdasarkan Note dan email user, bukan posisi teratas)

### TC-AUTH-RST-96: Request melebihi batas per email tercatat Failed / Too many reset attempts

14. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password", buka User Log untuk user "Fajar Nugroho", lalu catat jumlah baris kedua surface sebagai baseline B3
15. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `fajarnugroho+{runId}-040c@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] (Request ke-6)
16. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Fajar Nugroho"
17. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B3
18. Verifikasi entri baru pada kedua surface: Activity `Reset Password`, Status Failed, Note `Too many reset attempts` (dicari berdasarkan Note dan email user, bukan posisi teratas)

### TC-AUTH-RST-97: Resend melebihi batas per email tercatat Failed / Too many reset attempts

19. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `gitanugroho+{runId}-040d@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] sampai halaman Email Sent! tampil (percobaan ke-5)
20. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password", buka User Log untuk user "Gita Nugroho", lalu catat jumlah baris kedua surface sebagai baseline B4 (sudah memuat entri Success dari percobaan ke-5; diambil sebelum jam dimajukan)
21. Pindah ke jendela guest lalu majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
22. Klik [Resend email] (percobaan ke-6)
23. Pulihkan jam server dan jam browser ke waktu nyata
24. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Gita Nugroho"
25. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B4
26. Verifikasi entri baru pada kedua surface: Activity `Reset Password`, Status Failed, Note `Too many reset attempts` (dicari berdasarkan Note dan email user, bukan posisi teratas)

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. TC-AUTH-RST-96 dan 97 adalah Manual Only karena fixture counter; kebutuhan ditulis di Prerequisites.
- TC sumber menulis dependensi ke TC-AUTH-RST-25, 31, dan 49 untuk aksinya; aksi disalin utuh di sini (S-04). Entri log Request sukses untuk akun Pending Email Confirmation (TC-AUTH-RST-154) memakai jenis aksi sama dengan TC-AUTH-RST-94.
- Entri log Failed `Account is not activated` diasersi di `TC-AUTH-RST-E2E-009-inactive-pending-activation-status` dan `TC-AUTH-RST-E2E-039-defense-confirm-resend-endpoint`.
- Langkah penghubung (S-03): langkah 1 (persiapan jendela), pindah antar jendela guest dan admin, langkah 21 (jam dimajukan menggantikan menunggu 61 detik, konvensi bagian 6), dan langkah 23 (jam dipulihkan sebelum admin membuka log, S-09). Langkah baseline B1 sampai B4 ditambahkan agar entri "baru" terbukti (S-12).
- Spec ini menggeser jam server sehingga entri log yang dibuat saat jam digeser bercap waktu di masa depan dan entri sesudah jam dipulihkan bisa jatuh di bawahnya. Karena itu baseline hanya mencatat jumlah baris dan asersi memakai selisih jumlah baris terhadap baseline serta pencarian entri berdasarkan Note dan email user, bukan posisi teratas (S-12).
