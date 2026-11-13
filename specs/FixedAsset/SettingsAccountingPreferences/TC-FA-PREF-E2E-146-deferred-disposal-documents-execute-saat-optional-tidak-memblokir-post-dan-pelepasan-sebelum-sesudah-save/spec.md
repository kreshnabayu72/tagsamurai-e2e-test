---
id: TC-FA-PREF-E2E-146-deferred-disposal-documents-execute-saat-optional-tidak-memblokir-post-dan-pelepasan-sebelum-sesudah-save
title: "[DEFERRED] Disposal Documents: Execute saat Optional, tidak memblokir Post, pelepasan sebelum dan sesudah Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-466
  - TC-FA-PREF-467
  - TC-FA-PREF-468
  - TC-FA-PREF-469
  - TC-FA-PREF-470
coverage:
  web: automated
---

# [DEFERRED] Disposal Documents: Execute saat Optional, tidak memblokir Post, pelepasan sebelum dan sesudah Save

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (Disposal Documents keenam jenis Optional). Data modul Disposal (PC-16) disediakan tim FE setelah modul tersedia: baris pelepasan jenis Sell berstatus Waiting for Execution untuk TC-FA-PREF-466, 467, dan 469 (masing-masing satu baris sendiri, tanpa dokumen), baris 'disposal - 30' jenis Sell berstatus Executed dengan satu dokumen untuk TC-FA-PREF-468 (tab Waiting to Post), dan baris jenis Sell berstatus Executed tanpa dokumen untuk TC-FA-PREF-470. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Disposal Documents jenis Sell per TC (dibentuk lewat seed): Optional untuk TC-FA-PREF-466, 467, 469, 470; Required untuk TC-FA-PREF-468.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan baris pelepasan dengan status yang ditentukan; pengisian field wajib form Execute dan lampiran dokumen lewat UI modul pemilik; Post lewat tab Waiting to Post pada Disposal.
- State global yang diubah: Disposal Documents jenis Sell company; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-466: Execute pelepasan Sell dengan dokumen berhasil saat Optional

1. Seed Disposal Documents jenis Sell tersimpan Optional hingga tersimpan
2. Buka form Execute baris pelepasan jenis Sell berstatus Waiting for Execution pada Disposal Execute dan isi semua field wajib
3. Lampirkan satu dokumen
4. Klik Execute
5. Verifikasi baris pelepasan jenis Sell ter-Execute

### TC-FA-PREF-467: Execute pelepasan Sell tanpa dokumen berhasil saat Optional

6. Buka form Execute baris pelepasan jenis Sell berstatus Waiting for Execution pada Disposal Execute dan isi semua field wajib
7. Klik Execute tanpa melampirkan dokumen
8. Verifikasi baris pelepasan jenis Sell ter-Execute
9. Verifikasi pesan V-07 tidak tampil

### TC-FA-PREF-468: Disposal Documents Required tidak memblokir Post pelepasan

10. Seed Disposal Documents jenis Sell tersimpan Required dan baris pelepasan 'disposal - 30' jenis Sell berstatus Executed dengan satu dokumen hingga tersimpan
11. Post pelepasan 'disposal - 30' dari tab Waiting to Post pada Disposal
12. Verifikasi Post pelepasan 'disposal - 30' berhasil
13. Verifikasi Post tidak diblokir oleh setting Disposal Documents

### TC-FA-PREF-469: Pelepasan yang diajukan sebelum Save dan di-Execute sesudahnya memakai nilai Required yang baru

14. Seed Disposal Documents jenis Sell tersimpan Optional dan baris pelepasan jenis Sell berstatus Waiting for Execution tanpa dokumen hingga tersimpan
15. Buka Fixed Asset > Settings > Accounting > Preferences
16. Pilih "Required" pada Select Disposal Documents jenis Sell
17. Klik [Save changes]
18. Verifikasi toast "Success, accounting preferences have been saved." tampil
19. Buka form Execute baris pelepasan jenis Sell yang Waiting for Execution pada Disposal Execute
20. Klik Execute tanpa melampirkan dokumen
21. Verifikasi pesan "A document is required for sell disposals." tampil
22. Verifikasi baris pelepasan tidak ter-Execute

### TC-FA-PREF-470: Pelepasan yang sudah di-Execute tidak dievaluasi ulang setelah Disposal Documents berubah

23. Seed Disposal Documents jenis Sell tersimpan Optional dan baris pelepasan jenis Sell berstatus Executed tanpa dokumen hingga tersimpan
24. Buka Fixed Asset > Settings > Accounting > Preferences
25. Pilih "Required" pada Select Disposal Documents jenis Sell
26. Klik [Save changes]
27. Verifikasi toast "Success, accounting preferences have been saved." tampil
28. Buka baris pelepasan jenis Sell yang sudah Executed pada Disposal Execute (tab Waiting to Post)
29. Verifikasi baris tetap berstatus Executed
30. Verifikasi pesan V-07 tidak tampil
31. Verifikasi baris tidak ditolak
32. Pulihkan Disposal Documents jenis Sell ke "Optional" lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 15 dan 24 (membuka layar Preferences sesudah seed), langkah 32 (pemulihan state, S-09, R-08).
- TC-FA-PREF-466 dan 467 memakai nilai Preferences yang sama (Optional) dan satu seed pada langkah 1; TC-FA-PREF-468, 469, dan 470 memakai seed sendiri (langkah 10, 14, dan 23) sehingga tidak bergantung hasil TC sebelumnya.
- Asersi absence "pesan V-07 tidak tampil" (langkah 9 dan 30) memakai anchor positif: pada langkah 9 status ter-Execute (langkah 8) dan pada langkah 30 status Executed (langkah 29) menjadi bukti halaman termuat sebelum absence diasersi (bagian 8b butir 2). Asersi tersebut berasal dari Expected TC, bukan asersi log (kelas g).
- Temuan untuk QA:
  - TC-FA-PREF-468 dan 470 tidak menyebut label tombol Post atau cara membuka baris Executed; spec memakai teks TC (tab Waiting to Post pada Disposal) dan seed disediakan tim FE.
  - TC-FA-PREF-470 Expected b memuat tiga klausa ("tetap berstatus Executed", "tanpa pesan V-07", "tanpa penolakan") dan ditulis tiga `Verifikasi` (langkah 29 sampai 31, S-01).
  - TC-FA-PREF-468 Expected ("Posting berhasil tanpa diblokir oleh setting Disposal Documents") memuat dua klausa dan ditulis dua `Verifikasi` (langkah 12 dan 13); tanda teramati "tidak diblokir" tidak disebut di TC.
  - TC-FA-PREF-466 dan 467 Expected tidak menyebut toast atau tanda ter-Execute selain "Baris ter-Execute"; spec mengasersi teks itu apa adanya.
  - Post Condition TC-FA-PREF-466 sampai 470 ("Baris berstatus Executed", "Pelepasan terposting", "Baris tetap Waiting for Execution", "Baris yang sudah Executed tidak berubah") tidak punya langkah observasi terpisah di TC dan tidak diasersi selain yang tertulis di Expected (S-01).
  - TC-FA-PREF-469 dan 470 mensyaratkan baris pelepasan sudah ada sebelum Save; spec men-seed baris sebelum Save lewat langkah 14 dan 23.
