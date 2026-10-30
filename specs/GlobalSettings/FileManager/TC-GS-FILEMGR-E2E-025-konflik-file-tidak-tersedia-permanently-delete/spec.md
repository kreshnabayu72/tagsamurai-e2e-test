---
id: TC-GS-FILEMGR-E2E-025-konflik-file-tidak-tersedia-permanently-delete
title: "Konflik File Tidak Tersedia: Permanently Delete Single dan Bulk Setelah Diproses Pihak Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-94
  - TC-GS-FILEMGR-101
  - TC-GS-FILEMGR-264
coverage:
  web: automated
---

# Konflik File Tidak Tersedia: Permanently Delete Single dan Bulk Setelah Diproses Pihak Lain

## Prerequisites

- Mode: FE+BE (kelas multi-konteks; pelaku lain hanya memicu perubahan state lewat sesi API, P-2).
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Pelaku lain (sesi API, tanpa sesi UI kedua, P-2; disediakan tim FE/BE): hanya memicu penghapusan permanen file di Recycle Bin lewat fixture BE. Tidak ada asersi di sesi lain.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run, di Recycle Bin; pemilik adalah user klon milik spec): `recycled-photo-01-{runId}-025.jpg` (TC-GS-FILEMGR-94); `recycled-photo-08-{runId}-025.jpg` dan `recycled-photo-09-{runId}-025.jpg` (TC-GS-FILEMGR-101); `gone-photo-01-{runId}-025.jpg` dan `gone-photo-02-{runId}-025.jpg` (D09, TC-GS-FILEMGR-264). Seluruhnya JPG dengan Deleted Date kurang dari retensi.
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): seeding Recycle Bin dengan pemilik klon; penghapusan permanen file oleh proses lain; membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen sisa file seed, hapus user klon.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-94: Permanently Delete single pada file yang sudah dihapus proses lain

1. Klik tombol Recycle Bin di toolbar, lalu ketik Search `{runId}-025`, tekan Enter
2. Verifikasi baris `recycled-photo-01-{runId}-025.jpg` tampil di Recycle Bin
3. [Sesi API] Hapus permanen `recycled-photo-01-{runId}-025.jpg` lewat fixture BE hingga tersimpan
4. Klik ikon `⋯` baris `recycled-photo-01-{runId}-025.jpg`, lalu klik `Permanently Delete`
5. Klik [Permanently Delete] pada dialog
6. Verifikasi toast info: "This file is no longer available."
7. Verifikasi Recycle Bin di-refresh
8. Verifikasi baris `recycled-photo-01-{runId}-025.jpg` hilang dari Recycle Bin
9. Tutup modal Recycle Bin dengan `✕` di header
10. Klik ikon Changelog di toolbar, ketik Search `recycled-photo-01-{runId}-025`, tekan Enter
11. Verifikasi jumlah entri Changelog untuk `recycled-photo-01-{runId}-025.jpg` sama dengan baseline (tidak ada entri log baru)
12. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-101: Bulk Permanently Delete dengan sebagian file sudah dihapus proses lain

13. Klik tombol Recycle Bin di toolbar, lalu ketik Search `{runId}-025`, tekan Enter
14. Centang baris `recycled-photo-08-{runId}-025.jpg` dan `recycled-photo-09-{runId}-025.jpg`
15. [Sesi API] Hapus permanen `recycled-photo-09-{runId}-025.jpg` lewat fixture BE hingga tersimpan
16. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
17. Verifikasi toast sukses: "Success, file has been permanently deleted. Some items were skipped."
18. Verifikasi `recycled-photo-08-{runId}-025.jpg` hilang dari Recycle Bin
19. Tutup modal Recycle Bin dengan `✕` di header
20. Klik ikon Changelog di toolbar, ketik Search `recycled-photo-09-{runId}-025`, tekan Enter
21. Verifikasi jumlah entri Changelog untuk `recycled-photo-09-{runId}-025.jpg` sama dengan baseline (tidak ada entri log untuk file itu)
22. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-264: Bulk Permanently Delete saat seluruh file terseleksi sudah dihapus proses lain

23. Klik tombol Recycle Bin di toolbar, lalu ketik Search `gone-photo`, tekan Enter
24. Centang baris `gone-photo-01-{runId}-025.jpg` dan `gone-photo-02-{runId}-025.jpg`
25. [Sesi API] Hapus permanen `gone-photo-01-{runId}-025.jpg` dan `gone-photo-02-{runId}-025.jpg` lewat fixture BE hingga tersimpan
26. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
27. Verifikasi toast info: "This file is no longer available."
28. Verifikasi Recycle Bin di-refresh
29. Verifikasi kedua baris hilang dari Recycle Bin
30. Verifikasi tidak ada toast sukses
31. Verifikasi tidak ada toast error
32. Tutup modal Recycle Bin dengan `✕` di header
33. Klik ikon Changelog di toolbar, ketik Search `gone-photo`, tekan Enter
34. Verifikasi jumlah entri Changelog untuk `gone-photo-01-{runId}-025.jpg` dan `gone-photo-02-{runId}-025.jpg` sama dengan baseline (tidak ada entri log baru)
35. Tutup modal Changelog dengan `✕` di header

## Notes

- Mode: FE+BE. Kelas c multi-konteks. Butir P-2: pelaku lain hanya memicu penghapusan permanen lewat sesi API dan tidak ada asersi di sesi lain, sesuai bagian 3 prinsip 13 pengecualian P-2. Subjudul `###` memetakan langkah ke id TC granular.
- Spec dipisah dari `TC-GS-FILEMGR-E2E-024` karena objek ujinya aksi Recycle Bin (Permanently Delete) bukan tabel utama (prinsip 1: topik aksi berbeda).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 13, 23 (membuka modal dan Search untuk menemukan baris target), 9, 19, 32 (menutup modal Recycle Bin), 10, 12, 20, 22, 33, 35 (membuka dan menutup modal Changelog), 3, 15, 25 (pemicu sesi API, ditulis "hingga ... tersimpan").
- Asersi tambahan di luar Expected TC (S-03): langkah 2 (baris target tampil sebagai anchor sebelum pemicu), 30 dan 31 (TC-GS-FILEMGR-264 Expected c memuat "tidak ada toast sukses maupun toast error", dipecah per klausa).
- Absence log (TC-GS-FILEMGR-94 c, 101 c, 264 c) diasersi sebagai jumlah entri yang sama dengan baseline per File Name (keputusan D-1 pilihan B): langkah 11, 21, 34. Baseline dicatat di hook `before`.
- Temuan untuk QA:
  - Q-8: pemicu "dihapus permanen oleh proses lain" (TC-GS-FILEMGR-94, 101, 264; D09 `gone-photo-*`) tidak didefinisikan di TC; spec memakai fixture BE lewat sesi API tanpa endpoint karangan (S-13).
  - Q-5/Q-7: TC menargetkan baris Pre-setup R05, R12, R13 yang dihapus; spec memakai file bersuffix dengan pemilik klon.
  - TC-GS-FILEMGR-264 tidak menyebut Search untuk menemukan baris `gone-photo-*`; spec menambah Search `gone-photo` sebagai langkah penghubung (nama D09).
  - Post Condition semua TC bernilai `-`.
