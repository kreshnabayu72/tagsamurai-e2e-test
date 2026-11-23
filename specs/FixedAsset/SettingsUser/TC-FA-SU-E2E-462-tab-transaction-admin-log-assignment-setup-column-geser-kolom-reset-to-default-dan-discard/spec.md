---
id: TC-FA-SU-E2E-462-tab-transaction-admin-log-assignment-setup-column-geser-kolom-reset-to-default-dan-discard
title: "Tab Transaction Admin Log Sub-tab Assignment: Setup Column Geser Kolom, Reset to Default, dan Discard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1163
  - TC-FA-SU-1165
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Setup Column Geser Kolom, Reset to Default, dan Discard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Activity, Transaction ID, Name, Assignee, Group.
- Pemulihan konfigurasi tabel: konfigurasi tabel Assignment kembali ke default setelah `[Reset to Default]` dan `[Save]` pada TC-FA-SU-1165 dan dipastikan oleh penghapusan preferensi kolom di hook `after`.

## Test Steps

### TC-FA-SU-1163: Geser (drag reorder) Setup Column kelas Hideable (default tampil)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
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

### TC-FA-SU-1165: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column

13. Klik header kolom `⋯`, lalu klik item `Setup Column...`
14. Ubah pengaturan: hilangkan centang `Group`, drag kolom `Activity` satu posisi, dan klik icon Pin pada kolom `Transaction ID`
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
25. Klik Sub-tab Borrow
26. Verifikasi konfigurasi kolom sub-tab Borrow tidak berubah (urutan `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, `Group`, semua tampil, tanpa pin)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penghapusan preferensi kolom, dan perpindahan ke sub-tab Borrow; semuanya hanya mengembalikan state sebelum TC berikutnya atau membandingkan tabel lain (S-09).
- Pembagian TC lintas spec: ceklis ada di spec 461; Pin dan unpin ada di spec 463.
- Langkah berulang (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 6 kali, satu iterasi per baris di tabel Prerequisites; langkah 8 dijalankan 6 kali, satu iterasi per baris di tabel Prerequisites; langkah 11 dijalankan 6 kali, satu iterasi per baris di tabel Prerequisites.
- Temuan untuk QA (S-15): (1) TC tidak menyebut arah drag (TC-FA-SU-1163); spec menulis "satu posisi" mengikuti TC dan arah drag ditentukan skrip uji. (2) TC-FA-SU-1165 Langkah Uji nomor 6 ("Buka tabel lain yang punya Setup Column dan bandingkan") tidak menyebut tabel; spec memakai sub-tab Borrow sesuai Expected c dan mengasersi konfigurasinya tidak berubah. Karena konfigurasi tabel Assignment sudah kembali ke default sesudah `[Reset to Default]` dan `[Save]`, perbandingan itu tidak membuktikan independensi cache sepenuhnya. (3) Post Condition tidak punya langkah observasi dan tidak diasersi.
