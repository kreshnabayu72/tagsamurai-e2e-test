---
id: TC-FA-SU-E2E-116-tabel-user-list-search-bagian-2
title: "Tabel User List: Search (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-328
  - TC-FA-SU-329
  - TC-FA-SU-330
coverage:
  web: automated
---

# Tabel User List: Search (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Nilai Search kolom non-searchable: Last Updated `10/06/26 08:30` dan Temporary Until `31/12/26`.

## Test Steps

### TC-FA-SU-328: Siklus interaksi Search

1. Klik icon Search
2. Verifikasi input Search melebar
3. Verifikasi kursor fokus pada input Search
4. Verifikasi placeholder `Search by name, position, division...`
5. Hover icon Search
6. Verifikasi tooltip `Search` tampil
7. Ketik `B` (satu karakter dari `Budi`)
8. Verifikasi icon ✕ muncul di kanan input
9. Verifikasi tabel belum tersaring
10. Ketik sisa `udi`, tekan Enter
11. Verifikasi tabel tersaring menjadi `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim`
12. Klik ✕
13. Verifikasi input kosong
14. Verifikasi search bar tetap terbuka
15. Verifikasi kursor fokus pada input Search
16. Verifikasi tabel tetap menampilkan hasil search terakhir
17. Tekan Enter pada input kosong
18. Verifikasi tabel kembali ke semua baris
19. Ketik `Budi`, tekan Enter, lalu klik ←
20. Verifikasi search bar menutup
21. Verifikasi keyword dikosongkan
22. Verifikasi tabel langsung kembali ke semua baris
23. Klik Search, ketik `  Budi  ` (spasi awal dan akhir), tekan Enter
24. Verifikasi hasil sama dengan `Budi` tanpa spasi: `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim`
25. Verifikasi isi input tidak berubah (`  Budi  `)
26. Klik `(←)` pada kotak Search

### TC-FA-SU-329: Guard kolom non-searchable

27. Klik icon Search, ketik `10/06/26 08:30` (nilai kolom Last Updated), tekan Enter
28. Verifikasi empty state `No results found` tampil (penyaringan kolom Last Updated hanya lewat Filter Panel)
29. Ganti isi kotak search dengan `31/12/26` (nilai kolom Temporary Until), tekan Enter
30. Verifikasi empty state `No results found` tampil (penyaringan kolom Temporary Until hanya lewat Filter Panel)
31. Klik `(←)` pada kotak Search

### TC-FA-SU-330: Search terikat visibilitas kolom Name

32. Klik icon Search, ketik `Budi`, tekan Enter
33. Verifikasi sebelum hide: tabel menyisakan `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim`
34. Klik header ⋯, hapus centang `Name`
35. Ganti isi kotak search dengan `Budi`, tekan Enter
36. Verifikasi setelah kolom Name di-hide: tabel menyisakan `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim`
37. Klik header ⋯, centang kembali `Name`
38. Ganti isi kotak search dengan `Budi`, tekan Enter
39. Verifikasi setelah kolom Name di-unhide: hasil kembali `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim`
40. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 26, 31, 40 (menutup Search).
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis. (2) Expected b TC-FA-SU-330 (kolom Name di-hide) memuat daftar yang sama dengan Expected a; spec mengasersi sebagaimana tertulis.
- Alasan di atas sekitar 35 langkah: ketiga blok Search satu kelas fungsional pada halaman, akun, dan dataset yang sama tanpa mengubah data; TC-FA-SU-328 memuat 26 klausa Expected yang masing-masing satu `Verifikasi` (S-01) sehingga tidak dapat dirampingkan, dan TC-FA-SU-329 dan 330 berdiri sendiri sehingga kegagalan blok sebelumnya tidak menghilangkan maknanya (bagian 3 prinsip 13).
