---
id: TC-FA-SU-E2E-438-tab-transaction-admin-log-perilaku-filter-panel-sub-tab-borrow
title: "Tab Transaction Admin Log: Perilaku Filter Panel Sub-tab Borrow"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-781
coverage:
  web: automated
---

# Tab Transaction Admin Log: Perilaku Filter Panel Sub-tab Borrow

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso. Sub-tab Borrow berisi 5 baris sesuai Pre-setup #29 TC: `18/07/26` `Returned · Self-processed` `BRW-2026-0315` `Laptop Dell Latitude - 3` `Rina Wijaya` `General Affairs`; `16/07/26` `Rejected` `BRW-2026-0314` `Projector Epson - 1` `Andi Pratama` `Branch Surabaya`; `15/07/26` `Handed over` `BRW-2026-0313` `Camera Sony A7 - 2` `Budi Santoso` `Logistics Warehouse`; `13/07/26` `Requested` `BRW-2026-0312` `Laptop Dell Latitude - 5` `Dewi Lestari` `Finance & Accounting`; `12/07/26` `Draft created` `—` `Tablet Samsung Tab - 4` `—` `IT Infrastructure`. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Kemampuan teknis: dropdown multi-select pada Filter Panel, klik di luar panel, overlay Column Visibility pada header kolom `⋯`.
- State: Filter dan visibilitas kolom `Borrower` berubah di sisi klien; filter dibersihkan dan kolom `Borrower` dicentang kembali dengan langkah eksplisit (langkah 31 sampai 35), dan konfigurasi kolom yang tersimpan dibersihkan hook `after` suite (kemampuan hapus preferensi kolom disediakan tim FE). Tidak ada data yang dibuat spec.

## Test Steps

### TC-FA-SU-781: Perilaku Filter Panel, tutup tanpa Apply, indikator titik, dan nilai kosong

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Klik icon Filter
3. Buka dropdown Activity lalu centang `Rejected`
4. Klik di luar panel Filter
5. Klik icon Filter
6. Verifikasi field Activity tidak memuat chip `Rejected` dan menampilkan placeholder `All activities` (perubahan dibuang, nilai ter-Apply terakhir ditampilkan)
7. Verifikasi tabel tidak berubah (lima baris tampil)
8. Buka dropdown Activity lalu centang `Rejected`
9. Klik `[Apply]`
10. Verifikasi icon Filter menampilkan badge titik saat panel terbuka
11. Klik icon Filter
12. Verifikasi icon Filter menampilkan badge titik saat panel tertutup
13. Klik icon Filter
14. Klik `[Clear Field]`
15. Klik `[Apply]`
16. Verifikasi badge titik pada icon Filter hilang
17. Buka dropdown Borrower
18. Verifikasi opsi dropdown Borrower `Andi Pratama`, `Budi Santoso`, `Dewi Lestari`, dan `Rina Wijaya` tampil
19. Verifikasi dropdown Borrower tidak memiliki opsi untuk nilai kosong (`—`)
20. Centang `Dewi Lestari`
21. Klik `[Apply]`
22. Verifikasi tabel menyisakan `BRW-2026-0312` (1 baris)
23. Verifikasi baris Draft (`Draft created`, Borrower `—`) tidak tampil
24. Klik icon Filter
25. Klik header kolom `⋯`
26. Hilangkan centang `Borrower` pada overlay Column Visibility
27. Verifikasi kolom `Borrower` tidak tampil dan kolom `Date`, `Activity`, `Transaction ID`, `Name`, dan `Group` tetap tampil
28. Klik icon Filter
29. Verifikasi field `Borrower` tetap tampil pada Filter Panel dengan chip `Dewi Lestari`
30. Verifikasi filter ter-Apply tetap berlaku: tabel menyisakan `BRW-2026-0312` (1 baris)
31. Klik header kolom `⋯`
32. Centang kembali `Borrower` pada overlay Column Visibility
33. Klik `[Clear Field]`
34. Klik `[Apply]`
35. Klik icon Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec 258 memuat TC-FA-SU-779 dan 780 (kombinasi Search dan Filter, pelepasan kontrol) pada sub-tab yang sama.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna di User List lalu membuka sub-tab; R-16), pembukaan dan penutupan panel Filter (langkah 5, 11, 13, 24, 28, 35), pembersihan filter (langkah 14, 15, 33, 34; S-09), dan pemulihan kolom `Borrower` (langkah 31 dan 32; 8b.14, S-03). Pada langkah 17 dan 20 panel Filter masih terbuka sesudah `[Apply]` (8b.9), sehingga dropdown dibuka tanpa klik icon Filter.
- Langkah 18 (opsi lain tampil) adalah anchor positif sebelum asersi absence opsi nilai kosong pada langkah 19, dan langkah 22 (baris `BRW-2026-0312` tampil) adalah anchor sebelum absence baris Draft pada langkah 23 (8b.2). Langkah 27 (kolom lain tampil) mendahului asersi field filter tetap ada (langkah 29).
- Temuan untuk QA (S-15): (1) Kolom ACC TC-FA-SU-781 berisi `#20`, yang di Pre-setup adalah Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, Pre-setup #1). (2) TC-FA-SU-781 butir c ("Dropdown filter tidak memiliki opsi untuk nilai kosong; memilih opsi apa pun menyaring keluar baris yang nilainya kosong") tidak menyebut kolom filter; spec memakai Borrower (baris Draft bernilai `—`), dan langkah TC 5 ("Apply filter pada satu kolom lalu hide kolom itu") memakai kolom yang sama. (3) TC-FA-SU-781 butir a menyebut menutup panel lewat klik luar atau klik ulang icon Filter, sedangkan langkah TC 2 hanya "klik luar panel"; spec menjalankan klik luar (langkah 4) dan klik ulang icon Filter dicakup oleh langkah 11 dan 24 sebagai penutupan sesudah Apply. (4) Post Condition tidak ada.
