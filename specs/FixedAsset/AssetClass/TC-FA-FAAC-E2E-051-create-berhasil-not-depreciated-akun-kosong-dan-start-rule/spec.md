---
id: TC-FA-FAAC-E2E-051-create-berhasil-not-depreciated-akun-kosong-dan-start-rule
title: "Create Asset Class Berhasil: Method Not Depreciated, Tab Accounts Kosong, dan Start Convention serta Start Rule Bukan Nilai Awal"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-91
  - TC-FA-FAAC-92
  - TC-FA-FAAC-148
sourceRules: ["FAAC-LOGIC-02a", "FI-02", "ST-08", "FI-04", "ST-09", "FAAC-LOGIC-02g", "T-01", "§4.1.1#r4", "§4.1.1#r5", "FAAC-LOGIC-05c", "§4.1.1#r6", "FAAC-LOGIC-03b", "§4.1.1#r7", "FAAC-LOGIC-05b", "FAAC-LOGIC-05a", "FAAC-LOGIC-04f", "FAAC-LOGIC-02d"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-02a": 4
  "FI-02": 5
  "ST-08": 5
  "FI-04": [7, 8]
  "ST-09": 7
  "FAAC-LOGIC-02g": [7, 8]
  "T-01": [10, 19, 33]
  "§4.1.1#r4": 13
  "§4.1.1#r5": 13
  "FAAC-LOGIC-05c": 20
  "§4.1.1#r6": 23
  "FAAC-LOGIC-03b": 23
  "§4.1.1#r7": [25, 26]
  "FAAC-LOGIC-05b": 25
  "FAAC-LOGIC-05a": [26, 27]
  "FAAC-LOGIC-04f": 27
  "FAAC-LOGIC-02d": [35, 36]
coverage:
  web: automated
---

# Create Asset Class Berhasil: Method Not Depreciated, Tab Accounts Kosong, dan Start Convention serta Start Rule Bukan Nilai Awal

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Tax Depreciation Class `Tanah` Active tanpa metode penyusutan; Tax Depreciation Class `Bukan bangunan – Kelompok 3` Active.
- Data yang dibuat spec (nama literal dari TC): Asset Class `B-LAND`, `B-NOACC`, dan `B-CONV`. Ketiga Class Code belum ada sebelum spec; fixture BE menghapusnya bila ada. Hook `after` menghapus ketiganya lewat fixture BE (pembersihan tidak mengandalkan setup berhasil penuh).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-91: Create dengan Method Not Depreciated dan Tax Depreciation Class tanpa metode

1. Klik tombol `[+ Asset Class]` di toolbar tabel
2. Pada tab General isi Class Code `B-LAND`, Class Name `Land Fixture`
3. Klik tab `Depreciation` dan pilih Method `Not Depreciated`
4. Verifikasi Method bernilai `Not Depreciated` dan field Tax Depreciation Class tampil
5. Verifikasi Useful Life, Declining Rate, Total Estimated Units, Unit Type, dan Residual Value tidak tampil
6. Pilih Tax Depreciation Class `Tanah`
7. Verifikasi Tax Method read-only bernilai `—`
8. Verifikasi Tax Method tidak wajib
9. Klik `[Submit]`
10. Verifikasi toast sukses `Success, asset class has been created.`
11. Klik breadcrumb `Asset Class` untuk kembali ke tabel
12. Ketik Search `B-LAND`, tekan Enter
13. Verifikasi baris `B-LAND` menampilkan Commercial `Not Depreciated` dan Fiscal `Tanah` saja (tanpa Tax Method)

### TC-FA-FAAC-92: Create dengan tab Accounts dan Capitalization Threshold dibiarkan kosong

14. Klik tombol `[+ Asset Class]` di toolbar tabel
15. Pada tab General isi Class Code `B-NOACC`, Class Name `No Account Fixture`
16. Isi field lain dengan nilai valid: Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
17. Biarkan tab Accounts dan Capitalization Threshold kosong
18. Klik `[Submit]`
19. Verifikasi toast sukses `Success, asset class has been created.`
20. Verifikasi tidak muncul dialog atau peringatan apa pun terkait akun kosong
21. Klik breadcrumb `Asset Class` untuk kembali ke tabel
22. Ganti isi kotak search dengan `B-NOACC`, tekan Enter
23. Verifikasi Capitalization Threshold baris `B-NOACC` bernilai `Default`
24. Arahkan kursor ke ikon Accounts pada baris `B-NOACC`
25. Verifikasi ikon Accounts merah (belum lengkap)
26. Verifikasi tooltip `Accounts incomplete: Asset Cost, Accumulated Depreciation, Depreciation Expense. Journals for this asset class will be held at export.`
27. Verifikasi Gain on Disposal dan Loss on Disposal tidak tercantum pada tooltip sebagai akun yang belum lengkap (kosong berarti memakai Default Gain dan Default Loss company)

### TC-FA-FAAC-148: Create dengan Depreciation Start Convention dan Tax Depreciation Start Rule bukan nilai awal

28. Klik tombol `[+ Asset Class]` di toolbar tabel
29. Pada tab General isi Class Code `B-CONV`, Class Name `Convention Fixture`
30. Pada tab Depreciation isi Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
31. Pilih Depreciation Start Convention `Daily prorata` dan Tax Depreciation Start Rule `Month of use`
32. Klik `[Submit]`
33. Verifikasi toast sukses `Success, asset class has been created.`
34. Pada mode Edit buka tab `Depreciation`
35. Verifikasi Depreciation Start Convention `Daily prorata` tersimpan
36. Verifikasi Tax Depreciation Start Rule `Month of use` tersimpan

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-91, 92, 148). Tidak ada TC hanya-BE di spec ini.
- Pengecualian beralasan atas S-06 dan S-12: Class Code dan Class Name literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seed idempotent per spec oleh fixture BE (keputusan yang disetujui user).
- Spec ini sekitar 36 langkah, di atas 35 langkah. Alasan: ketiga TC satu topik (Create berhasil dengan variasi isian yang memengaruhi tampilan baris), tidak ada langkah yang diulang, dan tiap blok berdiri sendiri dengan data milik spec sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 11 dan 21 (kembali ke tabel lewat breadcrumb), langkah 12 dan 22 (Search untuk menemukan baris target; langkah 22 memakai "ganti isi kotak search" karena kotak Search mempertahankan nilainya sesudah breadcrumb), langkah 17 (menyalin "biarkan kosong" dari TC).
- Langkah 4 menjadi anchor positif untuk asersi absence pada langkah 5 (8b.2); langkah 19 menjadi anchor untuk langkah 20.
- Temuan untuk QA:
  - TC-92 Expected d ("Gain on Disposal dan Loss on Disposal kosong berarti memakai Default Gain dan Default Loss company") tidak punya langkah observasi di TC; diasersi lewat tooltip pada langkah 27 (kedua akun tidak tercantum sebagai belum lengkap) dan tidak memeriksa nilai Default company.
  - TC-91 Expected b menyebut "tidak wajib" tanpa cara pengamatan; spec memakai indikator wajib (tanpa tanda wajib) pada field Tax Method.
