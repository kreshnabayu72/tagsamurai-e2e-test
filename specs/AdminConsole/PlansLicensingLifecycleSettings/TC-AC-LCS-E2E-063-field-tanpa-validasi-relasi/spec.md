---
id: TC-AC-LCS-E2E-063-field-tanpa-validasi-relasi
title: "Field Tanpa Validasi Relasi: Max Trial dan Notify Plan Owner Before Event"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-299
  - TC-AC-LCS-313
coverage:
  web: automated
---

# Field Tanpa Validasi Relasi: Max Trial dan Notify Plan Owner Before Event

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: tab Trial Settings (Max Trial Duration `30`, Max Trial Asset Quota `50`, Max Trial Concurrent User Quota `10`) dan tab Client Lifecycle (First Reminder Before Event `30`, Notify Plan Owner Before Event `45`); tidak ada Save, sehingga tidak ada nilai tersimpan yang berubah.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-299: Field Max Trial tidak punya validasi relasi antar-field

1. Ubah Max Trial Duration menjadi `1`
2. Ubah Max Trial Asset Quota menjadi `999999`
3. Ubah Max Trial Concurrent User Quota menjadi `1`
4. Klik area kosong di luar field (blur)
5. Verifikasi tidak ada pesan error pada ketiga field Max Trial (Max Trial Duration, Max Trial Asset Quota, Max Trial Concurrent User Quota)
6. Verifikasi `[Save]` enabled
7. Kembalikan Max Trial Duration menjadi `30`, Max Trial Asset Quota menjadi `50`, dan Max Trial Concurrent User Quota menjadi `10`

### TC-AC-LCS-313: Notify Plan Owner Before Event diterima pada nilai lebih besar, sama, dan lebih kecil dari First Reminder Before Event

8. Klik tab Client Lifecycle
9. Ubah Notify Plan Owner Before Event menjadi `31` (lebih besar dari First Reminder Before Event `30`), lalu klik area kosong di luar field (blur)
10. Verifikasi tidak ada pesan error
11. Verifikasi `[Save]` enabled
12. Ubah Notify Plan Owner Before Event menjadi `30` (sama dengan First Reminder Before Event), lalu klik area kosong di luar field (blur)
13. Verifikasi tidak ada pesan error
14. Verifikasi `[Save]` enabled
15. Ubah Notify Plan Owner Before Event menjadi `10` (lebih kecil dari First Reminder Before Event), lalu klik area kosong di luar field (blur)
16. Verifikasi tidak ada pesan error
17. Verifikasi `[Save]` enabled
18. Kembalikan Notify Plan Owner Before Event menjadi `45`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 7 dan 18 (mengembalikan field ke nilai tersimpan agar form tidak berakhir dirty, S-09) dan langkah 8 (berpindah ke tab Client Lifecycle).
- Asersi tidak ada pesan error dan `[Save]` enabled mengikuti Expected TC; tab yang sudah termuat menjadi anchor permukaan.
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
