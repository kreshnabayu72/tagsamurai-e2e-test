---
id: TC-AC-PP-E2E-007-resilience-baca-tabel-dan-export
title: "Resilience Baca Tabel Version History: Loading, Error Load, Try Again, dan Kegagalan Download"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-07
  - TC-AC-PP-08
  - TC-AC-PP-09
  - TC-AC-PP-141
coverage:
  web: automated
---

# Resilience Baca Tabel Version History: Loading, Error Load, Try Again, dan Kegagalan Download

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; sebagian respons dipaksa lewat `Spectra.intercept()` dan dataset Riwayat A dari backend nyata diasersi).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Dataset Riwayat A (Version 3 Active, Version 2, Version 1). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan dataset ke Riwayat A. Spec tidak membuat data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`):
  - TC-AC-PP-07: menahan respons daftar riwayat versi selama 5 detik.
  - TC-AC-PP-08 dan TC-AC-PP-09: respons daftar riwayat versi dipaksa server error 500, lalu dipulihkan.
  - TC-AC-PP-141: respons Download (export) dipaksa 422.
  Semua intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Tunggu waktu nyata: 10 detik pada TC-AC-PP-141 untuk memastikan toast error persisten tetap tampil (jeda pendek, bagian 6 konvensi); 5 detik pada TC-AC-PP-07 adalah penahanan respons lewat intercept.
- Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-PP-07: Loading state tabel saat riwayat versi sedang diambil

1. Tahan respons daftar riwayat versi selama 5 detik (delay network)
2. Klik menu Settings > Privacy Policy di sidebar
3. Amati body tabel selama 5 detik
4. Verifikasi Loading component tampil di body tabel
5. Verifikasi empty state tidak tampil
6. Verifikasi error state tidak tampil
7. Lepaskan respons
8. Verifikasi loading hilang
9. Verifikasi 3 baris Riwayat A tampil

### TC-AC-PP-08: Error load riwayat versi menampilkan error state, bukan empty state

10. Atur respons daftar riwayat versi menjadi server error 500
11. Klik menu Settings > Privacy Policy di sidebar
12. Amati body tabel
13. Verifikasi body tabel menampilkan "Unable to load this data."
14. Verifikasi body tabel menampilkan button [Try Again]
15. Verifikasi empty state "No Privacy Policy has been published yet." tidak tampil
16. Verifikasi button [Create Privacy Policy] tidak tampil
17. Lepas intercept respons 500

### TC-AC-PP-09: Klik [Try Again] setelah server pulih memuat ulang tabel Version History

18. Atur respons daftar riwayat versi menjadi 500, lalu klik menu Settings > Privacy Policy
19. Verifikasi error state "Unable to load this data." tampil
20. Pulihkan respons daftar riwayat versi menjadi normal (lepas intercept)
21. Klik [Try Again]
22. Verifikasi Loading tampil sesaat
23. Verifikasi 3 baris Riwayat A tampil
24. Verifikasi badge `Active` ada pada `Version 3`
25. Verifikasi error state "Unable to load this data." tidak tampil lagi

### TC-AC-PP-141: Download gagal menampilkan toast error persisten tanpa ekstensi pada pesan

26. Atur respons Download menjadi 422 melalui intercept
27. Klik icon Download
28. Pilih "Download as CSV"
29. Amati toast; tunggu 10 detik
30. Verifikasi muncul toast error: "Error, failed to download Privacy-Policy-Version-History."
31. Verifikasi toast tetap tampil setelah 10 detik sampai di-dismiss manual
32. Verifikasi tidak ada file terunduh
33. Lepas intercept respons Download
34. Dismiss toast secara manual

## Notes

- Mode: FE+BE (kelas b, fault injection). Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 3 (amati selama 5 detik), 7 (melepas respons yang ditahan adalah bagian TC-AC-PP-07), langkah 17, 20, 33 (lepas intercept agar state tidak bocor ke TC berikutnya), langkah 29 (amati toast dan tunggu nyata 10 detik, dicatat di Prerequisites), langkah 34 (dismiss toast).
- Verifikasi langkah 19 (error state tampil) diturunkan dari tanda "→" di kolom Langkah Uji TC-AC-PP-09 langkah 1, bukan dari kolom Expected Result; ditambahkan sebagai penanda state sebelum memulihkan respons (S-03).
- Penyimpangan urutan: TC sumber mengurutkan 07, 08, 09 lalu TC-AC-PP-141 berada di bagian Download; digabung di sini karena sama-sama kelas b pada tabel utama dan dataset Riwayat A.
- Temuan untuk QA:
  - TC-AC-PP-09 Expected a menyebut "Loading tampil sesaat" tanpa penahanan respons; asersi loading sesaat tidak dapat dibuat deterministik tanpa delay, sehingga spec mengikuti TC dan hasilnya bergantung pada kecepatan respons (kurang precondition).
  - TC-AC-PP-141 menyebut respons Download 422 dengan pesan memakai nama file tanpa ekstensi; pemetaan status 422 → pesan berasal dari PRD V-03/T-03 dan tidak ditulis ulang di sini.
  - TC-AC-PP-08 Data Uji hanya menyebut "Respons daftar: 500" tanpa menyebut endpoint spesifik; spec memakai istilah generik "respons daftar riwayat versi" (S-13).
