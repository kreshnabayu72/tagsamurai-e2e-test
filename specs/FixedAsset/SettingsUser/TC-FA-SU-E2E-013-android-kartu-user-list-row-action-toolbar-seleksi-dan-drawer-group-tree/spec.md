---
id: TC-FA-SU-E2E-013-android-kartu-user-list-row-action-toolbar-seleksi-dan-drawer-group-tree
title: "Android: Kartu User List, Row Action, Toolbar, Seleksi, dan Drawer Group Tree"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-39
  - TC-FA-SU-40
  - TC-FA-SU-41
  - TC-FA-SU-42
  - TC-FA-SU-43
coverage:
  mobile: automated
---

# Android: Kartu User List, Row Action, Toolbar, Seleksi, dan Drawer Group Tree

## Prerequisites

- Mode: FE+BE (backend nyata).
- Perangkat: perangkat atau emulator Android dengan aplikasi native TAG Samurai Mobile (FAMS) terpasang (disediakan tim FE). Perangkat dipakai bersama sehingga spec berjalan dengan `parallel: false`; gestur long-press, drawer, dan bottom sheet diamati di perangkat itu.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di aplikasi Android di hook `before` spec ini. Hook `beforeEach` suite membuka halaman web dan tidak berlaku untuk perangkat Android, sehingga halaman Settings > User dibuka oleh langkah 1.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20) dan pohon grup (#21). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: gestur long-press dan ketuk pada perangkat Android; drawer off-canvas dan bottom sheet; pembacaan elemen aplikasi native (disediakan tim FE).
- State global: seleksi kartu dibersihkan langkah 27; tidak ada state server yang diubah (dialog Deactivate dibatalkan). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-39: Android: baris User List menjadi kartu ringkasan vertikal dengan field baku

1. Buka Settings > User di aplikasi Android
2. Verifikasi tiap pengguna tampil sebagai kartu: baris 1 sakelar Active, Nama (tebal), dan `[⋯]`; baris 2 `Position · Division`; baris 3 label jumlah Role (badge `Total Control` atau `Read Only` menggantikan label jumlah) dan badge Pending (`Pending Activation` atau `Pending Email Confirmation`) bila ada
3. Verifikasi kartu Budi Santoso menampilkan `4 roles`
4. Verifikasi kartu Ahmad Dahlan menampilkan badge `Total Control`
5. Verifikasi kartu Hana Kusuma menampilkan `0 roles` dan badge `Pending Activation`

### TC-FA-SU-40: Android: row action lewat ⋯ pada kartu memuat Detail dan aksi kondisional

6. Ketuk `[⋯]` pada kartu Hana Kusuma
7. Verifikasi menu `[⋯]` kartu Hana Kusuma memuat `Detail`, `Edit Home Group`, dan `Resend Activation Email`
8. Tutup menu
9. Ketuk `[⋯]` pada kartu Indra Wijaya
10. Verifikasi menu `[⋯]` kartu Indra Wijaya memuat `Detail`, `Edit Home Group`, dan `Resend Confirmation Email`
11. Tutup menu

### TC-FA-SU-41: Android: toolbar memakai inline search dan bottom sheet ⋯ untuk Column Visibility, Filter, dan Download

12. Ketuk ikon pencarian
13. Verifikasi ikon `[🔍]` membuka input pencarian inline
14. Tutup input pencarian
15. Ketuk `[⋯]` toolbar
16. Verifikasi `[⋯]` toolbar membuka bottom sheet berisi Column Visibility, Filter, dan Download
17. Tutup bottom sheet
18. Verifikasi ikon Changelog `[📋]` tetap di header halaman

### TC-FA-SU-42: Android: seleksi baris lewat long-press kartu dan aksi bulk Activate, Deactivate, Edit Home Group, Resend Activation Email

19. Long-press kartu Gita Permata
20. Verifikasi long-press kartu memilih baris dan menampilkan bar aksi massal dengan counter mobile
21. Ketuk kartu Hana Kusuma
22. Buka aksi massal
23. Verifikasi aksi bulk tersedia: Activate, Deactivate, Edit Home Group, dan Resend Activation Email (kondisional sesuai status seleksi)
24. Pilih aksi massal `Deactivate`
25. Verifikasi dialog konfirmasi bulk tampil sebagai bottom sheet
26. Tutup dialog konfirmasi tanpa mengonfirmasi
27. Hapus seleksi kartu

### TC-FA-SU-43: Android: Sidebar Group Tree disembunyikan dalam drawer samping

28. Verifikasi Sidebar Group Tree tidak tampil di layar utama (kartu User List tampil sebagai anchor)
29. Buka drawer Sidebar Group Tree
30. Verifikasi Sidebar Group Tree terbuka sebagai off-canvas drawer
31. Pilih node `Finance & Accounting`
32. Verifikasi daftar kartu terfilter seperti di web: kartu Budi Santoso tampil dan kartu Doni Prasetyo tidak tampil
33. Pilih node `All Groups` untuk memulihkan filter

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Seluruh TC bertanda `Manual Only (b)` tetap masuk spec (bagian 2 konvensi); kebutuhan teknisnya ada di `## Prerequisites`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8, 11, 14, 17, dan 26 (menutup menu, input, bottom sheet, atau dialog, S-09), langkah 27 (menghapus seleksi, S-09), langkah 33 (memulihkan filter node, S-09). Langkah 28 adalah baris anchor permukaan untuk asersi absence (bagian 8b butir 2, S-03); bukan Expected TC.
- Langkah 21 (ketuk kartu Hana Kusuma) menambah kartu ke seleksi karena bar aksi massal sudah aktif; Langkah Uji TC-FA-SU-42 tidak memisahkannya.
- Temuan untuk QA:
  - TC-FA-SU-42 Langkah Uji 3 ("pilih Deactivate") tidak menyebut apakah dialog dikonfirmasi; Expected c hanya meminta dialog tampil sebagai bottom sheet, sehingga spec membatalkan dialog agar status pengguna tidak berubah.
  - TC-FA-SU-40 Expected a menyebut `Edit Home Group` "kondisional" tanpa menjelaskan kondisinya; spec mengasersi `Edit Home Group` pada menu Hana Kusuma dan Indra Wijaya yang diasumsikan memenuhi kondisi (aktor Total Control, bukan Default User atau Self).
  - TC-FA-SU-42 Expected a menyebut "counter mobile" tanpa bentuk visual; spec mengasersi keberadaan counter.
