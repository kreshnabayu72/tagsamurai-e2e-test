---
id: TC-GS-FILEMGR-E2E-012-mobile-kartu-file-recycle-bin-storage-dan-guided-tooltip
title: "Mobile: Kartu File, Recycle Bin Bottom Sheet, Kartu Storage Usage, Tanpa Bulk, dan Guided Tooltip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-259
  - TC-GS-FILEMGR-260
  - TC-GS-FILEMGR-261
  - TC-GS-FILEMGR-267
  - TC-GS-FILEMGR-284
coverage:
  mobile: automated
---

# Mobile: Kartu File, Recycle Bin Bottom Sheet, Kartu Storage Usage, Tanpa Bulk, dan Guided Tooltip

## Prerequisites

- Mode: FE+BE (mobile). Platform: aplikasi native Android (PRD §4.6); tampilan berupa card list dengan bottom sheet toolbar.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Global Settings terpasang serta kemampuan mengetuk, menekan lama, membaca elemen UI, dan menekan tombol Back sistem Android (langkah 14, 19, 39, 40). Perangkat fisik bersama: `parallel: false` (S-09).
- Akun aktor: Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di aplikasi Android dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (data environment tetap, hanya dibaca): Tabel A2 (33 file aktif, termasuk F01 `budi-avatar.jpg`), Tabel A3 (16 file di Recycle Bin, termasuk R01 `old-avatar.png`, Auto-Purge In `29 days`), dan skenario S1 Tabel A5 (Total Used `4.8 GB`, Storage Quota `50.0 GB`, ProgressBar `9%`, `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB`, `Last updated 14/09/26 02:00`). Spec tidak membuat, mengubah, atau menghapus data; dialog Delete pada TC-261 tidak dikonfirmasi.
- Guided Tooltip (pengecualian dari pernyataan hook suite di `suite.md`): TC-267 mensyaratkan flag `guided_tooltip_seen_gs-file-manager` belum ada. Hook `before` spec ini mencatat nilai awal flag, menghapus flag untuk akun aktor lewat API (kemampuan "disediakan tim FE"), dan hook `after` memulihkan nilai awal. TC-267 dijalankan pertama dan setelah selesai flag berstatus seen sehingga TC lain tidak tertutup walkthrough.
- Kemampuan teknis: fixture BE untuk Tabel A2, A3, dan S1 (mekanisme seeding tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE); API untuk membaca, menghapus, dan memulihkan flag Guided Tooltip akun aktor.
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-267: Guided Tooltip di aplikasi mobile menyorot ikon toolbar yang memuat Recycle Bin

1. Buka Global Settings > File Manager di aplikasi Android (kunjungan pertama, flag belum ada)
2. Amati header dan walkthrough Step 1
3. Verifikasi header memuat tombol bantuan `[?]` di sebelah kanan Breadcrumb `File Manager`
4. Verifikasi Step 1 menyorot daftar kartu dengan judul `File Manager`
5. Ketuk `[Next]`
6. Amati Step 2
7. Verifikasi Step 2 menyorot ikon (⋯) toolbar yang memuat Recycle Bin dengan judul `Recycle Bin`
8. Ketuk `[Done]` untuk menutup walkthrough

### TC-GS-FILEMGR-259: Kartu file di aplikasi mobile menampilkan subset kolom dan row action Download dan Delete

9. Amati header, toolbar, dan satu kartu file
10. Verifikasi header memuat Breadcrumb `File Manager`, tombol bantuan `[?]` di sebelah kanan Breadcrumb, dan ikon Changelog
11. Ketuk ikon (⋯) pada toolbar
12. Verifikasi toolbar memuat ikon Search inline dan ikon (⋯)
13. Verifikasi bottom sheet toolbar berisi `Column Visibility`, `Filter`, `Download`, dan `Recycle Bin`
14. Tutup bottom sheet toolbar dengan menekan tombol Back sistem
15. Verifikasi kartu `budi-avatar.jpg` memuat File Name, Format, Size, dan User Name
16. Verifikasi Upload Date dan Uploaded By tidak tampil pada kartu
17. Ketuk ikon (⋯) pada kartu `budi-avatar.jpg`
18. Verifikasi menu (⋯) kartu memuat `Download` dan `Delete`
19. Tutup menu (⋯) kartu dengan menekan tombol Back sistem

### TC-GS-FILEMGR-284: Kartu Storage Usage di aplikasi mobile tampil penuh di atas toolbar dalam satu kolom

20. Amati urutan elemen dari atas ke bawah
21. Verifikasi kartu Storage Usage tampil di atas toolbar (Search inline dan ikon (⋯)) dan di atas kartu file
22. Verifikasi isi kartu Storage Usage sama dengan web: `Total Used` `4.8 GB`, `Storage Quota` `50.0 GB`, ProgressBar `9%`, `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB`, dan `Last updated 14/09/26 02:00`
23. Verifikasi ProgressBar dan daftar per app ditumpuk dalam satu kolom
24. Verifikasi kartu Storage Usage tidak disembunyikan

### TC-GS-FILEMGR-261: Tidak ada multi-select dan bulk action di aplikasi mobile

25. Tekan lama kartu `budi-avatar.jpg`
26. Verifikasi tidak ada checkbox pada kartu
27. Verifikasi tidak ada Floating Bottom Bulk Bar
28. Ketuk ikon (⋯) pada kartu `budi-avatar.jpg`
29. Ketuk `Delete`
30. Verifikasi dialog konfirmasi berjudul `Delete File` tampil sebagai bottom sheet
31. Tutup dialog konfirmasi dengan mengetuk `[Cancel]`

### TC-GS-FILEMGR-260: Kartu Recycle Bin di aplikasi mobile menambah Auto-Purge In dan row action Permanently Delete

32. Ketuk ikon (⋯) pada toolbar
33. Ketuk `Recycle Bin` pada bottom sheet toolbar
34. Verifikasi Recycle Bin tampil sebagai bottom sheet
35. Amati kartu `old-avatar.png`
36. Verifikasi kartu `old-avatar.png` memuat Auto-Purge In `29 days` selain kolom kartu tabel utama
37. Ketuk ikon (⋯) pada kartu `old-avatar.png`
38. Verifikasi menu (⋯) kartu memuat `Permanently Delete`
39. Tutup menu (⋯) kartu dengan menekan tombol Back sistem
40. Tutup bottom sheet Recycle Bin dengan menekan tombol Back sistem

## Notes

- Mode: FE+BE (mobile). Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. `coverage.mobile: automated`; `coverage.web` tidak ditulis karena spec berjalan di aplikasi Android.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-267 dijalankan pertama (bukan terakhir seperti pada sumber) karena walkthrough hanya muncul otomatis pada kunjungan pertama (state sementara, 8b butir 5) dan menutupi layar bagi TC lain; setelah langkah 8 flag berstatus seen. TC-261 dan TC-260 berurutan terakhir: TC-261 hanya membuka dialog konfirmasi tanpa mengonfirmasi dan TC-260 membuka bottom sheet Recycle Bin (prinsip 6). Urutan TC-259, TC-284 mengikuti sumber (TC-284 tepat setelah TC-259 karena sama-sama membaca layar awal).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (kunjungan pertama; layar awal untuk TC-259 dst. memakai kunjungan yang sama), langkah 8 (menutup walkthrough dengan `[Done]`), langkah 11 dan 14 (membuka dan menutup bottom sheet toolbar untuk mengamati isinya), langkah 19, 39, 40 (menutup menu/bottom sheet), langkah 31 (menutup dialog dengan `[Cancel]`), langkah 32 dan 33 (membuka Recycle Bin dari bottom sheet toolbar, sesuai langkah TC-260).
- Langkah 8: TC-267 hanya menulis langkah sampai Step 2; penutupan walkthrough dengan `[Done]` (label di Step terakhir menurut TC-GS-FILEMGR-34) adalah langkah penghubung.
- Langkah 31 memakai `[Cancel]` pada dialog konfirmasi sesuai konvensi (bagian 9) dan TC-GS-FILEMGR-61/62; TC-261 tidak menyebut cara menutup dialog.
- Langkah 14, 19, 39, 40: tombol Back sistem Android dipakai untuk menutup bottom sheet/menu; TC tidak menyebut cara menutupnya.
- Langkah 16 adalah asersi absence didahului anchor positif kartu memuat File Name, Format, Size, dan User Name pada langkah 15 (8b butir 2). Langkah 26 dan 27 didahului pemicu tekan lama (langkah 25) dan kartu tampil; anchor positif: daftar kartu tampil (langkah 15).
- Alasan spec di atas sekitar 35 langkah (S-10): seluruh blok berjalan di satu platform dan satu perangkat Android (kartu file, kartu Storage Usage, tanpa bulk, Recycle Bin bottom sheet, Guided Tooltip), semuanya baca-saja tanpa mengubah data; memecah per TC menambah login dan penyiapan perangkat tanpa manfaat karena tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna).
- Temuan untuk QA:
  - TC-267 Precondition b ("Akun belum pernah membuka File Manager di aplikasi Android") dan flag `guided_tooltip_seen_gs-file-manager`: flag sama dengan flag web; spec menghapus flag akun aktor lewat API sebelum spec dan memulihkannya sesudah. Tidak jelas apakah flag dibagi antara web dan Android per akun.
  - TC-267 hanya menulis langkah sampai Step 2; cara menutup walkthrough tidak disebut.
  - TC-261 Expected b tidak menyebut tombol penutup dialog `Delete File`; spec memakai `[Cancel]`.
  - Mekanisme fixture BE untuk Tabel A2, A3, dan S1 tidak disebut di TC, PRD, atau LLD (S-13).
