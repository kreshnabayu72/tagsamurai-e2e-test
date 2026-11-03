---
id: TC-AC-LCS-E2E-071-warning-note-tab-tanpa-warning
title: "Warning Note: Tab Tanpa Warning (Trial Settings, Free Plan, License Timing, Approval Settings, System Limits)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-331
  - TC-AC-LCS-332
  - TC-AC-LCS-333
  - TC-AC-LCS-334
  - TC-AC-LCS-335
coverage:
  web: automated
---

# Warning Note: Tab Tanpa Warning (Trial Settings, Free Plan, License Timing, Approval Settings, System Limits)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: satu field per tab (Max Trial Duration `30`, Free Plan Duration `365`, Managed Transition Time `24`, Approval Timeout `3`, Bulk Transaction Row Limit `1000`); tidak ada Save, sehingga tidak ada nilai tersimpan yang berubah.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-331: Mengubah Max Trial Duration pada tab Trial Settings tidak memunculkan warning note

1. Ubah Max Trial Duration dari `30` menjadi `31`, lalu klik area kosong di luar field (blur)
2. Verifikasi tidak ada warning note pada tab Trial Settings
3. Verifikasi `[Save]` enabled
4. Kembalikan Max Trial Duration menjadi `30`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-332: Mengubah Free Plan Duration pada tab Free Plan Settings tidak memunculkan warning note

5. Klik tab Free Plan Settings
6. Ubah Free Plan Duration dari `365` menjadi `366`, lalu klik area kosong di luar field (blur)
7. Verifikasi tidak ada warning note pada tab Free Plan Settings
8. Verifikasi `[Save]` enabled
9. Kembalikan Free Plan Duration menjadi `365`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-333: Mengubah Managed Transition Time pada tab License Timing tidak memunculkan warning note

10. Klik tab License Timing
11. Ubah Managed Transition Time dari `24` menjadi `25`, lalu klik area kosong di luar field (blur)
12. Verifikasi tidak ada warning note pada tab License Timing
13. Verifikasi `[Save]` enabled
14. Kembalikan Managed Transition Time menjadi `24`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-334: Mengubah Approval Timeout pada tab Approval Settings tidak memunculkan warning note

15. Klik tab Approval Settings
16. Ubah Approval Timeout dari `3` menjadi `4`, lalu klik area kosong di luar field (blur)
17. Verifikasi tidak ada warning note pada tab Approval Settings
18. Verifikasi `[Save]` enabled
19. Kembalikan Approval Timeout menjadi `3`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-335: Mengubah Bulk Transaction Row Limit pada tab System Limits tidak memunculkan warning note

20. Klik tab System Limits
21. Ubah Bulk Transaction Row Limit dari `1000` menjadi `1001`, lalu klik area kosong di luar field (blur)
22. Verifikasi tidak ada warning note pada tab System Limits
23. Verifikasi `[Save]` enabled
24. Kembalikan Bulk Transaction Row Limit menjadi `1000`, lalu klik area kosong di luar field (blur)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 4, 5, 9, 10, 14, 15, 19, 20, 24 (berpindah tab dan mengembalikan field ke nilai tersimpan agar form tidak berakhir dirty, S-09).
- Asersi tidak ada warning note memakai tab yang sudah termuat (field tab tampil) sebagai anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
