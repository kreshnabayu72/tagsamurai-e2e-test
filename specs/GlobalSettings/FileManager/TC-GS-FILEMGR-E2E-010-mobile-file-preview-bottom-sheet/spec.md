---
id: TC-GS-FILEMGR-E2E-010-mobile-file-preview-bottom-sheet
title: "Mobile: File Preview Bottom Sheet (Dimensions, Loading, Download, Tutup)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-49
  - TC-GS-FILEMGR-51
  - TC-GS-FILEMGR-54
  - TC-GS-FILEMGR-58
coverage:
  mobile: automated
---

# Mobile: File Preview Bottom Sheet (Dimensions, Loading, Download, Tutup)

## Prerequisites

- Mode: FE+BE (mobile, intercept parsial di atas backend nyata). Platform: aplikasi native Android; File Preview tampil sebagai bottom sheet.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Global Settings terpasang, kemampuan mengetuk elemen UI, serta membaca file unduhan di perangkat. Perangkat fisik bersama: `parallel: false` (S-09).
- Akun aktor: Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di aplikasi Android dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (data environment tetap, hanya dibaca): Tabel A2, F01 `budi-avatar.jpg` aktif dengan file fisik gambar berukuran 1200 × 800 piksel (disediakan tim FE/BE lewat fixture BE; mekanisme tidak disebut di TC, PRD, atau LLD). Spec tidak membuat, mengubah, atau menghapus data.
- Kebutuhan intercept (`Spectra.intercept()` pada jaringan perangkat Android, disediakan tim FE): respons pembacaan gambar file `budi-avatar.jpg`: tahan 3 detik lalu jawab normal (langkah 1 sampai 10); dipasang pada langkah 1 dan dilepas pada langkah 7. Nama endpoint konkret ditentukan tim FE di tahap script (tidak disebut di TC, PRD yang dibaca untuk spec ini).
- Kemampuan teknis: membaca file unduhan di perangkat (jumlah dan isi file di folder unduhan).
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-51 dan TC-GS-FILEMGR-49: State loading gambar dan nilai Dimensions pada File Preview

1. Pasang intercept respons pembacaan gambar file: tahan 3 detik
2. Ketuk teks `budi-avatar.jpg` di kolom File Name
3. Amati area gambar selama pembacaan tertunda
4. Verifikasi placeholder tampil di area gambar sampai gambar siap
5. Verifikasi judul bottom sheet `File Preview` dan tombol `[Close]` tampil selama loading
6. Tunggu respons diterima dan gambar selesai dimuat
7. Lepas intercept respons pembacaan gambar file
8. Verifikasi gambar menggantikan placeholder
9. Baca nilai `Dimensions`
10. Verifikasi `Dimensions` bernilai `1200 × 800 px`

### TC-GS-FILEMGR-58: Download file dari tombol Download File di File Preview

11. Catat jumlah file di folder unduhan perangkat
12. Ketuk tombol `[Download File]`
13. Verifikasi file gambar `budi-avatar.jpg` terunduh (jumlah file di folder unduhan bertambah satu dari hasil langkah 11)
14. Verifikasi isi file terunduh sama dengan file sumber
15. Verifikasi tidak ada toast sukses
16. Verifikasi bottom sheet File Preview tetap terbuka

### TC-GS-FILEMGR-54: Menutup bottom sheet File Preview lewat tombol Close dan ketuk backdrop

17. Ketuk tombol `[Close]`
18. Verifikasi bottom sheet File Preview tertutup
19. Verifikasi tidak ada toast
20. Verifikasi kartu `budi-avatar.jpg` tetap di daftar kartu (tidak ada mutasi)
21. Ketuk teks `budi-avatar.jpg` di kolom File Name
22. Ketuk area di luar bottom sheet
23. Verifikasi bottom sheet File Preview tidak tertutup
24. Verifikasi tidak ada toast
25. Verifikasi kartu `budi-avatar.jpg` tetap di daftar kartu (tidak ada mutasi)
26. Ketuk tombol `[Close]` untuk menutup bottom sheet

## Notes

- Mode: FE+BE (mobile). Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. `coverage.mobile: automated`; `coverage.web` tidak ditulis karena spec berjalan di aplikasi Android.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Layar File Manager di aplikasi Android dibuka di hook `beforeEach`, sehingga tidak ada langkah buka di `## Test Steps`.
- Penyimpangan urutan: TC-51 (loading) dan TC-49 (Dimensions) dikerjakan pada satu pembukaan bottom sheet (langkah 2 sampai 10) karena Dimensions dibaca setelah gambar selesai dimuat dan placeholder diasersi sebelum gambar siap (8b butir 5); TC-58 memakai bottom sheet yang sama; TC-54 (menutup) terakhir (prinsip 6).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 3 dan 6 (mengamati/menunggu), langkah 11 (baseline jumlah file unduhan, dipakai langkah 13), langkah 26 (menutup bottom sheet).
- Langkah 5 menulis judul `File Preview` dari PRD §4.6 mobile; Expected TC-51 butir b hanya menulis "judul bottom sheet".
- Langkah 20 dan 25 mengasersi "tidak ada mutasi" lewat kartu `budi-avatar.jpg` tetap di daftar; TC-54 butir c tidak merinci bentuk mutasi.
- Temuan untuk QA:
  - TC-51 dan TC-52 menyebut "intercept" pada aplikasi Android tanpa mekanisme; kemampuan intercept jaringan perangkat disediakan tim FE (S-13).
  - TC-49 butuh file fisik 1200 × 800 piksel; Tabel A2 hanya menyebut F01 berukuran 2.516.582 byte dan tidak menyatakan dimensinya (precondition TC-49 menambahkannya).
  - TC-58 Expected a ("isi sama dengan file sumber") tidak menyebut file sumber pembanding; spec membandingkan dengan file gambar sumber yang disediakan tim FE.
  - Mekanisme fixture BE untuk file fisik tidak disebut di TC, PRD, atau LLD (S-13).
