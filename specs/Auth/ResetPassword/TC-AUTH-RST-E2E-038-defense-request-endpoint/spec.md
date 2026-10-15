---
id: TC-AUTH-RST-E2E-038-defense-request-endpoint
title: "Defense-in-Depth Request: Payload Tidak Valid, Tanpa reCAPTCHA, Token Palsu, dan Injeksi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-119
  - TC-AUTH-RST-120
  - TC-AUTH-RST-121
  - TC-AUTH-RST-128
coverage:
  web: automated
---

# Defense-in-Depth Request: Payload Tidak Valid, Tanpa reCAPTCHA, Token Palsu, dan Injeksi

## Prerequisites

- Mode: FE+BE (kelas a: defense-in-depth).
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-038@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: klien API untuk mengirim request langsung ke POST /v2/iam/auth/reset-password/request (dengan atau tanpa identifier klien native dan token reCAPTCHA); mail-catcher dengan pembacaan jumlah email per alamat; reCAPTCHA mode uji; jendela privat tanpa sesi login; pemantauan dialog skrip dan toast.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-119, 120, 121, 128: User belum login (guest); browser web.
- TC-AUTH-RST-119 data: Email `bukan-email` dengan token reCAPTCHA valid.
- TC-AUTH-RST-120 data: Email `budisantoso+{runId}-038@qwertysystem.net` tanpa identifier klien native dan tanpa token reCAPTCHA.
- TC-AUTH-RST-121 data: Email `budisantoso+{runId}-038@qwertysystem.net`; token reCAPTCHA `invalid-token`.
- TC-AUTH-RST-128 data: Email 1 `' OR '1'='1`; Email 2 `<script>alert(1)</script>`.

## Test Steps

### TC-AUTH-RST-119: Server menolak email tidak valid walau validasi UI dilewati

1. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-038@qwertysystem.net` sebagai baseline M1
2. Kirim request langsung ke POST /v2/iam/auth/reset-password/request dengan email "bukan-email" dan token reCAPTCHA valid tanpa melalui halaman Reset Password
3. Verifikasi server menolak request tanpa menerbitkan token
4. Periksa mail-catcher untuk `budisantoso+{runId}-038@qwertysystem.net` (mailbox user spec ini; alamat "bukan-email" tidak punya mailbox)
5. Verifikasi tidak ada email baru: jumlah email sama dengan baseline M1

### TC-AUTH-RST-120: Request tanpa identifier klien dan tanpa token reCAPTCHA dianggap web dan ditolak

6. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-038@qwertysystem.net` sebagai baseline M2
7. Kirim request langsung ke POST /v2/iam/auth/reset-password/request dengan email `budisantoso+{runId}-038@qwertysystem.net`, tanpa identifier klien native dan tanpa token reCAPTCHA
8. Verifikasi server menolak request dengan alasan reCAPTCHA (setara caption "Please verify that you are not a robot" pada UI)
9. Periksa mail-catcher untuk `budisantoso+{runId}-038@qwertysystem.net`
10. Verifikasi tidak ada email baru: jumlah email sama dengan baseline M2

### TC-AUTH-RST-121: Token reCAPTCHA palsu ditolak

11. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-038@qwertysystem.net` sebagai baseline M3
12. Kirim request langsung ke POST /v2/iam/auth/reset-password/request dengan email `budisantoso+{runId}-038@qwertysystem.net` dan token reCAPTCHA berisi teks acak "invalid-token"
13. Verifikasi server menolak request dengan alasan reCAPTCHA
14. Periksa mail-catcher untuk `budisantoso+{runId}-038@qwertysystem.net`
15. Verifikasi tidak ada email baru: jumlah email sama dengan baseline M3

### TC-AUTH-RST-128: Payload injeksi pada field Email tidak menimbulkan error server atau eksekusi skrip

16. Buka jendela privat baru lalu buka halaman Reset Password (Request)
17. Ketik "' OR '1'='1" pada field Email, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
18. Verifikasi caption "Email format is incorrect" tampil di bawah field Email
19. Verifikasi tidak ada dialog skrip dan tidak ada toast error server
20. Verifikasi halaman tetap berfungsi
21. Ganti isi field Email dengan "<script>alert(1)</script>" lalu klik Button [Reset Password]
22. Verifikasi caption "Email format is incorrect" tampil di bawah field Email
23. Verifikasi tidak ada dialog skrip dan tidak ada toast error server
24. Verifikasi halaman tetap berfungsi

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Asersi "tidak ada entri log" pada TC-AUTH-RST-119, 120, 121, dan 128 diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g), yang memicu aksi nyata yang sama dengan baseline log sendiri dan hanya merujuk id TC ini (id tetap milik spec ini di `sourceTc`); status HTTP penolakan tidak disebut TC sehingga tidak diasersi (S-13).
- Temuan untuk QA: Post Condition "Tidak ada token baru" TC-AUTH-RST-119, 120, 121, dan 128 tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Dialog skrip dipantau lewat handler dialog browser; `alert(1)` hanya dipicu sebagai input data, bukan dieksekusi.
