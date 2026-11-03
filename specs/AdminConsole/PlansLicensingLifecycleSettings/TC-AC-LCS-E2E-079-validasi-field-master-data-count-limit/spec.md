---
id: TC-AC-LCS-E2E-079-validasi-field-master-data-count-limit
title: "Validasi Field Master Data Count Limit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-272
  - TC-AC-LCS-273
  - TC-AC-LCS-274
  - TC-AC-LCS-275
  - TC-AC-LCS-276
coverage:
  web: automated
---

# Validasi Field Master Data Count Limit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: field Master Data Count Limit (default `10000`, rentang valid sesuai pesan error "Value must be between 1,000 and 100,000").
- State global yang diubah: nilai tersimpan Master Data Count Limit menjadi `100000` pada TC-AC-LCS-276; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab System Limits

### TC-AC-LCS-272: Field Master Data Count Limit menolak karakter non-numerik

2. Klik di akhir nilai field Master Data Count Limit
3. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
4. Verifikasi karakter non-numerik tidak tampil pada field Master Data Count Limit
5. Verifikasi nilai Master Data Count Limit tetap `10000`
6. Verifikasi tidak ada pesan error
7. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-273: Field Master Data Count Limit dikosongkan, placeholder tampil, dan blur mengisi otomatis nilai minimum

8. Pilih seluruh isi field Master Data Count Limit (Ctrl+A) lalu tekan Delete
9. Verifikasi placeholder "Enter master data count limit" tampil pada field kosong
10. Klik area kosong di luar field (blur)
11. Verifikasi field terisi otomatis `1000`
12. Verifikasi tidak ada pesan error
13. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-274: Field Master Data Count Limit diisi 999 (di bawah minimum) menampilkan error rentang

14. Pilih seluruh isi field Master Data Count Limit lalu ketik `999`
15. Klik area kosong di luar field (blur)
16. Verifikasi inline error text (severity danger) di bawah field Master Data Count Limit: "Value must be between 1,000 and 100,000"
17. Verifikasi `[Save]` disabled

### TC-AC-LCS-275: Field Master Data Count Limit diisi 100001 (di atas maksimum) menampilkan error rentang

18. Pilih seluruh isi field Master Data Count Limit lalu ketik `100001`
19. Klik area kosong di luar field (blur)
20. Verifikasi inline error text (severity danger) di bawah field Master Data Count Limit: "Value must be between 1,000 and 100,000"
21. Verifikasi `[Save]` disabled

### TC-AC-LCS-276: Save Master Data Count Limit pada nilai maksimum

22. Ubah Master Data Count Limit menjadi `100000`
23. Verifikasi tidak ada pesan error rentang pada Master Data Count Limit saat nilai `100000` diisi
24. Klik `[Save]`
25. Verifikasi toast sukses "Success, system limits settings have been saved."
26. Verifikasi `[Save]` disabled setelah tab refresh
27. Muat ulang halaman dengan F5, lalu buka kembali tab System Limits
28. Verifikasi Master Data Count Limit bernilai `100000` (nilai tersimpan)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (membuka tab; hook `beforeEach` suite membuka tab Trial Settings).
- Urutan mengikuti nomor TC; Save sukses pada nilai maksimum berada paling akhir sesudah semua validasi yang diblokir (S-10). Field dibersihkan oleh isi ulang pada TC berikutnya (tiap TC memilih seluruh isi field lebih dulu).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
