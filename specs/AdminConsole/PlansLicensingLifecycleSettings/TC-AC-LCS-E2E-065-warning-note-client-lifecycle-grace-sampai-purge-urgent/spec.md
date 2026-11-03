---
id: TC-AC-LCS-E2E-065-warning-note-client-lifecycle-grace-sampai-purge-urgent
title: "Warning Note Client Lifecycle: Grace Period, Archive Period, Purge Warning, dan Purge Urgent Warning"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-319
  - TC-AC-LCS-320
  - TC-AC-LCS-321
  - TC-AC-LCS-322
coverage:
  web: automated
---

# Warning Note Client Lifecycle: Grace Period, Archive Period, Purge Warning, dan Purge Urgent Warning

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: nilai tersimpan Client Lifecycle pada default (Notify Plan Owner Before Event `45`, First Reminder Before Event `30`, Second Reminder Before Event `7`, Final Reminder Before Event `1`, Grace Period Duration `30`, Archive Period Duration `30`, Purge Warning Email `10`, Purge Urgent Warning Email `2`, Post-Purge Retention `730`); spec tidak menyimpan perubahan.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab Client Lifecycle

### TC-AC-LCS-319: Mengubah Grace Period Duration memunculkan warning note Client Lifecycle

2. Verifikasi warning note tidak tampil di bawah field Post-Purge Retention
3. Ubah Grace Period Duration dari `30` menjadi `31`, lalu klik area kosong di luar field (blur)
4. Verifikasi warning note (severity warning) tampil di bawah field Post-Purge Retention: "Changing these values will recalculate the timeline for all subscriptions currently in an active lifecycle (pre-event, grace, or archive)."
5. Kembalikan Grace Period Duration menjadi `30`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-320: Mengubah Archive Period Duration memunculkan warning note Client Lifecycle

6. Verifikasi warning note tidak tampil di bawah field Post-Purge Retention
7. Ubah Archive Period Duration dari `30` menjadi `31`, lalu klik area kosong di luar field (blur)
8. Verifikasi warning note (severity warning) tampil di bawah field Post-Purge Retention: "Changing these values will recalculate the timeline for all subscriptions currently in an active lifecycle (pre-event, grace, or archive)."
9. Kembalikan Archive Period Duration menjadi `30`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-321: Mengubah Purge Warning Email memunculkan warning note Client Lifecycle

10. Verifikasi warning note tidak tampil di bawah field Post-Purge Retention
11. Ubah Purge Warning Email dari `10` menjadi `11`, lalu klik area kosong di luar field (blur)
12. Verifikasi warning note (severity warning) tampil di bawah field Post-Purge Retention: "Changing these values will recalculate the timeline for all subscriptions currently in an active lifecycle (pre-event, grace, or archive)."
13. Kembalikan Purge Warning Email menjadi `10`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-322: Mengubah Purge Urgent Warning Email memunculkan warning note Client Lifecycle

14. Verifikasi warning note tidak tampil di bawah field Post-Purge Retention
15. Ubah Purge Urgent Warning Email dari `2` menjadi `3`, lalu klik area kosong di luar field (blur)
16. Verifikasi warning note (severity warning) tampil di bawah field Post-Purge Retention: "Changing these values will recalculate the timeline for all subscriptions currently in an active lifecycle (pre-event, grace, or archive)."
17. Kembalikan Purge Urgent Warning Email menjadi `2`, lalu klik area kosong di luar field (blur)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (berpindah ke tab Client Lifecycle) dan langkah 5, 9, 13, 17 (mengembalikan field ke nilai tersimpan sebelum TC berikutnya mengandalkan keadaan tanpa warning note, S-09).
- Asersi warning note tidak tampil memakai tab yang sudah termuat (field Post-Purge Retention dan field lain tampil) sebagai anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
