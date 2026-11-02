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

1. Klik (⋯) pada baris Warehouse A
2. Verifikasi urutan menu: Detail, Add Subgroup, Edit, Delete
3. Verifikasi ikon Detail `FileInfoLine` dark, Add Subgroup `AddLine` dark, Edit `Edit2Line` dark, Delete `DeleteBin6Line` danger
4. Tutup menu dengan Esc
5. Klik (⋯) pada node Warehouse A di sidebar
6. Verifikasi menu sidebar identik dengan menu baris tabel (urutan, ikon, dan severity)
7. Tutup menu dengan Esc

### TC-FA-GRP-951: Bulk action Delete

8. Centang 2 baris group
9. Verifikasi Bulk Action Bar menampilkan Delete dengan ikon `DeleteBin6Line` dan severity danger

### TC-FA-GRP-943: Tidak ada Activate/Deactivate/Move

10. Klik (⋯) pada baris Warehouse A
11. Verifikasi menu baris memuat Detail, Add Subgroup, Edit, Delete (anchor surface menu sudah tampil)
12. Verifikasi menu baris tidak memuat opsi Activate, Deactivate, atau Move
13. Tutup menu dengan Esc
14. Klik (⋯) pada node Warehouse A di sidebar
15. Verifikasi menu sidebar memuat Detail, Add Subgroup, Edit, Delete (anchor)
16. Verifikasi menu sidebar tidak memuat opsi Activate, Deactivate, atau Move
17. Tutup menu dengan Esc
18. Verifikasi Bulk Action Bar (dua baris masih tercentang) memuat Delete (anchor)
19. Verifikasi Bulk Action Bar tidak memuat opsi Activate, Deactivate, atau Move
20. Seret node Warehouse A di sidebar ke node Head Office
21. Verifikasi Warehouse A tidak berpindah di bawah Head Office di sidebar dan parent Warehouse A di fixture BE tidak berubah
22. Klik ikon `Filter`
23. Verifikasi panel Filter terbuka dengan field Function (anchor)
24. Verifikasi panel Filter tidak memuat field Status Active/Inactive
25. Tutup panel Filter dengan Esc
26. Hapus centang dua baris dengan Unselect All

### TC-FA-GRP-6: Klik area baris

27. Klik area kosong pada baris Head Office (bukan nama, angka, atau (⋯))
28. Verifikasi tidak ada popup atau navigasi yang terbuka
29. Verifikasi tabel tetap tampil dengan baris Head Office

### TC-FA-GRP-944: Nama All Groups bukan row

30. Ketik Search `All Groups`, tekan Enter
31. Verifikasi empty state `No results found` tampil (hasil Search tanpa baris)
32. Verifikasi tidak ada baris bernama `All Groups` pada tabel
33. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 4, 7, 13, 17, 25 (menutup menu/panel), langkah 26 (Unselect All sebelum TC berikutnya, S-09), langkah 33 (reset Search). Langkah 20 adalah pemicu drag untuk TC-FA-GRP-943.
- Urutan TC dalam spec: 950, 951, 943, 6, 944. Seleksi dua baris dari TC-FA-GRP-951 dipakai ulang TC-FA-GRP-943 untuk Bulk Action lalu dibersihkan (langkah 26).
- Temuan untuk QA:
  - TC-FA-GRP-943 langkah 3 ("coba drag node") tidak menyebut node asal/tujuan; spec memakai Warehouse A ke Head Office.
  - TC-FA-GRP-944 tidak menyebut cara cek tabel "tidak ada baris"; spec memakai Search sehingga empty state `No results found` menjadi anchor positif (8b butir 2).
  - TC-FA-GRP-951 tidak menyebut baris mana yang dicentang; spec memakai dua baris level 1 pertama.
