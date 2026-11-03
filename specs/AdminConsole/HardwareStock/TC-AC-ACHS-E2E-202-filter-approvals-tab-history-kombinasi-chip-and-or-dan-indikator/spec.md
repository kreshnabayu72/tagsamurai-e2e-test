---
id: TC-AC-ACHS-E2E-202-filter-approvals-tab-history-kombinasi-chip-and-or-dan-indikator
title: "Filter Approvals > Hardware Stock Tab History: Kombinasi Chip, AND/OR, dan Indikator"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-429
  - TC-AC-ACHS-430
  - TC-AC-ACHS-431
  - TC-AC-ACHS-432
  - TC-AC-ACHS-433
  - TC-AC-ACHS-434
  - TC-AC-ACHS-435
  - TC-AC-ACHS-436
  - TC-AC-ACHS-437
  - TC-AC-ACHS-438
coverage:
  web: automated
---

# Filter Approvals > Hardware Stock Tab History: Kombinasi Chip, AND/OR, dan Indikator

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini. Baris dirujuk lewat nomor baris Tabel D: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel D (`Fixture.hardwareStock.p22.d[n]`) pada urutan default (Resolved At terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup dan tidak ditulis di spec ini.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Type baris #n (n = 1 sampai 12) | #22 Tabel D | Activation Collision pada #1, #3, #6, #8, #10, #12; Register Duplicate pada #2, #4, #5, #7, #9, #11 | `Fixture.hardwareStock.p22.d[n].type` |
  | Category baris #n (n = 1 sampai 12) | #22 Tabel D | Short Range pada #1, #2, #6, #7, #9, #11; Long Range pada #4, #5, #10; Smart Fixed Reader pada #3, #12; `—` pada #8 | `Fixture.hardwareStock.p22.d[n].category` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #22 Tabel D | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #5 dan #8 berformat MAC dengan awalan yang sama | `Fixture.hardwareStock.p22.d[n].matchedIdentifier` |
  | Requested By baris #n (n = 1 sampai 12) | #22 Tabel D | Client, Distributor, atau Principal dengan label peran dalam kurung; entitas yang sama pada #4 dan #11 serta #8 dan #12 | `Fixture.hardwareStock.p22.d[n].requestedBy` |
  | Keyword Search nama Client | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[10].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; muncul pada Existing Record atau Requested By tepat tiga baris #1, #8, #10 | `Fixture.hardwareStock.derived.clientCoreNameHistory` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- State global: Column Visibility tabel (kolom Type) disembunyikan pada langkah 70 dan dipulihkan pada langkah 74; hook `after` menghapus preferensi kolom di browser bila ada (kemampuan disediakan tim FE). Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`
3. Klik icon Filter

### TC-AC-ACHS-429: Dua opsi dalam satu field Approval dihitung OR, chip di dalam field

4. Buka dropdown Approval, centang `Approved` lalu `Canceled`
5. Klik `[Apply]`
6. Verifikasi dua chip `Approved` dan `Canceled` tampil di dalam closed-state field
7. Verifikasi kedua chip tampil sejajar
8. Verifikasi tabel menampilkan gabungan (OR) 8 baris: #1, #2, #5, #6, #7, #8, #11, #12
9. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-430: Hapus satu chip Approval lewat (X) menyinkronkan checkbox

10. Buka dropdown Approval, centang `Approved` dan `Canceled`
11. Klik `(X)` pada chip `Approved` (tanpa membuka dropdown)
12. Verifikasi chip `Approved` hilang
13. Verifikasi chip `Canceled` tetap ada
14. Buka dropdown Approval
15. Verifikasi checkbox `Approved` di dalam dropdown ter-uncheck
16. Verifikasi checkbox `Canceled` tetap tercentang
17. Klik `[Apply]`
18. Verifikasi tabel menampilkan 2 baris: #1, #8
19. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-431: Uncheck di dalam dropdown Approval menghapus chip yang bersangkutan

20. Buka dropdown Approval, centang `Approved` dan `Canceled`
21. Dengan dropdown tetap terbuka, uncheck `Canceled`
22. Verifikasi chip `Canceled` hilang dari field
23. Verifikasi chip `Approved` tetap ada
24. Tutup dropdown dan klik `[Apply]`
25. Verifikasi tabel menampilkan 6 baris: #2, #5, #6, #7, #11, #12
26. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-432: Dua field berbeda dihitung AND

27. Isi Type = `Activation Collision` dan Approval = `Rejected`
28. Klik `[Apply]`
29. Verifikasi tabel menampilkan irisan 2 baris: #3, #10
30. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-433: Search lalu Filter, filter menimpa tanpa mereset keyword

31. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameHistory`, tekan Enter
32. Isi Type = `Activation Collision`
33. Klik `[Apply]`
34. Verifikasi tabel menampilkan irisan Search dan Filter, 3 baris: #1, #8, #10
35. Verifikasi keyword `Fixture.hardwareStock.derived.clientCoreNameHistory` tetap terisi di kotak Search
36. Klik `[Clear Field]`, lalu klik `[Apply]`
37. Klik icon `(←)`

### TC-AC-ACHS-434: Filter lalu Search, hasil identik dengan urutan Search lalu Filter

38. Isi Type = `Activation Collision`, klik `[Apply]`
39. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameHistory`, tekan Enter
40. Verifikasi tabel menampilkan 3 baris: #1, #8, #10, identik dengan hasil urutan Search lalu Filter
41. Klik icon `(←)`
42. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-435: Clear Field mempertahankan Search dan Sort aktif

43. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameHistory`, tekan Enter
44. Klik header kolom Resolved At sekali (Ascending)
45. Isi Type = `Activation Collision`, klik `[Apply]`
46. Klik `[Clear Field]`, lalu klik `[Apply]`
47. Verifikasi Filter Type kosong kembali
48. Verifikasi keyword `Fixture.hardwareStock.derived.clientCoreNameHistory` tetap menyaring 3 baris: #1, #8, #10
49. Verifikasi indikator sort Ascending tetap aktif pada Resolved At
50. Klik header kolom Resolved At dua kali sampai indikator sort netral
51. Klik icon `(←)`

### TC-AC-ACHS-436: Menutup panel tanpa Apply membuang draft

52. Isi Type = `Activation Collision`, klik `[Apply]`
53. Ubah field Approval menjadi `Rejected` tanpa klik `[Apply]`
54. Klik icon Filter untuk menutup panel
55. Klik icon Filter untuk membuka panel kembali
56. Verifikasi panel menampilkan nilai ter-Apply terakhir: Type = `Activation Collision`
57. Verifikasi draft Approval `Rejected` tidak tampil
58. Verifikasi tabel tetap menampilkan hasil filter terakhir yang di-Apply, 6 baris: #1, #3, #6, #8, #10, #12
59. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACHS-437: Indikator filter aktif, badge titik tanpa angka

60. Verifikasi ikon Filter tanpa badge
61. Isi Type = `Register Duplicate`, klik `[Apply]`
62. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel terbuka
63. Klik icon Filter untuk menutup panel
64. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel tertutup
65. Klik icon Filter untuk membuka panel
66. Klik `[Clear Field]`, lalu klik `[Apply]`
67. Verifikasi badge titik hilang dari ikon Filter

### TC-AC-ACHS-438: Filter independen dari Column Visibility, hide kolom Type tidak menghapus filter

68. Isi Type = `Activation Collision`, klik `[Apply]`
69. Klik header kolom Actions `(⋯)`
70. Uncheck `Type`
71. Klik icon Filter untuk membuka kembali Filter Panel
72. Verifikasi field Type tetap ada di Filter Panel dengan nilai `Activation Collision`
73. Verifikasi filter yang sudah di-Apply tetap berlaku, 6 baris: #1, #3, #6, #8, #10, #12
74. Klik header kolom Actions `(⋯)`, check `Type` kembali
75. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-429 sampai 438). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (bukan dari langkah TC): langkah 9, 19, 26, 30, 36, 42, 59, 66, 75 (membersihkan filter dengan `[Clear Field]` dan `[Apply]` agar TC berikutnya bermula dari tabel tanpa filter, S-09), langkah 37, 41, 51 (klik `(←)` mereset Search), langkah 50 (mengembalikan sort ke netral), langkah 74 (memulihkan kolom Type). Filter Panel tetap terbuka sesudah `[Apply]` (ditunjukkan TC-AC-ACHS-436), sehingga klik icon Filter hanya muncul pada langkah 3 dan pada TC yang menutup dan membuka panel.
- Spec ini di atas 35 langkah (75 langkah nominal). Alasan: semua blok memakai satu Filter Panel dan satu dataset read-only (Tab History), tiap TC dimulai dari tabel tanpa filter berkat langkah pembersih, dan topik Filter satu dataset digabung sesuai prinsip 1.
- Konfirmasi (#8): nama inti Client sama dengan substring yang ditulis TC-433 sampai 435 (bukan nilai kolom penuh); hasil pada Tabel D: tiga baris #1, #8, #10 (semua Activation Collision), sehingga irisan dengan Type = `Register Duplicate` kosong sesuai TC. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-430 dan TC-431 menjalankan "centang" lalu klik `(X)` atau uncheck tanpa menyebut apakah dropdown ditutup sebelumnya; spec mengikuti kata TC.
  - TC-437 "isi satu field" tidak menyebut field atau nilai; spec memakai Type = `Register Duplicate`.
  - TC-438 langkah 5 ("Buka kembali Filter Panel") tidak menyebut apakah panel masih terbuka sesudah overlay Column Visibility dibuka; spec menulis klik icon Filter dan hasilnya bergantung pada perilaku itu.
  - TC-435 butir b menyebut urutan hasil default padahal sort Resolved At Ascending aktif; spec hanya mengasersi himpunan 3 baris.
  - Populasi Pre-setup #22 dirujuk lewat nomor baris Tabel D (`#n` = `Fixture.hardwareStock.p22.d[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nama literal Pre-setup di spec dan tanpa pengecualian S-12. Literal yang tetap ada adalah teks UI nyata (placeholder, nilai Type, Approval, Category, `System`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
