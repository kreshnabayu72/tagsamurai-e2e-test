---
id: TC-AUTH-RST-E2E-010-request-special-client-conditions
title: "Request Sukses pada Client Suspended, Plan Starter, dan Pending Email Confirmation"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-26
  - TC-AUTH-RST-27
  - TC-AUTH-RST-154
coverage:
  web: automated
---

# Request Sukses pada Client Suspended, Plan Starter, dan Pending Email Confirmation

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) milik Client masing-masing, Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. TC-AUTH-RST-26 pada Client uji S (Suspended): `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` milik Client uji S, kredensial `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD`. TC-AUTH-RST-27 pada Client uji berplan Starter: `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` milik Client Starter, kredensial `Spectra.env.GS_PLANSTARTER_TC_PASSWORD`. TC-AUTH-RST-154: akun `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), tanpa token dan tanpa percobaan reset. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `GS_CLIENTSUSP_TC_PASSWORD`, `GS_PLANSTARTER_TC_PASSWORD`, `RST_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: Client uji S berstatus suspended (read-only) dan Client uji berplan Starter (fixture Client disiapkan tim FE/BE; user Client S di-seed saat Client masih aktif, lalu hook `before` mengubah status Client S menjadi Suspended, dan hook `after` memulihkan status Client S ke aktif sebelum menghapus user; mekanisme mengubah dan memulihkan status Client dari hook tidak didefinisikan di TC, PRD, maupun LLD); mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya); reCAPTCHA mode uji; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: status Client uji S (Suspended). Suite berjalan serial (`parallel: false`). Pemulihan: status Client S dipulihkan ke aktif di hook `after`.
- TC-AUTH-RST-26, TC-AUTH-RST-27, TC-AUTH-RST-154: User belum login (guest); browser web.
- TC-AUTH-RST-26: User `Rudi Hartono` (`rudihartono+{runId}-010a@qwertysystem.net`) berstatus Active pada Client berstatus suspended (read-only).
- TC-AUTH-RST-27: User `Maya Putri` (`mayaputri+{runId}-010b@qwertysystem.net`) berstatus Active pada Client berplan Starter.
- TC-AUTH-RST-154: User `Linda Sari` (`lindasari+{runId}-010c@qwertysystem.net`) berstatus Active dan Activated; email baru `lindasari.baru+{runId}-010c@qwertysystem.net` pending konfirmasi oleh admin (di-seed lewat API di hook `before`).

## Test Steps

### TC-AUTH-RST-26: Client suspended diproses seperti biasa

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `rudihartono+{runId}-010a@qwertysystem.net` sebagai baseline
3. Ketik `rudihartono+{runId}-010a@qwertysystem.net` pada field Email
4. Selesaikan reCAPTCHA (centang "I'm not a robot")
5. Klik Button [Reset Password]
6. Verifikasi browser menuju halaman Email Sent!
7. Verifikasi tidak ada toast
8. Verifikasi jumlah email di mail-catcher untuk `rudihartono+{runId}-010a@qwertysystem.net` bertambah 1 dibanding baseline

### TC-AUTH-RST-27: Client berplan Starter tidak dibatasi plan

9. Buka halaman Reset Password (Request) di jendela privat baru
10. Catat jumlah email di mail-catcher untuk `mayaputri+{runId}-010b@qwertysystem.net` sebagai baseline
11. Ketik `mayaputri+{runId}-010b@qwertysystem.net` pada field Email
12. Selesaikan reCAPTCHA (centang "I'm not a robot")
13. Klik Button [Reset Password]
14. Verifikasi browser menuju halaman Email Sent!
15. Verifikasi tidak ada toast
16. Verifikasi jumlah email di mail-catcher untuk `mayaputri+{runId}-010b@qwertysystem.net` bertambah 1 dibanding baseline

### TC-AUTH-RST-154: Email lama user dengan Pending Email Confirmation diproses normal

17. Buka halaman Reset Password (Request) di jendela privat baru
18. Catat jumlah email di mail-catcher untuk `lindasari+{runId}-010c@qwertysystem.net` sebagai baseline
19. Ketik `lindasari+{runId}-010c@qwertysystem.net` pada field Email
20. Selesaikan reCAPTCHA (centang "I'm not a robot")
21. Klik Button [Reset Password]
22. Verifikasi browser menuju halaman Email Sent!
23. Verifikasi tidak ada toast
24. Verifikasi jumlah email di mail-catcher untuk `lindasari+{runId}-010c@qwertysystem.net` bertambah 1 dibanding baseline

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Entri log Success `Password reset requested` pada TC-AUTH-RST-154 (Post Condition) diasersi pada spec `TC-AUTH-RST-E2E-040-log-request-resend` untuk jenis aksi yang sama (Request sukses, TC-AUTH-RST-94).
- Pembukaan halaman baru antar-TC dan pencatatan baseline jumlah email sebelum aksi adalah langkah penghubung (S-03, S-12).
- Temuan untuk QA: aktor dan API yang mengubah serta memulihkan status Client uji S (Suspended) dari hook tidak disebut di TC, PRD, maupun LLD (TC-AUTH-RST-26 hanya menyatakan Precondition "Client berstatus suspended"); mekanismenya disediakan tim FE/BE, sama seperti Auth > MFA spec 038 (S-15).
- Temuan untuk QA: Post Condition TC-AUTH-RST-26, 27, 154 (token reset aktif baru terbit) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
