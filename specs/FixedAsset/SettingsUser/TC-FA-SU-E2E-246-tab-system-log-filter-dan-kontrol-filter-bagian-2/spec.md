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

1. Buka Detail pengguna Budi Santoso lalu klik tab System Log
2. Ketik Search `Revert`, tekan Enter
3. Klik icon Filter
4. Buka dropdown Action, centang `Activate`
5. Klik `[Apply]`
6. Verifikasi Search `Revert` lalu Filter Action `Activate`: hasil irisan tidak ada baris (0 baris), empty state `No results found` tampil
7. Verifikasi keyword Search `Revert` tidak dikosongkan oleh Filter
8. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
9. Buka dropdown Action, centang `Activate`
10. Klik `[Apply]`
11. Ketik Search `Revert`, tekan Enter
12. Verifikasi Filter Action `Activate` lalu Search `Revert`: hasil identik, tidak ada baris (0 baris), empty state `No results found` tampil
13. Verifikasi Filter Action `Activate` tidak direset oleh Search
14. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah

### TC-FA-SU-749: Pelepasan kontrol

15. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
16. Klik icon Filter untuk menutup panel
17. Ketik Search `Revert`, tekan Enter
18. Klik icon Filter
19. Buka dropdown Action, centang `Activate`
20. Klik `[Apply]`
21. Klik header Date satu kali
22. Klik `[Clear Field]` lalu `[Apply]`
23. Verifikasi Search `Revert` tetap berlaku: S-2 (1 baris)
24. Verifikasi Sort Date tetap berlaku
25. Buka dropdown Action, centang `Activate`
26. Klik `[Apply]`
27. Klik `(←)` pada kotak Search
28. Verifikasi Filter Action `Activate` tetap berlaku (chip `Activate` tampil)
29. Verifikasi Sort Date tetap berlaku
30. Ketik Search `Revert`, tekan Enter
31. Klik header Action
32. Verifikasi sort pindah ke kolom Action
33. Verifikasi Search `Revert` tidak direset
34. Verifikasi Filter Action `Activate` tidak direset
35. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
36. Klik `(←)` pada kotak Search
37. Verifikasi baris yang cocok pulih: S-7
38. Klik `[Clear Field]` lalu `[Apply]`, lalu klik icon Filter untuk menutup panel

### TC-FA-SU-750: Perilaku Filter Panel

39. Klik icon Filter
40. Buka dropdown Action, centang `Edit` tanpa `[Apply]`
41. Klik di luar panel
42. Klik icon Filter
43. Verifikasi panel menampilkan nilai ter-Apply terakhir (perubahan dibuang)
44. Verifikasi tabel tidak berubah
45. Buka dropdown Action, centang `Assign`, klik `[Apply]`
46. Verifikasi badge titik tampil pada ikon Filter saat panel terbuka
47. Klik icon Filter untuk menutup panel
48. Verifikasi badge titik tampil pada ikon Filter saat panel tertutup
49. Klik icon Filter
50. Klik `[Clear Field]` lalu `[Apply]`
51. Verifikasi badge titik hilang
52. Buka dropdown Action
53. Verifikasi dropdown Action menampilkan opsi lain (`Edit` dan `Assign` tampil)
54. Verifikasi dropdown tidak memiliki opsi untuk nilai kosong
55. Centang `Edit`, klik `[Apply]`
56. Verifikasi hasil memuat sedikitnya satu baris
57. Verifikasi tidak ada baris dengan nilai kosong pada hasil
58. Klik header Column Visibility (⋯), hilangkan centang kolom Action
59. Klik icon Filter
60. Verifikasi field filter Action tetap ada di Filter Panel
61. Verifikasi filter ter-Apply tetap berlaku
62. Klik `[Clear Field]` lalu `[Apply]`, lalu klik header Column Visibility (⋯) dan centang kembali kolom Action

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Asersi tambahan di luar Expected (S-03): `Verifikasi` pada langkah 53 membuktikan opsi pembanding tampil di dropdown Action sebagai anchor positif sebelum asersi absence opsi nilai kosong (bagian 8b butir 2).
- Asersi tambahan di luar Expected (S-03): empty state `No results found` pada asersi hasil 0 baris TC-FA-SU-748, sebagai anchor positif absence (bagian 8b butir 2).
- Spec ini berjumlah 62 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) TC-FA-SU-748 menulis hasil irisan 0 baris tanpa menyebut empty state; spec menambahkan `Verifikasi` empty state `No results found` sebagai anchor positif. Butir d (kembali ke halaman 1 saat kriteria berubah) tidak dapat dibedakan pada fixture satu halaman. (3) TC-FA-SU-749: kombinasi Search `Revert` dan Filter Action `Activate` sudah menghasilkan 0 baris (irisan kosong), sehingga butir d diasersi dari kombinasi itu tanpa kata kunci tambahan; TC tidak menyebut kata kunci tanpa hasil secara konkret. (4) TC-FA-SU-750 butir c (memilih opsi apa pun menyaring keluar baris bernilai kosong) tidak punya baris bernilai kosong pada seed #28; spec memverifikasi bahwa dropdown tidak memuat opsi kosong dan hasil filter tidak memuat baris bernilai kosong, tanpa data kosong khusus.
- Klik header Column Visibility (`⋯`) dihitung sebagai klik luar panel Filter sehingga menutup panel (konvensi prd-conventions 9.8); `Klik icon Filter` berikutnya membuka kembali panel dengan nilai terakhir yang sudah diterapkan, dan nilai draft yang belum diterapkan dibuang.
