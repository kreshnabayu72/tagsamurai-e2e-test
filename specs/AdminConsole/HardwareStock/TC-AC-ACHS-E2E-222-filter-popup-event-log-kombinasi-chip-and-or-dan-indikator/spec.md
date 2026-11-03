---
id: TC-AC-ACHS-E2E-222-filter-popup-event-log-kombinasi-chip-and-or-dan-indikator
title: "Filter Popup Event Log: Kombinasi Chip, AND/OR, dan Indikator"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-477
  - TC-AC-ACHS-478
  - TC-AC-ACHS-479
  - TC-AC-ACHS-480
  - TC-AC-ACHS-481
  - TC-AC-ACHS-482
  - TC-AC-ACHS-483
  - TC-AC-ACHS-484
  - TC-AC-ACHS-485
  - TC-AC-ACHS-486
coverage:
  web: automated
---

# Filter Popup Event Log: Kombinasi Chip, AND/OR, dan Indikator

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Spec membuka Stock Detail dan popup Event Log sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #20 TC (Tabel B), SKU `Fixture.hardwareStock.p16.a[4].sku` (Handheld Reader - Long Range) memiliki tepat 12 sesi Event Log; baris dikenali lewat kolom Date. Event Log adalah audit trail permanen; total 12 sesi ditetapkan Pre-setup dan berlaku sebelum spec lain menambah sesi pada SKU ini (suite.md menjalankan spec yang mengubah baseline sesudah spec baca). Baris dirujuk lewat nomor baris Tabel B: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel B (`Fixture.hardwareStock.p20.b[n]`) pada urutan default (Date terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU Handheld Reader Long Range | #16 Tabel A baris 4 | kode SKU Handheld Reader - Long Range (RFD40); pemilik Event Log Pre-setup #20 | `Fixture.hardwareStock.p16.a[4].sku` |
  | Date baris #n (n = 1 sampai 12) | #20 Tabel B | identitas baris hasil; urutan default Date terbaru lebih dulu; format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p20.b[n].date` |
  | Activity baris #n (n = 1 sampai 12) | #20 Tabel B | Delete Stock pada #1, #5, #9; Add Stock pada baris lain (9 baris) | `Fixture.hardwareStock.p20.b[n].activity` |
  | Modified By baris #n (n = 1 sampai 12) | #20 Tabel B | nama singkat user: akun Pre-setup #1 pada #1, #4, #7, #10; user Distributor Pre-setup #11 pada #2, #5, #8, #11; user Distributor Pre-setup #10 pada #3, #6, #9, #12 | `Fixture.hardwareStock.p20.b[n].modifiedBy` |
  | Nama singkat akun Total Control Principal #1 | #1 | Total Control Principal; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p01.totalControl.shortName` |
  | Nama singkat akun user Distributor #10 | #10 | user Distributor; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
  | Nama singkat akun user Distributor #11 | #11 | user Distributor; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman yang dipakai suite (lihat suite.md).
- State global: Column Visibility kolom Activity disembunyikan pada langkah 71 dan dipulihkan pada langkah 75; hook `after` menghapus preferensi kolom di browser bila ada (kemampuan disediakan tim FE). Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab `Available` aktif
3. Klik icon `[Event Log]` di toolbar
4. Klik icon Filter

### TC-AC-ACHS-477: Dua opsi dalam satu field Modified By dihitung OR, chip di dalam field

5. Buka dropdown Modified By, centang `Fixture.hardwareStock.account.p10.distributorCakra.shortName` lalu `Fixture.hardwareStock.account.p11.distributorMitra.shortName`
6. Klik `[Apply]`
7. Verifikasi dua chip `Fixture.hardwareStock.account.p10.distributorCakra.shortName` dan `Fixture.hardwareStock.account.p11.distributorMitra.shortName` tampil di dalam closed-state field
8. Verifikasi kedua chip tampil sejajar
9. Verifikasi tabel menampilkan gabungan (OR) 8 baris: #2, #3, #5, #6, #8, #9, #11, #12
10. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-478: Hapus satu chip Modified By lewat (X) menyinkronkan checkbox

11. Centang `Fixture.hardwareStock.account.p10.distributorCakra.shortName` dan `Fixture.hardwareStock.account.p11.distributorMitra.shortName` pada dropdown Modified By
12. Klik `(X)` pada chip `Fixture.hardwareStock.account.p10.distributorCakra.shortName` (tanpa membuka dropdown)
13. Verifikasi chip `Fixture.hardwareStock.account.p10.distributorCakra.shortName` hilang
14. Verifikasi chip `Fixture.hardwareStock.account.p11.distributorMitra.shortName` tetap ada
15. Buka dropdown Modified By
16. Verifikasi checkbox `Fixture.hardwareStock.account.p10.distributorCakra.shortName` di dalam dropdown ter-uncheck
17. Verifikasi checkbox `Fixture.hardwareStock.account.p11.distributorMitra.shortName` tetap tercentang
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan 4 baris: #2, #5, #8, #11
20. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-479: Uncheck di dalam dropdown Modified By menghapus chip yang bersangkutan

21. Centang `Fixture.hardwareStock.account.p10.distributorCakra.shortName` dan `Fixture.hardwareStock.account.p11.distributorMitra.shortName` pada dropdown Modified By
22. Dengan dropdown tetap terbuka, uncheck `Fixture.hardwareStock.account.p11.distributorMitra.shortName`
23. Verifikasi chip `Fixture.hardwareStock.account.p11.distributorMitra.shortName` hilang dari field
24. Verifikasi chip `Fixture.hardwareStock.account.p10.distributorCakra.shortName` tetap ada
25. Tutup dropdown dan klik `[Apply]`
26. Verifikasi tabel menampilkan 4 baris: #3, #6, #9, #12
27. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-480: Dua field berbeda dihitung AND

28. Isi Activity = `Add Stock` dan Modified By = `Fixture.hardwareStock.account.p01.totalControl.shortName`
29. Klik `[Apply]`
30. Verifikasi tabel menampilkan irisan 3 baris: #4, #7, #10
31. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-481: Search lalu Filter, filter menimpa tanpa mereset keyword

32. Ketik Search `Delete`, tekan Enter
33. Isi Activity = `Add Stock`
34. Klik `[Apply]`
35. Verifikasi tabel menampilkan irisan Search dan Filter: 0 baris dengan empty state `No results found`
36. Verifikasi keyword `Delete` tetap terisi di kotak Search
37. Klik `[Clear Field]`, lalu klik `[Apply]`
38. Klik icon `(←)`

### TC-AC-ACHS-482: Filter lalu Search, hasil identik dengan urutan Search lalu Filter

39. Isi Activity = `Add Stock`, klik `[Apply]`
40. Ketik Search `Delete`, tekan Enter
41. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found`, identik dengan hasil urutan Search lalu Filter
42. Klik icon `(←)`
43. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-483: Clear Field mempertahankan Search dan Sort aktif

44. Ketik Search `Delete`, tekan Enter
45. Klik header kolom Success sekali (Ascending)
46. Isi Activity = `Add Stock`, klik `[Apply]`
47. Klik `[Clear Field]`, lalu klik `[Apply]`
48. Verifikasi filter Activity kosong kembali
49. Verifikasi keyword `Delete` tetap menyaring 3 baris: #1, #5, #9
50. Verifikasi indikator sort Ascending tetap aktif pada Success
51. Klik header kolom Success dua kali sampai indikator sort netral
52. Klik icon `(←)`

### TC-AC-ACHS-484: Menutup panel tanpa Apply membuang draft

53. Isi Activity = `Add Stock`, klik `[Apply]`
54. Ubah field Modified By menjadi `Fixture.hardwareStock.account.p01.totalControl.shortName` tanpa klik `[Apply]`
55. Klik icon Filter untuk menutup panel
56. Klik icon Filter untuk membuka panel kembali
57. Verifikasi panel menampilkan nilai ter-Apply terakhir: Activity = `Add Stock`
58. Verifikasi draft Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName` tidak tampil
59. Verifikasi tabel tetap menampilkan hasil filter terakhir yang di-Apply, 9 baris, lima teratas: #2, #3, #4, #6, #7
60. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-485: Indikator filter aktif, badge titik tanpa angka

61. Verifikasi ikon Filter tanpa badge
62. Isi Activity = `Delete Stock`, klik `[Apply]`
63. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel terbuka
64. Klik icon Filter untuk menutup panel
65. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel tertutup
66. Klik icon Filter untuk membuka panel
67. Klik `[Clear Field]`, lalu klik `[Apply]`
68. Verifikasi badge titik hilang dari ikon Filter

### TC-AC-ACHS-486: Filter independen dari Column Visibility, hide kolom Activity tidak menghapus filter

69. Isi Activity = `Add Stock`, klik `[Apply]`
70. Klik header kolom Actions `(⋯)`
71. Uncheck `Activity`
72. Klik icon Filter untuk membuka kembali Filter Panel
73. Verifikasi field Activity tetap ada di Filter Panel dengan nilai `Add Stock`
74. Verifikasi filter yang sudah di-Apply tetap berlaku, 9 baris, lima teratas: #2, #3, #4, #6, #7
75. Klik header kolom Actions `(⋯)`, check `Activity` kembali
76. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-477 sampai 486). Tidak ada TC hanya-BE di spec ini.
- Langkah 1 sampai 3 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Langkah penghubung (bukan dari langkah TC): langkah 10, 20, 27, 31, 37, 43, 60, 67, 76 (`[Clear Field]` dan `[Apply]` agar TC berikutnya bermula dari tabel tanpa filter, S-09), langkah 38, 42, 52 (klik `(←)` mereset Search), langkah 51 (mengembalikan sort ke netral), langkah 75 (memulihkan kolom Activity). Filter Panel tetap terbuka sesudah `[Apply]` (ditunjukkan TC-AC-ACHS-484), sehingga klik icon Filter hanya muncul pada langkah 4 dan pada TC yang menutup dan membuka panel.
- Spec ini di atas 35 langkah (76 langkah nominal). Alasan: semua blok memakai satu Filter Panel dan satu dataset read-only (Event Log satu SKU), tiap TC dimulai dari tabel tanpa filter berkat langkah pembersih, dan topik Filter satu dataset digabung sesuai prinsip 1.
- Temuan untuk QA:
  - TC-485 "isi satu field" tidak menyebut field atau nilai; spec memakai Activity = `Delete Stock`.
  - TC-486 langkah 7 ("Buka kembali Filter Panel") tidak menyebut apakah panel masih terbuka sesudah overlay Column Visibility dibuka; spec menulis klik icon Filter dan hasilnya bergantung pada perilaku itu.
  - TC-481 dan TC-482 menghasilkan 0 baris sehingga urutan Search dan Filter tidak dapat dibedakan lewat isi baris; spec mengikuti Expected TC.
  - Populasi Pre-setup #20 dirujuk lewat nomor baris Tabel B (`#n` = `Fixture.hardwareStock.p20.b[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nilai literal Pre-setup di spec dan tanpa pengecualian S-12. Total 12 sesi hanya berlaku sebelum spec lain menambah sesi pada SKU ini (audit trail permanen, lihat suite.md). Literal yang tetap ada adalah teks UI nyata (placeholder, `Add Stock`, `Delete Stock`, `Delete`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
