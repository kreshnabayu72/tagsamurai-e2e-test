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
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9). Node yang diperiksa pada langkah 14 sampai 19:

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
4. Klik (⋯) pada baris Warehouse A
5. Verifikasi menu baris hanya memuat Detail
6. Tutup menu dengan Esc
7. Klik (⋯) pada node Warehouse A di sidebar
8. Verifikasi menu sidebar hanya memuat Detail
9. Tutup menu dengan Esc
10. Verifikasi Bulk Delete tidak tersedia karena kolom Checkbox tidak dirender
11. Verifikasi sidebar menampilkan seluruh tree client (Head Office, Warehouse A, Warehouse B, Global HQ, dan Region East) dalam keadaan view-only
12. Verifikasi Search, Filter, Download, Changelog, sort, pagination, dan Column Visibility tampil dan aktif

### TC-FA-GRP-78: Read Only tanpa aksi tulis pada node mana pun

13. Untuk setiap baris tabel "Node yang diperiksa" di Prerequisites, lakukan langkah 14 sampai 19
14. Klik (⋯) pada baris node tersebut
15. Verifikasi menu baris hanya memuat Detail dan tidak memuat Add Subgroup, Edit, maupun Delete
16. Tutup menu dengan Esc
17. Klik (⋯) pada node tersebut di sidebar
18. Verifikasi menu sidebar hanya memuat Detail dan tidak memuat Add Subgroup, Edit, maupun Delete
19. Tutup menu dengan Esc
20. Verifikasi kolom Checkbox dan tombol [+] Group tidak dirender

## Notes

- Spec ditulis dengan login Read Only di hook `before`; tidak ada ganti akun.
- Langkah 14 sampai 19 diulang untuk tiga node pada tabel Prerequisites (Head Office, Disposal Yard, Warehouse B); Warehouse A sudah diperiksa pada langkah 4 sampai 9 (ekspansi 18 langkah; total ekspansi 32 langkah, di bawah batas sekitar 35).
- Langkah penghubung (S-03): langkah 6, 9, 16, 19 (menutup menu).
- Pembagian TC lintas spec: Role Total Control dan Default User (TC-FA-GRP-44 dan 45) ada di spec 015.
- Temuan untuk QA:
  - TC-FA-GRP-78 menyebut "elipsis tiap baris dan node sidebar" tanpa daftar baris; spec memeriksa Warehouse A (langkah 4 sampai 9) serta tiga node pada tabel Prerequisites yang mewakili Function None, Disposal Group, dan Excess.
  - TC-FA-GRP-46 menyebut "seluruh tree client view-only" tanpa daftar node; spec memakai node Tabel A yang tampil di sidebar.
