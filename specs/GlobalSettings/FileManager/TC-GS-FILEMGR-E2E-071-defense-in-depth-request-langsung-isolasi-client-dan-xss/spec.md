---
id: TC-GS-FILEMGR-E2E-071-defense-in-depth-request-langsung-isolasi-client-dan-xss
title: "Defense-in-Depth: Request Langsung Tanpa Capability, Isolasi ID Client Lain, dan Nama File Berisi Markup"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-248
  - TC-GS-FILEMGR-249
  - TC-GS-FILEMGR-250
  - TC-GS-FILEMGR-251
  - TC-GS-FILEMGR-252
  - TC-GS-FILEMGR-253
  - TC-GS-FILEMGR-282
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Tanpa Capability, Isolasi ID Client Lain, dan Nama File Berisi Markup

## Prerequisites

- Mode: FE+BE (klien HTTP untuk request langsung ke server; kelas defense-in-depth).
- Akun yang dipakai (login UI hanya untuk Total Control; akun lain hanya lewat sesi API klien HTTP):

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Aktor UI (hook `before`) dan sesi Total Control untuk TC-251, TC-252 | Total Control Sinta Maharani (`Sinta M`) | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Sesi request TC-248 | Read Only Rina Pratiwi | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_RO_PASSWORD` |
  | Sesi request TC-249 | Manage files: Read Doni Saputra | `manageFilesRead_automated_{namaCompany}@qwertysystem.net` | `GS_FILES_READ_PASSWORD` |
  | Sesi request TC-250, TC-282 | Tanpa akses File Manager Lina Marlina | `noAccessGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_NOACCESS_PASSWORD` |

  Akun aktor UI adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`, `GS_RO_PASSWORD`, `GS_FILES_READ_PASSWORD`, `GS_NOACCESS_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah laporan Storage (TC-282). Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE; endpoint dan mekanisme tidak didefinisikan di TC, lihat Temuan untuk QA):
  - Klien HTTP yang mengirim request ke API File Manager (list file aktif, Delete, Permanently Delete, pembacaan/unduh file lewat token, pembacaan Storage Usage) dengan sesi tiap akun pada tabel di atas dan membaca status serta isi respons.
  - Seeding file di client lain (`outsider-photo-{runId}-071.jpg` aktif dan `outsider-old-{runId}-071.png` di Recycle Bin) serta token terenkripsi (memuat client id dan file id) untuk file client lain dan untuk ID file yang tidak pernah ada, dan pembacaan state file client lain.
  - Seeding laporan Storage skenario S1 (Tabel A5) untuk TC-282.
- Data milik spec (suffix `{runId}-071`, seeding lewat fixture BE di hook `before`; Pre-setup bersama tidak dipakai sebagai target request karena request yang diuji ditolak juga memakai data milik spec, S-06):
  - `budi-avatar-{runId}-071.jpg` (salinan F01), file aktif, dipakai TC-248.
  - `old-avatar-{runId}-071.png` (salinan R01) di Recycle Bin, dipakai TC-249.
  - `<img src=x onerror=alert(1)>-{runId}-071.jpg`, file aktif (fixture BE), dipakai TC-253.
- Baseline log: nama file bersuffix unik, sehingga jumlah entri awal Changelog File Manager untuk nama-nama di atas dan `outsider` adalah nol.
- State global yang diubah: laporan Storage Client uji (TC-282). Hook `after` memulihkan laporan Storage awal.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus permanen lewat API file bersuffix `{runId}-071` yang masih ada; hapus file client lain yang di-seed.

## Test Steps

### TC-GS-FILEMGR-250: Request list langsung oleh akun tanpa akses ditolak

1. Kirim request list file aktif langsung ke API File Manager memakai sesi Lina Marlina (tanpa akses File Manager)
2. Verifikasi respons server berstatus 403 Forbidden
3. Verifikasi respons tidak memuat data file

### TC-GS-FILEMGR-282: Server menolak pembacaan Storage Usage tanpa akses

4. Siapkan laporan Storage skenario S1 lewat fixture BE
5. Panggil endpoint pembacaan Storage Usage langsung memakai sesi Lina Marlina
6. Verifikasi respons server berstatus 403
7. Verifikasi respons tidak memuat angka Storage apa pun

### TC-GS-FILEMGR-248: Request Delete langsung oleh Read Only ditolak

8. Kirim request Delete file `budi-avatar-{runId}-071.jpg` langsung ke API File Manager memakai sesi Rina Pratiwi (Read Only)
9. Verifikasi respons server berstatus 403 Forbidden
10. Muat ulang tabel utama File Manager dan ketik Search `budi-avatar-{runId}-071`, tekan Enter
11. Verifikasi `budi-avatar-{runId}-071.jpg` tetap di tabel utama
12. Klik tombol Recycle Bin di toolbar, ketik Search `budi-avatar-{runId}-071`, tekan Enter
13. Verifikasi `budi-avatar-{runId}-071.jpg` tidak ada di Recycle Bin (empty state "No results found")
14. Tutup modal Recycle Bin lewat `✕`, klik ikon Changelog di toolbar, ketik Search `budi-avatar-{runId}-071`, tekan Enter
15. Verifikasi Changelog File Manager tidak memuat entri baru untuk `budi-avatar-{runId}-071.jpg` (empty state "No results found")
16. Tutup modal Changelog lewat `✕`

### TC-GS-FILEMGR-249: Request Permanently Delete langsung oleh Manage files: Read ditolak

17. Kirim request Permanently Delete file `old-avatar-{runId}-071.png` langsung ke API File Manager memakai sesi Doni Saputra (Manage files: Read)
18. Verifikasi respons server berstatus 403 Forbidden
19. Klik tombol Recycle Bin di toolbar, ketik Search `old-avatar-{runId}-071`, tekan Enter
20. Verifikasi `old-avatar-{runId}-071.png` tetap di Recycle Bin
21. Tutup modal Recycle Bin lewat `✕`, klik ikon Changelog di toolbar, ketik Search `old-avatar-{runId}-071`, tekan Enter
22. Verifikasi Changelog File Manager tidak memuat entri baru untuk `old-avatar-{runId}-071.png` (empty state "No results found")
23. Tutup modal Changelog lewat `✕`

### TC-GS-FILEMGR-251: Delete dan Permanently Delete atas ID client lain diperlakukan sebagai tidak ditemukan

24. Kirim request Delete untuk ID `outsider-photo-{runId}-071.jpg` langsung ke API memakai sesi Total Control Sinta Maharani
25. Kirim request Permanently Delete untuk ID `outsider-old-{runId}-071.png` memakai sesi yang sama
26. Kirim request Delete untuk ID file yang tidak pernah ada memakai sesi yang sama
27. Verifikasi respons Delete untuk ID client lain (langkah 24) identik dengan respons Delete untuk ID yang tidak pernah ada (langkah 26)
28. Verifikasi respons Permanently Delete untuk ID client lain (langkah 25) identik dengan respons untuk ID yang tidak pernah ada (langkah 26)
29. Verifikasi file milik client lain tidak berubah (`outsider-photo-{runId}-071.jpg` tetap aktif dan `outsider-old-{runId}-071.png` tetap di Recycle Bin, dibaca lewat fixture BE)
30. Klik ikon Changelog di toolbar, ketik Search `outsider`, tekan Enter
31. Verifikasi Changelog File Manager client ini tidak memuat entri log untuk file client lain (empty state "No results found")
32. Tutup modal Changelog lewat `✕`

### TC-GS-FILEMGR-252: Preview dan Download atas ID client lain diperlakukan sebagai tidak ditemukan

33. Kirim request pembacaan/unduh memakai token terenkripsi yang memuat ID `outsider-photo-{runId}-071.jpg` (file client lain) langsung ke API memakai sesi Total Control Sinta Maharani
34. Kirim request memakai token terenkripsi yang memuat ID file yang tidak pernah ada
35. Verifikasi respons langkah 33 berstatus 404 dengan pesan `File not found`
36. Verifikasi respons langkah 33 identik dengan respons langkah 34
37. Verifikasi isi file client lain tidak terkirim pada respons langkah 33

### TC-GS-FILEMGR-253: Nama file berisi markup ditampilkan sebagai teks

38. Ketik Search `onerror=alert(1)` pada tabel utama, tekan Enter
39. Verifikasi kolom File Name menampilkan teks `<img src=x onerror=alert(1)>-{runId}-071.jpg` apa adanya
40. Verifikasi tidak ada gambar yang dirender pada kolom File Name
41. Klik ikon (⋯) baris tersebut, klik `Delete`, dan amati dialog
42. Verifikasi dialog Delete menampilkan nama `<img src=x onerror=alert(1)>-{runId}-071.jpg` sebagai teks
43. Verifikasi tidak ada dialog skrip yang muncul
44. Klik [Cancel] pada dialog Delete

## Notes

- Mode: FE+BE dengan klien HTTP. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas defense-in-depth (prinsip 13a) tanpa harness eksternal. Keputusan D-2: TC request-langsung (248 sampai 252, 282) tetap di E2E.
- Urutan TC di spec berbeda dari sumber: TC tanpa data seed lebih dulu (250, 282), lalu penolakan capability (248, 249), isolasi client (251, 252), dan terakhir TC-253 yang membuka dialog Delete (tidak menghabiskan data karena [Cancel]).
- Langkah request langsung hanya mengasersi respons server dan state data (bagian 8b butir 1). Perilaku FE yang ditulis TC tidak diasersi: TC-282 butir a ("toast baku 'You don't have permission to do this.' bila dipicu dari UI") tidak diasersi di spec ini.
- Spec berjumlah 44 langkah nominal, di atas sekitar 35 langkah. Semua blok satu kelas (defense-in-depth), berdiri sendiri, dan kegagalan satu blok tidak menghilangkan makna blok lain; langkah verifikasi state data (langkah 10 sampai 16, 19 sampai 23, 29 sampai 32) memakai pola Search, empty state, dan tutup modal yang berulang.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 (precondition fixture S1), langkah 10, 12, 14, 19, 21, 30, 38 (Search nama bersuffix atau membuka surface), langkah 16, 21, 23, 32, 44 (menutup modal atau dialog), langkah 44 memakai [Cancel] karena dialog konfirmasi Delete punya [Cancel].
- Pengecekan state TC-248 dan TC-249 ("buka File Manager lalu muat ulang tabel") dilakukan lewat sesi UI Total Control (hook `before`), bukan sesi Read Only atau Manage files: Read; sesi itu hanya memicu request (P-2). Asersi "tidak ada entri log baru" (langkah 15, 22, 31) memakai baseline nol karena nama bersuffix unik, dengan anchor positif status 403 (atau respons) dan baris file yang tetap ada (langkah 9, 11, 18, 20, 27 sampai 29). Keputusan D-1 opsi B: tidak ada spec absence terpisah; P-1 tidak dipakai karena tidak ada state berat.
- Temuan untuk QA:
  - Endpoint, format token terenkripsi, dan mekanisme seeding file client lain tidak didefinisikan di TC (Q-4); ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-282 mencampur perilaku server dan UI ("403 dan toast baku bila dipicu dari UI", Q-12); spec hanya mengasersi respons server. Jalur UI untuk toast tersebut belum punya TC sendiri.
  - TC-251 langkah 3 hanya mengirim Delete untuk ID yang tidak pernah ada; perbandingan Permanently Delete (langkah 28) memakai respons itu sebagai acuan, padahal endpoint Delete dan Permanently Delete bisa berbeda; usulan TC tambahan: request Permanently Delete untuk ID yang tidak pernah ada.
  - TC-248, TC-249, TC-251 menyebut "tidak ada entri log baru" tanpa surface log; spec memeriksa Changelog File Manager.
