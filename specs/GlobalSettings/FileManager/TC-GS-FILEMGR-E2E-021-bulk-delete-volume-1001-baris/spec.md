---
id: TC-GS-FILEMGR-E2E-021-bulk-delete-volume-1001-baris
title: "Bulk Delete dan Bulk Permanently Delete dengan 1.001 Baris Terseleksi"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-88
  - TC-GS-FILEMGR-105
coverage:
  web: automated
---

# Bulk Delete dan Bulk Permanently Delete dengan 1.001 Baris Terseleksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Kelas harness volume (kelas e, 1.001 baris). State global yang diubah: Selection Limit di Lifecycle Settings > System Limits dinaikkan ke 1500. Akun dan akses pengubah Lifecycle Settings tidak disebut TC, PRD, atau LLD File Manager: disediakan tim FE. Hook `before` mencatat nilai awal lalu menyetel 1500; hook `after` memulihkan nilai awal walau spec gagal.
- Data Dinamis (D07, seeding fixture BE di hook `before`, bersuffix per run): 1.001 file aktif `bulk-seed-0001-{runId}-021.jpg` s.d. `bulk-seed-1001-{runId}-021.jpg` (JPG). Tidak ada baris lain di tabel utama dan Recycle Bin yang cocok dengan Search `bulk-seed`. Dipakai oleh TC-GS-FILEMGR-88 (Bulk Delete); sesudah itu seluruhnya berada di Recycle Bin dan dipakai oleh TC-GS-FILEMGR-105 (Bulk Permanently Delete). Kedua TC memakai satu kali seeding karena D07 menyatakan 1.001 file "aktif (bulk Delete) atau di Recycle Bin (bulk Permanently Delete)".
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): seeding 1.001 file aktif; mengubah Selection Limit; batas waktu tunggu operasi massal diperpanjang sesuai ukuran data.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan Selection Limit awal; hapus permanen seluruh file `bulk-seed-*-{runId}-021.jpg` yang masih ada (aktif maupun di Recycle Bin).
- Suite serial (`parallel: false`). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-88: Bulk Delete 1.001 baris

1. Ketik Search `bulk-seed`, tekan Enter
2. Verifikasi sedikitnya satu baris tampil pada tabel utama
3. Klik tombol `Select All (1001 records)`
4. Verifikasi bar menampilkan `1001 Files selected`
5. Verifikasi tidak ada toast cap
6. Klik `Bulk Action`, klik `Delete`, lalu klik [Delete] pada dialog
7. Verifikasi toast sukses: "Success, file has been deleted."
8. Buka modal Recycle Bin, ketik Search `bulk-seed`, tekan Enter
9. Verifikasi hasil Search memuat 1.001 file `bulk-seed-` (tombol `Select All (1001 records)` tampil)
10. Verifikasi baris pada halaman aktif memiliki Deleted By `Sinta M`

### TC-GS-FILEMGR-105: Bulk Permanently Delete 1.001 baris

11. Klik tombol `Select All (1001 records)`
12. Verifikasi bar menampilkan `1001 Files selected`
13. Verifikasi tidak ada toast cap
14. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
15. Verifikasi toast sukses: "Success, file has been permanently deleted."
16. Verifikasi pencarian `bulk-seed` di Recycle Bin menampilkan `No results found`
17. Tutup modal Recycle Bin dengan `✕` di header

## Notes

- Mode: FE+BE. Kelas e (volume ≥ 1.000 baris, bagian 3 prinsip 13e). Subjudul `###` memetakan langkah ke id TC granular.
- TC-GS-FILEMGR-105 memakai 1.001 file hasil TC-GS-FILEMGR-88 di Recycle Bin (D07) supaya seeding volume tidak diulang; bila blok TC-GS-FILEMGR-88 gagal sebelum langkah 6, blok TC-GS-FILEMGR-105 kehilangan data. Alasan menggabung: sama-sama kelas e pada satu dataset D07 dan kegagalan seeding ulang 1.001 file menambah beban run.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 (Search sesuai TC), 8 (membuka Recycle Bin dan Search sesuai TC-GS-FILEMGR-88 langkah 4), 17 (menutup modal).
- Asersi tambahan di luar Expected TC (S-03): langkah 2 (baris pembanding sebelum Select All).
- Langkah 10 mengasersi Deleted By pada baris halaman aktif saja (Recycle Bin menampilkan 10 baris per halaman); TC menyebut 1.001 file tanpa menjelaskan cara memeriksa seluruh baris. Hitungan 1.001 diasersi lewat tombol `Select All (1001 records)`.
- Waktu tunggu: operasi massal 1.001 baris mungkin lebih lama dari operasi biasa; batas tunggu ditentukan tim FE di tahap script.
- Temuan untuk QA:
  - Q-4: seeding 1.001 file (D07) dan perubahan Selection Limit tidak memiliki mekanisme di TC; ditulis "disediakan tim FE/BE".
  - NC-07: cap API dinaikkan ke 5.000 sehingga seleksi 1.001 diproses seluruhnya; TC-GS-FILEMGR-88/105 menjadi dasar asersi.
  - Dependensi TC-GS-FILEMGR-105 menunjuk TC-GS-FILEMGR-100 (bulk Permanently Delete) bukan TC-GS-FILEMGR-88; spec tetap menggunakan data D07 hasil TC-GS-FILEMGR-88 (lihat Notes).
  - Post Condition semua TC bernilai `-`.
