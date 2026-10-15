---
id: TC-AUTH-RST-E2E-027-server-rejection-then-success
title: "Penolakan Server atas Password Tidak Valid lalu Submit Sukses pada Token yang Sama"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-75
  - TC-AUTH-RST-77
  - TC-AUTH-RST-78
  - TC-AUTH-RST-79
  - TC-AUTH-RST-76
coverage:
  web: automated
---

# Penolakan Server atas Password Tidak Valid lalu Submit Sukses pada Token yang Sama

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-027@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`; satu token reset aktif diterbitkan di hook `before` lewat API Request, tautan diambil dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Hook `before` (akun aktor): membuka jendela privat guest dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), membuka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password", dan mencatat jumlah baris Failed milik user "Budi Santoso" di Activity Log Session dan User Log sebagai baseline awal. Hook `after` menutup kedua jendela dan mengembalikan sesi ke akun default suite.
- Kemampuan teknis: mail-catcher; reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Activity Log Session dan User Log).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-75, TC-AUTH-RST-77, TC-AUTH-RST-78, TC-AUTH-RST-79, TC-AUTH-RST-76: User belum login (guest); browser web; Setup New Password terbuka dari tautan reset.
- TC-AUTH-RST-75 data: Password dan Confirm Password `abc` (literal; submit diblokir).
- TC-AUTH-RST-77 data: Password dan Confirm Password `Aa1!` + 69 karakter "a" (73 karakter; literal, submit diblokir).
- TC-AUTH-RST-78 data: Password dan Confirm Password berupa `Spectra.env.RST_PASSWORD_NEW` dengan spasi di awal dan akhir (" " + nilai env + " "; submit diblokir).
- TC-AUTH-RST-79 data: Password dan Confirm Password `Spectra.env.RST_PASSWORD` (sama dengan password aktif).
- TC-AUTH-RST-76 data: Password dan Confirm Password `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### TC-AUTH-RST-75: Password yang melanggar kebijakan ditolak server dan checklist tetap belum terpenuhi

1. Buka tautan reset milik `budisantoso+{runId}-027@qwertysystem.net` dari mail-catcher di jendela guest sehingga Setup New Password tampil
2. Ketik "abc" pada field Password dan "abc" pada field Confirm Password
3. Klik Button [Reset Password]
4. Verifikasi browser tetap di halaman Setup New Password
5. Verifikasi form tetap terbuka
6. Verifikasi input dipertahankan
7. Verifikasi item checklist yang belum terpenuhi tetap berstatus lingkaran kosong abu-abu
8. Verifikasi Button [Reset Password] kembali enabled
9. Pindah ke jendela admin, muat ulang Activity Log Session, dan buka User Log user "Budi Santoso"
10. Verifikasi jumlah baris Failed milik user "Budi Santoso" bertambah 1 dibanding baseline pada Activity Log Session dan User Log
11. Verifikasi entri Failed teratas pada kedua surface: Activity `Reset Password`, Status Failed, Note `Password does not meet requirements`
12. Catat jumlah baris Failed milik user "Budi Santoso" pada kedua surface sebagai baseline berikutnya
13. Pindah ke jendela guest

### TC-AUTH-RST-77: Password 73 karakter ditolak

14. Kosongkan field Password dan Confirm Password lalu ketik password 73 karakter (`Aa1!` + 69 karakter "a") pada kedua field
15. Klik Button [Reset Password]
16. Verifikasi caption "Max. 72 characters" tetap tampil pada field Password
17. Verifikasi browser tetap di halaman Setup New Password
18. Verifikasi form tetap terbuka
19. Verifikasi input dipertahankan
20. Pindah ke jendela admin, muat ulang Activity Log Session, dan buka User Log user "Budi Santoso"
21. Verifikasi jumlah baris Failed milik user "Budi Santoso" bertambah 1 dibanding baseline pada Activity Log Session dan User Log
22. Verifikasi entri Failed teratas pada kedua surface: Status Failed, Note `Password does not meet requirements`
23. Catat jumlah baris Failed milik user "Budi Santoso" pada kedua surface sebagai baseline berikutnya
24. Pindah ke jendela guest

### TC-AUTH-RST-78: Password dengan spasi di awal atau akhir tidak di-trim dan ditolak

25. Kosongkan field Password dan Confirm Password lalu ketik `Spectra.env.RST_PASSWORD_NEW` dengan spasi di awal dan akhir (" " + nilai env + " ") pada kedua field
26. Verifikasi item "Password cannot contain spaces" berstatus belum terpenuhi
27. Klik Button [Reset Password]
28. Verifikasi submit ditolak: browser tetap di halaman Setup New Password
29. Pindah ke jendela admin, muat ulang Activity Log Session, dan buka User Log user "Budi Santoso"
30. Verifikasi jumlah baris Failed milik user "Budi Santoso" bertambah 1 dibanding baseline pada Activity Log Session dan User Log
31. Verifikasi entri Failed teratas pada kedua surface: Status Failed, Note `Password does not meet requirements`
32. Catat jumlah baris Failed milik user "Budi Santoso" pada kedua surface sebagai baseline berikutnya
33. Pindah ke jendela guest

### TC-AUTH-RST-79: Password sama dengan password aktif

34. Kosongkan field Password dan Confirm Password lalu ketik `Spectra.env.RST_PASSWORD` pada kedua field
35. Klik Button [Reset Password]
36. Verifikasi caption inline pada field Password: "Password must be different from your old password"
37. Verifikasi field Password berstatus Invalid
38. Verifikasi browser tetap di halaman Setup New Password
39. Verifikasi form tetap terbuka
40. Verifikasi input dipertahankan
41. Pindah ke jendela admin, muat ulang Activity Log Session, dan buka User Log user "Budi Santoso"
42. Verifikasi jumlah baris Failed milik user "Budi Santoso" bertambah 1 dibanding baseline pada Activity Log Session dan User Log
43. Verifikasi entri Failed teratas pada kedua surface: Status Failed, Note `Password does not meet requirements`
44. Catat jumlah baris Failed milik user "Budi Santoso" pada kedua surface sebagai baseline berikutnya
45. Pindah ke jendela guest

### TC-AUTH-RST-76: Token yang ditolak masih dapat dipakai pada submit berikutnya

46. Kosongkan field Password dan Confirm Password lalu ketik `Spectra.env.RST_PASSWORD_NEW` pada kedua field
47. Klik Button [Reset Password]
48. Verifikasi browser menuju halaman Password Reset Successful

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Semua penolakan memakai satu token yang tetap active; submit sukses (TC-AUTH-RST-76) paling akhir karena mengonsumsi token (bagian 3 prinsip 3 dan 5).
- Entri log Failed `Password does not meet requirements` (Expected TC-AUTH-RST-75 butir d, TC-AUTH-RST-77 butir c, TC-AUTH-RST-78 butir c, TC-AUTH-RST-79 butir c) diasersi langsung di spec ini lewat jendela admin dengan baseline jumlah baris Failed (S-12); spec `TC-AUTH-RST-E2E-041-log-submit` mengulang aksi sejenis untuk TC-AUTH-RST-98 dan TC-AUTH-RST-101.
- Langkah penghubung (S-03): pindah jendela guest dan admin, muat ulang log, pencatatan baseline, dan pengosongan field antar-TC (S-09). Filter Activity = "Reset Password" aktif di Activity Log Session, sehingga atribut Activity hanya diasersi pada TC-AUTH-RST-75 yang Expected-nya menyebut Activity; TC-AUTH-RST-77, 78, dan 79 hanya Status dan Note sesuai Expected TC.
- TC-AUTH-RST-79 tidak bergantung pada TC lain selain token yang sama.
- Temuan untuk QA: (1) TC-AUTH-RST-78 Expected b memuat klausa password user tetap sama dengan password aktif (`Spectra.env.RST_PASSWORD`) tanpa langkah observasi di TC, sehingga tidak diasersi (S-01, S-15); (2) Post Condition TC-AUTH-RST-75, 77, 78, 79 (token tetap active, password user tidak berubah) dan TC-AUTH-RST-76 (token berstatus consumed) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Jumlah langkah 48 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (25 dari 48 langkah adalah Verifikasi; 23 sisanya aksi dan langkah penghubung: perpindahan jendela, muat ulang log, baseline, pengosongan field). Satu topik (penolakan server pada Submit lalu sukses), satu kelas harness (fungsional; jendela admin hanya membaca log), tanpa prefix login berulang (tidak ada login).
