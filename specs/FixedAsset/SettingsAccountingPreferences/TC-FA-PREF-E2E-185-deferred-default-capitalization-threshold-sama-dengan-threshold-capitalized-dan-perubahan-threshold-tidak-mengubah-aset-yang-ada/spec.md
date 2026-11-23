---
id: TC-FA-PREF-E2E-185-deferred-default-capitalization-threshold-sama-dengan-threshold-capitalized-dan-perubahan-threshold-tidak-mengubah-aset-yang-ada
title: "[DEFERRED] Default Capitalization Threshold: pembelian sama dengan threshold berstatus Capitalized dan perubahan threshold tidak mengubah status aset yang sudah ada"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-642
  - TC-FA-PREF-643
sourceRules: ["FAPREF-LOGIC-03c", "FAPREF-LOGIC-03d", "SET-02", "D-01", "T-01"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-03c": [4, 14, 18]
  "FAPREF-LOGIC-03d": [14, 18]
  "SET-02": [7, 8]
  "D-01": 9
  "T-01": 10
coverage:
  web: automated
---

# [DEFERRED] Default Capitalization Threshold: pembelian sama dengan threshold berstatus Capitalized dan perubahan threshold tidak mengubah status aset yang sudah ada

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (Default Capitalization Threshold tersimpan 5.000.000); Asset Class Vehicles tanpa threshold sendiri (PC-6); aset 'assignment - 12' (dibuat oleh langkah pembelian TC-FA-PREF-642), aset 'assignment - 13' (Acquisition Cost 7.000.000, sudah dikapitalisasi, Capitalized) dan 'assignment - 11' (Acquisition Cost 800.000, Tracked only) dari PC-16 (data modul pemilik, disediakan tim FE setelah modul Asset tersedia). Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan aset; pencatatan pembelian lewat UI modul transaksi aset; pembacaan Accounting Treatment pada Detail aset (modul Asset, `ASTD-LOGIC-19`).
- State global yang diubah: Default Capitalization Threshold company (TC-FA-PREF-643, 5.000.000 menjadi 10.000.000) dan aset 'assignment - 12'; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir (langkah 19) dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-642: Pembelian tepat sama dengan Default Capitalization Threshold berstatus awal Capitalized

1. Seed Default Capitalization Threshold tersimpan 5.000.000 dan Asset Class Vehicles tanpa threshold sendiri hingga tersimpan
2. Catat pembelian senilai "5000000" pada Asset Class Vehicles sebagai aset 'assignment - 12' di modul transaksi aset
3. Verifikasi aset 'assignment - 12' tercatat
4. Verifikasi status awal aset 'assignment - 12' adalah Capitalized (Acquisition Cost sama dengan threshold bukan di bawahnya)

### TC-FA-PREF-643: Perubahan Default Capitalization Threshold tidak mengubah status aset yang sudah ada

5. Seed Default Capitalization Threshold tersimpan 5.000.000, Asset Class Vehicles tanpa threshold sendiri, aset 'assignment - 13' (Acquisition Cost 7.000.000) sudah dikapitalisasi berstatus Capitalized, dan aset 'assignment - 11' (Acquisition Cost 800.000) berstatus Tracked only hingga tersimpan
6. Buka Fixed Asset > Settings > Accounting > Preferences
7. Ubah isi CurrencyInput Default Capitalization Threshold menjadi "10000000"
8. Klik [Save changes]
9. Klik [Save] pada dialog Save Changes
10. Verifikasi toast "Success, accounting preferences have been saved." tampil
11. Buka daftar aset di modul Asset
12. Ketik Search "assignment - 13", tekan Enter
13. Klik Name "assignment - 13" untuk membuka Detail aset
14. Verifikasi Accounting Treatment aset 'assignment - 13' tetap Capitalized walau Acquisition Cost 7.000.000 berada di bawah threshold baru 10.000.000
15. Klik Breadcrumb daftar aset untuk kembali ke daftar aset
16. Ganti isi kotak search dengan "assignment - 11", tekan Enter
17. Klik Name "assignment - 11" untuk membuka Detail aset
18. Verifikasi Accounting Treatment aset 'assignment - 11' tetap Tracked only
19. Pulihkan Preferences ke nilai awal PC-1 (Default Capitalization Threshold 5.000.000) dan status kapitalisasi aset ke nilai awal lewat seed hingga tersimpan

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Kedua TC bertanda `[DEFERRED]` karena status per aset dimiliki modul pemilik `asset-detail/` (`FAPREF-LOGIC-03d`, ASTD-LOGIC-19); modul ini hanya menyimpan nilai threshold.
- Langkah penghubung (S-03): langkah 6 (membuka layar Preferences sesudah seed), langkah 11 dan 15 (membuka daftar aset dan kembali ke daftar lewat Breadcrumb), langkah 12 dan 16 (Search sebagai langkah penghubung untuk menemukan baris target, R-16, R-23; langkah 16 memakai "ganti isi kotak search" karena kotak Search mempertahankan nilainya setelah kembali lewat Breadcrumb, bagian 8b butir 9), langkah 19 (pemulihan state global, S-09, R-08).
- Seed per TC (langkah 1 dan 5) membentuk precondition tanpa bergantung hasil TC sebelumnya.
- Temuan untuk QA (perlu konfirmasi FE):
  - TC-FA-PREF-643 langkah 3 menulis "Klik [Save] pada dialog Save Changes" untuk perubahan Default Capitalization Threshold saja, sedangkan spec lain di suite ini (mis. TC-FA-PREF-213 di spec 056 dan spec 054) memperlakukan threshold sebagai setting tanpa dampak sehingga Save langsung tanpa dialog. Spec mengikuti TC (langkah 9); apakah dialog Save Changes tampil untuk perubahan threshold saja perlu konfirmasi FE. Bila tidak tampil, langkah 9 dan rujukan D-01 dihapus.
  - TC-FA-PREF-642 langkah 2 ("Amati status Accounting Treatment aset 'assignment - 12'") tidak menyebut lokasi pengamatan (daftar aset atau Detail aset); spec menulisnya `Verifikasi` status awal tanpa menyebut layar, lokasi perlu konfirmasi FE. Modul transaksi aset dan tempat status Accounting Treatment tampil disediakan tim FE tanpa endpoint karangan (S-13).
  - TC-FA-PREF-642 Expected b memuat penjelasan dalam kurung ("Acquisition Cost sama dengan threshold bukan di bawahnya") yang bukan klausa teramati terpisah; spec memasukkannya ke satu `Verifikasi` (langkah 4).
  - TC-FA-PREF-643 Expected b memuat penjelasan dalam kurung ("status adalah snapshot saat aset dikapitalisasi") yang bukan klausa teramati terpisah; spec tidak menuliskannya sebagai asersi.
  - TC-FA-PREF-643 Expected b dan c ditulis dua `Verifikasi` per aset (langkah 14 dan 18); Post Condition a ("Default Capitalization Threshold tersimpan 10.000.000") dan b ("Accounting Treatment aset yang sudah ada tidak berubah", kesimpulan dari Expected b dan c) tidak diasersi terpisah.
  - TC-FA-PREF-643 tidak menyebut modul daftar aset atau nama menu untuk membuka detail aset; spec menulis "Buka daftar aset di modul Asset" dan Search nama aset (langkah penghubung).
  - TC-FA-PREF-642 tidak menyebut bagaimana status awal Capitalized ditetapkan bila Asset Class Vehicles tanpa threshold sendiri selain "threshold efektif 5.000.000"; spec mengikuti TC.
  - Post Condition TC yang tidak punya langkah observasi di TC tidak diasersi; tidak ada Expected log, sehingga tidak ada rujukan ke spec absence (S-05).
  - TC-FA-PREF-605 (pembelian di bawah threshold) ada di spec 149.
