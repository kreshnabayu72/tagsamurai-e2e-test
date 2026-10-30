---
id: TC-GS-FILEMGR-E2E-018-selection-limit-tabel-utama-dan-recycle-bin
title: "Selection Limit: Checkbox Diblokir, Select All di-cap, dan Kosongkan Recycle Bin Beberapa Putaran"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-75
  - TC-GS-FILEMGR-76
  - TC-GS-FILEMGR-104
coverage:
  web: automated
---

# Selection Limit: Checkbox Diblokir, Select All di-cap, dan Kosongkan Recycle Bin Beberapa Putaran

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- State global yang diubah: Selection Limit di Lifecycle Settings > System Limits diturunkan ke nilai terendah yang diizinkan (disebut `[Limit]` pada langkah; nilainya dibaca dari Lifecycle Settings; rentang yang diizinkan PRD Lifecycle Settings adalah 100 sampai 5.000 sehingga nilai terendah adalah 100, tidak ada angka di TC). Akun dan akses yang mengubah Lifecycle Settings tidak disebut TC, PRD, atau LLD File Manager: disediakan tim FE. Hook `before` mencatat nilai awal lalu menyetel `[Limit]`; hook `after` memulihkan nilai awal walau spec gagal.
- Kelas harness volume (kelas e): kebutuhan data bergantung pada `[Limit]`. Seeding fixture BE (disediakan tim FE/BE, bersuffix per run) di hook `before`:
  - Tabel utama: file aktif `limit-photo-NN-{runId}-018.jpg` (JPG, NN berurutan) sedemikian sehingga total baris tabel utama sama dengan `[Limit]` + 1 (menghitung 33 baris Tabel A2 yang ada; bila `[Limit]` + 1 kurang dari atau sama dengan 33, tidak ada seeding tambahan). `[N]` pada langkah adalah total baris tabel utama hasil seeding ini.
  - Recycle Bin: hook `before` mengosongkan Recycle Bin environment lewat fixture BE, lalu men-seed tepat `[Limit]` + 5 file `limit-bin-NN-{runId}-018.jpg`. Setelah TC-GS-FILEMGR-104 Recycle Bin environment kosong; spec lain men-seed ulang kebutuhan Recycle Bin-nya di hook `before` masing-masing.
- Kemampuan teknis (disediakan tim FE/BE): membaca dan mengubah Selection Limit; seeding file aktif dan Recycle Bin dalam jumlah bergantung `[Limit]`; mengosongkan Recycle Bin; jeda nyata sampai 6 detik untuk membuktikan toast error tidak hilang otomatis.
- Pemulihan di hook `after`: pulihkan Selection Limit awal; hapus permanen seluruh file seed `limit-photo-*` dan `limit-bin-*` yang masih ada.
- Suite serial (`parallel: false`). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-75: Seleksi manual melewati Selection Limit

1. Centang baris tabel utama satu per satu (lintas halaman bila perlu) sampai bar menampilkan `[Limit] Files selected`
2. Coba centang baris berikutnya
3. Verifikasi checkbox baris berikutnya disabled
4. Arahkan kursor ke checkbox yang disabled
5. Verifikasi tooltip checkbox disabled: "You've reached the maximum selection of [Limit] rows."
6. Verifikasi baris yang sudah tercentang tetap tercentang
7. Verifikasi Bulk Action Bar tetap aktif

### TC-GS-FILEMGR-76: Select All melebihi Selection Limit di-cap

8. Klik ikon `×` pada bar untuk mengosongkan seleksi
9. Klik tombol `Select All ([N] records)`
10. Verifikasi seleksi di-cap ke `[Limit]` baris pertama (bar menampilkan `[Limit] Files selected`)
11. Verifikasi toast error: "Error, only the first [Limit] of [N] rows were selected. Narrow your filter to include the rest."
12. Amati toast error selama 6 detik tanpa tindakan
13. Verifikasi toast error tidak hilang otomatis
14. Verifikasi Bulk Action Bar tetap tampil
15. Dismiss toast error, lalu klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-104: Kosongkan Recycle Bin lewat beberapa putaran

16. Klik tombol Recycle Bin di toolbar
17. Klik tombol `Select All ([N] records)` dengan `[N]` = `[Limit]` + 5
18. Verifikasi seleksi di-cap ke `[Limit]` baris (bar menampilkan `[Limit] Files selected`)
19. Verifikasi toast error cap: "Error, only the first [Limit] of [N] rows were selected. Narrow your filter to include the rest."
20. Dismiss toast error
21. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
22. Verifikasi toast sukses: "Success, file has been permanently deleted."
23. Verifikasi tombol `Select All (5 records)` tampil (tersisa 5 file; `[Limit]` file terhapus)
24. Klik tombol `Select All (5 records)`
25. Verifikasi bar menampilkan `5 Files selected` (sisa 5 file terseleksi)
26. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
27. Verifikasi toast sukses: "Success, file has been permanently deleted."
28. Verifikasi Recycle Bin menampilkan empty state `Recycle bin is empty`

## Notes

- Mode: FE+BE. Kelas e (volume/limit); satu-satunya state global yang diubah adalah Selection Limit dan dipulihkan di hook `after`. Subjudul `###` memetakan langkah ke id TC granular.
- TC-GS-FILEMGR-104 berada di akhir karena menghabiskan seluruh Recycle Bin (prinsip 5); TC-GS-FILEMGR-75 dan 76 tidak mengubah data.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 8 dan 15 (mengosongkan seleksi), 12 (jeda nyata untuk mengamati toast error), 15 dan 20 (dismiss toast error persisten sebelum diasersi lagi, S-09), 16 (membuka modal Recycle Bin), 17 (`[N]` = `[Limit]` + 5 hasil seeding, butir 10 bagian 8b).
- Asersi tambahan di luar Expected TC (S-03): langkah 22 dan 27 (toast sukses sebagai anchor absence untuk sisa file; TC hanya menyebut hasil akhir) dan langkah 23 (bukti `[Limit]` file terhapus pada putaran pertama lewat jumlah tersisa).
- Temuan untuk QA:
  - Q-2: "nilai terendah yang diizinkan" Selection Limit tidak diberi angka di TC dan dimiliki PRD Lifecycle Settings. TC-GS-FILEMGR-75 butuh baris tersedia = `[Limit]` + 1 dan TC-GS-FILEMGR-104 butuh `[Limit]` + 5; nilai terendah yang diizinkan PRD Lifecycle Settings adalah 100 (rentang 100 sampai 5.000), sehingga `[Limit]` = 100 lebih besar dari 32 dan dataset Pre-setup Tabel A2 (33 baris) tidak cukup; seeding tambahan (68 file aktif untuk TC-GS-FILEMGR-75, 100 + 5 file Recycle Bin untuk TC-GS-FILEMGR-104) disediakan tim FE/BE.
  - Q-4: TC-GS-FILEMGR-75/76/104 mensyaratkan seeding "lewat seed Pre-setup" tanpa mekanisme; ditulis "disediakan tim FE/BE" tanpa endpoint.
  - TC-GS-FILEMGR-104 mengharuskan Recycle Bin berisi tepat `[Limit]` + 5 file; Tabel A3 (16 baris) membuat hitungan itu salah sehingga hook `before` mengosongkan Recycle Bin terlebih dahulu. TC tidak menyatakan hal ini.
  - TC-GS-FILEMGR-104 Expected a menyebut "toast error cap" tanpa teks; spec memakai teks TC-GS-FILEMGR-76 (pola yang sama).
  - Post Condition semua TC bernilai `-`.
