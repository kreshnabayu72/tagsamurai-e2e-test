---
id: TC-FA-FAAC-E2E-013-banner-asset-name-tanpa-asset-class-dan-dialog-d23
title: "Banner Asset Name Tanpa Asset Class (0, 3, dan 1 Asset Name) serta Screening dan Penutupan Dialog Asset Names Without Asset Class"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-33
  - TC-FA-FAAC-35
  - TC-FA-FAAC-270
  - TC-FA-FAAC-271
  - TC-FA-FAAC-272
  - TC-FA-FAAC-34
sourceRules: ["§4.1#r2", "F-FAAC-13.k1", "§4.1.1#p3", "F-FAAC-13.k2", "§4.2g#p1", "§4.1.9#p1", "E-FAAC-108", "§4.1.9#r1", "§4.1.9#r2", "§4.1.9#r3", "F-FAAC-13.k3", "§4.1.9#r4", "§4.1.9#r5", "§4.1.9#r6", "§4.1.9#b1"]
smoke: []
dependsOn: []
trace:
  "§4.1#r2": 1
  "F-FAAC-13.k1": [2, 3]
  "§4.1.1#p3": [7, 33, 35]
  "F-FAAC-13.k2": [8, 25, 34]
  "§4.2g#p1": [10, 20]
  "§4.1.9#p1": [10, 12, 13, 21, 23, 28]
  "E-FAAC-108": 11
  "§4.1.9#r1": [13, 14, 15]
  "§4.1.9#r2": [13, 16, 18]
  "§4.1.9#r3": 13
  "F-FAAC-13.k3": [14, 19]
  "§4.1.9#r4": 14
  "§4.1.9#r5": 14
  "§4.1.9#r6": 14
  "§4.1.9#b1": 20
anchor: [24, 29]
coverage:
  web: automated
---

# Banner Asset Name Tanpa Asset Class (0, 3, dan 1 Asset Name) serta Screening dan Penutupan Dialog Asset Names Without Asset Class

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state global, keanggotaan Asset Name tanpa Asset Class): keadaan awal yang disiapkan hook `before` lewat fixture BE adalah semua Asset Name company sudah ter-assign ke Asset Class (jumlah tanpa Asset Class 0). Blok berikutnya mengatur keanggotaan lewat fixture BE: tepat tiga Asset Name tanpa Asset Class dengan data Forklift 3T (Machinery > Warehouse; 6 aset aktif), Laptop Standard (IT > Devices; 120 aset aktif), Crane Rental Unit (Machinery > Rented; 0 aset aktif) (TC-FA-FAAC-35, 270, 271, 272), lalu tepat satu Asset Name tanpa Asset Class: `Crane Rental Unit` (TC-FA-FAAC-34). Hook `after` memulihkan keanggotaan ke keadaan awal run.
- Kemampuan teknis: fixture BE untuk mengatur dan memulihkan keanggotaan Asset Name tanpa Asset Class; disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah keanggotaan Asset Name tanpa Asset Class yang dipakai bersama.

## Test Steps

### TC-FA-FAAC-33: Banner tidak tampil bila semua Asset Name sudah ter-assign

1. Verifikasi tabel Asset Class tampil
2. Verifikasi banner Alert warning `asset name has no asset class` Hidden
3. Verifikasi tidak ada link `[View asset names]`

### TC-FA-FAAC-35: Banner menampilkan teks bentuk jamak untuk 3 Asset Name

4. Atur Asset Name tanpa Asset Class menjadi tepat tiga (`Forklift 3T`, `Laptop Standard`, `Crane Rental Unit`) lewat fixture BE hingga tersimpan
5. Refresh halaman
6. Klik tab Asset Class
7. Verifikasi banner Alert warning tampil dengan teks `3 asset names have no asset class and will not be depreciated.`
8. Verifikasi banner memuat link `[View asset names]`

### TC-FA-FAAC-270: Screening dialog Asset Names Without Asset Class

9. Klik link `[View asset names]` pada banner
10. Verifikasi dialog ukuran MD berjudul `Asset Names Without Asset Class` dengan ikon `[✕]`
11. Verifikasi halaman tidak berpindah (tab `Asset Class` tetap aktif)
12. Verifikasi deskripsi di atas tabel `These asset names are not depreciated until they are assigned to an asset class.`
13. Verifikasi tabel read-only dengan kolom Asset Name, Category, Assets
14. Verifikasi baris terurut Asset Name A-Z: Crane Rental Unit (0), Forklift 3T (6), Laptop Standard (120)
15. Verifikasi Asset Name tampil sebagai teks biasa (bukan link)
16. Verifikasi Category tampil sebagai badge leaf (`Rented`, `Warehouse`, `Devices`)
17. Arahkan kursor ke badge Category baris Laptop Standard
18. Verifikasi hover badge menampilkan `IT > Devices`
19. Verifikasi Search tersedia
20. Verifikasi tidak ada Filter, kolom checkbox, row action, maupun bulk action
21. Verifikasi footer hanya berisi tombol `[Close]` tanpa `[Cancel]`

### TC-FA-FAAC-271: Menutup dialog D-23 dengan tombol Close tanpa konfirmasi

22. Klik `[Close]`
23. Verifikasi dialog menutup tanpa konfirmasi
24. Verifikasi tidak ada toast
25. Verifikasi tab `Asset Class` tetap tampil dengan banner

### TC-FA-FAAC-272: Menutup dialog D-23 dengan ikon ✕ tanpa konfirmasi

26. Klik link `[View asset names]` pada banner
27. Klik ikon `[✕]`
28. Verifikasi dialog menutup tanpa konfirmasi
29. Verifikasi tidak ada toast

### TC-FA-FAAC-34: Banner menampilkan teks bentuk tunggal untuk 1 Asset Name

30. Atur Asset Name tanpa Asset Class menjadi tepat satu (`Crane Rental Unit`) lewat fixture BE hingga tersimpan
31. Refresh halaman
32. Klik tab Asset Class
33. Verifikasi banner Alert warning tampil dengan teks `1 asset name has no asset class and will not be depreciated.`
34. Verifikasi banner memuat link `[View asset names]`
35. Verifikasi banner tidak memiliki tombol tutup `✕`

## Notes

- Langkah penghubung (S-03): langkah 4 dan 30 (mengatur keanggotaan Asset Name tanpa Asset Class lewat fixture BE sebagai precondition tiap blok), langkah 5 dan 6, 31 dan 32 (memuat ulang tab agar banner dihitung ulang; TC-FA-FAAC-33, 35, dan 34 langkah 1 berbunyi "Buka (muat ulang) tab Asset Class"; blok pertama memakai tab yang dibuka hook `beforeEach`).
- Urutan TC dalam spec: 33, 35, 270, 271, 272, 34. TC-FA-FAAC-271 langkah 1 (membuka dialog) dipenuhi dialog yang masih terbuka dari TC-FA-FAAC-270 (jumlah buka dialog tidak lebih dari jumlah menutup, S-10); TC-FA-FAAC-272 membuka dialog lagi.
- Anchor absence: langkah 1 (tabel tampil) mendahului absence banner pada langkah 2 dan 3 (8b butir 2). Langkah 24 dan 29 (absence toast) didahului penutupan dialog pada langkah 23 dan 28 sebagai anchor positif (8b butir 11).
- Nama literal Asset Name dan Asset Class Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan urutan persis dan keanggotaan dipulihkan fixture BE (S-06, S-12).
- Temuan untuk QA:
  - TC-FA-FAAC-35 menyebut tiga Asset Name tanpa menyebut kategori dan jumlah aset; spec memakai data dari precondition TC-FA-FAAC-270.
