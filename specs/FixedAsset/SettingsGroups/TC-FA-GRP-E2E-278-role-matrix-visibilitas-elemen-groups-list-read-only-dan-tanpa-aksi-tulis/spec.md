---
id: TC-FA-GRP-E2E-278-role-matrix-visibilitas-elemen-groups-list-read-only-dan-tanpa-aksi-tulis
title: "Role Matrix: Visibilitas Elemen Groups List Role Read Only dan Read Only Tanpa Aksi Tulis"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-46
  - TC-FA-GRP-78
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Groups List Role Read Only dan Read Only Tanpa Aksi Tulis

## Prerequisites

- Mode: FE+BE.
- Role yang diuji: Read Only (Pre-setup No 3) `readOnlyGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_RO_PASSWORD`.
- Login di hook `before` spec ini sebagai Read Only; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` untuk akun Read Only disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE); hook suite hanya menyetel akun aktor default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9). Node yang diperiksa pada langkah 16 sampai 23:

| Node | Function |
|---|---|
| Head Office | None |
| Disposal Yard | Disposal Group |
| Warehouse B | Assignable, Excess |

- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-46: Visibilitas elemen Read Only

1. Verifikasi menu Settings > Groups tampil (view)
2. Verifikasi kolom Checkbox Hidden
3. Verifikasi tombol [+] Group Hidden
4. Ketik Search `Warehouse A` pada Groups List, tekan Enter
5. Klik (⋯) pada baris Warehouse A
6. Verifikasi menu baris hanya memuat Detail
7. Tutup menu dengan Esc
8. Klik (⋯) pada node Warehouse A di sidebar
9. Verifikasi menu sidebar hanya memuat Detail
10. Tutup menu dengan Esc
11. Klik `(←)` pada kotak Search
12. Verifikasi Bulk Delete tidak tersedia karena kolom Checkbox tidak dirender
13. Verifikasi sidebar menampilkan seluruh tree client (Head Office, Warehouse A, Warehouse B, Global HQ, dan Region East) dalam keadaan view-only
14. Verifikasi Search, Filter, Download, Changelog, sort, pagination, dan Column Visibility tampil dan aktif

### TC-FA-GRP-78: Read Only tanpa aksi tulis pada node mana pun

15. Untuk setiap baris tabel "Node yang diperiksa" di Prerequisites, lakukan langkah 16 sampai 23
16. Ketik Search nama node tersebut pada Groups List, tekan Enter
17. Klik (⋯) pada baris node tersebut
18. Verifikasi menu baris hanya memuat Detail dan tidak memuat Add Subgroup, Edit, maupun Delete
19. Tutup menu dengan Esc
20. Klik (⋯) pada node tersebut di sidebar
21. Verifikasi menu sidebar hanya memuat Detail dan tidak memuat Add Subgroup, Edit, maupun Delete
22. Tutup menu dengan Esc
23. Klik `(←)` pada kotak Search
24. Verifikasi kolom Checkbox dan tombol [+] Group tidak dirender

## Notes

- Spec ditulis dengan login Read Only di hook `before`; tidak ada ganti akun.
- Langkah 16 sampai 23 diulang untuk tiga node pada tabel Prerequisites (Head Office, Disposal Yard, Warehouse B); Warehouse A sudah diperiksa pada langkah 4 sampai 11 (ekspansi 24 langkah; total ekspansi 40 langkah, di atas batas sekitar 35). Alasan di atas ~35 langkah: satu kelas (Role Matrix Read Only) dan satu dataset (Tabel A); tiap TC berdiri sendiri; 4 langkah penghubung per node (Search dan kosongkan Search) tidak membawa asersi baru.
- Langkah penghubung (S-03): langkah 7, 10, 19, 22 (menutup menu).
- Pembagian TC lintas spec: Role Total Control dan Default User (TC-FA-GRP-44 dan 45) ada di spec 015.
- Langkah penghubung (S-03, S-14, R-16): `Ketik Search` pada Groups List dengan nama node (`Warehouse A` dan tiap node pada tabel Prerequisites) sebelum membuka elipsis baris, karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; `Klik (←) pada kotak Search` sesudah menu ditutup mengembalikan tabel penuh untuk langkah berikutnya.
- Temuan untuk QA:
  - TC-FA-GRP-78 menyebut "elipsis tiap baris dan node sidebar" tanpa daftar baris; spec memeriksa Warehouse A (langkah 4 sampai 9) serta tiga node pada tabel Prerequisites yang mewakili Function None, Disposal Group, dan Excess.
  - TC-FA-GRP-46 menyebut "seluruh tree client view-only" tanpa daftar node; spec memakai node Tabel A yang tampil di sidebar.
