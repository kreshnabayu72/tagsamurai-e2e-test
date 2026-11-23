---
id: TC-FA-SU-E2E-261-tab-transaction-admin-log-pagination-dan-tooltip-icon
title: "Tab Transaction Admin Log: Pagination dan Tooltip Icon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-789
  - TC-FA-SU-794
coverage:
  web: automated
---

# Tab Transaction Admin Log: Pagination dan Tooltip Icon

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris (`BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`) dengan nilai Date, Activity, Name, Borrower, dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): tombol keyboard `Esc`, hover, dan muat ulang halaman (`F5`).
- Tabel "Nomor halaman" (parameter langkah berulang): `0`, `-1`, `999`, `abc`.

## Test Steps

### TC-FA-SU-789: Pagination (page size, navigasi, dan kasus tepi)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Verifikasi footer pagination menampilkan 10 baris per halaman
3. Klik dropdown page size
4. Verifikasi pilihan page size 10, 25, 50, 100
5. Verifikasi tidak ada opsi `All` pada pilihan page size
6. Tutup dropdown page size dengan `Esc`
7. Untuk setiap baris pada tabel "Nomor halaman" (langkah 8 sampai 9):
8. Isi nomor halaman pada footer pagination dengan nilai pada baris tersebut, tekan Enter
9. Verifikasi nilai pada baris tersebut diabaikan dan tabel tetap di halaman 1
10. Ganti page size ke 25
11. Verifikasi tabel tetap di halaman 1
12. Ganti page size ke 10
13. Verifikasi tabel tetap di halaman 1
14. Klik header kolom `Name` satu kali
15. Verifikasi tabel tetap di halaman 1
16. Klik header kolom `Name` dua kali lagi hingga sort kembali netral
17. Ketik Search `0313`, tekan Enter
18. Verifikasi tabel menyisakan `BRW-2026-0313` (1 baris)
19. Verifikasi tabel tetap di halaman 1
20. Klik `←` pada kotak Search

### TC-FA-SU-794: Tooltip icon Table Tools dan header Actions

21. Hover icon Search
22. Verifikasi tooltip `Search` tampil
23. Hover icon Filter
24. Verifikasi tooltip `Filter` tampil
25. Hover icon Download
26. Verifikasi tooltip `Download` tampil
27. Hover header kolom Actions (`⋯`)
28. Verifikasi tooltip `Column Visibility` tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penutupan dropdown page size dengan `Esc`, pengembalian page size ke 10 dan sort ke netral (klik header `Name` dua kali lagi), serta pengosongan Search dengan `←` pada akhir blok TC-FA-SU-789 (S-09).
- Langkah berulang (idiom bagian 8b butir 7): langkah 8 sampai 9 dijalankan 4 kali, satu iterasi per baris tabel "Nomor halaman".
- Pembagian TC lintas spec: state per sub-tab (TC-FA-SU-796) ada di spec 440.
- Temuan untuk QA (S-15): (1) TC-FA-SU-789 dan TC-FA-SU-794 menulis ACC `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun. Aktor memakai Total Control Lina Marlina (#1) dari hook suite. (2) TC-FA-SU-789 butir e menyatakan fixture memuat satu halaman data sehingga perpindahan antar halaman tidak dapat dicapai pada surface ini; karena itu "tetap di halaman 1" (butir b, c, d) tidak membuktikan reset dari halaman lain, dan spec tidak mengasersi perpindahan halaman (diuji pada TC-FA-SU-359 dan TC-FA-SU-1057 menurut TC). (3) TC-FA-SU-789 tidak menyebut kontrol input nomor halaman; spec memakai isian nomor halaman pada footer pagination. (4) Sort pada langkah dengan header `Name` dipilih spec karena TC tidak menyebut kolomnya. (5) Post Condition tidak ada.
