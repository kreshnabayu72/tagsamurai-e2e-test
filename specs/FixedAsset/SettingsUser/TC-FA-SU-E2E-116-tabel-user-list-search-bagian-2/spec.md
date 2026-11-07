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
- Email enam baris hasil Search `Budi` pada langkah 41 (`budi.santoso@corp.id`, `doni.prasetyo@corp.id`, `fajar.nugroho@corp.id`, `indra.wijaya@corp.id`, `kartika.sari@corp.id`, `lukman.hakim@corp.id`) dirujuk lewat `Fixture.fa-settings-user.<kunci>` per baris (nilai dari Pre-setup #43), bukan ditulis mentah di script.
- Nilai Search kolom non-searchable: Last Updated `10/06/26 08:30` (baris Ahmad Dahlan, kolom tampil secara default) dan Temporary Until `31/12/26` (baris Fajar Nugroho, Pre-setup #43). Kolom Temporary Until berkelas Curated (tersembunyi secara default) sehingga dicentang lewat overlay Column Visibility sebagai precondition asersi nilai Date; preferensi kolom itu dipulihkan hook `after` (bukan objek uji, 8b.14).

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

27. Ketik Search `Ahmad Dahlan`, tekan Enter
28. Verifikasi baris `Ahmad Dahlan` menampilkan Last Updated `10/06/26 08:30`
29. Klik header ⋯, centang `Temporary Until`
30. Ganti isi kotak search dengan `Fajar Nugroho`, tekan Enter
31. Verifikasi baris `Fajar Nugroho` menampilkan Temporary Until `31/12/26`
32. Ganti isi kotak search dengan `10/06/26 08:30` (nilai kolom Last Updated), tekan Enter
33. Verifikasi empty state `No results found` tampil (penyaringan kolom Last Updated hanya lewat Filter Panel)
34. Ganti isi kotak search dengan `31/12/26` (nilai kolom Temporary Until), tekan Enter
35. Verifikasi empty state `No results found` tampil (penyaringan kolom Temporary Until hanya lewat Filter Panel)
36. Klik `(←)` pada kotak Search

### TC-FA-SU-330: Search terikat visibilitas kolom Name

37. Klik icon Search, ketik `Budi`, tekan Enter
38. Verifikasi sebelum hide: tabel menyisakan `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim`
39. Klik header ⋯, hapus centang `Name`
40. Ganti isi kotak search dengan `Budi`, tekan Enter
41. Verifikasi setelah kolom Name di-hide (baris diidentifikasi lewat kolom Email karena Name tersembunyi): tabel menyisakan enam baris dengan Email `budi.santoso@corp.id`, `doni.prasetyo@corp.id`, `fajar.nugroho@corp.id`, `indra.wijaya@corp.id`, `kartika.sari@corp.id`, `lukman.hakim@corp.id`
42. Klik header ⋯, centang kembali `Name`
43. Ganti isi kotak search dengan `Budi`, tekan Enter
44. Verifikasi setelah kolom Name di-unhide: hasil kembali `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim`
45. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 26, 36, 45 (menutup Search), 27 dan 30 (Search untuk menemukan baris Ahmad Dahlan dan Fajar Nugroho sebelum nilai Date diverifikasi, R-16), dan 29 (menampilkan kolom Curated Temporary Until sebagai precondition).
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis. (2) Expected b TC-FA-SU-330 (kolom Name di-hide) memuat daftar yang sama dengan Expected a; spec mengasersi sebagaimana tertulis. (3) Expected b TC-FA-SU-330 menyebut nama baris pada kolom Name yang di-hide; spec mengidentifikasi baris lewat kolom Email (nilai dari Pre-setup #43) dan tidak mengasersi nama yang tidak tampil. (4) TC-FA-SU-329 tidak menyebut cara membuktikan nilai Date tampil di tabel; spec menambah pencarian baris Ahmad Dahlan dan Fajar Nugroho serta mencentang kolom Temporary Until agar nilai Date terbukti tampil sebelum diketik sebagai Search (8b.15 b).
- Alasan di atas sekitar 35 langkah: ketiga blok Search satu kelas fungsional pada halaman, akun, dan dataset yang sama tanpa mengubah data; TC-FA-SU-328 memuat 26 klausa Expected yang masing-masing satu `Verifikasi` (S-01) sehingga tidak dapat dirampingkan, dan TC-FA-SU-329 dan 330 berdiri sendiri sehingga kegagalan blok sebelumnya tidak menghilangkan maknanya (bagian 3 prinsip 13).
