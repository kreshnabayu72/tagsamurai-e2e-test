---
id: TC-FA-PREF-E2E-143-deferred-jurnal-pelepasan-ditahan-saat-akun-kosong-gain-loss-donate-dan-trade-in
title: "[DEFERRED] Jurnal pelepasan ditahan saat akun kosong (Gain, Loss, Donate, Trade-in)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-449
  - TC-FA-PREF-450
  - TC-FA-PREF-451
  - TC-FA-PREF-452
coverage:
  web: automated
---

# [DEFERRED] Jurnal pelepasan ditahan saat akun kosong (Gain, Loss, Donate, Trade-in)

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik dan konsumen yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (Default Gain on Disposal dan Default Loss on Disposal kosong); Asset Class PC-6 (IT Equipment mengosongkan akun Gain dan Loss); aset 'disposal - 28' kelas IT Equipment (PC-16) dengan kondisi pelepasan per TC:
  - TC-FA-PREF-449: dijual (Sell) di atas nilai buku.
  - TC-FA-PREF-450: dijual (Sell) di bawah nilai buku.
  - TC-FA-PREF-451: dilepas dengan jenis Donate.
  - TC-FA-PREF-452: dilepas dengan jenis Trade-in dengan selisih terhadap nilai buku.
  Data modul Disposal Posting dan Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed pelepasan dengan jenis dan selisih nilai buku yang ditentukan; posting pelepasan lewat UI Disposal Posting; pembacaan status ditahan jurnal pada Export Journal.
- State global yang diubah: status posting pelepasan 'disposal - 28'; dikembalikan ke nilai awal oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah). Preferences tidak diubah spec ini.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-449: Jurnal pelepasan di atas nilai buku ditahan saat akun Gain kosong

1. Seed Default Gain on Disposal dan Default Loss on Disposal tersimpan kosong, Asset Class IT Equipment mengosongkan akun Gain dan Loss, dan aset 'disposal - 28' kelas IT Equipment dijual (Sell) di atas nilai buku hingga tersimpan
2. Posting pelepasan 'disposal - 28' pada Disposal Posting
3. Verifikasi pelepasan 'disposal - 28' terposting
4. Buka Export Journal
5. Ketik Search "disposal - 28", tekan Enter
6. Verifikasi jurnal pelepasan 'disposal - 28' ditahan sebagai exception "Gain/Loss account not set" karena akun Gain kosong setelah akun Asset Class dan akun default

### TC-FA-PREF-450: Jurnal pelepasan di bawah nilai buku ditahan saat akun Loss kosong

7. Seed Default Gain on Disposal dan Default Loss on Disposal tersimpan kosong, Asset Class IT Equipment mengosongkan akun Gain dan Loss, dan aset 'disposal - 28' kelas IT Equipment dijual (Sell) di bawah nilai buku hingga tersimpan
8. Posting pelepasan 'disposal - 28' pada Disposal Posting
9. Verifikasi pelepasan 'disposal - 28' terposting
10. Buka Export Journal
11. Ketik Search "disposal - 28", tekan Enter
12. Verifikasi jurnal pelepasan 'disposal - 28' ditahan sebagai exception "Gain/Loss account not set" karena akun Loss kosong setelah akun Asset Class dan akun default

### TC-FA-PREF-451: Jurnal pelepasan Donate ditahan saat akun yang dibutuhkan kosong

13. Seed Default Gain on Disposal dan Default Loss on Disposal tersimpan kosong, Asset Class IT Equipment mengosongkan akun Gain dan Loss, dan aset 'disposal - 28' kelas IT Equipment dilepas dengan jenis Donate hingga tersimpan
14. Posting pelepasan 'disposal - 28' pada Disposal Posting
15. Verifikasi pelepasan 'disposal - 28' terposting
16. Buka Export Journal
17. Ketik Search "disposal - 28", tekan Enter
18. Verifikasi jurnal pelepasan 'disposal - 28' ditahan sebagai exception "Gain/Loss account not set" karena akun Loss kosong setelah akun Asset Class dan akun default

### TC-FA-PREF-452: Jurnal pelepasan Trade-in ditahan saat akun yang dibutuhkan kosong

19. Seed Default Gain on Disposal dan Default Loss on Disposal tersimpan kosong, Asset Class IT Equipment mengosongkan akun Gain dan Loss, dan aset 'disposal - 28' kelas IT Equipment dilepas dengan jenis Trade-in dengan selisih terhadap nilai buku hingga tersimpan
20. Posting pelepasan 'disposal - 28' pada Disposal Posting
21. Verifikasi pelepasan 'disposal - 28' terposting
22. Buka Export Journal
23. Ketik Search "disposal - 28", tekan Enter
24. Verifikasi jurnal pelepasan 'disposal - 28' ditahan sebagai exception "Gain/Loss account not set" karena akun yang dibutuhkan kosong setelah akun Asset Class dan akun default
25. Pulihkan status posting pelepasan 'disposal - 28' ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 4, 10, 16, dan 22 (membuka Export Journal), langkah 5, 11, 17, dan 23 (Search sebagai langkah penghubung untuk menemukan baris target, R-16, R-23), langkah 25 (pemulihan state, S-09, R-08).
- Keempat TC memakai aset bernama sama 'disposal - 28' dengan jenis dan selisih nilai buku berbeda; seed ulang pada langkah 1, 7, 13, dan 19 membentuk precondition tiap TC tanpa bergantung hasil posting TC sebelumnya.
- Temuan untuk QA:
  - TC-FA-PREF-449 sampai 452 menulis Expected "Pelepasan terposting" tanpa menyebut tempat teramatinya status posting; langkah 3, 9, 15, dan 21 mengasersi status pada Disposal Posting setelah posting, sedangkan Expected b diasersi pada Export Journal.
  - TC-FA-PREF-451 dan 452 menyebut "akun yang dibutuhkan" tanpa menyatakan akun Gain atau Loss secara spesifik pada Precondition; spec mengikuti Expected TC (451: akun Loss; 452: akun yang dibutuhkan).
  - TC-FA-PREF-449 sampai 452 tidak menyebut nilai buku atau harga jual aset; spec hanya menyebut "di atas", "di bawah", atau "dengan selisih" terhadap nilai buku sesuai TC.
  - Post Condition TC-FA-PREF-449 sampai 452 ("Jurnal ditahan sampai akun diisi") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-PREF-448 dan 453 (pelepasan tetap diposting saat akun kosong dan tepat nilai buku) ada di spec 142.
