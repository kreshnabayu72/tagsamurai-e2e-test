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

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
3. Telusuri semua halaman tabel dari halaman 1 sampai halaman terakhir, lalu catat himpunan nama aset distinct tanpa Increment pada baris tabel
4. Klik icon Filter
5. Verifikasi placeholder field Asset Name `All asset names`
6. Buka dropdown Asset Name
7. Verifikasi opsi = himpunan nama aset distinct tanpa Increment yang dicatat pada langkah 3
8. Verifikasi opsi `Laptop Dell` muncul satu kali walau ada 3 unit
9. Verifikasi tidak ada opsi berformat `Laptop Dell - 1`
10. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
11. Verifikasi kotak search internal tampil di dalam dropdown

### TC-FA-GRP-1005: Filter Asset Name satu opsi

12. Tutup dropdown Asset Name (langkah penghubung)
13. Pilih `Laptop Dell` pada Asset Name, klik [Apply]
14. Verifikasi `Laptop Dell - 1` tampil
15. Verifikasi `Laptop Dell - 2` tampil
16. Verifikasi `Laptop Dell - 10` tampil
17. Verifikasi `Monitor LG - 3` tidak tampil
18. Verifikasi setiap baris yang tampil bernama aset `Laptop Dell`
19. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-1006: Filter Asset Name dua opsi (OR)

20. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
21. Klik icon Filter, centang `Laptop Dell` dan `Monitor LG` pada Asset Name, klik [Apply]
22. Verifikasi baris bernama aset `Laptop Dell` tampil
23. Verifikasi baris bernama aset `Monitor LG` tampil
24. Verifikasi setiap baris yang tampil bernama aset `Laptop Dell` atau `Monitor LG`

### TC-FA-GRP-1007: Search internal dropdown Filter Asset Name

25. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
26. Klik icon Filter, buka dropdown Asset Name
27. Ketik `lap` di kotak search dropdown
28. Verifikasi opsi `Laptop Dell` tampil
29. Verifikasi setiap opsi yang tampil mengandung substring `lap` (case-insensitive)
30. Ganti isi kotak search dropdown dengan `Fixture.settingsGroups.filterTanpaMatch`
31. Verifikasi daftar opsi kosong dengan teks "No results found"
32. Verifikasi tidak ada ilustrasi pada daftar opsi kosong

## Notes

- Langkah penghubung (S-03): langkah 2 membuka Popup Detail Group Tab Assets; menutup dropdown, [Clear Field], dan [Apply] mengosongkan Filter antar-TC (S-09).
- Spec satu kelas harness dan satu dataset Warehouse A; Expected TC-1005 b ("aset bernama lain tidak tampil") ditulis sebagai `Verifikasi` universal setelah anchor unit `Laptop Dell` tampil.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Himpunan nama aset distinct dicatat dengan menelusuri seluruh halaman tabel sebelum Filter Panel dibuka (langkah 3), karena Warehouse A memuat 24 aset aktif dengan page size 10 sehingga halaman 1 saja tidak mewakili himpunan (S-11, S-14).
- Temuan untuk QA:
  - TC-1005: Expected b menyebut `Monitor LG - 3` tidak tampil dan "aset bernama lain" tidak tampil; Verifikasi "setiap baris bernama `Laptop Dell`" mencakup keduanya.
  - TC-1004 sampai TC-1007: nama aset acuan (`Laptop Dell - 1/2/10`, `Monitor LG - 3`) ditulis literal di TC dan harus ada di Warehouse A; Tabel A hanya menyebut 24 aset tanpa daftar nama.
