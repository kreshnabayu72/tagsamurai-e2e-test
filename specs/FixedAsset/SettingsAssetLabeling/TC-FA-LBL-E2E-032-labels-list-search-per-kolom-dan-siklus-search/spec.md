---
id: TC-FA-LBL-E2E-032-labels-list-search-per-kolom-dan-siklus-search
title: "Labels List: Search per kolom dan siklus Search"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-01/search-cycle
  - FALB:obl/T-ALB-01/search/FLD-01
  - FALB:obl/T-ALB-01/search/FLD-02
  - FALB:obl/T-ALB-01/search/FLD-04
  - FALB:global-table-rules/search
coverage:
  web: automated
---

# Labels List: Search per kolom dan siklus Search

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-56` (12 label bersuffix `Lst-{runId}-032-01` sampai `Lst-{runId}-032-12`, Modified By dari dua pelaku, kode hex tiap label berbeda). `DU-58` (kata kunci Search tanpa hasil, `zzz-{runId}-032`). `DU-31` (akun Total Control kedua, env `FA_TC2_EMAIL`, `FA_TC2_PASSWORD`) dipakai hanya sebagai pelaku kedua lewat sesi API saat seeding sebagian label `DU-56`; tidak login di UI.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset.
- Jeda nyata: satu langkah menunggu 1 detik (langkah 35), pilihan spec ini untuk memberi kesempatan debounce bila ada.
- State global: tidak ada yang diubah. Hook `after` menghapus label seed `DU-56` lewat sesi API.

## Test Steps

1. Ketik Search `DU-56` (nama dasar `Lst-{runId}-032`), tekan Enter
2. Verifikasi Labels List menampilkan 10 baris label `DU-56` di halaman pertama
3. Pindah ke halaman 2 pada Pagination
4. Verifikasi halaman 2 aktif menampilkan sisa 2 baris label `DU-56`

### FALB:obl/T-ALB-01/search-cycle: Siklus Search

5. Ganti isi kotak search dengan `DU-58`, tanpa menekan Enter
6. Verifikasi ikon `✕` tampil di dalam kotak Search
7. Verifikasi Labels List masih menampilkan 2 baris label `DU-56` di halaman 2 (belum tersaring)
8. Tekan Enter
9. Verifikasi empty state Labels List menampilkan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
10. Klik `✕` pada kotak Search
11. Verifikasi kotak Search kosong dan tetap terbuka dengan kursor fokus
12. Verifikasi empty state Labels List masih tampil (tabel belum direset)
13. Tekan Enter pada kotak Search kosong
14. Verifikasi Labels List kembali menampilkan sedikitnya satu baris data dan empty state tidak tampil
15. Ganti isi kotak search dengan `DU-56` (nama dasar `Lst-{runId}-032`), tekan Enter
16. Pindah ke halaman 2 pada Pagination
17. Ganti isi kotak search dengan nama label ke-01 `DU-56`, tekan Enter
18. Verifikasi halaman 1 aktif dan baris label ke-01 `DU-56` tampil
19. Ganti isi kotak search dengan `DU-58`, tekan Enter
20. Klik `(←)` di sisi kiri toolbar
21. Verifikasi kotak Search menutup menjadi ikon Search
22. Verifikasi Labels List langsung menampilkan sedikitnya satu baris data tanpa empty state

### FALB:obl/T-ALB-01/search/FLD-01: Search menemukan baris lewat kolom Label

23. Ketik Search potongan tengah nama label ke-02 `DU-56`, tekan Enter
24. Verifikasi baris label ke-02 `DU-56` tampil di Labels List

### FALB:obl/T-ALB-01/search/FLD-02: Search menemukan baris lewat kolom Color Hex

25. Ganti isi kotak search dengan kode hex yang tampil pada baris label ke-01 `DU-56`, tekan Enter
26. Verifikasi baris label ke-01 `DU-56` tampil di Labels List

### FALB:obl/T-ALB-01/search/FLD-04: Search menemukan baris lewat kolom Modified By

27. Ganti isi kotak search dengan nama lengkap user `DU-31`, tekan Enter
28. Verifikasi baris `DU-56` yang dimodifikasi `DU-31` tampil di Labels List
29. Verifikasi baris `DU-56` yang dimodifikasi `DU-01` tidak tampil di Labels List

### FALB:global-table-rules/search: Cakupan, huruf besar-kecil, placeholder, dan submit via Enter

30. Ganti isi kotak search dengan nama label ke-01 `DU-56` dalam huruf kapital semua, tekan Enter
31. Verifikasi baris label ke-01 `DU-56` tampil di Labels List
32. Klik `✕` pada kotak Search
33. Verifikasi kotak Search kosong menampilkan placeholder `Search label name, color hex...`
34. Ganti isi kotak search dengan `DU-58`, tanpa menekan Enter
35. Tunggu 1 detik tanpa menekan Enter
36. Verifikasi Labels List masih menampilkan baris label ke-01 `DU-56` tanpa empty state (pencarian tidak berjalan sebelum Enter dan tanpa debounce)
37. Klik `(←)` di sisi kiri toolbar

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit tabel ke label `DU-56`, R-16), langkah 3 dan 16 (pindah halaman untuk menyiapkan keadaan halaman lebih dari 1), langkah 37 (menutup kotak Search sebelum cleanup). Langkah 15 mengembalikan tabel ke 12 baris label `DU-56` sebelum langkah 16.
- Anchor positif (bagian 8b butir 2): langkah 4 membuktikan Labels List sudah termuat sebelum langkah 9 mengasersi hasil kosong; langkah 28 menjadi anchor langkah 29; langkah 31 menjadi anchor langkah 36.
- Kolom Last Updated bukan kolom Search (kolom bertipe tanggal dikecualikan, `prd-conventions.md` §9.1a) dan tidak diasersi di spec ini.
- Search `Modified By` pada langkah 27 memakai nama lengkap user `DU-31` (bukan format tampilan `[First Name] [Last Initial]`), sesuai PRD §4.1.1 Tabel 1 `FLD-04`.
- Spec ini di atas smell 35 langkah (37 langkah). Alasan dipertahankan: seluruh blok satu kelas harness (Search) pada dataset `DU-56` yang sama; setiap blok dimulai dengan mengganti isi kotak search sehingga tidak bergantung pada hasil blok sebelumnya, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
