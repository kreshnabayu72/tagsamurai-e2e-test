---
id: TC-FA-RP-E2E-179-tabel-role-transaksi-search-filter-dan-sort-3
title: "Tabel Role Transaksi: Search, Filter, dan Sort (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1071
  - TC-FA-RP-1072
coverage:
  web: automated
---

# Tabel Role Transaksi: Search, Filter, dan Sort (3/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon group), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab `Disposal`), dan #40 (tabel Role Transaksi section Asset Admin: Nadia Putri, Ahmad Fauzi, Dimas Pranata). Tanggal Temporary Until Nadia Putri dan Joined Date Dimas Pranata (15/02/26) dibaca dari fixture. Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- State yang diubah: konfigurasi kolom Setup Column tabel Role Transaksi (kolom curated ditampilkan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Header section `Asset Admin` memuat `6 users` (total seluruh baris tabel: tiga baris manual Pre-setup #40 dan tiga baris pola Admin Utama, Siti Rahmawati, Rina Wulandari; Pre-setup #19), dan jumlah itu tidak berubah oleh Search maupun Filter.
- Tabel Search kolom curated (TC-FA-RP-1071):

| Kolom | Keyword | Baris yang tampil |
|---|---|---|
| Email | `ahmadfauzi` | hanya Ahmad Fauzi |
| Activation Status | `pending activation` | hanya Nadia Putri |
| Temporary User | `yes` | hanya Nadia Putri |
| TAG | `tag-2002` | hanya Dimas Pranata |
| Cost Center | `cc-200` | hanya Dimas Pranata |
| Badge No | `bn-77` | hanya Ahmad Fauzi |

- Tabel Filter kolom curated (TC-FA-RP-1072):

| Field | Pilihan | Baris yang tampil |
|---|---|---|
| Activation Status | opsi `Pending Activation` | hanya Nadia Putri |
| Temporary User | opsi `Yes` | hanya Nadia Putri |
| Temporary Until | rentang tanggal yang mencakup tanggal Temporary Until Nadia Putri | hanya Nadia Putri |
| Cost Center | opsi `CC-200` | hanya Dimas Pranata |
| Joined Date | rentang tanggal yang mencakup Joined Date Dimas Pranata saja | hanya Dimas Pranata |

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
3. Buka section `Asset Admin`

### Search kolom curated (TC-FA-RP-1071)

4. Klik header `(⋯)` kolom Column Visibility pada section, klik `Setup Column...`, centang kolom `Email`, `Activation Status`, `Temporary User`, `TAG`, `Cost Center`, dan `Badge No`, lalu klik `[Save]`
5. Untuk setiap baris pada Tabel Search kolom curated, lakukan langkah 6 sampai 10
6. Ketik Search `<Keyword>`, tekan Enter
7. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel dan baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari tidak tampil (nilai kolomnya tidak memuat keyword)
8. Verifikasi header section `Asset Admin` tetap `6 users` (total seluruh baris, bukan jumlah hasil Search)
9. Kosongkan isi kotak search, tekan Enter
10. Verifikasi baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari tampil kembali bersama tiga baris manual

### Filter kolom curated (TC-FA-RP-1072)

11. Untuk setiap baris pada Tabel Filter kolom curated, lakukan langkah 12 sampai 16
12. Klik ikon Filter pada section, pilih `<Pilihan>` pada field `<Field>`, klik `[Apply]`
13. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel dan baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari tidak tampil (bukan Pending Activation, bukan Temporary User, tanpa Temporary Until, Cost Center dan Joined Date di luar pilihan)
14. Verifikasi header section `Asset Admin` tetap `6 users` (total seluruh baris, bukan jumlah hasil Filter)
15. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`
16. Verifikasi baris pola Admin Utama, Siti Rahmawati, dan Rina Wulandari tampil kembali bersama tiga baris manual

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 6 sampai 10 dan 12 sampai 16 adalah blok berulang dengan parameter pada Tabel Search kolom curated (enam iterasi) dan Tabel Filter kolom curated (lima iterasi); nominal 16 langkah, ekspansi 61. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #40), dan tiap iterasi berdiri sendiri karena Search dikosongkan dan Filter dibersihkan di akhir iterasi. Langkah yang diulang: 6 sampai 10 dan 12 sampai 16.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab, node, sub-tab, dan section (langkah 1, 2, 3); membuka Setup Column dan menyimpan (langkah 4); mengosongkan Search (langkah 9); membersihkan Filter (langkah 15).
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-1072 meminta rentang tanggal Temporary Until yang mencakup Nadia Putri dan rentang Joined Date yang mencakup Dimas Pranata saja; spec memakai tanggal dari fixture (Pre-setup #40 hanya menyebut Temporary Until Nadia sebagai "terisi" dan Joined Date `15/02/26` Dimas).
  - TC tidak menyebut apakah Filter Panel menutup sesudah `[Apply]`; spec mengasumsikan panel menutup dan dibuka ulang lewat ikon Filter.
  - Langkah Uji TC-FA-RP-1071 dan TC-FA-RP-1072 memakai Pre-setup #19 hanya sebagai precondition seed Role Transaksi; kolom data yang diasersi berasal dari Pre-setup #40.
