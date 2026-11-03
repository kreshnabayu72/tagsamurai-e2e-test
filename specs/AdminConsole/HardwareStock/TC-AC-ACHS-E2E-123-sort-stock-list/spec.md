---
id: TC-AC-ACHS-E2E-123-sort-stock-list
title: "Sort Stock List: Siklus 3-State Semua Kolom, Urutan Default, Nilai Kosong, Tie-Break, Kolom Non-Sortable, dan Search Tidak Direset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-227
  - TC-AC-ACHS-228
  - TC-AC-ACHS-229
  - TC-AC-ACHS-230
  - TC-AC-ACHS-231
  - TC-AC-ACHS-232
  - TC-AC-ACHS-233
  - TC-AC-ACHS-257
  - TC-AC-ACHS-258
coverage:
  web: automated
---

# Sort Stock List: Siklus 3-State Semua Kolom, Urutan Default, Nilai Kosong, Tie-Break, Kolom Non-Sortable, dan Search Tidak Direset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List (lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): #16 Katalog SKU 30 baris Stock List (Tabel A: 8 SKU nama dan 22 SKU `Fixture.hardwareStock.p16.a[9].sku` sampai `Fixture.hardwareStock.p16.a[30].sku`) dan #15 General Settings (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Brand baris 1 Tabel A | #16 Katalog SKU (Tabel A) | Brand baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19); Brand yang sama pada baris 3 dan 4 | `Fixture.hardwareStock.p16.a[1].brand` |
  | Model/Type baris 1 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p16.a[1].modelType` |
  | SKU baris 1 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p16.a[1].sku` |
  | SKU baris 2 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available | `Fixture.hardwareStock.p16.a[2].sku` |
  | Model/Type baris 3 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 3 Tabel A (#16): Smart Fixed Reader, 8 Available (#27) | `Fixture.hardwareStock.p16.a[3].modelType` |
  | SKU baris 3 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 3 Tabel A (#16): Smart Fixed Reader, 8 Available (#27) | `Fixture.hardwareStock.p16.a[3].sku` |
  | Model/Type baris 4 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].modelType` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | SKU baris 5 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 5 Tabel A (#16): BLE Gateway, 4 Available dan 1 In Use (#27) | `Fixture.hardwareStock.p16.a[5].sku` |
  | SKU baris 6 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 6 Tabel A (#16): Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated kosong) | `Fixture.hardwareStock.p16.a[6].sku` |
  | SKU baris 7 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 7 Tabel A (#16): BLE Gateway dengan Brand dan Model/Type bernilai panjang | `Fixture.hardwareStock.p16.a[7].sku` |
  | SKU baris 8 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 8 Tabel A (#16): Smart Fixed Reader dengan 120 Available (#24) | `Fixture.hardwareStock.p16.a[8].sku` |
  | SKU baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].sku` |
  | SKU baris padding 02 (Tabel A baris 10) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 02 (#16) | `Fixture.hardwareStock.p16.a[10].sku` |
  | SKU baris padding 03 (Tabel A baris 11) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 03 (#16) | `Fixture.hardwareStock.p16.a[11].sku` |
  | SKU baris padding 04 (Tabel A baris 12) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 04 (#16) | `Fixture.hardwareStock.p16.a[12].sku` |
  | SKU baris padding 05 (Tabel A baris 13) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 05 (#16) | `Fixture.hardwareStock.p16.a[13].sku` |
  | SKU baris padding 06 (Tabel A baris 14) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 06 (#16) | `Fixture.hardwareStock.p16.a[14].sku` |
  | SKU baris padding 17 (Tabel A baris 25) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 17 (#16) | `Fixture.hardwareStock.p16.a[25].sku` |
  | SKU baris padding 19 (Tabel A baris 27) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 19 (#16) | `Fixture.hardwareStock.p16.a[27].sku` |
  | SKU baris padding 20 (Tabel A baris 28) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 20 (#16) | `Fixture.hardwareStock.p16.a[28].sku` |
  | SKU baris padding 21 (Tabel A baris 29) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 21 (#16) | `Fixture.hardwareStock.p16.a[29].sku` |
  | SKU baris padding 22 (Tabel A baris 30) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 22 (#16) | `Fixture.hardwareStock.p16.a[30].sku` |
- Urutan default (netral): teratas `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`.
- Data uji TC-AC-ACHS-227 sampai TC-AC-ACHS-230 (siklus 3-state; klik #3 setiap kolom kembali netral dengan tiga baris teratas urutan default; kolom "TC" menunjuk kelas kolom: 227 teks, 228 badge, 229 angka, 230 tanggal):

  | No | TC | Kolom | Tiga teratas Ascending (`↑`) | Tiga teratas Descending (`↓`) |
  |---|---|---|---|---|
  | 1 | 227 | Device Name | `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[8].sku` | `Fixture.hardwareStock.p16.a[30].sku`, `Fixture.hardwareStock.p16.a[29].sku`, `Fixture.hardwareStock.p16.a[28].sku` |
  | 2 | 227 | SKU | `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[2].sku` | `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[6].sku`, `Fixture.hardwareStock.p16.a[8].sku` |
  | 3 | 227 | Range Type | `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[2].sku` | `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku` |
  | 4 | 228 | Type | `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[4].sku` | `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[29].sku` |
  | 5 | 228 | Brand | `Fixture.hardwareStock.p16.a[29].sku`, `Fixture.hardwareStock.p16.a[27].sku`, `Fixture.hardwareStock.p16.a[25].sku` | `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku` |
  | 6 | 228 | Model/Type | `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[2].sku`, `Fixture.hardwareStock.p16.a[3].sku` | `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[5].sku` |
  | 7 | 229 | Total Registered | `Fixture.hardwareStock.p16.a[6].sku`, `Fixture.hardwareStock.p16.a[9].sku`, `Fixture.hardwareStock.p16.a[10].sku` | `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[4].sku` |
  | 8 | 229 | Available | `Fixture.hardwareStock.p16.a[6].sku`, `Fixture.hardwareStock.p16.a[9].sku`, `Fixture.hardwareStock.p16.a[10].sku` | `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[30].sku` |
  | 9 | 229 | In Use | `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[3].sku` | `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[5].sku` |
  | 10 | 230 | Last Updated | `Fixture.hardwareStock.p16.a[9].sku`, `Fixture.hardwareStock.p16.a[11].sku`, `Fixture.hardwareStock.p16.a[13].sku` | `Fixture.hardwareStock.p16.a[10].sku`, `Fixture.hardwareStock.p16.a[12].sku`, `Fixture.hardwareStock.p16.a[14].sku` |

- Data uji TC-AC-ACHS-257 (nilai kosong `—`; rows per page 10 sehingga halaman terakhir adalah halaman 3):

  | No | Kolom | Ascending: teratas | Ascending: baris `—` terakhir | Descending: teratas (baris `—` di awal) |
  |---|---|---|---|---|
  | 1 | Range Type | `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[2].sku` | `Fixture.hardwareStock.p16.a[28].sku`, `Fixture.hardwareStock.p16.a[30].sku`, `Fixture.hardwareStock.p16.a[6].sku` | `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku` |

  Last Updated: Ascending (Oldest First) teratas `Fixture.hardwareStock.p16.a[9].sku`, `Fixture.hardwareStock.p16.a[11].sku`, `Fixture.hardwareStock.p16.a[13].sku` dengan baris `—` di akhir; Descending (Newest First) teratas `Fixture.hardwareStock.p16.a[10].sku`, `Fixture.hardwareStock.p16.a[12].sku`, `Fixture.hardwareStock.p16.a[14].sku` dengan baris `—` di awal; Netral teratas urutan default dengan baris `—` di paling bawah.
- Pilihan spec: TC-AC-ACHS-232 mengklik header Photo (langkah TC) lalu header Actions (Expected TC); TC-AC-ACHS-258 mengamati halaman terakhir (halaman 3) karena kolom Brand Ascending menaruh ketiga baris `Fixture.hardwareStock.p16.a[1].brand` di halaman itu.
- State global yang diubah: indikator sort dan Search dipulihkan ke netral pada akhir tiap TC. Preferensi kolom tidak diubah.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-227, 228, 229, 230: Siklus 3-state per kolom (teks, badge, angka, tanggal)

1. Untuk setiap baris tabel Data uji TC-AC-ACHS-227 sampai 230 (langkah 1 sampai 8): klik header kolom sekali
2. Verifikasi indikator Ascending (`↑`) aktif pada kolom
3. Verifikasi tiga baris teratas sesuai kolom "Ascending"
4. Klik header kolom lagi
5. Verifikasi indikator Descending (`↓`) aktif pada kolom
6. Verifikasi tiga baris teratas sesuai kolom "Descending"
7. Klik header kolom sekali lagi
8. Verifikasi kolom kembali netral dengan urutan default (tiga baris teratas `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku`)

### TC-AC-ACHS-231: Urutan default

9. Verifikasi urutan default: lima baris teratas `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`
10. Klik header Total Registered tiga kali sampai netral
11. Verifikasi urutan sama dengan urutan default (lima baris teratas sama)

### TC-AC-ACHS-232: Kolom non-sortable

12. Verifikasi kolom Photo tidak punya ikon sort
13. Klik header kolom Photo
14. Klik header kolom Actions `(⋯)`
15. Verifikasi urutan baris tidak berubah (lima baris teratas urutan default)
16. Verifikasi overlay `Column Visibility` terbuka
17. Tutup overlay Column Visibility

### TC-AC-ACHS-233: Sort tidak mereset Search dan Filter saat ganti kolom

18. Ketik Search `Fixture.hardwareStock.p16.a[1].brand`, tekan Enter
19. Klik header Total Registered (Ascending)
20. Klik header SKU (Ascending)
21. Verifikasi keyword `Fixture.hardwareStock.p16.a[1].brand` tetap terisi di kotak Search
22. Verifikasi tabel hanya berisi hasil search: 3 baris `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`
23. Verifikasi indikator Total Registered kembali netral
24. Verifikasi indikator SKU Ascending aktif
25. Klik header SKU dua kali sampai netral, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-257: Nilai kosong pada Range Type dan Last Updated

26. Klik header Range Type sekali (Ascending)
27. Verifikasi tiga baris teratas Range Type Ascending sesuai Data uji TC-AC-ACHS-257
28. Isi input halaman `3`, tekan Enter
29. Verifikasi baris bernilai `—` berada di akhir: tiga baris terakhir `Fixture.hardwareStock.p16.a[28].sku`, `Fixture.hardwareStock.p16.a[30].sku`, `Fixture.hardwareStock.p16.a[6].sku`
30. Isi input halaman `1`, tekan Enter
31. Klik header Range Type sekali lagi (Descending)
32. Verifikasi baris bernilai `—` berada di awal
33. Verifikasi tiga baris teratas Range Type Descending `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku`
34. Klik header Range Type sekali lagi sampai netral
35. Klik header Last Updated sekali (Ascending)
36. Verifikasi tiga baris teratas Last Updated Ascending (Oldest First) `Fixture.hardwareStock.p16.a[9].sku`, `Fixture.hardwareStock.p16.a[11].sku`, `Fixture.hardwareStock.p16.a[13].sku`
37. Isi input halaman `3`, tekan Enter
38. Verifikasi baris bernilai `—` berada di akhir (baris terakhir halaman 3 menampilkan Last Updated `—`)
39. Isi input halaman `1`, tekan Enter
40. Klik header Last Updated sekali lagi (Descending)
41. Verifikasi baris bernilai `—` berada di awal
42. Verifikasi tiga baris teratas Last Updated Descending (Newest First) `Fixture.hardwareStock.p16.a[10].sku`, `Fixture.hardwareStock.p16.a[12].sku`, `Fixture.hardwareStock.p16.a[14].sku`
43. Klik header Last Updated sekali lagi (Netral)
44. Verifikasi tiga baris teratas urutan default `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku`
45. Isi input halaman `3`, tekan Enter
46. Verifikasi baris bernilai `—` berada di paling bawah pada urutan default
47. Isi input halaman `1`, tekan Enter

### TC-AC-ACHS-258: Tie-break kolom Brand

48. Klik header Brand sekali (Ascending)
49. Isi input halaman `3`, tekan Enter
50. Verifikasi tiga baris Brand `Fixture.hardwareStock.p16.a[1].brand` berurutan mengikuti default sort (Last Updated terbaru dulu): `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`
51. Klik `Prev`, klik `Next`
52. Verifikasi urutan tiga baris Brand `Fixture.hardwareStock.p16.a[1].brand` identik dan tidak ada baris ganda atau terlewat di halaman 3
53. Klik header Brand dua kali sampai netral, isi input halaman `1`, tekan Enter


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi S-12 (keyword Search, #8): keyword `Zebra` (`Fixture.hardwareStock.p16.a[1].brand`) adalah nilai kolom Brand penuh yang sama persis dengan keyword literal TC (TC-AC-ACHS-204, 211, 249, 250, 258 menurut spec ini). Dicocokkan dengan Tabel A Pre-setup #16: kolom Brand bernilai `Zebra` hanya pada baris 1, 3, dan 4, dan tidak ada kolom searchable lain di baris lain yang memuat `Zebra`, sehingga himpunan hasil 3 baris sama dengan hasil keyword TC. Tidak ada perbedaan.
- Langkah 1 sampai 8 berulang untuk setiap baris tabel Data uji (sepuluh kolom; bagian 8b butir 7). TC-AC-ACHS-227 sampai 230 berbagi satu perulangan karena langkahnya identik dan hanya kolom yang berbeda.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengembalian sort ke netral dan halaman 1 (akhir tiap blok TC), pengosongan Search, penutupan overlay Column Visibility, serta navigasi halaman 3 dan 1 pada TC-AC-ACHS-257 dan 258 (S-14: asersi "di akhir" didahului pindah ke halaman terakhir).
- Spec memiliki 53 langkah nominal dan 125 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Sort Stock List pada akun dan dataset read-only yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari satu perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC-AC-ACHS-232 langkah 3 mengklik header kolom Photo, sedangkan Expected b menyebut klik header kolom Actions; spec melakukan keduanya dan hanya mengasersi Expected (urutan tidak berubah dan overlay terbuka setelah klik Actions).
  - TC-AC-ACHS-233 Expected b menulis urutan 3 baris hasil search `Fixture.hardwareStock.p16.a[3].modelType`, `Fixture.hardwareStock.p16.a[4].modelType`, `Fixture.hardwareStock.p16.a[1].modelType`, sedangkan sort SKU Ascending yang aktif menaruh `Fixture.hardwareStock.p16.a[4].sku` dan `Fixture.hardwareStock.p16.a[1].sku` sebelum `Fixture.hardwareStock.p16.a[3].sku`; spec mengasersi himpunan 3 baris tanpa urutan.
  - TC-AC-ACHS-257 menulis "klik sekali (Ascending) lalu dua kali (Descending)" tanpa halaman amatan untuk baris `—` dan tanpa asersi indikator; spec memakai halaman 1 dan halaman terakhir (halaman 3) dan tidak menambah asersi indikator.
  - TC-AC-ACHS-258 Expected b ("identik pada halaman berikutnya") ambigu karena ketiga baris `Fixture.hardwareStock.p16.a[1].brand` ada di halaman 3 pada 10 baris per halaman; spec mengasersi urutan identik setelah berpindah halaman bolak-balik.
