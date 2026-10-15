---
id: TC-AUTH-RST-E2E-014-ip-rate-limit-429
title: "Rate Limit per IP: Penolakan 429 pada Halaman Request"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-35
  - TC-AUTH-RST-36
  - TC-AUTH-RST-142
coverage:
  web: automated
---

# Rate Limit per IP: Penolakan 429 pada Halaman Request

## Prerequisites

- Mode: FE+BE (kelas c: flood rate-limit).
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: fixture BE untuk counter Request per IP penguji (jumlah Request dalam 1 jam terakhir) yang direset sebelum tiap TC dan dipulihkan di hook `after`; pembeku jam server uji (hanya bagian TC-AUTH-RST-142, supaya Request ke-19 dan Request cooldown tetap berjarak kurang dari 60 detik); mail-catcher (memastikan tidak ada email baru lewat baseline jumlah email); reCAPTCHA mode uji; jendela privat tanpa sesi login.
- State global yang diubah: counter Request per IP penguji dan jam server uji (dibekukan pada bagian TC-AUTH-RST-142). Suite berjalan serial (`parallel: false`). Pemulihan: counter dipulihkan dan jam server dikembalikan ke waktu nyata di hook `after` (tetap berjalan walau spec gagal di tengah).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE. Spec ini mengatur counter-nya sendiri sesudah reset itu (langkah 1, 11, dan 20).
- TC-AUTH-RST-35, TC-AUTH-RST-36, TC-AUTH-RST-142: User belum login (guest); browser web.
- TC-AUTH-RST-35: counter IP penguji = 20 Request dalam 1 jam terakhir; User `Budi Santoso` (`budisantoso+{runId}-014a@qwertysystem.net`) Active.
- TC-AUTH-RST-36: counter IP penguji = 20; User `Citra Dewi` (`citradewi+{runId}-014b@qwertysystem.net`) Active dan email tidak terdaftar `belumterdaftar+{runId}-014@qwertysystem.net`.
- TC-AUTH-RST-142: counter IP penguji = 18; User `Budi Santoso` (`budisantoso+{runId}-014c@qwertysystem.net`) Active tanpa Request sebelumnya (Request ke-19 dikirim oleh langkah spec ini, bukan oleh hook `before`); User `Dewi Lestari` (`dewilestari+{runId}-014d@qwertysystem.net`) Active.

## Test Steps

### TC-AUTH-RST-35: Request ke-21 dalam 1 jam dari IP yang sama ditolak 429

1. Atur counter IP penguji menjadi 20 Request dalam 1 jam terakhir (fixture BE)
2. Periksa mail-catcher dan catat jumlah email untuk `budisantoso+{runId}-014a@qwertysystem.net` sebagai baseline B1
3. Buka jendela privat guest (tanpa sesi login) lalu buka halaman Reset Password (Request), ketik `budisantoso+{runId}-014a@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
4. Verifikasi Alert Danger tampil di atas Button [Reset Password]
5. Verifikasi Alert Danger bertuliskan "Too many requests. Please try again later."
6. Verifikasi input Email dipertahankan
7. Verifikasi Button [Reset Password] tetap enabled
8. Verifikasi widget reCAPTCHA kembali ke status belum dicentang
9. Periksa mail-catcher
10. Verifikasi jumlah email untuk `budisantoso+{runId}-014a@qwertysystem.net` tetap sama dengan baseline B1 (tidak ada email terkirim)

### TC-AUTH-RST-36: 429 per IP identik untuk email terdaftar dan tidak terdaftar

11. Atur ulang counter IP penguji menjadi 20 Request dalam 1 jam terakhir (fixture BE)
12. Buka halaman Reset Password (Request) di jendela privat baru, ketik `citradewi+{runId}-014b@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
13. Catat hasil submit pertama
14. Ubah field Email menjadi `belumterdaftar+{runId}-014@qwertysystem.net`
15. Selesaikan reCAPTCHA (centang "I'm not a robot") karena widget kembali ke status belum dicentang setelah penolakan 429
16. Klik Button [Reset Password]
17. Verifikasi kedua submit menampilkan Alert Danger di atas Button [Reset Password]
18. Verifikasi kedua submit menampilkan Alert Danger bertuliskan "Too many requests. Please try again later." yang identik
19. Verifikasi caption "Email is not registered yet" tidak tampil pada submit kedua (cek per IP terjadi sebelum pencarian email)

### TC-AUTH-RST-142: Request dalam cooldown tetap menambah counter per IP

20. Atur ulang counter IP penguji menjadi 18 Request dalam 1 jam terakhir (fixture BE)
21. Bekukan jam server uji pada waktu saat ini
22. Buka halaman Reset Password (Request) di jendela privat baru, ketik `budisantoso+{runId}-014c@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] sampai halaman Email Sent! tampil (Request ke-19, menerbitkan email 1)
23. Periksa mail-catcher dan catat jumlah email untuk `budisantoso+{runId}-014c@qwertysystem.net` sebagai baseline B2
24. Buka halaman Reset Password (Request) di jendela privat baru, ketik `budisantoso+{runId}-014c@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] (Request di dalam cooldown)
25. Verifikasi halaman Email Sent! tampil
26. Verifikasi tidak ada toast
27. Periksa mail-catcher
28. Verifikasi jumlah email untuk `budisantoso+{runId}-014c@qwertysystem.net` tetap sama dengan baseline B2 (tidak ada email baru, no-op cooldown)
29. Kembali ke halaman Reset Password, ketik `dewilestari+{runId}-014d@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
30. Verifikasi Request ke-21 ditolak dengan Alert Danger "Too many requests. Please try again later." karena Request cooldown (Request ke-20) tetap dihitung ke counter per IP
31. Kembalikan jam server uji ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Asersi "tidak ada entri log baru" pada TC-AUTH-RST-35 (butir c) dan TC-AUTH-RST-36 diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g) lewat aksi nyata dengan baseline log sendiri untuk TC-AUTH-RST-35 (id TC-AUTH-RST-35 tetap di `sourceTc` spec ini dan tidak di `sourceTc` spec 043; S-05); spec ini hanya mengasersi ketiadaan email.
- Counter IP penguji direset lewat fixture BE sebelum tiap TC (state global) dan dipulihkan di hook `after`.
- Langkah penghubung (S-03): membuka jendela privat baru (langkah 3, 12, 22, 24) adalah langkah penghubung, bukan asersi TC.
- Langkah 21 sampai 24 TC-AUTH-RST-142: Request ke-19 (langkah 22) dikirim sebagai aksi spec dan jam server dibekukan supaya Request cooldown (langkah 24) pasti berada dalam 60 detik sejak Request ke-19; precondition TC ("Request ke-19 baru berhasil kurang dari 60 detik lalu") tidak punya langkah menuju keadaannya di TC (S-14).
- Temuan untuk QA: langkah 7 TC-AUTH-RST-36 di TC berbunyi "Selesaikan reCAPTCHA ... bila widget kembali ke status belum dicentang"; spec menulisnya tanpa syarat karena TC-AUTH-RST-35 butir b menetapkan widget kembali ke status belum dicentang setelah penolakan 429 (S-08, S-15).
- Temuan untuk QA: Post Condition TC-AUTH-RST-36 ("Tidak ada token") dan TC-AUTH-RST-142 ("Counter per email Budi tidak bertambah oleh langkah 2") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
