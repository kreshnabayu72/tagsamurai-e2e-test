---
id: TC-FA-PREF-E2E-142-deferred-akun-gain-dan-loss-default-pada-asset-class-dan-jurnal-pelepasan
title: "[DEFERRED] Akun Gain dan Loss default pada Asset Class dan jurnal pelepasan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-445
  - TC-FA-PREF-446
  - TC-FA-PREF-447
  - TC-FA-PREF-448
  - TC-FA-PREF-453
coverage:
  web: automated
---

# [DEFERRED] Akun Gain dan Loss default pada Asset Class dan jurnal pelepasan

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik dan konsumen yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1; Chart of Accounts PC-5 (`4-9100 – Laba Pelepasan Aset`, `5-9100 – Rugi Pelepasan Aset`, `4-7002 – Gain and Loss on Disposal`); Asset Class PC-6 (IT Equipment: akun Gain dan Loss kosong; Vehicles: akun Gain kosong, akun Loss terisi; Furniture: kedua akun terisi). Aset dan pelepasan PC-16, disediakan tim FE setelah modul Disposal Posting dan Export Journal tersedia:
  - 'disposal - 24' kelas Vehicles dijual di atas nilai buku (TC-FA-PREF-445).
  - 'disposal - 25' kelas IT Equipment dijual di bawah nilai buku (TC-FA-PREF-446).
  - 'disposal - 26' laptop kelas IT Equipment dijual di atas nilai buku (TC-FA-PREF-447).
  - 'disposal - 27' kelas IT Equipment dijual di atas nilai buku (TC-FA-PREF-448).
  - 'disposal - 29' dijual tepat sebesar nilai buku (TC-FA-PREF-453; pada TC-FA-PREF-448 dipakai sebagai jurnal pembanding yang sudah diposting).
- Nilai default Preferences per TC (dibentuk lewat seed, tidak lewat UI): TC-FA-PREF-445 Default Gain on Disposal `4-9100 – Laba Pelepasan Aset`; TC-FA-PREF-446 Default Loss on Disposal `5-9100 – Rugi Pelepasan Aset`; TC-FA-PREF-447 Default Gain dan Default Loss `4-7002 – Gain and Loss on Disposal`; TC-FA-PREF-448 dan 453 kosong. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences, Asset Class, aset, dan pelepasan dengan nilai buku dan harga jual yang ditentukan; posting pelepasan lewat UI Disposal Posting; pembacaan akun dan status ditahan jurnal pada Export Journal.
- State global yang diubah: nilai default Gain dan Loss on Disposal company dan status posting pelepasan; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-445: Asset Class yang mengosongkan akun Gain memakai akun default Gain company

1. Seed Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset", Asset Class Vehicles mengosongkan akun Gain, dan aset 'disposal - 24' kelas Vehicles dijual di atas nilai buku hingga tersimpan
2. Posting pelepasan 'disposal - 24' pada Disposal Posting
3. Buka Export Journal
4. Ketik Search "disposal - 24", tekan Enter
5. Buka jurnal pelepasan 'disposal - 24'
6. Verifikasi jurnal pelepasan 'disposal - 24' memakai akun "4-9100 – Laba Pelepasan Aset"

### TC-FA-PREF-446: Asset Class yang mengosongkan akun Loss memakai akun default Loss company

7. Seed Default Loss on Disposal tersimpan "5-9100 – Rugi Pelepasan Aset", Asset Class IT Equipment mengosongkan akun Loss, dan aset 'disposal - 25' kelas IT Equipment dijual di bawah nilai buku hingga tersimpan
8. Posting pelepasan 'disposal - 25' pada Disposal Posting
9. Buka Export Journal
10. Ketik Search "disposal - 25", tekan Enter
11. Buka jurnal pelepasan 'disposal - 25'
12. Verifikasi jurnal pelepasan 'disposal - 25' memakai akun "5-9100 – Rugi Pelepasan Aset"

### TC-FA-PREF-447: Akun gabungan Gain dan Loss dipakai jurnal pelepasan di atas nilai buku

13. Seed Default Gain on Disposal dan Default Loss on Disposal tersimpan "4-7002 – Gain and Loss on Disposal", Asset Class IT Equipment mengosongkan akun Gain dan Loss, dan laptop 'disposal - 26' kelas IT Equipment dijual di atas nilai buku hingga tersimpan
14. Posting pelepasan 'disposal - 26' pada Disposal Posting
15. Buka Export Journal
16. Ketik Search "disposal - 26", tekan Enter
17. Buka jurnal pelepasan 'disposal - 26'
18. Verifikasi jurnal pelepasan 'disposal - 26' memakai akun "4-7002 – Gain and Loss on Disposal"
19. Verifikasi pelepasan 'disposal - 26' terposting
20. Verifikasi jurnal pelepasan 'disposal - 26' tidak ditahan

### TC-FA-PREF-448: Pelepasan tetap dapat diposting bila akun Asset Class dan akun default sama-sama kosong

21. Seed Default Gain on Disposal dan Default Loss on Disposal tersimpan kosong, Asset Class IT Equipment mengosongkan akun Gain dan Loss, aset 'disposal - 27' kelas IT Equipment dijual di atas nilai buku, dan pelepasan 'disposal - 29' tepat sebesar nilai buku sudah diposting sebagai jurnal pembanding hingga tersimpan
22. Posting pelepasan 'disposal - 27' pada Disposal Posting
23. Verifikasi posting pelepasan 'disposal - 27' berhasil
24. Verifikasi pelepasan 'disposal - 27' terposting seperti posting pelepasan biasa menurut Disposal Posting
25. Buka Export Journal
26. Ketik Search "disposal - 2", tekan Enter
27. Verifikasi jurnal pelepasan 'disposal - 27' ditahan sebagai exception "Gain/Loss account not set"
28. Verifikasi jurnal pelepasan 'disposal - 29' tidak ditahan sebagai exception

### TC-FA-PREF-453: Pelepasan tepat sebesar nilai buku tidak membutuhkan akun Gain atau Loss

29. Seed Default Gain on Disposal dan Default Loss on Disposal tersimpan kosong, Asset Class IT Equipment mengosongkan akun Gain dan Loss, dan aset 'disposal - 29' dijual tepat sebesar nilai buku hingga tersimpan
30. Posting pelepasan 'disposal - 29' pada Disposal Posting
31. Buka Export Journal
32. Ketik Search "disposal - 29", tekan Enter
33. Buka jurnal pelepasan 'disposal - 29'
34. Verifikasi jurnal pelepasan 'disposal - 29' tidak ditahan sebagai exception "Gain/Loss account not set"
35. Pulihkan Preferences ke nilai awal PC-1 dan status posting pelepasan ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 3, 9, 15, 25, dan 31 (membuka Export Journal), langkah 4, 10, 16, 26, dan 32 (Search sebagai langkah penghubung untuk menemukan baris target, R-16, R-23), langkah 5, 11, 17, dan 33 (membuka jurnal dari hasil Search), langkah 35 (pemulihan state, S-09, R-08). Search "disposal - 2" pada langkah 26 menampilkan jurnal 'disposal - 27' dan 'disposal - 29' sekaligus (kedua nama memuat awalan "disposal - 2"), sehingga Verifikasi langkah 27 dan 28 dibaca pada hasil Search yang sama.
- Langkah 28 adalah asersi tambahan di luar Expected TC-FA-PREF-448: klausa "Hanya jurnal pelepasan 'disposal - 27' yang ditahan" diasersi dengan jurnal pembanding 'disposal - 29' yang tidak ditahan (bagian 8b butir 2); jurnal pembanding di-seed pada langkah 21.
- Seed Preferences pada langkah 1, 7, 13, 21, dan 29 membentuk precondition tiap TC tanpa bergantung hasil TC sebelumnya; nilai default tidak diubah lewat UI.
- Temuan untuk QA:
  - TC-FA-PREF-447 Expected b ("Pelepasan terposting dan jurnalnya tidak ditahan") memuat dua klausa dan ditulis dua `Verifikasi` (langkah 19 dan 20, S-01).
  - TC-FA-PREF-448 Expected b menyatakan hasil posting dimiliki modul Pelepasan (OI-21) tanpa kriteria teramati; langkah 24 mengasersi teks Expected apa adanya.
  - TC-FA-PREF-445 dan 446 tidak menyebut nilai buku dan harga jual aset; spec hanya menyebut "di atas" atau "di bawah" nilai buku sesuai TC.
  - TC-FA-PREF-445 sampai 448 dan 453 memakai langkah "Buka Export Journal" tanpa menyebut cara mencari jurnal per aset; spec memakai Search nama pelepasan (langkah penghubung).
  - Post Condition TC-FA-PREF-445, 446, 447, 448, dan 453 adalah kesimpulan dari Expected dan tidak diasersi terpisah (S-01).
  - TC-FA-PREF-449 sampai 452 (jurnal ditahan karena akun kosong) ada di spec 143.
