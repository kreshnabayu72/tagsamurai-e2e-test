---
id: TC-FA-FAAC-E2E-061-batas-method-plan-multi-depreciation
title: "Batas Method pada Plan Multi Depreciation: Max Depreciation Methods, Boundary, dan Perhitungan Method Lama"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-140
  - TC-FA-FAAC-141
  - TC-FA-FAAC-142
  - TC-FA-FAAC-146
  - TC-FA-FAAC-184
  - TC-FA-FAAC-185
coverage:
  web: automated
---

# Batas Method pada Plan Multi Depreciation: Max Depreciation Methods, Boundary, dan Perhitungan Method Lama

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- State global yang diubah spec: plan client Enterprise (Multi Depreciation), Max depreciation methods = 2 (dibaca di Admin Console > Plans & Licensing > Plans & Features, diubah ke 2 untuk uji ini), dan komposisi Method Asset Class pada tiga keadaan seed (E1, E2, E3 di bawah). Mekanisme pelaku perubahan ini tidak disebut TC, PRD, atau LLD; fixture BE untuk mengatur plan, Max depreciation methods, dan seed "disediakan tim FE/BE" (tanpa akun atau endpoint karangan). Hook `before` mencatat keadaan awal dan hook `after` memulihkannya lewat fixture BE, juga bila spec gagal di tengah. Suite berjalan serial.
- Keadaan E1 (langkah 1): Asset Class yang ada memakai `Straight Line` dan `Declining Balance`, masing-masing oleh lebih dari satu Asset Class, termasuk `B-PE3`; tidak ada yang memakai `Units of Production`. Keadaan E2 (langkah 35): `B-PE2` satu-satunya pemakai `Declining Balance`, Asset Class lain memakai `Straight Line`, tidak ada yang memakai `Units of Production`. Keadaan E3 (langkah 42): `B-PE8` satu-satunya pemakai `Declining Balance`, `Straight Line` dipakai Asset Class lain. Seed disediakan fixture BE.
- Data Pre-setup yang diubah dan dipulihkan fixture BE: `B-PE2` diganti Method menjadi `Units of Production` (langkah 38 dan 39) dan `B-PE8` dihapus (langkah 44); Last Updated `B-PE2` ikut berubah. Tax Depreciation Class `Tanah` dan `Bukan bangunan – Kelompok 3` Active.
- Data yang dibuat spec: Asset Class `B-P4`, `B-P5`, dan `B-P7` (disimpan); `B-P3` ditolak dialog sehingga tidak tersimpan. Hook `after` menghapus ketiganya lewat fixture BE.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Kemampuan teknis: membaca jumlah Asset Class dan jumlah entri Changelog Asset Class lewat fixture BE (audit trail permanen; asersi memakai selisih terhadap baseline, bukan angka absolut).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.

## Test Steps

### Keadaan E1: SL dan DB dipakai lebih dari satu Asset Class, Max depreciation methods 2

1. Atur lewat fixture BE keadaan E1; catat jumlah Asset Class (C1) dan jumlah entri Changelog Asset Class (N1); muat ulang halaman

### TC-FA-FAAC-140: Create Method baru melampaui Max depreciation methods ditolak D-22

2. Klik tombol `[+ Asset Class]` di toolbar tabel
3. Pada tab General isi Class Code `B-P3`, Class Name `Test Class`
4. Pada tab Depreciation pilih Method `Units of Production`, isi Useful Life `60`, Total Estimated Units `1000`, pilih Unit Type `Hour meter`, pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` lalu Tax Method `Straight Line`
5. Klik `[Submit]`
6. Verifikasi Dialog Blok `Depreciation Method Limit Reached` dengan teks `Your plan supports up to 2 depreciation methods. Use one of the methods already in use, or contact support.` dan tombol `OK`
7. Verifikasi jumlah Asset Class tetap C1 (tidak ada Asset Class dibuat)
8. Klik `[OK]` pada dialog
9. Klik breadcrumb `Asset Class`
10. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
11. Klik `[Leave]`

### TC-FA-FAAC-185: Edit ke Method ketiga melampaui batas ditolak D-22

12. Ketik Search `B-PE3`, tekan Enter
13. Klik link Class Code `B-PE3` di tabel
14. Pada tab Depreciation ganti Method menjadi `Units of Production`, isi Total Estimated Units `1000` dan Unit Type `Hour meter`
15. Klik `[Save]`
16. Verifikasi Dialog Blok `Depreciation Method Limit Reached` dengan teks `Your plan supports up to 2 depreciation methods. Use one of the methods already in use, or contact support.` dan tombol `OK`
17. Verifikasi jumlah entri Changelog Asset Class tetap N1 (tidak ada data tersimpan)
18. Klik `[OK]` pada dialog
19. Klik breadcrumb `Asset Class`
20. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
21. Klik `[Leave]`

### TC-FA-FAAC-141: Create memakai Method yang sudah ada tepat di batas berhasil

22. Klik tombol `[+ Asset Class]` di toolbar tabel
23. Pada tab General isi Class Code `B-P4`, Class Name `Test Class`
24. Pada tab Depreciation pilih Method `Declining Balance`, isi Useful Life `48` dan Declining Rate `40`, pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` lalu Tax Method `Declining Balance`
25. Klik `[Submit]`
26. Verifikasi toast sukses `Success, asset class has been created.`
27. Verifikasi tidak ada Dialog D-22 karena jumlah Method berbeda tetap 2

### TC-FA-FAAC-142: Not Depreciated tidak dihitung sebagai Method pada batas plan

28. Klik breadcrumb `Asset Class` untuk kembali ke tabel
29. Klik tombol `[+ Asset Class]` di toolbar tabel
30. Pada tab General isi Class Code `B-P5`, Class Name `NotDep Limit`
31. Pada tab Depreciation pilih Method `Not Depreciated` dan Tax Depreciation Class `Tanah`
32. Klik `[Submit]`
33. Verifikasi toast sukses `Success, asset class has been created.`
34. Verifikasi tidak ada Dialog D-22

### Keadaan E2: B-PE2 satu-satunya pemakai Declining Balance

35. Atur lewat fixture BE keadaan E2; muat ulang halaman lalu buka tab Asset Class

### TC-FA-FAAC-184: Edit mengganti Method satu-satunya pemakai Method lama pada batas berhasil

36. Ketik Search `B-PE2`, tekan Enter
37. Klik link Class Code `B-PE2` di tabel
38. Pada tab Depreciation ganti Method menjadi `Units of Production`, isi Total Estimated Units `1000` dan Unit Type `Hour meter`
39. Klik `[Save]`
40. Verifikasi toast sukses `Success, asset class has been updated.`
41. Verifikasi tidak ada Dialog D-22 karena Method lama `B-PE2` dikecualikan dari hitungan sehingga jumlah Method berbeda tetap 2

### Keadaan E3: B-PE8 satu-satunya pemakai Declining Balance

42. Atur lewat fixture BE keadaan E3; muat ulang halaman lalu buka tab Asset Class

### TC-FA-FAAC-146: Delete mengurangi hitungan Method sehingga Method lain dapat dipakai

43. Ketik Search `B-PE8`, tekan Enter
44. Hapus `B-PE8` lewat row action Delete lalu konfirmasi
45. Verifikasi empty state `No results found` tampil sehingga `B-PE8` sudah terhapus
46. Klik tombol `[+ Asset Class]` di toolbar tabel
47. Pada tab General isi Class Code `B-P7`, Class Name `Test Class`
48. Pada tab Depreciation pilih Method `Units of Production`, isi Useful Life `60`, Total Estimated Units `1000`, pilih Unit Type `Hour meter`, pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` lalu Tax Method `Straight Line`
49. Klik `[Submit]`
50. Verifikasi toast sukses `Success, asset class has been created.`
51. Verifikasi tidak ada Dialog D-22

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-140, 141, 142, 146, 184, 185). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC dikelompokkan menurut keadaan seed (E1, E2, E3); dalam E1 penolakan (TC-140, 185) lebih dulu dan Create sukses (TC-141, 142) sesudahnya karena TC-141 menambah pemakai `Declining Balance`; TC-184 dan TC-146 membutuhkan Method lama yang dipakai satu Asset Class sehingga memakai keadaan sendiri; TC-146 (Delete) terakhir (S-10).
- Pengecualian beralasan atas S-06 dan S-12: Class Code literal dari TC (`B-P3`, `B-P4`, `B-P5`, `B-P7`, `B-PE2`, `B-PE3`, `B-PE8`) dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seed idempotent per spec oleh fixture BE (keputusan yang disetujui user).
- Spec ini 51 langkah, di atas 35 langkah. Alasan: keenam TC satu topik (batas Method pada plan Multi Depreciation), setiap keadaan seed berdiri sendiri dan diatur ulang lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected mewajibkan `Verifikasi` dialog, state form, dan baseline per TC (S-01, S-12).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 1, 35, dan 42 (mengatur keadaan seed, mencatat baseline, dan memuat ulang), langkah 12, 36, dan 43 (Search untuk menemukan baris target), langkah 8 dan 18 (menutup Dialog Blok), langkah 9 sampai 11 dan 19 sampai 21 (menutup form dirty lewat dialog `Unsaved Changes`, S-08; langkah 10 dan 20 adalah `Verifikasi` dialog yang diwajibkan S-08), langkah 28 (kembali ke tabel lewat breadcrumb).
- Langkah 45 memakai empty state hasil Search sebagai bukti `B-PE8` terhapus karena TC-146 tidak menyebut teks toast Delete.
- Temuan untuk QA:
  - TC-140, 146, dan 185 tidak menyebut Useful Life, Class Name, dan nilai tax untuk "field wajib valid"; spec memakai `Test Class`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, dan Tax Method `Straight Line`.
  - TC-185 Expected b ("tidak ada data tersimpan") tidak menyebut cara pengamatan; langkah 17 membandingkan jumlah entri Changelog terhadap baseline.
  - TC-184 Expected ("Method lama B-PE2 dikecualikan dari hitungan sehingga jumlah Method berbeda tetap 2") adalah penjelasan; hanya ketiadaan D-22 dan toast yang diasersi.
  - TC-146 Expected "Delete berhasil" tidak menyebut cara pengamatan; lihat catatan langkah 45.
  - TC-142 tidak menyebut Useful Life dan Tax Method untuk Method `Not Depreciated`; spec mengikuti TC (hanya Method dan Tax Depreciation Class `Tanah`).
