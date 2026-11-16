---
id: TC-FA-FAAC-E2E-014-dialog-d23-search-dan-sort
title: "Dialog Asset Names Without Asset Class: Search Hanya Mencocokkan Asset Name dan Siklus Sort Tiga Tahap Tiap Kolom"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-273
  - TC-FA-FAAC-274
  - TC-FA-FAAC-275
  - TC-FA-FAAC-276
  - TC-FA-FAAC-277
sourceRules: ["F-FAAC-13.k3", "§4.1.9#b1", "§4.4#r14", "§4.1.9#r1", "§4.1.9#r2", "§4.1.9#r3"]
smoke: []
dependsOn: []
trace:
  "F-FAAC-13.k3": [3, 15, 22, 29]
  "§4.1.9#b1": [4, 7]
  "§4.4#r14": [10, 12, 14, 17, 19, 21, 24, 26, 28]
  "§4.1.9#r1": [10, 15, 22, 29]
  "§4.1.9#r2": 17
  "§4.1.9#r3": [24, 26]
coverage:
  web: automated
---

# Dialog Asset Names Without Asset Class: Search Hanya Mencocokkan Asset Name dan Siklus Sort Tiga Tahap Tiap Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state global, keanggotaan Asset Name tanpa Asset Class): hook `before` mengatur lewat fixture BE tepat tiga Asset Name tanpa Asset Class: Forklift 3T (Machinery > Warehouse; 6 aset aktif), Laptop Standard (IT > Devices; 120 aset aktif), Crane Rental Unit (Machinery > Rented; 0 aset aktif). Hook `after` memulihkan keanggotaan ke keadaan awal run. Seed disediakan tim FE/BE (lihat `suite.md`).
- Spec ini hanya membaca; tidak ada data yang dibuat atau diubah.
- Suite berjalan serial (`parallel: false`) karena spec ini bergantung pada keanggotaan Asset Name tanpa Asset Class yang dipakai bersama.

## Test Steps

### TC-FA-FAAC-273: Search dialog mencocokkan Asset Name

1. Klik link `[View asset names]` pada banner
2. Ketik Search `lap`, tekan Enter
3. Verifikasi tabel memuat `Laptop Standard`
4. Verifikasi tabel tidak memuat `Forklift 3T` dan `Crane Rental Unit`

### TC-FA-FAAC-274: Search dialog tidak mencocokkan Category

5. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
6. Ketik Search `Devices`, tekan Enter
7. Verifikasi EmptyState `No results found` dengan deskripsi `Try adjusting your search or filter.`
8. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-FAAC-275: Sort kolom Asset Name mengikuti siklus tiga tahap

9. Klik header `Asset Name` sekali
10. Verifikasi urutan A-Z: Crane Rental Unit, Forklift 3T, Laptop Standard
11. Klik header `Asset Name` sekali lagi
12. Verifikasi urutan Z-A: Laptop Standard, Forklift 3T, Crane Rental Unit
13. Klik header `Asset Name` sekali lagi
14. Verifikasi indikator sort netral
15. Verifikasi urutan kembali ke default Asset Name A-Z

### TC-FA-FAAC-276: Sort kolom Category mengikuti siklus tiga tahap

16. Klik header `Category` sekali
17. Verifikasi urutan A-Z menurut leaf Category: Devices (Laptop Standard), Rented (Crane Rental Unit), Warehouse (Forklift 3T)
18. Klik header `Category` sekali lagi
19. Verifikasi urutan Z-A: Warehouse, Rented, Devices
20. Klik header `Category` sekali lagi
21. Verifikasi indikator sort netral
22. Verifikasi urutan kembali ke default Asset Name A-Z

### TC-FA-FAAC-277: Sort kolom Assets mengikuti siklus tiga tahap

23. Klik header `Assets` sekali
24. Verifikasi urutan numerik naik: Crane Rental Unit (0), Forklift 3T (6), Laptop Standard (120)
25. Klik header `Assets` sekali lagi
26. Verifikasi urutan numerik turun: Laptop Standard, Forklift 3T, Crane Rental Unit
27. Klik header `Assets` sekali lagi
28. Verifikasi indikator sort netral
29. Verifikasi urutan kembali ke default Asset Name A-Z
30. Klik `[Close]` untuk menutup dialog

## Notes

- Langkah penghubung (S-03): langkah 5 dan 8 (mengosongkan Search dan mereset tabel, S-09; R-16), langkah 30 (menutup dialog sebelum spec berakhir).
- Dialog dibuka satu kali (langkah 1) dan dipakai untuk kelima TC karena semuanya hanya membaca dengan dataset yang sama (prinsip halaman yang sama dipakai berulang, bagian 3).
- Asersi "hanya" pada langkah 3 dan 4 didahului langkah 1 yang membuka dialog dengan tiga baris sebagai pembanding (8b butir 2); langkah 3 membuktikan baris target tampil sebelum langkah 4 mengasersi absensi baris lain.
- Temuan untuk QA:
  - TC-FA-FAAC-275 sampai TC-FA-FAAC-277 langkah 2 ("catat urutan") tidak menyebut cara membaca indikator sort netral; spec mengasersi indikator netral lalu urutan default.
