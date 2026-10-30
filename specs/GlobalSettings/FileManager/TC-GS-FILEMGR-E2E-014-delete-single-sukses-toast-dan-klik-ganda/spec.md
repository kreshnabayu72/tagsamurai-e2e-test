---
id: TC-GS-FILEMGR-E2E-014-delete-single-sukses-toast-dan-klik-ganda
title: "Delete Single Berhasil: Foto Aktif, Toast Otomatis Hilang, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-64
  - TC-GS-FILEMGR-65
  - TC-GS-FILEMGR-69
coverage:
  web: automated
---

# Delete Single Berhasil: Foto Aktif, Toast Otomatis Hilang, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run, seluruhnya dihapus oleh spec ini; pemilik adalah user klon milik spec dengan foto profil aktif, disediakan tim FE agar baris Pre-setup F01 s.d. F08 tidak diubah, S-06):
  - `budi-avatar-{runId}-014.jpg` (JPG, foto profil aktif pemilik klon `Budi Santoso`) untuk TC-GS-FILEMGR-64.
  - `siti-profile-{runId}-014.png` (PNG, foto profil aktif pemilik klon `Siti Rahmawati`) untuk TC-GS-FILEMGR-65.
  - `alex-photo-{runId}-014.jpeg` (JPEG, foto profil aktif pemilik klon `Alexander Graham Bell`) untuk TC-GS-FILEMGR-69.
- Kemampuan teknis (disediakan tim FE/BE): seeding file aktif dengan pemilik klon; membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`, sebelum aksi pertama); mengamati durasi toast; jam server dan jam browser sinkron (asersi Deleted Date dengan toleransi satu menit, S-12).
- Jeda nyata: langkah 16 menunggu sampai 6 detik untuk mengamati toast hilang otomatis (TC-GS-FILEMGR-65 menetapkan pengamatan 6 detik).
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen ketiga file dan hapus user klon bila masih ada.

## Test Steps

### TC-GS-FILEMGR-64: Konfirmasi Delete file foto profil aktif

1. Ketik Search `budi-avatar-{runId}-014`, tekan Enter
2. Klik ikon `⋯` baris `budi-avatar-{runId}-014.jpg`, lalu klik `Delete`
3. Klik [Delete] pada dialog
4. Verifikasi toast sukses: "Success, budi-avatar-{runId}-014.jpg has been deleted."
5. Verifikasi dialog tertutup
6. Verifikasi baris `budi-avatar-{runId}-014.jpg` hilang dari tabel utama
7. Verifikasi tidak ada dialog blok yang tampil
8. Buka modal Recycle Bin, ketik Search `budi-avatar-{runId}-014`, tekan Enter
9. Verifikasi `budi-avatar-{runId}-014.jpg` tampil di Recycle Bin dengan Deleted By `Sinta M`
10. Verifikasi Deleted Date `budi-avatar-{runId}-014.jpg` sesuai waktu aksi (toleransi satu menit)
11. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-65: Toast sukses hilang otomatis

12. Ganti isi kotak search dengan `siti-profile-{runId}-014`, tekan Enter
13. Klik ikon `⋯` baris `siti-profile-{runId}-014.png`, lalu klik `Delete`, lalu klik [Delete] pada dialog
14. Verifikasi toast sukses "Success, siti-profile-{runId}-014.png has been deleted." tampil
15. Verifikasi toast tampil di kanan bawah
16. Amati toast selama 6 detik tanpa tindakan
17. Verifikasi toast hilang otomatis setelah sekitar 4 detik

### TC-GS-FILEMGR-69: Klik ganda cepat pada [Delete]

18. Ganti isi kotak search dengan `alex-photo-{runId}-014`, tekan Enter
19. Klik ikon `⋯` baris `alex-photo-{runId}-014.jpeg`, lalu klik `Delete`
20. Klik ganda cepat pada [Delete] di dialog
21. Verifikasi tombol [Delete] dalam keadaan loading dan tidak dapat diklik ulang setelah klik pertama
22. Verifikasi hanya satu toast sukses "Success, alex-photo-{runId}-014.jpeg has been deleted." tampil
23. Buka modal Recycle Bin, ketik Search `alex-photo-{runId}-014`, tekan Enter
24. Verifikasi `alex-photo-{runId}-014.jpeg` muncul satu kali di Recycle Bin
25. Tutup modal Recycle Bin dengan `✕` di header
26. Klik ikon Changelog di toolbar, ketik Search `alex-photo-{runId}-014`, tekan Enter
27. Verifikasi jumlah entri Action `Delete` untuk `alex-photo-{runId}-014.jpeg` sama dengan baseline ditambah satu (tepat satu entri Delete)
28. Tutup modal Changelog dengan `✕` di header

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular. Aksi yang menghabisi data (Delete) ketiganya berada di spec ini; masing-masing memakai file sendiri sehingga urutan TC (64, 65, 69) tidak saling bergantung.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 12, 18 (Search untuk menemukan baris target), 8 dan 11, 23 dan 25, 26 dan 28 (membuka dan menutup modal Recycle Bin dan Changelog).
- Nama file memakai suffix per run, sehingga teks toast memuat nama bersuffix (S-12); TC sumber menulis nama tetap `budi-avatar.jpg`, `siti-profile.png`, `alex-photo.jpeg` dari Tabel A2. File Pre-setup tidak dihapus agar tidak bentrok dengan spec lain (S-06).
- Asersi absence baris (langkah 6) memakai toast sukses langkah 4 sebagai anchor (butir 2 bagian 8b).
- Temuan untuk QA:
  - Q-1 (TC-GS-FILEMGR-65): judul dan Expected menyebut hilang otomatis setelah 4 detik dengan pengamatan 6 detik; nilai 4 dan 6 detik hanya ada di `foundation/functions/toast-copy.md`, tidak di PRD, dan toleransi tidak didefinisikan. Langkah 17 mengasersi "sekitar 4 detik"; perlu konfirmasi toleransi.
  - Q-5/Q-7: TC menargetkan baris Pre-setup F01 (`budi-avatar.jpg`), F02, F03 untuk aksi hapus, bertentangan dengan S-06 dan merusak hitungan "33 records" spec lain; spec memakai file bersuffix dengan pemilik klon. Nama pemilik klon literal (mis. `Budi Santoso`) karena anotasi nama dan Deleted By dapat dibaca; pengecualian literal ini belum terdaftar di S-12.
  - Post Condition TC-GS-FILEMGR-64 butir b (foto profil Budi Santoso kosong di Detail User) tidak memiliki langkah observasi di TC (assertion di TC modul User), sehingga tidak diasersi di spec ini. Butir c (entri log Delete di Changelog File Manager, System Log, Activity Log) diasersi di spec `TC-GS-FILEMGR-E2E-056`.
  - Q-4: TC tidak menyebut cara membaca baseline entri Changelog atau seeding pemilik klon; ditulis "disediakan tim FE/BE" tanpa endpoint.
