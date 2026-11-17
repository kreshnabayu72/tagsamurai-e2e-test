---
id: TC-FA-TDC-E2E-156-setup-column-tabel-utama-tutup-tanpa-save-guard-panel-cepat-dan-lintas-popup
title: "Setup Column Tabel Utama: Tutup Tanpa Save, Guard Satu Kolom, Panel Cepat, dan Independensi Lintas Popup"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-548
  - TC-FA-TDC-549
  - TC-FA-TDC-550
  - TC-FA-TDC-552
  - TC-FA-TDC-553
sourceRules: ["§5#b9", "§4.1.1#b4", "§4.1.6#r1", "§4.1.6#r2", "§4.1.6#r3", "§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§9.5#r4"]
smoke: []
dependsOn: []
trace:
  "§5#b9": [6, 12, 27, 29, 30, 33]
  "§4.1.1#b4": [17, 22]
  "§4.1.6#r1": [40, 61]
  "§4.1.6#r2": [40, 62]
  "§4.1.6#r3": 40
  "§4.1.1#r25": [43, 68]
  "§4.1.1#r26": 43
  "§4.1.1#r27": 43
  "§4.1.1#r28": [43, 69]
  "§4.1.1#r29": 43
  "§4.1.1#r30": 43
  "§4.1.1#r31": 43
  "§9.5#r4": 59
anchor: [5, 11]
coverage:
  web: automated
---

# Setup Column Tabel Utama: Tutup Tanpa Save, Guard Satu Kolom, Panel Cepat, dan Independensi Lintas Popup

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-1 memiliki Used By `5` dan riwayat Changelog. Konfigurasi kolom awal adalah default: 10 kolom tampil (`Active`, `Class Code`, `Class Name`, `Asset Type`, `Useful Life (years)`, `Straight Line Rate`, `Declining Balance Rate`, `Allowed Methods`, `Used By`, `Effective From`) dan tiga kolom tersembunyi. Kolom Popup Used By: `Asset Class | Tax Method | Asset Names`; kolom Popup Changelog: `Date | Action | Class Code | Field | Old Value | New Value | Modified By`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); Overlay Column Visibility dan Popup Setup Column (termasuk pada Popup Used By dan Popup Changelog); mengarahkan kursor untuk tooltip; menekan Esc; muat ulang halaman (F5); preferensi kolom tersimpan di browser dan dihapus di hook `after` (`suite.md`); pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom tabel utama, Popup Used By, dan Popup Changelog (dipulihkan dengan langkah eksplisit pada langkah 23, 24, 45 sampai 48, 63 sampai 66, dan 70 sampai 73). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Menutup Popup Setup Column tanpa Save membuang perubahan (TC-FA-TDC-548)

1. Klik icon `⋯` pada header kolom Actions
2. Klik `Setup Column...`
3. Hapus centang checkbox Active
4. Klik `(X)` pada Popup
5. Verifikasi Popup tertutup
6. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (kolom Active tampil)
7. Klik icon `⋯` pada header kolom Actions
8. Klik `Setup Column...`
9. Hapus centang checkbox Active
10. Tekan Esc
11. Verifikasi Popup tertutup
12. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (kolom Active tampil)

### Guard satu kolom tersisa: checkbox terakhir tidak dapat di-uncheck (TC-FA-TDC-549)

13. Klik icon `⋯` pada header kolom Actions
14. Klik `Setup Column...`
15. Hapus centang semua kolom kecuali Class Code
16. Arahkan kursor ke checkbox Class Code
17. Verifikasi (Popup) checkbox Class Code Disabled (tetap tampil) dengan tooltip `At least one column must remain visible.`
18. Klik `(X)` pada Popup tanpa `[Save]`
19. Klik icon `⋯` pada header kolom Actions
20. Hapus centang semua kolom kecuali Class Code pada Overlay Column Visibility
21. Arahkan kursor ke checkbox Class Code
22. Verifikasi (Overlay) checkbox Class Code Disabled (tetap tampil) dengan tooltip `At least one column must remain visible.`
23. Centang kembali Active, Class Name, Asset Type, Useful Life (years), Straight Line Rate, Declining Balance Rate, Allowed Methods, Used By, dan Effective From pada Overlay Column Visibility
24. Tutup Overlay Column Visibility

### Panel cepat Column Visibility menerapkan perubahan langsung tanpa Save (TC-FA-TDC-550)

25. Klik icon `⋯` pada header kolom Actions
26. Hapus centang Used By
27. Verifikasi kolom Used By hilang dari tabel seketika tanpa tombol Save
28. Refresh halaman (F5)
29. Verifikasi kolom Class Code tampil di tabel
30. Verifikasi kolom Used By tetap tersembunyi setelah F5
31. Klik icon `⋯` pada header kolom Actions
32. Centang Used By
33. Verifikasi kolom Used By tampil seketika
34. Tutup Overlay Column Visibility

### Konfigurasi kolom tabel utama tidak memengaruhi Popup Used By dan Popup Changelog (TC-FA-TDC-552)

35. Klik icon `⋯` pada header kolom Actions
36. Klik `Setup Column...`
37. Hapus centang checkbox Used By
38. Klik `[Save]`
39. Klik angka `5` pada NB-1 untuk membuka Popup Used By
40. Verifikasi Popup Used By tetap menampilkan kolom `Asset Class | Tax Method | Asset Names`
41. Tutup Popup Used By
42. Klik icon Changelog
43. Verifikasi Popup Changelog tetap menampilkan 7 kolom `Date | Action | Class Code | Field | Old Value | New Value | Modified By`
44. Tutup Popup Changelog
45. Klik icon `⋯` pada header kolom Actions
46. Klik `Setup Column...`
47. Centang checkbox Used By
48. Klik `[Save]`

### Konfigurasi kolom Popup Used By dan Popup Changelog tidak memengaruhi tabel utama (TC-FA-TDC-553)

49. Klik angka `5` pada NB-1 untuk membuka Popup Used By
50. Buka Popup Setup Column pada Popup Used By
51. Hapus centang kolom Tax Method
52. Klik `[Save]`
53. Tutup Popup Used By
54. Klik icon Changelog
55. Buka Popup Setup Column pada Popup Changelog
56. Hapus centang kolom Field
57. Klik `[Save]`
58. Tutup Popup Changelog
59. Verifikasi tabel utama tetap menampilkan 10 kolom default
60. Klik angka `5` pada NB-1 untuk membuka Popup Used By
61. Verifikasi kolom Asset Class tampil pada Popup Used By
62. Verifikasi Popup Used By tetap menyembunyikan kolom Tax Method pada pembukaan berikutnya
63. Buka Popup Setup Column pada Popup Used By
64. Centang kolom Tax Method
65. Klik `[Save]`
66. Tutup Popup Used By
67. Klik icon Changelog
68. Verifikasi kolom Date tampil pada Popup Changelog
69. Verifikasi Popup Changelog tetap menyembunyikan kolom Field
70. Buka Popup Setup Column pada Popup Changelog
71. Centang kolom Field
72. Klik `[Save]`
73. Tutup Popup Changelog

## Notes

- Langkah penghubung (S-03): langkah 23 dan 24 (mengembalikan sembilan kolom di Overlay yang menerapkan perubahan langsung dan menutup Overlay; pemulihan Setup Column, 8b.14, R-24), langkah 34 (menutup Overlay), langkah 45 sampai 48 (menampilkan kembali kolom Used By pada tabel utama; pemulihan Setup Column), langkah 63 sampai 66 dan 70 sampai 73 (menampilkan kembali kolom Tax Method dan Field; pemulihan Setup Column), langkah 41, 44, 53, 58, dan 66 (menutup popup). Hook `after` hanya cadangan.
- Urutan TC dalam spec: TC-FA-TDC-548, 549, 550, 552, 553. TC-FA-TDC-551 (Column Visibility per browser) ada di spec lain.
- Asersi absence langkah 30 didahului anchor langkah 29 (kolom Class Code tampil sesudah F5); asersi absence langkah 62 dan 69 didahului anchor langkah 61 dan 68 (kolom lain pada popup yang sama tampil; 8b.2, asersi tambahan di luar TC).
- Spec ini 73 langkah, di atas ~35 langkah. Alasan: satu topik (Setup Column tabel utama dan independensinya terhadap popup lain) pada dataset Example Data yang sama, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan S-01 mengharuskan satu `Verifikasi` per klausa; langkah 23 dan 24, 45 sampai 48, serta 63 sampai 73 adalah pemulihan Setup Column yang diwajibkan 8b.14.
- Temuan untuk QA:
  - TC-FA-TDC-552 langkah 2 mengklik angka `5` pada NB-1 untuk membuka Popup Used By, padahal langkah 1 menyembunyikan kolom Used By pada tabel utama sehingga angka itu tidak tampil; langkah tidak dapat dijalankan sebagaimana tertulis. Spec mengikuti TC (langkah 39). Usulan: sembunyikan kolom lain atau buka Popup Used By lewat jalur yang tersedia saat kolom Used By tersembunyi.
  - TC-FA-TDC-553 tidak menyebut cara membuka Popup Setup Column pada Popup Used By dan Popup Changelog; spec menuliskan "Buka Popup Setup Column pada Popup ..." tanpa mengarang kontrol.
  - TC-FA-TDC-553 Expected a ("tabel utama tetap menampilkan 10 kolom default") mengandalkan kolom Used By tampil kembali; spec memulihkannya pada langkah 45 sampai 48 (TC-FA-TDC-552).
  - TC-FA-TDC-549 langkah 3 menyebut Overlay tanpa Save sehingga penghapusan centang berlaku langsung; spec memulihkannya pada langkah 23.
  - TC-FA-TDC-548 Expected tidak menyebut apakah konfirmasi diminta saat menutup Popup dengan perubahan; spec mengasumsikan tidak ada dialog.
  - Email akun Total Control tidak tertulis di TC.
