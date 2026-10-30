---
id: TC-GS-FILEMGR-E2E-062-tenant-write-lockdown-suspended-expired
title: "State Tenant: Aksi Tulis Ditolak saat Client Suspended atau Expired"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-244
  - TC-GS-FILEMGR-245
  - TC-GS-FILEMGR-246
coverage:
  web: automated
---

# State Tenant: Aksi Tulis Ditolak saat Client Suspended atau Expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah status Client uji. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE; akun pengubah status Client tidak disebut di TC, PRD, atau LLD, lihat Temuan untuk QA): mengubah status Client uji menjadi Suspended dan Expired, dengan halaman File Manager sudah terbuka (tanpa memuat ulang).
- State global yang diubah: status Client uji. Hook `after` (tetap jalan walau spec gagal di tengah) mengembalikan status ke Active.
- Data milik spec (suffix `{runId}-062`, seeding lewat fixture BE di hook `before`; mekanisme seeding disediakan tim FE/BE). Tidak ada data yang berubah karena semua aksi tulis ditolak:
  - `siti-profile-{runId}-062.png` (salinan F02), file aktif, dipakai TC-244.
  - `legacy-photo-{runId}-062.jpeg` (salinan R02) di Recycle Bin, dipakai TC-245.
  - `staff-photo-10-{runId}-062.jpg` dan `staff-photo-11-{runId}-062.jpg` (salinan F18 dan F19), file aktif, dipakai TC-246.
- Baseline log: nama file bersuffix unik, sehingga jumlah entri awal untuk semua nama di atas adalah nol di Changelog File Manager.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): kembalikan status Client ke Active, hapus permanen lewat API file bersuffix `{runId}-062`.

## Test Steps

### Client Suspended

1. Ubah status Client uji menjadi Suspended tanpa memuat ulang halaman File Manager
2. Ketik Search `{runId}-062`, tekan Enter

#### TC-GS-FILEMGR-244: Delete single ditolak (Suspended)

3. Klik ikon (⋯) baris `siti-profile-{runId}-062.png`, lalu klik `Delete`
4. Klik [Delete] pada dialog
5. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
6. Tutup toast error
7. Verifikasi `siti-profile-{runId}-062.png` tetap di tabel utama

#### TC-GS-FILEMGR-245: Permanently Delete single ditolak (Suspended)

8. Klik tombol Recycle Bin di toolbar, ketik Search `legacy-photo-{runId}-062`, tekan Enter
9. Klik ikon (⋯) baris `legacy-photo-{runId}-062.jpeg`, lalu klik `Permanently Delete`
10. Klik [Permanently Delete] pada dialog
11. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
12. Tutup toast error
13. Verifikasi `legacy-photo-{runId}-062.jpeg` tetap di Recycle Bin
14. Tutup modal Recycle Bin lewat `✕`

#### TC-GS-FILEMGR-246: Bulk Delete ditolak (Suspended)

15. Centang baris `staff-photo-10-{runId}-062.jpg` dan `staff-photo-11-{runId}-062.jpg`
16. Klik `Bulk Action`, klik `Delete`, lalu klik [Delete] pada dialog
17. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
18. Tutup toast error
19. Verifikasi `staff-photo-10-{runId}-062.jpg` dan `staff-photo-11-{runId}-062.jpg` tetap di tabel utama
20. Hapus centang kedua baris

#### Log (Suspended)

21. Klik ikon Changelog di toolbar, ketik Search `{runId}-062`, tekan Enter
22. Verifikasi Changelog File Manager tidak memuat entri baru untuk file bersuffix `{runId}-062` (empty state "No results found")
23. Tutup modal Changelog lewat `✕`

### Client Expired

24. Ubah status Client uji menjadi Expired tanpa memuat ulang halaman File Manager

#### TC-GS-FILEMGR-244 butir c: Delete single ditolak (Expired)

25. Klik ikon (⋯) baris `siti-profile-{runId}-062.png`, lalu klik `Delete`
26. Klik [Delete] pada dialog
27. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
28. Tutup toast error
29. Verifikasi `siti-profile-{runId}-062.png` tetap di tabel utama

#### TC-GS-FILEMGR-245 butir c: Permanently Delete single ditolak (Expired)

30. Klik tombol Recycle Bin di toolbar, ketik Search `legacy-photo-{runId}-062`, tekan Enter
31. Klik ikon (⋯) baris `legacy-photo-{runId}-062.jpeg`, lalu klik `Permanently Delete`
32. Klik [Permanently Delete] pada dialog
33. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
34. Tutup toast error
35. Verifikasi `legacy-photo-{runId}-062.jpeg` tetap di Recycle Bin
36. Tutup modal Recycle Bin lewat `✕`

#### Log (Expired)

37. Klik ikon Changelog di toolbar, ketik Search `{runId}-062`, tekan Enter
38. Verifikasi Changelog File Manager tidak memuat entri baru untuk file bersuffix `{runId}-062` (empty state "No results found")

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas state tenant (prinsip 13h): write-lockdown dipisah dari verifikasi baca, yang ada di spec `TC-GS-FILEMGR-E2E-063-tenant-baca-tetap-tersedia`. Semua aksi ditolak sehingga tidak ada data terhapus atau berubah.
- Urutan TC di spec dikelompokkan menurut status Client (Suspended: 244, 245, 246; lalu Expired: butir c 244 dan 245) agar status hanya diubah dua kali. Search `{runId}-062` pada langkah 2 mempertahankan baris milik spec tampil di halaman aktif; Search ini tidak ditulis di Langkah Uji TC sumber.
- Jumlah langkah 38 nominal, di atas sekitar 35 langkah; semua blok satu kelas (state tenant), berdiri sendiri, dan kegagalan satu blok tidak menghilangkan makna blok lain. Blok Expired mengulang TC-244 dan TC-245 sesuai Expected butir c TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 24 (prasyarat status Client dijadikan langkah eksplisit), langkah 2 (Search), langkah 6, 12, 18, 28, 34 (menutup toast error persisten sebelum asersi toast berikutnya, S-09), langkah 14, 20, 23, 36 (menutup modal dan menghapus centang), langkah 21 dan 37 (membuka Changelog dengan Search).
- Asersi "tidak ada entri log baru" (langkah 22 dan 38) memakai baseline nol karena nama file bersuffix unik, dengan anchor positif toast penolakan dan baris file yang tetap ada (langkah 5, 7, 11, 13, 17, 19, 27, 29, 33, 35); satu pengecekan Changelog per status, dikonsolidasikan untuk TC-244 dan TC-245 (dan TC-246 untuk Suspended). Keputusan D-1 opsi B: tidak ada spec absence terpisah; P-1 (state berat: status Client yang diubah pada langkah 1 dan 24 dibangun sebelum aksi tulis).
- Temuan untuk QA:
  - Akun dan mekanisme pengubah status Client tidak disebut TC, PRD, atau LLD (S-13); ditulis sebagai kemampuan yang disediakan tim FE.
  - Status Client diubah saat sesi Total Control sudah aktif; apakah sesi tetap valid setelah status berubah adalah asumsi TC.
  - TC-244/245 tidak menyebut surface log yang dicek untuk "tidak ada entri log baru"; spec memeriksa Changelog File Manager.
  - TC-246 hanya mensyaratkan Suspended; Expired tidak diuji untuk Bulk Delete.
