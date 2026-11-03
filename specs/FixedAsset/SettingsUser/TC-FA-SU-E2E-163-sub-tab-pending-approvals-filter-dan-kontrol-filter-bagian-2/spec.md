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

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Ketik Search `TRF-2026`, tekan Enter
4. Klik icon Filter
5. Buka dropdown Transaction
6. Centang `Assignment`
7. Klik `[Apply]`
8. Verifikasi hasil irisan Search lalu Filter tidak ada baris (0 baris)
9. Verifikasi keyword Search `TRF-2026` tetap terisi setelah Filter di-Apply
10. Verifikasi tabel berada di halaman 1
11. Klik `[Clear Field]`
12. Klik `[Apply]`
13. Klik `(←)` pada kotak Search
14. Buka dropdown Transaction
15. Centang `Assignment`
16. Klik `[Apply]`
17. Ketik Search `TRF-2026`, tekan Enter
18. Verifikasi hasil Filter lalu Search identik, tidak ada baris
19. Verifikasi chip Filter `Assignment` tetap berlaku setelah Search dijalankan
20. Klik `[Clear Field]`
21. Klik `[Apply]`
22. Klik `(←)` pada kotak Search
23. Klik icon Filter untuk menutup panel

### TC-FA-SU-485: Pelepasan kontrol Sub-tab Pending Approvals: Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

24. Ketik Search `TRF-2026`, tekan Enter
25. Klik icon Filter
26. Buka dropdown Transaction
27. Centang `Assignment`
28. Klik `[Apply]`
29. Klik header Transaction ID
30. Klik `[Clear Field]`
31. Klik `[Apply]`
32. Verifikasi Search `TRF-2026` tetap berlaku
33. Verifikasi Sort kolom Transaction ID tetap berlaku
34. Buka dropdown Transaction
35. Centang `Assignment`
36. Klik `[Apply]`
37. Kosongkan isi kotak search, tekan Enter
38. Verifikasi Filter Transaction `Assignment` tetap berlaku
39. Verifikasi Sort kolom Transaction ID tetap berlaku
40. Ketik Search `TRF-2026`, tekan Enter
41. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
42. Klik header Requester
43. Verifikasi sort pindah ke kolom Requester
44. Verifikasi keyword Search `TRF-2026` tidak direset
45. Verifikasi chip Filter `Assignment` tidak direset
46. Klik `(←)` pada kotak Search
47. Verifikasi baris yang cocok dengan Filter kembali tampil, yaitu `ASG-20260716-0015`
48. Klik `[Clear Field]`
49. Klik `[Apply]`
50. Klik icon Filter untuk menutup panel

### TC-FA-SU-486: Perilaku Filter Panel Sub-tab Pending Approvals: tutup tanpa Apply, indikator titik, dan nilai kosong

51. Klik icon Filter
52. Buka dropdown Transaction
53. Centang `Assignment`
54. Klik di luar panel Filter
55. Verifikasi tabel tidak berubah dan tetap menampilkan seluruh baris
56. Klik icon Filter
57. Verifikasi field Transaction menampilkan nilai ter-Apply terakhir (kosong, tanpa chip)
58. Buka dropdown Transaction
59. Centang `Assignment`
60. Klik `[Apply]`
61. Klik icon Filter untuk menutup panel
62. Verifikasi ikon Filter menampilkan badge titik saat panel tertutup
63. Klik icon Filter
64. Verifikasi ikon Filter menampilkan badge titik saat panel terbuka
65. Klik `[Clear Field]`
66. Klik `[Apply]`
67. Verifikasi badge titik pada ikon Filter hilang
68. Buka dropdown Transaction
69. Verifikasi dropdown Transaction menampilkan opsi nilai lain, antara lain `Assignment`
70. Verifikasi dropdown Transaction tidak memiliki opsi untuk nilai kosong
71. Tekan Esc untuk menutup dropdown
72. Centang `Assignment`
73. Klik `[Apply]`
74. Klik header Actions (⋯)
75. Uncheck kolom Transaction pada overlay Column Visibility
76. Verifikasi field Transaction tetap ada pada panel Filter
77. Verifikasi filter ter-Apply tetap berlaku dan tabel menampilkan satu baris
78. Klik header Actions (⋯)
79. Check kolom Transaction pada overlay Column Visibility
80. Klik `[Clear Field]`
81. Klik `[Apply]`
82. Klik icon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Kombinasi Search `TRF-2026` dan Filter Transaction `Assignment` mengikuti Data Uji TC dan menghasilkan 0 baris (irisan kosong); asersi "tidak ada baris" memakai empty state sebagai anchor positif (bagian 8b butir 2).
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (82 langkah, 82 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Pending Approvals, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-480 sampai 483 ada di spec 162.
- Temuan untuk QA (S-15):
  - TC-FA-SU-485 Langkah 4 mengosongkan Search sebelum Langkah 5 mengganti sort "saat Search dan Filter aktif"; spec mengaktifkan Search lagi (kombinasi 0 baris) sebelum mengganti sort, sehingga pemindahan sort teramati dari indikator header, bukan urutan baris.
  - TC-FA-SU-486 Expected c ("menyaring keluar baris yang nilainya kosong") tidak dapat diasersi: kelima baris Pre-setup #25 tidak memiliki nilai kosong pada kolom Transaction. Spec hanya mengasersi bahwa dropdown tidak memiliki opsi untuk nilai kosong. Expected d tidak menyebut kolom yang di-hide; spec memakai kolom Transaction.
