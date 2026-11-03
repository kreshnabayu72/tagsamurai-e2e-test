---
id: TC-FA-SU-E2E-286-tab-user-log-sub-tab-session-search-dan-sort
title: "Tab User Log sub-tab Session: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-873
  - TC-FA-SU-874
  - TC-FA-SU-875
  - TC-FA-SU-876
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Session Budi Santoso (Pre-setup #30, 9 baris; urutan default Date descending). Label baris = `Date|Note` (kolom Activity bernilai `Session`, kolom Status bernilai `—`); alias dipakai langkah:
  - S-1: `16/07/26 08:12|Session started`
  - S-2: `15/07/26 20:30|Session ended`
  - S-3: `15/07/26 08:00|Session started`
  - S-4: `14/07/26 08:40|Session ended`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-5: `14/07/26 08:05|Session started`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-6: `13/07/26 17:05|Session ended`
  - S-7: `13/07/26 08:10|Session started`
  - S-8: `12/07/26 17:15|Session ended`
  - S-9: `12/07/26 08:02|Session started`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-873: Siklus interaksi Search: reveal, Enter, clear, collapse

1. Buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Session
2. Klik icon Search
3. Verifikasi input melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder `Search note, IP address, or device...`
6. Hover icon Search
7. Verifikasi tooltip `Search`
8. Ketik 1 karakter dari `Session` (`S`)
9. Verifikasi icon ✕ muncul di kanan input
10. Verifikasi tabel belum tersaring
11. Ketik sisa `Session` (`ession`), tekan Enter
12. Verifikasi tabel tersaring menjadi 9 baris, termasuk S-1, S-2, S-3, S-4, S-5, S-6
13. Klik ✕
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input
17. Verifikasi tabel tetap menampilkan hasil search terakhir
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris
20. Ketik Search `Session`, tekan Enter
21. Klik icon ←
22. Verifikasi search bar menutup
23. Verifikasi keyword dikosongkan
24. Verifikasi tabel langsung kembali ke semua baris
25. Klik icon Search, ketik `  Session  ` (spasi awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan `Session` tanpa spasi
27. Verifikasi isi input tidak berubah
28. Klik icon ←

### TC-FA-SU-874: Guard kolom non-searchable: Date

29. Ketik Search `16/07/26 08:12` (nilai kolom Date), tekan Enter
30. Verifikasi `16/07/26 08:12` tidak mencocokkan baris melalui Search dan empty state `No results found` tampil (penyaringan kolom Date hanya lewat Filter Panel)
31. Klik icon ←

### TC-FA-SU-875: Search terikat visibilitas kolom Activity: hide lalu unhide

32. Ketik Search `Session`, tekan Enter
33. Verifikasi sebelum hide: keyword `Session` menyisakan 9 baris, termasuk S-1, S-2, S-3, S-4, S-5, S-6
34. Klik header kolom Column Visibility (⋯), hilangkan centang Activity, tekan Esc
35. Tekan Enter pada kotak Search (keyword `Session`)
36. Verifikasi setelah kolom Activity di-hide: keyword yang sama menyisakan 9 baris, termasuk S-1, S-2, S-3, S-4, S-5, S-6 (kolom tersembunyi tidak dicari; kolom lain yang tampil tetap dicari)
37. Klik header kolom Column Visibility (⋯), centang kembali Activity, tekan Esc
38. Tekan Enter pada kotak Search (keyword `Session`)
39. Verifikasi setelah kolom Activity di-unhide: hasil kembali 9 baris, termasuk S-1, S-2, S-3, S-4, S-5, S-6
40. Klik icon ←

### TC-FA-SU-876: Sort kelas date: Date

41. Klik header Date satu kali
42. Verifikasi Date klik 1 ascending (↑), lima baris pertama: S-9, S-8, S-7, S-6, S-5
43. Klik header Date kedua kali
44. Verifikasi Date klik 2 descending (↓), lima baris pertama: S-1, S-2, S-3, S-4, S-5
45. Klik header Date ketiga kali
46. Verifikasi Date klik 3 netral kembali ke default, lima baris pertama: S-1, S-2, S-3, S-4, S-5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 46 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-873 Expected c: daftar baris tertulis enam dari sembilan ("9 baris"). TC-FA-SU-875: sesudah kolom Activity di-hide, hasil Search `Session` tetap 9 baris karena kolom Note juga memuat teks `Session`, sehingga asersi hide tidak membedakan keadaan sebelum dan sesudah hide; spec mengikuti TC.
