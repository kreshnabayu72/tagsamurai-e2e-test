---
id: TC-GS-POS-E2E-053-multi-konteks-sinkron-realtime-tanpa-reload
title: "Multi-Konteks: Record Baru, Terhapus, dan Rename dari Sesi Lain Tanpa Muat Ulang serta Popup Edit Tidak Ter-refresh"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-175
  - TC-GS-POS-176
  - TC-GS-POS-278
  - TC-GS-POS-279
  - TC-GS-POS-297
coverage:
  web: automated
---

# Multi-Konteks: Record Baru, Terhapus, dan Rename dari Sesi Lain Tanpa Muat Ulang serta Popup Edit Tidak Ter-refresh

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun Sesi A (Admin A): Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (Admin B): Admin B Total Control (Andi Wijaya) `superAdminGlobalSettingsB_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`.
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` dan berada di Global Settings > User > Position pada entitas yang sama, tanpa Search atau Filter. Password tidak ditulis di spec atau fixture.
- Data Dinamis seeding lewat API di hook `before` (bersuffix per run, bebas relasi): `Training Coordinator {runId}-053` (TC-GS-POS-176; nama hasil `Training Lead {runId}-053`) dan `Marketing Manager {runId}-053` (TC-GS-POS-297; nama antara `Marketing Director {runId}-053`, nama akhir `Marketing Head {runId}-053`).
- Data Dinamis yang dibuat langkah spec oleh Sesi B: `Warehouse Clerk {runId}-053` (TC-GS-POS-175) dan `Quality Inspector {runId}-053` (TC-GS-POS-278, dihapus Sesi B di TC-GS-POS-279).
- Search `Coordinator` pada TC-GS-POS-175 dan TC-GS-POS-176 dapat menampilkan baris Position lain yang memuat `Coordinator` (mis. Pre-setup 16 `Sales Coordinator`) selain data spec ini; baris itu tidak diubah spec ini, dan total hasil Search `Coordinator` tidak lebih dari 10 baris sehingga muat satu halaman (ukuran halaman default 10).
- Total Position entitas tidak melebihi 100 supaya seluruh baris muat satu halaman pada ukuran halaman 100 (langkah 17, TC-GS-POS-278 dan TC-GS-POS-279).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` untuk akun aktor spec ini (Sesi A dan Sesi B) dan hook `after` memulihkannya; lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-053` yang masih ada (`Training Coordinator`, `Training Lead`, `Warehouse Clerk`, `Quality Inspector`, `Marketing Manager`, `Marketing Director`, `Marketing Head`); pulihkan ukuran halaman tabel Sesi A ke 10; tutup konteks Sesi B; kembalikan sesi ke akun default suite.
- Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > User > Position; layar awal dibuka di hook ini sehingga `## Test Steps` tidak mengulang langkah buka.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; pengamatan tabel Sesi A tanpa memuat ulang halaman selama jeda sinkronisasi realtime; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- State global yang diubah: tidak ada selain Position milik spec, dan ukuran halaman tabel Sesi A (dipulihkan pada langkah 33).

## Test Steps

### TC-GS-POS-175: Record baru dari sesi lain yang tidak cocok Search tidak muncul di tabel tersaring

1. [Sesi A] Ketik `Coordinator` pada Search tabel lalu tekan Enter
2. [Sesi A] Verifikasi tabel menampilkan baris `Training Coordinator {runId}-053`
3. [Sesi B] Klik `[+ Position]`
4. [Sesi B] Ketik `Warehouse Clerk {runId}-053` pada field Position Name
5. [Sesi B] Klik `[Submit]`
6. [Sesi B] Tunggu hingga Create selesai (toast sukses tampil)
7. [Sesi A] Amati tabel selama jeda sinkronisasi realtime tanpa memuat ulang halaman
8. [Sesi A] Verifikasi baris `Warehouse Clerk {runId}-053` tidak muncul di tabel yang masih tersaring `Coordinator`

### TC-GS-POS-176: Rename yang tidak lagi cocok Search menghilangkan baris dari tampilan

9. [Sesi A] Ganti isi kotak search tabel dengan `Coordinator`, tekan Enter
10. [Sesi A] Klik `⋯` pada baris `Training Coordinator {runId}-053`, pilih `Edit`
11. [Sesi A] Ganti isi field Position Name menjadi `Training Lead {runId}-053`
12. [Sesi A] Klik `[Save]`
13. [Sesi A] Verifikasi toast sukses: "Success, position has been updated."
14. [Sesi A] Verifikasi baris `Training Coordinator {runId}-053` tidak tampil di hasil Search `Coordinator`
15. [Sesi A] Verifikasi baris `Training Lead {runId}-053` tidak tampil di hasil Search `Coordinator`

### TC-GS-POS-278: Record baru dari sesi lain muncul tanpa reload

16. [Sesi A] Klik `←` pada kotak Search tabel (menutup input dan mereset tabel)
17. [Sesi A] Atur ukuran halaman tabel ke 100
18. [Sesi A] Catat nomor halaman aktif tabel
19. [Sesi B] Klik `[+ Position]`
20. [Sesi B] Ketik `Quality Inspector {runId}-053` pada field Position Name
21. [Sesi B] Klik `[Submit]`
22. [Sesi B] Tunggu hingga Create selesai (toast sukses tampil)
23. [Sesi A] Amati tabel selama jeda sinkronisasi realtime tanpa memuat ulang halaman
24. [Sesi A] Verifikasi baris `Quality Inspector {runId}-053` muncul di tabel tanpa memuat ulang halaman
25. [Sesi A] Verifikasi baris `Quality Inspector {runId}-053` berada pada posisi urutan Name A-Z di antara baris bertetangga
26. [Sesi A] Verifikasi halaman aktif tabel sama dengan yang dicatat pada langkah 18

### TC-GS-POS-279: Record yang dihapus dari sesi lain hilang tanpa reload

27. [Sesi B] Ketik `Quality Inspector {runId}-053` pada Search tabel lalu tekan Enter
28. [Sesi B] Klik `⋯` pada baris `Quality Inspector {runId}-053`, pilih `Delete`
29. [Sesi B] Klik `[Delete]` pada Dialog Delete Position
30. [Sesi B] Tunggu hingga Delete selesai (toast sukses tampil)
31. [Sesi A] Amati tabel selama jeda sinkronisasi realtime tanpa memuat ulang halaman
32. [Sesi A] Verifikasi baris `Quality Inspector {runId}-053` hilang dari tabel tanpa memuat ulang halaman
33. [Sesi A] Atur ukuran halaman tabel kembali ke 10

### TC-GS-POS-297: Popup Edit yang terbuka tidak di-refresh oleh rename dari sesi lain

34. [Sesi A] Ketik `Marketing Manager {runId}-053` pada Search tabel lalu tekan Enter
35. [Sesi A] Klik `⋯` pada baris `Marketing Manager {runId}-053`, pilih `Edit`
36. [Sesi A] Ganti isi field Position Name menjadi `Marketing Head {runId}-053`
37. [Sesi B] Ganti isi kotak search tabel dengan `Marketing Manager {runId}-053`, tekan Enter
38. [Sesi B] Klik `⋯` pada baris `Marketing Manager {runId}-053`, pilih `Edit`
39. [Sesi B] Ganti isi field Position Name menjadi `Marketing Director {runId}-053`
40. [Sesi B] Klik `[Save]`
41. [Sesi B] Tunggu hingga Save selesai (toast sukses tampil)
42. [Sesi A] Amati Popup Edit Position selama jeda sinkronisasi realtime tanpa aksi apa pun
43. [Sesi A] Verifikasi Popup Edit Position tidak berubah
44. [Sesi A] Verifikasi tidak ada dialog interupsi
45. [Sesi A] Verifikasi input `Marketing Head {runId}-053` dipertahankan pada field Position Name
46. [Sesi A] Klik `[Save]`
47. [Sesi A] Verifikasi toast sukses: "Success, position has been updated."
48. [Sesi A] Ganti isi kotak search tabel dengan `Marketing Head {runId}-053`, tekan Enter
49. [Sesi A] Verifikasi baris `Marketing Head {runId}-053` ada di tabel sebagai nilai akhir

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Kelas harness: multi-konteks (dua sesi admin), bagian 3 prinsip 13c. Spec serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 49 langkah (di atas smell sekitar 35 langkah). Alasan: seluruh blok satu kelas harness (dua sesi admin pada entitas yang sama), tiap blok memakai Position bersuffix sendiri (kecuali TC-GS-POS-279, yang memakai record yang dibuat TC-GS-POS-278 sehingga kehilangan makna bila langkah pembuatan di TC-GS-POS-278 gagal keras), dan kegagalan blok lain tidak menghilangkan makna blok TC-GS-POS-175, 176, 278, dan 297; jumlah langkah muncul dari satu baris per aksi per sesi dan satu `Verifikasi` per klausa Expected.
- Urutan TC sumber dipertahankan. TC-GS-POS-279 memakai `Quality Inspector {runId}-053` yang dibuat Sesi B pada TC-GS-POS-278 (langkah 19 sampai 22) dan dibuktikan tampil di Sesi A pada langkah 24; langkah TC-GS-POS-278 itu sudah memuat langkah dependensi sehingga tidak dirujuk ulang. TC-GS-POS-279 yang menghapus data hanya menghapus record milik blok itu.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 22, 30, dan 41 (menunggu aksi Sesi B selesai); langkah 7, 23, 31, dan 42 (mengamati tanpa aksi selama jeda sinkronisasi); langkah 9 (Search `Coordinator` diulang supaya state tabel Sesi A eksplisit; kotak sudah berisi sehingga isinya diganti); langkah 16 sampai 18 dan 33 (menutup input Search dan mereset tabel, mengatur dan memulihkan ukuran halaman, mencatat halaman aktif); langkah 27 (Sesi B mencari record yang akan dihapus); langkah 34 (mencari baris `Marketing Manager {runId}-053` agar Sesi A dapat membuka Edit); langkah 37 dan 48 (kotak search sudah berisi sehingga isinya diganti).
- Langkah 14 (`Verifikasi` baris `Training Coordinator {runId}-053` tidak tampil di hasil Search `Coordinator`) memakai toast sukses langkah 13 sebagai anchor (butir 2 konvensi 8b); langkah 15 mengasersi nama baru `Training Lead {runId}-053` tidak tampil karena namanya tidak cocok `Coordinator`. Keduanya klausa Expected b TC-GS-POS-176.
- Langkah 2 (`Verifikasi` baris `Training Coordinator {runId}-053` tampil di hasil Search) adalah anchor positif bahwa tabel Sesi A tersaring dan data spec ini ada sebelum Sesi B bertindak; tidak ada di Expected TC-GS-POS-175.
- Langkah 17 (ukuran halaman 100) dan langkah 18 (mencatat halaman aktif) menjadikan posisi urutan Name A-Z pada langkah 25 dapat diamati dalam satu halaman tanpa berpindah halaman.
- Pembagian TC lintas spec: TC-GS-POS-175 dan TC-GS-POS-176 ada di spec ini; TC-GS-POS-109, 118, 119, 147, 148, 271, dan 300 ada di spec 052.
- Temuan untuk QA:
  - Post Condition TC-GS-POS-297 ("Changelog mencatat 2 entri Edit terpisah") tidak punya langkah observasi di TC; tidak diasersi.
  - TC-GS-POS-278 dan TC-GS-POS-279 tidak menyebut cara Sesi A menjangkau halaman tempat posisi A-Z record baru berada pada tabel yang berisi banyak Position; spec memakai ukuran halaman 100 dan mensyaratkan total Position di bawah 100. Bila total melebihi 100, asersi posisi perlu cara navigasi lain.
  - TC-GS-POS-175 butir "tanpa reload" tidak menyebut durasi pengamatan; spec memakai "jeda sinkronisasi realtime" tanpa angka.
  - TC-GS-POS-297 langkah 1 menulis "mengetik `Marketing Head`" pada field yang sudah berisi `Marketing Manager`; spec menuliskannya sebagai mengganti isi field.
  - TC-GS-POS-176 tidak menyebut sesi; spec menjalankannya di Sesi A.
  - Sesi B pada TC-GS-POS-175, 278, 279, dan 297 memakai sesi UI mengikuti TC, padahal hanya memicu state; konvensi P-2 meminta pelaku kedua semacam itu memakai sesi API. Perlu konfirmasi QA sebelum langkah itu dipindah ke sesi API yang disediakan tim FE/BE.
