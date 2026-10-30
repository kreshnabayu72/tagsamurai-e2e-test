---
id: TC-GS-FILEMGR-E2E-011-mobile-resilience-preview-dan-download-gagal
title: "Mobile Resilience: Gagal Memuat Gambar Preview dan Download dari Preview Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-52
  - TC-GS-FILEMGR-59
coverage:
  mobile: automated
---

# Mobile Resilience: Gagal Memuat Gambar Preview dan Download dari Preview Gagal

## Prerequisites

- Mode: FE+BE (mobile, intercept parsial di atas backend nyata). Platform: aplikasi native Android; File Preview tampil sebagai bottom sheet.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Global Settings terpasang, kemampuan mengetuk elemen UI, serta membaca file unduhan di perangkat. Perangkat fisik bersama: `parallel: false` (S-09).
- Akun aktor: Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di aplikasi Android dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (data environment tetap, hanya dibaca): Tabel A2, F01 `budi-avatar.jpg` aktif dengan file fisik gambar berukuran 1200 × 800 piksel (disediakan tim FE/BE lewat fixture BE; mekanisme tidak disebut di TC, PRD, atau LLD). Spec tidak membuat, mengubah, atau menghapus data.
- Kebutuhan intercept (`Spectra.intercept()` pada jaringan perangkat Android, disediakan tim FE); nama endpoint konkret ditentukan tim FE di tahap script (tidak disebut di TC, PRD yang dibaca untuk spec ini):
  - Respons pembacaan gambar file `budi-avatar.jpg`: jawab 500 (dipasang pada langkah 1, dilepas pada langkah 6; TC-52).
  - Respons unduh file: jawab 500 (dipasang pada langkah 12, dilepas pada langkah 18; TC-59).
- Kemampuan teknis: membaca jumlah file di folder unduhan perangkat.
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah. Spec tidak mengubah data backend.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-52: Gagal memuat gambar pada File Preview lalu Try Again

1. Pasang intercept respons pembacaan gambar file: jawab 500
2. Ketuk teks `budi-avatar.jpg` di kolom File Name
3. Verifikasi area gambar menampilkan placeholder dengan teks `Unable to load this data.`
4. Verifikasi tombol `[Try Again]` tampil di dalam bottom sheet
5. Verifikasi bottom sheet tidak tertutup
6. Verifikasi `Dimensions` bernilai `—`
7. Lepas intercept respons pembacaan gambar file
8. Ketuk tombol `[Try Again]` di dalam bottom sheet
9. Verifikasi gambar tampil
10. Verifikasi `Dimensions` bernilai `1200 × 800 px`

### TC-GS-FILEMGR-59: Download file dari File Preview gagal karena storage

11. Catat jumlah file di folder unduhan perangkat
12. Pasang intercept request unduh file: jawab 500
13. Ketuk tombol `[Download File]`
14. Verifikasi toast error `Error, failed to download budi-avatar.jpg.`
15. Verifikasi tidak ada file terunduh (jumlah file di folder unduhan sama dengan hasil langkah 11)
16. Verifikasi bottom sheet File Preview tetap terbuka
17. Ketuk tombol `[Close]` untuk menutup bottom sheet
18. Lepas intercept request unduh file

## Notes

- Mode: FE+BE (mobile, kelas b). Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. `coverage.mobile: automated`; `coverage.web` tidak ditulis karena spec berjalan di aplikasi Android.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Layar File Manager di aplikasi Android dibuka di hook `beforeEach`.
- TC-59 butuh bottom sheet terbuka dengan gambar termuat sebelum intercept unduh dipasang: langkah 1 sampai 10 (TC-52) meninggalkan bottom sheet terbuka dengan gambar termuat, sehingga TC-59 memakainya tanpa pembukaan ulang; urutan sumber (TC-52, lalu TC-59) dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 11 (baseline jumlah file unduhan, dipakai langkah 15), langkah 17 (menutup bottom sheet), langkah 18 (melepas intercept setelah pemicu selesai, S-09).
- Langkah 15 (absence file terunduh) didahului anchor positif toast error pada langkah 14 pada pemicu yang sama (8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-52 dan TC-59 menyebut "intercept" pada aplikasi Android tanpa mekanisme; kemampuan intercept jaringan perangkat disediakan tim FE (S-13).
  - TC-59 judul "gagal karena storage" tetapi pemicunya adalah respons 500 pada request unduh; spec memaksa respons 500 lewat intercept (kelas b) dan mengasersi toast `T-11` PRD.
  - Mekanisme fixture BE untuk file fisik tidak disebut di TC, PRD, atau LLD (S-13).
