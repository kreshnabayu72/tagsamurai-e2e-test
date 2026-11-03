---
id: TC-AC-ACHS-E2E-200-search-approvals-tab-history
title: "Search Approvals > Hardware Stock Tab History"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-417
  - TC-AC-ACHS-418
  - TC-AC-ACHS-419
  - TC-AC-ACHS-420
  - TC-AC-ACHS-421
  - TC-AC-ACHS-422
  - TC-AC-ACHS-423
  - TC-AC-ACHS-424
coverage:
  web: automated
---

# Search Approvals > Hardware Stock Tab History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini. Baris dirujuk lewat nomor baris Tabel D: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel D (`Fixture.hardwareStock.p22.d[n]`) pada urutan default (Resolved At terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup dan tidak ditulis di spec ini. Nama, urutan, dan jumlah persis populasi menentukan asersi, sehingga isi tiap baris dipakai apa adanya dari fixture. Footer tabel dengan 12 entri pada ukuran halaman 10 membaca `Showing 1–10 of 12 entries`.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama singkat akun Total Control Principal #1 | #1 | Total Control Principal; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p01.totalControl.shortName` |
  | Type baris #n (n = 1 sampai 12) | #22 Tabel D | Activation Collision pada #1, #3, #6, #8, #10, #12; Register Duplicate pada #2, #4, #5, #7, #9, #11 | `Fixture.hardwareStock.p22.d[n].type` |
  | Device Name (SKU) baris #n (n = 1 sampai 12) | #22 Tabel D | Device Name diikuti kode SKU dalam kurung; #8 adalah Subject BYO tanpa SKU (berakhiran `(—)`, Category `—`) | `Fixture.hardwareStock.p22.d[n].deviceName` |
  | Category baris #n (n = 1 sampai 12) | #22 Tabel D | Short Range pada #1, #2, #6, #7, #9, #11; Long Range pada #4, #5, #10; Smart Fixed Reader pada #3, #12; `—` pada #8 | `Fixture.hardwareStock.p22.d[n].category` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #22 Tabel D | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #5 dan #8 berformat MAC dengan awalan yang sama | `Fixture.hardwareStock.p22.d[n].matchedIdentifier` |
  | Existing Record baris #n (n = 1 sampai 12) | #22 Tabel D | memuat kata `Registrant` pada #2, #4, #5, #7, #9, #11; memuat `Active (Client: ...)` pada baris lain | `Fixture.hardwareStock.p22.d[n].existingRecord` |
  | Requested By baris #n (n = 1 sampai 12) | #22 Tabel D | Client, Distributor, atau Principal dengan label peran dalam kurung; entitas yang sama pada #4 dan #11 serta #8 dan #12 | `Fixture.hardwareStock.p22.d[n].requestedBy` |
  | Approval baris #n (n = 1 sampai 12) | #22 Tabel D | Canceled pada #1, #8; Approved pada #2, #5, #6, #7, #11, #12; Rejected pada #3, #4, #9, #10 | `Fixture.hardwareStock.p22.d[n].approval` |
  | Approver baris #n (n = 1 sampai 12) | #22 Tabel D | `—` pada #1 dan #8 (Canceled); `System` pada #7; nama singkat akun Pre-setup #1 pada #2, #3, #9, #11, akun #2 pada #4, #5, #12, akun #6 pada #6, #10 | `Fixture.hardwareStock.p22.d[n].approver` |
  | Requested At baris #n (n = 1 sampai 12) | #22 Tabel D | tanggal Requested At tiap baris, format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p22.d[n].requestedAt` |
  | Keyword Search nama Client | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[10].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; muncul pada Existing Record atau Requested By tepat tiga baris #1, #8, #10 | `Fixture.hardwareStock.derived.clientCoreNameHistory` |
  | Keyword Search nama depan akun | #1 dan #22 Tabel D | diturunkan dari `Fixture.hardwareStock.account.p01.totalControl.shortName`: kata pertama (nama depan); muncul sebagai Approver pada #2, #3, #9, #11 | `Fixture.hardwareStock.derived.firstNameTotalControl` |
  | Keyword Search Device Name | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[8].deviceName`: dua kata pertama (tanpa kode SKU); hanya #8 yang memuatnya | `Fixture.hardwareStock.derived.deviceNameBleHistory` |
  | Keyword Search Matched Identifier | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[5].matchedIdentifier`: dua oktet pertama, awalan yang dipakai bersama #8; tidak mengandung huruf kecil | `Fixture.hardwareStock.derived.macPrefixSharedHistory` |
  | Keyword Search Requested By | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[8].requestedBy`: kata pertama nama entitas; muncul pada #8 dan #12 | `Fixture.hardwareStock.derived.requestedByFirstWord` |
  | Keyword Search bulan dan tahun | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[1].requestedAt`: bagian bulan dan tahun (tanpa hari dan jam); Requested At dan Resolved At bukan kolom searchable | `Fixture.hardwareStock.derived.requestedAtMonthYearHistory` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): hook `after` menghapus preferensi kolom Setup Column di browser (spec ini tidak menyimpan konfigurasi kolom; Column Visibility pada langkah 57 sampai 62 dipulihkan oleh spec).
- State global: tidak ada yang diubah.
- Suite serial: `parallel: false` (lihat suite.md).
- Parameter Search (dipakai langkah 27 sampai 43). Kolom Hasil memuat Matched Identifier baris hasil, urutan default:

| No | TC | Kolom | Keyword | Keyword kapital | Hasil |
|---|---|---|---|---|---|
| 1 | 418 | Type | `Duplicate` | `DUPLICATE` | 6 baris: #2, #4, #5, #7, #9, #11 |
| 2 | 418 | Approval | `Canceled` | `CANCELED` | 2 baris: #1, #8 |
| 3 | 419 | Device Name (SKU) | `Fixture.hardwareStock.derived.deviceNameBleHistory` | `Fixture.hardwareStock.derived.deviceNameBleHistory` kapital | 1 baris: #8 |
| 4 | 419 | Category | `Short Range` | `SHORT RANGE` | 6 baris: #1, #2, #6, #7, #9, #11 |
| 5 | 419 | Matched Identifier | `Fixture.hardwareStock.derived.macPrefixSharedHistory` | `Fixture.hardwareStock.derived.macPrefixSharedHistory` kapital | 2 baris: #5, #8 |
| 6 | 419 | Existing Record | `Registrant` | `REGISTRANT` | 6 baris: #2, #4, #5, #7, #9, #11 |
| 7 | 419 | Requested By | `Fixture.hardwareStock.derived.requestedByFirstWord` | `Fixture.hardwareStock.derived.requestedByFirstWord` kapital | 2 baris: #8, #12 |
| 8 | 420 | Approver | `System` | `SYSTEM` | 1 baris: #7 |

## Test Steps

### TC-AC-ACHS-417: Siklus Search toolbar (reveal, ketik belum menyaring, Enter, clear, Enter kosong, collapse)

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`
3. Hover icon Search
4. Verifikasi tooltip `Search`
5. Klik icon Search
6. Verifikasi kotak Search melebar
7. Verifikasi kursor fokus di input
8. Verifikasi placeholder `Search by device name, identifier, or entity...`
9. Ketik `Fixture.hardwareStock.derived.clientCoreNameHistory` tanpa menekan Enter
10. Verifikasi icon `(✕)` muncul
11. Verifikasi tabel belum tersaring: footer `Showing 1–10 of 12 entries`
12. Tekan Enter
13. Verifikasi 3 baris: #1, #8, #10
14. Klik icon `(✕)` di kotak Search
15. Verifikasi input kosong
16. Verifikasi kotak Search tetap terbuka
17. Verifikasi kursor tetap fokus di input
18. Verifikasi tabel masih menampilkan hasil search terakhir: 3 baris #1, #8, #10
19. Tekan Enter pada input yang sudah kosong
20. Verifikasi tabel kembali menampilkan 12 entri: footer `Showing 1–10 of 12 entries`
21. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameHistory`, tekan Enter
22. Klik icon `(←)` di kiri toolbar
23. Verifikasi kotak Search menutup menjadi icon Search
24. Verifikasi keyword Search dikosongkan
25. Verifikasi tabel langsung kembali ke seluruh baris tanpa Enter: footer `Showing 1–10 of 12 entries`

### TC-AC-ACHS-418: Search kelas badge (substring dan case-insensitive)

26. Untuk setiap baris 1 sampai 2 pada tabel Parameter Search, lakukan langkah 27 sampai 31
27. Ketik Search keyword baris tersebut, tekan Enter
28. Verifikasi hasil sesuai kolom Hasil baris tersebut
29. Ganti isi kotak search dengan keyword kapital baris tersebut, tekan Enter
30. Verifikasi hasil identik dengan hasil pada langkah 28
31. Klik icon `(←)`

### TC-AC-ACHS-419: Search kelas teks (substring dan case-insensitive)

32. Untuk setiap baris 3 sampai 7 pada tabel Parameter Search, lakukan langkah 33 sampai 37
33. Ketik Search keyword baris tersebut, tekan Enter
34. Verifikasi hasil sesuai kolom Hasil baris tersebut
35. Ganti isi kotak search dengan keyword kapital baris tersebut, tekan Enter
36. Verifikasi hasil identik dengan hasil pada langkah 34
37. Klik icon `(←)`

### TC-AC-ACHS-420: Search kelas pengguna (substring dan case-insensitive)

38. Untuk baris 8 pada tabel Parameter Search, lakukan langkah 39 sampai 43
39. Ketik Search keyword baris tersebut, tekan Enter
40. Verifikasi hasil sesuai kolom Hasil baris tersebut
41. Ganti isi kotak search dengan keyword kapital baris tersebut, tekan Enter
42. Verifikasi hasil identik dengan hasil pada langkah 40
43. Klik icon `(←)`

### TC-AC-ACHS-421: Search tanpa hasil menampilkan empty state

44. Ketik Search `zzqx-tidak-ada`, tekan Enter
45. Verifikasi tabel tidak menampilkan baris data
46. Verifikasi empty state: Illustration + Title `No results found` + Description `Try adjusting your search or filter.`
47. Klik icon `(←)`

### TC-AC-ACHS-422: Search tidak mencari kolom non-searchable (Requested At, Resolved At)

48. Ketik Search `Fixture.hardwareStock.derived.requestedAtMonthYearHistory` (bulan dan tahun nilai kolom Requested At yang tampil di tabel), tekan Enter
49. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found`
50. Verifikasi nilai kolom Requested At dan Resolved At tidak memicu match
51. Klik icon Filter
52. Verifikasi Filter Panel memuat field Requested At dan Resolved At sebagai satu-satunya jalur penyaringan kolom tanggal
53. Klik icon Filter untuk menutup panel
54. Klik icon `(←)`

### TC-AC-ACHS-423: Search terikat visibilitas kolom Approver (hide lalu unhide)

55. Ketik Search `Fixture.hardwareStock.derived.firstNameTotalControl`, tekan Enter
56. Verifikasi 4 baris: #2, #3, #9, #11
57. Klik header kolom Actions `(⋯)` (tooltip `Column Visibility`)
58. Uncheck `Approver`
59. Ganti isi kotak search dengan `Fixture.hardwareStock.derived.firstNameTotalControl`, tekan Enter
60. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found` (kolom Approver tidak lagi dicari)
61. Buka kembali `Column Visibility`
62. Check `Approver`
63. Ganti isi kotak search dengan `Fixture.hardwareStock.derived.firstNameTotalControl`, tekan Enter
64. Verifikasi hasil kembali sama dengan sebelum hide: 4 baris #2, #3, #9, #11
65. Klik icon `(←)`

### TC-AC-ACHS-424: Search membuang spasi awal dan akhir query saat Enter

66. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameHistory` dengan dua spasi di awal dan akhir (spasi di awal dan akhir), tekan Enter
67. Verifikasi hasil sama dengan keyword tanpa spasi tepi: 3 baris #1, #8, #10
68. Verifikasi isi kotak Search di layar tetap `Fixture.hardwareStock.derived.clientCoreNameHistory` dengan dua spasi di awal dan akhir
69. Ganti isi kotak search dengan `   ` (hanya spasi), tekan Enter
70. Verifikasi query yang hanya berisi spasi dianggap kosong: tabel kembali ke seluruh 12 entri (`Showing 1–10 of 12 entries`)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-417 sampai 424). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 31, 37, 43, 47, 54, 65 (klik `(←)` menutup input dan mereset tabel sebelum blok berikutnya, S-09), langkah 51 sampai 53 (membuka dan menutup Filter Panel untuk mengamati field tanggal). Langkah 59 dan 63 mengulang search yang sama sesuai langkah TC 5 dan 6.
- Spec ini di atas 35 langkah dengan ekspansi blok ulang (langkah 27 sampai 31, 33 sampai 37, 39 sampai 43: 8 iterasi kali 5 langkah). Alasan: semua blok berada pada satu permukaan dan satu dataset read-only (Tab History), tiap blok berdiri sendiri (kegagalan satu keyword tidak mengubah makna keyword lain), dan topik Search satu dataset digabung sesuai prinsip 1.
- Urutan TC mengikuti urutan sumber. TC-AC-ACHS-422 butir c ("penyaringan kolom itu hanya lewat Filter Panel") tidak punya langkah observasi di TC; spec mengamatinya dengan membuka Filter Panel (langkah 51 sampai 52) dan dicatat di sini sebagai asersi tambahan beralasan (S-03).
- Konfirmasi (#8): kata kunci turunan Search diperiksa terhadap Tabel D TC. Nama inti Client, dua kata pertama Device Name #8, dua oktet pertama Matched Identifier #5, kata pertama Requested By #8, nama depan akun Pre-setup #1, dan bulan-tahun Requested At sama dengan substring yang ditulis TC-417, 419, 422, dan 423 (bukan nilai kolom penuh); himpunan hasil identik dengan TC: nama Client #1, #8, #10; Device Name #8; Matched Identifier #5, #8; Requested By #8, #12; nama depan akun pada Approver #2, #3, #9, #11; bulan-tahun 0 baris. Tidak ada perbedaan.
- Temuan untuk QA:
  - Email akun Pre-setup #1 ditulis lengkap di TC; password env `AC_TC_PASSWORD` dan password akun lain memakai nama yang ditetapkan tim FE (lihat suite.md).
  - TC-419 baris Matched Identifier memakai keyword `Fixture.hardwareStock.derived.macPrefixSharedHistory` untuk huruf biasa dan huruf kapital sehingga sifat case-insensitive tidak teruji pada kolom itu; spec mengikuti TC.
  - TC-417 Expected e menyebut tabel "masih hasil search terakhir" tanpa jumlah baris; spec memakai 3 baris dari butir d.
  - TC-422 potongan bulan-tahun Requested At bergantung pada format tanggal General Settings yang dipakai tampilan (tidak diubah spec ini).
  - Populasi Pre-setup #22 dirujuk lewat nomor baris Tabel D (`#n` = `Fixture.hardwareStock.p22.d[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nama literal Pre-setup di spec dan tanpa pengecualian S-12. Literal yang tetap ada adalah teks UI nyata (placeholder, nilai Type, Approval, Category, `System`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
