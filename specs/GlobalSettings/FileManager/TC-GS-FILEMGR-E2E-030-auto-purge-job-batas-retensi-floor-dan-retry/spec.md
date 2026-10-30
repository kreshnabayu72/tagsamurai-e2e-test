---
id: TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry
title: "Auto-Purge Job: Batas Retensi Inklusif, Floor 48 Jam, Retry, dan Balapan dengan Permanently Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-22
  - TC-GS-FILEMGR-111
  - TC-GS-FILEMGR-112
  - TC-GS-FILEMGR-114
  - TC-GS-FILEMGR-257
coverage:
  web: automated
---

# Auto-Purge Job: Batas Retensi Inklusif, Floor 48 Jam, Retry, dan Balapan dengan Permanently Delete

## Prerequisites

- Mode: FE+BE (kelas harness eksternal: job latar auto-purge sebagai objek uji; pemicu fixture BE).
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`. Akun dan akses yang mengubah Lifecycle Settings (Admin Console) tidak disebut TC, PRD, atau LLD File Manager: disediakan tim FE.
- State global yang diubah (suite serial): durasi retensi Recycle Bin (30 hari awal; 10 hari hanya pada TC-GS-FILEMGR-22 lalu dikembalikan ke 30); jam server dibekukan untuk TC-GS-FILEMGR-112 (batas tepat) lalu dipulihkan; fixture storage tidak terjangkau untuk TC-GS-FILEMGR-114. Hook `after` memulihkan retensi 30 hari, jam server, dan fixture storage walau spec gagal di tengah. Job auto-purge harian dijeda di environment e2e dan hanya berjalan lewat pemicu fixture BE (Q-3). Pemicu job menghapus seluruh baris jatuh tempo di environment (lihat Temuan untuk QA).
- Data Dinamis (seeding fixture BE pada langkah pembuka blok masing-masing, bersuffix per run, di Recycle Bin; Deleted Date relatif terhadap waktu seeding; pemilik adalah user klon milik spec):
  - TC-GS-FILEMGR-22: `expired-avatar-{runId}-030.jpg` (Deleted Date sekarang - 29 hari) dan `grace-photo-{runId}-030.png` (sekarang - 31 hari), dihapus permanen lewat fixture BE di akhir blok.
  - TC-GS-FILEMGR-111: `due-photo-{runId}-030.png` (sekarang - 31 hari, retensi 30 hari).
  - TC-GS-FILEMGR-112: `boundary-on-{runId}-030.jpg` (dihapus tepat 30 hari sebelum waktu job) dan `boundary-before-{runId}-030.jpg` (30 hari dikurangi 1 jam sebelum waktu job); waktu job = jam server yang dibekukan.
  - TC-GS-FILEMGR-114: `retry-photo-{runId}-030.png` (sekarang - 31 hari); fixture BE membuat penghapusan storage gagal pada job pertama.
  - TC-GS-FILEMGR-257: `race-photo-{runId}-030.png` (sekarang - 31 hari).
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): seeding Recycle Bin dengan Deleted Date relatif/absolut; memicu job auto-purge harian dan job reset countdown sampai selesai; membekukan dan memulihkan jam server (jam browser diatur bersama, batas eksak memakai jam absolut, bagian 6 konvensi); fixture storage gagal/pulih; membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di langkah pembuka tiap blok sebelum job dipicu).
- Pemulihan di hook `after`: hapus permanen sisa file seed, pulihkan retensi 30 hari, jam server, dan fixture storage.
- Suite serial (`parallel: false`). Spec menghapus data lewat job: jalankan sesudah spec lain bila runner mengikuti nomor (belum terbukti). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-22: Auto-purge tidak menghapus file dalam floor 48 jam

1. Seed `expired-avatar-{runId}-030.jpg` dan `grace-photo-{runId}-030.png` di Recycle Bin lewat fixture BE
2. Buka Lifecycle Settings, ubah durasi retensi Recycle Bin menjadi 10, lalu klik [Save]
3. Picu job reset countdown lewat fixture BE sampai selesai
4. Picu job auto-purge harian lewat fixture BE sampai selesai
5. Buka Global Settings > File Manager, lalu klik tombol Recycle Bin di toolbar
6. Ketik Search `{runId}-030`, tekan Enter
7. Verifikasi `expired-avatar-{runId}-030.jpg` tetap di Recycle Bin dengan Auto-Purge In `2 days`
8. Verifikasi `grace-photo-{runId}-030.png` tetap di Recycle Bin dengan Auto-Purge In `2 days`
9. Verifikasi jumlah baris Recycle Bin pada hasil Search sama dengan jumlah sebelum job (baseline)
10. Tutup modal Recycle Bin dengan `✕` di header
11. Klik ikon Changelog di toolbar, ketik Search `-{runId}-030`, tekan Enter
12. Verifikasi jumlah entri Permanently Delete untuk `expired-avatar-{runId}-030.jpg` dan `grace-photo-{runId}-030.png` sama dengan baseline (tidak ada entri baru)
13. Tutup modal Changelog dengan `✕` di header
14. Hapus permanen `expired-avatar-{runId}-030.jpg` dan `grace-photo-{runId}-030.png` lewat fixture BE, lalu kembalikan durasi retensi Recycle Bin ke 30 (Lifecycle Settings, [Save]) dan picu job reset countdown sampai selesai

### TC-GS-FILEMGR-111: Auto-purge menghapus file yang batas retensinya tercapai

15. Seed `due-photo-{runId}-030.png` di Recycle Bin lewat fixture BE (Deleted Date sekarang - 31 hari)
16. Picu job auto-purge harian lewat fixture BE sampai selesai
17. Buka Global Settings > File Manager, lalu klik tombol Recycle Bin di toolbar
18. Verifikasi tidak ada toast kepada user
19. Ketik Search `due-photo-{runId}-030`, tekan Enter
20. Verifikasi empty state "No results found" pada Recycle Bin (`due-photo-{runId}-030.png` tidak lagi ada)
21. Tutup modal Recycle Bin dengan `✕` di header
22. Klik ikon Changelog di toolbar, ketik Search `due-photo-{runId}-030`, tekan Enter
23. Verifikasi modal Changelog memuat baris Action `Permanently Delete`, File Name `due-photo-{runId}-030.png`, Modified By `System`
24. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-112: Batas retensi inklusif

25. Bekukan jam server (jam browser diatur bersama) pada waktu T
26. Seed `boundary-on-{runId}-030.jpg` (Deleted Date tepat T - 30 hari) dan `boundary-before-{runId}-030.jpg` (Deleted Date T - 30 hari + 1 jam) di Recycle Bin lewat fixture BE
27. Picu job auto-purge harian lewat fixture BE sampai selesai
28. Pulihkan jam server dan jam browser
29. Buka Global Settings > File Manager, lalu klik tombol Recycle Bin di toolbar
30. Ketik Search `boundary-`, tekan Enter
31. Verifikasi `boundary-before-{runId}-030.jpg` tetap di Recycle Bin dengan Auto-Purge In `1 day`
32. Verifikasi `boundary-on-{runId}-030.jpg` terhapus permanen (tidak ada di Recycle Bin)
33. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-114: Auto-purge gagal di storage diulang pada job berikutnya

34. Seed `retry-photo-{runId}-030.png` di Recycle Bin lewat fixture BE (Deleted Date sekarang - 31 hari)
35. Aktifkan fixture BE penghapusan storage gagal
36. Picu job auto-purge harian lewat fixture BE sampai selesai
37. Klik tombol Recycle Bin di toolbar, lalu ketik Search `retry-photo-{runId}-030`, tekan Enter
38. Verifikasi `retry-photo-{runId}-030.png` tetap di Recycle Bin
39. Tutup modal Recycle Bin dengan `✕` di header
40. Klik ikon Changelog di toolbar, ketik Search `retry-photo-{runId}-030`, tekan Enter
41. Verifikasi jumlah entri Permanently Delete untuk `retry-photo-{runId}-030.png` sama dengan baseline (tidak ada entri log)
42. Tutup modal Changelog dengan `✕` di header
43. Nonaktifkan fixture BE penghapusan storage gagal
44. Picu job auto-purge berikutnya lewat fixture BE sampai selesai
45. Klik tombol Recycle Bin di toolbar, lalu ketik Search `retry-photo-{runId}-030`, tekan Enter
46. Verifikasi empty state "No results found" pada Recycle Bin (`retry-photo-{runId}-030.png` hilang)
47. Tutup modal Recycle Bin dengan `✕` di header
48. Klik ikon Changelog di toolbar, ketik Search `retry-photo-{runId}-030`, tekan Enter
49. Verifikasi jumlah entri Permanently Delete aktor `System` untuk `retry-photo-{runId}-030.png` tepat satu (baseline ditambah satu)
50. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-257: Permanently Delete manual bersamaan dengan auto-purge

51. Seed `race-photo-{runId}-030.png` di Recycle Bin lewat fixture BE (Deleted Date sekarang - 31 hari)
52. Klik tombol Recycle Bin di toolbar, lalu ketik Search `race-photo-{runId}-030`, tekan Enter
53. Klik ikon `⋯` baris `race-photo-{runId}-030.png`, lalu klik `Permanently Delete` (dialog Permanently Delete tetap terbuka)
54. Picu job auto-purge harian lewat fixture BE sampai selesai
55. Klik [Permanently Delete] pada dialog yang masih terbuka
56. Verifikasi toast info: "This file is no longer available."
57. Verifikasi Recycle Bin di-refresh
58. Verifikasi `race-photo-{runId}-030.png` tidak ada di Recycle Bin
59. Tutup modal Recycle Bin dengan `✕` di header
60. Klik ikon Changelog di toolbar, ketik Search `race-photo-{runId}-030`, tekan Enter
61. Verifikasi jumlah entri Permanently Delete untuk `race-photo-{runId}-030.png` tepat satu (baseline ditambah satu)
62. Verifikasi entri Permanently Delete tersebut bernilai Modified By `System`
63. Tutup modal Changelog dengan `✕` di header

## Notes

- Mode: FE+BE. Kelas d (harness eksternal: job latar auto-purge), bagian 3 prinsip 13d; pemicu job, jam, dan storage adalah objek uji bersama. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (63 langkah nominal, tanpa blok yang diulang). Alasan pertahanan: seluruh blok satu kelas dan satu harness (pemicu job auto-purge lewat fixture BE), tiap blok men-seed dan membersihkan filenya sendiri sehingga tidak bergantung pada blok lain; kegagalan satu blok (mis. job tidak selesai) tidak menghalangi makna blok berikutnya selama pemicu fixture tersedia.
- Urutan TC pada spec: 22, 111, 112, 114, 257 (mengikuti TC sumber). TC-GS-FILEMGR-22 di awal karena mengubah retensi dan mengembalikannya (langkah 14) sebelum blok berikutnya yang membutuhkan retensi 30 hari.
- Butir P-1: TC-GS-FILEMGR-22 mensyaratkan retensi yang baru diubah dan job reset countdown selesai (state berat dibangun di langkah 2 dan 3); asersi absence entri log Permanently Delete (Expected c) tetap di spec ini dengan baseline jumlah entri (keputusan D-1 pilihan B), bukan di spec absence.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 15, 26, 34, 51 (seeding fixture), 5, 17, 29, 37, 45, 52 (membuka File Manager dan Recycle Bin), 6, 11, 19, 22, 30, 40, 48, 60 (Search), 10, 13, 21, 24, 33, 39, 42, 47, 50, 59, 63 (menutup modal), 14 (cleanup blok TC-GS-FILEMGR-22 dan pemulihan retensi), 25 dan 28 (membekukan dan memulihkan jam), 35 dan 43 (fixture storage).
- Asersi tambahan di luar Expected TC (S-03): langkah 20 dan 46 (empty state "No results found" sebagai anchor absence), langkah 31 (pembanding sebelum absence `boundary-on`), langkah 62.
- Temuan untuk QA:
  - Q-3: `due-photo.png` R04 (Deleted Date sekarang - 31 hari) "tetap tampil sampai job auto-purge berikutnya"; tanpa jeda job otomatis, TC-GS-FILEMGR-22/111/112 menjadi flaky. Spec meminta job dijeda dan dipicu hanya lewat fixture BE.
  - Pemicu job auto-purge menghapus seluruh baris jatuh tempo di environment, termasuk baris Pre-setup R04 `due-photo.png` (Tabel A3) yang jatuh tempo. Spec lain (mis. `TC-GS-FILEMGR-E2E-022`, `029`) yang membaca Tabel A3 harus men-seed ulang Tabel A3 di hook `before`; TC tidak menjelaskan cara memicu job hanya untuk file tertentu.
  - Q-4: seeding Recycle Bin, pemicu job, jam beku, dan fixture storage gagal tidak punya mekanisme di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" tanpa endpoint karangan (S-13).
  - TC-GS-FILEMGR-112 tidak menyebut cara menetapkan "tepat 30 hari sebelum waktu job" dan "30 hari dikurangi 1 jam"; spec memakai jam server yang dibekukan pada waktu T dan seeding absolut (bagian 6 konvensi).
  - TC-GS-FILEMGR-257 Expected c ("tepat satu entri log Permanently Delete, aktor System") dan langkah 2 (job dipicu saat dialog terbuka): jam pemicu job relatif terhadap klik tidak ditetapkan; spec memicu job sampai selesai lalu klik [Permanently Delete].
  - Q-5/Q-7: TC menargetkan baris Pre-setup R03 `expired-avatar.jpg` dan R04 `due-photo.png` yang dihapus job; spec memakai file bersuffix.
  - Post Condition semua TC bernilai `-`.
