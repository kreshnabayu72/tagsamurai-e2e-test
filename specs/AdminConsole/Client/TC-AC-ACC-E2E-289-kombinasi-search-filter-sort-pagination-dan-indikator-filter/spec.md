---
id: TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter
title: "Client List: Kombinasi Search, Filter, Sort, dan Pagination, Indikator Tombol Filter, serta Independensi Pelepasan Kontrol"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-391
  - TC-AC-ACC-392
  - TC-AC-ACC-393
  - TC-AC-ACC-678
  - TC-AC-ACC-679
  - TC-AC-ACC-709
  - TC-AC-ACC-710
  - TC-AC-ACC-711
  - TC-AC-ACC-712
coverage:
  web: automated
---

# Client List: Kombinasi Search, Filter, Sort, dan Pagination, Indikator Tombol Filter, serta Independensi Pelepasan Kontrol

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 C-LST-1 sampai C-LST-3 (`PT Sortir Alfa` SRT-301 Healthcare, `PT Sortir Beta` SRT-100 Retail, `PT Sortir Gamma` SRT-200 Manufacturing) dan C-14 `PT Uji Halaman 01` sampai `PT Uji Halaman 30` (30 baris untuk pagination) tersedia dan hanya dibaca.
- Client Code Pre-setup yang diasersi: `GNM-013` (`PT Ganti Mitra`), `LJR-010` (`PT Lintas Jaringan`), `SJA-001` (`PT Sejahtera Abadi`), `SNR-011` (`PT Sinar Distributor`), `TMP-012` (`PT Timur Perkasa`).
- Kebutuhan data TC-AC-ACC-392: fixture residen A3 C-W3LST-7 (`PT Uji Halaman FAMS 01` sampai `06`, FAMS `Active`) tersedia dan hanya dibaca, sehingga hasil Search `PT` dengan Filter FAMS `Active` melebihi 10 baris (ukuran halaman default) dan halaman 2 berisi baris.
- Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Indikator tombol Filter (TC-AC-ACC-678 dan TC-AC-ACC-679)

1. Lihat tombol Filter pada toolbar List
2. Verifikasi tombol Filter berstatus default tanpa badge (belum ada filter ter-Apply)
3. Klik Filter, pilih FAMS `Active` dan `Grace`, lalu klik [Apply]
4. Verifikasi tombol Filter berstatus active dengan badge titik tanpa angka (satu field ter-Apply dengan dua nilai)
5. Klik Filter, pilih SAMS `Active` (FAMS `Active` dan `Grace` tetap terpilih), lalu klik [Apply]
6. Verifikasi tombol Filter tetap berstatus active dengan badge titik tanpa angka (tidak berubah menjadi angka)
7. Klik Filter, klik [Clear Field], lalu klik [Apply]
8. Klik Filter, pilih FAMS `Active`, lalu klik [Apply]
9. Ketik Search `PT Cahaya Baru`, tekan Enter
10. Verifikasi tombol Filter berstatus active dengan badge titik tanpa angka
11. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
12. Klik Filter, klik [Clear Field]
13. Verifikasi field FAMS kosong dengan placeholder `All statuses`
14. Klik [Apply]
15. Verifikasi tombol Filter berstatus default tanpa badge titik
16. Verifikasi baris `PT Cahaya Baru` tampil kembali
17. Klik `(←)` pada kotak Search

### Irisan Filter dan Search (TC-AC-ACC-709 dan TC-AC-ACC-710)

18. Klik Filter, pilih Partner `CV Mitra Sejati` dan FAMS `Active`, lalu klik [Apply]
19. Ubah ukuran halaman menjadi 100 baris
20. Verifikasi `PT Sejahtera Abadi`, `PT Lintas Jaringan`, dan `PT Ganti Mitra` tampil
21. Verifikasi `PT Teknologi Maju` (FAMS Grace), `PT Cahaya Baru` (FAMS Waiting for Approval), dan `PT Mulai Esok` (FAMS Pending) tidak tampil
22. Verifikasi `PT Timur Perkasa` (Partner CV Mitra Timur) tidak tampil
23. Klik Filter, klik [Clear Field], pilih FAMS `Active`, lalu klik [Apply]
24. Ketik Search `Sejati`, tekan Enter
25. Verifikasi `PT Sejahtera Abadi`, `PT Lintas Jaringan`, dan `PT Ganti Mitra` tampil (FAMS Active dan Managed By memuat `Sejati`)
26. Verifikasi `PT Teknologi Maju` tidak tampil karena filter FAMS tetap aktif
27. Verifikasi `PT Timur Perkasa` tidak tampil karena tidak cocok dengan Search
28. Verifikasi tombol Filter tetap berstatus active dengan badge titik tanpa angka
29. Klik Filter, klik [Clear Field], lalu klik [Apply], dan klik `(←)` pada kotak Search

### Mengosongkan Search saat Filter dan Sort aktif (TC-AC-ACC-711)

30. Klik Filter, pilih FAMS `Active`, lalu klik [Apply]
31. Ubah ukuran halaman menjadi 100 baris, lalu klik header kolom Client Code satu kali
32. Ketik Search `Sejati`, tekan Enter
33. Verifikasi `PT Ganti Mitra`, `PT Lintas Jaringan`, dan `PT Sejahtera Abadi` tampil (FAMS Active dan Managed By memuat `Sejati`)
34. Verifikasi urutan relatif Client Code ascending: `PT Ganti Mitra` (GNM-013), lalu `PT Lintas Jaringan` (LJR-010), lalu `PT Sejahtera Abadi` (SJA-001)
35. Klik ikon `✕` pada input Search, tekan Enter
36. Verifikasi `PT Sinar Distributor` dan `PT Timur Perkasa` (FAMS Active, Managed By bukan `Sejati`) tampil kembali
37. Verifikasi `PT Cahaya Baru` (FAMS Waiting for Approval) tetap tidak tampil
38. Verifikasi tombol Filter tetap berstatus active dengan badge titik tanpa angka
39. Verifikasi urutan relatif ascending Client Code tetap aktif: `PT Ganti Mitra` (GNM-013), `PT Lintas Jaringan` (LJR-010), `PT Sejahtera Abadi` (SJA-001), `PT Sinar Distributor` (SNR-011), `PT Timur Perkasa` (TMP-012)
40. Klik Filter, klik [Clear Field], klik [Apply], lalu klik header kolom Client Code dua kali sampai indikator sort nonaktif, dan klik `(←)` pada kotak Search

### Clear Field hanya mengosongkan filter (TC-AC-ACC-391)

41. Ketik Search `PT`, tekan Enter
42. Klik header kolom Client Code dua kali (Z-A)
43. Klik Filter, pilih FAMS `Active`, lalu klik [Apply]
44. Klik Filter lalu klik [Clear Field]
45. Verifikasi field filter FAMS kosong dengan placeholder `All statuses`
46. Verifikasi Search `PT` tetap menyaring: kotak Search masih berisi `PT` dan hasil Search tampil
47. Verifikasi sort Client Code descending tetap aktif
48. Klik [Apply], klik header kolom Client Code sampai indikator sort nonaktif, lalu klik `(←)` pada kotak Search

### Berpindah kolom sort saat Search dan Filter aktif (TC-AC-ACC-712)

49. Ketik Search `Sortir`, tekan Enter
50. Klik Filter, pilih Industry `Healthcare` dan `Retail`, lalu klik [Apply]
51. Verifikasi `PT Sortir Alfa` (Healthcare) dan `PT Sortir Beta` (Retail) tampil
52. Verifikasi `PT Sortir Gamma` (Manufacturing) tidak tampil
53. Klik header kolom Client Code satu kali
54. Verifikasi urutan `PT Sortir Beta` (SRT-100), lalu `PT Sortir Alfa` (SRT-301)
55. Klik header kolom Company Name satu kali
56. Verifikasi indikator sort Client Code nonaktif dan Company Name ascending aktif
57. Verifikasi urutan `PT Sortir Alfa`, lalu `PT Sortir Beta`
58. Verifikasi Search `Sortir` dan filter Industry tetap aktif: `PT Sortir Gamma` tetap tidak tampil
59. Klik Filter, klik [Clear Field], klik [Apply], lalu klik header kolom Company Name sampai indikator sort nonaktif, dan klik `(←)` pada kotak Search

### Kombinasi Search, Filter, Sort, dan Pagination serta reset ke halaman 1 (TC-AC-ACC-392 dan TC-AC-ACC-393)

60. Ketik Search `PT`, tekan Enter
61. Klik Filter, pilih FAMS `Active`, lalu klik [Apply]
62. Klik header kolom Company Name dua kali (Company Name Z-A)
63. Pindah ke halaman 2
64. Verifikasi halaman 2 memuat sedikitnya satu baris data (hasil Search `PT` dengan FAMS `Active` melebihi ukuran halaman 10)
65. Verifikasi hasil memenuhi semua kontrol (AND): baris pada halaman 2 mengandung `PT`, FAMS `Active`, urutan Company Name Z-A
66. Verifikasi Pagination mengikuti hasil (halaman 2 aktif)
67. Klik Filter, klik [Clear Field], klik [Apply], dan klik header kolom Company Name sampai indikator sort nonaktif, lalu klik `(←)` pada kotak Search
68. Pindah ke halaman 2 (30+ baris)
69. Ketik Search `Uji`, tekan Enter
70. Verifikasi paginasi kembali ke halaman 1
71. Klik `(←)` pada kotak Search

## Notes

- Urutan blok tidak mengikuti urutan nomor TC: blok indikator (678, 679) lebih dulu; blok TC-AC-ACC-392/393 di akhir karena memakai pagination/`Search PT` (S-10); langkah penghubung `[Clear Field]`/`[Apply]` dan `(←)` mereset state antar blok (S-09, S-03).
- Spec melewati sekitar 35 langkah; alasan: seluruh blok satu kelas harness dan satu dataset (kombinasi kontrol List), blok berurutan tanpa state bersama dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Sort `Client Code Z-A` pada TC-AC-ACC-391 diwujudkan sebagai dua klik header Client Code (ascending lalu descending) mengikuti siklus 3 state.
- Temuan untuk QA
  - TC-AC-ACC-391: Langkah 1 menulis `Search PT, sort Client Code Z-A, terapkan filter` tanpa nilai filter; spec memakai FAMS `Active`. Expected tidak menyebut sort/search diverifikasi lewat baris mana; spec memakai kolom Client Code descending dan Search `PT` sebagai petunjuk.
  - TC-AC-ACC-392: Data Uji kosong dan Expected hanya `Hasil memenuhi semua kontrol (AND)`; spec menurunkan verifikasi dari Langkah (Search `PT`, FAMS `Active`, Company Name Z-A, halaman 2). Kebutuhan data halaman 2 kini dijamin Precondition d TC-AC-ACC-392 (fixture residen C-W3LST-7); spec ini mengikuti Precondition tersebut.
  - TC-AC-ACC-393: `Pindah ke halaman 2 (30+ baris)` bergantung pada C-14 (30 baris `PT Uji Halaman`); precondition TC tidak menyebut C-14 secara eksplisit.
