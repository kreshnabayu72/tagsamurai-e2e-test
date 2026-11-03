---
id: TC-FA-GRP-E2E-002-interaksi-baris-groups-list-klik-baris-row-action-dan-bulk-action-icon
title: "Interaksi Baris Groups List: Klik Area Baris, Ikon dan Urutan Row Action, Ikon dan Severity Bulk Action Delete, Tidak Ada Aksi Activate/Deactivate/Move, dan Nama All Groups Tidak Tersimpan sebagai Row"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-6
  - TC-FA-GRP-943
  - TC-FA-GRP-944
  - TC-FA-GRP-950
  - TC-FA-GRP-951
coverage:
  web: automated
---

# Interaksi Baris Groups List: Klik Area Baris, Ikon dan Urutan Row Action, Ikon dan Severity Bulk Action Delete, Tidak Ada Aksi Activate/Deactivate/Move, dan Nama All Groups Tidak Tersimpan sebagai Row

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9) dengan Head Office, Warehouse A, dan sedikitnya dua baris level 1 lain. Spec ini tidak menjalankan Delete.
- Kemampuan teknis: pointer drag-and-drop pada node sidebar; fixture BE (pembacaan state parent node) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-950: Row action icon, severity, dan urutan menu

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik (⋯) pada baris Warehouse A
3. Verifikasi urutan menu: Detail, Add Subgroup, Edit, Delete
4. Verifikasi ikon Detail `FileInfoLine` dark, Add Subgroup `AddLine` dark, Edit `Edit2Line` dark, Delete `DeleteBin6Line` danger
5. Tutup menu dengan Esc
6. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
7. Klik (⋯) pada node Warehouse A di sidebar
8. Verifikasi menu sidebar identik dengan menu baris tabel (urutan, ikon, dan severity)
9. Tutup menu dengan Esc

### TC-FA-GRP-951: Bulk action Delete

10. Centang 2 baris group
11. Verifikasi Bulk Action Bar menampilkan Delete dengan ikon `DeleteBin6Line` dan severity danger

### TC-FA-GRP-943 (bagian 1): Bulk Action Bar tidak memuat Activate/Deactivate/Move

12. Verifikasi Bulk Action Bar (dua baris tercentang) memuat Delete (anchor)
13. Verifikasi Bulk Action Bar tidak memuat opsi Activate, Deactivate, atau Move
14. Hapus centang dua baris dengan Unselect All

### TC-FA-GRP-943 (bagian 2): Tidak ada Activate/Deactivate/Move pada menu, drag, dan Filter

15. Ketik Search `Warehouse A`, tekan Enter
16. Klik (⋯) pada baris Warehouse A
17. Verifikasi menu baris memuat Detail, Add Subgroup, Edit, Delete (anchor surface menu sudah tampil)
18. Verifikasi menu baris tidak memuat opsi Activate, Deactivate, atau Move
19. Tutup menu dengan Esc
20. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
21. Klik (⋯) pada node Warehouse A di sidebar
22. Verifikasi menu sidebar memuat Detail, Add Subgroup, Edit, Delete (anchor)
23. Verifikasi menu sidebar tidak memuat opsi Activate, Deactivate, atau Move
24. Tutup menu dengan Esc
25. Seret node Warehouse A di sidebar ke node Head Office
26. Verifikasi Warehouse A tidak berpindah di bawah Head Office di sidebar dan parent Warehouse A di fixture BE tidak berubah
27. Klik ikon `Filter`
28. Verifikasi panel Filter terbuka dengan field Function (anchor)
29. Verifikasi panel Filter tidak memuat field Status Active/Inactive
30. Tutup panel Filter dengan Esc

### TC-FA-GRP-6: Klik area baris

31. Ketik Search `Head Office`, tekan Enter
32. Klik area kosong pada baris Head Office (bukan nama, angka, atau (⋯))
33. Verifikasi tidak ada popup atau navigasi yang terbuka
34. Verifikasi tabel tetap tampil dengan baris Head Office
35. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-GRP-944: Nama All Groups bukan row

36. Ketik Search `All Groups`, tekan Enter
37. Verifikasi empty state `No results found` tampil (hasil Search tanpa baris)
38. Verifikasi tidak ada baris bernama `All Groups` pada tabel
39. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Spec melewati sekitar 35 langkah (39 langkah): lima blok TC kecil pada layar dan dataset yang sama (Groups List All Groups), tiap blok berdiri sendiri, dan memisahnya hanya menggandakan login, hook, dan cleanup tanpa alur baru; tambahan langkah Search karena baris target tidak boleh diandalkan berada di halaman 1.
- Langkah penghubung (S-03): langkah 5, 9, 19, 24, 30 (menutup menu/panel), langkah 14 (Unselect All sebelum TC berikutnya, S-09), langkah 25 adalah pemicu drag untuk TC-FA-GRP-943. Langkah 1, 15, dan 31 (Ketik Search `Warehouse A` atau `Head Office`, tekan Enter) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1; langkah 6, 20, 35, dan 39 (`(←)` pada kotak Search) mengembalikan tabel penuh (R-16).
- Urutan TC dalam spec: 950, 951, 943 (bagian 1: Bulk Action Bar), 943 (bagian 2: menu, drag, Filter), 6, 944. Seleksi dua baris dari TC-FA-GRP-951 dipakai ulang TC-FA-GRP-943 untuk Bulk Action lalu dibersihkan (langkah 14) sebelum Search dipakai, sehingga seleksi tidak bergantung pada perilaku Search.
- Temuan untuk QA:
  - TC-FA-GRP-943 langkah 3 ("coba drag node") tidak menyebut node asal/tujuan; spec memakai Warehouse A ke Head Office.
  - TC-FA-GRP-944 tidak menyebut cara cek tabel "tidak ada baris"; spec memakai Search sehingga empty state `No results found` menjadi anchor positif (8b butir 2).
  - TC-FA-GRP-951 tidak menyebut baris mana yang dicentang; spec memakai dua baris level 1 pertama.
