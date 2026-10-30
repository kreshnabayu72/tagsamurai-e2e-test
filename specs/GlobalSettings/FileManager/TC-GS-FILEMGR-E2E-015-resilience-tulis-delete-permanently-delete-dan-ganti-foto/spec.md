---
id: TC-GS-FILEMGR-E2E-015-resilience-tulis-delete-permanently-delete-dan-ganti-foto
title: "Resilience Tulis: Delete Single, Bulk Delete, Permanently Delete, Storage Tidak Terjangkau, dan Ganti Foto Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-66
  - TC-GS-FILEMGR-67
  - TC-GS-FILEMGR-86
  - TC-GS-FILEMGR-92
  - TC-GS-FILEMGR-93
  - TC-GS-FILEMGR-102
  - TC-GS-FILEMGR-108
coverage:
  web: automated
---

# Resilience Tulis: Delete Single, Bulk Delete, Permanently Delete, Storage Tidak Terjangkau, dan Ganti Foto Gagal

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan fixture BE untuk kegagalan sisi server; kelas harness fault injection).
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run; pemilik adalah user klon milik spec, disediakan tim FE agar baris Pre-setup tidak diubah, S-06):
  - `budi-avatar-{runId}-015.jpg` (JPG, foto profil aktif pemilik klon `Budi Santoso`) untuk TC-GS-FILEMGR-66, TC-GS-FILEMGR-67, dan TC-GS-FILEMGR-108 (tidak dihapus).
  - `staff-photo-06-{runId}-015.jpg` dan `staff-photo-07-{runId}-015.jpg` (JPG, aktif) untuk TC-GS-FILEMGR-86 (tidak dihapus).
  - Recycle Bin: `legacy-photo-{runId}-015.jpeg` (TC-GS-FILEMGR-92, tidak dihapus), `expired-avatar-{runId}-015.jpg` (TC-GS-FILEMGR-93, dihapus permanen pada pengulangan sukses), `recycled-photo-10-{runId}-015.jpg` dan `recycled-photo-11-{runId}-015.jpg` (TC-GS-FILEMGR-102, tidak dihapus).
  - File upload `budi-new-{runId}-015.png` (PNG, file fisik disediakan tim FE) untuk TC-GS-FILEMGR-108.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script:
  - Request Delete (single dan bulk) pada File Manager: jawab 500 (TC-GS-FILEMGR-66, 67, 86).
  - Request Permanently Delete (single dan bulk): jawab 500 (TC-GS-FILEMGR-92, 102).
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): fixture BE yang membuat penyimpanan file tidak terjangkau dan memulihkannya (TC-GS-FILEMGR-93); fixture BE yang menggagalkan langkah soft-delete file lama pada penggantian foto berikutnya (TC-GS-FILEMGR-108); mengamati permintaan data tabel dikirim ulang setelah respons 500 (asersi "di-refresh"); membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`); penggantian foto profil di Global Settings > User (selektor modul lain disediakan tim FE).
- Jeda nyata: langkah yang menunggu sampai 6 detik untuk membuktikan toast error tidak hilang otomatis (toast sukses hilang setelah 4 detik, `foundation/functions/toast-copy.md`).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): lepas semua intercept, nonaktifkan fixture storage tidak terjangkau dan fixture kegagalan soft-delete, hapus permanen seluruh file seed, hapus user klon.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain fixture di atas. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-66 dan TC-GS-FILEMGR-67: Delete single gagal di server

1. Ketik Search `budi-avatar-{runId}-015`, tekan Enter
2. Pasang intercept pada request Delete: jawab 500
3. Klik ikon `⋯` baris `budi-avatar-{runId}-015.jpg`, lalu klik `Delete`
4. Klik [Delete] pada dialog
5. Lepas intercept request Delete
6. Verifikasi toast error: "Error, failed to delete budi-avatar-{runId}-015.jpg."
7. Verifikasi dialog Delete tertutup
8. Amati toast error selama 6 detik tanpa tindakan
9. Verifikasi toast error tidak hilang otomatis
10. Verifikasi tabel utama di-refresh
11. Verifikasi `budi-avatar-{runId}-015.jpg` tetap di tabel utama
12. Dismiss toast error
13. Buka modal Recycle Bin, ketik Search `budi-avatar-{runId}-015`, tekan Enter
14. Verifikasi empty state "No results found" pada modal Recycle Bin (`budi-avatar-{runId}-015.jpg` tidak ada di Recycle Bin)
15. Tutup modal Recycle Bin dengan `✕` di header
16. Buka Global Settings > User > Detail User Budi Santoso (klon milik spec)
17. Verifikasi foto profil Budi Santoso tidak berubah

### TC-GS-FILEMGR-86: Bulk Delete gagal seluruhnya

18. Kembali ke Global Settings > File Manager, ketik Search `{runId}-015`, tekan Enter
19. Centang baris `staff-photo-06-{runId}-015.jpg` dan `staff-photo-07-{runId}-015.jpg`
20. Pasang intercept pada request Delete: jawab 500
21. Klik `Bulk Action`, lalu klik `Delete`, lalu klik [Delete] pada dialog
22. Lepas intercept request Delete
23. Verifikasi toast error: "Error, failed to delete file."
24. Amati toast error selama 6 detik tanpa tindakan
25. Verifikasi toast error tidak hilang otomatis
26. Verifikasi Bulk Action Bar dan seleksi `2 Files selected` dipertahankan
27. Verifikasi tabel di-refresh
28. Verifikasi kedua file masih ada di tabel utama
29. Dismiss toast error, lalu klik `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-92: Permanently Delete single gagal di server

30. Buka modal Recycle Bin, ketik Search `legacy-photo-{runId}-015`, tekan Enter
31. Pasang intercept pada request Permanently Delete: jawab 500
32. Klik ikon `⋯` baris `legacy-photo-{runId}-015.jpeg`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
33. Lepas intercept request Permanently Delete
34. Verifikasi toast error: "Error, failed to permanently delete legacy-photo-{runId}-015.jpeg."
35. Verifikasi dialog Permanently Delete tertutup
36. Verifikasi Recycle Bin di-refresh
37. Verifikasi baris `legacy-photo-{runId}-015.jpeg` tetap di Recycle Bin
38. Dismiss toast error

### TC-GS-FILEMGR-102: Bulk Permanently Delete gagal seluruhnya

39. Ganti isi kotak search dengan `{runId}-015`, tekan Enter
40. Centang baris `recycled-photo-10-{runId}-015.jpg` dan `recycled-photo-11-{runId}-015.jpg`
41. Pasang intercept pada request Permanently Delete: jawab 500
42. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
43. Lepas intercept request Permanently Delete
44. Verifikasi toast error: "Error, failed to permanently delete file."
45. Verifikasi Bar dan seleksi `2 Files selected` dipertahankan
46. Verifikasi kedua file masih di Recycle Bin setelah refresh
47. Dismiss toast error, lalu klik `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-93: Permanently Delete gagal saat penyimpanan tidak terjangkau

48. Ganti isi kotak search dengan `expired-avatar-{runId}-015`, tekan Enter
49. Aktifkan fixture BE yang membuat penyimpanan file tidak terjangkau
50. Klik ikon `⋯` baris `expired-avatar-{runId}-015.jpg`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
51. Verifikasi toast error: "Error, failed to permanently delete expired-avatar-{runId}-015.jpg."
52. Verifikasi baris `expired-avatar-{runId}-015.jpg` tetap di Recycle Bin
53. Dismiss toast error
54. Nonaktifkan fixture BE penyimpanan tidak terjangkau
55. Klik ikon `⋯` baris `expired-avatar-{runId}-015.jpg`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
56. Verifikasi toast sukses: "Success, expired-avatar-{runId}-015.jpg has been permanently deleted."
57. Tutup modal Recycle Bin dengan `✕` di header
58. Klik ikon Changelog di toolbar, ketik Search `expired-avatar-{runId}-015`, tekan Enter
59. Verifikasi jumlah entri Permanently Delete untuk `expired-avatar-{runId}-015.jpg` tepat satu (baseline ditambah satu, hanya dari pengulangan sukses; tidak ada entri dari percobaan gagal)
60. Ganti isi kotak search dengan `legacy-photo-{runId}-015`, tekan Enter
61. Verifikasi jumlah entri Changelog untuk `legacy-photo-{runId}-015.jpeg` sama dengan baseline (tidak ada entri log baru)
62. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-108: Kegagalan penggantian foto membatalkan seluruh operasi

63. Aktifkan fixture BE yang menggagalkan langkah soft-delete file lama pada penggantian foto
64. Di Global Settings > User > Detail User Budi Santoso (klon milik spec), ganti foto profil dengan `budi-new-{runId}-015.png`, lalu klik [Save]
65. Verifikasi penyimpanan foto gagal dengan toast error dari modul User
66. Nonaktifkan fixture BE kegagalan soft-delete
67. Buka Global Settings > File Manager, ketik Search `{runId}-015`, tekan Enter
68. Verifikasi `budi-avatar-{runId}-015.jpg` tetap di tabel utama sebagai foto aktif
69. Verifikasi `budi-new-{runId}-015.png` tidak ada di tabel utama
70. Buka modal Recycle Bin, ketik Search `budi-avatar-{runId}-015`, tekan Enter
71. Verifikasi empty state "No results found" (`budi-avatar-{runId}-015.jpg` tidak ada di Recycle Bin)
72. Tutup modal Recycle Bin dengan `✕` di header

## Notes

- Mode: FE+BE (intercept parsial dan fixture BE; kelas b fault injection, bagian 3 prinsip 13b). Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (72 langkah nominal; tidak ada blok berulang yang diekspansi). Alasan pertahanan: seluruh blok satu kelas harness (fault injection pada aksi tulis File Manager), tiap blok memakai data milik sendiri dan tidak membutuhkan hasil blok lain, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Ukuran lebih rendah mengharuskan membuka ulang login, hook, dan fixture yang sama tanpa menambah isolasi.
- TC-GS-FILEMGR-66 dan TC-GS-FILEMGR-67 memiliki langkah pemicu identik (intercept 500 pada Delete single `budi-avatar`); keduanya dijalankan sebagai satu alur dan Expected keduanya diasersi berurutan pada langkah 6 s.d. 11 (TC-66 a, b, c, d, e; TC-67 a, b, c).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 18, 30, 39, 48, 67 (Search/navigasi untuk menemukan baris target), 5, 22, 33, 43 (melepas intercept segera setelah pemicu, S-09), 12, 29, 38, 47, 53 (dismiss toast error persisten sebelum diasersi lagi, S-09; bar dikosongkan agar seleksi tidak terbawa), 13, 15, 57, 58, 62, 70, 72 (membuka dan menutup modal), 54, 64 (menonaktifkan fixture), 8 dan 24 (jeda nyata untuk mengamati toast error).
- Asersi tambahan di luar Expected TC (S-03): langkah 14, 71 (anchor absence "No results found"), 11 (pembanding baris), 16 dan 17 (TC-GS-FILEMGR-66 d: foto profil pemilik diperiksa lewat Detail User, selektor disediakan tim FE).
- Urutan: TC-93 ditempatkan sesudah TC-92/102 karena pengulangan yang sukses menghapus file permanen; TC-108 di akhir (langkah 63 sampai 72) karena membuka modul User dan memakai file `budi-avatar-{runId}-015.jpg` yang belum berubah.
- Asersi absence log (TC-GS-FILEMGR-93 b dan TC-GS-FILEMGR-92 c) memakai baseline jumlah entri Changelog (keputusan D-1 pilihan B; asersi jumlah, bukan kelas g, bagian 3 prinsip 13g): langkah 59 (jumlah tepat satu dari pengulangan sukses, tidak ada entri dari percobaan gagal) dan langkah 61 (jumlah sama dengan baseline). Baseline dicatat di hook `before`.
- Temuan untuk QA:
  - Q-4: kegagalan "penyimpanan file tidak terjangkau" (TC-GS-FILEMGR-93) dan "kegagalan langkah soft-delete" (TC-GS-FILEMGR-108) dipicu "fixture BE" tanpa mekanisme di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE", tanpa endpoint karangan.
  - Q-9: TC-GS-FILEMGR-108 mengganti foto di modul User; langkah UI modul lain tidak didefinisikan di TC ini; selektor ditandai "disediakan tim FE". Toast error "dari modul User" tidak memiliki teks persis di TC; langkah 63 mengasersi toast error tanpa teks.
  - TC-GS-FILEMGR-92 Expected c ("Tidak ada entri log baru") tidak menyebut surface log; spec mengasersi di Changelog File Manager saja.
  - TC-GS-FILEMGR-93 langkah 4 ("ulangi aksi yang sama") mengulang aksi pada baris yang sama; spec menuliskan ulang langkah (S-04).
  - Q-5/Q-7: TC menargetkan baris Pre-setup (F01, F14, F15, R02, R03, R14, R15); spec memakai file bersuffix milik spec (S-06). Pemilik klon bernama literal belum terdaftar sebagai pengecualian S-12.
  - Post Condition semua TC bernilai `-`.
