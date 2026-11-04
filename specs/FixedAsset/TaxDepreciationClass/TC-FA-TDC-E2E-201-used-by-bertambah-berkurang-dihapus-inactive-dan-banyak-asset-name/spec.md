---
id: TC-FA-TDC-E2E-201-used-by-bertambah-berkurang-dihapus-inactive-dan-banyak-asset-name
title: "Used By: Bertambah, Berkurang, Asset Class Dihapus, Asset Class Inactive, dan Banyak Asset Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-740
  - TC-FA-TDC-741
  - TC-FA-TDC-742
  - TC-FA-TDC-743
  - TC-FA-TDC-744
coverage:
  web: automated
---

# Used By: Bertambah, Berkurang, Asset Class Dihapus, Asset Class Inactive, dan Banyak Asset Name

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleDataPlusNb3`, fixture belum ada): sembilan class Example Data PRD ditambah class seed NB-3, sehingga tabel berisi 10 baris dalam satu halaman (10 baris per halaman) dan baris target tidak dicari lewat Search. Kondisi awal: NB-4 (`Bukan bangunan – Kelompok 4`, Active, Used By 0, tanpa Last Posted Tax Year) dan NB-3 (`Bukan bangunan – Kelompok 3`, Active, Used By 0). Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data Asset Class (disediakan tim FE/BE lewat fixture BE, kunci `assetClassLaptop`): Asset Class `AC-LAPTOP` memakai NB-4 dengan Tax Method `Straight Line`, Active, dan 5 Asset Name ter-assign. Dibentuk dan dipulihkan lewat seeding di langkah penghubung blok (langkah 15, 21, 26, 41) dan di hook `after`.
- Data Dinamis TC-740 (milik spec, kunci `assetClassBaru`): Asset Class baru `AC-NEW-{runId}-201` dengan field wajib lain berisi nilai dari fixture (TC tidak menyebut nilainya); dibuat lewat UI di langkah 8 dan dihapus lewat seeding di langkah 15 serta hook `after`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding dan penghapusan Asset Class beserta Asset Name, pengubahan status Active Asset Class, dan pemulihan class lewat API.
- State global yang diubah: Used By NB-4 dan NB-3, status AC-LAPTOP, dan penghapusan AC-LAPTOP. Dipulihkan di hook `after` lewat seeding ulang data di atas.

## Test Steps

### TC-FA-TDC-740: Used By bertambah saat Asset Class baru memakai class

1. Klik tab Asset Class
2. Klik `+ Asset Class`
3. Klik dropdown Tax Depreciation Class
4. Pilih `Bukan bangunan – Kelompok 4 — 20 yrs`
5. Klik dropdown Tax Method
6. Pilih `Straight Line`
7. Isi field wajib lain Asset Class `AC-NEW-{runId}-201` sesuai fixture `assetClassBaru`
8. Klik `[Submit]` hingga Asset Class berhasil tersimpan
9. Klik tab Tax Depreciation Class
10. Verifikasi kolom Used By baris NB-4 bernilai 1
11. Verifikasi kolom Used By baris NB-4 berupa link
12. Klik angka Used By baris NB-4
13. Verifikasi modal "Used By" memuat satu baris Asset Class `AC-NEW-{runId}-201` dengan Tax Method `Straight Line`
14. Verifikasi baris tersebut memuat kolom Asset Names dengan jumlah Asset Name
15. Hapus `AC-NEW-{runId}-201` dan seed `AC-LAPTOP` (NB-4, `Straight Line`, Active, 5 Asset Name) lewat seeding API, lalu muat ulang halaman

### TC-FA-TDC-744: Asset Class dengan banyak Asset Name dihitung satu kali

16. Verifikasi kolom Used By baris NB-4 bernilai 1
17. Klik angka Used By baris NB-4
18. Verifikasi modal "Used By" memuat satu baris AC-LAPTOP
19. Verifikasi baris AC-LAPTOP memuat kolom Asset Names bernilai 5
20. Tutup modal "Used By" lewat `[×]` pada header modal

### TC-FA-TDC-743: Asset Class Inactive tetap dihitung dalam Used By

21. Ubah AC-LAPTOP menjadi Inactive lewat seeding API, lalu muat ulang halaman
22. Verifikasi kolom Used By baris NB-4 bernilai 1
23. Klik toggle `Active` baris NB-4
24. Verifikasi dialog blok "Cannot Deactivate Tax Depreciation Class" dengan kalimat "Used by 1 asset class. Change it in Asset Class first."
25. Klik `[OK]` pada dialog blok

### TC-FA-TDC-741: Used By dihitung ulang saat Asset Class memindahkan class

26. Ubah AC-LAPTOP menjadi Active lewat seeding API
27. Klik tab Asset Class
28. Ketik Search `AC-LAPTOP`, tekan Enter
29. Buka Drawer Edit Asset Class AC-LAPTOP
30. Klik dropdown Tax Depreciation Class
31. Pilih `Bukan bangunan – Kelompok 3 — 16 yrs`
32. Klik dropdown Tax Method
33. Pilih `Straight Line`
34. Klik `[Save]` hingga Asset Class berhasil tersimpan
35. Klik tab Tax Depreciation Class
36. Verifikasi kolom Used By baris NB-4 bernilai 0
37. Verifikasi kolom Used By baris NB-4 berupa teks biasa
38. Verifikasi kolom Used By baris NB-3 bernilai 1
39. Verifikasi kolom Used By baris NB-3 berupa link

### TC-FA-TDC-742: Asset Class yang dihapus tidak dihitung dalam Used By

40. Klik tab Asset Class
41. Kembalikan AC-LAPTOP ke NB-4 (`Straight Line`, Active) lewat seeding API, lalu muat ulang halaman
42. Ganti isi kotak search dengan `AC-LAPTOP`, tekan Enter
43. Hapus Asset Class AC-LAPTOP dan konfirmasi hingga berhasil terhapus
44. Klik tab Tax Depreciation Class
45. Verifikasi kolom Used By baris NB-4 bernilai 0

## Notes

- Urutan TC di spec: 740, 744, 743, 741, 742. TC-740 mensyaratkan NB-4 Used By 0 sehingga berjalan pertama; TC-744 dan TC-743 membaca AC-LAPTOP pada NB-4; TC-741 memindahkan AC-LAPTOP ke NB-3 dan TC-742 menghapusnya sehingga keduanya terakhir.
- Langkah penghubung (S-03): langkah 1, 9, 27, 35, 40, 44 (berpindah tab), langkah 15, 21, 26, 41 (seeding, tanpa asersi), langkah 20 dan 25 (menutup modal atau dialog blok), serta langkah 28 dan 42 (Search AC-LAPTOP untuk menemukan baris target, R-16). Search, Filter, Sort, dan halaman dipertahankan sesudah muat ulang halaman (F5, 8b.9), jadi langkah 42 menulis "ganti isi kotak search" untuk mengganti nilai Search langkah 28. Asumsi (8b.9, keputusan user 2026-11-04): kotak Search tab Asset Class mempertahankan nilainya lintas pindah tab (langkah 35 dan 40) dan muat ulang halaman (langkah 41), sehingga pada langkah 42 kotak itu masih berisi `AC-LAPTOP`; perlu konfirmasi FE.
- Keadaan Used By setelah langkah 26 (NB-4 tetap 1, NB-3 0) adalah keadaan awal TC-741 menurut Pre-setup TC, bukan asersi spec; asersi pertama TC-741 ada di langkah 36 dan 38.
- Langkah 14 (kolom Asset Names tampil dengan jumlah) memecah Expected b TC-740; TC tidak menyebut nilai jumlah untuk Asset Class baru (lihat Temuan).
- Alasan di atas ~35 langkah (45 langkah, tanpa perulangan): satu topik (kolom Used By terhadap Asset Class pemakai) dengan lima blok TC. Blok dibentuk ulang lewat seeding pada langkah penghubung bernama (langkah 15, 21, 26, dan 41) sehingga tidak ada blok yang memakai hasil aksi tulis blok sebelumnya; sambungan antar blok hanya `AC-LAPTOP` yang disemai pada langkah 15 dan dibaca TC-744 (hanya baca), lalu diubah statusnya pada langkah 21 dan 26 serta dikembalikan pada langkah 41. Langkahnya panjang karena seeding ulang, perpindahan tab Tax Depreciation Class dan Asset Class, dan satu `Verifikasi` per klausa (S-01); spec tidak dipecah karena kelima blok memakai dataset dan Asset Class yang sama.
- Temuan untuk QA:
  - TC-740 menyebut "isi form" Asset Class hanya dengan Tax Depreciation Class dan Tax Method; field wajib lain tidak disebut, spec memakai nilai fixture.
  - TC-740 Expected b menyebut "jumlah Asset Names" tanpa nilainya; spec hanya mengasersi kolom memuat jumlah.
  - TC-741 dan 742 tidak menyebut cara membuka Drawer Edit dan menghapus Asset Class (menu baris atau lainnya); spec menulis "Buka Drawer Edit" dan "Hapus ... dan konfirmasi" tanpa label tombol, perlu dilengkapi dari PRD Asset Class.
  - TC-743 mensyaratkan AC-LAPTOP berstatus Inactive tanpa menyebut cara menyiapkannya; spec memakai seeding API.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
