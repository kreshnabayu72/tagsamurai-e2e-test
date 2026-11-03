---
id: TC-FA-RP-E2E-144-tab-total-control-sort-2
title: "Tab Total Control: Sort (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-500
  - TC-FA-RP-501
  - TC-FA-RP-502
  - TC-FA-RP-1059
coverage:
  web: automated
---

# Tab Total Control: Sort (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; urutan Last Updated dari terlama ke terbaru: Admin Utama, Siti Rahmawati, Rina Wulandari, Ahmad Fauzi, Siti Rahayu, Eka Saputra, Budi Santoso, Fitri Handayani, Rudi Hartono), #37 (Tab Read Only empat baris), #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No` untuk Ahmad Fauzi dan Budi Santoso). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Default sort tabel: Name A-Z.
- Tabel Sort kolom tanggal dan curated (TC 500 dan TC 1059):

| Kolom | Ascending | Descending |
|---|---|---|
| Last Updated | Oldest First: Admin Utama, Siti Rahmawati, Rina Wulandari, Ahmad Fauzi, Siti Rahayu, Eka Saputra, Budi Santoso, Fitri Handayani, Rudi Hartono | Newest First (urutan terbalik) |
| Temporary Until | Rudi Hartono lebih dulu, lalu delapan baris tanpa nilai di akhir | delapan baris tanpa nilai di awal, lalu Rudi Hartono |
| Email | nilai email berurut A-Z | urutan terbalik |
| TAG | Ahmad Fauzi (`TAG-1001`) lebih dulu, lalu delapan baris tanpa nilai di akhir | delapan baris tanpa nilai di awal, lalu Ahmad Fauzi |
| Cost Center | Ahmad Fauzi (`CC-100`), Budi Santoso (`CC-200`), lalu tujuh baris tanpa nilai di akhir | tujuh baris tanpa nilai di awal, lalu Budi Santoso, Ahmad Fauzi |
| Joined Date | Oldest First: Ahmad Fauzi, Budi Santoso, lalu tujuh baris tanpa nilai di akhir | Newest First (Budi Santoso mendahului Ahmad Fauzi) |
| Badge No | Ahmad Fauzi (`BN-77`), Budi Santoso (`BN-88`), lalu tujuh baris tanpa nilai di akhir | tujuh baris tanpa nilai di awal, lalu Budi Santoso, Ahmad Fauzi |

## Test Steps

### Siklus tiga state kelas tanggal dan kolom curated (TC 500 dan TC 1059)

1. Tampilkan kolom Temporary Until, Email, TAG, Cost Center, Joined Date, dan Badge No lewat Setup Column, lalu klik `[Save]`.
2. Untuk setiap kolom pada Tabel Sort kolom tanggal dan curated, lakukan langkah 3 sampai 8.
3. Klik header kolom sekali.
4. Verifikasi baris terurut ascending sesuai kolom "Ascending" pada tabel.
5. Klik header kolom kedua kali.
6. Verifikasi baris terurut descending sesuai kolom "Descending" pada tabel.
7. Klik header kolom ketiga kali.
8. Verifikasi urutan kembali ke default sort tabel (Name A-Z).

### Baris bernilai sama mengikuti default sort (TC 501)

9. Klik header kolom Position sekali (Position ascending).
10. Verifikasi Fitri Handayani tampil sebelum Siti Rahmawati (keduanya `Finance Officer`; tie-breaker default sort Name A-Z).
11. Klik header kolom Position dua kali lagi hingga urutan kembali ke default sort tabel.

### Guard kolom non-sortable (TC 502)

12. Arahkan kursor ke header kolom Column Visibility `(⋯)`.
13. Verifikasi header tidak memiliki ikon sort.
14. Klik header kolom Column Visibility `(⋯)`.
15. Verifikasi klik hanya membuka overlay Column Visibility.
16. Tutup overlay dengan Esc.
17. Sembunyikan kolom Temporary Until, Email, TAG, Cost Center, Joined Date, dan Badge No lewat Setup Column, lalu klik `[Save]`.

## Notes

- Alasan di atas 35 langkah: langkah 3 sampai 8 (tujuh iterasi) adalah blok berulang dengan parameter pada tabel Prerequisites; seluruh blok berkelas fungsional sama, dataset sama, dan tiap kolom berdiri sendiri karena klik ketiga mengembalikan tabel ke default. Langkah yang diulang: 3 sampai 8. Tabel memuat kolom TC 500 (Last Updated, Temporary Until) dan TC 1059 (Email, TAG, Cost Center, Joined Date, Badge No).
- Langkah penghubung (S-03): langkah 1, 2, 3, 5, 7, 9, 11, 12, 14, 16, dan 17. Langkah 1 menampilkan kolom yang disembunyikan secara default; langkah 11 dan 17 memulihkan sort dan kolom (S-09).
- Temuan untuk QA:
  - TC 500 dan TC 1059 merinci urutan ascending; urutan descending dan posisi baris bernilai kosong hanya dirinci sebagian (TAG, Cost Center, Badge No, Temporary Until) sehingga asersi descending Last Updated, Email, dan Joined Date memakai pembalikan nilai kolom. Urutan sesama baris kosong tidak diasersi.
  - TC 501 tidak menyebut cara mengembalikan sort; spec menambah langkah 11.
