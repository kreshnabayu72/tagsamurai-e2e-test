---
id: TC-GS-FILEMGR-E2E-040-filter-recycle-bin-panel-opsi-rentang-dan-logika
title: "Filter Modal Recycle Bin: Panel, Opsi Dropdown, OR, Rentang Size, Rentang Deleted Date, dan AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-204
  - TC-GS-FILEMGR-205
  - TC-GS-FILEMGR-206
  - TC-GS-FILEMGR-207
  - TC-GS-FILEMGR-208
  - TC-GS-FILEMGR-209
coverage:
  web: automated
---

# Filter Modal Recycle Bin: Panel, Opsi Dropdown, OR, Rentang Size, Rentang Deleted Date, dan AND

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A3 (16 baris Recycle Bin, retensi 30 hari, Deleted Date relatif terhadap waktu uji). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Nama file literal sesuai Tabel A3 karena asersi filter bergantung pada nama, format, ukuran, dan Deleted By (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): hitungan baris hasil filter hanya valid bila tidak ada spec lain yang menambah atau menghapus file Recycle Bin bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: kontrol date range picker yang dapat memilih hari relatif terhadap waktu uji (langkah 36: hari Deleted Date `old-avatar.png`, yaitu sekarang − 1 hari); mengisi field Min dan Max rentang Size; mengetik di kotak search di dalam dropdown filter; membaca placeholder field.

## Test Steps

1. Klik tombol Recycle Bin di toolbar
2. Verifikasi tabel Recycle Bin memuat sedikitnya satu baris
3. Klik ikon Filter di toolbar modal

### TC-GS-FILEMGR-204: Screening Filter Panel modal Recycle Bin

4. Verifikasi ikon Filter berubah gelap saat panel terbuka
5. Verifikasi field pertama `File Format` berupa multi-select searchable dengan placeholder `All formats`
6. Verifikasi field kedua `Size (KB)` berupa Range Min–Max dengan placeholder `Min` dan `Max`
7. Verifikasi field ketiga `Deleted Date` berupa date range picker dengan placeholder `Select date`
8. Verifikasi field keempat `Deleted By` berupa multi-select searchable dengan placeholder `All users`
9. Verifikasi tidak ada field filter untuk `Auto-Purge In`
10. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-GS-FILEMGR-205: Opsi dropdown filter berasal dari data Recycle Bin

11. Buka dropdown `File Format`
12. Verifikasi opsi tepat tiga: `JPEG`, `JPG`, `PNG`
13. Verifikasi opsi File Format tidak berasal dari file aktif tabel utama: tidak ada opsi selain `JPEG`, `JPG`, dan `PNG`
14. Tutup dropdown `File Format`, lalu buka dropdown `Deleted By`
15. Verifikasi opsi tepat tiga nama lengkap: `Agus Wibowo`, `Sinta Maharani`, `System`
16. Tutup dropdown `Deleted By`

### TC-GS-FILEMGR-206: Filter multi-select File Format dan Deleted By dengan logika OR dalam satu field

17. Pilih `JPEG` pada File Format, klik `[Apply]`
18. Verifikasi tabel memuat 1 baris: `legacy-photo.jpeg`
19. Klik `[Clear Field]`, klik `[Apply]`
20. Pilih `JPEG` dan `PNG` pada File Format, klik `[Apply]`
21. Verifikasi tabel memuat 3 baris: `old-avatar.png`, `legacy-photo.jpeg`, `due-photo.png`
22. Klik `[Clear Field]`, klik `[Apply]`
23. Pilih `System` pada Deleted By, klik `[Apply]`
24. Verifikasi tabel memuat 5 baris: `legacy-photo.jpeg`, `recycled-photo-09.jpg`, `recycled-photo-10.jpg`, `recycled-photo-11.jpg`, `recycled-photo-12.jpg`

### TC-GS-FILEMGR-207: Filter rentang Size dalam KB dengan batas inklusif

25. Klik `[Clear Field]`, isi Min `700` dan Max `700`, klik `[Apply]`
26. Verifikasi tabel hanya memuat `due-photo.png`
27. Klik `[Clear Field]`, isi Min `2048` dan Max `2048`, klik `[Apply]`
28. Verifikasi tabel hanya memuat `old-avatar.png`
29. Klik `[Clear Field]`, isi Min `701` dan Max `1023`, klik `[Apply]`
30. Verifikasi tampil `No results found`

### TC-GS-FILEMGR-209: Kombinasi filter File Format dan Deleted By dengan logika AND

31. Klik `[Clear Field]`
32. Pilih `JPG` pada File Format dan `System` pada Deleted By, klik `[Apply]`
33. Verifikasi tabel memuat 4 baris: `recycled-photo-09.jpg`, `recycled-photo-10.jpg`, `recycled-photo-11.jpg`, `recycled-photo-12.jpg`
34. Verifikasi `legacy-photo.jpeg` (System tetapi JPEG) tidak tampil

### TC-GS-FILEMGR-208: Filter rentang Deleted Date dengan batas inklusif satu hari

35. Klik `[Clear Field]`
36. Pilih Deleted Date dengan awal dan akhir sama pada tanggal `old-avatar.png` (sekarang − 1 hari), klik `[Apply]`
37. Verifikasi tabel hanya memuat `old-avatar.png`
38. Verifikasi baris lain (Deleted Date berbeda hari, mis. `recycled-photo-01.jpg`) tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 204, 205, 206, 207, 209, 208. Screening dan opsi dropdown di awal, validasi nilai filter sesudahnya. TC-GS-FILEMGR-208 diletakkan terakhir karena satu-satunya yang bergantung pada tanggal relatif terhadap waktu uji.
- Panjang spec: 38 langkah, sedikit di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok berkelas sama (filter satu panel, satu dataset Tabel A3, tanpa aksi tulis), setiap blok memulai dari `[Clear Field]` sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya menambah buka modal dan login ulang tanpa pemisah nyata (bagian 3, ukuran batas spec).
- Anchor: langkah 2 membuktikan tabel Recycle Bin termuat (pembanding sedikitnya satu baris) sebelum asersi universal "hanya ...". Langkah 30 memakai empty state "No results found" sebagai anchor positif sah untuk absence.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14, 16, 19, 22, 25, 27, 29, 31, 35 (membersihkan filter dari blok sebelumnya atau menutup dropdown). Filter Panel diasumsikan tetap terbuka setelah `[Apply]` mengikuti langkah TC (TC langsung memakai `[Clear Field]` setelah `[Apply]`).
- Temuan untuk QA:
  - TC-GS-FILEMGR-205 butir b ("opsi tidak berasal dari file aktif di tabel utama") tidak dapat dibedakan dari butir a pada data Pre-setup, karena Tabel A2 dan A3 memuat himpunan format yang sama (JPG, PNG, JPEG). Langkah 13 mengikuti TC tetapi tidak membuktikan sumber opsi; perlu data file aktif berformat di luar Recycle Bin bila butir ini harus teruji.
  - TC tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`; spec mengikuti langkah TC (langsung `[Clear Field]`). Perlu konfirmasi perilaku panel agar skrip menulis langkah buka-ulang yang benar.
  - Nilai Size 700 KB dan 2048 KB pada TC-GS-FILEMGR-207 diturunkan dari byte Tabel A3 (716.800 dan 2.097.152 byte) dan tidak ada di PRD (Q-14); aritmetika konsisten.
  - Baris `due-photo.png` (sekarang − 31 hari) tampil sampai job auto-purge berikutnya; bila job berjalan antara seeding dan asersi, langkah 21, 26 menjadi tidak stabil (Q-3).
  - Mekanisme dan endpoint seeding Tabel A3 tidak didefinisikan di TC (Q-4); hitungan baris mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
