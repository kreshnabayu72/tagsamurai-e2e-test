---
id: TC-AUTH-RST-E2E-009-inactive-pending-activation-status
title: "Request untuk Akun Inactive, Pending Activation, dan Perubahan Status oleh Admin"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-25
  - TC-AUTH-RST-151
  - TC-AUTH-RST-153
  - TC-AUTH-RST-115
coverage:
  web: automated
---

# Request untuk Akun Inactive, Pending Activation, dan Perubahan Status oleh Admin

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dengan password aktif `Spectra.env.RST_PASSWORD` hanya untuk user berstatus Activated (`Tono Kurniawan` dan `Budi Santoso`; `Dian Pratama` dan `Eka Pratama` berstatus Pending Activation dan belum punya password), tanpa percobaan reset dalam 24 jam. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya); reCAPTCHA mode uji; jendela privat guest dan jendela privat admin terpisah; akun aktor admin dapat membuka Global Settings > Activity Log > Session dan Global Settings > User (ubah status lewat toggle Active beserta dialog Deactivate User dan Activate); pengaturan jam server dan jam browser bersama (cooldown 60 detik dilewati dengan memajukan jam).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: jam server dan jam browser. Suite berjalan serial (`parallel: false`). Pemulihan: jam server dan jam browser dipulihkan pada langkah terakhir spec dan di hook `after` (cadangan bila spec gagal di tengah). Jam dimajukan hanya setelah semua pembacaan Activity Log Session selesai.
- TC-AUTH-RST-25, TC-AUTH-RST-151, TC-AUTH-RST-153, TC-AUTH-RST-115: User belum login (guest) pada jendela guest; browser web.
- TC-AUTH-RST-25: User `Tono Kurniawan` (`tonokurniawan+{runId}-009a@qwertysystem.net`) berstatus Inactive (dinonaktifkan admin).
- TC-AUTH-RST-151: User `Dian Pratama` (`dianpratama+{runId}-009b@qwertysystem.net`) berstatus Pending Activation (belum menetapkan password), toggle Active ON.
- TC-AUTH-RST-153: User `Eka Pratama` (`ekapratama+{runId}-009c@qwertysystem.net`) berstatus Pending Activation dan toggle Active OFF (di-set lewat API di hook `before`).
- TC-AUTH-RST-115: User `Budi Santoso` (`budisantoso+{runId}-009d@qwertysystem.net`) berstatus Active.

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-25: Akun Inactive dalam batas rate limit

2. Pindah ke jendela guest lalu buka halaman Reset Password (Request)
3. Catat jumlah email di mail-catcher untuk `tonokurniawan+{runId}-009a@qwertysystem.net` sebagai baseline
4. Ketik `tonokurniawan+{runId}-009a@qwertysystem.net` pada field Email
5. Selesaikan reCAPTCHA (centang "I'm not a robot")
6. Klik Button [Reset Password]
7. Verifikasi caption inline di bawah field Email: "Your account is inactive"
8. Verifikasi field Email berstatus Invalid
9. Verifikasi browser tetap di halaman Reset Password
10. Verifikasi jumlah email di mail-catcher untuk `tonokurniawan+{runId}-009a@qwertysystem.net` sama dengan baseline

### TC-AUTH-RST-151: Akun Pending Activation ditolak dengan caption belum aktivasi

11. Muat ulang halaman Reset Password (F5)
12. Catat jumlah email di mail-catcher untuk `dianpratama+{runId}-009b@qwertysystem.net` sebagai baseline
13. Ketik `dianpratama+{runId}-009b@qwertysystem.net` pada field Email
14. Selesaikan reCAPTCHA (centang "I'm not a robot")
15. Klik Button [Reset Password]
16. Verifikasi caption inline di bawah field Email: "Your account has not been activated"
17. Verifikasi field Email berstatus Invalid
18. Verifikasi browser tetap di halaman Reset Password
19. Verifikasi jumlah email di mail-catcher untuk `dianpratama+{runId}-009b@qwertysystem.net` sama dengan baseline

### TC-AUTH-RST-153: Pending Activation sekaligus Inactive, status belum aktivasi dicek lebih dulu

20. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password", lalu catat jumlah baris dan baris teratas sebagai baseline
21. Pindah ke jendela guest lalu muat ulang halaman Reset Password (F5)
22. Ketik `ekapratama+{runId}-009c@qwertysystem.net` pada field Email
23. Selesaikan reCAPTCHA (centang "I'm not a robot")
24. Klik Button [Reset Password]
25. Verifikasi caption "Your account has not been activated" tampil
26. Verifikasi caption "Your account is inactive" tidak tampil
27. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password"
28. Verifikasi jumlah baris Activity Log Session bertambah tepat satu dibanding baseline
29. Verifikasi baris baru teratas untuk user dengan email `ekapratama+{runId}-009c@qwertysystem.net`: Status Failed, Note `Account is not activated`

### TC-AUTH-RST-115: Perubahan status user di Global Settings memengaruhi Request

30. Pindah ke jendela admin, buka Global Settings > User lalu klik switch Active (ON) user `budisantoso+{runId}-009d@qwertysystem.net`
31. Verifikasi dialog dengan Title "Deactivate User" tampil
32. Verifikasi body dialog memuat "This will deactivate user across all products."
33. Verifikasi body dialog memuat "Are you sure you want to deactivate it?"
34. Klik [Deactivate] pada dialog
35. Pindah ke jendela guest lalu buka halaman Reset Password (Request)
36. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-009d@qwertysystem.net` sebagai baseline
37. Ketik `budisantoso+{runId}-009d@qwertysystem.net` pada field Email
38. Selesaikan reCAPTCHA (centang "I'm not a robot")
39. Klik Button [Reset Password]
40. Verifikasi caption "Your account is inactive" tampil
41. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-009d@qwertysystem.net` sama dengan baseline
42. Pindah ke jendela admin lalu klik switch Active (OFF) user `budisantoso+{runId}-009d@qwertysystem.net` di Global Settings > User
43. Verifikasi dialog Activate tampil dengan body "This will activate user across all products. Are you sure you want to activate it?"
44. Klik [Activate] pada dialog
45. Pindah ke jendela guest, majukan jam server dan jam browser sebanyak 60 detik atau lebih, lalu muat ulang halaman Reset Password
46. Ketik `budisantoso+{runId}-009d@qwertysystem.net` pada field Email
47. Selesaikan reCAPTCHA (centang "I'm not a robot")
48. Klik Button [Reset Password]
49. Verifikasi browser menuju halaman Email Sent!
50. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-009d@qwertysystem.net` bertambah 1 dibanding baseline
51. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Entri log Failed `Account is inactive` (TC-AUTH-RST-25) dan Failed `Account is not activated` (TC-AUTH-RST-151) adalah Post Condition; entri untuk `Account is inactive` diasersi di spec `TC-AUTH-RST-E2E-040-log-request-resend`, dan entri `Account is not activated` yang diasersi di spec ini (langkah 29) adalah entri user Eka (TC-AUTH-RST-153), bukan entri Post Condition TC-AUTH-RST-151.
- Langkah "Persiapan konteks" membuka jendela admin sekali di awal; langkah "pindah ke jendela ..." adalah penghubung antar-konteks (S-03, S-07). Muat ulang halaman antar-TC adalah langkah penghubung.
- Langkah mencatat jumlah email di mail-catcher sebelum aksi adalah baseline asersi email (S-12, S-03). Pada TC-AUTH-RST-115 satu baseline dipakai untuk asersi "tidak ada email" (setelah Request ditolak) dan "bertambah 1" (setelah Request sukses).
- Temuan untuk QA: Post Condition TC-AUTH-RST-151 (entri log Failed `Account is not activated` untuk Dian) tidak punya langkah observasi di spec ini karena TC tidak menulis langkah pembacaan log untuk TC-151 (S-15).
- Temuan untuk QA: Post Condition TC-AUTH-RST-25, 151, 153 (tidak ada token dibuat) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- TC-AUTH-RST-115: dialog Deactivate User (langkah 30 sampai 34) dan dialog Activate (langkah 42 sampai 44) mengikuti TC-GS-USER-241 dan TC-GS-USER-246 di `global-settings/user/TestCases/tc-user.md`; tanpa klik konfirmasi user tetap Active dan Request di TC-AUTH-RST-115 tidak ditolak.
- Jam server dan jam browser dimajukan di langkah 45 setelah semua pembacaan Activity Log Session selesai, lalu dipulihkan di langkah 51 (S-09); hook `after` hanya cadangan.
- TC-AUTH-RST-153 memakai user terpisah dari TC-AUTH-RST-151 (TC sumber memakai `dianpratama` dengan toggle Active OFF diatur BE).
- Jumlah langkah 51 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (20 dari 51 langkah adalah Verifikasi; 31 sisanya aksi dan langkah penghubung, termasuk langkah 1 persiapan konteks). Satu topik (Request untuk status akun Inactive, Pending Activation, dan perubahan status), satu kelas harness (fungsional; jendela admin hanya membaca log atau mengubah state target, jam hanya untuk melewati cooldown), tanpa prefix login berulang (login admin sekali di langkah 1).
