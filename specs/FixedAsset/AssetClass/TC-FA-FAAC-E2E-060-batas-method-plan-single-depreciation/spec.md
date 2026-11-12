---
id: TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation
title: "Batas Method pada Plan Single Depreciation: Dialog Blok Depreciation Method Limit Reached"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-138
  - TC-FA-FAAC-139
  - TC-FA-FAAC-144
  - TC-FA-FAAC-145
  - TC-FA-FAAC-183
  - TC-FA-FAAC-186
  - TC-FA-FAAC-187
coverage:
  web: automated
---

# Batas Method pada Plan Single Depreciation: Dialog Blok Depreciation Method Limit Reached

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- State global yang diubah spec: plan client Growth (Single Depreciation) dan komposisi Method Asset Class pada tiga keadaan seed (S1, S2, S3 di bawah). Mekanisme pelaku perubahan plan dan seed tidak disebut TC, PRD, atau LLD; fixture BE untuk mengatur plan dan seed "disediakan tim FE/BE" (tanpa akun atau endpoint karangan). Hook `before` mencatat keadaan awal dan hook `after` memulihkan plan dan seed awal lewat fixture BE, juga bila spec gagal di tengah. Suite berjalan serial.
- Keadaan S1 (langkah 1): plan Growth (Single Depreciation); semua Asset Class berpenyusutan memakai `Straight Line`, termasuk `B-PE1`. Keadaan S2 (langkah 37): plan Growth; Asset Class Active memakai `Straight Line`; `B-PE6` dan `B-PE7` Inactive memakai `Declining Balance`. Keadaan S3 (langkah 53): plan Growth setelah downgrade dari Enterprise; data tersimpan memakai `Straight Line` dan `Declining Balance` (`B-PE4` dan `B-PE5`). Seed disediakan fixture BE.
- Data Pre-setup yang diubah dan dipulihkan fixture BE: `B-PE6` diaktifkan (langkah 50) dan `B-PE4` diganti Class Name menjadi `Downgrade Renamed` (langkah 65 dan 66); Last Updated keduanya ikut berubah.
- Data yang dibuat spec: Asset Class `B-P2` (langkah 31 sampai 34); `B-P1` dan `B-P6` ditolak dialog sehingga tidak tersimpan. Hook `after` menghapus `B-P2` lewat fixture BE.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Kemampuan teknis: membaca jumlah Asset Class dan jumlah entri Changelog Asset Class, System Log aktor, dan Activity Log FAMS lewat fixture BE (audit trail permanen; asersi memakai selisih terhadap baseline, bukan angka absolut).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.

## Test Steps

### Keadaan S1: semua Asset Class berpenyusutan memakai Straight Line

1. Atur lewat fixture BE keadaan S1; catat jumlah Asset Class (C1) serta jumlah entri Changelog Asset Class (N1), System Log aktor (Ns1), dan Activity Log FAMS (Na1); muat ulang halaman

### TC-FA-FAAC-138: Create dengan Method berbeda pada plan Single Depreciation ditolak D-22

2. Klik tombol `[+ Asset Class]` di toolbar tabel
3. Pada tab General isi Class Code `B-P1`, Class Name `Test Class`
4. Pada tab Depreciation pilih Method `Declining Balance`, isi Useful Life `48` dan Declining Rate `40`, pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` lalu Tax Method `Declining Balance`
5. Klik `[Submit]`
6. Verifikasi Dialog Blok `Depreciation Method Limit Reached` dengan teks `Your plan supports 1 depreciation method. Use the method your asset classes already use, or upgrade your plan.` dan tombol `OK`
7. Klik `[OK]` pada dialog
8. Verifikasi halaman Detail tetap terbuka dengan isian utuh
9. Verifikasi jumlah Asset Class tetap C1 (tidak ada Asset Class dibuat)
10. Verifikasi jumlah entri Changelog Asset Class tetap N1 (tidak ada log)
11. Verifikasi jumlah entri System Log aktor tetap Ns1 (tidak ada log)
12. Verifikasi jumlah entri Activity Log FAMS tetap Na1 (tidak ada log)
13. Klik breadcrumb `Asset Class`
14. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
15. Klik `[Leave]`
16. Catat ulang jumlah entri Changelog Asset Class (N2), System Log aktor (Ns2), dan Activity Log FAMS (Na2) lewat kemampuan baca BE sebagai baseline TC-FA-FAAC-183

### TC-FA-FAAC-183: Edit mengubah Method sehingga melampaui batas ditolak D-22

17. Ketik Search `B-PE1`, tekan Enter
18. Klik link Class Code `B-PE1` di tabel
19. Pada tab Depreciation ganti Method menjadi `Declining Balance` dan isi Declining Rate `40`
20. Klik `[Save]`
21. Verifikasi Dialog Blok `Depreciation Method Limit Reached` dengan teks `Your plan supports 1 depreciation method. Use the method your asset classes already use, or upgrade your plan.` dan tombol `OK`
22. Klik `[OK]` pada dialog
23. Verifikasi halaman Detail tetap terbuka
24. Verifikasi jumlah entri Changelog Asset Class tetap N2 (tidak ada log)
25. Verifikasi jumlah entri System Log aktor tetap Ns2 (tidak ada log)
26. Verifikasi jumlah entri Activity Log FAMS tetap Na2 (tidak ada log)
27. Klik breadcrumb `Asset Class`
28. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
29. Klik `[Leave]`
30. Verifikasi kolom Commercial baris `B-PE1` tetap memuat Method `Straight Line` (tidak ada data tersimpan)

### TC-FA-FAAC-139: Create dengan Method yang sama pada plan Single Depreciation berhasil

31. Klik tombol `[+ Asset Class]` di toolbar tabel
32. Pada tab General isi Class Code `B-P2`, Class Name `Test Class`
33. Pada tab Depreciation pilih Method `Straight Line`, isi Useful Life `60`, pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` lalu Tax Method `Declining Balance`
34. Klik `[Submit]`
35. Verifikasi toast sukses `Success, asset class has been created.`
36. Verifikasi tidak ada Dialog D-22

### Keadaan S2: Asset Class Inactive tetap dihitung pada batas Method

37. Atur lewat fixture BE keadaan S2; catat jumlah Asset Class (C2); muat ulang halaman lalu buka tab Asset Class

### TC-FA-FAAC-145: Asset Class Inactive tetap dihitung pada batas Method

38. Klik tombol `[+ Asset Class]` di toolbar tabel
39. Pada tab General isi Class Code `B-P6`, Class Name `Test Class`
40. Pada tab Depreciation pilih Method `Declining Balance`, isi Useful Life `48` dan Declining Rate `40`, pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` lalu Tax Method `Declining Balance`
41. Klik `[Submit]`
42. Verifikasi Dialog Blok `Depreciation Method Limit Reached` dengan teks `Your plan supports 1 depreciation method. Use the method your asset classes already use, or upgrade your plan.` dan tombol `OK`
43. Verifikasi jumlah Asset Class tetap C2 (tidak ada Asset Class dibuat)
44. Klik `[OK]` pada dialog
45. Klik breadcrumb `Asset Class`
46. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
47. Klik `[Leave]`

### TC-FA-FAAC-144: Activate Asset Class tidak mengubah hitungan Method

48. Ketik Search `B-PE6`, tekan Enter
49. Klik toggle Active pada baris `B-PE6` (Method `Declining Balance`, Inactive)
50. Konfirmasi pada dialog aktivasi
51. Verifikasi toast sukses `Success, asset class has been activated.`
52. Verifikasi tidak ada Dialog D-22 dan tidak ada pengecekan batas plan

### Keadaan S3: setelah downgrade dari Enterprise

53. Atur lewat fixture BE keadaan S3; muat ulang halaman lalu buka tab Asset Class

### TC-FA-FAAC-187: Save yang mengubah Method setelah downgrade ditolak D-22

54. Ketik Search `B-PE5`, tekan Enter
55. Klik link Class Code `B-PE5` di tabel
56. Ganti Method `B-PE5` dari `Declining Balance` menjadi `Units of Production`, isi Total Estimated Units `1000` dan Unit Type `Hour meter`
57. Klik `[Save]`
58. Verifikasi Dialog Blok `Depreciation Method Limit Reached` dengan teks `Your plan supports 1 depreciation method. Use the method your asset classes already use, or upgrade your plan.` dan tombol `OK`
59. Klik `[OK]` pada dialog
60. Klik breadcrumb `Asset Class`
61. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
62. Klik `[Leave]`

### TC-FA-FAAC-186: Save tanpa mengubah Method tetap berhasil setelah downgrade

63. Ganti isi kotak search dengan `B-PE4`, tekan Enter
64. Klik link Class Code `B-PE4` di tabel
65. Pada tab General ubah Class Name menjadi `Downgrade Renamed` tanpa mengubah Method
66. Klik `[Save]`
67. Verifikasi toast sukses `Success, asset class has been updated.`
68. Verifikasi tidak muncul Dialog D-22

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-138, 139, 144, 145, 183, 186, 187). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC dikelompokkan menurut keadaan seed (S1, S2, S3) agar fixture BE mengatur state sekali per keadaan; dalam S1 penolakan (TC-138, 183) lebih dulu dan Create sukses (TC-139) terakhir; TC-145 sebelum TC-144 karena TC-144 mengaktifkan `B-PE6` yang dibutuhkan TC-145 tetap Inactive; TC-187 sebelum TC-186 (S-10).
- Pengecualian beralasan atas S-06 dan S-12: Class Code literal dari TC (`B-P1`, `B-P2`, `B-P6`, `B-PE1`, `B-PE4` sampai `B-PE7`) dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seed idempotent per spec oleh fixture BE (keputusan yang disetujui user).
- Spec ini 68 langkah, di atas 35 langkah. Alasan: ketujuh TC satu topik (batas Method pada plan Single Depreciation), setiap keadaan seed berdiri sendiri dan diatur ulang lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected mewajibkan `Verifikasi` dialog, state form, dan baseline log per TC (S-01, S-12).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 1, 37, dan 53 (mengatur keadaan seed, mencatat baseline, dan memuat ulang), langkah 16 (mencatat ulang baseline sebelum TC-FA-FAAC-183), langkah 17, 48, 54, dan 63 (Search untuk menemukan baris target; langkah 63 memakai "ganti isi kotak search" karena kotak Search mempertahankan nilainya, 8b.9), langkah 7, 22, 44, dan 59 (menutup Dialog Blok seperti langkah TC), langkah 13 sampai 15, 27 sampai 29, 45 sampai 47, dan 60 sampai 62 (menutup form dirty lewat dialog `Unsaved Changes`, S-08; langkah 14, 28, 46, dan 61 adalah `Verifikasi` dialog yang diwajibkan S-08), langkah 50 (konfirmasi aktivasi seperti TC-144).
- "Tidak ada log" pada langkah 10 sampai 12 dan 24 sampai 26 adalah asersi selisih jumlah terhadap baseline di tiga surface (Changelog Asset Class, System Log aktor, Activity Log FAMS; S-12, prinsip 13g), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC-145 menyebut `B-PE7` Inactive di Precondition dan `B-PE6` di langkah 2 sebagai satu-satunya Asset Class dengan `Declining Balance`; TC-144 memakai `B-PE6` yang sama sebagai Inactive yang diaktifkan. Spec mengasumsikan `B-PE6` dan `B-PE7` keduanya Inactive `Declining Balance` pada keadaan S2.
  - TC-145 Expected a memakai klausa "bila batas satu Method"; spec memakai teks plan Single Depreciation.
  - TC-138, 145, 183, dan 187 tidak menyebut Class Name dan nilai tax untuk "field wajib valid"; spec memakai `Test Class` dan Tax Depreciation Class `Bukan bangunan – Kelompok 3` dengan Tax Method `Declining Balance` seperti TC Create lain.
  - TC-183 Expected b ("tidak ada data tersimpan") tidak menyebut cara pengamatan; langkah 30 membaca kolom Commercial baris `B-PE1` sesudah form ditutup.
  - TC-144 Expected ("tanpa pengecekan batas plan") hanya teramati sebagai ketiadaan Dialog D-22; langkah 52 mengasersi ketiadaan dialog.
  - TC-144 tidak menyebut teks dialog konfirmasi aktivasi; spec memakai "dialog aktivasi" generik.
