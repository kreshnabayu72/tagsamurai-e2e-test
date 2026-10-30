---
id: TC-GS-FILEMGR-E2E-013-delete-single-dialog-screening-cancel-dan-esc
title: "Dialog Delete Single: Screening, Cancel, Backdrop, dan Esc"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-60
  - TC-GS-FILEMGR-61
  - TC-GS-FILEMGR-62
  - TC-GS-FILEMGR-63
coverage:
  web: automated
---

# Dialog Delete Single: Screening, Cancel, Backdrop, dan Esc

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (hanya dibaca, tidak diubah; semua aksi pada spec ini dibatalkan lewat Cancel, backdrop, atau Esc): F01 `budi-avatar.jpg` (foto profil aktif Budi Santoso, Tabel A2). Hook `before` memastikan Tabel A2 (33 baris aktif) tersedia secara idempotent (dilewati bila sudah ada).
- Data Dinamis (D05, seeding fixture BE di hook `before`, bersuffix per run): `inactive-photo-01-{runId}-013.jpg` (JPG, aktif tetapi bukan foto profil aktif, pemilik Fajar Nugroho). Menambah 1 baris pada tabel utama (34 baris selama spec berjalan). Dipakai sebagai precondition TC-GS-FILEMGR-61 dan tidak dihapus.
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): seeding file aktif dengan status `is_referenced = false`; membaca foto profil pemilik di Global Settings > User > Detail User (selektor modul lain disediakan tim FE).
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md` (flag `guided_tooltip_seen_gs-file-manager`).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen `inactive-photo-01-{runId}-013.jpg` lewat fixture BE bila masih ada. Hook `beforeEach`: tutup dialog yang terbuka dan kembali ke Global Settings > File Manager.

## Test Steps

### TC-GS-FILEMGR-60: Screening dialog Delete untuk foto profil aktif

1. Ketik Search `budi-avatar`, tekan Enter
2. Verifikasi baris `budi-avatar.jpg` tampil pada tabel utama
3. Klik ikon `⋯` baris `budi-avatar.jpg`
4. Verifikasi opsi `Delete` pada overlay row action enabled (tidak Disabled)
5. Klik `Delete`
6. Verifikasi judul dialog: "Delete File"
7. Verifikasi isi dialog berurutan: nama file `budi-avatar.jpg` dengan anotasi `currently Budi S's profile photo`, kalimat "Deleting these will remove the corresponding profile photo.", lalu "Are you sure you want to delete it? This action cannot be undone."
8. Verifikasi tombol [Cancel] dan [Delete]
9. Verifikasi tidak ada dialog blok yang tampil selain dialog konfirmasi ini

### TC-GS-FILEMGR-63: Backdrop tidak menutup dialog, Esc menutupnya

10. Klik area gelap di luar dialog
11. Verifikasi dialog Delete tetap terbuka
12. Tekan Esc
13. Verifikasi dialog tertutup
14. Verifikasi tidak ada toast
15. Verifikasi baris `budi-avatar.jpg` tetap di tabel utama
16. Buka modal Recycle Bin, ketik Search `budi-avatar`, tekan Enter
17. Verifikasi empty state "No results found" pada modal Recycle Bin (`budi-avatar.jpg` tidak ada di Recycle Bin)
18. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-61: Screening dialog Delete untuk file aktif bukan foto profil aktif

19. Ganti isi kotak search dengan `inactive-photo-01-{runId}-013`, tekan Enter
20. Verifikasi baris `inactive-photo-01-{runId}-013.jpg` tampil
21. Klik ikon `⋯` baris `inactive-photo-01-{runId}-013.jpg`, lalu klik `Delete`
22. Verifikasi judul dialog: "Delete File"
23. Verifikasi isi dialog: nama file `inactive-photo-01-{runId}-013.jpg` tanpa anotasi foto profil, lalu "Are you sure you want to delete it? This action cannot be undone."
24. Verifikasi tidak ada kalimat "Deleting these will remove the corresponding profile photo."
25. Verifikasi tombol [Cancel] dan [Delete]
26. Tekan Esc untuk menutup dialog

### TC-GS-FILEMGR-62: Cancel tidak mengubah data

27. Ganti isi kotak search dengan `budi-avatar`, tekan Enter
28. Klik ikon `⋯` baris `budi-avatar.jpg`, lalu klik `Delete`
29. Klik [Cancel]
30. Verifikasi dialog tertutup
31. Verifikasi tidak ada toast
32. Verifikasi baris `budi-avatar.jpg` tetap di tabel utama
33. Buka modal Recycle Bin, ketik Search `budi-avatar`, tekan Enter
34. Verifikasi empty state "No results found" pada modal Recycle Bin (`budi-avatar.jpg` tidak ada di Recycle Bin)
35. Tutup modal Recycle Bin dengan `✕` di header
36. Buka Global Settings > User > Detail User Budi Santoso
37. Verifikasi foto profil Budi Santoso tidak berubah (tetap `budi-avatar.jpg`)

## Notes

- Mode: FE+BE. Kelas screening dan jalur batal; tidak ada mutasi data, sehingga baris Pre-setup F01 boleh menjadi target aksi yang dibatalkan (S-06, pengecualian aksi yang dibatalkan, hanya dibaca).
- Spec melewati sekitar 35 langkah (37 langkah nominal, tanpa blok yang diulang). Alasan pertahanan: seluruh blok satu kelas (screening dan jalur batal dialog Delete single tanpa mutasi data) pada dataset yang sama, dan tiap blok membuka dialognya sendiri dari baris yang dicari lewat Search sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC pada spec: 60, 63, 61, 62. TC-GS-FILEMGR-63 mendahului TC-GS-FILEMGR-61 karena menutup dialog yang sama dengan TC-GS-FILEMGR-60 tanpa membuka ulang (prinsip 6); TC-GS-FILEMGR-62 membuka dialog baru sebagai kasus penutupan terakhir.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 19 dan 27 (Search untuk menemukan baris target; tabel utama memiliki 34 baris), 16, 18, 33, 35 (membuka dan menutup modal Recycle Bin), 26 (menutup dialog TC-GS-FILEMGR-61 dengan Esc).
- Asersi tambahan di luar Expected TC (dicatat sesuai S-03): langkah 2 dan 20 (baris target tampil sebagai anchor positif sebelum klik), langkah 17 dan 34 (empty state "No results found" sebagai anchor absence `budi-avatar.jpg` di Recycle Bin).
- Langkah 4 (opsi `Delete` enabled) memenuhi butir d Expected TC-GS-FILEMGR-60 ("Tombol Delete di baris tetap enabled"); diasersi sebelum klik karena state itu hanya teramati pada overlay row action sebelum dialog dibuka (butir 5).
- Temuan untuk QA:
  - Q-4 (mekanisme fixture BE): TC-GS-FILEMGR-61 mensyaratkan file aktif `is_referenced = false` (D05) lewat fixture BE; TC, PRD, dan LLD tidak menyebut endpoint/mekanismenya. Spec menulisnya "disediakan tim FE/BE" tanpa mengarang endpoint.
  - Q-7: TC-GS-FILEMGR-61 menambah satu baris pada tabel utama (D05); hitungan baru 34 baris dinyatakan di Prerequisites.
  - Q-9: langkah 36 dan 37 membuka Detail User (modul User) yang selektornya tidak didefinisikan di TC ini; ditandai "disediakan tim FE".
  - Post Condition TC-GS-FILEMGR-60 s.d. 63 bernilai `-`; tidak ada yang diasersi di luar Expected.
  - Anotasi `currently Budi S's profile photo` (NC-19) memakai bentuk `[First Name] [Last Initial]` sesuai TC.
