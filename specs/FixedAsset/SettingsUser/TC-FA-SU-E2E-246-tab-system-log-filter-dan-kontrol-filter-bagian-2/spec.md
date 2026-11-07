---
id: TC-FA-SU-E2E-246-tab-system-log-filter-dan-kontrol-filter-bagian-2
title: "Tab System Log: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-748
  - TC-FA-SU-749
  - TC-FA-SU-750
coverage:
  web: automated
---

# Tab System Log: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan System Log (#28). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab System Log Budi Santoso (Pre-setup #28, 7 baris; urutan default Date descending; kolom Name berisi target perubahan). Alias baris yang dipakai langkah (Action | Name | Field):
  - S-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`
  - S-2: `Auto-Revert` | `Oscar Pranata` | `Group Manager — IT Infrastructure`
  - S-3: `Edit` | `Oscar Pranata` | `Manage group — IT Infrastructure — Update`
  - S-4: `Assign` | `Lina Marlina` | `Access Level`
  - S-5: `Assign` | `Eka Wulandari` | `Manage group — Finance & Accounting`
  - S-6: `Assign` | `Eka Wulandari` | `Manage accounting`
  - S-7: `Activate` | `Eka Wulandari` | `Status`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed System Log #28 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface System Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-748: Kombinasi Search dan Filter dua arah

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab System Log
3. Ketik Search `Revert`, tekan Enter
4. Verifikasi keyword Search `Revert` menyisakan S-2 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
5. Klik icon Filter
6. Buka dropdown Action, centang `Activate`
7. Klik `[Apply]`
8. Verifikasi Search `Revert` lalu Filter Action `Activate`: hasil irisan tidak memuat baris seed (0 baris seed; baris non-seed yang memenuhi kedua kriteria boleh ikut tampil)
9. Verifikasi keyword Search `Revert` tidak dikosongkan oleh Filter
10. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
11. Buka dropdown Action, centang `Activate`
12. Klik `[Apply]`
13. Verifikasi Filter Action `Activate` menyisakan S-7 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
14. Ketik Search `Revert`, tekan Enter
15. Verifikasi Filter Action `Activate` lalu Search `Revert`: hasil identik, tidak memuat baris seed (0 baris seed; baris non-seed yang memenuhi kedua kriteria boleh ikut tampil)
16. Verifikasi Filter Action `Activate` tidak direset oleh Search
17. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah

### TC-FA-SU-749: Pelepasan kontrol

18. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
19. Klik icon Filter untuk menutup panel
20. Ketik Search `Revert`, tekan Enter
21. Klik icon Filter
22. Buka dropdown Action, centang `Activate`
23. Klik `[Apply]`
24. Klik header Date satu kali
25. Klik `[Clear Field]` lalu `[Apply]`
26. Verifikasi Search `Revert` tetap berlaku: S-2 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
27. Verifikasi Sort Date tetap berlaku
28. Buka dropdown Action, centang `Activate`
29. Klik `[Apply]`
30. Klik `(←)` pada kotak Search
31. Verifikasi Filter Action `Activate` tetap berlaku (chip `Activate` tampil)
32. Verifikasi Sort Date tetap berlaku
33. Ketik Search `Revert`, tekan Enter
34. Klik header Action
35. Verifikasi sort pindah ke kolom Action
36. Verifikasi Search `Revert` tidak direset
37. Verifikasi Filter Action `Activate` tidak direset
38. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
39. Klik `(←)` pada kotak Search
40. Verifikasi baris yang cocok pulih: S-7
41. Klik `[Clear Field]` lalu `[Apply]`, lalu klik icon Filter untuk menutup panel

### TC-FA-SU-750: Perilaku Filter Panel

42. Klik icon Filter
43. Buka dropdown Action, centang `Edit` tanpa `[Apply]`
44. Klik di luar panel
45. Klik icon Filter
46. Verifikasi panel menampilkan nilai ter-Apply terakhir (perubahan dibuang)
47. Verifikasi tabel tidak berubah
48. Buka dropdown Action, centang `Assign`, klik `[Apply]`
49. Verifikasi badge titik tampil pada ikon Filter saat panel terbuka
50. Klik icon Filter untuk menutup panel
51. Verifikasi badge titik tampil pada ikon Filter saat panel tertutup
52. Klik icon Filter
53. Klik `[Clear Field]` lalu `[Apply]`
54. Verifikasi badge titik hilang
55. Buka dropdown Action
56. Verifikasi dropdown Action menampilkan opsi lain (`Edit` dan `Assign` tampil)
57. Verifikasi dropdown tidak memiliki opsi untuk nilai kosong
58. Centang `Edit`, klik `[Apply]`
59. Verifikasi hasil memuat sedikitnya satu baris
60. Verifikasi tidak ada baris dengan nilai kosong pada hasil
61. Klik header Column Visibility (⋯), hilangkan centang kolom Action
62. Klik icon Filter
63. Verifikasi field filter Action tetap ada di Filter Panel
64. Verifikasi filter ter-Apply tetap berlaku
65. Klik `[Clear Field]` lalu `[Apply]`, lalu klik header Column Visibility (⋯) dan centang kembali kolom Action

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (Ketik Search `Budi Santoso` di User List untuk menemukan baris target sebelum membuka Detail, R-16, butir 8b.13); User List memuat 25 pengguna pada 3 halaman sehingga posisi baris tidak diandalkan.
- Asersi tambahan di luar Expected (S-03): `Verifikasi` pada langkah 56 membuktikan opsi pembanding tampil di dropdown Action sebagai anchor positif sebelum asersi absence opsi nilai kosong (bagian 8b butir 2).
- Asersi tambahan di luar Expected (S-03): `Verifikasi` langkah 4 (Search `Revert` menyisakan S-2) dan langkah 13 (Filter Action `Activate` menyisakan S-7) sebagai anchor positif sebelum asersi irisan tanpa baris seed pada TC-FA-SU-748 (bagian 8b butir 2).
- Spec ini berjumlah 65 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) TC-FA-SU-748 menulis hasil irisan sebagai tidak memuat baris seed (baris non-seed boleh ikut tampil) tanpa menyebut empty state; spec tidak mengasersi empty state di TC ini dan menambahkan `Verifikasi` baris seed tunggal (S-2, S-7) sebagai anchor positif. Butir d (kembali ke halaman 1 saat kriteria berubah) tidak dapat dibedakan pada fixture satu halaman. (3) TC-FA-SU-749: kombinasi Search `Revert` dan Filter Action `Activate` sudah menghasilkan 0 baris (irisan kosong), sehingga butir d diasersi dari kombinasi itu tanpa kata kunci tambahan; TC tidak menyebut kata kunci tanpa hasil secara konkret. (4) TC-FA-SU-750 butir c (memilih opsi apa pun menyaring keluar baris bernilai kosong) tidak punya baris bernilai kosong pada seed #28; spec memverifikasi bahwa dropdown tidak memuat opsi kosong dan hasil filter tidak memuat baris bernilai kosong, tanpa data kosong khusus. (5) Ketidakselarasan irisan kosong: langkah 8 dan 15 menulis irisan Search `Revert` dengan Filter Action `Activate` sebagai "0 baris seed" (baris non-seed boleh ikut tampil, tanpa asersi empty state) mengikuti TC-FA-SU-748 dan 749, sedangkan langkah 38 mengasersi kombinasi 0 baris menampilkan `No results found`; kedua penulisan tidak selaras untuk kombinasi yang sama. Akarnya di TC-FA-SU-749 butir d, yang menyebut hasil kosong tanpa kualifier seed; mohon TC diselaraskan.
- Klik header Column Visibility (`⋯`) dihitung sebagai klik luar panel Filter sehingga menutup panel (konvensi prd-conventions 9.8); `Klik icon Filter` berikutnya membuka kembali panel dengan nilai terakhir yang sudah diterapkan, dan nilai draft yang belum diterapkan dibuang.
