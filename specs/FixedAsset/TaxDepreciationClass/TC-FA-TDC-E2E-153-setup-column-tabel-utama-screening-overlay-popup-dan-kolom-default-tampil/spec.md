---
id: TC-FA-TDC-E2E-153-setup-column-tabel-utama-screening-overlay-popup-dan-kolom-default-tampil
title: "Setup Column Tabel Utama: Screening Overlay dan Popup, serta Kolom Default Tampil"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-539
  - TC-FA-TDC-540
  - TC-FA-TDC-541
sourceRules: ["§4.4#r11", "§4.1.1#r1", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r8", "§4.1.1#r9", "§4.1.1#r10", "§4.1.1#r11", "§4.1.1#r12", "§4.1.1#r13", "§9.5#r4", "§4.1#r8", "§5#b9"]
smoke: []
dependsOn: []
trace:
  "§4.4#r11": [2, 6]
  "§4.1.1#r1": [3, 13]
  "§4.1.1#r2": [3, 13]
  "§4.1.1#r3": [3, 13]
  "§4.1.1#r4": [3, 13]
  "§4.1.1#r5": [3, 13]
  "§4.1.1#r6": [3, 13]
  "§4.1.1#r7": [3, 13]
  "§4.1.1#r8": [3, 13]
  "§4.1.1#r9": [3, 13]
  "§4.1.1#r10": [3, 13]
  "§4.1.1#r11": [3, 13]
  "§4.1.1#r12": [3, 13]
  "§4.1.1#r13": [3, 13]
  "§9.5#r4": [4, 14]
  "§4.1#r8": 10
  "§5#b9": [19, 25, 27, 32]
anchor: [5, 11, 12, 15, 16, 17, 23]
coverage:
  web: automated
---

# Setup Column Tabel Utama: Screening Overlay dan Popup, serta Kolom Default Tampil

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. Konfigurasi kolom awal adalah default: 13 kolom berurutan `Active`, `Class Code`, `Class Name`, `Asset Type`, `Useful Life (years)`, `Straight Line Rate`, `Declining Balance Rate`, `Allowed Methods`, `Used By`, `Effective From`, `Regulation Reference`, `Modified By`, `Last Updated`; 10 kolom pertama tampil dan tiga kolom terakhir tersembunyi.
- Tabel parameter perulangan TC-FA-TDC-541 (kolom tampil secara default), literal TC: `Active`, `Class Code`, `Class Name`, `Asset Type`, `Useful Life (years)`, `Straight Line Rate`, `Declining Balance Rate`, `Allowed Methods`, `Used By`, `Effective From` (sepuluh baris, satu kolom per baris).
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); Overlay Column Visibility dan Popup Setup Column; muat ulang halaman (F5); preferensi kolom tersimpan di browser dan dihapus di hook `after` (`suite.md`); pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom tabel utama (satu kolom disembunyikan lalu ditampilkan kembali di tiap iterasi langkah 19 sampai 32, sehingga kembali ke default). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Screening Overlay Column Visibility (TC-FA-TDC-539)

1. Klik icon `⋯` pada header kolom Actions
2. Verifikasi Overlay tampil menempel pada pemicu tanpa backdrop
3. Verifikasi daftar kolom berurutan `Active | Class Code | Class Name | Asset Type | Useful Life (years) | Straight Line Rate | Declining Balance Rate | Allowed Methods | Used By | Effective From | Regulation Reference | Modified By | Last Updated`
4. Verifikasi status checkbox default: Active, Class Code, Class Name, Asset Type, Useful Life (years), Straight Line Rate, Declining Balance Rate, Allowed Methods, Used By, dan Effective From checked dan enabled; Regulation Reference, Modified By, dan Last Updated unchecked dan enabled
5. Verifikasi setiap baris kolom memiliki drag handle
6. Verifikasi item `Setup Column...` ada di bagian bawah panel
7. Tutup Overlay Column Visibility

### Screening Popup Setup Column (TC-FA-TDC-540)

8. Klik icon `⋯` pada header kolom Actions
9. Klik `Setup Column...`
10. Verifikasi Title `Setup Column`
11. Verifikasi Deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
12. Verifikasi tombol Close `(X)` di kanan atas
13. Verifikasi daftar kolom berurutan `Active | Class Code | Class Name | Asset Type | Useful Life (years) | Straight Line Rate | Declining Balance Rate | Allowed Methods | Used By | Effective From | Regulation Reference | Modified By | Last Updated` dengan checkbox, drag handle, dan icon Pin per baris
14. Verifikasi status checkbox default: Active, Class Code, Class Name, Asset Type, Useful Life (years), Straight Line Rate, Declining Balance Rate, Allowed Methods, Used By, dan Effective From checked; Regulation Reference, Modified By, dan Last Updated unchecked
15. Verifikasi Live Preview tabel menampilkan urutan header dan data sel yang sama dengan tabel asli
16. Verifikasi tombol `[Reset to Default]` dan `[Save]` rata kanan pada Footer
17. Verifikasi tidak ada tombol `[Cancel]` pada Footer
18. Klik `(X)` pada Popup Setup Column

### Ceklis dan unceklis di Popup Setup Column: kolom tampil secara default (TC-FA-TDC-541)

Untuk setiap baris tabel parameter TC-FA-TDC-541 pada Prerequisites, lakukan langkah 19 sampai 32.

19. Verifikasi kolom pada baris tabel tampil di tabel
20. Klik icon `⋯` pada header kolom Actions
21. Klik `Setup Column...`
22. Hapus centang checkbox kolom pada baris tabel
23. Verifikasi kolom hilang dari Live Preview
24. Klik `[Save]`
25. Verifikasi kolom hilang dari tabel
26. Refresh halaman (F5)
27. Verifikasi kolom tetap hilang dari tabel setelah F5
28. Klik icon `⋯` pada header kolom Actions
29. Klik `Setup Column...`
30. Centang checkbox kolom pada baris tabel
31. Klik `[Save]`
32. Verifikasi kolom tampil kembali di tabel

## Notes

- Langkah penghubung (S-03): langkah 7 dan 18 (menutup Overlay dan Popup). Langkah 28 sampai 31 pada tiap iterasi (menampilkan kolom kembali) sekaligus pemulihan Setup Column (8b.14, R-24) dan Expected k TC-FA-TDC-541; hook `after` hanya cadangan.
- Perulangan langkah 19 sampai 32 memakai idiom "Untuk setiap baris tabel ... (langkah X sampai Y)" (8b.7); `Verifikasi` yang diulang tetap satu per klausa. TC-FA-TDC-541 menulis langkah 3 untuk tiap kolom, lalu F5 (langkah 4) dan pemulihan (langkah 5) sekali; spec menjalankan F5 dan pemulihan pada tiap iterasi karena menyembunyikan seluruh sepuluh kolom sekaligus mengosongkan tabel (checkbox kolom terakhir Disabled, TC-FA-TDC-549) dan Expected a sampai j menyatakan "tetap hilang setelah F5" per kolom.
- Asersi absence langkah 23, 25, dan 27 didahului anchor positif langkah 19 (kolom yang sama tampil di tabel sebelum disembunyikan; asersi tambahan di luar TC, 8b.2) dan baris Example Data yang tampil pada tabel yang sama.
- Spec ini 32 langkah nominal dan sekitar 158 langkah setelah ekspansi perulangan (10 kolom), di atas ~35 langkah. Alasan: satu topik (Setup Column tabel utama, kolom tampil secara default) pada dataset Example Data yang sama, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan perulangan per kolom mengikuti idiom 8b.7 dengan parameter di Prerequisites; S-01 mengharuskan satu `Verifikasi` per klausa.
- Temuan untuk QA:
  - TC-FA-TDC-541 menyembunyikan seluruh sepuluh kolom default dalam satu langkah berulang tetapi guard TC-FA-TDC-549 melarang menyembunyikan kolom terakhir; spec menyembunyikan dan memulihkan satu kolom per iterasi.
  - TC-FA-TDC-541 tidak menyebut apakah Popup Setup Column menutup sesudah `[Save]`; spec mengasumsikan menutup (langkah berikutnya membuka kembali lewat `⋯`).
  - TC-FA-TDC-539 Expected a ("menempel pada pemicu tanpa backdrop") tanpa langkah observasi spesifik; spec mengasersinya apa adanya.
  - TC-FA-TDC-540 Expected b i menyebut checkbox, drag handle, dan icon Pin per baris; spec mengasersi ketiganya pada satu `Verifikasi` sesuai satu butir Expected TC.
  - Email akun Total Control tidak tertulis di TC.
