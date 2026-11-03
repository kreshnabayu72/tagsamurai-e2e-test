---
id: TC-FA-FAAL-E2E-029-interaksi-search-filter-sort-tab-session
title: "Interaksi Search dan Filter Tab Session: Irisan Dua Urutan, Pemulihan Empty State, dan Filter Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-90
  - TC-FA-FAAL-91
  - TC-FA-FAAL-96
  - TC-FA-FAAL-97
coverage:
  web: automated
---

# Interaksi Search dan Filter Tab Session: Irisan Dua Urutan, Pemulihan Empty State, dan Filter Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session). Tidak ada ganti akun di tengah spec.
- Data Pre-setup #11 (Tab Session SS-01 sampai SS-11), hanya dibaca dan tidak diubah. Baris yang dipakai spec ini: SS-03 (Siti Nurbaya, Finance), SS-05 (Jane Smith, Finance), SS-08 (Hendra Pratama #1, Marketing), SS-09 (Hendra Pratama #2, Finance), SS-11 (John Davis, Finance). Identitas baris dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE); nama dan nilai ditulis seperti di TC.
- Nilai Data Uji TC: Search `Hendra` dan `zzz`; Division `Finance`; Position `Manager`; Division `Operations` (ditulis seperti di TC).
- Posisi dan isi baris pada asersi bergantung pada Tab Session client uji yang hanya memuat baris seed #11 saat spec berjalan; jaminan itu disediakan tim FE/BE (lihat Temuan untuk QA). Total entri tidak diasersi sebagai angka absolut.
- State yang diubah spec: Search dan Filter Tab Session; keduanya dibersihkan oleh langkah penghubung dan di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-90: Search lalu Filter menghasilkan irisan

1. Ketik Search `Hendra`, tekan Enter
2. Verifikasi tabel menampilkan hanya SS-08 dan SS-09
3. Klik icon Filter, pilih Division `Finance`, klik `[Apply]`
4. Verifikasi tabel menampilkan hanya SS-09
5. Verifikasi keyword `Hendra` tetap terisi di Search
6. Klik `(✕)` pada Search, tekan Enter
7. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
8. Klik icon Filter untuk menutup panel

### TC-FA-FAAL-91: Filter lalu Search menghasilkan irisan identik

9. Klik icon Filter, pilih Division `Finance`, klik `[Apply]`
10. Verifikasi tabel menampilkan hanya SS-03, SS-05, SS-09, dan SS-11
11. Ketik Search `Hendra`, tekan Enter
12. Verifikasi tabel menampilkan hanya SS-09
13. Verifikasi filter Division `Finance` tetap aktif
14. Klik `(✕)` pada Search, tekan Enter
15. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
16. Klik icon Filter untuk menutup panel

### TC-FA-FAAL-96: Pemulihan dari empty state saat salah satu kontrol dilepas

17. Klik icon Filter, pilih Division `Finance`, klik `[Apply]`
18. Ketik Search `zzz`, tekan Enter
19. Verifikasi tabel menampilkan `No results found`
20. Klik `(✕)` pada Search, tekan Enter
21. Verifikasi tabel menampilkan kembali SS-03, SS-05, SS-09, dan SS-11
22. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
23. Klik icon Filter untuk menutup panel

### TC-FA-FAAL-97: Filter tanpa hasil di Tab Session menampilkan state kosong terfilter

24. Klik icon Filter
25. Pilih Position `Manager` dan Division `Operations`
26. Klik `[Apply]`
27. Verifikasi tampil Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
28. Verifikasi tidak ada baris tabel dan tidak ada pesan error

## Notes

- Urutan TC: TC-FA-FAAL-90, 91, 96, 97. Pembagian TC lintas spec: TC-FA-FAAL-92, 93, 94, 95 ada di spec 069.
- Langkah penghubung (S-03): langkah 6, 7, 8, 14, 15, 16, 22, 23 (membersihkan Search dan Filter dan menutup Filter Panel sebelum TC berikutnya, S-09). Langkah 8, 16, dan 23 menutup Filter Panel dengan klik icon Filter karena TC-FA-FAAL-98 langkah 2 menyiratkan panel tetap terbuka sesudah `[Apply]` dan klik icon Filter berikutnya akan menutupnya.
- Langkah 19 dan 27 memuat `No results found` sebagai anchor positif hasil Search atau Filter; langkah 28 (daftar elemen yang sama-sama tidak ada) disebut utuh dalam satu `Verifikasi` (S-01).
- Langkah 2, 4, 10, 12, dan 21 menyebut daftar baris seed; baris tersebut sekaligus pembanding positif asersi "hanya" (butir 8b.2).
- Temuan untuk QA:
  - TC-FA-FAAL-90, 91, 96, 97 mengasumsikan Tab Session hanya berisi SS-01 sampai SS-11, padahal Activity Log adalah audit trail permanen yang tumbuh; spec mengikuti TC dan menuliskan jaminan data di Prerequisites sebagai kebutuhan tim FE/BE.
  - TC tidak menyatakan apakah Filter Panel tetap terbuka atau menutup sesudah `[Apply]`; spec memakai pembacaan "tetap terbuka" (TC-FA-FAAL-98) dan menambah langkah penutup panel (langkah 8, 16, 23).
  - TC-FA-FAAL-90 dan 91 tidak menyebut cara membuktikan "filter Division `Finance` tetap aktif" (badge titik atau isi panel); spec menulisnya apa adanya (langkah 13).
