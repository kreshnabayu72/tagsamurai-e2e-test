---
id: TC-FA-LBL-E2E-141-sinkron-delete-label-single-dan-bulk-ke-konsumen
title: "Sinkron Delete Label (Single dan Bulk) ke Konsumen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-420
  - TC-FA-LBL-421
  - TC-FA-LBL-422
  - TC-FA-LBL-522
coverage:
  web: automated
---

# Sinkron Delete Label (Single dan Bulk) ke Konsumen

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-141`, Color `Fixture.assetLabeling.warnaSeed`):
  - Label bersih (Total Asset 0, bukan Default Label): `Gone 420 {runId}-141`, `Gone 421 {runId}-141`, `Gone 422 {runId}-141`, `Sync Bulk A 522 {runId}-141`, `Sync Bulk B 522 {runId}-141`.
  - Label dipakai: `Sync Used 522 {runId}-141` tertempel pada aset Active milik spec `Sync Used Asset {runId}-141` (pola Pre-setup #13, dimiliki spec agar aset Pre-setup tidak berubah, S-06).
  - Data Pre-setup #14: Asset Name `Warehouse Item` (popup Edit dibuka untuk melihat dropdown Default Label, tidak disimpan).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### Keadaan awal dropdown penugasan label (TC-FA-LBL-522, langkah 1 TC)

1. Buka Fixed Asset > Asset List, ketik Search `Sync Used Asset {runId}-141`, tekan Enter, lalu buka Asset Detail baris itu
2. Buka dropdown penugasan label, catat opsi `Sync Bulk A 522 {runId}-141`, `Sync Bulk B 522 {runId}-141`, dan `Sync Used 522 {runId}-141`, lalu tutup dropdown
3. Buka Fixed Asset > Settings > Asset Master > tab Labels

### TC-FA-LBL-420, TC-FA-LBL-421, TC-FA-LBL-422: Hapus label bersih satu per satu di tab Labels

4. Ketik Search `Gone 420 {runId}-141`, tekan Enter
5. Klik `⋯` pada baris `Gone 420 {runId}-141`, lalu klik `Delete`
6. Klik `[Delete]` pada dialog `Delete Label`, lalu tunggu aksi selesai (dialog tertutup)
7. Ganti isi kotak search dengan `Gone 421 {runId}-141`, tekan Enter
8. Klik `⋯` pada baris `Gone 421 {runId}-141`, lalu klik `Delete`
9. Klik `[Delete]` pada dialog `Delete Label`, lalu tunggu aksi selesai (dialog tertutup)
10. Ganti isi kotak search dengan `Gone 422 {runId}-141`, tekan Enter
11. Klik `⋯` pada baris `Gone 422 {runId}-141`, lalu klik `Delete`
12. Klik `[Delete]` pada dialog `Delete Label`, lalu tunggu aksi selesai (dialog tertutup)

### TC-FA-LBL-522: Bulk Delete tiga label (dua bersih, satu dipakai)

13. Ganti isi kotak search dengan `522 {runId}-141`, tekan Enter
14. Centang baris `Sync Bulk A 522 {runId}-141`, `Sync Bulk B 522 {runId}-141`, dan `Sync Used 522 {runId}-141`
15. Klik `Bulk Action` lalu klik `Delete`
16. Klik `[Continue]`
17. Verifikasi toast `Success, label has been deleted. Some items were skipped.`

### Dropdown penugasan label di Asset Detail (TC-FA-LBL-420 dan TC-FA-LBL-522)

18. Buka Fixed Asset > Asset List, ketik Search `Sync Used Asset {runId}-141`, tekan Enter, buka Asset Detail baris itu, lalu buka dropdown penugasan label
19. Verifikasi opsi `Sync Used 522 {runId}-141` masih ada pada dropdown
20. Verifikasi opsi `Gone 420 {runId}-141` tidak ada pada dropdown penugasan label
21. Verifikasi opsi `Sync Bulk A 522 {runId}-141` dan `Sync Bulk B 522 {runId}-141` tidak ada pada dropdown

### Filter Label di Reports (TC-FA-LBL-421 dan TC-FA-LBL-522)

22. Buka Reports dan buka filter Label
23. Verifikasi filter Label masih memuat `Sync Used 522 {runId}-141`
24. Verifikasi opsi `Gone 421 {runId}-141` tidak ada di filter Label
25. Verifikasi filter Label tidak memuat `Sync Bulk A 522 {runId}-141` dan `Sync Bulk B 522 {runId}-141`

### Dropdown Default Label di Asset Name (TC-FA-LBL-422 dan TC-FA-LBL-522)

26. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik `⋯` pada baris Asset Name `Warehouse Item`, lalu klik `Edit`
27. Buka dropdown Default Label
28. Verifikasi dropdown Default Label masih memuat `Sync Used 522 {runId}-141`
29. Verifikasi opsi `Gone 422 {runId}-141` tidak ada di dropdown Default Label
30. Verifikasi dropdown Default Label tidak memuat `Sync Bulk A 522 {runId}-141` dan `Sync Bulk B 522 {runId}-141`
31. Klik icon `[✕]` untuk menutup popup Edit Asset Name tanpa mengubah apa pun

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 4, 7, 10, 13 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 1, 2, 3, 18, 22, 26, 27, 31 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Urutan (bagian 3): penghapusan TC-FA-LBL-420, 421, 422, dan 522 dikerjakan lebih dulu di tab Labels, lalu tiap konsumen (Asset Detail, Reports, Asset Name) dibuka sekali dan memuat asersi TC-FA-LBL-420/421/422 dan 522 bersama. Keadaan awal dropdown (langkah TC-FA-LBL-522 nomor 1) dicatat sebelum penghapusan. Verifikasi opsi yang masih ada pada tiap konsumen menjadi anchor absence opsi yang dihapus (bagian 8b butir 2).
- Ukuran spec (31 langkah, sekitar 35): keempat TC satu topik (sinkron Delete ke tiga konsumen), satu akun, label seed milik masing-masing, dan blok konsumen berdiri sendiri; langkah dipadatkan dengan membuka tiap konsumen sekali.
- Temuan untuk QA:
  - TC-FA-LBL-420 sampai 422 tidak menyebut toast hasil Delete; spec menunggu dialog tertutup sebelum membuka konsumen.
  - TC-FA-LBL-522 memakai `Laptop Dell - 1` (Pre-setup #13) sebagai aset berlabel; spec memakai aset milik spec dengan pola yang sama (S-06).
