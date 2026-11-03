---
id: TC-FA-PREF-E2E-154-deferred-konsumen-depreciation-run-dan-export-journal-setup-incomplete-pembacaan-preferences-dan-label-tahun-fiskal
title: "[DEFERRED] Konsumen: Depreciation Run dan Export Journal terblokir saat Setup Incomplete, pembacaan Preferences, dan label tahun fiskal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-504
  - TC-FA-PREF-505
  - TC-FA-PREF-506
  - TC-FA-PREF-507
  - TC-FA-PREF-509
  - TC-FA-PREF-510
coverage:
  web: automated
---

# [DEFERRED] Konsumen: Depreciation Run dan Export Journal terblokir saat Setup Incomplete, pembacaan Preferences, dan label tahun fiskal

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul konsumen yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1; Asset Class PC-6; 3 pelepasan belum diposting (PC-7); varian Preferences per TC (dibentuk lewat seed):
  - TC-FA-PREF-504 dan 505: In-service Date Source tersimpan kosong sehingga banner Setup Incomplete tampil (PC-12).
  - TC-FA-PREF-506: seluruh setting wajib tersimpan terisi (PC-1).
  - TC-FA-PREF-507: Depreciation in Disposal Month tersimpan "Up to previous month" dengan 3 pelepasan menunggu posting (PC-1, PC-6, PC-7).
  - TC-FA-PREF-509: modul akuntansi aktif tetapi company belum memiliki baris Preferences (PC-13).
  - TC-FA-PREF-510: transaksi bertanggal 15 Mei 2026 sudah ada, Fiscal Year Start tersimpan January, First Accounting Period tersimpan Mar 2026 (PC-4, PC-16).
  Data modul Depreciation Run, Export Journal, transaksi, dan Accounting Period (`settings-accounting-period/`) disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences (termasuk company tanpa baris Preferences dan setting wajib kosong), pelepasan menunggu posting, dan transaksi bertanggal; pembacaan nilai Preferences yang dibaca Depreciation Run; pembacaan label tahun fiskal transaksi dan periode.
- State global yang diubah: Preferences company (setting wajib, Depreciation in Disposal Month, Fiscal Year Start, baris Preferences) dan periode akuntansi hasil pembangunan ulang; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-504: Depreciation Run terblokir selama banner Setup Incomplete tampil

1. Seed In-service Date Source tersimpan kosong sehingga banner Setup Incomplete tampil hingga tersimpan
2. Buka Depreciation Run dan coba jalankan prosesnya
3. Verifikasi Depreciation Run terblokir sampai setting wajib terisi

### TC-FA-PREF-505: Export Journal terblokir selama banner Setup Incomplete tampil

4. Buka Export Journal dan coba jalankan prosesnya
5. Verifikasi Export Journal terblokir sampai setting wajib terisi

### TC-FA-PREF-506: Depreciation Run dan Export Journal tidak terblokir saat seluruh setting wajib terisi

6. Seed seluruh setting wajib tersimpan terisi hingga tersimpan
7. Buka Depreciation Run dan coba jalankan prosesnya
8. Verifikasi Depreciation Run tidak terblokir oleh Preferences
9. Buka Export Journal dan coba jalankan prosesnya
10. Verifikasi Export Journal tidak terblokir oleh Preferences

### TC-FA-PREF-507: Modul konsumen membaca nilai Preferences baru pada pembacaan berikutnya

11. Seed Depreciation in Disposal Month tersimpan "Up to previous month" dan 3 pelepasan belum diposting hingga tersimpan
12. Buka Fixed Asset > Settings > Accounting > Preferences
13. Pilih "Including disposal month" pada Select Depreciation in Disposal Month
14. Klik [Save changes]
15. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "3 disposals waiting posting are affected." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
16. Klik [Save] pada dialog Save Changes
17. Tunggu aksi selesai
18. Buka Depreciation Run
19. Verifikasi Depreciation Run membaca Including disposal month pada pembacaan berikutnya

### TC-FA-PREF-509: Konsumen memperlakukan company tanpa baris Preferences sebagai tidak tersedia

20. Seed company dengan modul akuntansi aktif tetapi tanpa baris Preferences hingga tersimpan
21. Buka Depreciation Run
22. Verifikasi nilai Preferences diperlakukan tidak tersedia oleh Depreciation Run

### TC-FA-PREF-510: Label tahun fiskal transaksi mengikuti hasil pembangunan ulang periode

23. Seed transaksi bertanggal 15 Mei 2026, Fiscal Year Start tersimpan January, dan First Accounting Period tersimpan Mar 2026 hingga tersimpan
24. Buka Fixed Asset > Settings > Accounting > Preferences
25. Pilih "April" pada Select Fiscal Year Start
26. Klik [Save changes]
27. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "13 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
28. Klik [Save] pada dialog Save Changes
29. Tunggu aksi selesai
30. Buka transaksi bertanggal 15 Mei 2026
31. Buka daftar periode di modul Accounting Period (`settings-accounting-period/`)
32. Atur ukuran halaman ke 25
33. Verifikasi label tahun fiskal transaksi 15 Mei 2026 sama dengan tahun fiskal periode Mei 2026 pada Accounting Period setelah pembangunan ulang
34. Pulihkan Preferences ke nilai awal PC-1 dan periode akuntansi ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 12 dan 24 (membuka layar Preferences sesudah seed), langkah 17 dan 29 ("Tunggu aksi selesai", bagian 8b butir 8, karena langkah berikutnya berpindah modul), langkah 34 (pemulihan state, S-09, R-08).
- Langkah 4 memakai state seed langkah 1 (TC-FA-PREF-504 dan 505 memiliki Precondition yang sama); TC lain memakai seed sendiri (langkah 6, 11, 20, 23) sehingga tidak bergantung hasil TC sebelumnya.
- Langkah 30 membuka transaksi bertanggal 15 Mei 2026 tanpa Search karena TC tidak menyebut nama transaksi; pada langkah 31 dan 32 daftar periode dibuka dengan ukuran halaman 25 sehingga periode Mei 2026 terlihat tanpa pindah halaman.
- TC-FA-PREF-508 (ErrorState konsumen saat pembacaan Preferences gagal) ada di spec 096 (resilience kelas b).
- Temuan untuk QA:
  - TC-FA-PREF-504 dan 505 menyebut "coba jalankan prosesnya" tanpa menyebut tanda "terblokir" (disabled, pesan, atau penolakan); spec mengasersi teks Expected apa adanya.
  - TC-FA-PREF-507 Expected b ("membaca Including disposal month pada pembacaan berikutnya") tidak menyebut lokasi tampilnya nilai pada Depreciation Run; spec mengasersi teks Expected apa adanya.
  - TC-FA-PREF-509 Expected tidak menyebut tampilan "tidak tersedia" pada Depreciation Run; spec mengasersi teks Expected apa adanya.
  - TC-FA-PREF-510 Expected b membutuhkan pembacaan label tahun fiskal pada transaksi dan periode tanpa menyebut elemen UI yang menampilkannya; nilai label tidak ditulis di spec.
  - TC-FA-PREF-506 Expected a dan b tidak menyebut tanda "tidak terblokir"; spec mengasersi teks Expected apa adanya.
  - Post Condition TC-FA-PREF-504 sampai 510 yang ada ("Preferences tidak berubah", "Label tahun fiskal diturunkan dari periode dan tidak disimpan di transaksi", "Nilai yang dibaca konsumen mengikuti Preferences") tidak punya langkah observasi terpisah di TC dan tidak diasersi selain Expected (S-01).
