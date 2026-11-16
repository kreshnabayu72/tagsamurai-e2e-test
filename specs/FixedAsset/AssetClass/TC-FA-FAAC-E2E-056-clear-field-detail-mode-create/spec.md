---
id: TC-FA-FAAC-E2E-056-clear-field-detail-mode-create
title: "Clear Field pada Detail Mode Create: Seluruh Field Dikosongkan dan Select Start Kembali ke Nilai Awal"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-647
  - TC-FA-FAAC-696
sourceRules: ["V-05", "F-FAAC-01.k4", "§4.1.2#p1", "§4.2f#b2", "§4.1.2#r1", "§4.1.2#r2", "§4.1.2#r3", "§4.1.2#r6", "§4.1.2#r14", "FAAC-LOGIC-02d", "§4.1.2#r13", "§4.1.2#r18", "§4.1.2#r19", "FLD-07", "§4.1.2#r12", "§4.1.2#r20", "§4.1.2#r21", "§4.1.2#r22", "§4.1.2#r23", "§4.1.2#r24", "§4.1.2#p11", "V-18", "V-21"]
smoke: []
dependsOn: []
trace:
  "V-05": [8, 16]
  "F-FAAC-01.k4": 9
  "§4.1.2#p1": 11
  "§4.2f#b2": [12, 29]
  "§4.1.2#r1": 13
  "§4.1.2#r2": 14
  "§4.1.2#r3": 15
  "§4.1.2#r6": 18
  "§4.1.2#r14": 19
  "FAAC-LOGIC-02d": [20, 21, 35, 36]
  "§4.1.2#r13": [20, 35, 37]
  "§4.1.2#r18": [21, 36, 37]
  "§4.1.2#r19": 22
  "FLD-07": 24
  "§4.1.2#r12": 25
  "§4.1.2#r20": 27
  "§4.1.2#r21": 27
  "§4.1.2#r22": 27
  "§4.1.2#r23": 27
  "§4.1.2#r24": 27
  "§4.1.2#p11": 29
  "V-18": 38
  "V-21": 38
coverage:
  web: automated
---

# Clear Field pada Detail Mode Create: Seluruh Field Dikosongkan dan Select Start Kembali ke Nilai Awal

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Chart of Accounts memuat akun Active `11001 – Machinery Cost` dan `12001 – Accumulated Depreciation Machinery`; Tax Depreciation Class `Bukan bangunan – Kelompok 3` Active.
- Data (nama literal dari TC): Class Code `B-CLRALL` belum ada sebelum spec dan tidak pernah disimpan (form hanya ditolak validasi lalu dikosongkan); fixture BE menghapusnya bila ada. Hook `after` menghapusnya bila ada.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-696: Clear Field pada Detail mode Create mengosongkan seluruh field dan mereset caption tanpa dialog

1. Klik tombol `[+ Asset Class]` di toolbar tabel
2. Pada tab General isi Class Code `B-CLRALL` dan Description `Clear field fixture`; biarkan Class Name kosong
3. Klik tab `Depreciation`; pilih Method `Straight Line`, isi Useful Life `60`, pilih unit `Amount` pada Residual Value dan isi `1000`, pilih Depreciation Start Convention `Start next month`
4. Pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` lalu Tax Method `Declining Balance`, pilih Tax Depreciation Start Rule `Month of use`, isi Capitalization Threshold `5000000`
5. Klik tab `Accounts`; pilih Asset Cost `11001 – Machinery Cost` dan Accumulated Depreciation `12001 – Accumulated Depreciation Machinery`
6. Klik `[Submit]`
7. Klik tab `General`
8. Verifikasi caption `Class name must not be empty` tampil pada Class Name
9. Verifikasi halaman tetap `Add Asset Class` (tidak berpindah ke mode Edit) sehingga Asset Class tidak dibuat
10. Klik `[Clear Field]` di footer
11. Verifikasi halaman `Add Asset Class` tetap terbuka dengan footer `[Clear Field]` dan `[Submit]`
12. Verifikasi tidak ada dialog apa pun, termasuk Unsaved Changes
13. Verifikasi Class Code kosong
14. Verifikasi Class Name kosong
15. Verifikasi Description kosong
16. Verifikasi caption `Class name must not be empty` hilang
17. Klik tab `Depreciation`
18. Verifikasi Method belum terpilih (placeholder `Select method`)
19. Verifikasi Tax Depreciation Class belum terpilih (placeholder `Select tax depreciation class`)
20. Verifikasi Depreciation Start Convention kembali `Full month from in-service date`
21. Verifikasi Tax Depreciation Start Rule kembali `Month of expenditure`
22. Verifikasi Capitalization Threshold kosong
23. Pilih Method `Straight Line`
24. Verifikasi Useful Life kosong (placeholder `Enter useful life`)
25. Verifikasi Residual Value kosong dengan unit `Percent` terpilih
26. Klik tab `Accounts`
27. Verifikasi kelima field akun kosong (placeholder `Select account`)
28. Klik breadcrumb `Asset Class`
29. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
30. Klik `[Leave]`

### TC-FA-FAAC-647: Clear Field pada Detail mode Create mengembalikan dua select start ke nilai awal

31. Klik tombol `[+ Asset Class]` di toolbar tabel
32. Klik tab `Depreciation`
33. Pilih Depreciation Start Convention `Start next month` dan Tax Depreciation Start Rule `Month of use`
34. Klik `[Clear Field]` di footer
35. Verifikasi Depreciation Start Convention kembali bernilai `Full month from in-service date`
36. Verifikasi Tax Depreciation Start Rule kembali bernilai `Month of expenditure`
37. Verifikasi kedua select tidak kosong
38. Verifikasi tidak ada caption `Depreciation start convention must not be empty` maupun `Tax depreciation start rule must not be empty`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-647, 696). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-696 lebih dulu karena berakhir dengan form dirty yang ditutup lewat dialog `Unsaved Changes` (langkah 28 sampai 30, S-08); TC-647 berakhir dengan kedua select pada nilai awal sehingga tidak ada form dirty tersisa (S-09, S-10).
- Spec ini sekitar 38 langkah, di atas 35 langkah. Alasan: kedua TC menguji satu aksi (`[Clear Field]` pada Detail mode Create), satu kelas, tanpa data bersama; Expected TC-696 memuat 6 butir dengan banyak field yang tiap-tiapnya wajib `Verifikasi` sendiri (S-01), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 7 (membuka tab General untuk mengamati caption; TC tidak menyebut tab aktif sesudah `[Submit]`), langkah 28 dan 30 (menutup form dirty), langkah 3 dan 4 menyalin langkah 3 TC-696 yang dipecah dua, langkah 33 menggabungkan langkah 3 dan 4 TC-647.
- Langkah 8 menjadi anchor positif untuk asersi absence caption pada langkah 16; langkah 11 menjadi anchor untuk absence dialog pada langkah 12; langkah 35 menjadi anchor untuk absence caption pada langkah 38.
- Temuan untuk QA:
  - TC-696 Expected a ("Asset Class tidak dibuat") tidak menyebut cara pengamatan; langkah 9 mengasersinya dari halaman yang tetap `Add Asset Class` setelah `[Submit]`.
  - TC-696 langkah 5 "perhatikan tab General" tidak menyebut apakah tab General aktif otomatis sesudah `[Submit]`; spec membukanya eksplisit (langkah 7).
  - TC-647 tidak menyatakan apakah form dianggap dirty sesudah `[Clear Field]` mengembalikan nilai awal; spec berakhir tanpa langkah menutup form dan hanya mengandalkan jaring pengaman hook `beforeEach` suite bila dialog `Unsaved Changes` muncul.
