---
id: TC-FA-LBL-E2E-140-sinkron-rename-label-ke-asset-list-asset-detail-reports-dan-asset-transactional-policy
title: "Sinkron Rename Label ke Asset List, Asset Detail, Reports, dan Asset Transactional Policy"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-415
  - TC-FA-LBL-416
  - TC-FA-LBL-417
  - TC-FA-LBL-418
coverage:
  web: automated
---

# Sinkron Rename Label ke Asset List, Asset Detail, Reports, dan Asset Transactional Policy

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, nama bersuffix `{runId}-140`; pola Pre-setup #13 dan #14 dimiliki spec agar `Last Updated` aset Pre-setup tidak berubah, S-06): Asset Name `Sync Item {runId}-140`, aset Active `Sync Asset {runId}-140` (Asset Name itu) yang tertempel keempat label di bawah, dan keempat label (Color `Fixture.assetLabeling.warnaSeed`) menjadi Default Label Asset Name `Sync Item {runId}-140`:
  - `Urgent 415 {runId}-140` (TC-FA-LBL-415), `Urgent 416 {runId}-140` (TC-FA-LBL-416), `Urgent 417 {runId}-140` (TC-FA-LBL-417), `Urgent 418 {runId}-140` (TC-FA-LBL-418).
  - Nama hasil rename: `Critical 415 {runId}-140`, `Critical 416 {runId}-140`, `Critical 417 {runId}-140`, `Critical 418 {runId}-140`.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### Rename keempat label di tab Labels (dipakai TC-FA-LBL-415, TC-FA-LBL-416, TC-FA-LBL-417, TC-FA-LBL-418)

1. Ketik Search `Urgent 415 {runId}-140`, tekan Enter
2. Klik `⋯` pada baris `Urgent 415 {runId}-140`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Critical 415 {runId}-140`
4. Klik `[Save]`, lalu tunggu aksi selesai (modal Edit Label tertutup)
5. Ganti isi kotak search dengan `Urgent 416 {runId}-140`, tekan Enter
6. Klik `⋯` pada baris `Urgent 416 {runId}-140`, lalu klik `Edit`
7. Ganti isi Label Name dengan `Critical 416 {runId}-140`
8. Klik `[Save]`, lalu tunggu aksi selesai (modal Edit Label tertutup)
9. Ganti isi kotak search dengan `Urgent 417 {runId}-140`, tekan Enter
10. Klik `⋯` pada baris `Urgent 417 {runId}-140`, lalu klik `Edit`
11. Ganti isi Label Name dengan `Critical 417 {runId}-140`
12. Klik `[Save]`, lalu tunggu aksi selesai (modal Edit Label tertutup)
13. Ganti isi kotak search dengan `Urgent 418 {runId}-140`, tekan Enter
14. Klik `⋯` pada baris `Urgent 418 {runId}-140`, lalu klik `Edit`
15. Ganti isi Label Name dengan `Critical 418 {runId}-140`
16. Klik `[Save]`, lalu tunggu aksi selesai (modal Edit Label tertutup)

### TC-FA-LBL-415: Rename label tercermin langsung di Asset List

17. Buka Fixed Asset > Asset List tanpa menyunting data aset, lalu ketik Search `Sync Asset {runId}-140`, tekan Enter
18. Verifikasi chip pada kolom label baris `Sync Asset {runId}-140` menampilkan nama baru `Critical 415 {runId}-140`
19. Verifikasi nama lama `Urgent 415 {runId}-140` tidak tampil pada kolom label

### TC-FA-LBL-416: Rename label tercermin langsung di Asset Detail

20. Buka Asset Detail baris `Sync Asset {runId}-140` tanpa menyunting data aset
21. Verifikasi chip pada bagian labels Asset Detail menampilkan nama baru `Critical 416 {runId}-140`
22. Verifikasi nama lama `Urgent 416 {runId}-140` tidak tampil pada bagian labels

### TC-FA-LBL-417: Rename label tercermin langsung di Reports

23. Buka Reports tanpa menyunting data aset, lalu buka filter Label
24. Verifikasi chip di Reports menampilkan nama baru `Critical 417 {runId}-140`
25. Verifikasi opsi filter label di Reports menampilkan nama baru `Critical 417 {runId}-140`
26. Verifikasi nama lama `Urgent 417 {runId}-140` tidak tampil pada chip maupun opsi filter label

### TC-FA-LBL-418: Rename label tercermin langsung di Asset Transactional Policy

27. Buka Fixed Asset > Settings > Asset Transactional Policy tanpa menyunting data aset, lalu buka filter default label
28. Verifikasi kolom default label menampilkan nama baru `Critical 418 {runId}-140`
29. Verifikasi filter default label menampilkan nama baru `Critical 418 {runId}-140`
30. Verifikasi nama lama `Urgent 418 {runId}-140` tidak tampil pada kolom maupun filter default label

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 5, 9, 13, 17 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 20, 23, 27 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Urutan (bagian 3): keempat rename dikerjakan berurutan di tab Labels lebih dulu, lalu tiap konsumen dibuka sekali; tiap TC mengasersi konsumennya sendiri, sehingga TC-FA-LBL-415 sampai 418 tidak saling bergantung. Absence nama lama didahului `Verifikasi` nama baru pada surface yang sama sebagai anchor (bagian 8b butir 2).
- Ukuran spec (30 langkah, sekitar 35): keempat TC satu pola (rename lalu cek satu konsumen), satu akun, satu dataset seed, dan tiap blok konsumen berdiri sendiri; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01) dan empat rename berurutan.
- Temuan untuk QA:
  - TC-FA-LBL-417 dan 418 menyebut "chip dan opsi filter label di reports" serta "kolom dan filter default label" tanpa nama kolom atau laporan; spec memeriksa chip dan opsi filter pada halaman Reports dan Asset Transactional Policy yang dibuka.
  - Precondition TC memakai aset `Laptop Dell - 1` Pre-setup #13; spec memakai aset milik spec dengan pola yang sama supaya relasi dan `Last Updated` aset Pre-setup tidak berubah (S-06).
