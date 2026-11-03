---
id: TC-AC-SG-E2E-014-mobile-android-card-list-bottom-sheet-tree-dan-toolbar
title: "Mobile Android: Card List, Bottom Sheet Tree, dan Toolbar Settings > Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-52
  - TC-AC-SG-53
  - TC-AC-SG-54
coverage:
  web: unsupported
  mobile: automated
---

# Mobile Android: Card List, Bottom Sheet Tree, dan Toolbar Settings > Group

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android TAG Samurai (PRD §4.6).
- Perangkat atau emulator Android dengan aplikasi terpasang (Pre-setup #37), serta kemampuan tap, ketik, dan mengetuk elemen UI. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Pre-setup #37 menyebut "akun Total Control Principal uji" tanpa email; spec memakai akun Pre-setup #1 (lihat Temuan untuk QA). Login di aplikasi Android dilakukan di hook `before` spec ini.
- Hook suite web (`beforeEach` pembuka halaman) berlaku untuk sesi browser; pada sesi aplikasi Android halaman dibuka lewat langkah spec ini. Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` untuk akun aktor disetel `seen` oleh hook suite (kemampuan disediakan tim FE/BE; lihat `suite.md`).
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group; Card List halaman 1 memuat `Region A`).
- State yang diubah spec: konfigurasi kolom Column Visibility di perangkat (kolom `Modified By` disembunyikan lalu ditampilkan kembali pada langkah 8); hook `before` dan `after` spec ini menghapus preferensi kolom tabel di aplikasi (kemampuan disediakan tim FE).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data group sehingga tidak ada seeding, suffix `{runId}-014`, maupun cleanup data.

## Test Steps

### TC-AC-SG-52: Screening Card List mobile pada halaman Settings > Group

1. Buka menu `Settings > Group` di aplikasi mobile
2. Susuri satu card pada daftar
3. Verifikasi tabel berganti menjadi Card List
4. Verifikasi tiap card menampilkan nama group (tebal), Total User, Total Member, Modified By, Last Updated, dan ikon `⋯`
5. Verifikasi tidak ada kolom Checkbox permanen di luar selection mode
6. Sembunyikan kolom `Modified By` lewat Column Visibility pada bottom sheet `⋯`
7. Verifikasi kolom `Modified By` tidak tampil pada card
8. Tampilkan kembali kolom `Modified By` lewat Column Visibility

### TC-AC-SG-53: Sidebar tree mobile menjadi bottom sheet berisi tombol [+] Group

9. Ketuk ikon tree pada toolbar mobile
10. Verifikasi bottom sheet menampilkan tree grup dengan tombol `[+] Group` di dalamnya
11. Tutup bottom sheet tree
12. Cari tombol create level 1 di toolbar mobile dan floating action button
13. Verifikasi toolbar mobile tampil dengan ikon tree
14. Verifikasi toolbar mobile tidak memiliki tombol create level 1
15. Verifikasi tidak ada floating action button

### TC-AC-SG-54: Toolbar mobile: tombol ⋯ bottom sheet dan search inline

16. Ketuk ikon `⋯` pada toolbar mobile
17. Verifikasi bottom sheet `⋯` memuat Column Visibility, Filter, dan Download
18. Tutup bottom sheet `⋯`
19. Ketuk ikon pencarian `[🔍]`, ketik "Region", lalu submit
20. Verifikasi Search tampil inline
21. Verifikasi hasil memuat sedikitnya satu card
22. Verifikasi setiap card hasil cocok dengan pencarian "Region"
23. Ketuk `✕` pada kotak Search untuk mengosongkan pencarian

## Notes

- Langkah penghubung (S-03, S-09): langkah 2 mengamati tanpa asersi sendiri; langkah 6 dan 8 menyembunyikan dan menampilkan kembali kolom `Modified By` sebagai prasyarat Expected c TC-AC-SG-52 (TC tidak memuat langkahnya); langkah 11, 18 menutup bottom sheet; langkah 12 mengamati tanpa asersi sendiri; langkah 23 mengosongkan Search. Langkah 1 membuka halaman secara eksplisit karena hook `beforeEach` suite membuka halaman pada sesi web.
- Asersi absence langkah 14 dan 15 berjangkar pada toolbar mobile yang tampil (langkah 13); asersi universal langkah 22 didahului pembanding "sedikitnya satu card" (langkah 21).
- Temuan untuk QA:
  - TC-AC-SG-52 Expected c ("kolom yang di-hide lewat Column Visibility tidak tampil pada card") tidak punya langkah atau precondition yang menyembunyikan kolom; langkah 6 sampai 8 ditambahkan sebagai langkah penghubung (S-03) dan label kolom yang disembunyikan (`Modified By`) dipilih spec.
  - Pre-setup #37 tidak menyebut email akun Total Control Principal untuk mobile, dan TC-AC-SG-53 sampai 56 tidak menyebut nomor Pre-setup di precondition; spec memakai akun Pre-setup #1.
  - TC-AC-SG-52 sampai 54 bertanda `Manual Only`; spec tetap ditulis dengan perangkat Android yang dibutuhkan dicatat di Prerequisites.
  - Cara membuka bottom sheet toolbar dan label tombol submit pencarian mobile tidak disebut TC selain ikon `[🔍]` dan "submit".
