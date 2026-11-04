---
id: TC-FA-RP-E2E-180-tabel-role-transaksi-search-filter-dan-sort-4
title: "Tabel Role Transaksi: Search, Filter, dan Sort (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1073
  - TC-FA-RP-1106
coverage:
  web: automated
---

# Tabel Role Transaksi: Search, Filter, dan Sort (4/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #18 (pohon group), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab `Disposal`), #40 (tabel Role Transaksi section Asset Admin: Nadia Putri, Ahmad Fauzi, Dimas Pranata), dan #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No`). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Date Format General Settings (#34) tidak diubah spec ini; teks tanggal dicatat dari sel sesuai format yang berlaku.
- State yang diubah: konfigurasi kolom Setup Column tabel Role Transaksi (kolom curated ditampilkan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Header section `Asset Admin` memuat `6 users` (total seluruh baris termasuk tiga baris pola Admin Utama, Siti Rahmawati, Rina Wulandari; Pre-setup #19) dan tidak berubah oleh klik header kolom.
- Urutan default sort tabel (Name A-Z): Ahmad Fauzi, Dimas Pranata, Nadia Putri.
- Tabel Sort kolom curated (TC-FA-RP-1073; urutan di bawah adalah urutan relatif tiga baris manual; baris pola ikut tersortir menurut nilai kolomnya; descending adalah urutan ascending dibalik):

| Kolom | Urutan ascending |
|---|---|
| Email | Ahmad Fauzi, Dimas Pranata, Nadia Putri |
| Activation Status | `Activated` (Ahmad Fauzi, Dimas Pranata) lalu `Pending Activation` (Nadia Putri) |
| Temporary User | `No` (Ahmad Fauzi, Dimas Pranata) sebelum `Yes` (Nadia Putri) |
| Temporary Until | Oldest First: Nadia Putri lebih dulu lalu dua baris tanpa nilai di akhir (descending: Newest First) |
| TAG | Ahmad Fauzi (`TAG-1001`), Dimas Pranata (`TAG-2002`), lalu Nadia Putri tanpa nilai di akhir |
| Cost Center | Ahmad Fauzi (`CC-100`), Dimas Pranata (`CC-200`), lalu Nadia Putri tanpa nilai di akhir |
| Joined Date | Oldest First: Ahmad Fauzi, Dimas Pranata, lalu Nadia Putri tanpa nilai di akhir (descending: Newest First) |
| Badge No | Ahmad Fauzi (`BN-77`), Dimas Pranata (`BN-88`), lalu Nadia Putri tanpa nilai di akhir |

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
3. Buka section `Asset Admin`

### Sort siklus tiga state kolom curated (TC-FA-RP-1073)

4. Klik header `(⋯)` kolom Column Visibility pada section, klik `Setup Column...`, centang kolom `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, dan `Badge No`, lalu klik `[Save]`
5. Untuk setiap baris pada Tabel Sort kolom curated, lakukan langkah 6 sampai 14
6. Klik header kolom `<Kolom>` sekali
7. Verifikasi klik 1 ascending sesuai urutan pada tabel dan baris pola Admin Utama, Siti Rahmawati, serta Rina Wulandari tampil dan ikut tersortir menurut nilai kolomnya (urutan relatif tiga baris manual tidak berubah)
8. Verifikasi header section `Asset Admin` tetap `6 users` pada klik 1
9. Klik header kolom `<Kolom>` sekali lagi
10. Verifikasi klik 2 descending (urutan ascending dibalik) dan baris pola Admin Utama, Siti Rahmawati, serta Rina Wulandari tampil dan ikut tersortir menurut nilai kolomnya (urutan relatif tiga baris manual tidak berubah)
11. Verifikasi header section `Asset Admin` tetap `6 users` pada klik 2
12. Klik header kolom `<Kolom>` sekali lagi
13. Verifikasi klik 3 kembali ke default sort tabel (Name A-Z: Ahmad Fauzi, Dimas Pranata, Nadia Putri) dan baris pola Admin Utama, Siti Rahmawati, serta Rina Wulandari tampil dan ikut tersortir menurut nilai kolomnya (urutan relatif tiga baris manual tidak berubah)
14. Verifikasi header section `Asset Admin` tetap `6 users` pada klik 3

### Kolom Joined Date tidak dapat dicari (TC-FA-RP-1106)

15. Catat teks sel Joined Date baris Ahmad Fauzi
16. Ketik Search teks tanggal yang dicatat, tekan Enter
17. Verifikasi empty state `No results found` (kolom Custom Field bertipe Date tidak dapat dicari)
18. Klik ikon Filter pada section
19. Verifikasi Filter Panel memuat field `Joined Date` sebagai jalur penyaringan kolom tanggal
20. Tutup Filter Panel
21. Kosongkan isi kotak search, tekan Enter

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 6 sampai 14 adalah blok berulang dengan parameter pada Tabel Sort kolom curated (delapan iterasi); nominal 21 langkah, ekspansi 84. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #40), dan tiap iterasi berdiri sendiri karena siklus tiga klik mengembalikan sort ke default (S-09). Langkah yang diulang: 6 sampai 14.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab, node, sub-tab, dan section (langkah 1, 2, 3); membuka Setup Column dan menyimpan (langkah 4); klik header kolom (langkah 6, 9, 12); mencatat teks sel (langkah 15); menutup Filter Panel (langkah 20); mengosongkan Search (langkah 21).
- Kolom `Joined Date` sudah ditampilkan pada langkah 4, sehingga langkah "Tampilkan kolom Joined Date lewat Setup Column" TC-FA-RP-1106 tidak diulang.
- Temuan untuk QA:
  - TC tidak menyebut cara menutup Filter Panel tanpa `[Apply]`; spec menulis "Tutup Filter Panel" sebagai langkah penghubung.
