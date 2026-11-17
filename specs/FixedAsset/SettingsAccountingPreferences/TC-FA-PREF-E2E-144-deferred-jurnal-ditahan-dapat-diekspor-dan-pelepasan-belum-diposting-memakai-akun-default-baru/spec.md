---
id: TC-FA-PREF-E2E-144-deferred-jurnal-ditahan-dapat-diekspor-dan-pelepasan-belum-diposting-memakai-akun-default-baru
title: "[DEFERRED] Jurnal ditahan dapat diekspor setelah akun diisi dan pelepasan belum diposting memakai akun default baru"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-454
  - TC-FA-PREF-455
sourceRules: ["D-01", "PV-02", "FAPREF-LOGIC-06f", "FAPREF-LOGIC-06g"]
smoke: []
dependsOn: []
trace:
  "D-01": [5, 15]
  "PV-02": [5, 15]
  "FAPREF-LOGIC-06f": 10
  "FAPREF-LOGIC-06g": 22
coverage:
  web: automated
---

# [DEFERRED] Jurnal ditahan dapat diekspor setelah akun diisi dan pelepasan belum diposting memakai akun default baru

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik dan konsumen yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1; Chart of Accounts PC-5 (`4-9100 – Laba Pelepasan Aset`, `4-7002 – Gain and Loss on Disposal`); Asset Class PC-6 (IT Equipment dan Vehicles mengosongkan akun Gain sehingga 2 Asset Class memakai akun default); 3 pelepasan belum diposting (PC-7); aset dan pelepasan PC-16 'disposal - 28' (TC-FA-PREF-454: jurnal ditahan sebagai exception "Gain/Loss account not set" karena akun Gain kosong) dan 'disposal - 23' (TC-FA-PREF-455: belum diposting, dijual di atas nilai buku, kelas IT Equipment mengosongkan akun Gain; salah satu dari 3 pelepasan PC-7). Data modul Disposal Posting dan Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Preferences per TC (dibentuk lewat seed): TC-FA-PREF-454 Default Gain on Disposal kosong; TC-FA-PREF-455 Default Gain on Disposal `4-9100 – Laba Pelepasan Aset`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences, Asset Class, pelepasan, dan jurnal ditahan; posting pelepasan lewat UI Disposal Posting; pembacaan akun dan status ekspor jurnal pada Export Journal.
- State global yang diubah: Default Gain on Disposal company dan status posting pelepasan; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-454: Jurnal yang ditahan dapat diekspor setelah akun diisi tanpa posting ulang

1. Seed Default Gain on Disposal tersimpan kosong, 3 pelepasan belum diposting, dan jurnal pelepasan 'disposal - 28' ditahan sebagai exception "Gain/Loss account not set" karena akun Gain kosong hingga tersimpan
2. Buka Fixed Asset > Settings > Accounting > Preferences
3. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
4. Klik [Save changes]
5. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default account. 3 unposted disposals will use the new account." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
6. Klik [Save] pada dialog Save Changes
7. Tunggu aksi selesai
8. Buka Export Journal
9. Ketik Search "disposal - 28", tekan Enter
10. Verifikasi jurnal pelepasan 'disposal - 28' dapat diekspor tanpa posting ulang

### TC-FA-PREF-455: Pelepasan yang belum diposting memakai akun default baru setelah Save

11. Seed Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset", pelepasan 'disposal - 23' belum diposting dan dijual di atas nilai buku, serta 3 pelepasan belum diposting hingga tersimpan
12. Buka Fixed Asset > Settings > Accounting > Preferences
13. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Gain on Disposal
14. Klik [Save changes]
15. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default account. 3 unposted disposals will use the new account." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
16. Klik [Save] pada dialog Save Changes
17. Tunggu aksi selesai
18. Posting pelepasan 'disposal - 23' pada Disposal Posting
19. Buka Export Journal
20. Ketik Search "disposal - 23", tekan Enter
21. Buka jurnal pelepasan 'disposal - 23'
22. Verifikasi jurnal pelepasan 'disposal - 23' memakai akun "4-7002 – Gain and Loss on Disposal"
23. Pulihkan Preferences ke nilai awal PC-1 dan status posting pelepasan ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 2 dan 12 (membuka layar Preferences sesudah seed), langkah 7 dan 17 ("Tunggu aksi selesai", bagian 8b butir 8, karena langkah berikutnya berpindah modul), langkah 8 dan 19 (membuka Export Journal), langkah 9 dan 20 (Search sebagai langkah penghubung untuk menemukan baris target, R-16, R-23), langkah 21 (membuka jurnal dari hasil Search), langkah 23 (pemulihan state, S-09, R-08).
- TC-FA-PREF-454 dan 455 memakai seed terpisah (langkah 1 dan 11) sehingga tiap TC tidak bergantung hasil TC sebelumnya.
- TC-FA-PREF-456 dan 457 (akun default baru pada jurnal terposting belum dan sudah diekspor) ada di spec 174.
- Temuan untuk QA:
  - TC-FA-PREF-454 Expected b ("dapat diekspor tanpa posting ulang") tidak menyebut tanda teramatinya; langkah 10 mengasersi teks Expected apa adanya pada Export Journal.
  - TC-FA-PREF-455 precondition menyebut 'disposal - 23' belum diposting sedangkan PC-7 menyebut 3 pelepasan belum diposting; spec men-seed 'disposal - 23' sebagai salah satu dari 3 pelepasan itu (dialog menyebut "3 unposted disposals").
  - Post Condition TC-FA-PREF-454 ("Jurnal yang ditahan menjadi dapat diekspor") dan TC-FA-PREF-455 ("Pelepasan belum diposting memakai akun baru") adalah kesimpulan dari Expected dan tidak diasersi terpisah (S-01).
