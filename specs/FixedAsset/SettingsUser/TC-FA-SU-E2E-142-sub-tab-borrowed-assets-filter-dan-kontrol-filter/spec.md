---
id: TC-FA-SU-E2E-142-sub-tab-borrowed-assets-filter-dan-kontrol-filter
title: "Sub-tab Borrowed Assets: Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-423
  - TC-FA-SU-424
  - TC-FA-SU-425
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-423: Filter Sub-tab Borrowed Assets kelas date: Due Return Date

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Klik icon Filter
4. Pilih rentang 10/09/26 sampai 02/10/26 pada Due Return Date
5. Klik `[Apply]`
6. Verifikasi rentang inklusif 10/09/26 sampai 02/10/26 menyisakan `Laptop - 1`, `Laptop - 2`, dan `Kamera DSLR` (3 baris)
7. Klik `[Clear Field]`
8. Klik `[Apply]`
9. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-424: Kombinasi Search dan Filter Sub-tab Borrowed Assets dua arah

10. Ketik Search `Kamera`, tekan Enter
11. Klik icon Filter
12. Buka dropdown Name
13. Centang `Kamera DSLR`
14. Klik `[Apply]`
15. Verifikasi Search `Kamera` lalu Filter Name `Kamera DSLR`: hasil irisan `Kamera DSLR` (1 baris)
16. Verifikasi kotak Search tetap berisi `Kamera` setelah Filter diterapkan
17. Verifikasi indikator pagination menunjukkan halaman 1 saat kriteria berubah
18. Klik `[Clear Field]`
19. Klik `[Apply]`
20. Klik `(←)` pada kotak Search
21. Buka dropdown Name
22. Centang `Kamera DSLR`
23. Klik `[Apply]`
24. Ketik Search `Kamera`, tekan Enter
25. Verifikasi Filter Name `Kamera DSLR` lalu Search `Kamera`: hasil identik `Kamera DSLR` (1 baris)
26. Verifikasi chip `Kamera DSLR` tetap tampil di field Name setelah Search dijalankan
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Klik `(←)` pada kotak Search
30. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-425: Pelepasan kontrol Sub-tab Borrowed Assets: Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

31. Ketik Search `Kamera`, tekan Enter
32. Klik icon Filter
33. Buka dropdown Name
34. Centang `Kamera DSLR`
35. Klik `[Apply]`
36. Klik header kolom Name satu kali
37. Klik `[Clear Field]`
38. Klik `[Apply]`
39. Verifikasi Clear Field saat Search `Kamera` dan Sort aktif: Search tetap berlaku, tabel menyisakan `Kamera DSLR`
40. Verifikasi Clear Field saat Search dan Sort aktif: Sort kolom Name tetap berlaku
41. Buka dropdown Name
42. Centang `Kamera DSLR`
43. Klik `[Apply]`
44. Klik `✕` pada Search, tekan Enter
45. Verifikasi setelah Search dikosongkan saat Filter Name dan Sort aktif: Filter tetap berlaku, tabel menyisakan `Kamera DSLR`
46. Verifikasi setelah Search dikosongkan saat Filter dan Sort aktif: Sort kolom Name tetap berlaku
47. Ketik Search `Kamera`, tekan Enter
48. Klik header kolom Brand satu kali
49. Verifikasi mengganti kolom sort memindahkan Sort ke kolom Brand
50. Verifikasi Search `Kamera` tidak direset oleh ganti sort
51. Verifikasi Filter Name `Kamera DSLR` tidak direset oleh ganti sort
52. Ganti isi kotak search dengan `Laptop`, tekan Enter
53. Verifikasi kombinasi Search `Laptop` dan Filter Name `Kamera DSLR` yang menghasilkan 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
54. Klik `✕` pada Search, tekan Enter
55. Verifikasi melepas Search langsung memulihkan baris yang cocok: `Kamera DSLR` tampil
56. Klik `[Clear Field]`
57. Klik `[Apply]`
58. Tutup panel Filter dengan klik icon Filter
59. Klik header kolom Brand dua kali lagi sampai kembali netral

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Alasan melewati sekitar 35 langkah (59 langkah tertulis, 59 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-423: format tanggal 10/09/26 dan 02/10/26 mengikuti General Settings dan langkah memilih rentang pada date range picker tidak dirinci TC; spec menuliskan satu langkah pemilihan rentang.
  - TC-FA-SU-424 butir d: "halaman 1 saat kriteria berubah" tidak dapat dibedakan pada fixture satu halaman (TC-FA-SU-434 butir e); spec mengasersi indikator pagination halaman 1.
  - TC-FA-SU-425 langkah 6: "keyword yang tidak ada hasilnya" tidak diberi nilai; spec memakai Search `Laptop` bersama Filter Name `Kamera DSLR` (0 baris).
