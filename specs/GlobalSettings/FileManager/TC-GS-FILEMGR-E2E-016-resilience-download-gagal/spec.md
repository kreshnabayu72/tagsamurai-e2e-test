---
id: TC-GS-FILEMGR-E2E-016-resilience-download-gagal
title: "Resilience Download: Kegagalan Download File, Changelog, Tabel Utama, dan Recycle Bin"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-56
  - TC-GS-FILEMGR-173
  - TC-GS-FILEMGR-196
  - TC-GS-FILEMGR-222
coverage:
  web: automated
---

# Resilience Download: Kegagalan Download File, Changelog, Tabel Utama, dan Recycle Bin

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness fault injection).
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (hanya dibaca, tidak diubah; Download tidak mengubah data): Tabel A2 (33 file aktif, termasuk F01 `budi-avatar.jpg`), Tabel A3 (16 file Recycle Bin), Tabel A4 (14 entri Changelog). Hook `before` memastikan ketiganya tersedia secara idempotent.
- Data Dinamis: tidak ada; spec tidak membuat data.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script:
  - Request unduh file (row action `Download`): jawab 500 (TC-GS-FILEMGR-56).
  - Request export Changelog File Manager: jawab 500 (TC-GS-FILEMGR-173).
  - Request export tabel utama: jawab 500 (TC-GS-FILEMGR-196).
  - Request export Recycle Bin: jawab 500 (TC-GS-FILEMGR-222).
- Kemampuan teknis: mengamati event download browser (tidak ada file terunduh); jeda nyata sampai 6 detik untuk membuktikan toast error tidak hilang otomatis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): lepas semua intercept.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-56: Download dari row action gagal

1. Ketik Search `budi-avatar`, tekan Enter
2. Pasang intercept pada request unduh file: jawab 500
3. Klik ikon `⋯` baris `budi-avatar.jpg`
4. Klik `Download`
5. Lepas intercept request unduh file
6. Verifikasi toast error: "Error, failed to download budi-avatar.jpg."
7. Amati toast error selama 6 detik tanpa tindakan
8. Verifikasi toast error tidak hilang otomatis
9. Verifikasi tidak ada file terunduh
10. Dismiss toast error

### TC-GS-FILEMGR-196: Download tabel utama gagal

11. Kosongkan Search (klik `(←)` pada kotak Search)
12. Verifikasi sedikitnya satu baris tampil pada tabel utama
13. Pasang intercept pada request export tabel utama: jawab 500
14. Klik ikon Download
15. Klik `Download as CSV`
16. Lepas intercept request export tabel utama
17. Verifikasi toast error: "Error, failed to download File-Manager-List."
18. Amati toast error selama 6 detik tanpa tindakan
19. Verifikasi toast error tidak hilang otomatis
20. Verifikasi tidak ada file terunduh
21. Dismiss toast error

### TC-GS-FILEMGR-222: Download Recycle Bin gagal

22. Klik tombol Recycle Bin di toolbar
23. Pasang intercept pada request export Recycle Bin: jawab 500
24. Klik ikon Download
25. Klik `Download as XLSX`
26. Lepas intercept request export Recycle Bin
27. Verifikasi toast error: "Error, failed to download File-Manager-Recycle-Bin."
28. Amati toast error selama 6 detik tanpa tindakan
29. Verifikasi toast error tidak hilang otomatis
30. Verifikasi tidak ada file terunduh
31. Dismiss toast error
32. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-173: Download Changelog gagal

33. Klik ikon Changelog di toolbar
34. Pasang intercept pada request export Changelog: jawab 500
35. Klik ikon Download
36. Klik `Download as CSV`
37. Lepas intercept request export Changelog
38. Verifikasi toast error: "Error, failed to download Changelog-File-Manager."
39. Amati toast error selama 6 detik tanpa tindakan
40. Verifikasi toast error tidak hilang otomatis
41. Verifikasi tidak ada file terunduh
42. Dismiss toast error
43. Tutup modal Changelog dengan `✕` di header

## Notes

- Mode: FE+BE (intercept parsial; kelas b fault injection, bagian 3 prinsip 13b). Seluruh kegagalan dapat dipicu lewat intercept respons HTTP, sehingga tidak membutuhkan `Mode: mock`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (43 langkah nominal, tanpa blok yang diulang). Alasan pertahanan: seluruh blok satu kelas harness (fault injection pada download, intercept parsial) dan berdiri sendiri; tiap blok memasang dan melepas intercept sendiri serta men-dismiss toast, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC pada spec: 56, 196, 222, 173. Urutan mengikuti surface (baris, tabel utama, modal Recycle Bin, modal Changelog) agar modal dibuka sekali tiap surface, bukan urutan TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 (Search untuk menemukan baris target), 5, 16, 26, 37 (melepas intercept segera setelah pemicu, S-09), 7, 18, 28, 39 (jeda nyata untuk mengamati toast error), 10, 21, 31, 42 (dismiss toast error persisten sebelum diasersi lagi, S-09), 11 (mengosongkan Search), 22, 32, 33, 43 (membuka dan menutup modal).
- Asersi tambahan di luar Expected TC (S-03): langkah 12 (baris pembanding sebelum export tabel utama).
- Spec tidak membuat maupun mengubah data; seluruh baris Pre-setup hanya dibaca (S-06).
- Temuan untuk QA:
  - TC-GS-FILEMGR-173 Dependensi menunjuk TC-GS-FILEMGR-28; TC-GS-FILEMGR-222 menunjuk TC-GS-FILEMGR-16 (precondition modal). Tidak ada kontradiksi.
  - Post Condition semua TC bernilai `-`.
