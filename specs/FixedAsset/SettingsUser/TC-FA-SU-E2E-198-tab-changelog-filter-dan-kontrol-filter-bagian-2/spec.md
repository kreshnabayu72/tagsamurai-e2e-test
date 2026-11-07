---
id: TC-FA-SU-E2E-198-tab-changelog-filter-dan-kontrol-filter-bagian-2
title: "Tab Changelog: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-591
  - TC-FA-SU-592
  - TC-FA-SU-593
coverage:
  web: automated
---

# Tab Changelog: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By dalam format `[First Name] [Last Initial]`):
  - T-1: Field `Manage files — IT Infrastructure`, Modified By `Ahmad D`
  - T-2: Field `Manage group — IT Infrastructure — Delete`, Modified By `Ahmad D`
  - T-3: Field `Manage group — IT Infrastructure — Update`, Modified By `Ahmad D`
  - T-4: Field `Home Group`, Modified By `Lina M`
  - T-5: Field `Manage asset master data — Delete`, Modified By `Ahmad D`
  - T-6: Field `Manage accounting`, Modified By `Ahmad D`
  - T-7: Field `Status`, Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-591: Pelepasan kontrol

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
3. Ketik Search `Home`, tekan Enter
4. Klik icon Filter
5. Buka dropdown Action, centang `Activate`
6. Klik `[Apply]`
7. Klik header Date satu kali
8. Klik `[Clear Field]` lalu `[Apply]`
9. Verifikasi Search `Home` tetap berlaku: `Home Group` (T-4; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
10. Verifikasi Sort Date tetap berlaku
11. Buka dropdown Action, centang `Activate`
12. Klik `[Apply]`
13. Klik `(←)` pada kotak Search
14. Verifikasi Filter Action `Activate` tetap berlaku (chip `Activate` tampil)
15. Verifikasi Sort Date tetap berlaku
16. Ketik Search `Home`, tekan Enter
17. Klik header Action
18. Verifikasi sort pindah ke kolom Action
19. Verifikasi Search `Home` tidak direset
20. Verifikasi Filter Action `Activate` tidak direset
21. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
22. Klik `(←)` pada kotak Search
23. Verifikasi baris yang cocok pulih: `Status` (T-7; 1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
24. Klik `[Clear Field]` lalu `[Apply]`, lalu klik icon Filter untuk menutup panel

### TC-FA-SU-592: Perilaku Filter Panel

25. Klik icon Filter
26. Buka dropdown Action, centang `Edit` tanpa `[Apply]`
27. Klik di luar panel
28. Klik icon Filter
29. Verifikasi panel menampilkan nilai ter-Apply terakhir (perubahan dibuang)
30. Verifikasi tabel tidak berubah
31. Centang `Activate` pada dropdown Action, klik `[Apply]`
32. Verifikasi badge titik tampil pada ikon Filter saat panel terbuka
33. Klik icon Filter untuk menutup panel
34. Verifikasi badge titik tampil pada ikon Filter saat panel tertutup
35. Klik icon Filter
36. Klik `[Clear Field]` lalu `[Apply]`
37. Verifikasi badge titik hilang
38. Buka dropdown Action
39. Verifikasi dropdown Action menampilkan opsi `Activate`, `Edit`, dan `Assign`
40. Verifikasi dropdown tidak memiliki opsi untuk nilai kosong
41. Centang `Edit`, klik `[Apply]`
42. Verifikasi hasil memuat sedikitnya satu baris
43. Verifikasi tidak ada baris dengan nilai kosong pada hasil
44. Klik header Column Visibility (⋯), hilangkan centang kolom Action
45. Klik icon Filter
46. Verifikasi field filter Action tetap ada di Filter Panel
47. Verifikasi filter ter-Apply tetap berlaku
48. Klik `[Clear Field]` lalu `[Apply]`, lalu klik header Column Visibility (⋯) dan centang kembali kolom Action

### TC-FA-SU-593: Chip dan checkbox dropdown Filter

49. Klik icon Filter
50. Buka dropdown Action
51. Centang dua opsi (`Edit` dan `Assign`), klik `[Apply]`
52. Verifikasi dua chip tampil di dalam field
53. Verifikasi hasil adalah gabungan (OR) kedua opsi
54. Klik ✕ pada satu chip tanpa membuka dropdown
55. Verifikasi chip itu hilang
56. Buka dropdown Action
57. Verifikasi checkbox opsi terkait ter-uncheck
58. Verifikasi chip lain tetap
59. Hilangkan centang opsi yang tersisa
60. Verifikasi chip yang bersangkutan hilang
61. Centang dua opsi (`Edit` dan `Assign`) lalu hilangkan centang satu opsi
62. Verifikasi chip opsi yang di-uncheck hilang
63. Verifikasi chip lain tetap
64. Ketik `ass` pada kotak cari dropdown
65. Verifikasi opsi dipersempit (substring, tidak case-sensitive)
66. Ganti isi kotak cari dropdown dengan `zzzz`
67. Verifikasi `No results found` tampil di dropdown

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- Langkah penghubung tambahan (S-03): langkah 24 (`[Clear Field]` lalu `[Apply]`, lalu tutup panel dengan icon Filter) melepas Filter Action `Activate` yang masih ter-Apply dari TC-FA-SU-591 supaya TC-FA-SU-592 tidak mewarisinya (S-09).
- Asersi tambahan di luar Expected (S-03): langkah 39 (opsi lain tampil di dropdown Action) menjadi anchor positif untuk asersi absence opsi nilai kosong (bagian 8b butir 2).
- Asersi baris seed pada Tab Changelog (audit trail permanen) ditulis relatif terhadap baris seed: jumlah baris seed, dengan baris non-seed yang memenuhi kriteria boleh ikut tampil (S-14); kualifier ini ditambahkan pada langkah 9 dan 23, mengikuti pola TC sibling pada surface ini.
- Spec ini berjumlah 67 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Kombinasi Search dan Filter pada Expected tidak menyebut nilai konkret; spec memakai keyword dan filter yang sama dengan TC kombinasi pada surface ini, dan keyword tanpa hasil `Zzzz` (modal) dipilih spec. (3) Expected c ("memilih opsi apa pun menyaring keluar baris yang nilainya kosong") tidak punya baris bernilai kosong pada seed #27; spec memverifikasi bahwa dropdown tidak memuat opsi kosong dan hasil filter tidak memuat baris bernilai kosong, tanpa data kosong khusus. (4) TC-FA-SU-592 dan TC-FA-SU-593 tidak menyebut opsi Action dan keyword dropdown; spec memilih opsi `Activate`, `Edit`, `Assign`, keyword dropdown `ass` dan `zzzz` (Search `Home` dan Filter Action `Activate` pada TC-FA-SU-591 berasal dari Data TC).
