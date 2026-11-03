---
id: TC-FA-LIC-E2E-078-active-sessions-search-terikat-visibilitas-search
title: "Active Sessions: Search dan Sort Terikat Visibilitas Kolom, Kolom Curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-266
  - TC-FA-LIC-267
  - TC-FA-LIC-514
  - TC-FA-LIC-515
  - TC-FA-LIC-516
coverage:
  web: automated
---

# Active Sessions: Search dan Sort Terikat Visibilitas Kolom, Kolom Curated

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #26 (fixture tabel sesi, dipulihkan fixture BE di hook `before`): tepat lima sesi cuplikan pada client Paid Pre-setup #1; Online Users 5/25. Profil Curated: Rudi Hartono Activated, TAG-001; Dewi Lestari Activated, Temporary User Yes sampai 31/12/26; Andi Pratama Pending Activation; Siti Rahma Activated, TAG-014; Budi Santoso Activated. Pengguna selain Dewi Lestari bukan user temporary (Temporary User `No`); TAG hanya Rudi Hartono dan Siti Rahma. Urutan default (Login Time terbaru lebih dulu): Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso. Kolom Curated (`Activation Status`, `Temporary User`, `Temporary Until`, `TAG`) Hidden secara default. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.*` (berkas fixture belum ada, disiapkan tim FE); nilai pada langkah dan tabel di bawah adalah nilai fixture itu.
- Data Dinamis: tidak ada. Spec ini tidak mengubah data sesi.
- Tabel "Sort kolom Curated alfabetis" (parameter langkah 29 sampai 34); klik 3 selalu kembali ke urutan default:

  | Kolom | Klik 1 (Ascending `↑`) | Klik 2 (Descending `↓`) |
  |---|---|---|
  | Activation Status | Rudi Hartono, Dewi Lestari, Siti Rahma, Budi Santoso, Andi Pratama | Andi Pratama, Rudi Hartono, Dewi Lestari, Siti Rahma, Budi Santoso |
  | Temporary User | Rudi Hartono, Andi Pratama, Siti Rahma, Budi Santoso, Dewi Lestari | Dewi Lestari, Rudi Hartono, Andi Pratama, Siti Rahma, Budi Santoso |
  | TAG | Rudi Hartono, Siti Rahma, Dewi Lestari, Andi Pratama, Budi Santoso (nilai kosong `—` di akhir) | Dewi Lestari, Andi Pratama, Budi Santoso, Siti Rahma, Rudi Hartono (nilai kosong `—` di awal) |

- Konfigurasi kolom (visibilitas) yang diubah spec ini tersimpan di browser; hook `after` menghapus preferensi kolom di browser (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26; pemulihan konfigurasi kolom.

## Test Steps

### TC-FA-LIC-266: Search terikat visibilitas kolom IP Address

1. Klik tab Concurrent User
2. Ketik Search `198.51.100`, tekan Enter
3. Verifikasi tabel menampilkan: Rudi Hartono, Andi Pratama
4. Klik header kolom Actions `⋯`, lalu hilangkan centang `IP Address` pada overlay Column Visibility
5. Verifikasi kolom `IP Address` hilang dari tabel
6. Ganti isi kotak search dengan `198.51.100`, tekan Enter
7. Verifikasi pencarian `198.51.100` tidak mencocokkan baris melalui kolom itu: tabel menampilkan empty state `No results found`
8. Klik header kolom Actions `⋯`, lalu centang kembali `IP Address`
9. Ganti isi kotak search dengan `198.51.100`, tekan Enter
10. Verifikasi hasil kembali seperti awal: Rudi Hartono, Andi Pratama
11. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-267: Search kolom Curated hanya mencocokkan setelah kolom ditampilkan

12. Ketik Search `TAG-014`, tekan Enter
13. Verifikasi tabel menampilkan empty state `No results found`
14. Klik header kolom Actions `⋯`, lalu centang `TAG` pada overlay Column Visibility
15. Ganti isi kotak search dengan `TAG-014`, tekan Enter
16. Verifikasi tabel menampilkan: Siti Rahma
17. Klik header kolom Actions `⋯`, lalu centang `Activation Status`
18. Ganti isi kotak search dengan `Pending`, tekan Enter
19. Verifikasi tabel menampilkan: Andi Pratama
20. Kosongkan isi kotak search, tekan Enter
21. Verifikasi badge `Activated` pada Rudi Hartono, Dewi Lestari, Siti Rahma, dan Budi Santoso bersverity `success`
22. Verifikasi badge `Pending Activation` pada Andi Pratama bersverity `warning`

### TC-FA-LIC-514: Search kolom Curated Temporary User dan guard kolom tanggal Temporary Until

23. Klik header kolom Actions `⋯`, lalu centang `Temporary User` dan `Temporary Until`
24. Ketik Search `Yes`, tekan Enter
25. Verifikasi tabel menampilkan: Dewi Lestari
26. Ganti isi kotak search dengan `31/12/26`, tekan Enter
27. Verifikasi tabel menampilkan empty state `No results found` (kolom tanggal tidak dicari; penyaringan lewat Filter Panel)
28. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-515: Sort kolom Curated alfabetis, siklus 3-state

29. Untuk setiap baris tabel "Sort kolom Curated alfabetis" (langkah 29 sampai 34): klik header kolom pada baris itu sekali
30. Verifikasi urutan baris klik 1 sesuai tabel dengan indikator `↑`
31. Klik header kolom yang sama sekali lagi
32. Verifikasi urutan baris klik 2 sesuai tabel dengan indikator `↓`
33. Klik header kolom yang sama sekali lagi
34. Verifikasi urutan kembali ke default: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso

### TC-FA-LIC-516: Sort kolom Curated tanggal Temporary Until, siklus 3-state

35. Klik header kolom `Temporary Until` sekali
36. Verifikasi urutan klik 1 `↑`: Dewi Lestari, Rudi Hartono, Andi Pratama, Siti Rahma, Budi Santoso (nilai kosong `—` di akhir)
37. Klik header kolom `Temporary Until` sekali lagi
38. Verifikasi urutan klik 2 `↓`: Rudi Hartono, Andi Pratama, Siti Rahma, Budi Santoso, Dewi Lestari (nilai kosong `—` di awal)
39. Klik header kolom `Temporary Until` sekali lagi
40. Verifikasi urutan kembali ke default: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso

## Notes

- Langkah penghubung tanpa `Verifikasi`: mengosongkan Search di akhir tiap blok (S-09) dan mengubah visibilitas kolom lewat overlay Column Visibility yang diterapkan langsung tanpa `[Save]`. Kolom `TAG`, `Activation Status`, `Temporary User`, dan `Temporary Until` yang ditampilkan pada TC-FA-LIC-267 dan TC-FA-LIC-514 tetap tampil untuk TC-FA-LIC-515 dan TC-FA-LIC-516, sehingga langkah "Tampilkan kolom" milik kedua TC itu sudah tercakup.
- Blok ulang: langkah 29 sampai 34 dijalankan 3 kali (spec ini melewati sekitar 35 langkah, nominal dan setelah ekspansi). Alasan: seluruh blok memakai kolom Curated yang harus ditampilkan lewat Column Visibility pada satu tabel, satu dataset Pre-setup #26, dan satu kelas harness (fungsional), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Search tidak diganti antar-TC lewat navigasi sidebar karena kolom yang ditampilkan perlu dipertahankan.
- Temuan untuk QA: pada TC-FA-LIC-266 butir b, Expected bersyarat ("empty state `No results found` bila tidak ada kolom lain yang cocok"). Pada data Pre-setup #26 tidak ada kolom lain yang memuat `198.51.100`, sehingga spec mengasersi empty state. TC-FA-LIC-515 dan TC-FA-LIC-516 berjudul Sort tetapi dikelompokkan di spec ini karena memakai kolom Curated yang harus ditampilkan lewat Column Visibility.
