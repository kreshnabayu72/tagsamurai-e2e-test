---
id: TC-FA-PREF-E2E-174-deferred-jurnal-pelepasan-terposting-belum-dan-sudah-diekspor-saat-akun-default-diganti
title: "[DEFERRED] Jurnal pelepasan terposting: belum diekspor memakai akun yang berlaku saat ekspor, sudah diekspor tidak berubah"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-456
  - TC-FA-PREF-457
sourceRules: ["D-01", "PV-02", "FAPREF-LOGIC-06g"]
smoke: []
dependsOn: []
trace:
  "D-01": [5, 16]
  "PV-02": [5, 16]
  "FAPREF-LOGIC-06g": [11, 22]
coverage:
  web: automated
---

# [DEFERRED] Jurnal pelepasan terposting: belum diekspor memakai akun yang berlaku saat ekspor, sudah diekspor tidak berubah

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik dan konsumen yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 dengan Default Gain on Disposal `4-9100 – Laba Pelepasan Aset`; Chart of Accounts PC-5 (`4-9100 – Laba Pelepasan Aset`, `4-7002 – Gain and Loss on Disposal`); Asset Class PC-6 (IT Equipment dan Vehicles mengosongkan akun Gain sehingga 2 Asset Class memakai akun default); 3 pelepasan belum diposting (PC-7); PC-16: pelepasan 'disposal - 24' sudah diposting tetapi jurnalnya belum diekspor (TC-FA-PREF-456) dan jurnal pelepasan 'disposal - 25' sudah diekspor dengan akun `4-9100 – Laba Pelepasan Aset` (TC-FA-PREF-457). Data modul Disposal Posting dan Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences, pelepasan terposting, dan jurnal yang sudah diekspor; ekspor jurnal pelepasan lewat UI Export Journal; pembacaan akun jurnal pada Export Journal.
- State global yang diubah: Default Gain on Disposal company dan status ekspor jurnal pelepasan; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-456: Jurnal pelepasan terposting yang belum diekspor memakai akun default yang berlaku saat diekspor

1. Seed Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset", pelepasan 'disposal - 24' sudah diposting dengan jurnal belum diekspor, serta 3 pelepasan belum diposting hingga tersimpan
2. Buka Fixed Asset > Settings > Accounting > Preferences
3. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Gain on Disposal
4. Klik [Save changes]
5. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default account. 3 unposted disposals will use the new account." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
6. Klik [Save] pada dialog Save Changes
7. Tunggu aksi selesai
8. Buka Export Journal
9. Ketik Search "disposal - 24", tekan Enter
10. Ekspor jurnal pelepasan 'disposal - 24' pada Export Journal
11. Verifikasi jurnal pelepasan 'disposal - 24' diekspor dengan akun "4-7002 – Gain and Loss on Disposal" tanpa posting ulang

### TC-FA-PREF-457: Jurnal pelepasan yang sudah diekspor tidak berubah saat akun default diganti

12. Seed Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset", jurnal pelepasan 'disposal - 25' sudah diekspor dengan akun "4-9100 – Laba Pelepasan Aset", serta 3 pelepasan belum diposting hingga tersimpan
13. Buka Fixed Asset > Settings > Accounting > Preferences
14. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Gain on Disposal
15. Klik [Save changes]
16. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default account. 3 unposted disposals will use the new account." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
17. Klik [Save] pada dialog Save Changes
18. Tunggu aksi selesai
19. Buka Export Journal
20. Ketik Search "disposal - 25", tekan Enter
21. Buka jurnal pelepasan 'disposal - 25' yang sudah diekspor
22. Verifikasi jurnal pelepasan 'disposal - 25' tetap memakai akun "4-9100 – Laba Pelepasan Aset"
23. Pulihkan Preferences ke nilai awal PC-1 dan status ekspor jurnal ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 2 dan 13 (membuka layar Preferences sesudah seed), langkah 7 dan 18 ("Tunggu aksi selesai", bagian 8b butir 8, karena langkah berikutnya berpindah modul), langkah 8 dan 19 (membuka Export Journal), langkah 9 dan 20 (Search sebagai langkah penghubung untuk menemukan baris target, R-16, R-23), langkah 23 (pemulihan state, S-09, R-08).
- TC-FA-PREF-456 dan 457 memakai seed terpisah (langkah 1 dan 12) sehingga tiap TC tidak bergantung hasil TC sebelumnya.
- TC-FA-PREF-454 dan 455 (jurnal ditahan dapat diekspor, pelepasan belum diposting memakai akun baru) ada di spec 144.
- Temuan untuk QA:
  - TC-FA-PREF-456 Expected b menyebut "tanpa posting ulang" tanpa tanda teramati; langkah 11 mengasersi teks Expected apa adanya pada hasil ekspor.
  - TC-FA-PREF-456 dan 457 menyebut "3 unposted disposals" pada dialog tetapi precondition hanya menyebut PC-7 (3 pelepasan belum diposting) tanpa menyatakan hubungannya dengan 'disposal - 24' dan 'disposal - 25' (yang sudah diposting); spec men-seed 3 pelepasan belum diposting terpisah dari kedua aset itu.
  - TC-FA-PREF-457 langkah TC "Buka jurnal pelepasan 'disposal - 25' yang sudah diekspor" tidak menyebut tempat pembacaan akun jurnal; spec membacanya pada jurnal yang dibuka dari Export Journal.
  - Post Condition TC-FA-PREF-456 ("Akun yang berlaku saat ekspor dipakai") dan TC-FA-PREF-457 ("Jurnal yang sudah diekspor tidak berubah") adalah kesimpulan dari Expected dan tidak diasersi terpisah (S-01).
