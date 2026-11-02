---
id: TC-AC-SU-E2E-175-format-tanggal-dan-waktu-general-settings
title: "Format Tanggal dan Waktu General Settings Berlaku di User List, Popup Changelog, dan Tab Detail User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-7
  - TC-AC-SU-605
  - TC-AC-SU-606
  - TC-AC-SU-607
coverage:
  web: automated
---

# Format Tanggal dan Waktu General Settings Berlaku di User List, Popup Changelog, dan Tab Detail User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- State global yang diubah spec: General Settings (Date Format, Time Format, Timezone). Nilai awal dicatat di hook `before` lewat Fixture BE dan dipulihkan di hook `after`. Nilai yang diatur spec: Date Format `DD/MM/YY`, Time Format 24-hour (lalu 12-hour), Timezone `Asia/Jakarta`. Suite berjalan serial.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. User milik spec: U1 `Mike Tan {runId}-175`, email `miketan+{runId}-175@qwertysystem.net`, Activated, dengan entri Changelog, System Log, dan User Log, serta satu entri Responsibilities (Approval dengan Submission Date) milik U1 (seeding dan kemampuan membaca disediakan tim FE/BE; Approval Pre-setup tidak diubah).
- Kemampuan teknis: Fixture BE (seeding user, entri log, dan Approval; membaca dan memulihkan General Settings). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### Format 24-hour (TC-AC-SU-7, TC-AC-SU-605, TC-AC-SU-606, TC-AC-SU-607 butir a)
1. Buka Global Settings > General Settings, lalu atur Date Format `DD/MM/YY`, Time Format 24-hour, dan Timezone `Asia/Jakarta`, lalu simpan
2. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Mike Tan {runId}-175`, tekan Enter
3. Verifikasi nilai kolom Last Updated baris U1 mengikuti pola `DD/MM/YY HH:mm` (bukan format hardcode)
4. Klik icon Filter di toolbar sehingga Filter Panel terbuka, lalu pilih rentang tanggal pada field Last Updated
5. Verifikasi nilai kolom Last Updated pada tabel mengikuti `DD/MM/YY HH:mm` zona `Asia/Jakarta`
6. Verifikasi teks input date range filter Last Updated mengikuti `DD/MM/YY HH:mm` zona `Asia/Jakarta`
7. Tutup Filter Panel tanpa menerapkan filter, klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka, lalu buka Filter dan pilih rentang Date
8. Verifikasi nilai kolom Date pada Popup Changelog: User mengikuti `DD/MM/YY HH:mm` zona `Asia/Jakarta`
9. Verifikasi teks input date range filter Date mengikuti `DD/MM/YY HH:mm` zona `Asia/Jakarta`
10. Tutup popup, buka Detail U1 lewat Search nama, lalu klik Tab Changelog
11. Verifikasi nilai kolom Date Tab Changelog mengikuti `DD/MM/YY HH:mm` zona `Asia/Jakarta`
12. Klik Tab System Log
13. Verifikasi nilai kolom Date Tab System Log mengikuti `DD/MM/YY HH:mm` zona `Asia/Jakarta`
14. Klik Tab User Log
15. Verifikasi nilai kolom Date Tab User Log mengikuti `DD/MM/YY HH:mm` zona `Asia/Jakarta`
16. Klik Tab Responsibilities
17. Verifikasi nilai kolom Submission Date Tab Responsibilities mengikuti `DD/MM/YY HH:mm` zona `Asia/Jakarta`
### Format 12-hour (TC-AC-SU-605, TC-AC-SU-606, TC-AC-SU-607 butir b)
18. Buka Global Settings > General Settings, ubah Time Format ke 12-hour, lalu simpan
19. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Mike Tan {runId}-175`, tekan Enter
20. Verifikasi nilai kolom Last Updated baris U1 mengikuti pola `hh:mm a`
21. Klik icon Filter di toolbar sehingga Filter Panel terbuka, lalu pilih rentang tanggal pada field Last Updated
22. Verifikasi teks input date range filter Last Updated mengikuti pola `hh:mm a`
23. Tutup Filter Panel tanpa menerapkan filter, klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka, lalu buka Filter dan pilih rentang Date
24. Verifikasi nilai kolom Date Popup Changelog: User dan teks input date range filter Date mengikuti pola `hh:mm a`
25. Tutup popup, buka Detail U1 lewat Search nama, lalu klik Tab Changelog
26. Verifikasi nilai kolom Date Tab Changelog mengikuti pola `hh:mm a`
27. Klik Tab System Log
28. Verifikasi nilai kolom Date Tab System Log mengikuti pola `hh:mm a`
29. Klik Tab User Log
30. Verifikasi nilai kolom Date Tab User Log mengikuti pola `hh:mm a`
31. Klik Tab Responsibilities
32. Verifikasi nilai kolom Submission Date Tab Responsibilities mengikuti pola `hh:mm a`

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pengaturan General Settings (langkah 1 dan langkah awal fase 12-hour), Search nama target dan pembukaan Detail (langkah 2 dan langkah serupa, R-16), pemilihan rentang pada Filter, membuka dan menutup panel, popup, dan tab.
- Urutan: seluruh asersi format 24-hour (TC-7, TC-605 butir a, TC-606 butir a, TC-607 butir a) dikumpulkan lebih dulu, lalu satu perubahan Time Format ke 12-hour dan seluruh asersi butir b (TC-605, TC-606, TC-607) agar General Settings hanya diubah dua kali. Urutan ini mengubah urutan nomor TC (S-10). Spec ini mengubah state global dan dipulihkan di hook `after` (R-08).
- Dua fase memuat asersi serupa pada permukaan yang sama; 32 langkah dipertahankan karena pengulangan bermakna dua keadaan format (24-hour dan 12-hour) yang masing-masing mengamati keempat permukaan, dan kegagalan satu permukaan tidak membuat permukaan lain kehilangan makna.
- Temuan untuk QA:
  - TC-605 sampai TC-607 butir b menyebut "nilai berubah ke `hh:mm a`" tanpa menyebut bagian tanggal; spec mengasersi pola waktu `hh:mm a` setelah Time Format 12-hour, sedangkan bagian tanggal mengikuti `DD/MM/YY` seperti fase pertama.
  - TC-605 menyebut "teks input date range filter" tanpa menyebut contoh nilai; spec mengasersi pola format.
  - TC-607 menyebut kolom "Date/Submission Date tiap tab"; User Log dan Responsibilities tidak disebut kolom persisnya selain Submission Date untuk Responsibilities, sehingga kolom Date dipakai untuk User Log.
  - TC-607 membutuhkan data log dan Approval pada user target tanpa Dependensi; spec men-seed lewat Fixture BE (kemampuan disediakan tim FE/BE).
  - TC memakai nama literal `Mike Tan`; spec memakai nama bersuffix (S-12).
