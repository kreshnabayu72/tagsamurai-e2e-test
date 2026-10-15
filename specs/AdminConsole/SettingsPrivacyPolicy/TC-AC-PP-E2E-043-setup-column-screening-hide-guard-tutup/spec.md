---
id: TC-AC-PP-E2E-043-setup-column-screening-hide-guard-tutup
title: "Setup Column dan Column Visibility: Screening, Hide, Guard, dan Tutup Tanpa Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-128
  - TC-AC-PP-129
  - TC-AC-PP-130
  - TC-AC-PP-134
  - TC-AC-PP-136
coverage:
  web: automated
---

# Setup Column dan Column Visibility: Screening, Hide, Guard, dan Tutup Tanpa Save

## Prerequisites

- Mode: mock. Seluruh API di-mock sebagai integration test tim FE; kebutuhan mock: (a) respons endpoint daftar riwayat versi dengan Riwayat A (Version 3 Active, John Doe, 10 Aug 2026; Version 2, John Doe, 02 Jul 2026; Version 1, Jane Smith, 15 Jan 2026); (b) payload sesi dan izin Total Control (capability "Manage privacy policy" Read dan Update) sehingga halaman dan Table Tools tampil. Tidak ada endpoint lain yang dipaksa. Sesi login disediakan harness pada run mock.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`) sebagai sesi default suite; pada run non-mock hook `before` login nyata sebagai akun ini dengan `AC_TC_PASSWORD` (nama env perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; baru `AC_TC_PASSWORD` yang terdaftar), pada run mock sesi disediakan harness; hook `after` mengembalikan sesi ke akun default suite.
- Konfigurasi kolom tersimpan di cache browser (bukan di server); hook `before` mengosongkan cache konfigurasi kolom sehingga spec mulai dari konfigurasi default (Version, Published At, Published By, semua visible), dan hook `after` memulihkannya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Suite berjalan serial (`parallel: false`) karena konfigurasi kolom tersimpan di cache browser yang sama dengan spec lain dalam suite.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-128: Screening overlay Column Visibility dari header kolom Actions

1. Buka Settings > Privacy Policy lewat sidebar
2. Hover header kolom Actions `(⋯)`
3. Verifikasi tooltip "Column Visibility" tampil
4. Klik header `(⋯)`
5. Verifikasi Overlay Column Visibility terbuka
6. Verifikasi daftar berurutan `Version`, `Published At`, `Published By`
7. Verifikasi masing-masing item punya checkbox tercentang
8. Verifikasi masing-masing item punya checkbox enabled
9. Verifikasi masing-masing item punya drag handle
10. Verifikasi item "Setup Column..." ada di bagian bawah overlay
11. Verifikasi kolom Checkbox dan Actions tidak ada pada daftar
12. Tutup overlay Column Visibility

### TC-AC-PP-130: Screening popup Setup Column dan Live Preview

13. Klik header `(⋯)`
14. Klik "Setup Column..."
15. Verifikasi popup Setup Column terbuka
16. Verifikasi Title popup "Setup Column"
17. Verifikasi Deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
18. Verifikasi tombol close `[✕]` ada
19. Verifikasi daftar `Version`, `Published At`, `Published By` masing-masing tercentang
20. Verifikasi daftar `Version`, `Published At`, `Published By` masing-masing Hideable dan enabled
21. Verifikasi masing-masing item punya drag handle
22. Verifikasi masing-masing item punya icon Pin
23. Verifikasi Live Preview menampilkan urutan header kolom dan data sel yang sama dengan tabel
24. Verifikasi footer menampilkan `[Reset to Default]` (Text, primary)
25. Verifikasi footer menampilkan `[Save]` (filled, success)
26. Verifikasi tidak ada tombol `[Cancel]`

### TC-AC-PP-134: Guard satu kolom tersisa: checkbox kolom terakhir yang visible disabled dengan tooltip

27. Pada popup Setup Column, uncheck `Version`
28. Uncheck `Published At`
29. Verifikasi checkbox `Published By` disabled
30. Hover checkbox `Published By`
31. Verifikasi tooltip "At least one column must remain visible."
32. Check kembali `Published At`
33. Verifikasi checkbox `Published By` kembali enabled
34. Klik `[✕]` pada popup untuk menutup tanpa Save

### TC-AC-PP-136: Menutup popup Setup Column lewat [✕] atau Esc tanpa Save membuang perubahan

35. Klik header `(⋯)` lalu klik "Setup Column..."
36. Uncheck `Published At`
37. Klik `[✕]`
38. Verifikasi popup tertutup tanpa dialog
39. Verifikasi tabel menampilkan ketiga kolom `Version`, `Published At`, `Published By` (konfigurasi tersimpan terakhir)
40. Klik header `(⋯)` lalu klik "Setup Column..."
41. Uncheck `Published By`
42. Tekan Esc
43. Verifikasi popup tertutup tanpa dialog
44. Verifikasi tabel menampilkan ketiga kolom `Version`, `Published At`, `Published By`
45. Muat ulang halaman dengan F5
46. Verifikasi tabel masih menampilkan ketiga kolom (konfigurasi di cache tidak berubah)

### TC-AC-PP-129: Perubahan di overlay Column Visibility langsung diterapkan ke tabel tanpa tombol Save

47. Klik header `(⋯)`
48. Uncheck `Published At` pada overlay Column Visibility
49. Verifikasi kolom `Published At` hilang dari tabel seketika
50. Tarik `Published By` ke posisi paling atas daftar di overlay
51. Verifikasi urutan kolom tabel menjadi `Published By`, `Version`
52. Verifikasi tidak ada tombol Save pada overlay
53. Muat ulang halaman dengan F5
54. Verifikasi konfigurasi tetap berlaku setelah F5 (kolom `Published By`, `Version`; `Published At` tersembunyi)
55. Klik header `(⋯)` lalu klik "Setup Column...", klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: mock. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec ini 128, 130, 134, 136, 129 (TC sumber 128 sampai 130, 134, 136). TC-129 dipindah ke akhir karena menyimpan perubahan konfigurasi kolom yang mengubah precondition TC lain (screening dan guard memerlukan konfigurasi default), sesuai prinsip aksi yang mengubah state di akhir (S-05, S-10).
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 12 (tutup overlay), langkah 34 (tutup popup tanpa Save agar konfigurasi tetap default), langkah 55 (kembalikan konfigurasi ke default lewat `[Reset to Default]` dan `[Save]`; hook `after` menjadi cadangan).
- Langkah 46 mengamati "konfigurasi di cache tidak berubah" (Expected b TC-136) lewat muat ulang halaman karena cache browser tidak dapat dibaca langsung dari UI; ini asersi tambahan yang dicatat sesuai S-03.
- Spec tidak membuat data dan tidak mengubah Pre-setup; konfigurasi kolom hanya di cache browser.
- Spec bermode mock: login nyata di hook `before` hanya untuk run non-mock; pada run mock sesi dan izin Total Control disediakan harness (lihat Prerequisites).
- Temuan untuk QA: tidak ada.
- Panjang spec (55 langkah) melewati perkiraan 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: TC dalam spec satu topik, satu akun, dan satu dataset; tiap bagian dipisah subjudul TC dan tetap bermakna walau bagian sebelumnya gagal karena state dikembalikan di langkah penghubung (batas ukuran konvensi bagian 3 bukan jumlah langkah).
