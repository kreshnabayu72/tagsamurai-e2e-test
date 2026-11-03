---
id: TC-FA-FAAM-E2E-092-delete-single-dialog-cancel-dan-blok-in-use
title: "Delete Single: Dialog Konfirmasi, Cancel, dan Dialog Blok In-Use (Jamak, Tunggal, Aset Draft dan Waiting for Approval)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-261
  - TC-FA-FAAM-263
  - TC-FA-FAAM-264
  - TC-FA-FAAM-265
  - TC-FA-FAAM-266
coverage:
  web: automated
---

# Delete Single: Dialog Konfirmasi, Cancel, dan Dialog Blok In-Use (Jamak, Tunggal, Aset Draft dan Waiting for Approval)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak menyimpan perubahan data dan tidak memakai seed API per TC.
- Data Pre-setup yang hanya dibaca (dialog dibatalkan atau ditolak guard in-use, tidak ada record yang diubah atau dihapus, Last Updated tidak berubah; S-06):
  - Pre-setup #13: `Warehouse Pallet` (Code `PLT-WH`, Total Asset 0), fixture `Fixture.faAssetName.warehousePallet`.
  - Pre-setup #10: `Dell Latitude` (Total Asset 42), fixture `Fixture.faAssetName.dellLatitude`.
  - Pre-setup #14h: `Single Asset Item` (Total Asset 1), fixture `Fixture.faAssetName.singleAssetItem`.
  - Pre-setup #14w: `Draft Pending Item` (Total Asset 2: 1 aset Draft dan 1 aset Waiting for Approval), fixture `Fixture.faAssetName.draftPendingItem`.
- Kemampuan teknis (disediakan tim BE/FE): membaca jumlah entri Changelog tanpa mengubahnya (baseline N0, dicatat sebelum aksi pertama).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-261 dan TC-FA-FAAM-263: Dialog konfirmasi Delete dan Cancel

1. Catat jumlah entri Changelog sebagai N0 lewat kemampuan baca
2. Ketik Search `Warehouse Pallet`, tekan Enter
3. Klik `⋯` baris `Warehouse Pallet` lalu `Delete`
4. Verifikasi dialog `Delete Asset Name` dengan bullet `Warehouse Pallet` dan teks `Are you sure you want to delete it? This action cannot be undone.` serta tombol `[Cancel]` dan `[Delete]` (merah) tampil
5. Klik `[Cancel]`
6. Verifikasi dialog tertutup
7. Verifikasi baris `Warehouse Pallet` tetap ada
8. Verifikasi tidak ada toast
9. Buka Changelog
10. Verifikasi jumlah entri Changelog sama dengan N0
11. Tutup Changelog

### TC-FA-FAAM-264: Dialog blok jamak untuk Asset Name in-use

12. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
13. Klik `⋯` baris `Dell Latitude` lalu `Delete`
14. Verifikasi dialog `Cannot Delete Asset Name` dengan bullet `Dell Latitude` dan teks `This asset name is used by 42 assets and cannot be deleted.` serta tombol `[OK]` tampil
15. Klik `[OK]`
16. Buka Changelog
17. Verifikasi jumlah entri Changelog sama dengan N0 (tidak ada mutasi)
18. Tutup Changelog
19. Verifikasi baris `Dell Latitude` tetap ada

### TC-FA-FAAM-265: Dialog blok bentuk tunggal untuk 1 aset

20. Ganti isi kotak search dengan `Single Asset Item`, tekan Enter
21. Klik `⋯` baris `Single Asset Item` lalu `Delete`
22. Verifikasi dialog `Cannot Delete Asset Name` dengan teks `This asset name is used by 1 asset and cannot be deleted.` tampil
23. Klik `[OK]`

### TC-FA-FAAM-266: Aset Draft dan Waiting for Approval menahan Delete

24. Ganti isi kotak search dengan `Draft Pending Item`, tekan Enter
25. Klik `⋯` baris `Draft Pending Item` lalu `Delete`
26. Verifikasi dialog blok `Cannot Delete Asset Name` dengan teks `This asset name is used by 2 assets and cannot be deleted.` tampil
27. Klik `[OK]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 2, 12, 20, 24), `[OK]` menutup dialog blok (langkah 15, 23, 27), serta membuka dan menutup Changelog sebagai observasi "tanpa log" dan "tidak ada mutasi" (langkah 9, 11, 16, 18).
- TC-FA-FAAM-261 dan TC-FA-FAAM-263 memakai langkah pembuka yang identik (klik `⋯` lalu `Delete` pada `Warehouse Pallet`) tanpa submit; dialog yang sama dipakai untuk screening TC-FA-FAAM-261 lalu dibatalkan oleh TC-FA-FAAM-263.
- Dialog konfirmasi pada langkah 4 dan dialog blok pada langkah 14 ditulis sebagai satu `Verifikasi` karena judul, isi, dan tombol disebut utuh pada Expected TC (S-01, dialog konfirmasi satu elemen).
- Temuan untuk QA:
  - TC-FA-FAAM-264 Expected c "Tidak ada mutasi" dan TC-FA-FAAM-263 Expected c "tanpa log" tidak punya langkah observasi di TC; spec mengamatinya lewat jumlah entri Changelog terhadap baseline N0 (S-12).
  - TC-FA-FAAM-266 mensyaratkan satu aset Draft dan satu aset Waiting for Approval pada `Draft Pending Item`, tetapi jumlah di dialog (2 assets) hanya mengonfirmasi total; status tiap aset tidak diasersi di UI.
  - TC-FA-FAAM-263 tidak menyebut bahwa `Warehouse Pallet` harus dipilih tanpa baris lain yang namanya memuat `Warehouse Pallet` (salinan seed spec lain); spec mencari baris dengan nama persis `Warehouse Pallet` pada hasil Search.
