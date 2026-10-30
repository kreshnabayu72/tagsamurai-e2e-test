---
id: TC-GS-FILEMGR-E2E-004-resilience-baca-loading-error-dan-try-again
title: "Resilience Baca: Loading, Error Load, dan Try Again pada Tabel, Recycle Bin, Changelog, dan Kartu Storage"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-14
  - TC-GS-FILEMGR-15
  - TC-GS-FILEMGR-25
  - TC-GS-FILEMGR-32
  - TC-GS-FILEMGR-277
  - TC-GS-FILEMGR-278
  - TC-GS-FILEMGR-279
coverage:
  web: automated
---

# Resilience Baca: Loading, Error Load, dan Try Again pada Tabel, Recycle Bin, Changelog, dan Kartu Storage

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (data environment tetap, hanya dibaca): Tabel A2 (33 file aktif), Tabel A3 (16 file di Recycle Bin, retensi 30 hari), Tabel A4 (14 entri Changelog), dan skenario S1 Tabel A5 (Storage Quota 50 GB; Fixed Asset `3.2 GB`, Admin Console `1.4 GB`, Global Settings `204.8 MB`; Total Used `4.8 GB`; Last updated 14/09/26 02:00). Spec tidak membuat atau mengubah data.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script (tidak disebut di TC, PRD yang dibaca untuk spec ini):
  - Respons list File Manager: tahan 3 detik lalu jawab normal (langkah 1 sampai 8, TC-15); jawab 500 (langkah 9 sampai 15, TC-14; langkah 16 sampai 20, TC-278).
  - Respons kartu Storage Usage: tahan 3 detik lalu jawab normal (langkah 22 sampai 29, TC-279); jawab 500 (langkah 30 sampai 39, TC-277).
  - Respons list Recycle Bin: jawab 500 (langkah 40 sampai 47, TC-25).
  - Respons list Changelog: jawab 500 (langkah 48 sampai 54, TC-32).
- Kemampuan teknis: menghitung jumlah request list File Manager yang dikirim halaman (dipakai langkah 35 dan 39 untuk TC-277).
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah. Spec tidak mengubah data backend.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-15: Tampilan loading tabel utama saat data sedang dimuat

1. Pasang intercept respons list File Manager: tahan 3 detik
2. Buka Global Settings > File Manager dari sidebar
3. Verifikasi komponen skeleton/loading tampil di area tabel selama request berjalan
4. Verifikasi tidak ada empty state `No files yet` selama loading
5. Verifikasi tidak ada pesan error `Unable to load this data.` selama loading
6. Tunggu respons diterima
7. Verifikasi baris data menggantikan skeleton
8. Lepas intercept respons list File Manager

### TC-GS-FILEMGR-14: Tampilan tabel utama saat gagal memuat data lalu Try Again berhasil

9. Pasang intercept respons list File Manager: jawab 500
10. Buka ulang Global Settings > File Manager dari sidebar
11. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
12. Verifikasi area tabel bukan empty state `No files yet`
13. Lepas intercept respons list File Manager
14. Klik `[Try Again]`
15. Verifikasi tabel memuat baris data Tabel A2

### TC-GS-FILEMGR-278: Tabel gagal memuat tidak memengaruhi kartu Storage Usage

16. Pasang intercept respons list File Manager: jawab 500
17. Buka ulang Global Settings > File Manager dari sidebar
18. Verifikasi tabel menampilkan `Unable to load this data.` dengan `[Try Again]`
19. Verifikasi kartu Storage Usage menampilkan Total Used `4.8 GB`
20. Verifikasi kartu Storage Usage menampilkan daftar app `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, dan `Global Settings 204.8 MB`

### TC-GS-FILEMGR-279: Kartu menampilkan skeleton saat data sedang dimuat

21. Lepas intercept respons list File Manager
22. Pasang intercept respons kartu Storage Usage: tahan 3 detik
23. Buka ulang Global Settings > File Manager dari sidebar
24. Verifikasi komponen skeleton/loading tampil di dalam kartu Storage Usage selama request berjalan
25. Verifikasi tidak ada empty state `No storage data yet` dan tidak ada pesan error `Unable to load this data.` di kartu selama loading
26. Verifikasi tabel utama memuat baris data selagi kartu masih menampilkan skeleton
27. Tunggu respons kartu diterima
28. Verifikasi data S1 (Total Used `4.8 GB`) menggantikan skeleton di kartu
29. Lepas intercept respons kartu Storage Usage

### TC-GS-FILEMGR-277: Kartu gagal memuat lalu Try Again berhasil, tabel tidak terpengaruh

30. Pasang intercept respons kartu Storage Usage: jawab 500
31. Buka ulang Global Settings > File Manager dari sidebar
32. Verifikasi kartu menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
33. Verifikasi tidak ada toast
34. Verifikasi tabel utama tetap memuat baris data Tabel A2
35. Catat jumlah request list File Manager yang sudah terkirim
36. Lepas intercept respons kartu Storage Usage
37. Klik `[Try Again]` di dalam kartu
38. Verifikasi kartu memuat data S1 (Total Used `4.8 GB`)
39. Verifikasi jumlah request list File Manager sama dengan hasil langkah 35 sehingga tabel tidak ikut dimuat ulang

### TC-GS-FILEMGR-25: Tampilan Recycle Bin saat gagal memuat data lalu Try Again berhasil

40. Pasang intercept respons list Recycle Bin: jawab 500
41. Klik tombol Recycle Bin di toolbar
42. Verifikasi area tabel Recycle Bin menampilkan `Unable to load this data.` dan tombol `[Try Again]`
43. Verifikasi area tabel Recycle Bin bukan `Recycle bin is empty`
44. Lepas intercept respons list Recycle Bin
45. Klik `[Try Again]`
46. Verifikasi baris Tabel A3 tampil
47. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-32: Tampilan modal Changelog saat gagal memuat data lalu Try Again berhasil

48. Pasang intercept respons list Changelog: jawab 500
49. Klik ikon Changelog di toolbar
50. Verifikasi area tabel Changelog menampilkan `Unable to load this data.` dan tombol `[Try Again]`
51. Verifikasi area tabel Changelog bukan `No changelog yet`
52. Lepas intercept respons list Changelog
53. Klik `[Try Again]`
54. Verifikasi entri Tabel A4 tampil

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-15 (tunda respons) ditaruh sebelum TC-14 karena TC-15 hanya menahan respons; blok TC-278, TC-279, dan TC-277 ditaruh sebelum TC-25 dan TC-32 supaya semua blok yang memuat ulang halaman penuh berurutan, lalu dua modal.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 6 (menunggu respons), langkah 10, 17, 23, dan 31 (membuka ulang halaman dari sidebar), langkah 21 dan 22 (pelepasan dan pemasangan intercept), langkah 35 (mencatat baseline jumlah request), langkah 47 (menutup modal Recycle Bin dengan `✕`). Modal Changelog ditutup oleh hook `after`/`beforeEach` berikutnya.
- Alasan spec di atas sekitar 35 langkah (S-10, prinsip 13): seluruh blok berkelas b (fault injection dan penundaan respons baca) pada satu halaman dengan data Pre-setup yang sama dan tanpa mengubah data; tiap blok memasang dan melepas intercept sendiri serta memuat ulang halaman, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah login tidak ada di spec (hook `before`).
- Pengecualian: P-2 tidak dipakai; intercept adalah objek uji.
- Langkah 4, 5, dan 25 (asersi absence state sementara selama loading) didahului anchor positif skeleton pada surface yang sama (langkah 3 dan 24) sesuai 8b butir 11.
- Langkah 39: TC-277 butir c menyatakan "tabel tidak ikut dimuat ulang" tanpa menyebut cara mengamatinya; spec memakai hitungan request list (kemampuan teknis di Prerequisites).
- Temuan untuk QA:
  - TC-277 butir c ("tabel tidak ikut dimuat ulang") tidak memberi cara observasi; spec memakai hitungan request.
  - TC-14, TC-25, dan TC-32 tidak menyebut endpoint yang di-intercept; endpoint ditentukan tim FE (S-13).
  - Fixture S1 Tabel A5 dan Tabel A2 sampai A4 disediakan lewat fixture BE yang mekanismenya tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE.
