---
id: TC-FA-FAAC-E2E-102-apply-changes-alert-dampak-dan-capitalization-threshold
title: "Apply Changes: Alert Dampak Not Depreciated dan Perubahan Capitalization Threshold Saja"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-313
  - TC-FA-FAAC-314
  - TC-FA-FAAC-315
sourceRules: ["FAAC-LOGIC-07g", "F-FAAC-02.k10", "§4.2f#b2", "FI-10", "FAAC-LOGIC-07a", "FAAC-LOGIC-07f", "T-02", "S-03d"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-07g": [6, 17]
  "F-FAAC-02.k10": 7
  "§4.2f#b2": [10, 22]
  "FI-10": 19
  "FAAC-LOGIC-07a": 29
  "FAAC-LOGIC-07f": 30
  "T-02": 32
  "S-03d": 33
coverage:
  web: automated
---

# Apply Changes: Alert Dampak Not Depreciated dan Perubahan Capitalization Threshold Saja

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-ASSETS` dipakai aset: 1 Asset Name dengan 5 aset aktif, Method Straight Line, Useful Life 60, belum pernah diposting; Asset Class `B-ASSET1` dipakai aset: 1 Asset Name dengan 1 aset aktif, Method Straight Line.
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser sinkron dan tidak digeser spec ini. Kemampuan membaca nilai Capitalization Threshold aset yang sudah ada lewat fixture BE disediakan tim FE/BE.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Capitalization Threshold `B-ASSETS` kembali ke nilai seed (TC-313 menyimpan 7000000).
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan jumlah aset aktif itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-314: Mengubah Method ke Not Depreciated menampilkan Alert jumlah aset (jamak)

1. Ketik Search `B-ASSETS`, tekan Enter
2. Klik link Class Code `B-ASSETS` di tabel
3. Klik tab `Depreciation`
4. Ganti Method menjadi `Not Depreciated`
5. Klik `Save`
6. Verifikasi dialog `Apply Changes` memuat Alert warning `5 active assets will stop being depreciated from [Effective From].` dengan [Effective From] berisi bulan yang dipilih (ditulis MMM YYYY)
7. Verifikasi konfirmasi tetap lewat tombol `Apply`
8. Klik `Cancel`
9. Klik breadcrumb `Asset Class`
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`

### TC-FA-FAAC-315: Mengubah Method ke Not Depreciated menampilkan Alert jumlah aset (tunggal) dan hilang saat checkbox dilepas

12. Ganti isi kotak search dengan `B-ASSET1`, tekan Enter
13. Klik link Class Code `B-ASSET1` di tabel
14. Klik tab `Depreciation`
15. Ganti Method menjadi `Not Depreciated`
16. Klik `Save`
17. Verifikasi Alert warning `1 active asset will stop being depreciated from [Effective From].`
18. Hilangkan centang `Apply to existing assets`
19. Verifikasi Alert tidak tampil
20. Klik `Cancel`
21. Klik breadcrumb `Asset Class`
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]`

### TC-FA-FAAC-313: Perubahan hanya Capitalization Threshold menampilkan D-11 hanya dengan Effective From

24. Ganti isi kotak search dengan `B-ASSETS`, tekan Enter
25. Klik link Class Code `B-ASSETS` di tabel
26. Klik tab `Depreciation`
27. Ubah Capitalization Threshold menjadi 7000000
28. Klik `Save`
29. Verifikasi dialog `Apply Changes` hanya berisi Effective From
30. Verifikasi tidak ada checkbox `Apply to existing assets` dan tidak ada blok pratinjau dampak
31. Klik `Apply`
32. Verifikasi toast sukses `Success, asset class has been updated.`
33. Verifikasi versi berlaku pada pendaftaran aset sejak Effective From dan tidak mengubah aset yang sudah ada (Capitalization Threshold aset yang sudah ada tidak berubah, dibaca lewat fixture BE)
34. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: dua kasus yang berhenti di dialog (TC-314 dan TC-315, form ditutup tanpa menyimpan) lebih dulu, lalu TC-313 yang menyimpan data di akhir.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 12, dan 24 (Search untuk menemukan baris target, R-16), langkah 8 dan 20 (menutup dialog `Apply Changes`), dan langkah 34 (mengosongkan Search). Langkah 9 sampai 11 dan 21 sampai 23 menutup form yang masih terisi lewat breadcrumb `Asset Class`, `Unsaved Changes`, dan `[Leave]` (S-08, S-09).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan jumlah aset aktif tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Pembagian TC: TC-607 (klik ganda Apply dan Create Recommended) ada di spec 111.
5. Temuan untuk QA: TC-313 Expected c ("Versi berlaku pada pendaftaran aset sejak Effective From dan tidak mengubah aset yang sudah ada") tidak menyebut cara observasi; spec membaca nilai Capitalization Threshold aset yang sudah ada lewat kemampuan baca BE yang disediakan tim FE/BE. TC-314 Expected b ("konfirmasi tetap lewat tombol Apply") diasersi sebagai tombol `Apply` tampil.
