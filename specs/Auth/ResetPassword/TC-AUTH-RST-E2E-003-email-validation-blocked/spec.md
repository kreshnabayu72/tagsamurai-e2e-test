---
id: TC-AUTH-RST-E2E-003-email-validation-blocked
title: "Validasi Field Email pada Halaman Request Diblokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-15
  - TC-AUTH-RST-16
  - TC-AUTH-RST-17
  - TC-AUTH-RST-18
coverage:
  web: automated
---

# Validasi Field Email pada Halaman Request Diblokir

## Prerequisites

- Mode: FE+BE. Tidak ada data yang di-seed; tidak ada akun yang login.
- Kemampuan teknis: reCAPTCHA mode uji di environment; jendela privat tanpa sesi login; mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-15, TC-AUTH-RST-16, TC-AUTH-RST-17, TC-AUTH-RST-18: User belum login (guest); browser web.
- TC-AUTH-RST-15 data: field Email dikosongkan; alamat uji untuk baseline email: `belumterdaftar+{runId}-003@qwertysystem.id`.
- TC-AUTH-RST-16 data: Email `budisantoso+{runId}-003@qwertysystem` (tanpa TLD); alamat uji valid untuk baseline email: `budisantoso+{runId}-003@qwertysystem.net`.
- TC-AUTH-RST-17 data: Email 1 `budi@qwertysystem.n`; Email 2 `belumterdaftar+{runId}-003@qwertysystem.id` (format lolos, email tidak boleh terdaftar di environment).
- TC-AUTH-RST-18 data: Email 121 karakter = 104 karakter "a" + `@qwertysystem.net`; Email 120 karakter = 103 karakter "a" + `@qwertysystem.net`.

## Test Steps

### TC-AUTH-RST-15: Field Email kosong

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `belumterdaftar+{runId}-003@qwertysystem.id` sebagai baseline
3. Selesaikan reCAPTCHA (centang "I'm not a robot")
4. Klik Button [Reset Password]
5. Verifikasi caption inline di bawah field Email: "Email must not be empty"
6. Verifikasi field Email berstatus Invalid
7. Verifikasi browser tetap di halaman Reset Password
8. Verifikasi jumlah email di mail-catcher untuk `belumterdaftar+{runId}-003@qwertysystem.id` sama dengan baseline

### TC-AUTH-RST-16: Format email salah

9. Muat ulang halaman Reset Password (F5)
10. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-003@qwertysystem.net` sebagai baseline
11. Ketik `budisantoso+{runId}-003@qwertysystem` pada field Email
12. Selesaikan reCAPTCHA (centang "I'm not a robot")
13. Klik Button [Reset Password]
14. Verifikasi caption inline di bawah field Email: "Email format is incorrect"
15. Verifikasi field Email berstatus Invalid
16. Verifikasi browser tetap di halaman Reset Password
17. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-003@qwertysystem.net` sama dengan baseline

### TC-AUTH-RST-18: Batas panjang email 121 dan 120 karakter

18. Muat ulang halaman Reset Password (F5)
19. Ketik email 121 karakter pada field Email
20. Verifikasi caption inline "Max. 120 characters" tampil saat mengetik (sebelum klik Reset Password)
21. Verifikasi field Email berstatus Invalid
22. Hapus satu karakter sehingga panjang email menjadi 120 karakter
23. Verifikasi caption "Max. 120 characters" hilang
24. Verifikasi field Email tidak berstatus Invalid

### TC-AUTH-RST-17: Batas format email: satu karakter setelah titik ditolak, dua karakter lolos format

25. Muat ulang halaman Reset Password (F5)
26. Ketik `budi@qwertysystem.n` pada field Email
27. Selesaikan reCAPTCHA (centang "I'm not a robot")
28. Klik Button [Reset Password]
29. Verifikasi caption "Email format is incorrect" tampil di bawah field Email
30. Ganti isi field Email menjadi `belumterdaftar+{runId}-003@qwertysystem.id`
31. Selesaikan reCAPTCHA (centang "I'm not a robot")
32. Klik Button [Reset Password]
33. Verifikasi caption "Email format is incorrect" tidak tampil
34. Verifikasi caption yang tampil "Email is not registered yet" (format lolos, email tidak terdaftar)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Semua kasus adalah validasi yang diblokir; tidak ada data yang tercipta.
- Urutan di spec: TC-AUTH-RST-18 ditaruh sebelum TC-AUTH-RST-17 karena TC-AUTH-RST-17 berakhir pada submit yang lolos format dan memanggil backend (validasi klien murni lebih dulu). Muat ulang halaman antar-TC adalah langkah penghubung (S-03).
- Asersi "tidak ada entri log" pada TC-AUTH-RST-15 dan 16 diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g, prinsip 10).
- Langkah mencatat jumlah email di mail-catcher sebelum aksi adalah baseline asersi "tidak ada email terkirim" (S-12, S-03). Pada TC-AUTH-RST-15 field Email kosong dan pada TC-AUTH-RST-16 alamat yang diketik tidak punya TLD, sehingga baseline diambil pada alamat uji valid milik spec ini.
- Temuan untuk QA: Post Condition TC-AUTH-RST-15, 16, 17 ("tidak ada token baru") dan "tidak ada entri log" TC-AUTH-RST-17 tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Temuan untuk QA: mekanisme reset counter rate limit per IP penguji (hook `beforeEach` suite) tidak didefinisikan di TC, PRD, maupun LLD; disediakan tim FE/BE (S-13, S-15).
- Temuan untuk QA: langkah 6 TC-AUTH-RST-17 berbunyi "Selesaikan reCAPTCHA ... bila widget kembali ke status belum dicentang", tetapi TC, PRD, dan LLD tidak menetapkan apakah widget kembali ke status belum dicentang setelah penolakan format klien. Spec menulis langkah 31 tanpa syarat (S-08) dan mengikuti TC; QA perlu menetapkan perilaku widget setelah penolakan format (S-15).
- Email `belumterdaftar+{runId}-003@qwertysystem.id` menggantikan nilai tetap TC supaya bersuffix per run.
