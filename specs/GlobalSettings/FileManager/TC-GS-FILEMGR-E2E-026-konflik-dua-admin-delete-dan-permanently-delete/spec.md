---
id: TC-GS-FILEMGR-E2E-026-konflik-dua-admin-delete-dan-permanently-delete
title: "Konflik Dua Admin: Delete dan Permanently Delete File yang Sama Bersamaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-255
  - TC-GS-FILEMGR-256
coverage:
  web: automated
---

# Konflik Dua Admin: Delete dan Permanently Delete File yang Sama Bersamaan

## Prerequisites

- Mode: FE+BE (kelas multi-konteks: dua sesi UI paralel; hasil di kedua sesi diasersi).
- Akun Sesi Sinta (admin utama): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`.
- Akun Sesi Agus (admin kedua): Manage files: Delete Agus Wibowo `manageFilesDelete_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_FILES_DELETE_PASSWORD`. Login di hook `before` pada konteks browser terpisah. Nama env `GS_TC_PASSWORD` dan `GS_FILES_DELETE_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` menutup konteks Sesi Agus dan mengembalikan sesi ke akun default suite.
- Dua sesi browser: keduanya berada di Global Settings > File Manager sebelum langkah pertama (TC-GS-FILEMGR-255) lalu membuka modal Recycle Bin (TC-GS-FILEMGR-256). Kedua sesi mengasersi hasilnya sehingga keduanya sesi UI (bukan sesi API).
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run, dihapus oleh spec ini; pemilik adalah user klon milik spec): `staff-photo-12-{runId}-026.jpg` (JPG, foto profil aktif, TC-GS-FILEMGR-255), `recycled-photo-12-{runId}-026.jpg` (JPG, di Recycle Bin, TC-GS-FILEMGR-256).
- Kemampuan teknis (disediakan tim FE/BE): dua konteks browser paralel dalam satu spec dengan penanda `[Sesi Sinta]` dan `[Sesi Agus]`; seeding file dengan pemilik klon; membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`); jam server dan jam browser sinkron (S-12).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen sisa file seed, hapus user klon, tutup konteks Sesi Agus.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-255: Dua admin menghapus file yang sama bersamaan

1. [Sesi Sinta] Ketik Search `staff-photo-12-{runId}-026`, tekan Enter
2. [Sesi Agus] Ketik Search `staff-photo-12-{runId}-026`, tekan Enter
3. [Sesi Sinta] Klik ikon `⋯` baris `staff-photo-12-{runId}-026.jpg`, lalu klik `Delete` (dialog Delete terbuka)
4. [Sesi Agus] Klik ikon `⋯` baris `staff-photo-12-{runId}-026.jpg`, lalu klik `Delete` (dialog Delete terbuka)
5. [Sesi Sinta] Klik [Delete] pada dialog
6. [Sesi Sinta] Verifikasi toast sukses: "Success, staff-photo-12-{runId}-026.jpg has been deleted."
7. [Sesi Agus] Klik [Delete] pada dialog
8. [Sesi Agus] Verifikasi toast info: "This file is no longer available."
9. [Sesi Agus] Verifikasi tabel di-refresh
10. [Sesi Sinta] Buka modal Recycle Bin, ketik Search `staff-photo-12-{runId}-026`, tekan Enter
11. [Sesi Sinta] Verifikasi `staff-photo-12-{runId}-026.jpg` tampil satu kali di Recycle Bin dengan Deleted By `Sinta M`
12. [Sesi Sinta] Tutup modal Recycle Bin dengan `✕` di header
13. [Sesi Sinta] Klik ikon Changelog di toolbar, ketik Search `staff-photo-12-{runId}-026`, tekan Enter
14. [Sesi Sinta] Verifikasi jumlah entri Action `Delete` untuk `staff-photo-12-{runId}-026.jpg` tepat satu (baseline ditambah satu)
15. [Sesi Sinta] Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-256: Dua admin menghapus permanen file yang sama bersamaan

16. [Sesi Sinta] Buka modal Recycle Bin, ketik Search `recycled-photo-12-{runId}-026`, tekan Enter
17. [Sesi Agus] Buka modal Recycle Bin, ketik Search `recycled-photo-12-{runId}-026`, tekan Enter
18. [Sesi Sinta] Klik ikon `⋯` baris `recycled-photo-12-{runId}-026.jpg`, lalu klik `Permanently Delete` (dialog terbuka)
19. [Sesi Agus] Klik ikon `⋯` baris `recycled-photo-12-{runId}-026.jpg`, lalu klik `Permanently Delete` (dialog terbuka)
20. [Sesi Sinta] Klik [Permanently Delete] pada dialog
21. [Sesi Sinta] Verifikasi toast sukses: "Success, recycled-photo-12-{runId}-026.jpg has been permanently deleted."
22. [Sesi Agus] Klik [Permanently Delete] pada dialog
23. [Sesi Agus] Verifikasi toast info: "This file is no longer available."
24. [Sesi Agus] Verifikasi Recycle Bin di-refresh
25. [Sesi Sinta] Tutup modal Recycle Bin dengan `✕` di header, lalu klik ikon Changelog di toolbar
26. [Sesi Sinta] Ketik Search `recycled-photo-12-{runId}-026`, tekan Enter
27. [Sesi Sinta] Verifikasi jumlah entri Action `Permanently Delete` untuk `recycled-photo-12-{runId}-026.jpg` tepat satu (baseline ditambah satu)

## Notes

- Mode: FE+BE. Kelas c multi-konteks (dua admin, dua sesi UI). Spec memakai dua akun dengan penanda sesi eksplisit; bagian sesi Agus tetap bermakna karena kedua TC mengasersi keluaran kedua sesi. Subjudul `###` memetakan langkah ke id TC granular.
- Aksi menghabisi data (Delete dan Permanently Delete) hanya dilakukan pada file milik spec.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 2, 16, 17 (membuka modal dan Search untuk menemukan baris target), 10, 12, 13, 15, 25, 26 (membuka dan menutup modal Recycle Bin dan Changelog untuk memeriksa hasil).
- Urutan klik mengikuti TC sumber: dialog dibuka di kedua sesi lebih dulu, lalu konfirmasi Sesi Sinta, lalu konfirmasi Sesi Agus (S-04).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Temuan untuk QA:
  - Q-4: TC-GS-FILEMGR-255 dan 256 bertanda "Manual Only (d) dua sesi paralel", tetapi kemampuan dua konteks browser dicatat di Prerequisites sebagai kebutuhan resmi (bagian 2 konvensi, hambatan teknis bukan alasan mengeluarkan TC). Akun Agus Wibowo (Manage files: Delete) hanya login dan tidak diubah (Q-5 tidak berlaku).
  - Q-5/Q-7: TC menargetkan baris Pre-setup F20 `staff-photo-12.jpg` dan R16 `recycled-photo-12.jpg`; spec memakai file bersuffix dengan pemilik klon.
  - TC-GS-FILEMGR-255 Expected c ("tepat satu entri log Delete") tidak menyebut surface log; spec mengasersi di Changelog File Manager (baseline ditambah satu).
  - Post Condition semua TC bernilai `-`.
