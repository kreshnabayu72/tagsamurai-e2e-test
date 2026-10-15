---
id: TC-AUTH-RST-E2E-011-request-cooldown-60s
title: "Cooldown 60 Detik pada Request Ulang untuk Email yang Sama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-29
  - TC-AUTH-RST-147
  - TC-AUTH-RST-139
coverage:
  web: automated
---

# Cooldown 60 Detik pada Request Ulang untuk Email yang Sama

## Prerequisites

- Mode: FE+BE.
- Seeding: tiga user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`, tanpa token dan tanpa percobaan reset. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya); reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Activity Log Session); fixture BE untuk menonaktifkan user dan memicu Resend pada akun Inactive di dalam cooldown (TC-AUTH-RST-139, dipanggil langsung ke endpoint Resend tanpa UI); pembekuan dan pemulihan jam server dan jam browser: jam dibekukan sebelum Request pertama dan dipertahankan sampai Request kedua (dan Resend) selesai sehingga Request kedua untuk user yang sama pasti berada di dalam cooldown 60 detik berapa pun lama eksekusi, sementara jendela admin membaca Activity Log Session pada jam nyata (jam dipulihkan sebelum itu); klien HTTP atau fixture BE untuk memanggil endpoint Resend langsung dan membaca responsnya.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: jam server dan jam browser (dibekukan hanya dari sebelum Request pertama sampai Request kedua atau Resend selesai). Suite berjalan serial (`parallel: false`). Pemulihan: jam dipulihkan sebagai langkah aksi sebelum jendela admin membuka Activity Log Session, dan di hook `after` sebagai cadangan.
- TC-AUTH-RST-29, TC-AUTH-RST-147, TC-AUTH-RST-139: User belum login (guest); browser web.
- TC-AUTH-RST-29: User `Budi Santoso` (`budisantoso+{runId}-011a@qwertysystem.net`) berstatus Active.
- TC-AUTH-RST-147: User `Citra Dewi` (`citradewi+{runId}-011b@qwertysystem.net`) berstatus Active; data Request kedua: `CITRADEWI+{runId}-011B@QWERTYSYSTEM.NET`.
- TC-AUTH-RST-139: User `Tono Kurniawan` (`tonokurniawan+{runId}-011c@qwertysystem.net`) berstatus Active saat Request pertama, lalu dinonaktifkan lewat fixture BE.

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-29: Request ulang di dalam cooldown 60 detik

2. Bekukan jam server dan jam browser pada waktu saat ini (dibekukan sampai Request kedua dan pembukaan tautan selesai)
3. Pindah ke jendela guest, buka halaman Reset Password (Request), lalu catat jumlah email di mail-catcher untuk `budisantoso+{runId}-011a@qwertysystem.net` sebagai baseline sebelum Request pertama
4. Ketik `budisantoso+{runId}-011a@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
5. Verifikasi browser menuju halaman Email Sent!
6. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-011a@qwertysystem.net` bertambah 1 dibanding baseline sebelum Request pertama (email pertama)
7. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-011a@qwertysystem.net` sebagai baseline sebelum Request kedua
8. Dengan jam masih dibekukan (di dalam cooldown 60 detik), buka halaman Reset Password (Request) lagi, ketik `budisantoso+{runId}-011a@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
9. Verifikasi browser menuju halaman Email Sent!
10. Verifikasi tidak ada toast (UI menampilkan respons seperti biasa)
11. Periksa mail-catcher
12. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-011a@qwertysystem.net` sama dengan baseline sebelum Request kedua (hanya email dari Request pertama)
13. Buka tautan dari email pertama
14. Verifikasi tautan dari email pertama masih membuka Setup New Password
15. Pulihkan jam server dan jam browser ke waktu nyata

### TC-AUTH-RST-147: Variasi huruf besar tidak menghindari cooldown 60 detik

16. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password", lalu catat jumlah baris dan baris teratas sebagai baseline B1 (sebelum Request pertama)
17. Pindah ke jendela guest, buka halaman Reset Password (Request), lalu catat jumlah email di mail-catcher untuk `citradewi+{runId}-011b@qwertysystem.net` sebagai baseline sebelum Request pertama
18. Bekukan jam server dan jam browser pada waktu saat ini (dibekukan sampai Request kedua dan pembukaan tautan selesai)
19. Ketik `citradewi+{runId}-011b@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
20. Verifikasi browser menuju halaman Email Sent!
21. Verifikasi jumlah email di mail-catcher untuk `citradewi+{runId}-011b@qwertysystem.net` bertambah 1 dibanding baseline sebelum Request pertama (email pertama)
22. Catat jumlah email di mail-catcher untuk `citradewi+{runId}-011b@qwertysystem.net` sebagai baseline sebelum Request kedua
23. Dengan jam masih dibekukan (di dalam cooldown 60 detik), buka halaman Reset Password (Request) lagi, ketik `CITRADEWI+{runId}-011B@QWERTYSYSTEM.NET`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
24. Verifikasi browser menuju halaman Email Sent!
25. Verifikasi tidak ada toast (UI menampilkan respons seperti biasa)
26. Periksa mail-catcher
27. Verifikasi jumlah email di mail-catcher untuk `citradewi+{runId}-011b@qwertysystem.net` sama dengan baseline sebelum Request kedua (hanya email dari Request pertama)
28. Buka tautan dari email pertama
29. Verifikasi tautan dari email pertama masih membuka Setup New Password
30. Pulihkan jam server dan jam browser ke waktu nyata
31. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password"
32. Verifikasi jumlah baris Activity Log Session bertambah tepat satu dibanding baseline B1 (hanya entri Success Request pertama; Request kedua tidak menambah entri)

### TC-AUTH-RST-139: Akun Inactive di dalam cooldown, status akun dicek lebih dulu

33. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password", lalu catat jumlah baris dan baris teratas sebagai baseline B2 (sebelum Request pertama)
34. Pindah ke jendela guest, buka halaman Reset Password (Request), lalu catat jumlah email di mail-catcher untuk `tonokurniawan+{runId}-011c@qwertysystem.net` sebagai baseline sebelum Request pertama
35. Bekukan jam server dan jam browser pada waktu saat ini (dibekukan sampai Request kedua dan Resend selesai)
36. Ketik `tonokurniawan+{runId}-011c@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
37. Verifikasi browser menuju halaman Email Sent! (Request pertama berhasil)
38. Nonaktifkan (Active OFF) user `tonokurniawan+{runId}-011c@qwertysystem.net` lewat fixture BE
39. Dengan jam masih dibekukan (di dalam cooldown 60 detik), buka halaman Reset Password (Request) lagi, ketik `tonokurniawan+{runId}-011c@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
40. Verifikasi caption "Your account is inactive" tampil di bawah field Email
41. Verifikasi browser tetap di halaman Reset Password
42. Verifikasi halaman Email Sent! tidak tampil
43. Periksa mail-catcher
44. Verifikasi jumlah email di mail-catcher untuk `tonokurniawan+{runId}-011c@qwertysystem.net` bertambah 1 dibanding baseline sebelum Request pertama (hanya email dari Request pertama)
45. Catat jumlah email di mail-catcher untuk `tonokurniawan+{runId}-011c@qwertysystem.net` sebagai baseline sebelum Resend
46. Dengan jam masih dibekukan (akun Inactive, cooldown belum lewat), picu Resend untuk email `tonokurniawan+{runId}-011c@qwertysystem.net` lewat fixture BE (panggilan langsung ke endpoint Resend, tanpa UI)
47. Verifikasi respons endpoint Resend sukses
48. Periksa mail-catcher
49. Verifikasi jumlah email di mail-catcher untuk `tonokurniawan+{runId}-011c@qwertysystem.net` sama dengan baseline sebelum Resend (tidak ada email baru)
50. Pulihkan jam server dan jam browser ke waktu nyata
51. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password"
52. Verifikasi jumlah baris Activity Log Session bertambah tepat tiga dibanding baseline B2 (entri Success Request pertama, entri Failed Request kedua, dan entri Failed Resend)
53. Verifikasi terdapat dua entri untuk user dengan email `tonokurniawan+{runId}-011c@qwertysystem.net` dengan Note "Account is inactive": Status Failed (entri Request kedua dan entri Resend, dicari berdasarkan Note dan email)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Asersi "tidak ada entri log baru" pada TC-AUTH-RST-29 (Expected d) diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g) lewat Request di dalam cooldown dengan baseline log sendiri. Id TC-AUTH-RST-29 tetap di `sourceTc` spec ini; rujukan dicatat di Notes kedua spec (S-05).
- P-1 (state berat): asersi "tidak ada entri log baru" TC-AUTH-RST-147 (Expected d) diasersi di spec ini pada langkah 16 dan 31 sampai 32 sebagai kenaikan tepat satu entri terhadap baseline B1 (hanya entri Success Request pertama; Request kedua tidak menambah entri), karena TC-AUTH-RST-147 bergantung pada state cooldown yang dibangun Request pertama di langkah 19 sampai 21 dan tidak punya aksi di spec absence.
- TC-AUTH-RST-147 di TC sumber memakai user yang sama dengan TC-AUTH-RST-29 (dependensi); di spec dipakai user terpisah dan Request pertama disalin utuh (S-04).
- Langkah penghubung (S-03): langkah 1 ("Persiapan konteks": jendela guest dan admin, login admin, buka Activity Log Session dengan Filter), langkah membekukan dan memulihkan jam server dan jam browser (langkah 2, 15, 18, 30, 35, 50; S-09), perpindahan jendela guest dan admin, muat ulang Activity Log Session (langkah 16, 31, 33, 51), pencatatan baseline log B1 (langkah 16) dan B2 (langkah 33), pencatatan baseline jumlah email (langkah 3, 7, 17, 22, 34, 45; S-12), serta langkah "Periksa mail-catcher" (langkah 11, 26, 43, 48) sebelum asersi email.
- Jumlah langkah 53 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (22 dari 53 langkah adalah Verifikasi; 31 sisanya aksi dan langkah penghubung, termasuk langkah 1). Satu topik (cooldown 60 detik Request), satu kelas harness (mail-catcher dan jam, bagian 6), tanpa prefix login berulang (login admin sekali di langkah 1).
- Jam dibekukan sebelum Request pertama pada TC-AUTH-RST-29, TC-AUTH-RST-147, dan TC-AUTH-RST-139 serta dipertahankan sampai Request kedua selesai (pada TC-AUTH-RST-139 sampai Resend selesai), sehingga Request kedua dan Resend pasti berada di dalam cooldown 60 detik. Baseline log B1 dan B2 dicatat sebelum jam dibekukan; baseline email sebelum Request pertama dicatat sebelum jam dibekukan pada TC-AUTH-RST-147 dan TC-AUTH-RST-139 dan sesudahnya pada TC-AUTH-RST-29 (langkah 3). Jam dipulihkan sekali per TC sebelum jendela admin membuka Activity Log Session (S-09). Pada TC-AUTH-RST-139 hasil Request kedua dan Resend akun Inactive tidak bergantung pada cooldown karena status akun dicek lebih dulu.
- Pada TC-AUTH-RST-139 langkah 52 dan 53, ketiga entri (Success Request pertama, Failed Request kedua, Failed Resend) bercap waktu sama karena jam dibekukan sepanjang ketiga aksi, sehingga entri dicari berdasarkan Note dan email user, bukan posisi teratas (S-12).
- TC-AUTH-RST-139: penonaktifan user dilakukan lewat fixture BE sesuai Precondition TC (bukan lewat UI admin) agar jendela cooldown tidak bergantung pada kecepatan UI. Resend akun Inactive di dalam cooldown dipanggil langsung ke endpoint Resend lewat fixture BE (Expected d TC-AUTH-RST-139), sehingga yang diasersi adalah respons endpoint, jumlah email, dan entri log; tidak ada toast yang diamati.
- Temuan untuk QA: Post Condition TC-AUTH-RST-29, 147 (token reset tidak berubah, counter per email dan per IP tidak bertambah) dan TC-AUTH-RST-139 (tidak ada token reset baru) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Temuan untuk QA: kolom Tipe TC-AUTH-RST-139 tertulis "Negatif" (bukan "Negative") (S-15).
- Temuan untuk QA: bagian "tanpa token baru" pada Expected d TC-AUTH-RST-139 tidak punya cara observasi di TC; yang diasersi hanya ketiadaan email baru (S-01, S-15).
