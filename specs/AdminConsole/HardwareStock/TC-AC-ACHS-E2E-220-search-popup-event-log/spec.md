---
id: TC-AC-ACHS-E2E-220-search-popup-event-log
title: "Search Popup Event Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-466
  - TC-AC-ACHS-467
  - TC-AC-ACHS-468
  - TC-AC-ACHS-469
  - TC-AC-ACHS-470
  - TC-AC-ACHS-471
  - TC-AC-ACHS-472
coverage:
  web: automated
---

# Search Popup Event Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Spec membuka Stock Detail dan popup Event Log sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #20 TC (Tabel B), SKU `Fixture.hardwareStock.p16.a[4].sku` (Handheld Reader - Long Range) memiliki 12 sesi Event Log pada Pre-setup (Tabel B baris #1 sampai #12); baris dikenali lewat kolom Date. Event Log adalah audit trail permanen dan spec lain dapat menambah sesi pada SKU ini, sehingga total tanpa filter tidak diasersi absolut (S-12): hook `before` membaca jumlah sesi sebagai `{nEventLog}` (baseline) lewat kemampuan baca dan footer tanpa filter membaca `Showing 1–10 of {nEventLog} entries`. Baris dirujuk lewat nomor baris Tabel B: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel B (`Fixture.hardwareStock.p20.b[n]`) pada urutan default (Date terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU Handheld Reader Long Range | #16 Tabel A baris 4 | kode SKU Handheld Reader - Long Range (RFD40); pemilik Event Log Pre-setup #20 | `Fixture.hardwareStock.p16.a[4].sku` |
  | Date baris #n (n = 1 sampai 12) | #20 Tabel B | identitas baris hasil; urutan default Date terbaru lebih dulu; format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p20.b[n].date` |
  | Activity baris #n (n = 1 sampai 12) | #20 Tabel B | Delete Stock pada #1, #5, #9; Add Stock pada baris lain (9 baris) | `Fixture.hardwareStock.p20.b[n].activity` |
  | Modified By baris #n (n = 1 sampai 12) | #20 Tabel B | nama singkat user: akun Pre-setup #1 pada #1, #4, #7, #10; user Distributor Pre-setup #11 pada #2, #5, #8, #11; user Distributor Pre-setup #10 pada #3, #6, #9, #12 | `Fixture.hardwareStock.p20.b[n].modifiedBy` |
  | Jumlah sesi Event Log SKU Handheld Reader Long Range (`nEventLog`) | #20 | baseline relatif: jumlah sesi yang dibaca hook `before` lewat kemampuan baca (disediakan tim FE/BE) sebelum aksi pertama; Pre-setup #20 menyediakan 12 sesi tetapi angka itu tidak diasersi | dibaca saat run |
  | Nama singkat akun Total Control Principal #1 | #1 | Total Control Principal; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p01.totalControl.shortName` |
  | Nama singkat akun user Distributor #11 | #11 | user Distributor; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |
  | Keyword Search nama depan user | #1 dan #20 Tabel B | diturunkan dari `Fixture.hardwareStock.account.p01.totalControl.shortName`: kata pertama (nama depan); muncul pada Modified By #1, #4, #7, #10 | `Fixture.hardwareStock.derived.firstNameTotalControl` |
  | Keyword Search nama depan user Distributor | #11 dan #20 Tabel B | diturunkan dari `Fixture.hardwareStock.account.p11.distributorMitra.shortName`: kata pertama (nama depan); muncul pada Modified By #2, #5, #8, #11 | `Fixture.hardwareStock.derived.firstNameDistributorMitra` |
  | Keyword Search bulan dan tahun | #20 Tabel B | diturunkan dari `Fixture.hardwareStock.p20.b[1].date`: bagian bulan dan tahun (tanpa hari dan jam); Date bukan kolom searchable | `Fixture.hardwareStock.derived.dateMonthYear` |
- Format tanggal dan jam General Settings: bawaan yang tampil pada Pre-setup (contoh #1); spec tidak mengubahnya.
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman yang dipakai suite (lihat suite.md).
- State global: Column Visibility kolom Modified By disembunyikan pada langkah 48 dan dipulihkan pada langkah 52. Suite serial: `parallel: false` (lihat suite.md).
- Parameter Search (langkah 28 sampai 32). Kolom Hasil memuat nilai kolom Date baris hasil, urutan default:

| No | TC | Kolom | Keyword | Keyword kapital | Hasil |
|---|---|---|---|---|---|
| 1 | 467 | Activity | `Add Stock` | `ADD STOCK` | 9 baris, lima teratas: #2, #3, #4, #6, #7 |
| 2 | 468 | Modified By | `Fixture.hardwareStock.derived.firstNameTotalControl` | `Fixture.hardwareStock.derived.firstNameTotalControl` kapital | 4 baris: #1, #4, #7, #10 |

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Klik Tab `Available`
3. Klik icon `[Event Log]` di toolbar

### TC-AC-ACHS-466: Siklus Search toolbar (reveal, ketik belum menyaring, Enter, clear, Enter kosong, collapse)

4. Hover icon Search
5. Verifikasi tooltip `Search`
6. Klik icon Search
7. Verifikasi kotak Search melebar
8. Verifikasi kursor fokus di input
9. Verifikasi placeholder `Search by activity or modified by...`
10. Ketik `Delete` tanpa menekan Enter
11. Verifikasi icon `(✕)` muncul
12. Verifikasi tabel belum tersaring: footer `Showing 1–10 of {nEventLog} entries`
13. Tekan Enter
14. Verifikasi 3 baris: #1, #5, #9
15. Klik icon `(✕)` di kotak Search
16. Verifikasi input kosong
17. Verifikasi kotak Search tetap terbuka
18. Verifikasi kursor tetap fokus di input
19. Verifikasi tabel masih menampilkan hasil search terakhir: 3 baris #1, #5, #9
20. Tekan Enter pada input yang sudah kosong
21. Verifikasi tabel kembali menampilkan seluruh entri: footer `Showing 1–10 of {nEventLog} entries`
22. Ketik Search `Delete`, tekan Enter
23. Klik icon `(←)` di kiri toolbar
24. Verifikasi kotak Search menutup menjadi icon Search
25. Verifikasi keyword Search dikosongkan
26. Verifikasi tabel langsung kembali ke seluruh baris tanpa Enter: footer `Showing 1–10 of {nEventLog} entries`

### TC-AC-ACHS-467 dan TC-AC-ACHS-468: Search kelas teks dan kelas pengguna (substring dan case-insensitive)

27. Untuk setiap baris tabel Parameter Search (2 baris), lakukan langkah 28 sampai 32
28. Ketik Search keyword baris tersebut, tekan Enter
29. Verifikasi hasil sesuai kolom Hasil baris tersebut
30. Ganti isi kotak search dengan keyword kapital baris tersebut, tekan Enter
31. Verifikasi hasil identik dengan hasil pada langkah 29
32. Klik icon `(←)`

### TC-AC-ACHS-469: Search tanpa hasil menampilkan empty state

33. Ketik Search `zzqx-tidak-ada`, tekan Enter
34. Verifikasi tabel tidak menampilkan baris data
35. Verifikasi empty state: Illustration + Title `No results found` + Description `Try adjusting your search or filter.`
36. Klik icon `(←)`

### TC-AC-ACHS-470: Search tidak mencari kolom non-searchable (Date, Success, Waiting for Approval)

37. Ketik Search `Fixture.hardwareStock.derived.dateMonthYear` (bagian bulan dan tahun nilai kolom Date yang tampil di tabel), tekan Enter
38. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found`
39. Verifikasi nilai kolom Date, Success, dan Waiting for Approval tidak memicu match
40. Klik icon Filter
41. Verifikasi Filter Panel memuat field Date sebagai jalur penyaringan kolom tanggal
42. Klik icon Filter untuk menutup panel
43. Klik icon `(←)`

### TC-AC-ACHS-471: Search terikat visibilitas kolom Modified By (hide lalu unhide)

44. Ketik Search `Fixture.hardwareStock.derived.firstNameDistributorMitra`, tekan Enter
45. Verifikasi 4 baris: #2, #5, #8, #11
46. Klik header kolom Actions `(⋯)` (tooltip `Column Visibility`)
47. Verifikasi overlay `Column Visibility` terbuka
48. Uncheck `Modified By`
49. Ganti isi kotak search dengan `Fixture.hardwareStock.derived.firstNameDistributorMitra`, tekan Enter
50. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found` (kolom Modified By tidak lagi dicari)
51. Buka kembali `Column Visibility`
52. Check `Modified By`
53. Ganti isi kotak search dengan `Fixture.hardwareStock.derived.firstNameDistributorMitra`, tekan Enter
54. Verifikasi hasil kembali sama dengan sebelum hide: 4 baris #2, #5, #8, #11
55. Klik icon `(←)`

### TC-AC-ACHS-472: Search membuang spasi awal dan akhir query saat Enter

56. Ketik Search `  Delete  ` (spasi di awal dan akhir), tekan Enter
57. Verifikasi hasil sama dengan keyword tanpa spasi tepi: 3 baris #1, #5, #9
58. Verifikasi isi kotak Search di layar tetap `  Delete  `
59. Ganti isi kotak search dengan `   ` (hanya spasi), tekan Enter
60. Verifikasi query yang hanya berisi spasi dianggap kosong: tabel kembali ke seluruh entri (`Showing 1–10 of {nEventLog} entries`)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-466 sampai 472). Tidak ada TC hanya-BE di spec ini.
- Langkah 1 sampai 3 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Langkah penghubung (bukan dari langkah TC): langkah 2 (`Klik Tab Available`, dari langkah TC "Pastikan Tab Available aktif"), langkah 32, 36, 43, 55 (klik `(←)` mereset Search, S-09), langkah 40 sampai 42 (membuka dan menutup Filter Panel untuk mengamati field tanggal), langkah 47 (anchor positif overlay Column Visibility terbuka). Langkah 49 dan 53 mengulang search yang sama sesuai langkah TC 7 dan 8.
- Spec ini di atas 35 langkah (60 langkah nominal). Alasan: semua blok berada pada satu popup dan satu dataset read-only (Event Log SKU `Fixture.hardwareStock.p16.a[4].sku`), tiap blok berdiri sendiri, dan topik Search satu dataset digabung sesuai prinsip 1.
- Konfirmasi (#8): nama depan user akun Pre-setup #1, nama depan user Distributor Pre-setup #11, dan bulan-tahun Date #1 sama dengan substring yang ditulis TC-468, 471, dan 470 (bukan nilai kolom penuh); himpunan hasil identik dengan TC pada Tabel B: nama depan akun #1 pada Modified By #1, #4, #7, #10; nama depan user Distributor #11 pada #2, #5, #8, #11; bulan-tahun 0 baris. Tidak ada perbedaan.
- Total Event Log (S-12): angka 12 adalah Pre-setup #20 dan spec tidak mengasersi angka absolut; `{nEventLog}` dibaca hook `before` sebelum aksi pertama dan asersi pagination/footer tanpa filter diturunkan darinya. Footer hasil Search/Filter yang menyaring (mis. `Showing 1–3 of 3 entries`) tetap literal karena hasil filter deterministik dari Tabel B.
- Temuan untuk QA:
  - TC-470 butir c menyebut penyaringan kolom Date, Success, dan Waiting for Approval hanya lewat Filter Panel, tetapi Filter Panel Event Log hanya memuat Date, Activity, dan Modified By (TC-473); spec mengamati field Date saja.
  - TC-470 `Fixture.hardwareStock.derived.dateMonthYear` bergantung pada format tanggal General Settings yang tampil.
  - Populasi Pre-setup #20 dirujuk lewat nomor baris Tabel B (`#n` = `Fixture.hardwareStock.p20.b[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nilai literal Pre-setup di spec dan tanpa pengecualian S-12. Angka 12 sesi adalah populasi Pre-setup #20 dan tidak diasersi absolut: total tanpa filter memakai baseline relatif `{nEventLog}` (S-12, keputusan 2026-11-02). Literal yang tetap ada adalah teks UI nyata (placeholder, `Add Stock`, `Delete Stock`, `Delete`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
