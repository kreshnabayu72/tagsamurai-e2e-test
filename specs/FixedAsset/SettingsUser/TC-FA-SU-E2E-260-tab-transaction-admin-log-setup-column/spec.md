---
id: TC-FA-SU-E2E-260-tab-transaction-admin-log-setup-column
title: "Tab Transaction Admin Log: Setup Column (Drag Reorder dan Reset to Default)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-786
  - TC-FA-SU-788
coverage:
  web: automated
---

# Tab Transaction Admin Log: Setup Column (Drag Reorder dan Reset to Default)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Transaction ID, Group, Role, Action Taken, Date, Transaction Status.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment

### TC-FA-SU-786: Geser (drag reorder) Setup Column kelas Hideable (default tampil)

2. Klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 4 sampai 5):
4. Drag kolom tersebut satu posisi
5. Verifikasi urutan Live Preview berubah
6. Klik `[Save]`
7. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 8):
8. Verifikasi posisi kolom tersebut pada tabel berubah
9. Klik F5
10. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 11):
11. Verifikasi posisi kolom tersebut pada tabel tetap berubah setelah refresh (F5)
12. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-788: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column

13. Klik header kolom `⋯`, lalu klik item `Setup Column...`
14. Ubah pengaturan: hilangkan centang `Group`, drag kolom `Role` satu posisi, dan klik icon Pin pada kolom `Transaction ID`
15. Klik `[Reset to Default]`
16. Verifikasi preview mengembalikan visibility, urutan, dan pin ke default modul
17. Klik `[Save]`
18. Verifikasi tabel menampilkan visibility, urutan, dan pin default setelah `[Save]`
19. Buka Setup Column, hilangkan centang `Group`, lalu klik `✕`
20. Verifikasi perubahan preview dibuang
21. Verifikasi tabel memakai konfigurasi tersimpan terakhir
22. Buka Setup Column, hilangkan centang `Group`, lalu tekan Esc
23. Verifikasi perubahan preview dibuang
24. Verifikasi tabel memakai konfigurasi tersimpan terakhir
25. Klik Back breadcrumb ke User List
26. Verifikasi konfigurasi kolom tabel User List tidak berubah (tidak terpengaruh perubahan tabel ini)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pembagian TC lintas spec: TC-FA-SU-787 (Pin dan unpin) ada di spec 275; TC-FA-SU-785 ada di spec 259.
- Temuan untuk QA (S-15): TC tidak menyebut arah drag; spec menulis "satu posisi" mengikuti TC dan arah drag ditentukan skrip uji.
- Temuan untuk QA (S-15) tambahan: (1) TC-FA-SU-788 Langkah Uji nomor 6 ("Buka tabel lain yang punya Setup Column dan bandingkan") tidak menyebut tabel; spec memakai tabel User List dan mengasersi konfigurasinya tidak berubah. Karena konfigurasi tabel ini sudah kembali ke default sesudah `[Reset to Default]` dan `[Save]`, perbandingan itu tidak membuktikan independensi cache sepenuhnya. (2) Post Condition TC-FA-SU-788 tidak punya langkah observasi dan tidak diasersi.
- Langkah berulang (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 6 kali, satu iterasi per baris di tabel Prerequisites; langkah 8 dijalankan 6 kali, satu iterasi per baris di tabel Prerequisites; langkah 11 dijalankan 6 kali, satu iterasi per baris di tabel Prerequisites.
- Spec ini berjumlah 46 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
