---
id: TC-FA-SU-E2E-236-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-2
title: "Modal Combined Changelog: User: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-718
  - TC-FA-SU-719
  - TC-FA-SU-720
coverage:
  web: automated
---

# Modal Combined Changelog: User: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Modal Combined Changelog dibuka dari icon Changelog di Table Tools halaman User List dan memuat riwayat seluruh pengguna Client `FaUserMain`. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Combined Changelog (Pre-setup #27, 6 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | User Name | Field; Modified By dalam format `[First Name] [Last Initial]`):
  - C-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`; Modified By `Ahmad D`
  - C-2: `Deactivate` | `Doni Prasetyo` | `Status`; Modified By `Budi S`
  - C-3: `Edit Home Group` | `Budi Santoso` | `Home Group`; Modified By `Lina M`
  - C-4: `Edit` | `Gita Permata` | `Manage group — Finance & Accounting — Update`; Modified By `Ahmad D`
  - C-5: `Assign` | `Budi Santoso` | `Manage accounting`; Modified By `Ahmad D`
  - C-6: `Activate` | `Eka Wulandari` | `Status`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Combined Changelog dan tidak menambah entri.

## Test Steps

### TC-FA-SU-718: Kombinasi Search dan Filter dua arah

1. Klik icon Changelog di Table Tools halaman User List
2. Ketik Search `Resend`, tekan Enter
3. Verifikasi keyword Search `Resend` menyisakan C-1 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
4. Klik icon Filter
5. Buka dropdown Action, centang `Activate`
6. Klik `[Apply]`
7. Verifikasi Search `Resend` lalu Filter Action `Activate`: hasil irisan tidak memuat baris seed (0 baris seed; baris non-seed yang memenuhi kedua kriteria boleh ikut tampil)
8. Verifikasi keyword Search `Resend` tidak dikosongkan oleh Filter
9. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
10. Buka dropdown Action, centang `Activate`
11. Klik `[Apply]`
12. Verifikasi Filter Action `Activate` menyisakan C-6 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
13. Ketik Search `Resend`, tekan Enter
14. Verifikasi Filter Action `Activate` lalu Search `Resend`: hasil identik, tidak memuat baris seed (0 baris seed; baris non-seed yang memenuhi kedua kriteria boleh ikut tampil)
15. Verifikasi Filter Action `Activate` tidak direset oleh Search
16. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah

### TC-FA-SU-719: Pelepasan kontrol

17. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
18. Klik icon Filter untuk menutup panel
19. Ketik Search `Resend`, tekan Enter
20. Klik icon Filter
21. Buka dropdown Action, centang `Activate`
22. Klik `[Apply]`
23. Klik header Date satu kali
24. Klik `[Clear Field]` lalu `[Apply]`
25. Verifikasi Search `Resend` tetap berlaku: C-1 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
26. Verifikasi Sort Date tetap berlaku
27. Buka dropdown Action, centang `Activate`
28. Klik `[Apply]`
29. Klik `(←)` pada kotak Search
30. Verifikasi Filter Action `Activate` tetap berlaku (chip `Activate` tampil)
31. Verifikasi Sort Date tetap berlaku
32. Ketik Search `Resend`, tekan Enter
33. Klik header Action
34. Verifikasi sort pindah ke kolom Action
35. Verifikasi Search `Resend` tidak direset
36. Verifikasi Filter Action `Activate` tidak direset
37. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
38. Klik `(←)` pada kotak Search
39. Verifikasi baris yang cocok pulih: C-6 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
40. Klik `[Clear Field]` lalu `[Apply]`, lalu klik icon Filter untuk menutup panel

### TC-FA-SU-720: Perilaku Filter Panel

41. Klik icon Filter
42. Buka dropdown Action, centang `Edit` tanpa `[Apply]`
43. Klik di luar panel
44. Klik icon Filter
45. Verifikasi panel menampilkan nilai ter-Apply terakhir (perubahan dibuang)
46. Verifikasi tabel tidak berubah
47. Buka dropdown Action, centang `Assign`, klik `[Apply]`
48. Verifikasi badge titik tampil pada ikon Filter saat panel terbuka
49. Klik icon Filter untuk menutup panel
50. Verifikasi badge titik tampil pada ikon Filter saat panel tertutup
51. Klik icon Filter
52. Klik `[Clear Field]` lalu `[Apply]`
53. Verifikasi badge titik hilang
54. Buka dropdown Action
55. Verifikasi dropdown Action menampilkan opsi lain (`Edit` dan `Assign` tampil)
56. Verifikasi dropdown tidak memiliki opsi untuk nilai kosong
57. Centang `Edit`, klik `[Apply]`
58. Verifikasi hasil memuat sedikitnya satu baris
59. Verifikasi tidak ada baris dengan nilai kosong pada hasil
60. Klik header Column Visibility (⋯), hilangkan centang kolom Action
61. Klik icon Filter
62. Verifikasi field filter Action tetap ada di Filter Panel
63. Verifikasi filter ter-Apply tetap berlaku
64. Klik `[Clear Field]` lalu `[Apply]`, lalu klik header Column Visibility (⋯) dan centang kembali kolom Action

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Asersi tambahan di luar Expected (S-03): `Verifikasi` pada langkah 55 membuktikan opsi pembanding tampil di dropdown Action sebagai anchor positif sebelum asersi absence opsi nilai kosong (bagian 8b butir 2).
- Asersi tambahan di luar Expected (S-03): `Verifikasi` langkah 3 (Search `Resend` menyisakan C-1) dan langkah 12 (Filter Action `Activate` menyisakan C-6) sebagai anchor positif sebelum asersi irisan tanpa baris seed pada TC-FA-SU-718 (bagian 8b butir 2).
- Spec ini berjumlah 64 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed. (2) TC-FA-SU-718 menulis hasil irisan sebagai tidak memuat baris seed (baris non-seed boleh ikut tampil) tanpa menyebut empty state; spec tidak mengasersi empty state di TC ini dan menambahkan `Verifikasi` baris seed tunggal (C-1, C-6) sebagai anchor positif. Butir d (kembali ke halaman 1 saat kriteria berubah) tidak dapat dibedakan pada fixture satu halaman. (3) TC-FA-SU-719: kombinasi Search `Resend` dan Filter Action `Activate` sudah menghasilkan 0 baris (irisan kosong), sehingga butir d diasersi dari kombinasi itu tanpa kata kunci tambahan; TC tidak menyebut kata kunci tanpa hasil secara konkret. (4) TC-FA-SU-720 butir c (memilih opsi apa pun menyaring keluar baris bernilai kosong) tidak punya baris bernilai kosong pada seed #27; spec memverifikasi bahwa dropdown tidak memuat opsi kosong dan hasil filter tidak memuat baris bernilai kosong, tanpa data kosong khusus.
- Klik header Column Visibility (`⋯`) dihitung sebagai klik luar panel Filter sehingga menutup panel (konvensi prd-conventions 9.8); `Klik icon Filter` berikutnya membuka kembali panel dengan nilai terakhir yang sudah diterapkan, dan nilai draft yang belum diterapkan dibuang.
