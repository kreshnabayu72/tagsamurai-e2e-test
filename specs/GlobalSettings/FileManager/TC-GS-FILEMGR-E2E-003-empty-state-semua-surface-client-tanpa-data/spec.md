---
id: TC-GS-FILEMGR-E2E-003-empty-state-semua-surface-client-tanpa-data
title: "Empty State Tabel Utama, Recycle Bin, Changelog, dan Kartu Storage Usage pada Client Tanpa Data"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-12
  - TC-GS-FILEMGR-23
  - TC-GS-FILEMGR-30
  - TC-GS-FILEMGR-272
coverage:
  web: automated
---

# Empty State Tabel Utama, Recycle Bin, Changelog, dan Kartu Storage Usage pada Client Tanpa Data

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada client uji tanpa data (client milik automation, lihat Temuan untuk QA). Akun, email, dan password disediakan tim FE (tidak ada di Tabel Data Uji Pre-setup TC); kredensial lewat env var `Spectra.env.GS_TC_EMPTY_PASSWORD` yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`. Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Kondisi awal client uji (disediakan tim FE/BE lewat fixture BE; mekanisme tidak disebut di TC, PRD, atau LLD): tanpa file aktif, tanpa file di Recycle Bin, tanpa entri Changelog File Manager, dan tanpa laporan Storage dari app mana pun (skenario S5 Tabel A5, Storage Quota 50 GB).
- Data yang di-seed spec di tengah alur (langkah 15): Tabel A2 (33 file aktif) untuk client uji lewat fixture BE; dibersihkan di hook `after` (semua file client uji dihapus permanen lewat API sehingga client kembali kosong). Pembersihan tidak berasumsi seeding berhasil penuh.
- Retensi Recycle Bin default 30 hari (tidak diubah spec).
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` untuk akun client uji disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-12: Tampilan tabel utama saat belum ada file sama sekali

1. Buka Global Settings > File Manager dari sidebar
2. Verifikasi ilustrasi empty state tampil dengan judul `No files yet`
3. Verifikasi deskripsi `Profile photos will appear here once users add them.`
4. Verifikasi tidak ada tombol CTA
5. Verifikasi tidak ada pesan error

### TC-GS-FILEMGR-23: Tampilan Recycle Bin saat tidak ada file yang dihapus

6. Klik tombol Recycle Bin di toolbar
7. Verifikasi ilustrasi empty state dengan judul `Recycle bin is empty`
8. Verifikasi deskripsi `Deleted files will appear here before being permanently removed.`
9. Verifikasi teks info retensi `Files are permanently deleted after 30 days.` tetap tampil
10. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-30: Tampilan modal Changelog saat belum ada entri

11. Klik ikon Changelog di toolbar
12. Verifikasi ilustrasi dengan judul `No changelog yet`
13. Verifikasi deskripsi `Activities and changes will appear here.`
14. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-272: Kartu menampilkan empty state saat belum ada app yang melapor, tabel tetap berfungsi

15. Seed Tabel A2 (33 file aktif) untuk client uji lewat fixture BE (dipakai sebagai precondition TC-272, tidak diasersi selain baris tabel)
16. Buka ulang Global Settings > File Manager dari sidebar
17. Amati kartu Storage Usage dan tabel utama
18. Verifikasi kartu menampilkan ilustrasi dengan judul `No storage data yet`
19. Verifikasi kartu menampilkan deskripsi `Storage usage will appear here once products report their usage.`
20. Verifikasi `Total Used` tidak tampil di kartu
21. Verifikasi `Storage Quota` tidak tampil di kartu
22. Verifikasi ProgressBar tidak tampil di kartu
23. Verifikasi `Last updated` tidak tampil di kartu
24. Verifikasi tabel utama memuat baris Tabel A2 (baris pertama `budi-avatar.jpg`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-272 ditaruh terakhir karena butuh Tabel A2 yang di-seed di tengah spec, sedangkan TC-12, TC-23, dan TC-30 butuh client tanpa file (prinsip 5: aksi yang menambah/mengubah data di akhir). Satu client dipakai untuk keempat TC dengan seeding langkah 15, sehingga tidak ada Step ganti akun.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 dan 14 (menutup modal), langkah 15 dan 16 (seeding dan buka ulang). Langkah 17 hanya mengamati.
- Langkah 9 memakai teks info retensi `Files are permanently deleted after 30 days.` dari Expected TC-GS-FILEMGR-16 (Section 1b); Expected TC-23 butir c hanya menulis "Teks info retensi tetap tampil".
- Langkah 20 sampai 23 adalah asersi absence atas elemen kartu; anchor positifnya adalah judul `No storage data yet` pada langkah 18 pada surface yang sama (8b butir 2).
- Temuan untuk QA:
  - TC-12, TC-23, dan TC-30 butuh client tanpa file aktif, tanpa Recycle Bin, dan tanpa Changelog, sedangkan TC-272 mensyaratkan Tabel A2 (33 file) pada client yang laporan Storage-nya S5; Pre-setup TC tidak menyebut client semacam itu. Spec memakai satu client uji milik automation dan men-seed Tabel A2 di tengah alur.
  - TC-23 Post/Expected c tidak menyebut teks info retensi; teks diambil dari TC-16.
  - Mekanisme fixture BE untuk menyiapkan client kosong, S5, dan seeding Tabel A2 tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Akun Total Control client uji tidak ada di Tabel A1 (S-11).
