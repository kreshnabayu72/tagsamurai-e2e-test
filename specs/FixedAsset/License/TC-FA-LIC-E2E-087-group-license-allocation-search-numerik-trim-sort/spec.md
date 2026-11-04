---
id: TC-FA-LIC-E2E-087-group-license-allocation-search-numerik-trim-sort
title: "Group License Allocation: Sort Default, Search Trim dan Numerik, Sort Alfabetis, dan Perpindahan Kolom Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-303
  - TC-FA-LIC-304
  - TC-FA-LIC-305
  - TC-FA-LIC-307
  - TC-FA-LIC-308
  - TC-FA-LIC-511
coverage:
  web: automated
---

# Group License Allocation: Sort Default, Search Trim dan Numerik, Sort Alfabetis, dan Perpindahan Kolom Sort

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`): client Paid Pre-setup #1 dengan `License allocation per group` ON; hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan. Tabel Group License Allocation pada node All Groups menampilkan empat baris level 1; urutan default Used by This Group tertinggi: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki` (belum ada, disiapkan tim FE); nilai pada langkah dan tabel di bawah adalah nilai fixture itu.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Tabel "Search numerik tambahan" (parameter langkah 12 sampai 14):

  | Kolom | Kata kunci | Baris yang tampil |
  |---|---|---|
  | Allocated to Subgroups | `600` | Kantor Pusat |
  | + Audit | `10` | Cabang Medan, Cabang Surabaya, Kantor Pusat (Kantor Pusat cocok hanya melalui + Audit 10) |
  | + Repair Ticketing | `3` | Cabang Medan |
  | + Maps | `40` | Produksi (cocok melalui + IT Inventory 40; kolom + Maps bernilai `—` pada semua baris sehingga tidak menambah baris) |

- Tabel "Sort alfabetis" (parameter langkah 15 sampai 20); klik 3 selalu kembali ke urutan default Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat:

  | Kolom | Klik 1 (Ascending `↑`) | Klik 2 (Descending `↓`) |
  |---|---|---|
  | Group Name | Cabang Medan, Cabang Surabaya, Kantor Pusat, Produksi | Produksi, Kantor Pusat, Cabang Surabaya, Cabang Medan |
  | Group Code | Kantor Pusat, Cabang Medan, Produksi, Cabang Surabaya | Cabang Surabaya, Produksi, Cabang Medan, Kantor Pusat |

- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12.

## Test Steps

### TC-FA-LIC-307: Sort default, Used by This Group tertinggi lebih dulu

1. Klik tab Allocation Quota di node All Groups
2. Verifikasi urutan awal tanpa mengklik header (Used by This Group tertinggi lebih dulu): Produksi (1450), Cabang Medan (880), Cabang Surabaya (780), Kantor Pusat (700)
3. Verifikasi indikator sort aktif pada kolom `Used by This Group`

### TC-FA-LIC-303: Spasi tepi di-trim saat Enter, spasi tengah dipertahankan, tidak case-sensitive

4. Ketik Search `  MEDAN  `, tekan Enter
5. Verifikasi tabel menampilkan: Cabang Medan
6. Verifikasi isi kotak Search di layar tetap `  MEDAN  ` (spasi tepi tetap terlihat)

### TC-FA-LIC-304: Search numerik, pemisah ribuan bukan bagian pencocokan

7. Ganti isi kotak search dengan `1,500`, tekan Enter
8. Verifikasi `1,500` tidak menemukan baris: tabel menampilkan empty state `No results found`
9. Ganti isi kotak search dengan `1500`, tekan Enter
10. Verifikasi `1500` menampilkan: Produksi, Kantor Pusat
11. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-511: Search numerik per kelas kolom Allocated to Subgroups, + Audit, + Repair Ticketing, + Maps

12. Untuk setiap baris tabel "Search numerik tambahan" (langkah 12 sampai 14): ketik Search kata kunci pada baris itu, tekan Enter
13. Verifikasi tabel menampilkan tepat baris yang tercantum pada kolom "Baris yang tampil" untuk baris tabel itu
14. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-305: Sort siklus 3-state per kelas kolom alfabetis (Group Name, Group Code)

15. Untuk setiap baris tabel "Sort alfabetis" (langkah 15 sampai 20): klik header kolom pada baris itu sekali
16. Verifikasi urutan baris klik 1 sesuai tabel dengan indikator `↑`
17. Klik header kolom yang sama sekali lagi
18. Verifikasi urutan baris klik 2 sesuai tabel dengan indikator `↓`
19. Klik header kolom yang sama sekali lagi
20. Verifikasi urutan kembali ke default: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat

### TC-FA-LIC-308: Berpindah kolom mereset kolom sebelumnya dan tidak menghapus Search

21. Klik header `Group Name` sekali
22. Klik header `+ IT Inventory` sekali
23. Verifikasi kolom `Group Name` kembali netral (indikator sort tidak aktif)
24. Verifikasi kolom `+ IT Inventory` memulai dari Ascending (`↑`)
25. Ketik Search `GRP-`, tekan Enter
26. Klik header `+ IT Inventory` sekali lagi untuk mengubah arah sort
27. Verifikasi kata kunci Search `GRP-` tidak direset: kotak Search tetap berisi `GRP-` dan tabel tetap tersaring
28. Klik header `+ IT Inventory` sekali lagi hingga netral, lalu kosongkan isi kotak search, tekan Enter

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 14 (mengosongkan Search antar iterasi, S-09), mengosongkan Search di akhir TC-FA-LIC-304 dan TC-FA-LIC-308, dan mengembalikan sort ke netral di akhir TC-FA-LIC-308. Pada TC-FA-LIC-303 dan TC-FA-LIC-304 kotak Search masih terbuka dari langkah sebelumnya sehingga isinya diganti, bukan dibuka ulang.
- Blok ulang: langkah 12 sampai 14 dijalankan 4 kali dan langkah 15 sampai 20 2 kali. Spec di atas 35 langkah (28 langkah nominal; 43 langkah setelah ekspansi). Alasan: seluruh blok adalah Search atau Sort satu tabel dengan satu dataset Pre-setup #12 dan satu kelas harness, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-FA-LIC-308 tidak menyebut hasil tabel setelah Search `GRP-`; spec mengasersi kotak Search tetap berisi `GRP-` dan tabel tetap tersaring tanpa daftar baris.
