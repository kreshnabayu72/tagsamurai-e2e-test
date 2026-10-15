---
id: TC-AUTH-RST-E2E-042-log-token-states
title: "Pencatatan Status Token: Akun Nonaktif atau Dihapus, Invalidated, dan Consumed"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-100
  - TC-AUTH-RST-136
  - TC-AUTH-RST-135
coverage:
  web: automated
---

# Pencatatan Status Token: Akun Nonaktif atau Dihapus, Invalidated, dan Consumed

## Prerequisites

- Mode: FE+BE.
- Seeding: empat user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`; satu token reset aktif per user diterbitkan di hook `before` lewat API Request (kecuali TC-AUTH-RST-136), tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`, `RST_PASSWORD_ALT2`.
- Kemampuan teknis: mail-catcher; reCAPTCHA mode uji; dua tab guest per TC; jendela guest dan jendela admin terpisah (admin menonaktifkan atau menghapus user di Global Settings > User dan membaca Global Settings > Activity Log > Session dan User Log); pengaturan jam server dan jam browser bersama (cooldown ditegakkan di server, countdown [Resend email] berjalan di jam klien).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: jam server dan jam browser. Suite berjalan serial (`parallel: false`). Pemulihan: kedua jam dipulihkan di hook `after` (tetap berjalan walau spec gagal di tengah).
- TC-AUTH-RST-100, 136, 135: aksi oleh guest (browser web); admin pengamat log pada jendela terpisah.
- TC-AUTH-RST-100 (kondisi Inactive): User `Budi Santoso` (`budisantoso+{runId}-042a@qwertysystem.net`) dengan token aktif; data submit `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-100 (kondisi Deleted): User `Citra Dewi` (`citradewi+{runId}-042b@qwertysystem.net`) dengan token aktif; data submit `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-136: User `Dewi Lestari` (`dewilestari+{runId}-042c@qwertysystem.net`) Active; Request pertama dilakukan lewat UI; data submit `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-135: User `Eko Santoso` (`ekosantoso+{runId}-042d@qwertysystem.net`) dengan token aktif; data submit tab 1 `Spectra.env.RST_PASSWORD_NEW`, tab 2 `Spectra.env.RST_PASSWORD_ALT2`.

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-100: Akun nonaktif atau dihapus saat Validate Link atau Submit

2. Pindah ke jendela guest lalu buka tautan reset milik `budisantoso+{runId}-042a@qwertysystem.net` di tab 1 sehingga Setup New Password tampil
3. Pindah ke jendela admin, buka Global Settings > User lalu nonaktifkan user `budisantoso+{runId}-042a@qwertysystem.net`
4. Muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log untuk user "Budi Santoso", lalu catat jumlah baris kedua surface sebagai baseline B1
5. Pindah ke jendela guest, buka tautan yang sama di tab 2 (Validate Link)
6. Verifikasi tab 2 menampilkan Halaman 404 varian Expired
7. Pada tab 1, ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password] (Submit)
8. Verifikasi tab 1 menampilkan Halaman 404 varian Expired
9. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Budi Santoso"
10. Verifikasi jumlah baris User Log "Budi Santoso" bertambah tepat dua dibanding baseline B1 (Validate Link dan Submit)
11. Verifikasi pada kedua surface muncul dua entri baru untuk Validate Link dan untuk Submit: Activity `Reset Password`, Status Failed, Note `Reset link expired` (dicari berdasarkan Note dan email user, bukan posisi teratas)
12. Pindah ke jendela guest, buka tautan reset milik `citradewi+{runId}-042b@qwertysystem.net` di tab 1 sehingga Setup New Password tampil
13. Pindah ke jendela admin lalu hapus user `citradewi+{runId}-042b@qwertysystem.net` di Global Settings > User
14. Muat ulang Activity Log Session (Filter Activity = "Reset Password") lalu catat jumlah baris sebagai baseline B2
15. Pindah ke jendela guest, buka tautan yang sama di tab 2 (Validate Link)
16. Verifikasi tab 2 menampilkan Halaman 404 varian Expired
17. Pada tab 1, ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password] (Submit)
18. Verifikasi tab 1 menampilkan Halaman 404 varian Expired
19. Pindah ke jendela admin dan muat ulang Activity Log Session (Filter Activity = "Reset Password")
20. Verifikasi jumlah baris Activity Log Session bertambah tepat dua dibanding baseline B2
21. Verifikasi dua entri baru untuk user "Citra Dewi" (Validate Link dan Submit): Activity `Reset Password`, Status Failed, Note `Reset link expired` (dicari berdasarkan Note dan email user, bukan posisi teratas)

### TC-AUTH-RST-136: Submit dengan token yang sudah di-invalidate tercatat Failed / Reset link expired

22. Pindah ke jendela guest, buka halaman Reset Password (Request) di tab 1, ketik `dewilestari+{runId}-042c@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password] sampai halaman Email Sent! tampil (token A)
23. Buka tautan token A di tab 2 sehingga Setup New Password tampil
24. Majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
25. Pada tab 1 klik [Resend email] (token A di-invalidate, token B terbit)
26. Pulihkan jam server dan jam browser ke waktu nyata
27. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Dewi Lestari", lalu catat jumlah baris kedua surface sebagai baseline B3 (sudah memuat entri dari Request dan Resend)
28. Pindah ke jendela guest, pada tab 2 ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
29. Verifikasi tab 2 menampilkan Halaman 404 varian Expired
30. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), dan muat ulang User Log user "Dewi Lestari"
31. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B3
32. Verifikasi entri baru pada kedua surface: Activity `Reset Password`, Status Failed, Note `Reset link expired` (dicari berdasarkan Note dan email user, bukan posisi teratas)

### TC-AUTH-RST-135: Submit dengan token consumed tercatat Failed / Reset link already used

33. Pindah ke jendela guest lalu buka tautan reset milik `ekosantoso+{runId}-042d@qwertysystem.net` di tab 1 dan tab 2; keduanya menampilkan Setup New Password
34. Pada tab 1, ketik `Spectra.env.RST_PASSWORD_NEW` pada kedua field lalu klik Button [Reset Password]
35. Verifikasi tab 1 menuju halaman Password Reset Successful
36. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Eko Santoso", lalu catat jumlah baris kedua surface sebagai baseline B4 (sudah memuat entri Success dari tab 1)
37. Pindah ke jendela guest, pada tab 2 ketik `Spectra.env.RST_PASSWORD_ALT2` pada kedua field lalu klik Button [Reset Password]
38. Verifikasi tab 2 menampilkan Halaman 404 varian Already Used
39. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), dan muat ulang User Log user "Eko Santoso"
40. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B4
41. Verifikasi entri baru pada kedua surface: Activity `Reset Password`, Status Failed, Note `Reset link already used` (dicari berdasarkan Note dan email user, bukan posisi teratas)

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Temuan untuk QA: precondition TC-AUTH-RST-100 mencampur kondisi "Inactive lalu Deleted" pada satu akun; spec memecahnya per kondisi (satu user Inactive dan satu user Deleted) agar tiap token punya penyebab invalidasi yang jelas (S-15).
- TC-AUTH-RST-100 kondisi Deleted (langkah 12 sampai 21) hanya diasersi pada Activity Log Session, sesuai Expected TC: User Log user yang sudah dihapus tidak diperiksa. Kondisi Inactive memeriksa kedua surface (langkah 4 sampai 11).
- Langkah "tab 1" pada TC-AUTH-RST-136 adalah tab yang menampilkan Email Sent!; tab 2 menampilkan Setup New Password dari token A.
- Langkah penghubung (S-03): langkah 1 (persiapan jendela), pindah antar jendela guest dan admin, langkah 3 dan 13 (menonaktifkan dan menghapus user sebagai pemicu kondisi, TC-AUTH-RST-100 precondition), langkah 24 (jam dimajukan menggantikan menunggu 61 detik, konvensi bagian 6), langkah 26 (jam dipulihkan sebelum admin membuka log, S-09), dan baseline B1 sampai B4 agar entri "baru" terbukti (S-12).
- Asersi tambahan dari TC dependensi (S-03, S-04): Halaman 404 varian Expired pada langkah 6, 8, 16, 18, dan 29 berasal dari TC-AUTH-RST-60 (dependensi TC-AUTH-RST-100) dan TC-AUTH-RST-130 (dependensi TC-AUTH-RST-136); halaman Password Reset Successful pada langkah 35 dan Halaman 404 varian Already Used pada langkah 38 berasal dari TC-AUTH-RST-129 (dependensi TC-AUTH-RST-135). Asersi ini membuktikan kondisi token sebelum log diasersi dan tidak ada di Expected TC log.
- Urutan TC dalam spec (100, 136, 135) berbeda dari urutan di TC sumber (100, 135, 136); TC-AUTH-RST-135 ditaruh terakhir karena submit suksesnya mengonsumsi token milik user itu dan tidak dipakai bagian lain (S-05).
- Langkah 10 dan 20 menyatakan "tepat dua" karena Validate Link dan Submit masing-masing menulis satu entri sesuai Expected TC-AUTH-RST-100.
- Jumlah langkah 41 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (15 dari 41 langkah adalah Verifikasi; 26 sisanya aksi dan langkah penghubung: perpindahan jendela, muat ulang log, baseline, pemicu kondisi). Satu topik (pencatatan log untuk state token), satu kelas harness (fungsional dengan log dan jam), tanpa prefix login berulang (login admin sekali di langkah 1).
- Spec ini menggeser jam server sehingga entri log yang dibuat saat jam digeser bercap waktu di masa depan dan entri sesudah jam dipulihkan bisa jatuh di bawahnya. Karena itu baseline hanya mencatat jumlah baris dan asersi memakai selisih jumlah baris terhadap baseline serta pencarian entri berdasarkan Note dan email user, bukan posisi teratas (S-12).
