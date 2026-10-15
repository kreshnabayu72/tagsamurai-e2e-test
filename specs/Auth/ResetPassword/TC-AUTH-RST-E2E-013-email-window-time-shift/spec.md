---
id: TC-AUTH-RST-E2E-013-email-window-time-shift
title: "Budget Request dan Resend Bersama serta Jendela Bergulir 24 Jam per Email"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-33
  - TC-AUTH-RST-38
coverage:
  web: automated
---

# Budget Request dan Resend Bersama serta Jendela Bergulir 24 Jam per Email

## Prerequisites

- Mode: FE+BE (kelas d: geser waktu server).
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: pengatur jam server uji dan jam browser/perangkat (countdown Resend berjalan di jam klien, sehingga keduanya digeser bersama pada langkah TC-AUTH-RST-33; langkah TC-AUTH-RST-38 hanya menggeser jam server karena jendela 24 jam dihitung murni di server; kedua jam dipulihkan ke waktu nyata sebagai langkah aksi sebelum admin membaca Activity Log Session, dan jam browser tidak digeser lagi pada langkah TC-AUTH-RST-38); fixture BE untuk riwayat percobaan dengan cap waktu tertentu; mail-catcher dengan pembacaan jumlah email per alamat (asersi email baru dan tidak ada email baru memakai baseline jumlah email); reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Activity Log Session).
- State global yang diubah: jam server uji dan jam browser/perangkat. Suite berjalan serial (`parallel: false`). Pemulihan: keduanya dikembalikan ke waktu nyata sebagai langkah aksi (langkah 13 dan 20, sebelum admin membuka Activity Log Session) dan di hook `after` sebagai cadangan (tetap berjalan walau spec gagal di tengah).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-33, TC-AUTH-RST-38: User belum login (guest); browser web.
- TC-AUTH-RST-33: User `Dewi Lestari` (`dewilestari+{runId}-013a@qwertysystem.net`) Active tanpa percobaan dalam 24 jam terakhir.
- TC-AUTH-RST-38: User `Joko Lestari` (`jokolestari+{runId}-013b@qwertysystem.net`) Active dengan 5 percobaan: satu pada T0 dan empat pada T0+23 jam (fixture BE). T0 adalah cap waktu fixture yang dibaca di hook `before`; langkah 24 memakai nilai T0 itu.

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-33: Request dan Resend berbagi satu budget 5 kali per email

2. Pindah ke jendela guest, periksa mail-catcher lalu catat jumlah email untuk `dewilestari+{runId}-013a@qwertysystem.net` sebagai baseline M1
3. Buka halaman Reset Password (Request), ketik `dewilestari+{runId}-013a@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] sampai halaman Email Sent! tampil
4. Majukan jam server dan jam browser 61 detik lalu klik [Resend email]
5. Majukan jam server dan jam browser 61 detik lalu klik [Resend email]
6. Majukan jam server dan jam browser 61 detik lalu klik [Resend email]
7. Majukan jam server dan jam browser 61 detik lalu klik [Resend email] (total 5 percobaan: 1 Request dan 4 Resend)
8. Periksa mail-catcher
9. Verifikasi jumlah email reset untuk `dewilestari+{runId}-013a@qwertysystem.net` bertambah 5 dibanding baseline M1
10. Buka tautan dari email 1, email 2, email 3, dan email 4 satu per satu di tab baru
11. Verifikasi tiap tautan dari email 1 sampai email 4 menampilkan Halaman 404 dengan Title "Reset Link Expired" (tiap Resend meng-invalidate token sebelumnya)
12. Verifikasi tiap tautan dari email 1 sampai email 4 menampilkan Halaman 404 dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
13. Pulihkan jam server dan jam browser ke waktu nyata
14. Pindah ke jendela admin, muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", lalu catat jumlah entri sebagai baseline B1 (sesudah pembukaan tautan lama)
15. Pindah ke jendela guest, periksa mail-catcher lalu catat jumlah email untuk `dewilestari+{runId}-013a@qwertysystem.net` sebagai baseline M2
16. Majukan jam server dan jam browser 305 detik dari waktu nyata (melewati cooldown 60 detik sejak Resend ke-4 pada langkah 7), buka halaman Reset Password (Request), ketik `dewilestari+{runId}-013a@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
17. Verifikasi halaman Email Sent! tampil identik dengan sukses
18. Periksa mail-catcher
19. Verifikasi jumlah email untuk `dewilestari+{runId}-013a@qwertysystem.net` sama dengan baseline M2 (tidak ada email ke-6)
20. Pulihkan jam server dan jam browser ke waktu nyata
21. Pindah ke jendela admin dan muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password"
22. Verifikasi jumlah entri bertambah satu dibanding baseline B1
23. Verifikasi entri baru dengan Note `Too many reset attempts` untuk user dengan email `dewilestari+{runId}-013a@qwertysystem.net`: Activity `Reset Password`, Status Failed (dicari berdasarkan Note dan email, bukan posisi teratas, karena entri bercap waktu jam server yang dimajukan)

### TC-AUTH-RST-38: Jendela bergulir: percobaan tertua melewati 24 jam

24. Majukan jam server (tanpa jam browser) ke T0+24 jam 1 menit, dengan T0 = cap waktu fixture yang dibaca di hook `before`
25. Pindah ke jendela guest lalu buka halaman Reset Password (Request)
26. Periksa mail-catcher dan catat jumlah email untuk `jokolestari+{runId}-013b@qwertysystem.net` sebagai baseline M3
27. Ketik `jokolestari+{runId}-013b@qwertysystem.net` pada field Email
28. Selesaikan reCAPTCHA (centang "I'm not a robot")
29. Klik Button [Reset Password]
30. Verifikasi browser menuju halaman Email Sent!
31. Verifikasi tidak ada toast
32. Periksa mail-catcher
33. Verifikasi jumlah email untuk `jokolestari+{runId}-013b@qwertysystem.net` bertambah satu dibanding baseline M3 (email reset baru; percobaan pada T0 sudah keluar dari jendela 24 jam bergulir)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Titik tepat 60 detik dan tepi jendela 24 jam tidak diuji: ditahan oleh `GAP-467` di TC sumber (hanya sisi aman: 61 detik dan 24 jam 1 menit).
- Urutan: TC-AUTH-RST-33 sebelum TC-AUTH-RST-38 karena geser waktu hanya maju. T0 pada TC-AUTH-RST-38 adalah cap waktu fixture yang dibaca di hook `before`.
- TC-AUTH-RST-33 langkah 3 menyalin langkah Request dari TC-AUTH-RST-12 (S-04).
- Urutan TC-AUTH-RST-33 (S-05): langkah 10 sampai 12 (membuka tautan email 1 sampai 4, langkah 4 dan Expected c TC) dijalankan sebelum Request ke-6 (langkah 16 dan Expected b TC) karena pembukaan tautan lama dapat mencatat entri log; dengan urutan ini hitungan log untuk Request ke-6 tidak tercampur entri pembukaan tautan.
- Langkah penghubung (S-03): langkah 1 (Persiapan konteks), langkah 14, 21, dan 25 (pindah jendela, muat ulang log, buka halaman Request) bukan asersi TC. Langkah 13 dan 20 memulihkan jam server dan jam browser ke waktu nyata sebelum admin membuka Activity Log Session (S-09); langkah 16 memajukan jam 305 detik (5 interval 61 detik) karena cap waktu Resend ke-4 (langkah 7) berada di jam maju dan cooldown 60 detik harus sudah lewat. Langkah 10 sampai 12 adalah observasi Expected c TC-AUTH-RST-33 ("tiap tautan dari email 1 sampai 4 menampilkan Halaman 404"), memakai pola Halaman 404 varian Expired dari TC-AUTH-RST-43; baseline B1 diambil sesudahnya (S-12). Asersi log memakai selisih jumlah entri terhadap baseline B1 dan pencarian entri berdasarkan Note dan email, bukan posisi teratas, karena entri yang dibuat saat jam server dimajukan bercap waktu di masa depan dan setelah jam dipulihkan dapat berada di atas entri berikutnya (S-12). Muat ulang Activity Log Session selalu disertai penerapan ulang Filter Activity = "Reset Password" supaya baseline dan pembandingnya dihitung pada kumpulan baris yang sama. Langkah 2, 15, dan 26 mencatat baseline jumlah email M1, M2, dan M3 (S-12).
- Temuan untuk QA: Post Condition TC-AUTH-RST-33 ("Counter per email tetap 5") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
