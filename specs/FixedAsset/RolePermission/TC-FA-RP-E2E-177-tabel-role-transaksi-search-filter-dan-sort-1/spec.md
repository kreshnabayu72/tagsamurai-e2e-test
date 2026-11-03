---
id: TC-FA-RP-E2E-177-tabel-role-transaksi-search-filter-dan-sort-1
title: "Tabel Role Transaksi: Search, Filter, dan Sort (1/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-593
  - TC-FA-RP-594
  - TC-FA-RP-595
coverage:
  web: automated
---

# Tabel Role Transaksi: Search, Filter, dan Sort (1/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`, section Asset Admin: Nadia Putri, Ahmad Fauzi, Dimas Pranata) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Tabel Search per kelas teks (TC-FA-RP-594):

| Kolom | Keyword | Baris yang tampil |
|---|---|---|
| Name | `nadia` | hanya Nadia Putri |
| Position | `CUSTOD` | hanya Ahmad Fauzi |
| Division | `it op` | hanya Dimas Pranata |

## Test Steps

### Siklus interaksi Search toolbar (TC-FA-RP-593)

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
3. Buka section `Asset Admin`
4. Hover ikon Search di toolbar
5. Verifikasi tooltip `Search`
6. Klik ikon Search
7. Verifikasi kotak Search melebar dan kursor otomatis fokus di input
8. Verifikasi placeholder input `Search name, position, division...`
9. Ketik `nadia` tanpa menekan Enter
10. Verifikasi ikon `(✕)` muncul di dalam input
11. Verifikasi tabel belum tersaring (ketiga baris section Asset Admin tetap tampil)
12. Tekan Enter
13. Verifikasi tabel tersaring: hanya baris Nadia Putri
14. Klik ikon `(✕)` pada kotak Search
15. Verifikasi teks input terhapus
16. Verifikasi kotak Search tetap terbuka dan kursor tetap fokus
17. Verifikasi tabel tetap menampilkan hasil pencarian terakhir
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali menampilkan seluruh data
20. Ketik Search `nadia`, tekan Enter
21. Klik ikon `(←)`
22. Verifikasi kotak Search menutup
23. Verifikasi keyword dikosongkan
24. Verifikasi tabel langsung kembali ke seluruh data

### Search per kelas teks: substring dan tidak case-sensitive (TC-FA-RP-594)

25. Untuk setiap baris pada Tabel Search per kelas teks, lakukan langkah 26 sampai 28
26. Ketik Search `<Keyword>`, tekan Enter
27. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel
28. Kosongkan isi kotak search, tekan Enter

### Screening Filter Panel (TC-FA-RP-595)

29. Klik ikon Filter
30. Verifikasi Filter Panel section Asset Admin memuat field `Position` (`All positions`) dan `Division` (`All divisions`)
31. Verifikasi Filter Panel memuat field curated `Activation Status`, `Temporary User`, `Temporary Until`, `Cost Center` (multi-select searchable), dan `Joined Date` (date range picker, `Select date`)
32. Verifikasi `Badge No` dan `Name` tidak punya field filter
33. Verifikasi footer Filter Panel memuat `[Clear Field]` dan `[Apply]`
34. Tutup Filter Panel

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 26 sampai 28 adalah blok berulang dengan parameter pada Tabel Search per kelas teks (tiga iterasi); nominal 34 langkah, ekspansi 40. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #40), dan tiap iterasi berdiri sendiri karena Search dikosongkan di akhir iterasi. Langkah yang diulang: 26 sampai 28.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab, node, sub-tab, dan section (langkah 1, 2, 3); hover dan klik ikon Search (langkah 4, 6); mengosongkan Search (langkah 28); langkah 20 membangun state hasil pencarian sebelum `(←)`; membuka dan menutup Filter Panel (langkah 29, 34).
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - Langkah Uji TC-FA-RP-593 sampai TC-FA-RP-595 tidak menyebut section yang dibuka, sedangkan judul menyebut section Asset Admin; spec membuka section `Asset Admin` (langkah 3) seperti Langkah Uji TC-FA-RP-1071.
  - TC-FA-RP-593 Expected g ("keyword dikosongkan") tidak menyebut cara mengamati keyword pada kotak Search yang menutup; spec mengasersi bahwa kotak yang tertutup tidak lagi memuat `nadia` (langkah 23).
  - TC-FA-RP-595 Expected a menyebut kolom `Badge No` dan `Name` tanpa field filter; spec mengasersi ketiadaan field itu pada panel.
