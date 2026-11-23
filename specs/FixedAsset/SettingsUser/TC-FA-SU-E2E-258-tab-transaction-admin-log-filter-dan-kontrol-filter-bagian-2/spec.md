---
id: TC-FA-SU-E2E-258-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-2
title: "Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-779
  - TC-FA-SU-780
coverage:
  web: automated
---

# Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso. Sub-tab Borrow berisi 5 baris sesuai Pre-setup #29 TC: `18/07/26` `Returned · Self-processed` `BRW-2026-0315` `Laptop Dell Latitude - 3` `Rina Wijaya` `General Affairs`; `16/07/26` `Rejected` `BRW-2026-0314` `Projector Epson - 1` `Andi Pratama` `Branch Surabaya`; `15/07/26` `Handed over` `BRW-2026-0313` `Camera Sony A7 - 2` `Budi Santoso` `Logistics Warehouse`; `13/07/26` `Requested` `BRW-2026-0312` `Laptop Dell Latitude - 5` `Dewi Lestari` `Finance & Accounting`; `12/07/26` `Draft created` `—` `Tablet Samsung Tab - 4` `—` `IT Infrastructure`. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Kemampuan teknis: dropdown multi-select pada Filter Panel, ikon `←` pada kotak Search.
- State: yang berubah hanya Search, Filter, dan Sort di sisi klien; ketiganya dikembalikan ke keadaan awal dengan langkah eksplisit di akhir spec (langkah 35 sampai 39). Tidak ada state global dan tidak ada data yang dibuat spec.

## Test Steps

### TC-FA-SU-779: Kombinasi Search dan Filter dua arah

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Ketik Search `0313`, tekan Enter
3. Klik icon Filter
4. Buka dropdown Group lalu centang `Branch Surabaya`
5. Klik `[Apply]`
6. Verifikasi hasil irisan Search `0313` dan Filter Group `Branch Surabaya` tidak ada baris (0 baris)
7. Verifikasi kotak Search tetap berisi `0313` (menerapkan Filter tidak mengosongkan keyword Search)
8. Klik `←` pada kotak Search
9. Klik `[Clear Field]`
10. Klik `[Apply]`
11. Verifikasi tabel kembali menampilkan semua baris (lima baris)
12. Buka dropdown Group lalu centang `Branch Surabaya`
13. Klik `[Apply]`
14. Ketik Search `0313`, tekan Enter
15. Verifikasi hasil Filter Group `Branch Surabaya` lalu Search `0313` identik: tidak ada baris
16. Verifikasi chip `Branch Surabaya` tetap tampil di field Group (menjalankan Search tidak mereset Filter)
17. Verifikasi tabel berada di halaman 1 setelah kriteria berubah

### TC-FA-SU-780: Pelepasan kontrol: Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

18. Klik header `Transaction ID` (Search `0313` dan Filter Group `Branch Surabaya` masih aktif)
19. Klik `[Clear Field]`
20. Klik `[Apply]`
21. Verifikasi Search tetap berlaku: tabel menyisakan `BRW-2026-0313` (1 baris)
22. Verifikasi Sort kolom `Transaction ID` tetap berlaku
23. Buka dropdown Group lalu centang `Branch Surabaya`
24. Klik `[Apply]`
25. Klik `←` pada kotak Search
26. Verifikasi Filter tetap berlaku: tabel menyisakan `BRW-2026-0314` (1 baris)
27. Verifikasi Sort kolom `Transaction ID` tetap berlaku
28. Ketik Search `0313`, tekan Enter
29. Klik header `Name`
30. Verifikasi Sort berpindah ke kolom `Name`
31. Verifikasi keyword Search `0313` dan chip Filter `Branch Surabaya` tetap berlaku
32. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
33. Klik `←` pada kotak Search
34. Verifikasi baris yang cocok dengan Filter dipulihkan: tabel menyisakan `BRW-2026-0314` (1 baris)
35. Klik `[Clear Field]`
36. Klik `[Apply]`
37. Klik icon Filter
38. Klik header `Name`
39. Klik header `Name`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Perilaku Filter Panel sub-tab Borrow (tutup tanpa Apply, indikator titik, nilai kosong; TC-FA-SU-781) ada di spec 438.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna di User List lalu membuka sub-tab; R-16), pembersihan Search dan Filter pada langkah 8 sampai 10, dan pemulihan akhir pada langkah 35 sampai 39 (Clear Field, Apply, tutup panel, dua klik `Name` agar sort netral; S-09). Kondisi awal TC-FA-SU-780 (Search `0313`, Filter Group `Branch Surabaya`) dibentuk oleh langkah 14 dan 13; TC-FA-SU-780 langkah 2 mensyaratkan keadaan yang sama persis, sehingga spec tidak mengosongkan dan mengisi ulang keduanya. Pada langkah 23 dan 28 panel Filter masih terbuka sesudah `[Apply]` (8b.9), sehingga dropdown dibuka tanpa klik icon Filter; kotak Search yang ditutup oleh `←` diisi lewat "Ketik Search" (langkah 14 dan 28).
- Langkah 11 adalah anchor bahwa tabel penuh (lima baris) pulih sebelum urutan sebaliknya (8b.2). Langkah 6 dan 15 menjadi satu-satunya sumber asersi irisan kosong; empty state pada langkah 32 diasersi karena Expected d TC-FA-SU-780 menyebut judul dan deskripsinya.
- Temuan untuk QA (S-15): (1) Kolom ACC TC-FA-SU-779 dan 780 berisi `#20`, yang di Pre-setup adalah Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, Pre-setup #1). (2) Kombinasi Search `0313` dengan Filter Group `Branch Surabaya` (TC-FA-SU-779 butir a) menghasilkan 0 baris, padahal TC-FA-SU-780 langkah 2 memakai kombinasi yang sama sebagai kondisi awal Sort; efek Sort pada hasil tidak dapat diamati karena tabel kosong, sehingga spec hanya mengasersi bahwa kolom sort aktif tetap berlaku (langkah 22, 27, 30). (3) TC-FA-SU-780 langkah 6 ("lepas salah satu kontrol") tidak menyebut kontrol yang dilepas; spec memakai `←` pada kotak Search. (4) TC-FA-SU-779 butir d ("kembali ke halaman 1") tidak dapat dibedakan pada fixture satu halaman; spec mengasersi nomor halaman 1. (5) Post Condition tidak ada pada kedua TC.
- Spec ini berjumlah 39 langkah dan di atas sekitar 35 langkah. Alasan: kedua TC satu kelas (fungsional baca) pada satu surface dengan seed yang sama; TC-FA-SU-780 mensyaratkan kondisi awal yang sama dengan akhir TC-FA-SU-779 sehingga keduanya berbagi dataset dan state, dan ukuran berasal dari empat butir Expected tiap TC (satu `Verifikasi` per klausa, S-01) ditambah pembersihan state di akhir.
