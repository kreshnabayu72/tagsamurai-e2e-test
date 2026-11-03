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
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); spec menulis nilai uji sesuai TC (S-02).
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: satu field per tab (Max Trial Duration `30`, Free Plan Duration `365`, Managed Transition Time `24`, Approval Timeout `3`, Bulk Transaction Row Limit `1000`); tidak ada Save, sehingga tidak ada nilai tersimpan yang berubah.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-331: Mengubah Max Trial Duration pada tab Trial Settings tidak memunculkan warning note

1. Ubah Max Trial Duration dari `30` menjadi `31`, lalu klik area kosong di luar field (blur)
2. Verifikasi Field Max Trial Duration tetap tampil bernilai `31`
3. Verifikasi tidak ada warning note pada tab Trial Settings
4. Verifikasi `[Save]` enabled
5. Kembalikan Max Trial Duration menjadi `30`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-332: Mengubah Free Plan Duration pada tab Free Plan Settings tidak memunculkan warning note

6. Klik tab Free Plan Settings
7. Ubah Free Plan Duration dari `365` menjadi `366`, lalu klik area kosong di luar field (blur)
8. Verifikasi Field Free Plan Duration tetap tampil bernilai `366`
9. Verifikasi tidak ada warning note pada tab Free Plan Settings
10. Verifikasi `[Save]` enabled
11. Kembalikan Free Plan Duration menjadi `365`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-333: Mengubah Managed Transition Time pada tab License Timing tidak memunculkan warning note

12. Klik tab License Timing
13. Ubah Managed Transition Time dari `24` menjadi `25`, lalu klik area kosong di luar field (blur)
14. Verifikasi Field Managed Transition Time tetap tampil bernilai `25`
15. Verifikasi tidak ada warning note pada tab License Timing
16. Verifikasi `[Save]` enabled
17. Kembalikan Managed Transition Time menjadi `24`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-334: Mengubah Approval Timeout pada tab Approval Settings tidak memunculkan warning note

18. Klik tab Approval Settings
19. Ubah Approval Timeout dari `3` menjadi `4`, lalu klik area kosong di luar field (blur)
20. Verifikasi Field Approval Timeout tetap tampil bernilai `4`
21. Verifikasi tidak ada warning note pada tab Approval Settings
22. Verifikasi `[Save]` enabled
23. Kembalikan Approval Timeout menjadi `3`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-335: Mengubah Bulk Transaction Row Limit pada tab System Limits tidak memunculkan warning note

24. Klik tab System Limits
25. Ubah Bulk Transaction Row Limit dari `1000` menjadi `1001`, lalu klik area kosong di luar field (blur)
26. Verifikasi Field Bulk Transaction Row Limit tetap tampil bernilai `1001`
27. Verifikasi tidak ada warning note pada tab System Limits
28. Verifikasi `[Save]` enabled
29. Kembalikan Bulk Transaction Row Limit menjadi `1000`, lalu klik area kosong di luar field (blur)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 5, 6, 11, 12, 17, 18, 23, 24, 29 (berpindah tab dan mengembalikan field ke nilai tersimpan agar form tidak berakhir dirty, S-09).
- Langkah 2, 8, 14, 20, dan 26 adalah `Verifikasi` anchor field yang diubah tetap tampil bernilai baru (klausa kedua Expected a TC-AC-LCS-331 sampai TC-AC-LCS-335) sebelum asersi absence warning note pada langkah 3, 9, 15, 21, dan 27 (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
