---
id: TC-FA-GRP-E2E-011-refresh-f5-dan-sinkron-seleksi-node-terpilih-setelah-hapus-dan-klik-ulang-menu
title: "Refresh F5 Mempertahankan Node Terpilih dan State Tabel, Node Terpilih Dihapus (Langsung, Cascade, Oleh User Lain), dan Klik Ulang Menu Groups"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-30
  - TC-FA-GRP-31
  - TC-FA-GRP-32
  - TC-FA-GRP-33
  - TC-FA-GRP-1122
coverage:
  web: automated
---

# Refresh F5 Mempertahankan Node Terpilih dan State Tabel, Node Terpilih Dihapus (Langsung, Cascade, Oleh User Lain), dan Klik Ulang Menu Groups

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (di-seed di hook `before` lewat API, milik spec ini, dihapus di hook `after` bila masih ada; node level 1 sehingga tampil di sidebar). Node milik spec dipakai agar Head Office dan Branch Office Tabel A tidak berubah (S-06):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-FA-GRP-30, 1122 | Head Office dengan 11 child atau lebih | `Page Parent {runId}-011` | Function None, level 1, berisi 12 child `Child 01 {runId}-011` sampai `Child 12 {runId}-011`, semuanya Assignable dan tanpa aset |
| TC-FA-GRP-31 | Branch Office | `Gone Office {runId}-011` | Level 1, kosong |
| TC-FA-GRP-32 | Temp Delete | `Temp Delete {runId}-011` | Level 1, kosong |
| TC-FA-GRP-33 | Cascade Root > Cascade Child | `Cascade Root {runId}-011` > `Cascade Child {runId}-011` | Keduanya kosong |

- Ukuran halaman tabel 10 baris per halaman (default), sehingga 12 child menempati dua halaman.
- Kemampuan teknis: fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor (login API password untuk akun Total Control sebagai admin lain), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-30: Refresh F5 mempertahankan node terpilih dan state tabel

1. Klik `Page Parent {runId}-011` di sidebar
2. Ketik Search `Child`, tekan Enter
3. Klik ikon `Filter`
4. Pilih Function `Assignable`
5. Klik [Apply]
6. Klik header kolom Group 2× (sort Group Z→A)
7. Klik halaman 2 pada pagination
8. Muat ulang halaman dengan F5
9. Verifikasi `Page Parent {runId}-011` tetap terpilih
10. Verifikasi Search `Child` tetap terisi
11. Verifikasi filter Function `Assignable` tetap aktif
12. Verifikasi sort Group Z→A tetap
13. Verifikasi halaman 2 tetap aktif

### TC-FA-GRP-1122: Klik ulang menu Settings > Groups mereset node dan state tabel

14. Klik menu Settings > Groups pada sidebar navigasi aplikasi
15. Verifikasi node `All Groups` terpilih kembali dan tabel menampilkan group level 1 dengan Group Context Header `All Groups`
16. Verifikasi Search kosong
17. Verifikasi tidak ada filter aktif
18. Verifikasi Sort kembali ke default (Group A–Z)
19. Verifikasi halaman 1 aktif

### TC-FA-GRP-31: Refresh F5 saat node terpilih sudah dihapus user lain

20. Klik `Gone Office {runId}-011` di sidebar
21. Hapus `Gone Office {runId}-011` lewat sesi API admin lain hingga penghapusan tersimpan
22. Muat ulang halaman dengan F5
23. Verifikasi tampilan kembali ke `All Groups`

### TC-FA-GRP-32: Delete node yang sedang terpilih

24. Klik `Temp Delete {runId}-011` di sidebar
25. Klik elipsis (⋯) node `Temp Delete {runId}-011` di sidebar
26. Klik `Delete`
27. Klik [Delete] pada dialog konfirmasi
28. Verifikasi toast sukses `Success, group has been deleted.`
29. Verifikasi seleksi sidebar kembali ke `All Groups`
30. Verifikasi Group Context Header kembali ke `All Groups`

### TC-FA-GRP-33: Node terpilih ikut terhapus via cascade ancestor

31. Klik chevron node `Cascade Root {runId}-011` untuk expand
32. Klik `Cascade Child {runId}-011` di sidebar
33. Klik elipsis (⋯) node `Cascade Root {runId}-011` di sidebar
34. Klik `Delete`
35. Klik [Delete] pada dialog konfirmasi
36. Verifikasi toast sukses `Success, group has been deleted.`
37. Verifikasi seleksi kembali ke `All Groups`
38. Verifikasi `Cascade Root {runId}-011` dan `Cascade Child {runId}-011` tidak ada di tree

## Notes

- Spec melewati sekitar 35 langkah (38 langkah): seluruh blok adalah satu kelas (sinkron seleksi node di Groups List) pada dataset milik spec, tiap blok berdiri sendiri, dan blok yang menghapus data (TC-FA-GRP-32 dan 33) berada paling akhir.
- Langkah penghubung (S-03): langkah 21 (pelaku kedua lewat sesi API, bukan konteks kedua, P-2 `[KEPUTUSAN 2026-10-30]`), langkah 31 (expand node agar Cascade Child dapat diklik).
- State TC-FA-GRP-1122 (node, Search, Filter, Sort terpilih) dibentuk oleh langkah 1 sampai 7 yang sama dengan TC-FA-GRP-30 dan dipakai langsung; TC-FA-GRP-1122 menyebut keyword `floor` sedangkan langkah 2 memakai `Child` karena data milik spec.
- Urutan TC dalam spec: 30, 1122, 31, 32, 33.
- Temuan untuk QA:
  - TC-FA-GRP-30 dan 1122 menyebut Head Office dan keyword `floor`; spec memakai parent milik spec dengan 12 child karena Head Office Tabel A hanya punya satu child (Floor 2).
  - TC-FA-GRP-31 menghapus Branch Office; spec memakai `Gone Office {runId}-011` agar Pre-setup tidak berubah.
