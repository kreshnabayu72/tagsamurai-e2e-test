---
id: TC-FA-GRP-E2E-216-tab-assets-filter-asset-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown
title: "Tab Assets Filter Asset Name: Isi Opsi, Satu Opsi (Semua Unit), Dua Opsi OR, dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1004
  - TC-FA-GRP-1005
  - TC-FA-GRP-1006
  - TC-FA-GRP-1007
coverage:
  web: automated
---

# Tab Assets Filter Asset Name: Isi Opsi, Satu Opsi (Semua Unit), Dua Opsi OR, dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Aset acuan di Warehouse A (hanya dibaca): `Laptop Dell - 1`, `Laptop Dell - 2`, `Laptop Dell - 10`, `Monitor LG - 3`; nilai pencarian dropdown `lap` (huruf kecil) dan teks tanpa kecocokan Fixture.settingsGroups.filterTanpaMatch.

## Test Steps

### TC-FA-GRP-1004: Screening isi opsi dropdown Filter Asset Name

1. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
2. Klik icon Filter
3. Verifikasi placeholder field Asset Name `All asset names`
4. Buka dropdown Asset Name
5. Verifikasi opsi adalah nama aset distinct tanpa Increment yang ada di baris tabel
6. Verifikasi opsi `Laptop Dell` muncul satu kali walau ada 3 unit
7. Verifikasi tidak ada opsi berformat `Laptop Dell - 1`
8. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
9. Verifikasi kotak search internal tampil di dalam dropdown

### TC-FA-GRP-1005: Filter Asset Name satu opsi

10. Tutup dropdown Asset Name (langkah penghubung)
11. Pilih `Laptop Dell` pada Asset Name, klik [Apply]
12. Verifikasi `Laptop Dell - 1` tampil
13. Verifikasi `Laptop Dell - 2` tampil
14. Verifikasi `Laptop Dell - 10` tampil
15. Verifikasi `Monitor LG - 3` tidak tampil
16. Verifikasi setiap baris yang tampil bernama aset `Laptop Dell`
17. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-1006: Filter Asset Name dua opsi (OR)

18. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
19. Klik icon Filter, centang `Laptop Dell` dan `Monitor LG` pada Asset Name, klik [Apply]
20. Verifikasi baris bernama aset `Laptop Dell` tampil
21. Verifikasi baris bernama aset `Monitor LG` tampil
22. Verifikasi setiap baris yang tampil bernama aset `Laptop Dell` atau `Monitor LG`

### TC-FA-GRP-1007: Search internal dropdown Filter Asset Name

23. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
24. Klik icon Filter, buka dropdown Asset Name
25. Ketik `lap` di kotak search dropdown
26. Verifikasi opsi `Laptop Dell` tampil
27. Verifikasi setiap opsi yang tampil mengandung substring `lap` (case-insensitive)
28. Ganti isi kotak search dropdown dengan `Fixture.settingsGroups.filterTanpaMatch`
29. Verifikasi daftar opsi kosong dengan teks "No results found"
30. Verifikasi tidak ada ilustrasi pada daftar opsi kosong

## Notes

- Langkah penghubung (S-03): langkah 1 membuka Popup Detail Group Tab Assets; menutup dropdown, [Clear Field], dan [Apply] mengosongkan Filter antar-TC (S-09).
- Spec satu kelas harness dan satu dataset Warehouse A; Expected TC-1005 b ("aset bernama lain tidak tampil") ditulis sebagai `Verifikasi` universal setelah anchor unit `Laptop Dell` tampil.
- Temuan untuk QA:
  - TC-1005: Expected b menyebut `Monitor LG - 3` tidak tampil dan "aset bernama lain" tidak tampil; Verifikasi "setiap baris bernama `Laptop Dell`" mencakup keduanya.
  - TC-1004 sampai TC-1007: nama aset acuan (`Laptop Dell - 1/2/10`, `Monitor LG - 3`) ditulis literal di TC dan harus ada di Warehouse A; Tabel A hanya menyebut 24 aset tanpa daftar nama.
