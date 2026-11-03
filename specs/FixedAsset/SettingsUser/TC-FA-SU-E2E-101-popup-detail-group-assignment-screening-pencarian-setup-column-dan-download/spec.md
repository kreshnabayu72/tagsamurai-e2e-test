---
id: TC-FA-SU-E2E-101-popup-detail-group-assignment-screening-pencarian-setup-column-dan-download
title: "Popup Detail Group Assignment: Screening, Pencarian, Setup Column, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-901
  - TC-FA-SU-902
  - TC-FA-SU-903
  - TC-FA-SU-1056
coverage:
  web: automated
---

# Popup Detail Group Assignment: Screening, Pencarian, Setup Column, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Wawan Setiawan (Pre-setup #23: Manage files pada IT Infrastructure dan Branch Surabaya; Manage purchase pada General Affairs dan Logistics Warehouse; Manage group pada Branch Surabaya, Finance & Accounting, dan Logistics Warehouse). Role tanpa grup (Expected c TC-FA-SU-902) memakai Group Role Manage user & role Wawan Setiawan tanpa grup (Pre-setup #45, varian `FaUserGR`); data itu disediakan tim FE. Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis: pembacaan isi berkas CSV dan XLSX hasil unduhan (nama berkas dan jumlah baris) disediakan tim FE. Berkas yang diunduh dibuang sesudah spec.
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan. Setup Column popup tidak disimpan, tidak ada preferensi kolom yang perlu dipulihkan.

## Test Steps

### TC-FA-SU-901: Screening popup Detail Group Assignment

1. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
2. Klik `[Detail]` pada baris Manage purchase
3. Verifikasi header `Group Assignment` dengan close `[×]` tampil
4. Verifikasi Subtitle nama role `Manage purchase` tampil
5. Verifikasi toolbar menampilkan kolom pencarian dengan placeholder `Search groups...` dan tombol Download berlabel `Download`
6. Verifikasi tabel Group | C | R | U | D read-only tanpa checkbox interaktif
7. Verifikasi tabel tanpa aksi baris (kolom Actions hanya memuat header ⋯ sebagai pintu Column Visibility)
8. Verifikasi dimensi yang tidak applicable tidak dirender sebagai kolom
9. Verifikasi tidak ada tombol footer

### TC-FA-SU-1056: Setup Column popup Detail Group Assignment

10. Klik header kolom Actions (⋯) pada tabel popup
11. Verifikasi overlay Column Visibility tampil dengan tooltip `Column Visibility` pada header
12. Verifikasi kolom Actions tidak memuat aksi baris
13. Verifikasi kolom Group tercantum Hideable (tercentang, Enabled) pada Column Visibility
14. Verifikasi kolom C/R/U/D tidak tercantum di Column Visibility dan selalu tampil
15. Hapus centang Group
16. Verifikasi kolom Group tersembunyi dengan kolom C/R/U/D tetap tampil
17. Centang kembali Group
18. Verifikasi kolom Group pulih

### TC-FA-SU-902: Pencarian, penutupan, dan klik backdrop

19. Ketik Search `General`, tekan Enter
20. Verifikasi baris General Affairs tampil
21. Verifikasi baris Logistics Warehouse tidak tampil
22. Ganti isi kotak Search dengan `zzz`, tekan Enter
23. Verifikasi empty state `No results found` dan `Try adjusting your search or filter.` tampil
24. Klik backdrop
25. Verifikasi popup tidak tertutup
26. Tekan Esc
27. Verifikasi popup tertutup
28. Klik `[Detail]` pada baris role tanpa grup
29. Verifikasi empty state `No groups assigned yet` dengan `This role has no group assignments.` tampil
30. Klik `[×]`
31. Verifikasi popup tertutup

### TC-FA-SU-903: Download popup Detail Group Assignment

32. Klik `[Detail]` pada baris Manage purchase lalu ketik Search `General`, tekan Enter
33. Klik Download
34. Verifikasi format picker memuat CSV dan XLSX
35. Pilih CSV
36. Verifikasi tidak ada toast sukses
37. Verifikasi filename `Group-Assignment-Wawan-Setiawan-Manage-purchase-document`
38. Verifikasi baris yang diekspor sama dengan hasil Search aktif
39. Klik Download lalu pilih XLSX
40. Verifikasi filename `Group-Assignment-Wawan-Setiawan-Manage-purchase-document` dan baris yang diekspor sama dengan hasil Search aktif

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan melewati sekitar 35 langkah: seluruh blok memakai popup Detail Group Assignment yang sama pada data tanpa mutasi dan semuanya satu kelas (fungsional, tanpa harness); satu pembukaan popup dipakai berulang untuk TC-FA-SU-901, TC-FA-SU-1056, dan TC-FA-SU-902 (bagian 3, halaman yang sama dipakai berulang). Pemisahan akan mengulang hook, login, dan pembukaan Detail tanpa makna baru, dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Wawan Setiawan dan popup, mencentang kembali Group (pemulihan Setup Column), dan membuka ulang popup untuk Download. Download kegagalan ada pada spec lain.
- Temuan untuk QA (S-15): (1) TC-FA-SU-902 langkah 5 ("Buka Detail role tanpa grup") tidak menyebut role; spec memakai Group Role Manage user & role tanpa grup dari Pre-setup #45 yang tidak tertulis pada precondition TC. (2) Keyword tanpa hasil pada TC-FA-SU-902 ditulis `zzz`. (3) TC-FA-SU-903 menyebut format CSV dan XLSX tanpa memberi isi berkas; spec hanya mengasersi nama berkas dan jumlah baris (isi sel adalah kelas f). (4) Expected b TC-FA-SU-901 menyebut tutup lewat `[×]` atau Esc; diamati pada TC-FA-SU-902.
