---
id: TC-AC-SU-E2E-177-resilience-resend-gagal-dan-kegagalan-penulisan-log
title: "Resilience Resend Email Gagal Layanan Email atau Server dan Kegagalan Penulisan Log tidak Membatalkan Pengiriman"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-151
  - TC-AC-SU-158
  - TC-AC-SU-160
  - TC-AC-SU-635
coverage:
  web: automated
---

# Resilience Resend Email Gagal Layanan Email atau Server dan Kegagalan Penulisan Log tidak Membatalkan Pengiriman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu set user bersama (nama berprefix `{runId}-177`):

| Kode | Name | Email | State awal |
|---|---|---|---|
| A | `Mike Tan {runId}-177A` | `miketan+{runId}-177a@qwertysystem.net` | Pending Activation, di luar cooldown Resend |
| B | `Sarah Lee {runId}-177B` | `sarahlee+{runId}-177b@qwertysystem.net` | Pending Activation, di luar cooldown Resend |

- Kemampuan teknis (kelas b): (1) kegagalan Layanan email (pengiriman email gagal) yang diaktifkan dan dipulihkan lewat kemampuan BE yang disediakan tim FE/BE (bukan intercept; TC-151 dan TC-635); (2) `Spectra.intercept()` pada respons request Bulk Resend dengan 500 (TC-158); (3) kegagalan penulisan log yang diaktifkan dan dipulihkan lewat kemampuan BE yang disediakan tim FE/BE (TC-160). Mekanisme tiap kegagalan tidak disebut TC, PRD, atau LLD (S-13). Seluruh kegagalan dipulihkan di hook `after` yang tetap jalan walau spec gagal di tengah.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-151: Resend gagal karena Layanan email error
1. Aktifkan kegagalan Layanan email, lalu ketik Search `Mike Tan {runId}-177A`, tekan Enter
2. Buka row action (⋯) baris A, lalu klik Resend Activation Email
3. Verifikasi toast error `"Error, failed to send email."`
4. Klik row action (⋯) baris A lagi
5. Verifikasi opsi Resend Activation Email tetap enabled untuk retry
### TC-AC-SU-635: Resend gagal di Layanan email tidak memulai cooldown
6. Tutup menu row action, lalu ketik Search `Sarah Lee {runId}-177B`, tekan Enter dan tunggu toast error lama hilang otomatis
7. Buka row action (⋯) baris B, lalu klik Resend Activation Email
8. Verifikasi toast error `"Error, failed to send email."`
9. Verifikasi tombol Resend Activation Email baris B tetap enabled untuk retry
### TC-AC-SU-158: Bulk Resend gagal menyeluruh (5xx)
10. Pulihkan Layanan email, atur intercept: respons request Bulk Resend dikembalikan 500, lalu tunggu toast error lama hilang otomatis
11. Ketik Search `{runId}-177`, tekan Enter, lalu centang baris A dan baris B
12. Klik `[Bulk Action ▾]`, lalu pilih `Resend Activation Email`
13. Verifikasi toast error `"Error, failed to send email."`
### TC-AC-SU-160: Kegagalan menulis log Resend tidak membatalkan pengiriman email
14. Lepas intercept, klik icon `×` pada Bulk Action Bar, lalu aktifkan kegagalan penulisan log
15. Ketik Search `Mike Tan {runId}-177A`, tekan Enter dan tunggu toast error lama hilang otomatis
16. Buka row action (⋯) baris A, lalu klik Resend Activation Email
17. Verifikasi toast sukses `"Success, email has been sent."`

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): mengaktifkan dan memulihkan kegagalan, Search baris target (R-16), menutup menu row action, klik icon `×` pada Bulk Action Bar untuk melepas seleksi parsial (S-09), dan menunggu toast lama hilang (R-12). TC-160 dijalankan terakhir karena Resend yang sukses memulai cooldown pada baris A.
- TC-151 dan TC-635 adalah pasangan topik yang sama dengan sudut berbeda (kegagalan Layanan email pada user berbeda); keduanya tetap di spec ini sebagai blok terpisah. Post Condition TC-151 ("Tidak ada entri log Resend") dan TC-160 (email terkirim, penulisan log dicoba ulang dan kegagalan akhir ditandai) tidak punya langkah observasi di TC dan tidak diasersi.
- Empat blok kelas b berpola sama (kegagalan dipaksa, aksi Resend, toast); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-151, TC-158, TC-160, dan TC-635 tidak menyebut cara memicu kegagalan Layanan email, respons 500 pada Bulk Resend, dan kegagalan penulisan log; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-160 tidak memberi cara mengamati bahwa email terkirim walau log gagal; spec hanya mengasersi toast sukses sesuai Expected TC.
  - TC memakai nama literal `Mike Tan` dan `Sarah Lee`; spec memakai nama bersuffix (S-12).
