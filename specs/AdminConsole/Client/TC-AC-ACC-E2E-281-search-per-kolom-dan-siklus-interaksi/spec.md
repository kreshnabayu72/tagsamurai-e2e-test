---
id: TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi
title: "Search Client List: Siklus Interaksi, Pencarian per Kolom, Kolom Last Updated Tidak Dicari, dan Input Literal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-373
  - TC-AC-ACC-717
  - TC-AC-ACC-356
  - TC-AC-ACC-357
  - TC-AC-ACC-358
  - TC-AC-ACC-359
  - TC-AC-ACC-360
  - TC-AC-ACC-361
  - TC-AC-ACC-362
  - TC-AC-ACC-363
  - TC-AC-ACC-364
  - TC-AC-ACC-372
  - TC-AC-ACC-374
coverage:
  web: automated
---

# Search Client List: Siklus Interaksi, Pencarian per Kolom, Kolom Last Updated Tidak Dicari, dan Input Literal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Tabel parameter Search per kolom (dipakai langkah 29 sampai 31):

  | Sub-tab | Kolom | Kata kunci | Baris yang tampil |
  |---|---|---|---|
  | Active | Company Name | `sejahtera` | `PT Sejahtera Abadi` |
  | Active | Client Code | `tkm-002` | `PT Teknologi Maju` |
  | Active | PIC Name | `rina` | baris Client dengan PIC Rina |
  | Active | Managed By | `mitra lestari` | `PT Teknologi Maju` |
  | Active | Group | `menteng` | baris Client ber-Group Cabang Menteng (C-09 `PT Baru Daftar`) |
  | Active | FAMS | `grace` | `PT Teknologi Maju` |
  | Active | SIEM | `active` | `PT Sejahtera Abadi` |
  | Active | Modified By | `andi` | baris Client terakhir diubah Andi |
  | Suspended | SAMS | `archive` | `PT Wahana Nusantara` (C-03 berstatus Suspended) |

- Ukuran halaman 10 (default); keyword Search tidak dipakai ulang antar kolom tanpa langkah ganti isi kotak search.
- Tidak ada data yang dibuat atau diubah spec ini; tidak butuh klien HTTP, intercept, atau jam server. Tidak ada preferensi Setup Column yang diubah.

## Test Steps

### Siklus interaksi Search (TC-AC-ACC-373 dan TC-AC-ACC-717)

1. Ubah ukuran halaman menjadi 100 baris, lalu catat nama Client pada baris pertama dan baris terakhir yang tampil (baseline)
2. Arahkan kursor ke ikon Search di toolbar
3. Verifikasi tooltip `Search` tampil
4. Klik ikon Search
5. Verifikasi input Search terbuka dengan fokus otomatis
6. Verifikasi placeholder input Search `Search by company name, client code, or PIC name...`
7. Ketik `Sejati` tanpa menekan Enter
8. Verifikasi ikon `✕` muncul di dalam input Search
9. Verifikasi tabel belum tersaring: baris pertama dan baris terakhir yang tampil sama dengan baseline
10. Tekan Enter
11. Verifikasi tabel tersaring: `PT Sejahtera Abadi` tampil
12. Verifikasi `PT Timur Perkasa` tidak tampil
13. Klik ikon `✕` pada input Search
14. Verifikasi teks input terhapus dan kembali ke placeholder
15. Verifikasi input Search tetap terbuka
16. Verifikasi tabel masih menampilkan hasil Search terakhir: `PT Sejahtera Abadi` tampil dan `PT Timur Perkasa` tidak tampil
17. Tekan Enter pada input yang kosong
18. Verifikasi tabel direset: baris pertama dan baris terakhir yang tampil sama dengan baseline
19. Ketik Search `Sejati`, tekan Enter
20. Klik ikon panah kembali `(←)` di kiri toolbar
21. Verifikasi input Search menutup menjadi ikon Search
22. Verifikasi keyword Search kosong
23. Verifikasi tabel langsung direset tanpa menekan Enter: baris pertama dan baris terakhir yang tampil sama dengan baseline
24. Klik ikon Search, ketik `Sejati` tanpa menekan Enter (Search autofocus dan submit via Enter; TC-AC-ACC-373)
25. Verifikasi hasil tabel tidak berubah sebelum Enter: baris pertama dan baris terakhir yang tampil sama dengan baseline
26. Tekan Enter
27. Verifikasi hasil berubah setelah Enter: `PT Timur Perkasa` tidak tampil
28. Klik ikon panah kembali `(←)` di kiri toolbar

### Pencarian per kolom (TC-AC-ACC-356 sampai TC-AC-ACC-364)

29. Untuk setiap baris tabel parameter Search per kolom di Prerequisites: klik sub-tab sesuai kolom Sub-tab, lalu ketik Search kata kunci kolom itu (huruf kecil, tanpa debounce), tekan Enter
30. Verifikasi baris yang cocok pada kolom tersebut tampil (sesuai tabel parameter)
31. Verifikasi pencarian tidak membedakan huruf besar-kecil: kata kunci berhuruf kecil cocok dengan nilai kolom berhuruf kapital pada baris yang tampil
32. Klik sub-tab Active, lalu klik `(←)` pada kotak Search

### Kolom Last Updated tidak dicari (TC-AC-ACC-372)

33. Catat teks sel Last Updated baris `PT Sejahtera Abadi`
34. Ketik Search teks tanggal Last Updated yang dicatat, tekan Enter
35. Verifikasi tidak ada baris cocok: empty state `No results found` tampil
36. Klik `(←)` pada kotak Search

### Input diperlakukan sebagai teks literal (TC-AC-ACC-374)

37. Ketik Search `%' OR 1=1 --`, tekan Enter
38. Verifikasi tidak ada error: tidak ada toast error dan halaman tetap tampil
39. Verifikasi hasil kosong dengan empty state `No results found`
40. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
41. Verifikasi tidak ada eksekusi script: tidak ada dialog alert
42. Verifikasi hasil kosong dengan empty state `No results found`
43. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): pemilihan sub-tab, `(←)` pada kotak Search, dan ubah ukuran halaman menjadi 100 adalah langkah pemulihan/penghubung tanpa asersi. Baseline baris pertama dan terakhir dicatat sebelum aksi Search (S-12/S-14).
- Langkah 29 sampai 31 diulang per baris tabel parameter (9 iterasi; satu `Verifikasi` per klausa Expected tiap iterasi). Spec melewati sekitar 35 langkah setelah ekspansi; alasan: seluruh blok satu kelas harness (Search List, dataset Pre-setup sama, tanpa state yang dibangun antar blok) dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- P-5: TC-AC-ACC-374 (injeksi SQL/XSS lewat input Search, kelas a) adalah satu-satunya objek uji ringan kelas a/b/h di spec ini; dijalankan lewat UI, bukan request langsung, sehingga tidak ada butir K-1. Penjaga empty state `No results found` pada TC-AC-ACC-374 mengikuti judul empty state pada TC-AC-ACC-372 karena Expected TC-AC-ACC-374 hanya menyebut `empty state`.
- Temuan untuk QA
  - TC-AC-ACC-358: Expected menyebut `Client dengan PIC Rina` tanpa nama Client; precondition tidak menyebut Client mana yang ber-PIC Rina. Spec memakai deskripsi TC apa adanya.
  - TC-AC-ACC-364: Expected menyebut `Client terakhir diubah Andi` tanpa nama Client; spec memakai deskripsi TC apa adanya.
  - TC-AC-ACC-362: kata kunci `archive` pada kolom SAMS menunjuk `PT Wahana Nusantara` (C-03) yang berstatus Suspended (sub-tab Suspended), tetapi Langkah TC tidak menyebut sub-tab; spec menambah langkah penghubung klik sub-tab Suspended.
  - TC-AC-ACC-360: Expected menyebut `Client berGroup Cabang Menteng` tanpa nama; spec memakai C-09 `PT Baru Daftar` sebagai contoh dari Tabel A.
  - TC-AC-ACC-373: Langkah `Ketik tanpa Enter` tidak menyebut keyword; spec memakai `Sejati` sama seperti TC-AC-ACC-717.
