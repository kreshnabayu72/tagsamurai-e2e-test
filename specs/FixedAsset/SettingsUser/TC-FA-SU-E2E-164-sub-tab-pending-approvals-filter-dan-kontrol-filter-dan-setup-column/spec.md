---
id: TC-FA-SU-E2E-164-sub-tab-pending-approvals-filter-dan-kontrol-filter-dan-setup-column
title: "Sub-tab Pending Approvals: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-487
  - TC-FA-SU-488
  - TC-FA-SU-489
  - TC-FA-SU-490
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Filter dan Kontrol Filter dan Setup Column

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
- Tabel parameter "Kolom Disembunyikan" (dipakai langkah 51 sampai 52):

| Kolom |
|---|
| `Transaction ID` |
| `Transaction` |
| `Requester` |

Kolom `Submission Date` tetap visible sebagai satu-satunya kolom pada langkah penguji batas. Putaran kedua: centang `Transaction ID` dan uncheck `Submission Date`, karena kolom yang tersisa sebagai satu-satunya kolom visible tidak dapat di-uncheck.
- Kemampuan menghapus preferensi kolom Setup Column di browser (disediakan tim FE): dipakai sebagai langkah pemulihan dan di hook `after` untuk tabel yang konfigurasinya disimpan spec ini (bagian 4 konvensi). Konfigurasi kolom tersimpan per perangkat dan per tabel.

## Test Steps

### TC-FA-SU-487: Chip dan checkbox dropdown Filter Sub-tab Pending Approvals sinkron dua arah, logika OR dalam field

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Klik icon Filter
4. Buka dropdown Transaction
5. Centang `Assignment`
6. Centang `Borrow`
7. Klik `[Apply]`
8. Verifikasi dua chip `Assignment` dan `Borrow` tampil di dalam field Transaction
9. Verifikasi hasil tabel adalah gabungan (OR) kedua opsi
10. Klik ✕ pada chip `Borrow` tanpa membuka dropdown
11. Verifikasi chip `Borrow` hilang
12. Verifikasi chip `Assignment` tetap tampil
13. Buka dropdown Transaction
14. Verifikasi checkbox opsi `Borrow` ter-uncheck
15. Centang kembali `Borrow`
16. Uncheck `Assignment`
17. Verifikasi chip `Assignment` hilang
18. Verifikasi chip `Borrow` tetap tampil
19. Ketik `BORR` di kotak cari dropdown
20. Verifikasi opsi dropdown dipersempit menjadi `Borrow` (substring, tidak case-sensitive)
21. Ganti isi kotak cari dropdown dengan `zzz-tidak-ada`
22. Verifikasi dropdown menampilkan `No results found`
23. Tekan Esc untuk menutup dropdown
24. Klik `[Clear Field]`
25. Klik `[Apply]`
26. Klik icon Filter untuk menutup panel

### TC-FA-SU-488: Screening Overlay Column Visibility Sub-tab Pending Approvals

27. Hover header kolom Actions (⋯)
28. Verifikasi tooltip `Column Visibility` tampil pada header
29. Klik header kolom Actions (⋯)
30. Verifikasi overlay Column Visibility tampil
31. Verifikasi daftar kolom berurutan `Transaction ID`, `Transaction`, `Requester`, `Submission Date`
32. Verifikasi tiap kolom memiliki checkbox ☑ Hideable terpilih dan enabled
33. Verifikasi tiap kolom memiliki drag handle
34. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
35. Tekan Esc untuk menutup overlay

### TC-FA-SU-489: Screening Popup Setup Column dan Preview Table Sub-tab Pending Approvals

36. Klik header kolom Actions (⋯)
37. Klik `Setup Column...`
38. Verifikasi Title popup `Setup Column`
39. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
40. Verifikasi icon close ✕ tampil di header popup
41. Verifikasi body memuat daftar kolom `Transaction ID`, `Transaction`, `Requester`, `Submission Date`
42. Verifikasi tiap kolom memiliki checkbox
43. Verifikasi tiap kolom memiliki drag handle
44. Verifikasi tiap kolom memiliki icon Pin
45. Verifikasi Live Preview tabel tampil
46. Verifikasi footer menampilkan `[Reset to Default]` dan `[Save]` rata kanan
47. Verifikasi footer tanpa `[Cancel]`
48. Klik ✕ pada popup Setup Column

### TC-FA-SU-490: Ceklis dan unceklis Setup Column Sub-tab Pending Approvals kelas Hideable (default tampil)

49. Klik header kolom Actions (⋯)
50. Klik `Setup Column...`
51. Untuk setiap baris tabel parameter "Kolom Disembunyikan" (langkah 51 sampai 52): uncheck kolom itu pada popup Setup Column
52. Verifikasi kolom itu hilang dari Live Preview
53. Hover checkbox kolom `Submission Date` (satu-satunya kolom visible)
54. Verifikasi checkbox kolom `Submission Date` disabled dengan tooltip `At least one column must remain visible.`
55. Klik `[Save]`
56. Untuk setiap baris tabel parameter "Kolom Disembunyikan" (langkah 56): Verifikasi kolom itu tidak tampil di tabel
57. Tekan F5 pada halaman Detail
58. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
59. Untuk setiap baris tabel parameter "Kolom Disembunyikan" (langkah 59): Verifikasi kolom itu tetap tidak tampil di tabel setelah F5
60. Klik header kolom Actions (⋯)
61. Klik `Setup Column...`
62. Check kolom `Transaction ID` pada popup Setup Column
63. Verifikasi kolom `Transaction ID` tampil di Live Preview
64. Uncheck kolom `Submission Date` pada popup Setup Column
65. Verifikasi kolom `Submission Date` hilang dari Live Preview
66. Klik `[Save]`
67. Verifikasi kolom `Transaction ID` tampil di tabel
68. Verifikasi kolom `Submission Date` tidak tampil di tabel
69. Tekan F5 pada halaman Detail
70. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
71. Verifikasi kolom `Transaction ID` tetap tampil di tabel setelah F5
72. Verifikasi kolom `Submission Date` tetap tidak tampil di tabel setelah F5
73. Pulihkan konfigurasi kolom tabel Pending Approvals: hapus preferensi kolom di browser
74. Tekan F5 pada halaman Detail
75. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Opsi `Assignment` dan `Borrow` (field Transaction) serta kata kunci cari dropdown `BORR` dan `zzz-tidak-ada` dipilih spec karena TC-FA-SU-487 tidak menyebut nilainya; `BORR` berhuruf besar untuk membuktikan pencarian tidak case-sensitive.
- Langkah 51 sampai 52, 56, dan 59 diulang untuk tiga baris tabel parameter "Kolom Disembunyikan" (bagian 8b butir 7); `Verifikasi` tetap satu per klausa (Live Preview, tabel, setelah F5).
- Langkah pemulihan konfigurasi kolom (73) dan F5 sesudahnya memulihkan tabel ke default; hook `after` mengulang pemulihan sebagai cadangan.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (83 langkah, 75 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Pending Approvals, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-491 dan 493 ada di spec 165; TC-FA-SU-492 ada di spec 168.
- Temuan untuk QA (S-15):
  - TC-FA-SU-487 Langkah 5 ("uncheck opsi yang tersisa") meninggalkan nol chip sehingga Expected c ("chip lain tetap") tidak teramati; spec mencentang kembali satu opsi lalu meng-uncheck opsi lain.
  - TC-FA-SU-490 mensyaratkan setiap kolom diubah lalu `[Save]`, sedangkan kolom terakhir yang visible tidak dapat di-uncheck (Expected e); spec memakai dua putaran (tiga kolom, lalu `Transaction ID` dan `Submission Date`). Langkah F5 tidak menyebut tab dan sub-tab aktif setelah muat ulang; spec membukanya kembali.
