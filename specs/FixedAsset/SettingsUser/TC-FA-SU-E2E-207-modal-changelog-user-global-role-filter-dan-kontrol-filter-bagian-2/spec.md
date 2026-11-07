---
id: TC-FA-SU-E2E-207-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-2
title: "Modal Changelog User > Global Role: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-623
  - TC-FA-SU-624
  - TC-FA-SU-625
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Global Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | Role Name | Field; Modified By):
  - G-1: `Remove` | `Manage global license` | `Manage global license`; Modified By `Lina M`
  - G-2: `Remove (via Total Control)` | `Manage global license` | `Access`; Modified By `Ahmad D`
  - G-3: `Assign (via Total Control)` | `Import Data` | `Access`; Modified By `Ahmad D`
  - G-4: `Edit` | `Manage asset master data` | `Manage asset master data — Delete`; Modified By `Ahmad D`
  - G-5: `Assign` | `Manage accounting` | `Manage accounting`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-623: Pelepasan kontrol

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
2. Ketik Search `Assign`, tekan Enter
3. Klik icon Filter
4. Buka dropdown Action, centang `Assign`
5. Klik `[Apply]`
6. Klik header Date satu kali
7. Klik `[Clear Field]` lalu `[Apply]`
8. Verifikasi Search `Assign` tetap berlaku: G-1, G-2, G-3, G-5 (4 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
9. Verifikasi Sort Date tetap berlaku
10. Buka dropdown Action, centang `Assign`
11. Klik `[Apply]`
12. Klik `(←)` pada kotak Search
13. Verifikasi Filter Action `Assign` tetap berlaku (chip `Assign` tampil)
14. Verifikasi Sort Date tetap berlaku
15. Ketik Search `Assign`, tekan Enter
16. Klik header Action
17. Verifikasi sort pindah ke kolom Action
18. Verifikasi Search `Assign` tidak direset
19. Verifikasi Filter Action `Assign` tidak direset
20. Ganti isi kotak search dengan `Zzzz` (tidak ada hasilnya), tekan Enter
21. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
22. Klik `(←)` pada kotak Search
23. Verifikasi baris yang cocok pulih: G-5 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
24. Klik `[Clear Field]` lalu `[Apply]`, lalu klik icon Filter untuk menutup panel

### TC-FA-SU-624: Perilaku Filter Panel

25. Klik icon Filter
26. Buka dropdown Action, centang `Edit` tanpa `[Apply]`
27. Klik di luar panel
28. Klik icon Filter
29. Verifikasi panel menampilkan nilai ter-Apply terakhir (perubahan dibuang)
30. Verifikasi tabel tidak berubah
31. Centang `Assign` pada dropdown Action, klik `[Apply]`
32. Verifikasi badge titik tampil pada ikon Filter saat panel terbuka
33. Klik icon Filter untuk menutup panel
34. Verifikasi badge titik tampil pada ikon Filter saat panel tertutup
35. Klik icon Filter
36. Klik `[Clear Field]` lalu `[Apply]`
37. Verifikasi badge titik hilang
38. Buka dropdown Action
39. Verifikasi dropdown Action menampilkan opsi `Edit` dan `Assign`
40. Verifikasi dropdown tidak memiliki opsi untuk nilai kosong
41. Centang `Edit`, klik `[Apply]`
42. Verifikasi hasil memuat sedikitnya satu baris
43. Verifikasi tidak ada baris dengan nilai kosong pada hasil
44. Klik header Column Visibility (⋯), hilangkan centang kolom Action
45. Klik icon Filter
46. Verifikasi field filter Action tetap ada di Filter Panel
47. Verifikasi filter ter-Apply tetap berlaku
48. Klik `[Clear Field]` lalu `[Apply]`, lalu klik header Column Visibility (⋯) dan centang kembali kolom Action

### TC-FA-SU-625: Chip dan checkbox dropdown Filter

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
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Asersi baris seed pada Modal Changelog (audit trail permanen) ditulis relatif terhadap baris seed: urutan relatif dan jumlah baris seed, dengan baris non-seed yang memenuhi kriteria boleh menyisip atau ikut tampil (S-14), mengikuti kualifier Expected TC sumber. TC-FA-SU-623 menulis hasil tanpa jumlah baris; langkah 8 dan 23 memakai kualifier yang sama seperti TC sibling pada surface ini (TC-FA-SU-622 butir a).
- Langkah penghubung tambahan (S-03): langkah 24 (`[Clear Field]` lalu `[Apply]`, lalu tutup panel dengan icon Filter) melepas Filter Action `Assign` yang masih ter-Apply dari TC-FA-SU-623 supaya TC-FA-SU-624 tidak mewarisinya (S-09).
- Asersi tambahan di luar Expected (S-03): langkah 39 (opsi lain tampil di dropdown Action) menjadi anchor positif untuk asersi absence opsi nilai kosong (bagian 8b butir 2).
- Spec ini berjumlah 67 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Kombinasi Search dan Filter pada Expected tidak menyebut nilai konkret; spec memakai keyword dan filter yang sama dengan TC kombinasi pada surface ini, dan keyword tanpa hasil `Zzzz` (modal) dipilih spec. (3) Expected c ("memilih opsi apa pun menyaring keluar baris yang nilainya kosong") tidak punya baris bernilai kosong pada seed #27; spec memverifikasi bahwa dropdown tidak memuat opsi kosong dan hasil filter tidak memuat baris bernilai kosong, tanpa data kosong khusus. (4) Nilai pilihan spec (TC tidak menyebut nilai konkret): kolom sort pengganti `Action` (langkah 16, TC-FA-SU-623 "ganti sort ke kolom lain"); opsi Filter Action `Edit` (langkah 26 dan 41) dan `Assign` (langkah 31) pada TC-FA-SU-624; kolom yang di-hide `Action` (langkah 44); dua opsi `Edit` dan `Assign` (langkah 51 dan 61), keyword kotak cari dropdown `ass` (langkah 64), dan keyword tanpa hasil `zzzz` (langkah 66) pada TC-FA-SU-625. Mohon QA mengonfirmasi atau menetapkan nilainya.
