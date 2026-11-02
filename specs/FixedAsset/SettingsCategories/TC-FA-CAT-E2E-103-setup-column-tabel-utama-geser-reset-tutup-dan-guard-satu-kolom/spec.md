---
id: TC-FA-CAT-E2E-103-setup-column-tabel-utama-geser-reset-tutup-dan-guard-satu-kolom
title: "Setup Column Tabel Utama: Geser Urutan, Reset to Default, Tutup Tanpa Save, Guard Satu Kolom, dan Independensi Antar Tabel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-356
  - TC-FA-CAT-359
  - TC-FA-CAT-360
  - TC-FA-CAT-361
  - TC-FA-CAT-362
coverage:
  web: automated
---

# Setup Column Tabel Utama: Geser Urutan, Reset to Default, Tutup Tanpa Save, Guard Satu Kolom, dan Independensi Antar Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` (Total Asset 0 sampai 29). Popup Detail langkah 37 dan 47 dibuka pada baris ber-Total Asset 29. Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Kolom untuk langkah berulang (langkah 28 sampai 29):

  | Kolom |
  |---|
  | `Category` |
  | `Code` |
  | `Total Asset` |
  | `Modified By` |
  | `Last Updated` |

- State yang diubah spec: konfigurasi kolom tabel utama (disimpan lewat `[Save]`). Hook `after` memulihkannya dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-359: Reset to Default mengembalikan konfigurasi bawaan

1. Klik header Actions (⋯) > `Setup Column...`
2. Hilangkan centang kolom `Code`
3. Geser kolom `Last Updated` ke posisi pertama
4. Klik `[Reset to Default]`
5. Verifikasi preview kembali ke lima kolom default berurutan Category, Code, Total Asset, Modified By, Last Updated
6. Klik `[Save]`
7. Verifikasi tabel memakai lima kolom default berurutan Category, Code, Total Asset, Modified By, Last Updated
8. Tekan F5
9. Verifikasi tabel tetap memakai lima kolom default berurutan setelah F5

### TC-FA-CAT-360: Menutup popup tanpa Save membuang perubahan

10. Klik header Actions (⋯) > `Setup Column...`
11. Hilangkan centang kolom `Code`
12. Klik icon Close (✕)
13. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Code` masih tampil dan urutan default)
14. Klik header Actions (⋯) > `Setup Column...`
15. Geser kolom `Last Updated` ke posisi pertama
16. Tekan `Esc`
17. Verifikasi tabel memakai konfigurasi tersimpan terakhir (urutan default)

### TC-FA-CAT-361: Guard satu kolom tersisa

18. Klik header Actions (⋯) > `Setup Column...`
19. Hilangkan centang kolom `Category`
20. Hilangkan centang kolom `Code`
21. Hilangkan centang kolom `Total Asset`
22. Hilangkan centang kolom `Modified By`
23. Hover checkbox kolom `Last Updated` yang tersisa
24. Verifikasi checkbox kolom `Last Updated` disabled
25. Verifikasi tooltip `At least one column must remain visible.`
26. Klik icon Close (✕)

### TC-FA-CAT-356: Geser urutan kolom dan persist

27. Klik header Actions (⋯) > `Setup Column...`
28. Geser kolom `Category` ke posisi pertama
29. Verifikasi preview menempatkan `Category` sebagai kolom data pertama
30. Ulangi langkah 28 sampai 29 untuk setiap kolom lain pada tabel Prerequisites (`Code`, `Total Asset`, `Modified By`, `Last Updated`)
31. Klik `[Save]`
32. Tekan F5
33. Verifikasi urutan kolom data menjadi Last Updated, Modified By, Total Asset, Code, Category dan bertahan setelah F5

### TC-FA-CAT-362: Konfigurasi kolom tabel utama tidak memengaruhi tabel lain

34. Klik icon Changelog di Table Tools
35. Catat kolom Modal Changelog (baseline)
36. Tutup Modal Changelog dengan icon Close (✕)
37. Klik elipsis (⋯) pada baris ber-Total Asset 29 > `Detail`
38. Catat kolom tabel Assets pada Popup Detail (baseline)
39. Tutup Popup Detail
40. Klik header Actions (⋯) > `Setup Column...`
41. Hilangkan centang kolom `Code`
42. Klik `[Save]`
43. Verifikasi kolom `Code` tidak ada di tabel utama
44. Klik icon Changelog di Table Tools
45. Verifikasi kolom Modal Changelog sama dengan baseline
46. Tutup Modal Changelog dengan icon Close (✕)
47. Klik elipsis (⋯) pada baris ber-Total Asset 29 > `Detail`
48. Verifikasi kolom tabel Assets sama dengan baseline
49. Tutup Popup Detail

## Notes

- Langkah berulang: langkah 28 sampai 29 diulang untuk lima kolom pada tabel Prerequisites (idiom "Untuk setiap baris tabel", butir 8b.7); `Verifikasi` tetap satu per klausa. Hitungan dengan ekspansi sekitar 58 langkah. Alasan: seluruh TC satu halaman, satu dataset CatMany, dan satu kelas harness (fungsional Setup Column), dan tiap blok berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-359 dijalankan lebih dulu agar TC-356 dan TC-362 berangkat dari konfigurasi default tersimpan (S-09/S-10); TC-359 sendiri mengubah konfigurasi lalu mengembalikannya lewat `[Reset to Default]` dan `[Save]`.
- Langkah penghubung (S-03): langkah 12, 26, 36, 39, 46, 49 (menutup popup dan modal); langkah 35 dan 38 (mencatat baseline kolom untuk asersi langkah 45 dan 48).
- Temuan untuk QA:
  - TC-362 tidak menyebut daftar kolom tabel Assets dan Modal Changelog sebagai baseline; spec mencatat kolom keduanya sebelum perubahan (langkah 35 dan 38).
  - TC-359 tidak menyebut kondisi konfigurasi tersimpan sebelum Reset; spec memulai dari konfigurasi default sehingga persistensi Reset to Default hanya teruji sebagai "tetap default setelah F5".
  - Baris ber-Total Asset 29 bergantung pada mapping nama dan angka seed #24 yang tidak tertulis eksplisit di tabel Data Uji.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
- Spec melewati 35 langkah (49 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
