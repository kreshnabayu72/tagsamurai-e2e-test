---
id: TC-FA-FAAL-E2E-069-interaksi-search-filter-sort-kombinasi-irisan-tab-session
title: "Kombinasi Filter, Search, Sort, dan Ukuran Halaman Tab Session: Pelepasan Kontrol dan Pindah Kolom Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-92
  - TC-FA-FAAL-93
  - TC-FA-FAAL-94
  - TC-FA-FAAL-95
coverage:
  web: automated
---

# Kombinasi Filter, Search, Sort, dan Ukuran Halaman Tab Session: Pelepasan Kontrol dan Pindah Kolom Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session). Tidak ada ganti akun di tengah spec.
- Data Pre-setup #11 (Tab Session SS-01 sampai SS-11), hanya dibaca dan tidak diubah. Baris yang dipakai spec ini: SS-01 dan SS-02 (John Doe, Marketing, Chrome on Windows), SS-04 (Mike Tan, Operations, Chrome on Android), SS-07 (Dewi Lestari, Marketing), SS-08 (Hendra Pratama #1, Marketing), SS-10 (John Dalton, Operations, Chrome on Windows). Identitas baris dirujuk lewat `Fixture.activity-log.<kunci>` (fixture `fixtures/activity-log.json` disediakan tim FE; nama kunci ditetapkan tim FE).
- Nilai Data Uji TC: Division `Marketing`; Search `Chrome`; Sort header User Ascending; Rows per page 25 (dirujuk lewat fixture yang sama). Nilai Rows per page awal adalah 10 (SS-05 berada di halaman 2 menurut TC-FA-FAAL-103).
- Posisi dan isi baris pada asersi bergantung pada Tab Session client uji yang hanya memuat baris seed #11 saat spec berjalan; jaminan itu disediakan tim FE/BE (lihat Temuan untuk QA). Total entri tidak diasersi sebagai angka absolut kecuali hitungan yang dibatasi Filter dan Search (langkah 9).
- State yang diubah spec: Search, Filter, Sort, dan Rows per page Tab Session. Search, Filter, dan Sort dibersihkan pembukaan layar hook `beforeEach` suite sebelum spec berikutnya; Rows per page dikembalikan ke 10 oleh langkah terakhir.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-92: Kombinasi Filter, Search, Sort, dan ukuran halaman

1. Klik icon Filter, pilih Division `Marketing`, klik `[Apply]`
2. Ketik Search `Chrome`, tekan Enter
3. Klik header User sekali (Ascending)
4. Verifikasi urutan baris SS-02 lalu SS-01 (keduanya `John Doe`, tie diselesaikan Date terbaru di atas)
5. Ubah Rows per page menjadi 25
6. Verifikasi filter Division `Marketing` tetap aktif
7. Verifikasi Search `Chrome` tetap aktif
8. Verifikasi Sort User Ascending tetap aktif
9. Verifikasi `Showing 1–2 of 2 entries`

### TC-FA-FAAL-94: Mengosongkan Search mempertahankan Filter dan Sort

10. Klik `(✕)` pada input Search lalu tekan Enter
11. Verifikasi filter Division `Marketing` tetap aktif
12. Verifikasi Sort User Ascending tetap aktif
13. Verifikasi urutan baris SS-07, SS-08, SS-02, SS-01
14. Ketik Search `Chrome`, tekan Enter

### TC-FA-FAAL-93: Clear Field filter mempertahankan Search dan Sort

15. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
16. Verifikasi Search `Chrome` tetap aktif
17. Verifikasi Sort User Ascending tetap aktif
18. Verifikasi urutan baris SS-10, SS-02, SS-01, SS-04
19. Klik icon Filter untuk menutup panel
20. Klik icon Filter, pilih Division `Marketing`, klik `[Apply]`

### TC-FA-FAAL-95: Pindah kolom sort tidak mereset Search dan Filter

21. Klik header Position sekali
22. Verifikasi Sort pindah ke Position Ascending
23. Verifikasi indikator sort kolom User kembali netral
24. Verifikasi Search `Chrome` tetap aktif
25. Verifikasi Filter Division `Marketing` tetap aktif
26. Verifikasi urutan baris SS-02 lalu SS-01
27. Ubah Rows per page menjadi 10

## Notes

- Urutan TC: TC-FA-FAAL-92, 94, 93, 95. TC-FA-FAAL-93, 94, dan 95 bergantung pada state hasil langkah 1 sampai 3 TC-FA-FAAL-92 (Division `Marketing`, Search `Chrome`, Sort User Ascending); state itu dibangun langkah 1 sampai 3 dan dipulihkan langkah 14 dan 20 sebelum TC yang membutuhkannya (S-04, S-09). TC-FA-FAAL-94 dijalankan sebelum TC-FA-FAAL-93 karena langkah 14 memulihkan Search sedangkan TC-FA-FAAL-93 mengosongkan Filter dan langkah 20 memulihkannya.
- Langkah penghubung (S-03): langkah 14 dan 20 (memulihkan Search dan Filter untuk TC berikutnya), langkah 19 (menutup Filter Panel yang tetap terbuka sesudah `[Apply]` agar klik icon Filter pada langkah 20 membukanya), langkah 27 (mengembalikan Rows per page ke 10).
- Pembagian TC lintas spec: TC-FA-FAAL-90, 91, 96, 97 ada di spec 029.
- Langkah 4, 13, 18, dan 26 menyebut daftar baris seed sekaligus sebagai pembanding positif asersi urutan.
- Temuan untuk QA:
  - TC-FA-FAAL-92, 93, 94, 95 mengasumsikan Tab Session hanya berisi SS-01 sampai SS-11, padahal Activity Log adalah audit trail permanen yang tumbuh; spec mengikuti TC dan menuliskan jaminan data di Prerequisites sebagai kebutuhan tim FE/BE.
  - TC tidak menyatakan apakah Filter Panel tetap terbuka atau menutup sesudah `[Apply]` (TC-FA-FAAL-98 langkah 2 menyiratkan tetap terbuka); spec memakai pembacaan "tetap terbuka" dan menambah langkah penutup panel (langkah 19).
  - TC-FA-FAAL-92 sampai 95 tidak menyebut cara membuktikan "filter, Search, Sort tetap aktif" (badge titik, isi kotak, indikator header); spec menulisnya apa adanya.
  - Precondition d TC-FA-FAAL-93, 94, 95 tidak menyebut ukuran halaman; spec mempertahankan Rows per page 25 hasil TC-FA-FAAL-92 sampai langkah 27.
