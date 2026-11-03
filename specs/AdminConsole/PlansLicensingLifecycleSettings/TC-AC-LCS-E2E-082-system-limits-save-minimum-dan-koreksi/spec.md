---
id: TC-AC-LCS-E2E-082-system-limits-save-minimum-dan-koreksi
title: "Tab System Limits: Save Nilai Minimum dan Koreksi Nilai Salah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-284
  - TC-AC-LCS-291
coverage:
  web: automated
---

# Tab System Limits: Save Nilai Minimum dan Koreksi Nilai Salah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: Bulk Transaction Row Limit `99` lalu `1001`; nilai minimum Save: Bulk Transaction Row Limit `100`, Selection Limit `100`, Register Asset Bulk Limit `100`, Hierarchy Depth Limit `5`, Master Data Count Limit `1000`, Max Visible Columns `20`.
- State global yang diubah: keenam nilai tersimpan System Limits menjadi nilai minimum pada TC-AC-LCS-284; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab System Limits

### TC-AC-LCS-291: Tab System Limits: memperbaiki nilai yang salah menghapus pesan error dan meng-enable Save

2. Isi Bulk Transaction Row Limit dengan `99`, lalu klik area kosong di luar field (blur)
3. Verifikasi pesan error rentang "Value must be between 100 and 5,000" tampil
4. Verifikasi `[Save]` disabled
5. Isi Bulk Transaction Row Limit dengan `1001`, lalu klik area kosong di luar field (blur)
6. Verifikasi pesan error hilang
7. Verifikasi `[Save]` enabled

### TC-AC-LCS-284: Save tab System Limits dengan nilai minimum yang valid

8. Ubah Bulk Transaction Row Limit menjadi `100`
9. Ubah Selection Limit menjadi `100`
10. Ubah Register Asset Bulk Limit menjadi `100`
11. Ubah Hierarchy Depth Limit menjadi `5`
12. Ubah Master Data Count Limit menjadi `1000`
13. Ubah Max Visible Columns menjadi `20`
14. Verifikasi tidak ada pesan error pada seluruh field yang diisi
15. Klik `[Save]`
16. Verifikasi toast sukses "Success, system limits settings have been saved."
17. Verifikasi tab refresh: Bulk Transaction Row Limit `100`
18. Verifikasi tab refresh: Selection Limit `100`
19. Verifikasi tab refresh: Register Asset Bulk Limit `100`
20. Verifikasi tab refresh: Hierarchy Depth Limit `5`
21. Verifikasi tab refresh: Master Data Count Limit `1000`
22. Verifikasi tab refresh: Max Visible Columns `20`
23. Verifikasi `[Save]` disabled setelah tab refresh

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (berpindah ke tab).
- Urutan di spec: TC-AC-LCS-291 sebelum TC-AC-LCS-284 (koreksi nilai yang diblokir sebelum Save sukses, S-10); urutan nomor TC berbeda.
- Teks pesan error rentang pada TC-AC-LCS-291 diambil dari TC validasi field Bulk Transaction Row Limit (Value must be between 100 and 5,000); Expected TC hanya menyebut "pesan error rentang".
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - Expected TC-AC-LCS-291 menyebut "pesan error rentang" tanpa teks; spec memakai teks dari TC validasi field yang sama.
