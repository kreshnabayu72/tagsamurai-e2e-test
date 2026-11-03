---
id: TC-FA-GRP-E2E-008-navigasi-node-sidebar-direct-children-all-groups-noop-leaf-dan-transisi-empty-subgroup
title: "Navigasi Node Sidebar: Direct Children, All Groups, Klik Ulang No-Op, Leaf, serta Transisi Masuk dan Keluar Empty State Subgroup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-20
  - TC-FA-GRP-21
  - TC-FA-GRP-22
  - TC-FA-GRP-23
  - TC-FA-GRP-945
  - TC-FA-GRP-946
coverage:
  web: automated
---

# Navigasi Node Sidebar: Direct Children, All Groups, Klik Ulang No-Op, Leaf, serta Transisi Masuk dan Keluar Empty State Subgroup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubah flag itu.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9): Head Office > Floor 2 > IT Department > Server Room (Server Room adalah leaf).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after` bila masih ada):

| TC | Nama TC | Nama seed | Keterangan |
|---|---|---|---|
| TC-FA-GRP-945 | Solo Parent > Solo Child | `Solo Parent {runId}-008` > `Solo Child {runId}-008` | Level 1 dengan satu child kosong; Solo Child dihapus oleh langkah 29 sampai 31 |
| TC-FA-GRP-946 | Leaf Parent | `Leaf Parent {runId}-008` | Level 1 tanpa child |
| TC-FA-GRP-946 | First Child | `First Child {runId}-008` | Dibuat oleh langkah 22 dan 23 di bawah Leaf Parent; dihapus di hook `after` |

- Kemampuan teknis: fixture BE (seeding, pembacaan agregat Total Asset dan Total User, pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-20: Klik node sidebar menampilkan direct children

1. Klik node Head Office di sidebar
2. Verifikasi tabel hanya berisi Floor 2 (direct child)
3. Verifikasi Head Office, IT Department, dan Server Room tidak menjadi baris tabel
4. Verifikasi node Head Office tampil terpilih di sidebar
5. Verifikasi Group Context Header menampilkan Head Office
6. Verifikasi Popup Detail Group tidak terbuka

### TC-FA-GRP-22: Klik node yang sudah terpilih

7. Klik node Head Office di sidebar lagi
8. Verifikasi Head Office tetap terpilih
9. Verifikasi tabel tidak berubah (tetap hanya Floor 2, tidak kembali ke All Groups)

### TC-FA-GRP-21: Klik All Groups

10. Klik node `All Groups` di sidebar
11. Verifikasi tabel kembali ke node level 1
12. Verifikasi Group Context Header menampilkan judul `All Groups` dengan Total Asset dan Total User atas union himpunan seluruh node dalam scope aktor (seluruh tree client untuk Total Control), distinct dedup, sesuai pembacaan fixture BE

### TC-FA-GRP-23: Klik leaf node

13. Klik toggle expand-all pada sidebar
14. Klik node Server Room (leaf) di sidebar
15. Verifikasi tabel menampilkan Illustration dengan title `No subgroup yet` dan body `This group does not have any subgroups.`
16. Verifikasi tampilan itu bukan error
17. Verifikasi Group Context Header tetap tampil dengan Total Asset dan Total User exact-match Server Room sesuai pembacaan fixture BE

### TC-FA-GRP-946: Transisi keluar empty state saat child pertama dibuat

18. Klik node `Leaf Parent {runId}-008` di sidebar
19. Verifikasi tabel menampilkan empty state `No subgroup yet` (kondisi awal sebelum child dibuat)
20. Klik elipsis (⋯) node `Leaf Parent {runId}-008` di sidebar
21. Klik `Add Subgroup`
22. Isi Group Name `First Child {runId}-008`
23. Klik [Submit]
24. Verifikasi toast sukses `Success, group has been created.`
25. Verifikasi empty state hilang dan tabel menampilkan baris `First Child {runId}-008`
26. Verifikasi `Leaf Parent {runId}-008` tetap terpilih

### TC-FA-GRP-945: Transisi masuk empty state saat child terakhir dihapus

27. Klik node `Solo Parent {runId}-008` di sidebar
28. Verifikasi tabel menampilkan baris `Solo Child {runId}-008` (kondisi awal sebelum dihapus)
29. Klik (⋯) pada baris `Solo Child {runId}-008`
30. Klik `Delete`
31. Klik [Delete] pada dialog konfirmasi
32. Verifikasi toast sukses `Success, group has been deleted.`
33. Verifikasi tabel otomatis berpindah ke Illustration dengan title `No subgroup yet` dan body `This group does not have any subgroups.`
34. Verifikasi `Solo Parent {runId}-008` tetap terpilih dan Group Context Header tetap tampil

## Notes

- Spec 34 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 13 (expand-all agar Server Room terlihat), langkah 19 dan 28 (`Verifikasi` kondisi awal sebagai anchor sebelum transisi; tidak ada di Expected TC dan dicatat di sini sesuai S-03).
- Urutan TC dalam spec: 20, 22, 21, 23, 946, 945. Aksi hapus child terakhir (TC-FA-GRP-945) diletakkan paling akhir (S-10).
- Temuan untuk QA:
  - TC-FA-GRP-21 menyebut union himpunan tanpa angka; spec mengasersi lewat pembacaan fixture BE (disediakan tim FE/BE).
  - TC-FA-GRP-945 dan 946 memakai nama literal (`Solo Parent`, `Leaf Parent`, `First Child`); spec memakai nama bersuffix (S-12).
