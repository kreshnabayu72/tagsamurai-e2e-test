---
id: TC-GS-BRAND-E2E-058-detail-device-sku-list-search-filter-sort
title: "Brand Detail Principal: Search, Filter Category, dan Sort Accordion Device SKU List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-196
  - TC-GS-BRAND-260
  - TC-GS-BRAND-251
  - TC-GS-BRAND-255
coverage:
  web: automated
---

# Brand Detail Principal: Search, Filter Category, dan Sort Accordion Device SKU List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), Hendra Wijaya, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 8), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Login di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_PRINCIPAL_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Principal (tetap di environment, hanya dibaca, tanpa suffix `{runId}`): brand `Signal One` dengan tiga Device SKU: `SKU-HR-001` (Device Name `Handheld Reader A1`, Category `Handheld Reader`), `SKU-TB-002` (`Tablet T10`, `Tablet`), `SKU-GW-003` (`BLE Gateway G2`, `BLE Gateway`).
- Spec tidak membuat atau mengubah data, sehingga tidak ada seeding dan cleanup. Tidak ada state global yang diubah.
- TC-GS-BRAND-196, 260, 251, 255: login sebagai Total Control (Principal) dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-255: Isi opsi Filter Category accordion Device SKU List

1. Search `Signal One` pada tabel Brand, klik `⋯` pada baris Signal One > Detail → modal Brand Detail tampil
2. Expand accordion Device SKU List
3. Klik Filter
4. Buka dropdown Category
5. Verifikasi dropdown Category berplaceholder `All categories`
6. Verifikasi opsi dropdown Category: BLE Gateway, Handheld Reader, Tablet
7. Tutup dropdown Category tanpa memilih opsi

### TC-GS-BRAND-196: Search dan Filter accordion Device SKU List

8. Verifikasi placeholder Search `Search SKU code, device name, or category...` (kolom Search masih kosong)
9. Search `tablet`
10. Verifikasi hasil Search `tablet`: SKU-TB-002
11. Kosongkan Search
12. Klik Filter, pilih Category `Handheld Reader`, klik [Apply]
13. Verifikasi hasil Filter Category Handheld Reader: SKU-HR-001
14. Hapus filter Category `Handheld Reader` sehingga ketiga SKU tampil kembali

### TC-GS-BRAND-260: Search accordion Device SKU List pada SKU Code

15. Search `gw-0`
16. Verifikasi hanya SKU-GW-003 yang tampil
17. Kosongkan Search, lalu Search `hr-001`
18. Verifikasi hanya SKU-HR-001 yang tampil (tidak membedakan huruf besar kecil)
19. Kosongkan Search

### TC-GS-BRAND-251: Sort accordion Device SKU List: SKU Code, Device Name, Category

20. Klik header SKU Code
21. Verifikasi urutan SKU Code klik 1: SKU-GW-003, SKU-HR-001, SKU-TB-002
22. Klik header SKU Code sekali lagi
23. Verifikasi urutan SKU Code klik 2: SKU-TB-002, SKU-HR-001, SKU-GW-003
24. Klik header Device Name dua kali
25. Verifikasi urutan Device Name klik 2: Tablet T10, Handheld Reader A1, BLE Gateway G2
26. Klik header Category dua kali
27. Verifikasi urutan Category klik 2 (menurut label badge): Tablet, Handheld Reader, BLE Gateway
28. Klik header Category sekali lagi
29. Verifikasi klik ke-3 pada Category mengembalikan urutan default SKU A-Z
30. Verifikasi tidak ada indikator sort aktif

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan sumber: isi dropdown Filter (255) lebih dulu karena tidak mengubah tampilan tabel; Search dan Filter (196) berikutnya dengan placeholder dicek saat kolom Search masih kosong; lalu Search SKU Code (260); Sort (251) terakhir setelah Search dan Filter dibersihkan supaya Sort memakai ketiga SKU (prinsip 3 konvensi).
- Langkah penghubung: langkah 1 (membuka Detail lewat Search `Signal One`), langkah 7 (menutup dropdown Category tanpa memilih opsi), langkah 14 (membersihkan filter Category), dan langkah 19 (mengosongkan Search) tidak tertulis di Langkah Uji TC sumber; tujuannya menyiapkan atau mengembalikan state antar TC.
- TC-GS-BRAND-196 Langkah Uji 1 menyebut "expand Device SKU" sedangkan TC lain menyebut "Device SKU List"; spec memakai nama accordion `Device SKU List`.
