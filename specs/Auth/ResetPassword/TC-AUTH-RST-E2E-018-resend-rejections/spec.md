---
id: TC-AUTH-RST-E2E-018-resend-rejections
title: "Resend untuk Akun Inactive, Dihapus, dan Kuota Per Email Habis"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-47
  - TC-AUTH-RST-48
  - TC-AUTH-RST-49
coverage:
  web: automated
---

# Resend untuk Akun Inactive, Dihapus, dan Kuota Per Email Habis

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher (membaca email dan baseline jumlah email); reCAPTCHA mode uji; fixture BE untuk counter per email; jendela guest dan jendela admin terpisah (admin menonaktifkan atau menghapus user di Global Settings > User dan membaca Activity Log Session dan User Log, user dicari lewat email bersuffix); pengatur jam server uji dan jam browser/perangkat (digeser bersama 61 detik per TC, karena countdown UI berjalan di jam klien, dan dipulihkan ke waktu nyata sebagai langkah aksi sebelum admin membuka Activity Log Session atau User Log).
- State global yang diubah: jam server uji dan jam browser/perangkat. Suite berjalan serial (`parallel: false`). Pemulihan: keduanya dikembalikan ke waktu nyata sebagai langkah aksi (langkah 11, 23, dan 33) dan di hook `after` sebagai cadangan (tetap berjalan walau spec gagal di tengah).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-47, TC-AUTH-RST-48, TC-AUTH-RST-49: User belum login (guest); browser web.
- TC-AUTH-RST-47: User `Budi Santoso` (`budisantoso+{runId}-018a@qwertysystem.net`) Active.
- TC-AUTH-RST-48: User `Citra Dewi` (`citradewi+{runId}-018b@qwertysystem.net`) Active.
- TC-AUTH-RST-49: User `Fajar Nugroho` (`fajarnugroho+{runId}-018c@qwertysystem.net`) Active dengan 4 percobaan dalam 24 jam terakhir dan cooldown 60 detik sudah lewat (fixture BE).

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-47: Resend untuk akun yang menjadi Inactive setelah Request

2. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `budisantoso+{runId}-018a@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] sampai halaman Email Sent! tampil
3. Pindah ke jendela admin, buka Global Settings > User lalu nonaktifkan user `budisantoso+{runId}-018a@qwertysystem.net`
4. Muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", lalu catat jumlah entri; buka User Log user `budisantoso+{runId}-018a@qwertysystem.net` (cari lewat email) lalu catat jumlah entri sebagai baseline B2 (Activity Log Session dan User Log)
5. Pindah ke jendela guest, majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
6. Periksa mail-catcher dan catat jumlah email untuk `budisantoso+{runId}-018a@qwertysystem.net` sebagai baseline B1
7. Klik [Resend email]
8. Verifikasi toast sukses muncul: "Success, email has been sent to budisantoso+{runId}-018a@qwertysystem.net."
9. Periksa mail-catcher
10. Verifikasi jumlah email untuk `budisantoso+{runId}-018a@qwertysystem.net` tetap sama dengan baseline B1 (tidak ada email baru)
11. Pulihkan jam server dan jam browser ke waktu nyata
12. Pindah ke jendela admin, muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", dan muat ulang User Log user `budisantoso+{runId}-018a@qwertysystem.net`
13. Verifikasi Activity Log Session dan User Log masing-masing bertambah satu entri dibanding baseline B2
14. Verifikasi entri baru dengan Note `Account is inactive` untuk user dengan email `budisantoso+{runId}-018a@qwertysystem.net` pada kedua surface: Status Failed (dicari berdasarkan Note dan email, bukan posisi teratas)

### TC-AUTH-RST-48: Resend untuk akun yang dihapus tetap menampilkan toast sukses tanpa email

15. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `citradewi+{runId}-018b@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] sampai halaman Email Sent! tampil
16. Pindah ke jendela admin, buka Global Settings > User lalu hapus user `citradewi+{runId}-018b@qwertysystem.net`
17. Pindah ke jendela guest, majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
18. Periksa mail-catcher dan catat jumlah email untuk `citradewi+{runId}-018b@qwertysystem.net` sebagai baseline B3
19. Klik [Resend email]
20. Verifikasi toast sukses muncul: "Success, email has been sent to citradewi+{runId}-018b@qwertysystem.net."
21. Periksa mail-catcher
22. Verifikasi jumlah email untuk `citradewi+{runId}-018b@qwertysystem.net` tetap sama dengan baseline B3 (tidak ada email baru)
23. Pulihkan jam server dan jam browser ke waktu nyata

### TC-AUTH-RST-49: Resend melebihi batas per email menampilkan toast sukses tanpa email dan dicatat

24. Buka halaman Reset Password (Request) di jendela guest, ketik `fajarnugroho+{runId}-018c@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] sampai halaman Email Sent!
25. Pindah ke jendela admin, muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", lalu catat jumlah entri; buka User Log user `fajarnugroho+{runId}-018c@qwertysystem.net` (cari lewat email) lalu catat jumlah entri sebagai baseline B5 (Activity Log Session dan User Log)
26. Pindah ke jendela guest, majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
27. Periksa mail-catcher dan catat jumlah email untuk `fajarnugroho+{runId}-018c@qwertysystem.net` sebagai baseline B4
28. Klik [Resend email]
29. Verifikasi toast sukses muncul: "Success, email has been sent to fajarnugroho+{runId}-018c@qwertysystem.net."
30. Verifikasi tidak ada toast error
31. Periksa mail-catcher
32. Verifikasi jumlah email untuk `fajarnugroho+{runId}-018c@qwertysystem.net` tetap sama dengan baseline B4 (tidak ada email baru)
33. Pulihkan jam server dan jam browser ke waktu nyata
34. Pindah ke jendela admin, muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", dan muat ulang User Log user `fajarnugroho+{runId}-018c@qwertysystem.net`
35. Verifikasi Activity Log Session dan User Log masing-masing bertambah satu entri dibanding baseline B5
36. Verifikasi entri baru dengan Note `Too many reset attempts` untuk user dengan email `fajarnugroho+{runId}-018c@qwertysystem.net` pada kedua surface: Status Failed (dicari berdasarkan Note dan email, bukan posisi teratas)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Asersi "tidak ada entri log baru" pada TC-AUTH-RST-48 diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g) lewat aksi nyata dengan baseline log sendiri untuk TC-AUTH-RST-48 (id TC-AUTH-RST-48 tetap di `sourceTc` spec ini dan tidak di `sourceTc` spec 043; S-05).
- Langkah penghubung (S-03, S-07): langkah "pindah ke jendela ..." dan Persiapan konteks (langkah 1) adalah penghubung antar-konteks. Countdown Resend dipenuhi dengan memajukan jam server dan jam browser 61 detik per TC (bukan menunggu nyata). Langkah 11, 23, dan 33 memulihkan kedua jam ke waktu nyata sebelum admin membuka Activity Log Session atau User Log (S-09).
- Urutan di spec (S-05): pada TC-AUTH-RST-47, 48, dan 49 penonaktifan atau penghapusan user dan baseline log admin dijalankan sebelum jam dimajukan, supaya admin membaca log pada jam nyata; precondition TC (akun berubah sesudah Request, countdown sudah lewat saat Resend diklik) tetap terpenuhi. Baseline email B1, B3, dan B4 diambil tepat sebelum klik [Resend email]. Muat ulang Activity Log Session selalu disertai penerapan ulang Filter Activity = "Reset Password". Resend yang dipicu saat jam dimajukan 61 detik mencatat entri bercap waktu di masa depan, sehingga asersi log memakai selisih jumlah entri terhadap baseline (B2, B5) dan pencarian entri berdasarkan Note dan email, bukan posisi teratas (S-12).
- Temuan untuk QA: Post Condition TC-AUTH-RST-47 dan TC-AUTH-RST-49 ("Tidak ada token baru dan token aktif sebelumnya tidak berubah") dan TC-AUTH-RST-48 ("Tidak ada token baru") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Jumlah langkah 36 melampaui ±35: alasan satu topik (Resend untuk akun Inactive, dihapus, dan kuota habis) dan satu kelas, 11 langkah Verifikasi akibat pemecahan per klausa (S-01) dan sisanya aksi, baseline, serta pemulihan jam, tanpa prefix login berulang.
