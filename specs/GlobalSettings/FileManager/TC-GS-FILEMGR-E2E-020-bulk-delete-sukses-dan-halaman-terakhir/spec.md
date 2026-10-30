---
id: TC-GS-FILEMGR-E2E-020-bulk-delete-sukses-dan-halaman-terakhir
title: "Bulk Delete Berhasil: Campuran, Seleksi Direset, dan Pindah ke Halaman Terakhir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-82
  - TC-GS-FILEMGR-84
  - TC-GS-FILEMGR-153
coverage:
  web: automated
---

# Bulk Delete Berhasil: Campuran, Seleksi Direset, dan Pindah ke Halaman Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run, seluruhnya dihapus oleh spec ini; pemilik adalah user klon milik spec dengan nama tampil seperti Tabel A2, disediakan tim FE agar baris Pre-setup tidak diubah, S-06):
  - TC-GS-FILEMGR-82: `inactive-photo-02-{runId}-020.jpg` (D05, JPG, aktif tetapi bukan foto profil aktif, pemilik klon `Gita Lestari`) dan `alex-photo-{runId}-020.jpeg` (JPEG, foto profil aktif pemilik klon `Alexander Graham Bell`).
  - TC-GS-FILEMGR-84 (D02): `staff-photo-01-{runId}-020.jpg`, `staff-photo-02-{runId}-020.jpg`, `staff-photo-03-{runId}-020.jpg` (JPG, foto profil aktif tiga pemilik klon).
  - TC-GS-FILEMGR-153: 25 file `lot-photo-01-{runId}-020.jpg` s.d. `lot-photo-25-{runId}-020.jpg` (JPG, aktif; 3 halaman pada ukuran halaman 10, halaman 3 berisi 5 baris), berfungsi sebagai pengganti 25 baris `staff-photo-` Tabel A2 yang tidak boleh dihapus.
- Kemampuan teknis (disediakan tim FE/BE): seeding file dengan pemilik klon; membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`); jam server dan jam browser sinkron (asersi Deleted Date, toleransi satu menit, S-12); membaca foto profil pemilik di Global Settings > User > Detail User (selektor modul lain disediakan tim FE).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen seluruh file seed (termasuk yang berada di Recycle Bin) dan hapus user klon.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-82: Bulk Delete campuran

1. Ketik Search `{runId}-020`, tekan Enter
2. Centang baris `inactive-photo-02-{runId}-020.jpg` dan `alex-photo-{runId}-020.jpeg`
3. Klik `Bulk Action`, klik `Delete`, lalu klik [Delete] pada dialog
4. Verifikasi toast sukses: "Success, file has been deleted."
5. Verifikasi Bulk Action Bar hilang
6. Verifikasi seleksi kembali 0
7. Buka modal Recycle Bin, ketik Search `{runId}-020`, tekan Enter
8. Verifikasi `inactive-photo-02-{runId}-020.jpg` dan `alex-photo-{runId}-020.jpeg` tampil di Recycle Bin dengan Deleted By `Sinta M`
9. Tutup modal Recycle Bin dengan `✕` di header
10. Buka Global Settings > User > Detail User Alexander Graham Bell (klon milik spec)
11. Verifikasi foto profil Alexander Graham Bell kosong
12. Buka Global Settings > User > Detail User Gita Lestari (klon milik spec)
13. Verifikasi foto profil Gita Lestari tidak berubah

### TC-GS-FILEMGR-84: Bulk Delete memproses seluruh file terseleksi dan mereset seleksi

14. Buka Global Settings > File Manager, ketik Search `{runId}-020`, tekan Enter
15. Centang baris `staff-photo-01-{runId}-020.jpg`, `staff-photo-02-{runId}-020.jpg`, dan `staff-photo-03-{runId}-020.jpg`
16. Klik `Bulk Action`, klik `Delete`, lalu klik [Delete] pada dialog
17. Verifikasi toast sukses: "Success, file has been deleted."
18. Verifikasi Bulk Action Bar hilang
19. Verifikasi seleksi kembali 0
20. Verifikasi ketiga baris hilang dari tabel utama
21. Buka modal Recycle Bin, ketik Search `{runId}-020`, tekan Enter
22. Verifikasi ketiga file tampil di Recycle Bin dengan Deleted By `Sinta M`
23. Verifikasi tidak ada file yang dilewati karena status foto profil aktif (ketiga file ada di Recycle Bin)
24. Tutup modal Recycle Bin dengan `✕` di header
25. Klik ikon Changelog di toolbar, ketik Search `{runId}-020`, tekan Enter
26. Verifikasi Changelog memuat tepat tiga baris Action `Delete` baru (satu per file) untuk ketiga file (jumlah = baseline ditambah tiga)
27. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-153: Hapus seluruh baris halaman terakhir

28. Ganti isi kotak search dengan `lot-photo`, tekan Enter
29. Pindah ke halaman 3
30. Verifikasi halaman 3 berisi 5 baris
31. Centang checkbox header
32. Klik `Bulk Action`, klik `Delete`, lalu klik [Delete] pada dialog
33. Verifikasi toast sukses: "Success, file has been deleted."
34. Verifikasi tabel pindah ke halaman 2 (halaman terakhir yang masih ada)
35. Verifikasi halaman 2 berisi 10 baris

## Notes

- Mode: FE+BE (destruktif). Subjudul `###` memetakan langkah ke id TC granular. Seluruh aksi menghapus data dan dikelompokkan di spec ini; TC-GS-FILEMGR-153 di akhir karena memakai pool file sendiri.
- Urutan TC pada spec mengikuti TC sumber (82, 84, 153); tidak ada pergeseran. Dependensi TC (TC-GS-FILEMGR-82 pada TC-GS-FILEMGR-81, TC-GS-FILEMGR-84 pada TC-GS-FILEMGR-79, TC-GS-FILEMGR-153 pada TC-GS-FILEMGR-84) tidak menjadi dependensi spec: tiap blok memakai data dan langkahnya sendiri (S-04).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 14, 28 (Search untuk menemukan baris target), 7, 9, 21, 24, 25, 27 (membuka dan menutup modal Recycle Bin dan Changelog), 10, 12, 14 (navigasi antar modul), 29 (pindah ke halaman 3 sesuai TC-GS-FILEMGR-153).
- Asersi tambahan di luar Expected TC (S-03): langkah 30 (precondition halaman 3 berisi 5 baris, S-14: keadaan dicek sebelum aksi).
- Asersi absence baris (langkah 20) memakai toast sukses langkah 17 sebagai anchor (butir 2 bagian 8b).
- TC-GS-FILEMGR-84 Expected e ("Tidak ada file yang dilewati karena status foto profil aktif") diasersi pada langkah 23 lewat ketiga file ada di Recycle Bin.
- Temuan untuk QA:
  - Q-5/Q-7: TC menargetkan baris Pre-setup F03 `alex-photo.jpeg`, F09 s.d. F11, dan 25 baris `staff-photo-` (F09 s.d. F33) untuk dihapus, bertentangan dengan S-06 dan hitungan 33 baris spec lain. Spec memakai file bersuffix dengan pemilik klon, dan 25 file `lot-photo-` menggantikan 25 baris `staff-photo-` pada TC-GS-FILEMGR-153 (Search `lot-photo` menggantikan `staff-photo`). Nama pemilik klon literal belum terdaftar sebagai pengecualian S-12.
  - Q-9: TC-GS-FILEMGR-82 langkah 4 membuka Detail User; selektor modul lain ditandai "disediakan tim FE".
  - Post Condition TC-GS-FILEMGR-84 butir b (foto profil ketiga owner kosong) dan butir c (entri log di System Log Sinta Maharani dan Activity Log) tidak memiliki langkah observasi di TC (assertion detail di TC modul User/Section 5); butir c Changelog File Manager diasersi pada langkah 26, tiga surface log lengkap pada spec `TC-GS-FILEMGR-E2E-056`.
  - TC-GS-FILEMGR-82 Expected a menulis "Success, file has been deleted." (tanpa nama file); spec mengikuti TC.
