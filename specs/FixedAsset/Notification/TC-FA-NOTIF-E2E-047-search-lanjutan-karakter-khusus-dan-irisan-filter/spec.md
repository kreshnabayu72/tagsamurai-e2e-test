---
id: TC-FA-NOTIF-E2E-047-search-lanjutan-karakter-khusus-dan-irisan-filter
title: "Search Lanjutan: Input Kosong, Karakter Khusus, Timestamp Relatif, dan Irisan dengan Filter"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-192
  - TC-FA-NOTIF-193
  - TC-FA-NOTIF-194
  - TC-FA-NOTIF-195
coverage:
  web: automated
---

# Search Lanjutan: Input Kosong, Karakter Khusus, Timestamp Relatif, dan Irisan dengan Filter

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi) milik akun aktor. TC-194 memakai varian seed umur 30 detik (minimal satu item bertimestamp `Just now`) beserta N-41 (event_type `assignment_declined`, dibuat 11/06/26, timestamp absolut `11/06/26`; Pre-setup #18), ditukar fixture BE penukar sebagai langkah penghubung. Seed dipulihkan fixture BE pemulih di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih dan penukar seed notifikasi.

## Test Steps

### TC-FA-NOTIF-192: Search input kosong atau hanya spasi menampilkan semua data

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Ketik Search `repaired`, tekan Enter
3. Verifikasi item `Asset has been repaired` tampil pada list
4. Verifikasi list tersaring (item `Waiting for your approval` tidak tampil)
5. Ganti isi kotak search dengan tiga spasi, tekan Enter
6. Verifikasi list kembali menampilkan semua data tanpa saringan (item `Waiting for your approval` tampil)

### TC-FA-NOTIF-193: Search karakter khusus dicocokkan sebagai teks biasa

7. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
8. Ketik Search `%`, tekan Enter
9. Verifikasi empty state tampil dengan Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
10. Ganti isi kotak search dengan `<b>x</b>`, tekan Enter
11. Verifikasi empty state tampil dengan Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`

### TC-FA-NOTIF-194: Guard Search: timestamp relatif tidak dicocokkan oleh Search

12. Pulihkan seed notifikasi lewat fixture BE pemulih, tukar ke varian seed umur 30 detik dengan N-41 lewat fixture BE penukar, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
13. Verifikasi sedikitnya satu item menampilkan timestamp `Just now`
14. Scroll sampai akhir list hingga seluruh item termuat
15. Verifikasi N-41 menampilkan timestamp absolut `11/06/26`
16. Ketik Search `Just now`, tekan Enter
17. Verifikasi empty state tampil dengan Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`
18. Ganti isi kotak search dengan `11/06/26`, tekan Enter
19. Verifikasi empty state tampil dengan Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.`

### TC-FA-NOTIF-195: Search dan Filter dua arah menghasilkan irisan identik

20. Pulihkan seed notifikasi lewat fixture BE pemulih, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
21. Ketik Search `access`, tekan Enter
22. Klik icon Filter, pilih Event Type `Access Total Control Removed`, lalu klik `[Apply]`
23. Scroll sampai akhir list hingga seluruh item termuat
24. Verifikasi list memuat sedikitnya satu item
25. Catat daftar item hasil (irisan Search dan Filter, arah pertama)
26. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
27. Klik icon Filter, pilih Event Type `Access Total Control Removed`, lalu klik `[Apply]`
28. Ketik Search `access`, tekan Enter
29. Scroll sampai akhir list hingga seluruh item termuat
30. Verifikasi daftar item hasil sama dengan daftar yang dicatat pada langkah 25
31. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 7, 26, 31 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 12 dan 20 (pemulihan seed, penukaran varian, dan muat ulang), 14 dan 23 dan 29 (memuat seluruh item), 25 (mencatat hasil arah pertama untuk dibandingkan di langkah 30).
- Asersi tambahan di luar Expected TC (S-03): langkah 3 dan 4 (item pembanding sebelum asersi universal, 8b butir 2), langkah 13 dan 15 (precondition TC-194 butir d dan e sebagai anchor positif sebelum asersi empty state, 8b butir 2), langkah 24 (item pembanding sebelum membandingkan daftar). Empty state `No results found` hasil Search pada langkah 9, 11, 17, 19 adalah anchor positif yang sah bagi hasil Search.
- Pencarian `%` dan `<b>x</b>` (langkah 8 dan 10) tidak diasersi selain empty state karena Expected TC-193 hanya menyebut empty state.
- Temuan untuk QA:
  - TC-195 menyebut "Hasil langkah 2 dan langkah 3 identik" tanpa isi hasil; spec membandingkan daftar item hasil kedua arah.
  - TC-194 tidak mengharuskan Verifikasi bahwa seed umur 30 detik dan N-41 sudah ada (precondition d dan e); spec menambahkannya sebagai anchor (langkah 13 dan 15).
  - TC-192 judul "input kosong atau hanya spasi" tetapi langkah dan Expected hanya mencakup tiga spasi; input kosong tanpa spasi ada di spec 046 (TC-188 butir d).
