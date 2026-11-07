---
id: TC-FA-SU-E2E-163-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-2
title: "Sub-tab Pending Approvals: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-484
  - TC-FA-SU-485
  - TC-FA-SU-486
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#25): Detail Budi Santoso dengan Sub-tab Pending Approvals 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #25 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC:

| Transaction ID | Transaction | Requester | Submission Date |
|---|---|---|---|
| `BRW-20260712-0341` | `Borrow` | `Ahmad D` | 12/07/26 |
| `TRF-20260714-0088` | `Transfer` | `Citra L` (Citra Lestari) | 14/07/26 |
| `DSP-20260715-0022` | `Disposal` | `Eka W` | 15/07/26 |
| `ASG-20260716-0015` | `Assignment` | `Budi S` | 16/07/26 |
| `BRW-20260718-0007` | `Borrow` | `Citra L` (Citra Lestari) | 18/07/26 |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-484: Kombinasi Search dan Filter Sub-tab Pending Approvals dua arah

1. Ketik Search `Budi Santoso`, tekan Enter, lalu klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Ketik Search `TRF-2026`, tekan Enter
4. Klik icon Filter
5. Buka dropdown Transaction
6. Centang `Assignment`
7. Klik `[Apply]`
8. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
9. Verifikasi hasil irisan Search lalu Filter tidak ada baris (0 baris)
10. Verifikasi keyword Search `TRF-2026` tetap terisi setelah Filter di-Apply
11. Verifikasi tabel berada di halaman 1
12. Klik `[Clear Field]`
13. Klik `[Apply]`
14. Klik `(←)` pada kotak Search
15. Buka dropdown Transaction
16. Centang `Assignment`
17. Klik `[Apply]`
18. Ketik Search `TRF-2026`, tekan Enter
19. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
20. Verifikasi hasil Filter lalu Search identik, tidak ada baris
21. Verifikasi chip Filter `Assignment` tetap berlaku setelah Search dijalankan
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Klik `(←)` pada kotak Search
25. Klik icon Filter untuk menutup panel

### TC-FA-SU-485: Pelepasan kontrol Sub-tab Pending Approvals: Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

26. Ketik Search `TRF-2026`, tekan Enter
27. Klik icon Filter
28. Buka dropdown Transaction
29. Centang `Assignment`
30. Klik `[Apply]`
31. Klik header Transaction ID
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Verifikasi Search `TRF-2026` tetap berlaku
35. Verifikasi Sort kolom Transaction ID tetap berlaku
36. Buka dropdown Transaction
37. Centang `Assignment`
38. Klik `[Apply]`
39. Kosongkan isi kotak search, tekan Enter
40. Verifikasi Filter Transaction `Assignment` tetap berlaku
41. Verifikasi Sort kolom Transaction ID tetap berlaku
42. Ketik Search `TRF-2026`, tekan Enter
43. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
44. Klik header Requester
45. Verifikasi sort pindah ke kolom Requester
46. Verifikasi keyword Search `TRF-2026` tidak direset
47. Verifikasi chip Filter `Assignment` tidak direset
48. Klik `(←)` pada kotak Search
49. Verifikasi baris yang cocok dengan Filter kembali tampil, yaitu `ASG-20260716-0015`
50. Klik `[Clear Field]`
51. Klik `[Apply]`
52. Klik icon Filter untuk menutup panel

### TC-FA-SU-486: Perilaku Filter Panel Sub-tab Pending Approvals: tutup tanpa Apply, indikator titik, dan nilai kosong

53. Klik icon Filter
54. Buka dropdown Transaction
55. Centang `Assignment`
56. Klik di luar panel Filter
57. Verifikasi tabel tidak berubah dan tetap menampilkan seluruh baris
58. Klik icon Filter
59. Verifikasi field Transaction menampilkan nilai ter-Apply terakhir (kosong, tanpa chip)
60. Buka dropdown Transaction
61. Centang `Assignment`
62. Klik `[Apply]`
63. Klik icon Filter untuk menutup panel
64. Verifikasi ikon Filter menampilkan badge titik saat panel tertutup
65. Klik icon Filter
66. Verifikasi ikon Filter menampilkan badge titik saat panel terbuka
67. Klik `[Clear Field]`
68. Klik `[Apply]`
69. Verifikasi badge titik pada ikon Filter hilang
70. Buka dropdown Transaction
71. Verifikasi dropdown Transaction menampilkan opsi nilai lain, antara lain `Assignment`
72. Verifikasi dropdown Transaction tidak memiliki opsi untuk nilai kosong
73. Tekan Esc untuk menutup dropdown
74. Buka dropdown Transaction, centang `Assignment`
75. Klik `[Apply]`
76. Klik header Actions (⋯)
77. Uncheck kolom Transaction pada overlay Column Visibility
78. Verifikasi field Transaction tetap ada pada panel Filter
79. Verifikasi filter ter-Apply tetap berlaku dan tabel menampilkan satu baris
80. Klik header Actions (⋯)
81. Check kolom Transaction pada overlay Column Visibility
82. Klik `[Clear Field]`
83. Klik `[Apply]`
84. Klik icon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): Search nama `Budi Santoso` serta pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Kombinasi Search `TRF-2026` dan Filter Transaction `Assignment` mengikuti Data Uji TC dan menghasilkan 0 baris (irisan kosong); asersi "tidak ada baris" didahului `Verifikasi` empty state sebagai anchor positif (bagian 8b butir 2; langkah 8 dan 19, asersi tambahan di luar Expected TC-FA-SU-484, S-03).
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (84 langkah, 84 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Pending Approvals, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-480 sampai 483 ada di spec 162.
- Temuan untuk QA (S-15):
  - TC-FA-SU-485 Langkah 4 mengosongkan Search sebelum Langkah 5 mengganti sort "saat Search dan Filter aktif"; spec mengaktifkan Search lagi (kombinasi 0 baris) sebelum mengganti sort, sehingga pemindahan sort teramati dari indikator header, bukan urutan baris.
  - TC-FA-SU-486 Expected c ("menyaring keluar baris yang nilainya kosong") tidak dapat diasersi: kelima baris Pre-setup #25 tidak memiliki nilai kosong pada kolom Transaction. Spec hanya mengasersi bahwa dropdown tidak memiliki opsi untuk nilai kosong. Expected d tidak menyebut kolom yang di-hide; spec memakai kolom Transaction.
