---
id: TC-GS-FILEMGR-E2E-007-role-matrix-positif-download-delete-dan-permanently-delete
title: "Role Matrix Positif: Download, Delete, dan Permanently Delete per Capability"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-47
  - TC-GS-FILEMGR-200
  - TC-GS-FILEMGR-289
coverage:
  web: automated
---

# Role Matrix Positif: Download, Delete, dan Permanently Delete per Capability

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Read Only Rina Pratiwi) dilakukan di hook `before`; ganti akun ke role berikutnya ditulis sebagai langkah eksplisit (langkah 5 dan 11). Spec berakhir di akun Manage files: Delete; hook `after` mengembalikan sesi ke akun default suite (Total Control Sinta Maharani, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (Tabel Data Uji Pre-setup A1; domain `{namaCompany}`):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-FILEMGR-200 | Read Only | Rina Pratiwi | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-FILEMGR-200 | Manage files: Read | Doni Saputra | `manageFilesRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FILES_READ_PASSWORD` |
| TC-GS-FILEMGR-47, TC-GS-FILEMGR-289 | Manage files: Delete | Agus Wibowo | `manageFilesDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FILES_DELETE_PASSWORD` |

- Langkah ketiga role berbeda (Download CSV untuk dua role pertama; Delete dan Permanently Delete untuk role ketiga), sehingga spec ditulis per blok role.
- Data Dinamis milik spec, di-seed lewat fixture BE di hook `before` dan dibersihkan lewat API di hook `after` (hanya yang dibuat spec ini; pembersihan tidak berasumsi seeding berhasil penuh):
  - `fm-delete-{runId}-007.png`: file aktif yang bukan foto profil aktif (pola D05), dipakai TC-47 sebagai pengganti `siti-profile.png` supaya baris Pre-setup tidak diubah (S-06).
  - `fm-purge-{runId}-007.png`: file di Recycle Bin (pola D09), dipakai TC-289 sebagai pengganti `old-avatar.png`.
- Kemampuan teknis: fixture BE untuk kedua file (mekanisme seeding tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE); membaca file CSV terunduh di perangkat uji.
- Data Pre-setup yang dibaca: Tabel A2 (33 file aktif) agar tabel utama berisi data saat Download CSV.
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true untuk ketiga akun oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-200: Read Only dan Manage files: Read dapat mengunduh export

1. Klik ikon Download di toolbar tabel utama
2. Pilih `Download as CSV`
3. Verifikasi file CSV terunduh
4. Verifikasi tidak ada toast sukses
5. Ganti akun: logout, lalu login sebagai Manage files: Read
6. Buka Global Settings > File Manager dari sidebar
7. Klik ikon Download di toolbar tabel utama
8. Pilih `Download as CSV`
9. Verifikasi file CSV terunduh
10. Verifikasi tidak ada toast sukses

### TC-GS-FILEMGR-47: Manage files: Delete menjalankan Delete single sampai sukses

11. Ganti akun: logout, lalu login sebagai Manage files: Delete
12. Buka Global Settings > File Manager dari sidebar
13. Ketik Search `fm-delete-{runId}-007`, tekan Enter
14. Verifikasi baris `fm-delete-{runId}-007.png` tampil di tabel utama
15. Klik ikon (⋯) baris `fm-delete-{runId}-007.png`
16. Klik `Delete`
17. Klik `[Delete]` pada dialog konfirmasi
18. Verifikasi toast sukses `Success, fm-delete-{runId}-007.png has been deleted.`
19. Verifikasi baris `fm-delete-{runId}-007.png` hilang dari tabel utama
20. Klik tombol Recycle Bin di toolbar
21. Ketik Search `fm-delete-{runId}-007`, tekan Enter
22. Verifikasi `fm-delete-{runId}-007.png` tampil di Recycle Bin
23. Verifikasi Deleted By `fm-delete-{runId}-007.png` bernilai `Agus W`

### TC-GS-FILEMGR-289: Permanently Delete oleh pemegang Manage files: Delete menghapus permanen file di Recycle Bin

24. Klik `(←)` pada kotak Search Recycle Bin
25. Ketik Search `fm-purge-{runId}-007`, tekan Enter
26. Verifikasi baris `fm-purge-{runId}-007.png` tampil di Recycle Bin
27. Klik ikon (⋯) baris `fm-purge-{runId}-007.png`
28. Klik `Permanently Delete`
29. Klik `[Permanently Delete]` pada dialog konfirmasi
30. Verifikasi toast sukses `Success, fm-purge-{runId}-007.png has been permanently deleted.`
31. Verifikasi baris `fm-purge-{runId}-007.png` hilang dari Recycle Bin
32. Tutup modal Recycle Bin dengan `✕` di header
33. Klik ikon Changelog di toolbar
34. Ketik Search `fm-purge-{runId}-007`, tekan Enter
35. Verifikasi Modal Changelog memuat entri `Permanently Delete` untuk `fm-purge-{runId}-007.png`
36. Verifikasi Modified By entri itu bernilai `Agus W`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-200 (hanya baca) ditaruh pertama dan dua aksi destruktif (TC-47 Delete, TC-289 Permanently Delete) terakhir (prinsip 5); urutan sumber TC-47, TC-200, TC-289.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 5, 11 (ganti akun), langkah 6, 12 (membuka File Manager di akun baru), langkah 13, 21, 25, 34 (Search untuk menemukan baris target), langkah 24 (mengosongkan Search Recycle Bin), langkah 32 (menutup modal Recycle Bin).
- Langkah 4 dan 10 (absence toast sukses) didahului pemicu yang menjadi anchor positif (file terunduh pada langkah 3 dan 9), sesuai 8b butir 11.
- Langkah 23 dan 36 memakai bentuk `[First Name] [Last Initial]` (`Agus W`) untuk Deleted By dan Modified By (S-02); Expected TC-47 sudah menulis `Agus W`, sedangkan Expected TC-289 butir c menulis `Agus Wibowo`.
- Langkah 17 memakai label tombol `[Delete]` sesuai TC-47. Langkah 29 memakai `[Permanently Delete]` sesuai dialog TC-GS-FILEMGR-90 (PRD D-06); TC-289 menulis `[Delete]`.
- Alasan spec di atas sekitar 35 langkah (S-10, bagian 3a): spec Role Matrix positif dengan tiga blok role yang tiap bloknya berdiri sendiri lewat Step ganti akun eksplisit; kegagalan satu blok tidak membuat blok role berikutnya kehilangan makna karena tiap blok membuka File Manager dari sidebar sebagai akun barunya dan memakai data milik spec sendiri.
- Temuan untuk QA:
  - TC-289 langkah 3 menulis `[Delete]` untuk dialog Permanently Delete, sedangkan TC-GS-FILEMGR-90 menulis `[Permanently Delete]`; salah satu perlu dikoreksi.
  - TC-289 Expected a hanya menulis "toast sukses untuk `old-avatar.png`" tanpa teks; spec memakai pola TC-90 `Success, [File Name] has been permanently deleted.`
  - TC-289 Expected c menulis Modified By `Agus Wibowo` (nama lengkap), sedangkan konvensi kolom Modified By `[First Name] [Last Initial]` (`Agus W`); spec memakai `Agus W`.
  - TC-47 dan TC-289 memakai baris Pre-setup (`siti-profile.png` foto profil aktif, `old-avatar.png` R01) sebagai target; spec memakai file milik spec (S-06) sehingga dialog Delete yang muncul untuk file bukan foto profil aktif (tanpa anotasi foto profil) berbeda dari kasus `siti-profile.png`; TC-47 tidak mengasersi isi dialog.
  - TC-200 tidak menyebut isi file CSV yang diunduh; isi tidak diasersi di spec ini (diuji di spec 052).
  - Mekanisme fixture BE untuk file milik spec tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
