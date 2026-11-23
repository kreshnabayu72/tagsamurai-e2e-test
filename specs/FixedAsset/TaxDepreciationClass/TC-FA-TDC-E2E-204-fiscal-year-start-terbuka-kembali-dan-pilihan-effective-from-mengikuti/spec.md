---
id: TC-FA-TDC-E2E-204-fiscal-year-start-terbuka-kembali-dan-pilihan-effective-from-mengikuti
title: "Preferences: Fiscal Year Start Terbuka Kembali dan Pilihan Effective From Mengikuti Fiscal Year Start"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-753
  - TC-FA-TDC-754
  - TC-FA-TDC-755
  - TC-FA-TDC-924
  - TC-FA-TDC-925
sourceRules: ["FATDC-LOGIC-04z", "S-12b", "S-12a", "T-07", "FATDC-LOGIC-04i", "§11.2#r6", "FATDC-LOGIC-04t", "FATDC-LOGIC-04d", "FATDC-LOGIC-04af", "FATDC-LOGIC-04ag", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04z": [6, 9, 20, 21, 31, 32]
  "S-12b": [6, 20]
  "S-12a": [9, 31, 32, 43, 44, 54, 55]
  "T-07": [15, 26, 38]
  "FATDC-LOGIC-04i": 15
  "§11.2#r6": [31, 43]
  "FATDC-LOGIC-04t": 62
  "FATDC-LOGIC-04d": 62
  "FATDC-LOGIC-04af": 63
  "FATDC-LOGIC-04ag": 63
  "§4.2c#b1": 67
coverage:
  web: automated
---

# Preferences: Fiscal Year Start Terbuka Kembali dan Pilihan Effective From Mengikuti Fiscal Year Start

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00); jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleData`, fixture belum ada): sembilan class Example Data PRD dengan tabel dalam satu halaman (9 baris, 10 baris per halaman) sehingga baris target tidak dicari lewat Search; belum ada penyusutan diposting. Kondisi tiap blok dibentuk lewat seeding di langkah penghubung (langkah 1, 10, 33, 45, 56):
  - TC-924: Fiscal Year Start `January`; NB-4 memiliki tiga versi (versi pertama tanpa Effective From berstatus Past, versi Jan 2025 Past, versi Jan 2026 Current); tidak ada versi Scheduled di class mana pun.
  - TC-925: Fiscal Year Start `January`; NB-2 memiliki versi Scheduled mulai Jan 2027 dan NB-3 (Used By 0) memiliki versi Scheduled mulai Jan 2028; tidak ada versi bertanggal lain.
  - TC-753: Fiscal Year Start `January`; NB-2 memiliki versi Scheduled mulai Jan 2027 sebagai satu-satunya versi bertanggal di seluruh class.
  - TC-754: Fiscal Year Start `January`; NB-3 (Used By 0, tanpa Last Posted Tax Year) memiliki versi Scheduled mulai Jan 2027 sebagai satu-satunya versi bertanggal di seluruh class.
  - TC-755: Fiscal Year Start `July` tersimpan; NB-4 hanya memiliki versi pertama tanpa Effective From.
  - Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data uji: perubahan Fiscal Year Start ke `July` pada tiap blok; TC-755 mengubah Useful Life NB-4 menjadi 10 untuk membuka dialog Save Changes.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class, versi (Past, Current, Scheduled), dan Fiscal Year Start lewat API (tanpa Run Posted); pemulihan data lewat API.
- State global yang diubah: Fiscal Year Start (menjadi July pada blok TC-925, TC-753, dan TC-754), versi NB-2, NB-3, dan NB-4, penghapusan NB-3, serta jam server dan browser. Dipulihkan di hook `after` lewat seeding ulang Fiscal Year Start `January` dan class Example Data, serta pemulihan jam.

## Test Steps

### TC-FA-TDC-924: Fiscal Year Start tidak dapat diubah selama ada versi Current yang memiliki Effective From

1. Seed NB-4 dengan tiga versi (pertama tanpa Effective From, Jan 2025, dan Jan 2026 Current), tanpa versi Scheduled, dan Fiscal Year Start `January` lewat seeding API
2. Buka Settings > Accounting > Preferences
3. Ubah Fiscal Year Start dari `January` menjadi `July`
4. Klik `[Save changes]`
5. Klik `[Save]` pada dialog konfirmasi Save Changes
6. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada field Fiscal Year Start
7. Kembalikan field Fiscal Year Start ke `January`
8. Muat ulang halaman
9. Verifikasi Fiscal Year Start tetap `January`

### TC-FA-TDC-925: Fiscal Year Start tetap terkunci selama masih ada versi Scheduled di class lain

10. Seed NB-2 dengan versi Scheduled Jan 2027, NB-3 dengan versi Scheduled Jan 2028, dan Fiscal Year Start `January` lewat seeding API
11. Buka Settings > Accounting > Tax Depreciation Class
12. Klik Class Code NB-2
13. Klik `[Cancel scheduled version]` pada Alert
14. Klik `[Cancel version]` pada dialog
15. Verifikasi toast sukses "Success, scheduled version has been cancelled."
16. Buka Settings > Accounting > Preferences
17. Ubah Fiscal Year Start dari `January` menjadi `July`
18. Klik `[Save changes]`
19. Klik `[Save]` pada dialog konfirmasi Save Changes
20. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada field Fiscal Year Start
21. Verifikasi nilai Fiscal Year Start tetap `January`
22. Buka Settings > Accounting > Tax Depreciation Class
23. Klik Class Code NB-3
24. Klik `[Cancel scheduled version]` pada Alert
25. Klik `[Cancel version]` pada dialog
26. Verifikasi toast sukses "Success, scheduled version has been cancelled."
27. Buka Settings > Accounting > Preferences
28. Ubah Fiscal Year Start dari `January` menjadi `July`
29. Klik `[Save changes]`
30. Klik `[Save]` pada dialog konfirmasi Save Changes hingga perubahan berhasil tersimpan
31. Verifikasi Fiscal Year Start tersimpan `July`
32. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tidak tampil

### TC-FA-TDC-753: Fiscal Year Start dapat diubah lagi setelah satu-satunya versi bertanggal dibatalkan

33. Seed NB-2 dengan versi Scheduled Jan 2027 sebagai satu-satunya versi bertanggal dan Fiscal Year Start `January` lewat seeding API
34. Buka Settings > Accounting > Tax Depreciation Class
35. Klik Class Code NB-2
36. Klik `[Cancel scheduled version]` pada Alert
37. Klik `[Cancel version]` pada dialog
38. Verifikasi toast sukses "Success, scheduled version has been cancelled."
39. Buka Settings > Accounting > Preferences
40. Ubah Fiscal Year Start dari `January` menjadi `July`
41. Klik `[Save changes]`
42. Klik `[Save]` pada dialog konfirmasi Save Changes hingga perubahan berhasil tersimpan
43. Verifikasi Fiscal Year Start tersimpan `July`
44. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tidak tampil

### TC-FA-TDC-754: Fiscal Year Start dapat diubah lagi setelah class pemilik versi bertanggal terakhir dihapus

45. Seed NB-3 dengan versi Scheduled Jan 2027 sebagai satu-satunya versi bertanggal dan Fiscal Year Start `January` lewat seeding API
46. Buka Settings > Accounting > Tax Depreciation Class
47. Klik tombol `⋯` baris NB-3
48. Klik `Delete`
49. Klik `[Delete]` pada dialog konfirmasi hingga NB-3 berhasil terhapus
50. Buka Settings > Accounting > Preferences
51. Ubah Fiscal Year Start dari `January` menjadi `July`
52. Klik `[Save changes]`
53. Klik `[Save]` pada dialog konfirmasi Save Changes hingga perubahan berhasil tersimpan
54. Verifikasi Fiscal Year Start tersimpan `July`
55. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tidak tampil

### TC-FA-TDC-755: Pilihan Effective From mengikuti Fiscal Year Start terbaru

56. Seed NB-4 hanya dengan versi pertama tanpa Effective From dan Fiscal Year Start `July` lewat seeding API
57. Buka Settings > Accounting > Tax Depreciation Class
58. Klik Class Code NB-4
59. Ubah Useful Life menjadi `10`
60. Klik `[Save]`
61. Klik field Effective From pada dialog Save Changes
62. Verifikasi nilai awal field Effective From adalah `Jul 2026`
63. Verifikasi pilihan Effective From berlabel `Jul 2026`, `Jul 2027`, `Jul 2028`, `Jul 2029`, `Jul 2030`, dan `Jul 2031`
64. Tekan Esc untuk menutup daftar pilihan Effective From
65. Klik `[Cancel]` pada dialog Save Changes
66. Klik `[×]` pada header Drawer Edit
67. Verifikasi dialog `Unsaved Changes` tampil
68. Klik `[Leave]`

## Notes

- Urutan TC di spec: 924, 925, 753, 754, 755. TC-924 dan TC-925 mengunci Fiscal Year Start dan berjalan dari kondisi `January`; TC-925, 753, dan 754 menyimpan `July` sehingga masing-masing didahului seeding `January` (langkah 10, 33, 45); TC-755 mensyaratkan `July` (langkah 56).
- Langkah penghubung (S-03): langkah 1, 10, 33, 45, 56 (seeding, tanpa asersi), langkah 2, 11, 16, 22, 27, 34, 39, 46, 50, 57 (berpindah halaman), langkah 7 (mengembalikan field dirty ke nilai tersimpan sebelum muat ulang, S-08 dan S-09), langkah 64 sampai 68 (menutup daftar pilihan, membatalkan dialog, dan menutup Drawer dirty lewat `[×]` dan `[Leave]`, S-08).
- Urutan `Verifikasi` pada blok yang berakhir dengan "tersimpan July" (langkah 31 dan 32, 43 dan 44, 54 dan 55): kondisi tersimpan `July` ditulis lebih dulu sebagai anchor positif sebelum asersi caption tidak tampil (8b.2).
- Langkah 20 dan 21 memecah Expected b TC-925 ("caption tampil pada field Fiscal Year Start dan nilai tetap January") menjadi dua `Verifikasi` (S-01); langkah 62 dan 63 memecah Expected TC-755 ("nilai awal ... dan pilihan ...").
- Alasan di atas ~35 langkah (68 langkah): satu topik (penguncian dan pembukaan kembali Fiscal Year Start oleh versi bertanggal). Kelima blok di-seed ulang di langkah 1, 10, 33, 45, dan 56, sehingga tidak ada blok yang bergantung pada hasil blok sebelumnya. Langkah menyambung hanya di dalam blok TC-FA-TDC-925: langkah 22 sampai 32 (batalkan versi NB-3 lalu simpan `July`) bergantung pada seed langkah 10 dan pembatalan versi NB-2 pada langkah 12 sampai 15. Panjang spec berasal dari perpindahan berulang antara Preferences dan Tax Depreciation Class.
- Pembagian TC lintas spec: TC-749, 750, 751, dan 752 (Fiscal Year Start terkunci) ada di spec 203.
- Temuan untuk QA:
  - TC-925 Expected b menyebut "nilai tetap January" segera setelah penolakan; TC tidak menyebut apakah field kembali ke nilai tersimpan atau tetap menampilkan nilai yang diubah. Spec mengikuti Expected TC (langkah 21) tanpa muat ulang.
  - TC-753, 754, 925 Expected tentang "tersimpan July" tidak menyebut toast sukses Preferences; spec mengasersi nilai field setelah simpan (langkah 31, 43, 54).
  - TC-755 tidak menyebut cara menutup daftar pilihan dan dialog sesudah asersi; spec menutupnya lewat `Esc`, `[Cancel]`, dan `[Leave]` supaya NB-4 tidak berubah.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
