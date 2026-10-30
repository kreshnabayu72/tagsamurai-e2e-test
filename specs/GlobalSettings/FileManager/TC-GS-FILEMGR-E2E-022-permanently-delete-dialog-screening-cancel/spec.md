---
id: TC-GS-FILEMGR-E2E-022-permanently-delete-dialog-screening-cancel
title: "Dialog Permanently Delete Single dan Bulk: Screening, Satu Baris, Cancel, dan Bulk Action Bar Recycle Bin"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-89
  - TC-GS-FILEMGR-91
  - TC-GS-FILEMGR-96
  - TC-GS-FILEMGR-97
  - TC-GS-FILEMGR-98
  - TC-GS-FILEMGR-99
coverage:
  web: automated
---

# Dialog Permanently Delete Single dan Bulk: Screening, Satu Baris, Cancel, dan Bulk Action Bar Recycle Bin

## Prerequisites

- Mode: FE+BE.
- Spec melewati sekitar 35 langkah (39 langkah nominal, tanpa blok yang diulang). Alasan pertahanan: seluruh blok satu kelas (screening dialog dan Bulk Action Bar Recycle Bin tanpa mutasi data) pada dataset Tabel A3 yang sama; tiap blok dimulai dari seleksi kosong dan dialog tertutup (Esc/penghubung) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (hanya dibaca, tidak diubah; semua dialog ditutup tanpa konfirmasi): Tabel A3, 16 file di Recycle Bin (2 halaman pada ukuran halaman 10), termasuk R01 `old-avatar.png`, R02 `legacy-photo.jpeg` (Auto-Purge In `12 days`), R05 `recycled-photo-01.jpg`, R06 `recycled-photo-02.jpg`, R07 `recycled-photo-03.jpg`, R08 `recycled-photo-04.jpg`, R09 `recycled-photo-05.jpg`. Hook `before` memastikan Tabel A3 tersedia secara idempotent (total tepat 16 baris; spec lain membersihkan seed-nya sendiri).
- State global yang dibaca (tidak diubah): durasi retensi Recycle Bin 30 hari (default Lifecycle Settings); Selection Limit lebih besar dari 16.
- Job auto-purge harian tidak boleh berjalan selama spec (menghapus baris jatuh tempo, mis. R04 `due-photo.png`, sehingga hitungan 16 berubah); dijeda di environment e2e (lihat Temuan untuk QA).
- Suite serial (`parallel: false`). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.
- Hook `beforeEach`: tutup dialog dan modal Recycle Bin yang terbuka, kosongkan seleksi.

## Test Steps

### TC-GS-FILEMGR-89: Screening dialog Permanently Delete single

1. Klik tombol Recycle Bin di toolbar
2. Klik ikon `⋯` baris `old-avatar.png`
3. Verifikasi opsi overlay `Permanently Delete` memakai ikon DeleteBin6Line dengan severity danger
4. Klik `Permanently Delete`
5. Verifikasi judul dialog: "Permanently Delete File"
6. Verifikasi isi dialog: nama file `old-avatar.png` di dalam container scrollable, lalu "Are you sure you want to permanently delete it? This action cannot be undone."
7. Verifikasi tombol [Cancel] dan [Permanently Delete]
8. Tekan Esc untuk menutup dialog

### TC-GS-FILEMGR-97: Screening Bulk Action Bar Recycle Bin

9. Centang checkbox baris `old-avatar.png`
10. Verifikasi urutan elemen bar: tombol `Bulk Action`, teks `1 File selected`, tombol `Select All (16 records)`, ikon `×`
11. Klik tombol `Bulk Action` untuk membuka overlay
12. Verifikasi overlay memuat satu aksi: `Permanently Delete` (ikon DeleteBin6Line, severity danger)
13. Verifikasi tidak ada aksi Recover
14. Tutup overlay `Bulk Action` dengan Esc, lalu klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-96: Screening dialog bulk Permanently Delete

15. Centang baris `recycled-photo-03.jpg` dan `recycled-photo-04.jpg`
16. Klik `Bulk Action`, lalu klik `Permanently Delete`
17. Verifikasi judul dialog: "Permanently Delete Files"
18. Verifikasi isi dialog: nama `recycled-photo-03.jpg` dan `recycled-photo-04.jpg` sebagai bullet dalam container scrollable, lalu "Are you sure you want to permanently delete them? This action cannot be undone."
19. Verifikasi tombol [Cancel] dan [Permanently Delete]
20. Tekan Esc untuk menutup dialog, lalu klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-99: Bulk Permanently Delete satu baris menampilkan dialog single

21. Centang hanya baris `recycled-photo-05.jpg`
22. Klik `Bulk Action`, lalu klik `Permanently Delete`
23. Verifikasi judul dialog "Permanently Delete File" (singular)
24. Verifikasi isi dialog sama dengan dialog single: "Are you sure you want to permanently delete it? This action cannot be undone."
25. Tekan Esc untuk menutup dialog, lalu klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-98: Cancel dialog bulk Permanently Delete

26. Centang baris `recycled-photo-01.jpg` dan `recycled-photo-02.jpg`
27. Klik `Bulk Action`, lalu klik `Permanently Delete`
28. Klik [Cancel]
29. Verifikasi dialog tertutup
30. Verifikasi tidak ada toast
31. Verifikasi bar tetap tampil dengan `2 Files selected`
32. Verifikasi baris `recycled-photo-01.jpg` dan `recycled-photo-02.jpg` tetap di Recycle Bin
33. Klik ikon `×` pada bar untuk mengosongkan seleksi

### TC-GS-FILEMGR-91: Cancel dialog Permanently Delete single

34. Klik ikon `⋯` baris `legacy-photo.jpeg`, lalu klik `Permanently Delete`
35. Klik [Cancel]
36. Verifikasi dialog tertutup
37. Verifikasi tidak ada toast
38. Verifikasi baris `legacy-photo.jpeg` tetap di Recycle Bin dengan Auto-Purge In `12 days`
39. Tutup modal Recycle Bin dengan `✕` di header

## Notes

- Mode: FE+BE. Spec tidak menghabisi data: seluruh dialog ditutup lewat Esc atau [Cancel], sehingga baris Pre-setup A3 boleh menjadi target aksi yang dibatalkan dan hanya dibaca (S-06, pengecualian aksi yang dibatalkan). Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC pada spec: 89, 97, 96, 99, 98, 91 (screening dialog single, screening bar, screening dialog bulk, satu baris, lalu jalur Cancel di akhir, prinsip 3 dan 6). TC-GS-FILEMGR-91 terakhir karena menutup modal Recycle Bin yang dibuka sekali di awal.
- Panjang spec: 39 langkah, di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu kelas (screening dan jalur batal dialog Permanently Delete tanpa mutasi data) pada dataset Tabel A3 yang sama, dan tiap blok membuka dialognya sendiri dari seleksi kosong sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 8, 20, 25 (menutup dialog dengan Esc), 14, 20, 25, 33 (mengosongkan seleksi dan menutup overlay, S-09), 39 (menutup modal).
- Temuan untuk QA:
  - Q-3: Tabel A3 R04 `due-photo.png` (Deleted Date sekarang - 31 hari, retensi 30 hari) "tetap tampil sampai job auto-purge berikutnya"; bila job harian berjalan antara seeding dan asersi, hitungan `Select All (16 records)` berubah. Perlu keputusan: job dijeda di environment e2e atau jam dibekukan; ditulis di Prerequisites sebagai kemampuan teknis yang diminta.
  - Q-4: seeding Tabel A3 tidak punya mekanisme di TC; ditulis "disediakan tim FE/BE".
  - TC-GS-FILEMGR-96 dan TC-GS-FILEMGR-99 tidak menyebut cara menutup dialog; spec memakai Esc sebagai langkah penghubung.
  - TC-GS-FILEMGR-97 menyebut `Select All (16 records)`; hitungan valid hanya bila tidak ada baris Recycle Bin lain (Q-7).
  - Post Condition semua TC bernilai `-`.
