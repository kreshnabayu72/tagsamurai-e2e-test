---
id: TC-FA-GRP-E2E-032-popup-detail-group-state-search-filter-sort-paginasi-per-tab-dipulihkan-dan-direset
title: "Popup Detail Group: State Search/Filter/Sort/Paginasi per Tab Dipulihkan Saat Kembali ke Tab, Tidak Memengaruhi Tab Lain, dan Direset Saat Popup Ditutup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1052
  - TC-FA-GRP-1053
  - TC-FA-GRP-1054
coverage:
  web: automated
---

# Popup Detail Group: State Search/Filter/Sort/Paginasi per Tab Dipulihkan Saat Kembali ke Tab, Tidak Memengaruhi Tab Lain, dan Direset Saat Popup Ditutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9) dengan Warehouse A: 24 aset aktif dengan sedikitnya 11 unit bernama `Laptop Dell` (sedikitnya dua nilai Asset Name distinct), serta sedikitnya 12 user ber-Position `Warehouse Staff` dengan email berdomain `qwertysystem.net` (sedikitnya dua nilai Position distinct). Ukuran halaman 10 baris per halaman (default). Komposisi ini diverifikasi lewat fixture BE sebelum spec berjalan (lihat Temuan untuk QA). Spec ini tidak menjalankan aksi tulis.
- Kemampuan teknis: fixture BE (pembacaan komposisi aset dan user Warehouse A) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-1052: State tiap tab dipulihkan saat kembali ke tab

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik nama Warehouse A
3. Ketik Search `Laptop`, tekan Enter pada Tab Assets
4. Klik ikon `Filter`
5. Pilih Asset Name `Laptop Dell`
6. Klik [Apply]
7. Klik header kolom Name (sort Name Z–A dari default A–Z)
8. Klik halaman 2 pada pagination
9. Klik Tab Users
10. Ketik Search `qwertysystem`, tekan Enter pada Tab Users
11. Klik ikon `Filter`
12. Pilih Position `Warehouse Staff`
13. Klik [Apply]
14. Klik header kolom Name (sort Name Z–A dari default A–Z)
15. Klik halaman 2 pada pagination
16. Klik Tab Assets
17. Verifikasi Tab Assets menampilkan kembali Search `Laptop`, Filter Asset Name `Laptop Dell`, sort Name Z–A, dan halaman 2
18. Verifikasi indikator filter aktif tetap tampil pada ikon `Filter` Tab Assets
19. Klik Tab Users
20. Verifikasi Tab Users menampilkan kembali Search `qwertysystem`, Filter Position `Warehouse Staff`, sort Name Z–A, dan halaman 2
21. Verifikasi indikator filter aktif tetap tampil pada ikon `Filter` Tab Users

### TC-FA-GRP-1054: Menutup popup mereset state seluruh tab

22. Klik [X]
23. Klik nama Warehouse A
24. Verifikasi popup terbuka pada Tab Assets dengan state awal: Search kosong, tanpa filter aktif, sort default Name A–Z, halaman 1
25. Klik Tab Users
26. Verifikasi Tab Users memakai state awal: Search kosong, tanpa filter aktif, sort default Name A–Z, halaman 1

### TC-FA-GRP-1053: State satu tab tidak memengaruhi tab lain

27. Klik Tab Assets
28. Ketik Search `Laptop`, tekan Enter pada Tab Assets
29. Klik header kolom Name (sort Name Z–A dari default A–Z)
30. Klik Tab Users
31. Verifikasi Tab Users tampil dengan state awal sendiri: Search kosong, tanpa filter aktif, sort default Name A–Z, halaman 1
32. Verifikasi Search dan sort Tab Assets tidak terbawa ke Tab Users
33. Klik [X]

## Notes

- Spec 33 langkah, di bawah batas sekitar 35 langkah.
- Urutan TC dalam spec: 1052, 1054, 1053. State dua tab yang dibentuk langkah 2 sampai 15 (TC-FA-GRP-1052) juga menjadi precondition TC-FA-GRP-1054 (state yang ditutup); sort Name Z–A yang ikut terbentuk adalah state tambahan yang tetap tercakup oleh Expected "state awal" (S-04: langkah precondition TC-FA-GRP-1054 disalin utuh oleh langkah 2 sampai 15). TC-FA-GRP-1053 terakhir karena memakai popup yang baru dibuka dengan state awal.
- Langkah penghubung (S-03): langkah 22 (menutup popup), langkah 27 (kembali ke Tab Assets sebagai persiapan TC-FA-GRP-1053), langkah 33 (menutup popup). Langkah 1 (Ketik Search `Warehouse A` pada tabel Groups List, tekan Enter) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1; Search tabel tetap aktif untuk membuka popup lagi pada langkah 23 dan tidak sama dengan Search tab di dalam popup (R-16).
- Temuan untuk QA:
  - TC-FA-GRP-1052 dan 1054 menyebut komposisi Warehouse A (sedikitnya 11 unit Laptop Dell, sedikitnya 12 user Warehouse Staff) yang tidak tercantum pada Tabel A; spec membaca komposisi lewat fixture BE.
  - TC-FA-GRP-1052 menyebut "sort Name Z–A" tanpa jumlah klik; spec mengklik header Name satu kali dari default A–Z.
  - TC-FA-GRP-1054 tidak menyebut sort pada langkah pembentukan state; langkah 7 dan 14 ikut dikerjakan sebagai bagian dari TC-FA-GRP-1052 dan tidak mengubah Expected TC-FA-GRP-1054.
