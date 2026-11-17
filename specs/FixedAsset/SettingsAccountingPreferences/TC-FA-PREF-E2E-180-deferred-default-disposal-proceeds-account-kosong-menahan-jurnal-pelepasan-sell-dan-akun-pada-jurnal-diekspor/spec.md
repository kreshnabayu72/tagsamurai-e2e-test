---
id: TC-FA-PREF-E2E-180-deferred-default-disposal-proceeds-account-kosong-menahan-jurnal-pelepasan-sell-dan-akun-pada-jurnal-diekspor
title: "[DEFERRED] Default Disposal Proceeds Account kosong menahan jurnal pelepasan Sell, diekspor setelah diisi, dan jurnal yang sudah diekspor tidak berubah"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-629
  - TC-FA-PREF-630
  - TC-FA-PREF-631
sourceRules: ["FAPREF-LOGIC-06k", "FAPREF-LOGIC-10j", "F-FAPREF-01.k22b", "T-01", "FAPREF-LOGIC-06f", "FAPREF-LOGIC-06g", "§11.2#r8"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-06k": [5, 8]
  "FAPREF-LOGIC-10j": [13, 23]
  "F-FAPREF-01.k22b": [14, 24]
  "T-01": [14, 24]
  "FAPREF-LOGIC-06f": 18
  "FAPREF-LOGIC-06g": [18, 28]
  "§11.2#r8": 28
anchor: [6]
coverage:
  web: automated
---

# [DEFERRED] Default Disposal Proceeds Account kosong menahan jurnal pelepasan Sell, diekspor setelah diisi, dan jurnal yang sudah diekspor tidak berubah

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik dan konsumen yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 dengan Default Gain on Disposal dan Default Loss on Disposal terisi; Chart of Accounts PC-22 (Active `1-3100 – Kliring Hasil Pelepasan` dan `1-3110 – Kliring Hasil Pelepasan Cabang`, function Disposal Proceeds); PC-16: satu pelepasan Sell berstatus Executed dengan Proceeds lebih dari 0 untuk TC-FA-PREF-629, jurnal pelepasan Sell yang sudah diposting dan ditahan dengan alasan `Proceeds account not set` untuk TC-FA-PREF-630, dan jurnal pelepasan Sell yang sudah diekspor dengan akun `1-3100 – Kliring Hasil Pelepasan` untuk TC-FA-PREF-631. Data modul Disposal dan Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences, pelepasan Executed, jurnal ditahan, dan jurnal yang sudah diekspor; Post lewat tab Waiting to Post pada Disposal; ekspor jurnal pelepasan lewat UI Export Journal; pembacaan akun jurnal pada Export Journal.
- State global yang diubah: Default Disposal Proceeds Account company, status Posted baris pelepasan, dan status ekspor jurnal pelepasan; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-629: Default Disposal Proceeds Account kosong menahan jurnal pelepasan Sell di Export Journal dan Post tidak diblokir

1. Seed Default Disposal Proceeds Account tersimpan kosong, Default Gain on Disposal dan Default Loss on Disposal terisi, serta satu pelepasan Sell berstatus Executed dengan Proceeds lebih dari 0 hingga tersimpan
2. Buka tab Waiting to Post pada Disposal
3. Klik Post pada baris pelepasan Sell itu
4. Tunggu aksi selesai
5. Verifikasi baris pelepasan Sell itu berstatus Posted
6. Verifikasi nomor jurnal tersimpan di baris pelepasan Sell itu
7. Buka Export Journal
8. Verifikasi jurnal pelepasan itu ditahan di Export Journal sebagai exception `Proceeds account not set`

### TC-FA-PREF-630: Jurnal pelepasan yang ditahan karena akun Proceeds kosong dapat diekspor setelah akun diisi tanpa posting ulang

9. Seed Default Disposal Proceeds Account tersimpan kosong dan jurnal pelepasan Sell sudah diposting dan ditahan dengan alasan `Proceeds account not set` hingga tersimpan
10. Buka Fixed Asset > Settings > Accounting > Preferences
11. Pilih "1-3100 – Kliring Hasil Pelepasan" pada Select Default Disposal Proceeds Account
12. Klik [Save changes]
13. Verifikasi dialog Save Changes tidak tampil
14. Verifikasi toast "Success, accounting preferences have been saved." tampil
15. Tunggu aksi selesai
16. Buka Export Journal
17. Ekspor jurnal pelepasan yang ditahan pada Export Journal
18. Verifikasi jurnal pelepasan diekspor dengan baris Proceeds pada akun "1-3100 – Kliring Hasil Pelepasan" tanpa posting ulang

### TC-FA-PREF-631: Jurnal pelepasan yang sudah diekspor tidak berubah saat Default Disposal Proceeds Account diganti

19. Seed Default Disposal Proceeds Account tersimpan "1-3100 – Kliring Hasil Pelepasan" dan jurnal pelepasan Sell sudah diekspor dengan akun "1-3100 – Kliring Hasil Pelepasan" hingga tersimpan
20. Buka Fixed Asset > Settings > Accounting > Preferences
21. Pilih "1-3110 – Kliring Hasil Pelepasan Cabang" pada Select Default Disposal Proceeds Account
22. Klik [Save changes]
23. Verifikasi dialog Save Changes tidak tampil
24. Verifikasi toast "Success, accounting preferences have been saved." tampil
25. Tunggu aksi selesai
26. Buka Export Journal
27. Buka jurnal pelepasan Sell yang sudah diekspor
28. Verifikasi jurnal pelepasan yang sudah diekspor tetap memakai akun "1-3100 – Kliring Hasil Pelepasan"
29. Pulihkan Preferences ke nilai awal PC-1 dan status ekspor jurnal ke nilai awal lewat seed hingga tersimpan

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 4, 15, dan 25 ("Tunggu aksi selesai", bagian 8b butir 8, karena langkah berikutnya berpindah modul), langkah 2, 7, 16, dan 26 (membuka tab Waiting to Post dan Export Journal), langkah 10 dan 20 (membuka layar Preferences sesudah seed), langkah 29 (pemulihan state, S-09, R-08).
- Tiap TC memakai seed sendiri (langkah 1, 9, dan 19) sehingga tidak bergantung hasil TC sebelumnya.
- Spec ini hanya memuat TC `[DEFERRED]` seri Default Disposal Proceeds Account; TC-FA-PREF-622 sampai 628 ada di spec 177, 178, dan 179.
- Temuan untuk QA:
  - TC-FA-PREF-629 langkah 1 ("klik Post pada baris Sell itu") dan Expected a ("nomor jurnal tersimpan di baris") tidak menyebut label kolom atau tanda teramati nomor jurnal; spec memakai teks TC.
  - TC-FA-PREF-629 Expected a memuat dua klausa ("baris menjadi Posted", "nomor jurnal tersimpan di baris") dan ditulis dua `Verifikasi` (langkah 5 dan 6, S-01).
  - TC-FA-PREF-630 Expected b menyebut "tanpa posting ulang" tanpa tanda teramati; langkah 18 mengasersi teks Expected apa adanya pada hasil ekspor. Langkah TC 3 ("ekspor jurnal pelepasan yang ditahan") tidak menyebut cara menemukan baris di Export Journal; spec tidak memakai Search karena jurnal ditahan tunggal pada seed.
  - TC-FA-PREF-631 langkah TC 3 ("Buka jurnal pelepasan yang sudah diekspor") tidak menyebut tempat pembacaan akun jurnal; spec membacanya pada jurnal yang dibuka dari Export Journal.
  - Post Condition TC-FA-PREF-629 ("Baris Posted; jurnal ditahan"), 630, dan 631 adalah kesimpulan dari Expected dan tidak diasersi terpisah (S-01).
