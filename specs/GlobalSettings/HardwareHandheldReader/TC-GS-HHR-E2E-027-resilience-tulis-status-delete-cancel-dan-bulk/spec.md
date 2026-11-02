---
id: TC-GS-HHR-E2E-027-resilience-tulis-status-delete-cancel-dan-bulk
title: "Resilience Tulis: Mark as, Delete, Cancel Request, dan Aksi Bulk saat Kegagalan Server 5xx serta Tidak Ada Entri Log Baru"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-147
  - TC-GS-HHR-155
  - TC-GS-HHR-160
  - TC-GS-HHR-225
  - TC-GS-HHR-226
  - TC-GS-HHR-352
coverage:
  web: automated
---

# Resilience Tulis: Mark as, Delete, Cancel Request, dan Aksi Bulk saat Kegagalan Server 5xx serta Tidak Ada Entri Log Baru

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata). Respons yang dipaksa lewat `Spectra.intercept()` pada request yang dimaksud TC (endpoint tidak disebut di TC, PRD, atau LLD yang dirujuk spec ini, sehingga tidak dituliskan): request ubah status (respons 500, langkah 5), request delete (500, langkah 21), request cancel (500, langkah 31), request bulk ubah status (500, langkah 40), request bulk delete (500, langkah 60), dan request edit (500, langkah 74). Setiap intercept dilepas segera setelah pemicunya selesai (S-09).
- Suite serial (`parallel: false`). Spec ini tidak mengubah state global karena seluruh aksi tulis diblokir respons 500. Hook `after` melepas intercept yang tersisa dan menutup dialog atau mengosongkan seleksi yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; langkah buka halaman di `## Test Steps` hanya ada sebagai langkah kembali dari surface log.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Client A): Seed Reader A, plan Growth, `Long Range` terpakai 5 dari 6 dan `Short Range` terpakai 5 dari 8, General Settings `dd/MM/yy` 24-hour Asia/Jakarta. Reader target (tidak ada yang diubah karena respons 500): DD-01 (Serial Number `SN-HHR-00101`, Long Range, Available, Alias Name `—`), DD-05 (`SN-HHR-00105`, `Chainway C72 - 1`, Waiting for Approval), DD-07 (`SN-HHR-00108`, `Honeywell CK65 - 1`, Long Range, Available), DD-08 (`SN-HHR-00109`, `Unitech EA520 - 1`, Short Range, Available). Device Name DD-01 sama dengan DD-06 (`Zebra RFID Reader - 1`), sehingga DD-01 ditemukan lewat Serial Number. Fixture baru `Fixture.hardwareHandheldReader.resilienceStatus027`.
- Data Dinamis: tidak ada.
- Baseline: jumlah entri Changelog Handheld Reader, System Log aktor (Detail User akun aktor > Tab System Log, PRD §8.2), dan Activity Log (Global Settings > Activity Log, PRD §8.3) dicatat sekali sebelum intercept pertama (langkah 1) dan dibandingkan pada langkah 13, 52, dan 83. Seluruh aksi spec ini gagal, sehingga baseline tidak berubah antar blok.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500; membaca toast beserta ketahanannya (toast error tidak hilang otomatis; `foundation/functions/toast-copy.md`) dan men-dismiss toast; membaca jumlah entri Changelog, System Log, dan Activity Log.

## Test Steps

### Baseline

1. Klik ikon Changelog, catat jumlah entri Changelog Handheld Reader sebagai baseline, lalu tutup Modal Changelog lewat `✕`
2. Buka Detail User akun aktor > Tab System Log, lalu catat jumlah entri System Log sebagai baseline
3. Buka Global Settings > Activity Log, lalu catat jumlah entri Activity Log sebagai baseline
4. Kembali ke Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-147: Konfirmasi Mark as Damaged gagal 5xx tidak mengubah status

5. Pasang intercept pada request ubah status: respons 500
6. Ketik Search `SN-HHR-00101`, tekan Enter
7. Klik `⋯` pada baris DD-01, pilih `Mark as Damaged`
8. Klik `[Mark as Damaged]` pada dialog
9. Verifikasi toast error "Error, failed to update device status." tampil
10. Verifikasi `Status` baris DD-01 tetap `Available`
11. Dismiss toast error, lalu tekan `Esc` untuk menutup dialog
12. Lepas intercept pada request ubah status
13. Klik ikon Changelog
14. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline
15. Tutup Modal Changelog lewat `✕`
16. Buka Detail User akun aktor > Tab System Log
17. Verifikasi jumlah entri System Log sama dengan baseline
18. Buka Global Settings > Activity Log
19. Verifikasi jumlah entri Activity Log sama dengan baseline
20. Kembali ke Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-155: Konfirmasi Delete gagal 5xx tidak menghapus reader

21. Pasang intercept pada request delete: respons 500
22. Ketik Search `SN-HHR-00101`, tekan Enter
23. Klik `⋯` pada baris DD-01, pilih `Delete`
24. Klik `[Delete]` pada dialog
25. Verifikasi toast error "Error, failed to delete device." tampil
26. Verifikasi baris DD-01 tetap ada
27. Verifikasi kartu `Long Range` tetap `5 of 6`
28. Dismiss toast error, lalu tekan `Esc` untuk menutup dialog
29. Lepas intercept pada request delete
30. Klik `(←)` pada kotak Search

### TC-GS-HHR-160: Konfirmasi Cancel Request gagal 5xx tidak membatalkan permintaan

31. Pasang intercept pada request cancel: respons 500
32. Ketik Search `SN-HHR-00105`, tekan Enter
33. Klik `⋯` pada baris DD-05, pilih `Cancel Request`
34. Klik `[Cancel Request]` pada dialog
35. Verifikasi toast error "Error, failed to cancel request." tampil
36. Verifikasi baris DD-05 tetap `Waiting for Approval`
37. Dismiss toast error, lalu tekan `Esc` untuk menutup dialog
38. Lepas intercept pada request cancel
39. Klik `(←)` pada kotak Search

### TC-GS-HHR-225: Konfirmasi bulk Mark as Damaged gagal 5xx tidak mengubah status

40. Pasang intercept pada request bulk ubah status: respons 500
41. Centang checkbox baris DD-01
42. Centang checkbox baris DD-07
43. Klik tombol `Bulk Action`
44. Klik `Mark as Damaged`
45. Klik `[Mark as Damaged]` pada dialog
46. Verifikasi toast error "Error, failed to update reader status." tampil
47. Verifikasi `Status` baris DD-01 tetap `Available`
48. Verifikasi `Status` baris DD-07 tetap `Available`
49. Dismiss toast error, lalu tekan `Esc` untuk menutup dialog
50. Lepas intercept pada request bulk ubah status
51. Hapus centang checkbox baris DD-01 dan DD-07
52. Klik ikon Changelog
53. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline
54. Tutup Modal Changelog lewat `✕`
55. Buka Detail User akun aktor > Tab System Log
56. Verifikasi jumlah entri System Log sama dengan baseline
57. Buka Global Settings > Activity Log
58. Verifikasi jumlah entri Activity Log sama dengan baseline
59. Kembali ke Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-226: Konfirmasi bulk Delete gagal 5xx tidak menghapus reader

60. Pasang intercept pada request bulk delete: respons 500
61. Centang checkbox baris DD-07
62. Centang checkbox baris DD-08
63. Klik tombol `Bulk Action`
64. Klik `Delete`
65. Klik `[Delete]` pada dialog
66. Verifikasi toast error "Error, failed to delete reader." tampil
67. Verifikasi baris DD-07 tetap ada
68. Verifikasi baris DD-08 tetap ada
69. Verifikasi kartu `Long Range` tetap `5 of 6`
70. Verifikasi kartu `Short Range` tetap `5 of 8`
71. Dismiss toast error, lalu tekan `Esc` untuk menutup dialog
72. Lepas intercept pada request bulk delete
73. Hapus centang checkbox baris DD-07 dan DD-08

### TC-GS-HHR-352: Aksi tulis gagal 5xx tidak menambah entri pada tiga surface

74. Pasang intercept pada request edit: respons 500
75. Ketik Search `SN-HHR-00101`, tekan Enter
76. Klik `⋯` pada baris DD-01, pilih `Edit Alias Name`
77. Isi `Alias Name` dengan `Reader Dock 01`
78. Klik `[Save]`
79. Dismiss toast error
80. Lepas intercept pada request edit
81. Klik `✕` di header dialog, lalu klik `[Leave]` pada dialog `Unsaved Changes`
82. Klik `(←)` pada kotak Search
83. Klik ikon Changelog
84. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline
85. Tutup Modal Changelog lewat `✕`
86. Buka Detail User akun aktor > Tab System Log
87. Verifikasi jumlah entri System Log sama dengan baseline
88. Buka Global Settings > Activity Log
89. Verifikasi jumlah entri Activity Log sama dengan baseline

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok mengikuti urutan nomor TC kecuali TC-GS-HHR-352 yang memakai Edit Alias Name ditaruh paling akhir. Tidak ada aksi yang menghabisi atau mengubah data, karena seluruh aksi tulis ditolak respons 500 (konvensi bagian 3 butir 5 tidak berlaku).
- Pencatatan baseline: TC-GS-HHR-147, 225, dan 352 masing-masing menulis baseline sebelum aksi; spec ini mencatatnya sekali di langkah 1 sebelum intercept pertama, karena aksi gagal tidak menambah entri sehingga baseline yang sama berlaku bagi ketiga pembanding (langkah 13, 52, 83). Asersi memakai selisih jumlah entri terhadap baseline, bukan angka absolut (S-12).
- Langkah penghubung (aksi tanpa `Verifikasi`): pemasangan dan pelepasan intercept; dismiss toast error dan `Esc` untuk menutup dialog konfirmasi (error-handling-convention §2: pada 5xx dialog tetap terbuka); Search untuk menemukan baris target dan `(←)` untuk mengosongkan Search; navigasi ke dan dari surface log; menghapus centang seleksi sebelum blok berikutnya (S-09); `✕` dan `[Leave]` untuk menutup dialog edit yang dirty (S-08; dialog `Unsaved Changes` tidak perlu dicatat lagi).
- Spec melewati sekitar 35 langkah (89 langkah). Alasan: seluruhnya satu kelas harness (kelas b: fault injection 5xx pada aksi tulis) dan satu akun aktor, tanpa data baru. Tiap blok TC memasang intercept sendiri, tidak mengubah data, dan menutup dialog di akhirnya, sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Langkah baca-log (buka surface, bandingkan jumlah entri) berpola dan diulang tiga kali mulai langkah 13, 52, dan 83 (tujuh sampai delapan langkah tiap blok).
- Spec 026, 027, dan 028 menguji kelas b (fault injection 5xx) pada permukaan berbeda dan sengaja dipisah: gabungannya 244 langkah (122, 89, dan 33), jauh di atas sekitar 35 langkah. Spec 026 membutuhkan simulator USB dan membuat reader, spec ini hanya memicu 5xx pada aksi tulis atas Seed Reader A yang tidak berubah, dan spec 028 hanya memicu 5xx pada unduhan, sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Pengecualian S-12 Population Seed Reader A HHR (A-5) berlaku untuk Seed Reader A (nama dan Serial Number literal tanpa suffix `{runId}`); spec ini tidak mengubah reader, dan pemulihan Seed Reader A dijamin fixture backend serta dinyatakan di `suite.md`.
- Pembagian TC lintas spec: TC-GS-HHR-96, 97, 121, 122, 137, 368, dan 436 (5xx dan timeout pada aktivasi serta edit) ada di spec 026; TC-GS-HHR-184, 315, dan 339 (kegagalan unduh) ada di spec 028. Asersi "tidak ada entri log" pada TC-GS-HHR-147, 225, dan 352 adalah asersi jumlah dengan baseline dan toast error sebagai anchor positif, sehingga ditulis di spec ini dan bukan di spec absence (kelas g); pencatatan log per aksi ada di spec 063.
- Temuan untuk QA:
  - TC-GS-HHR-147, 155, 160, 225, 226, dan 352 tidak menyebut cara membuka System Log aktor dan Activity Log; spec memakai PRD §8.2 (Detail User > Tab System Log) dan §8.3 (Global Settings > Activity Log) untuk navigasi.
  - TC-GS-HHR-147, 155, 160, 225, dan 226 tidak menyebut cara menutup dialog konfirmasi sesudah 5xx; spec menekan `Esc` (dialog tetap terbuka pada 5xx menurut error-handling-convention §2). Label tombol penutup dialog tidak disebut di TC.
  - TC-GS-HHR-147, 225, dan 352 menyebut System Log "aktor" tanpa menyebut identifikasi aktor selain akun yang sedang login; spec memakai Detail User akun aktor (Sari Dewi).
  - TC-GS-HHR-155 dan 226 menyebut "kuota tetap/tidak berubah" tanpa angka untuk kartu `Short Range`; spec memakai angka seeding Client A (`Long Range` `5 of 6`, `Short Range` `5 of 8`).
  - TC-GS-HHR-352 tidak menyebut toast error pada Expected; spec hanya men-dismiss toast tersebut dan tidak mengasersinya.
  - TC-GS-HHR-225 dan 226 menyebut checkbox baris tanpa menyebut bahwa seluruh baris harus berada pada halaman aktif; spec mengasumsikan 10 reader Seed Reader A tampil pada satu halaman.
