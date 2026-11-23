---
id: TC-FA-SU-E2E-259-tab-transaction-admin-log-filter-dan-kontrol-filter-dan-setup-column
title: "Tab Transaction Admin Log: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-782
  - TC-FA-SU-783
  - TC-FA-SU-784
coverage:
  web: automated
---

# Tab Transaction Admin Log: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris (`BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`) dengan nilai Date, Activity, Name, Borrower, dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): tombol keyboard `Esc`, hover, dan muat ulang halaman (`F5`).
- Popup Setup Column hanya dibuka dan ditutup lewat `✕` tanpa `[Save]`; spec ini tidak mengubah preferensi kolom.

## Test Steps

### TC-FA-SU-782: Chip dan checkbox dropdown Filter sinkron dua arah, logika OR dalam field

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Klik icon Filter
3. Buka dropdown Group
4. Centang opsi `Branch Surabaya` dan `Finance & Accounting`
5. Klik `[Apply]`
6. Verifikasi dua chip `Branch Surabaya` dan `Finance & Accounting` tampil di dalam field Group
7. Verifikasi tabel menyisakan `BRW-2026-0314` dan `BRW-2026-0312` (2 baris, gabungan OR kedua opsi)
8. Klik `✕` pada chip `Branch Surabaya` tanpa membuka dropdown
9. Verifikasi chip `Branch Surabaya` hilang dari field Group
10. Verifikasi chip `Finance & Accounting` tetap tampil
11. Buka dropdown Group
12. Verifikasi checkbox opsi `Branch Surabaya` ter-uncheck
13. Hilangkan centang opsi `Finance & Accounting`
14. Verifikasi chip `Finance & Accounting` hilang dari field Group
15. Ketik `surab` di kotak cari dropdown Group
16. Verifikasi daftar opsi dropdown menyisakan `Branch Surabaya`
17. Ganti isi kotak cari dropdown Group dengan `zzz`
18. Verifikasi dropdown menampilkan `No results found`
19. Tutup dropdown Group dengan `Esc`
20. Klik `[Clear Field]`, lalu klik `[Apply]`
21. Klik icon Filter untuk menutup panel

### TC-FA-SU-783: Screening Overlay Column Visibility

22. Hover header kolom `⋯`
23. Verifikasi tooltip `Column Visibility` tampil pada header kolom `⋯`
24. Klik header kolom `⋯`
25. Verifikasi overlay Column Visibility tampil
26. Verifikasi daftar kolom pada overlay berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, `Group`
27. Verifikasi tiap kolom pada overlay memiliki checkbox Hideable terpilih dan enabled
28. Verifikasi tiap kolom pada overlay memiliki drag handle
29. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-FA-SU-784: Screening Popup Setup Column dan Preview Table

30. Klik item `Setup Column...`
31. Verifikasi Title popup `Setup Column`
32. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
33. Verifikasi icon close `✕` tampil pada header popup
34. Verifikasi body memuat daftar kolom `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, `Group` dengan checkbox, drag handle, dan icon Pin
35. Verifikasi Live Preview tabel tampil
36. Verifikasi footer memuat `[Reset to Default]` dan `[Save]` rata kanan
37. Verifikasi footer tidak memuat `[Cancel]`
38. Klik `✕` pada popup Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penutupan dropdown Group dengan `Esc`, pemulihan Filter (`[Clear Field]` lalu `[Apply]`) dan penutupan panel Filter di akhir blok TC-FA-SU-782 (S-09), serta penutupan popup Setup Column tanpa `[Save]` di akhir spec (S-09).
- Pembagian TC lintas spec: TC-FA-SU-785 (ceklis dan unceklis Setup Column) ada di spec 439; TC-FA-SU-786 dan TC-FA-SU-788 ada di spec 260; TC-FA-SU-787 ada di spec 275.
- Opsi Group, kata kunci pencarian dropdown (`surab`, `zzz`), dan pasangan opsi `Branch Surabaya` dengan `Finance & Accounting` dipilih spec karena TC-FA-SU-782 tidak menyebut nilainya; kata kunci `surab` (huruf kecil, sebagian kata) mengasersi pencarian substring tanpa membedakan huruf besar kecil.
- Temuan untuk QA (S-15): (1) TC-FA-SU-782 sampai 784 menulis ACC `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun. Aktor memakai Total Control Lina Marlina (#1) dari hook suite. (2) TC-FA-SU-782 butir c ("chip yang bersangkutan hilang, chip lain tetap") tidak dapat diasersi sebagai "chip lain tetap" karena Langkah Uji nomor 5 meng-uncheck opsi yang tersisa; spec mengasersi chip yang bersangkutan hilang dan chip lain tetap pada langkah 10 (sesudah klik `✕` pada chip). (3) Post Condition tidak ada.
- Spec ini berjumlah 38 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
