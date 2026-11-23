---
id: TC-FA-SU-E2E-278-tab-user-log-sub-tab-assignment-search-dan-sort
title: "Tab User Log sub-tab Assignment: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-842
  - TC-FA-SU-843
  - TC-FA-SU-844
  - TC-FA-SU-845
coverage:
  web: automated
---

# Tab User Log sub-tab Assignment: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Assignment Budi Santoso (Pre-setup #30, 5 baris; urutan default Date descending). Label baris = `Activity|Transaction ID`; alias dipakai langkah:
  - A-1: `Unassigned|ASG-20260618-0089`, Date `30/06/26`, PIC `Eka W` (keyword `Wulandari`)
  - A-2: `Handed over|ASG-20260625-0102`, Name `Lemari`, PIC `Ahmad D`
  - A-3: `Handed over|ASG-20260618-0089`, PIC `Eka W` (keyword `Wulandari`)
  - A-4: `Handed over|ASG-20260512-0067`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
  - A-5: `Handed over|ASG-20260505-0045`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
- Nilai Date seed untuk Search kolom non-searchable: A-1 bernilai `30/06/26`; nilai ini harus tampil pada sel kolom Date tabel sebelum dipakai sebagai keyword.
- Kemampuan seed API: menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-842: Siklus interaksi Search: reveal, Enter, clear, collapse

1. Ketik Search `Budi Santoso`, tekan Enter, buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Assignment
2. Klik icon Search
3. Verifikasi input melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder `Search transaction ID, name, or PIC...`
6. Hover icon Search
7. Verifikasi tooltip `Search`
8. Ketik 1 karakter dari `Unassigned` (`U`)
9. Verifikasi icon ✕ muncul di kanan input
10. Verifikasi tabel belum tersaring
11. Ketik sisa `Unassigned` (`nassigned`), tekan Enter
12. Verifikasi tabel tersaring menjadi A-1 (`Unassigned|ASG-20260618-0089`)
13. Klik ✕
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input
17. Verifikasi tabel tetap menampilkan hasil search terakhir
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris
20. Ketik Search `Unassigned`, tekan Enter
21. Klik icon ←
22. Verifikasi search bar menutup
23. Verifikasi keyword dikosongkan
24. Verifikasi tabel langsung kembali ke semua baris
25. Klik icon Search, ketik `  Unassigned  ` (spasi awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan `Unassigned` tanpa spasi
27. Verifikasi isi input tidak berubah
28. Klik icon ←

### TC-FA-SU-843: Guard kolom non-searchable: Date

29. Verifikasi sel Date baris A-1 pada tabel menampilkan `30/06/26`
30. Ketik Search `30/06/26` (nilai kolom Date), tekan Enter
31. Verifikasi `30/06/26` tidak mencocokkan baris melalui Search dan empty state `No results found` tampil (penyaringan kolom Date hanya lewat Filter Panel)
32. Klik icon ←

### TC-FA-SU-844: Search terikat visibilitas kolom Activity: hide lalu unhide

33. Ketik Search `Unassigned`, tekan Enter
34. Verifikasi sebelum hide: keyword `Unassigned` menyisakan A-1 (`Unassigned|ASG-20260618-0089`)
35. Klik header kolom Column Visibility (⋯), hilangkan centang Activity, tekan Esc
36. Tekan Enter pada kotak Search (keyword `Unassigned`)
37. Verifikasi setelah kolom Activity di-hide: keyword yang sama menyisakan tidak ada baris (kolom tersembunyi tidak dicari; kolom lain yang tampil tetap dicari)
38. Klik header kolom Column Visibility (⋯), centang kembali Activity, tekan Esc
39. Tekan Enter pada kotak Search (keyword `Unassigned`)
40. Verifikasi setelah kolom Activity di-unhide: hasil kembali A-1 (`Unassigned|ASG-20260618-0089`)
41. Klik icon ←

### TC-FA-SU-845: Sort kelas date: Date

42. Klik header Date satu kali
43. Verifikasi Date klik 1 ascending (↑), lima baris pertama: A-5, A-4, A-3, A-2, A-1
44. Klik header Date kedua kali
45. Verifikasi Date klik 2 descending (↓), lima baris pertama: A-1, A-2, A-3, A-4, A-5
46. Klik header Date ketiga kali
47. Verifikasi Date klik 3 netral kembali ke default, lima baris pertama: A-1, A-2, A-3, A-4, A-5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung pencarian baris (S-03, R-16, bagian 8b butir 13): langkah 1 mencari pengguna lewat Search nama persis `Budi Santoso` (nama Pre-setup) sebelum membuka Detail, karena User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman) sehingga spec tidak mengandalkan posisi baris di halaman.
- Spec ini berjumlah 47 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Verifikasi sel Date langkah 29 adalah asersi tambahan di luar Expected TC-FA-SU-843: ditambahkan sebagai langkah penghubung agar nilai Date seed `30/06/26` tampil di sel sebelum dipakai sebagai keyword Search (S-03, bagian 8b butir 15 b).
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-844: setelah kolom Activity di-hide hasil Search `Unassigned` adalah tidak ada baris; asersi tanpa baris memakai `Verifikasi` hasil sebelum hide (A-1) pada surface yang sama sebagai anchor. TC-FA-SU-843 memakai nilai Date `30/06/26` yang hanya diketahui dari urutan sort (A-1).
