---
id: TC-FA-SU-E2E-115-tabel-user-list-search-bagian-1
title: "Tabel User List: Search (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-324
  - TC-FA-SU-325
  - TC-FA-SU-326
  - TC-FA-SU-327
coverage:
  web: automated
---

# Tabel User List: Search (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Kolom `Activation Status`, `Temporary User`, dan `Shift` ditampilkan lewat Setup Column pada langkah 8 dan 15.
- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-324: Search kelas badge

1. Ketik Search `Branch` (kolom Home Group), tekan Enter
2. Verifikasi tabel menyisakan `Eka Wulandari`, `Fajar Nugroho`, `Lukman Hakim`, `Umar Faruq` (4 baris)
3. Klik `(←)` pada kotak Search

### TC-FA-SU-325: Search kelas user

4. Ketik Search `Dahlan` (kolom Modified By), tekan Enter
5. Verifikasi tabel menyisakan `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Eka Wulandari`, `Gita Permata`, `Hana Kusuma` (18 baris: 17 baris ber-Modified By `Ahmad Dahlan` ditambah baris `Ahmad Dahlan` yang cocok lewat kolom Name, Pre-setup #43)
6. Klik `(←)` pada kotak Search

### TC-FA-SU-326: Search kelas enum

7. Klik header kolom Actions (⋯), klik `Setup Column...`
8. Centang `Activation Status` dan `Temporary User`, klik `[Save]`
9. Klik icon Search, ketik `Pending` (kolom Activation Status), tekan Enter
10. Verifikasi tabel menyisakan `Hana Kusuma`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim` (4 baris)
11. Ganti isi kotak search dengan `Yes` (kolom Temporary User), tekan Enter
12. Verifikasi tabel menyisakan `Fajar Nugroho` (1 baris)
13. Klik `(←)` pada kotak Search

### TC-FA-SU-327: Search kelas cf

14. Klik header kolom Actions (⋯), klik `Setup Column...`
15. Centang `Shift`, klik `[Save]`
16. Klik icon Search, ketik `Night` (kolom Shift), tekan Enter
17. Verifikasi tabel menyisakan `Citra Lestari`, `Eka Wulandari`, `Indra Wijaya`, `Lukman Hakim`, `Oscar Pranata`, `Rina Susanti` (10 baris)
18. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 3, 6, 13, 18 (menutup Search), 7, 8, 14, dan 15 (menampilkan kolom curated lewat Setup Column).
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis.
