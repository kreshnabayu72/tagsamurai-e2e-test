---
id: TC-FA-GRP-E2E-179-tab-users-setup-column-batas-max-visible-columns-reset-esc-dan-cache
title: "Tab Users Setup Column: Batas Max Visible Columns Kolom ke-21, [Reset to Default], (X) dan Esc, serta Cache Tidak Memengaruhi Tabel Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-666
  - TC-FA-GRP-667
  - TC-FA-GRP-668
  - TC-FA-GRP-1091
coverage:
  web: automated
---

# Tab Users Setup Column: Batas Max Visible Columns Kolom ke-21, [Reset to Default], (X) dan Esc, serta Cache Tidak Memengaruhi Tabel Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Untuk TC-1091 (S-11): client punya 12 Custom Field User aktif sehingga Tab Users memiliki 9 kolom bawaan dan curated ditambah 12 kolom Custom Field (total 21); Max Visible Columns pada System Limits = 20. Di hook `before` spec ini sesi API aktor membaca jumlah Custom Field User aktif client, lalu membuat Custom Field User aktif bersuffix `CF-{n} {runId}` sampai total Custom Field User aktif client = 12; hook `after` menghapus Custom Field yang dibuat spec ini dan preferensi kolom (lihat Temuan untuk QA).
- State yang diubah spec: konfigurasi Setup Column tersimpan (urutan, hide, pin) dan kolom Tab Users; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE). Spec mengasumsikan Tab Assets tersedia sebagai tabel lain di modul yang sama (TC-668).

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A

### TC-666: [Reset to Default]

2. Buka Popup Setup Column, ubah urutan kolom, hide satu kolom, pin satu kolom, lalu klik [Save]
3. Buka lagi Popup Setup Column
4. Klik [Reset to Default]
5. Verifikasi Live Preview kembali ke susunan default (kolom default tampil, curated tersembunyi, tanpa pin)
6. Klik [Save]
7. Verifikasi tabel kembali ke susunan default
8. Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
9. Verifikasi tabel tetap berada pada susunan default setelah F5

### TC-667: (X) dan Esc membatalkan perubahan

10. Buka Popup Setup Column, uncheck satu kolom
11. Verifikasi footer popup tidak memuat [Cancel]
12. Klik (X)
13. Verifikasi popup tertutup tanpa menerapkan perubahan
14. Buka lagi Popup Setup Column, drag satu kolom
15. Tekan Esc
16. Verifikasi popup tertutup tanpa menerapkan perubahan
17. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir

### TC-668: Cache tidak memengaruhi tabel lain

18. Buka tabel lain modul ini (klik Tab Assets)
19. Catat susunan kolom tabel Tab Assets (urutan dan kolom yang tampil)
20. Kembali ke Tab Users
21. Hide satu kolom di tabel ini, lalu klik [Save]
22. Buka tabel lain modul ini (klik Tab Assets)
23. Verifikasi susunan kolom Tab Assets sama dengan catatan langkah 19 (tabel Tab Assets tetap memakai konfigurasi kolomnya sendiri)
24. Kembali ke Tab Users
25. Verifikasi konfigurasi Tab Users tetap tersimpan (kolom yang di-hide tidak tampil)

### TC-1091: Batas Max Visible Columns

26. Buka Popup Setup Column
27. Centang kolom hingga 20 kolom tercentang
28. Verifikasi tepat 20 kolom tercentang
29. Hover checkbox kolom ke-21 yang belum tercentang
30. Verifikasi checkbox kolom ke-21 disabled
31. Verifikasi tooltip `Maximum 20 columns can be shown at once. Uncheck another column first.` tampil
32. Verifikasi 20 kolom yang tercentang tidak berubah
33. Uncheck satu kolom yang tercentang
34. Hover checkbox kolom ke-21
35. Verifikasi checkbox kolom ke-21 kembali enabled
36. Klik (X) untuk menutup popup tanpa menyimpan

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): `Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A` pada TC-666 (TC tidak menyebut pembukaan ulang popup sesudah F5; lihat Temuan untuk QA), membuka Tab Assets, mencatat susunan kolomnya sebagai baseline sebelum hide (S-12), dan kembali ke Tab Users pada TC-668, dan menutup popup lewat `(X)` di akhir spec.
- Spec memiliki 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Setup Column Tab Users pada dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan TC-668 memuat baseline Tab Assets.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-666 langkah 3 "ubah urutan, hide, dan pin beberapa kolom" tidak menyebut kolom; spec memilih satu kolom tiap aksi. Perilaku sesudah F5 (popup tertutup atau tetap terbuka) tidak disebut TC.
  - TC-1091 mensyaratkan client dengan 12 Custom Field User aktif dan Max Visible Columns = 20 (System Limits) yang tidak ada di Pre-setup; spec men-seed kekurangan Custom Field di hook `before` dan menghapusnya di hook `after` (S-11).
  - TC-1091: 12 Custom Field User aktif di-seed dengan membaca jumlah aktif lalu membuat `CF-{n} {runId}` lewat sesi API akun aktor; kemampuan membaca dan membuat Custom Field lewat API belum dikonfirmasi di LLD. Dikonfirmasi tim BE.
