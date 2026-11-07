---
id: TC-FA-SU-E2E-283-tab-user-log-sub-tab-assignment-setup-column-pagination-dan-tooltip-icon
title: "Tab User Log sub-tab Assignment: Setup Column, Pagination, dan Tooltip Icon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-862
  - TC-FA-SU-863
  - TC-FA-SU-868
coverage:
  web: automated
---

# Tab User Log sub-tab Assignment: Setup Column, Pagination, dan Tooltip Icon

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Assignment Budi Santoso (Pre-setup #30, 5 baris; urutan default Date descending): dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-862: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column

1. Ketik Search `Budi Santoso`, tekan Enter, buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Assignment
2. Buka Setup Column, sembunyikan satu kolom dan pin satu kolom
3. Klik `[Reset to Default]`
4. Verifikasi visibility, urutan, dan pin kembali ke default modul pada preview
5. Klik `[Save]`
6. Verifikasi konfigurasi default menjadi permanen setelah `[Save]`
7. Buka Setup Column, sembunyikan satu kolom, lalu tutup lewat ✕
8. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
9. Buka Setup Column, sembunyikan satu kolom, lalu tekan Esc
10. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
11. Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka tabel lain yang punya Setup Column (User List)
12. Verifikasi konfigurasi tabel lain tidak terpengaruh perubahan tabel ini (cache per tabel)
13. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-863: Pagination: page size, navigasi, dan kasus tepi

14. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, klik nama Budi Santoso, lalu buka tab User Log, sub-tab Assignment
15. Verifikasi default 10 baris per halaman
16. Klik dropdown page size
17. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
18. Tekan Esc untuk menutup dropdown page size
19. Isi nomor halaman `0`, tekan Enter
20. Verifikasi tabel tetap di halaman 1
21. Isi nomor halaman `-1`, tekan Enter
22. Verifikasi tabel tetap di halaman 1
23. Isi nomor halaman `999`, tekan Enter
24. Verifikasi tabel tetap di halaman 1
25. Isi nomor halaman `abc`, tekan Enter
26. Verifikasi tabel tetap di halaman 1
27. Ganti page size ke 25
28. Verifikasi tabel menampilkan halaman 1
29. Ganti page size kembali ke 10
30. Verifikasi tabel menampilkan halaman 1
31. Klik header Date satu kali
32. Verifikasi tabel menampilkan halaman 1
33. Klik header Date dua kali lagi hingga netral
34. Ketik Search `Unassigned`, tekan Enter
35. Verifikasi tabel menampilkan halaman 1
36. Klik icon ← pada kotak Search

### TC-FA-SU-868: Tooltip icon Table Tools dan header Actions

37. Hover icon Search
38. Verifikasi tooltip `Search`
39. Hover icon Filter
40. Verifikasi tooltip `Filter`
41. Hover icon Download
42. Verifikasi tooltip `Download`
43. Hover header kolom Actions (⋯)
44. Verifikasi tooltip `Column Visibility`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan ulang Detail Budi Santoso > User Log > Assignment sesudah User List dan muat ulang (langkah 14), pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung pencarian baris (S-03, R-16, bagian 8b butir 13): langkah 1 dan 14 mencari pengguna lewat Search nama persis `Budi Santoso` (nama Pre-setup) sebelum membuka Detail, karena User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman) sehingga spec tidak mengandalkan posisi baris di halaman. Sesudah muat ulang atau kembali ke User List (langkah 11 sampai 13), kotak Search mempertahankan nilainya sehingga langkah 14 ditulis "ganti isi kotak search" (bagian 8b butir 9).
- Langkah 16 (`Klik dropdown page size`) dan langkah 18 (`Tekan Esc untuk menutup dropdown page size`) mengikuti Langkah Uji TC (klik dropdown page size, amati pilihan, tutup dengan Esc) sehingga pilihan page size diasersi saat dropdown terbuka.
- Spec ini berjumlah 44 langkah dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- TC-FA-SU-859 dan TC-FA-SU-860 ada di spec 282; TC-FA-SU-861 ada di spec 293.
- Temuan untuk QA (S-15): (0) Langkah `[Save]` pada langkah 11 ("Buka Setup Column, sembunyikan satu kolom, klik `[Save]`, lalu buka tabel lain") ditambahkan spec tanpa dasar TC: TC-FA-SU-862 langkah 4 dan 5 hanya menutup lewat ✕ atau Esc, dan langkah 6 membandingkan tabel lain tanpa menyebut Save. Save dipilih agar perubahan tersimpan di tabel ini sebelum dibandingkan dengan User List (Expected c); pemilik TC perlu mengonfirmasi atau menyatakan cara lain. (1) TC-FA-SU-863: Expected e (fixture satu halaman, multi-halaman diuji di TC-FA-SU-359 dan TC-FA-SU-1057) adalah catatan tanpa langkah observasi sehingga tidak diasersi. Post Condition preferensi kolom tersimpan per perangkat (atau kembali ke default) tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan. Spec ini menyimpan konfigurasi Setup Column di browser; `suite.md` belum mencantumkan daftar spec yang menyimpan konfigurasi kolom (bagian 4 konvensi), sehingga perlu ditambahkan tim FE.
