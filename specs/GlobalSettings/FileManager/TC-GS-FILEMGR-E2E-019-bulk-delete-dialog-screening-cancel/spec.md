---
id: TC-GS-FILEMGR-E2E-019-bulk-delete-dialog-screening-cancel
title: "Dialog Bulk Delete: Screening Homogen dan Campuran, Satu Baris, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-79
  - TC-GS-FILEMGR-80
  - TC-GS-FILEMGR-81
  - TC-GS-FILEMGR-83
  - TC-GS-FILEMGR-87
coverage:
  web: automated
---

# Dialog Bulk Delete: Screening Homogen dan Campuran, Satu Baris, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (hanya dibaca, tidak diubah; semua dialog ditutup tanpa konfirmasi): Tabel A2, termasuk F01 `budi-avatar.jpg` (pemilik Budi Santoso), F02 `siti-profile.png` (pemilik Siti Rahmawati), F16 `staff-photo-08.jpg`, F17 `staff-photo-09.jpg`. Hook `before` memastikan Tabel A2 tersedia secara idempotent.
- Data Dinamis (D05, seeding fixture BE di hook `before`, bersuffix per run): `inactive-photo-01-{runId}-019.jpg` (pemilik Fajar Nugroho) dan `inactive-photo-02-{runId}-019.jpg` (pemilik Gita Lestari), JPG, aktif tetapi bukan foto profil aktif (`is_referenced = false`). Menambah 2 baris pada tabel utama (35 baris selama spec berjalan). Dipakai oleh TC-GS-FILEMGR-80 dan 81 dan tidak dihapus.
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): seeding file aktif dengan `is_referenced = false`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen kedua file `inactive-photo-*-{runId}-019.jpg` bila masih ada.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.
- Hook `beforeEach`: tutup dialog yang terbuka, kosongkan seleksi, dan kosongkan Search.

## Test Steps

### TC-GS-FILEMGR-79: Dialog bulk Delete seleksi seluruhnya foto profil aktif

1. Centang baris `budi-avatar.jpg` dan `siti-profile.png`
2. Klik `Bulk Action`
3. Klik `Delete`
4. Verifikasi judul dialog: "Delete Files"
5. Verifikasi isi dialog: daftar nama `budi-avatar.jpg` dan `siti-profile.png` dengan anotasi `currently Budi S's profile photo` dan `currently Siti R's profile photo`, kalimat "Deleting these will remove the corresponding profile photos.", lalu "Are you sure you want to delete them? This action cannot be undone."
6. Verifikasi tombol [Cancel] dan [Delete]
7. Tekan Esc untuk menutup dialog
8. Klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-81: Dialog bulk Delete seleksi campuran

9. Ketik Search `a`, tekan Enter
10. Centang baris `inactive-photo-01-{runId}-019.jpg` dan `budi-avatar.jpg`
11. Klik `Bulk Action`
12. Klik `Delete`
13. Verifikasi judul dialog: "Delete Files"
14. Verifikasi kelompok pertama berlabel "The following will be deleted:" memuat `inactive-photo-01-{runId}-019.jpg`
15. Verifikasi kelompok kedua berlabel "The following are currently used as profile photos and will also be removed:" memuat `budi-avatar.jpg`
16. Verifikasi penutup dialog: "Are you sure you want to delete them? This action cannot be undone."
17. Verifikasi tombol [Cancel] dan [Delete]
18. Tekan Esc untuk menutup dialog
19. Klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-80: Dialog bulk Delete seleksi seluruhnya bukan foto profil aktif

20. Ganti isi kotak search dengan `inactive-photo`, tekan Enter
21. Centang baris `inactive-photo-01-{runId}-019.jpg` dan `inactive-photo-02-{runId}-019.jpg`
22. Klik `Bulk Action`
23. Klik `Delete`
24. Verifikasi judul dialog: "Delete Files"
25. Verifikasi isi dialog: daftar nama `inactive-photo-01-{runId}-019.jpg` dan `inactive-photo-02-{runId}-019.jpg`, lalu "Are you sure you want to delete them? This action cannot be undone."
26. Verifikasi tidak ada kalimat "Deleting these will remove the corresponding profile photos."
27. Verifikasi tombol [Cancel] dan [Delete]
28. Tekan Esc untuk menutup dialog
29. Klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-83: Bulk Delete satu baris menampilkan dialog single

30. Ganti isi kotak search dengan `budi-avatar`, tekan Enter
31. Centang hanya baris `budi-avatar.jpg`
32. Klik `Bulk Action`
33. Klik `Delete`
34. Verifikasi judul dialog "Delete File" (singular)
35. Verifikasi isi dialog sama dengan dialog Delete single: nama file `budi-avatar.jpg` dengan anotasi `currently Budi S's profile photo`, "Deleting these will remove the corresponding profile photo.", "Are you sure you want to delete it? This action cannot be undone."
36. Verifikasi tidak ada daftar berlabel "The following will be deleted:"
37. Tekan Esc untuk menutup dialog
38. Klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-87: Cancel mempertahankan seleksi tanpa mutasi

39. Ganti isi kotak search dengan `staff-photo-0`, tekan Enter
40. Centang baris `staff-photo-08.jpg` dan `staff-photo-09.jpg`
41. Klik `Bulk Action`
42. Klik `Delete`
43. Klik [Cancel]
44. Verifikasi dialog tertutup
45. Verifikasi tidak ada toast
46. Verifikasi Bulk Action Bar tetap tampil dengan `2 Files selected`
47. Verifikasi baris `staff-photo-08.jpg` dan `staff-photo-09.jpg` tetap di tabel utama
48. Klik ikon `×` pada bar untuk mengosongkan seleksi

## Notes

- Mode: FE+BE. Spec tidak menghabisi data: semua dialog ditutup lewat Esc atau [Cancel], sehingga baris Pre-setup boleh menjadi target aksi yang dibatalkan dan hanya dibaca (S-06, pengecualian aksi yang dibatalkan). Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (48 langkah nominal). Alasan pertahanan: semua blok satu kelas (screening dialog tanpa mutasi) dan satu dataset, setiap blok diawali Search dan seleksi kosong sehingga tidak bergantung pada hasil blok lain, dan kegagalan satu dialog tidak membuat blok dialog lain kehilangan makna.
- Urutan TC pada spec: 79, 81, 80, 83, 87; screening homogen dan campuran lebih dulu, satu baris, lalu jalur Cancel di akhir (prinsip 6). Semua dialog sebelum TC-GS-FILEMGR-87 ditutup dengan Esc (penghubung).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 7, 18, 28, 37 (menutup dialog dengan Esc), 8, 19, 29, 38, 48 (mengosongkan seleksi, S-09), 9, 20, 30, 39 (Search untuk menemukan baris target; langkah 9 mengikuti TC-GS-FILEMGR-81).
- Pada TC sumber TC-GS-FILEMGR-79 tidak menyebut cara menutup dialog dan baris dipilih dari halaman aktif; baris F01 dan F02 berada di halaman 1 (urutan default Upload Date terbaru, D05 yang baru di-seed berada paling atas) sehingga tidak butuh Search.
- Temuan untuk QA:
  - Q-4: TC-GS-FILEMGR-80 dan 81 mensyaratkan file aktif bukan foto profil aktif (D05) lewat fixture BE; mekanismenya tidak didefinisikan. Ditulis "disediakan tim FE/BE" tanpa endpoint.
  - Q-7: D05 menambah 2 baris pada tabel utama; hitungan baru 35 baris dinyatakan di Prerequisites.
  - TC-GS-FILEMGR-81 langkah 1 mengetik Search `a` (huruf tunggal); hasil Search ini memuat banyak baris (substring `a` pada File Name atau kolom lain) sehingga baris target mungkin berada di halaman berikutnya. Spec mengikuti TC dan mengandalkan urutan default (D05 terbaru di halaman 1).
  - Post Condition semua TC bernilai `-`.
