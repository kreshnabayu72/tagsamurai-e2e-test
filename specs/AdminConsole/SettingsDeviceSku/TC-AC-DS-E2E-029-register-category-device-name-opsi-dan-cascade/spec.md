---
id: TC-AC-DS-E2E-029-register-category-device-name-opsi-dan-cascade
title: "Register SKU: Opsi Device Name Mengikuti Category, Pilih Device Name Mengisi Category, dan No options available"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-94
  - TC-AC-DS-95
  - TC-AC-DS-96
  - TC-AC-DS-97
  - TC-AC-DS-594
coverage:
  web: automated
---

# Register SKU: Opsi Device Name Mengikuti Category, Pilih Device Name Mengisi Category, dan No options available

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25, Device Name #26 (14 Device Name Principal), Brand #27 (`Veltrix`), file foto #37, SKU inti #29 dan seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada). Spec ini tidak menyimpan SKU: popup Register SKU ditutup lewat `[✕]` dan `[Leave]`.
- Data khusus disiapkan lewat fixture BE pada langkah 6 (bukan di hook `before`, supaya TC-94 mengasersi daftar 14 Device Name tanpa Device Name tambahan) dan dihapus oleh hook `after` lewat fixture BE yang disediakan tim BE/FE; seeding idempotent (dilewati bila sudah ada) dan cleanup hanya menghapus yang dibuat spec ini:
  - Hierarki mendalam Pre-setup #42: Subcategory `UHF Handheld Gudang` (tingkat ke-4) dan `UHF Handheld Lapangan` (tingkat ke-4, tanpa Device Name dan tanpa SKU) di bawah `UHF Handheld`; Device Name `Pemindai Gudang` (Category `UHF Handheld Gudang`); SKU `HHR-GDG-01` dan `HHR-PRT-01` (Device Name `Pemindai Ujung`) sesuai Pre-setup #42.
  - Data khusus Pre-setup #40: Subcategory `Kategori Sementara` (di bawah `Asset TAG`, tanpa Device Name).
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini mengubah data Category dan SKU bersama (#42 dan #40) sehingga pemulihannya dijamin hook `after`.

## Test Steps

### TC-AC-DS-94: Opsi Device Name tanpa Category terpilih

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Device Name
3. Verifikasi daftar opsi memuat seluruh Device Name Principal: `4-Port Fixed Reader`, `anggur sensor`, `Apel sensor`, `Asset TAG`, `BLE Gateway`, `Gerbang Bantu`, `Industrial Handheld Reader`, `Pemindai Ujung`, `Rugged Handheld Reader`, `Seed Tag`, `Tunnel Scanner`, `UHF Handheld Reader`, `UHF Handheld Reader Pro`, `Wearable TAG`
4. Verifikasi field Category belum berubah dan masih menampilkan placeholder "Select category"
5. Klik ikon close `[✕]`

### Persiapan data hierarki mendalam dan data khusus

6. Siapkan data hierarki mendalam Pre-setup #42 dan Subcategory `Kategori Sementara` Pre-setup #40 lewat fixture BE hingga data tersimpan
7. Muat ulang halaman `Settings > Device > Device SKU`

### TC-AC-DS-95: Category induk memfilter opsi Device Name

8. Klik tombol `[+ SKU]` pada toolbar
9. Klik field Category
10. Expand node `Hardware`
11. Klik node `Handheld Reader`
12. Klik `[Select]`
13. Klik field Device Name
14. Verifikasi opsi Device Name hanya `Industrial Handheld Reader`, `Pemindai Gudang`, `Pemindai Ujung`, `Rugged Handheld Reader`, `UHF Handheld Reader`, dan `UHF Handheld Reader Pro`
15. Verifikasi Device Name berkategori `Portal Reader`, `BLE Gateway`, dan TAG (`4-Port Fixed Reader`, `BLE Gateway`, `Asset TAG`) tidak tampil

### TC-AC-DS-96: Category daun memfilter opsi Device Name

16. Klik `[Clear Field]`
17. Klik field Category
18. Expand node `Hardware` lalu `Smart Fixed Reader`
19. Klik node `Portal Reader`
20. Klik `[Select]`
21. Klik field Device Name
22. Verifikasi opsi Device Name hanya `4-Port Fixed Reader`

### TC-AC-DS-97: Memilih Device Name lebih dulu mengisi Category

23. Klik `[Clear Field]`
24. Klik field Brand
25. Pilih Brand `Veltrix`
26. Ketik `SF-9` pada field Model/Type
27. Klik field Device Name
28. Pilih Device Name `Wearable TAG`
29. Verifikasi field Category terisi `Wearable TAG`
30. Verifikasi section checkbox `This is User TAG` muncul
31. Verifikasi field Brand tetap `Veltrix`
32. Verifikasi field Model/Type tetap `SF-9`

### TC-AC-DS-594: Category tanpa Device Name

33. Klik `[Clear Field]`
34. Klik field Category
35. Expand node `TAG`, `NFC`, lalu `Asset TAG`
36. Klik node `Kategori Sementara`
37. Klik `[Select]`
38. Klik field Device Name
39. Verifikasi dropdown Device Name menampilkan teks "No options available"
40. Verifikasi popup Register SKU tetap terbuka
41. Verifikasi field Category tetap menampilkan `Kategori Sementara`
42. Klik ikon close `[✕]`
43. Verifikasi dialog `Unsaved Changes` tampil
44. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-94, persiapan data, TC-95, TC-96, TC-97, TC-594. TC-94 diletakkan pertama karena mengasersi daftar 14 Device Name tanpa Device Name `Pemindai Gudang` dari data #42 (S-10). TC-95 sampai TC-594 memakai satu pembukaan popup Register SKU; popup ditutup di langkah 42 sampai 44 (S-08).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 2, 5 (membuka dan menutup popup serta dropdown untuk TC-94), 6 dan 7 (seeding dan memuat ulang), 8 sampai 13, 17 sampai 21, 24 sampai 28, 34 sampai 38 (membuka popup, picker, dropdown, dan memilih node atau nilai; hasilnya diasersi pada langkah berikutnya), 16, 23, 33 (`[Clear Field]` mengosongkan field sebelum TC berikutnya mengandalkannya, S-09).
- Asersi absence langkah 15 didahului langkah 14 (opsi lain tampil pada dropdown yang sama sebagai anchor).
- Spec melewati sekitar 35 langkah (44 langkah). Alasan pertahanan: seluruh blok memeriksa opsi Device Name dan cascade Category-Device Name pada satu popup Register SKU dalam satu kelas (fungsional form Register, tanpa menyimpan SKU); popup hanya dibuka dua kali (sebelum dan sesudah seeding) dan data hierarki dipakai bersama TC-95 sampai TC-594; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #25/#26/#40/#42 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan). Seeding #42 dan #40 memakai nama literal (idempotent, serial) sampai ada keputusan.
  - Fixture rancangan: ketersediaan Pre-setup #25/#26/#40/#42 di environment belum diverifikasi.
  - TC-94 menyebut 14 Device Name Principal (tanpa `Pemindai Gudang`), sedangkan TC-95 menyebut `Pemindai Gudang` dari data #42; spec memisahkan kedua keadaan dengan seeding di tengah spec.
  - TC-594 menulis `Kategori Sementara` sebagai Subcategory buatan dari `Asset TAG` yang "dihapus sesi kedua" pada Pre-setup #40 untuk TC lain; spec hanya memakai keberadaan Subcategory tanpa Device Name.
  - TC-97 langkah 3 dan 4 mengisi Brand dan Model/Type sebelum Device Name; spec mengikuti TC dan mengosongkan form dengan `[Clear Field]` sebelumnya.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
