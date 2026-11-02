---
id: TC-AC-SG-E2E-103-konkurensi-dua-admin-delete-bersamaan-menghabiskan-group-dan-invarian-minimal-satu-group
title: "Konkurensi Dua Admin: Delete Bersamaan Menghabiskan Group dan Invarian Minimal Satu Group"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-382
  - TC-AC-SG-391
coverage:
  web: automated
---

# Konkurensi Dua Admin: Delete Bersamaan Menghabiskan Group dan Invarian Minimal Satu Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (Sesi A): Total Control entitas Distributor Dua Group, `totalControlDuaGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #23), password `Spectra.env.AC_SG_DUA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi B (konteks browser kedua, Pre-setup #39): akun yang sama dengan Sesi A. Dibuka di langkah 1 dan ditutup di langkah 11 (S-09).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data Pre-setup yang menjadi target aksi tulis dan hapus: entitas `Distributor Dua Group` berisi tepat dua group tanpa entitas, `Gudang Utara` dan `Gudang Selatan` (Pre-setup #23). Pengecualian S-06 (data tidak dapat dimiliki spec, dengan pemulihan lewat fixture backend): entitas ini tidak dapat dimiliki spec karena invarian "tepat 2 group" menjadi objek uji; pemulihannya ke baseline (tepat `Gudang Utara` dan `Gudang Selatan`) dijamin Fixture BE yang disediakan tim FE/BE dan dinyatakan di suite.md, dijalankan di hook `before` dan `after` serta pada langkah 10 antar blok TC. Efeknya: Last Updated, Modified By, dan entri audit trail Changelog `Gudang Utara` dan `Gudang Selatan` bertambah setiap run; suite berjalan serial (`parallel: false`).
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas Distributor Dua Group; disediakan tim FE/BE).

## Test Steps

1. Buka konteks browser kedua (Sesi B), login sebagai Total Control Distributor Dua Group, lalu buka halaman Settings > Group

### TC-AC-SG-382: Dua admin menghapus node berbeda bersamaan sehingga menghabiskan seluruh group

2. Pada Sesi A, klik ikon `⋯` pada baris `Gudang Utara` lalu `Delete` sehingga dialog Delete terbuka
3. Pada Sesi B, klik ikon `⋯` pada baris `Gudang Selatan` lalu `Delete` sehingga dialog Delete terbuka
4. Pada Sesi A, klik `[Delete]` pada dialog
5. Verifikasi Sesi A menampilkan toast sukses: "Success, group has been deleted."
6. Pada Sesi B, klik `[Delete]` pada dialog
7. Verifikasi Sesi B menampilkan dialog blok D-02 "Cannot Delete Group"
8. Pada Sesi B, klik `[OK]` pada dialog blok
9. Verifikasi tepat satu group tersisa (`Gudang Selatan`) pada Sidebar Group Tree Sesi A
10. Pulihkan baseline entitas Distributor Dua Group (tepat `Gudang Utara` dan `Gudang Selatan`) lewat Fixture BE, lalu muat ulang halaman Sesi A
11. Tutup konteks browser Sesi B

### TC-AC-SG-391: Invarian minimal satu group: hapus satu dari dua lolos, hapus keduanya diblok

12. Pada Sesi A, klik ikon `⋯` pada baris `Gudang Utara` lalu `Delete`
13. Pada Sesi A, konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
14. Verifikasi penghapusan pertama sukses dengan toast: "Success, group has been deleted."
15. Pada Sesi A, tunggu toast lama hilang otomatis
16. Pada Sesi A, klik ikon `⋯` pada baris `Gudang Selatan` lalu `Delete`
17. Verifikasi dialog blok D-02 "Cannot Delete Group" tampil karena penghapusan menyisakan 0 group
18. Pada Sesi A, klik `[OK]` pada dialog blok
19. Verifikasi `Gudang Selatan` masih ada

## Notes

- Kelas c (multi-konteks, dua admin) untuk TC-AC-SG-382: Sesi B menjadi objek asersi (dialog blok pada langkah 7). TC-AC-SG-391 satu sesi dan ditaruh sesudah Sesi B ditutup; keduanya berbagi entitas dan baseline sehingga memakai satu spec.
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (membuka Sesi B), langkah 8 (menutup dialog blok), langkah 10 (pemulihan baseline dan memuat ulang halaman Sesi A, S-09), langkah 11 (menutup konteks Sesi B), dan langkah 15 (menunggu toast lama hilang agar toast berulang diasersi sebagai toast baru, R-12).
- Penghapusan `Gudang Selatan` pada TC-AC-SG-391 (langkah 17) tidak dikonfirmasi karena yang diasersi adalah diblokirnya penghapusan oleh dialog blok D-02; langkah 19 membuktikan group masih ada setelah `[OK]`.
- Hook `after` memulihkan baseline entitas Distributor Dua Group dan mengembalikan sesi ke akun default spec.
- Temuan untuk QA:
  - Pre-setup #39 menyebut dua sesi dengan akun Total Control yang sama dan Pre-setup #23 hanya memuat satu akun Total Control untuk `Distributor Dua Group`; bila batas satu sesi web per akun berlaku, Sesi A dapat terusir saat Sesi B login. Perlu konfirmasi tim FE/BE.
  - TC-AC-SG-382 Expected tidak menyebut isi body dialog blok D-02, hanya judul "Cannot Delete Group"; spec mengasersi dialog dengan judul itu.
  - TC-AC-SG-382 dan TC-AC-SG-391 tidak menyebut hasil UI Sesi A setelah Sesi B ditolak; spec mengasersi Sidebar Group Tree Sesi A memuat tepat satu group.
