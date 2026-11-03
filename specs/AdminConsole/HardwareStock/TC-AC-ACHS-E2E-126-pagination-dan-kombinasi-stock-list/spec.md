---
id: TC-AC-ACHS-E2E-126-pagination-dan-kombinasi-stock-list
title: "Pagination Stock List: Default, Navigasi, Input Halaman, Reset ke Halaman 1, Batas 25 Baris, dan Kombinasi Empat Kontrol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-246
  - TC-AC-ACHS-247
  - TC-AC-ACHS-248
  - TC-AC-ACHS-249
  - TC-AC-ACHS-250
  - TC-AC-ACHS-260
coverage:
  web: automated
---

# Pagination Stock List: Default, Navigasi, Input Halaman, Reset ke Halaman 1, Batas 25 Baris, dan Kombinasi Empat Kontrol

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
  | SKU baris 1 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p16.a[1].sku` |
  | SKU baris 2 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available | `Fixture.hardwareStock.p16.a[2].sku` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | SKU baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].sku` |
  | SKU baris padding 22 (Tabel A baris 30) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 22 (#16) | `Fixture.hardwareStock.p16.a[30].sku` |
  | Nilai turunan searchSkuPad | turunan dari `Fixture.hardwareStock.p16.a[9].sku` | keyword Search: awalan kode SKU seluruh baris padding tanpa nomor (`SKU-PAD-`; 22 baris) | `Fixture.hardwareStock.derived.searchSkuPad` |
- Data uji TC-AC-ACHS-248 (input nomor halaman tidak valid pada halaman 1 dari 3 halaman):

  | No | Input | Keterangan |
  |---|---|---|
  | 1 | `0` | nol |
  | 2 | `8` | melebihi halaman terakhir (halaman terakhir adalah 3) |
  | 3 | `abc` | bukan angka |

- Pilihan spec: TC-AC-ACHS-249 memakai keyword Search `Fixture.hardwareStock.derived.searchSkuPad` (22 baris, 3 halaman pada 10 baris per halaman) karena keyword `Fixture.hardwareStock.p16.a[1].brand` dari TC hanya menghasilkan 3 baris sehingga halaman 2 tidak ada; TC-AC-ACHS-250 memakai Filter Type = `Handheld Reader`, sort Total Registered Ascending, dan rows per page 25 (TC menulis "satu Filter" dan "header sort" tanpa nilai).
- State global yang diubah: tidak ada yang bertahan; Search dan sort dipulihkan ke netral pada akhir tiap TC.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-246: Default dan opsi rows per page

1. Verifikasi tabel menampilkan 10 baris per halaman
2. Verifikasi info `Showing 1–10 of 30 entries`
3. Buka dropdown rows per page
4. Verifikasi opsi rows per page 10, 25, 50, 100 (tanpa opsi All)
5. Tutup dropdown rows per page

### TC-AC-ACHS-247: Next, input nomor halaman, dan ganti page size

6. Klik `Next`
7. Verifikasi info `Showing 11–20 of 30 entries`
8. Isi input halaman `1`, tekan Enter
9. Verifikasi info `Showing 1–10 of 30 entries`
10. Klik `Next`
11. Pilih rows per page 25
12. Verifikasi tabel kembali ke halaman 1 (info `Showing 1–25 of 30 entries`)
13. Klik `Next`
14. Pilih rows per page 10
15. Verifikasi tabel kembali ke halaman 1 (info `Showing 1–10 of 30 entries`)

### TC-AC-ACHS-248: Input nomor halaman tidak valid diabaikan

16. Untuk setiap baris tabel Data uji TC-AC-ACHS-248 (langkah 16 sampai 17): isi input halaman dengan nilai, tekan Enter
17. Verifikasi tabel tetap di halaman sekarang (info `Showing 1–10 of 30 entries`)

### TC-AC-ACHS-249: Search kembali ke halaman 1, ganti sort tetap di halaman sekarang

18. Klik `Next`
19. Ketik Search `Fixture.hardwareStock.derived.searchSkuPad`, tekan Enter
20. Verifikasi tabel kembali ke halaman 1 (info `Showing 1–10 of 22 entries`)
21. Klik `Next`
22. Klik header Total Registered sekali
23. Verifikasi nomor halaman tidak berubah (info `Showing 11–20 of 22 entries`)
24. Klik header Total Registered dua kali sampai netral, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-250: Kombinasi empat kontrol dan recovery dari 0 hasil

25. Ketik Search `Fixture.hardwareStock.p16.a[1].brand`, tekan Enter
26. Klik icon Filter, isi Type = `Handheld Reader`, klik `[Apply]`
27. Klik header Total Registered sekali (Ascending)
28. Pilih rows per page 25
29. Verifikasi keyword `Fixture.hardwareStock.p16.a[1].brand` tetap terisi di kotak Search
30. Verifikasi badge titik tampil pada ikon Filter
31. Verifikasi indikator sort Ascending aktif pada Total Registered
32. Verifikasi rows per page 25 terpilih
33. Verifikasi tabel menampilkan irisan Search dan Filter: 2 baris `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`
34. Ganti isi kotak search dengan `zzqx-tidak-ada`, tekan Enter
35. Verifikasi tampil `No results found`
36. Klik `✕` pada Search, tekan Enter
37. Verifikasi tabel hanya memuat baris bertipe `Handheld Reader` (3 baris urut Total Registered Ascending: `Fixture.hardwareStock.p16.a[2].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`)
38. Verifikasi indikator sort Ascending tetap aktif pada Total Registered
39. Verifikasi rows per page 25 tetap terpilih
40. Klik `[Clear Field]`, klik `[Apply]`, klik icon Filter untuk menutup panel, klik header Total Registered dua kali sampai netral, pilih rows per page 10

### TC-AC-ACHS-260: 25 baris per halaman dan halaman kedua berisi 5 baris

41. Pilih rows per page 25
42. Verifikasi halaman 1 `Showing 1–25 of 30 entries`
43. Klik `Next`
44. Verifikasi halaman 2 `Showing 26–30 of 30 entries`
45. Verifikasi halaman 2 berisi 5 baris
46. Pilih rows per page 50
47. Verifikasi tabel menampilkan 30 baris pada satu halaman
48. Verifikasi tombol `Next` tidak aktif
49. Pilih rows per page 10


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi S-12 (keyword Search, #8): keyword `Zebra` (`Fixture.hardwareStock.p16.a[1].brand`) adalah nilai kolom Brand penuh yang sama persis dengan keyword literal TC (TC-AC-ACHS-204, 211, 249, 250, 258 menurut spec ini). Dicocokkan dengan Tabel A Pre-setup #16: kolom Brand bernilai `Zebra` hanya pada baris 1, 3, dan 4, dan tidak ada kolom searchable lain di baris lain yang memuat `Zebra`, sehingga himpunan hasil 3 baris sama dengan hasil keyword TC. Tidak ada perbedaan.
- Langkah 16 sampai 17 berulang untuk setiap baris tabel Data uji (tiga iterasi; bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): pemulihan rows per page 10, sort netral, pengosongan Search, `[Clear Field]` dan `[Apply]`, serta penutupan panel Filter. Klik menu sidebar tidak dipakai di antara TC sehingga rows per page dipulihkan eksplisit.
- Spec memiliki 49 langkah nominal dan 53 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Pagination Stock List pada akun dan dataset read-only yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari satu perulangan input tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC-AC-ACHS-247 langkah 4 menulis "klik Next jika ada halaman berikutnya" dan langkah 5 "pada halaman 2 ganti rows per page ke 10": pada 25 baris per halaman halaman 2 ada (30 baris); spec menulis Next tanpa syarat dan menguji ganti page size dari halaman 2.
  - TC-AC-ACHS-249 judul menyebut "Search dan Apply Filter kembali ke halaman 1" tetapi langkah dan Expected hanya menguji Search; keyword TC `Fixture.hardwareStock.p16.a[1].brand` hanya 3 baris sehingga halaman 2 tidak ada; spec memakai `Fixture.hardwareStock.derived.searchSkuPad` (22 baris). Angka 22 diturunkan dari Pre-setup #16 (22 SKU `{sku_pad_NN}`).
  - TC-AC-ACHS-250 tidak menyebut nilai Filter dan kolom sort; spec memilih Type = `Handheld Reader` dan Total Registered (pilihan spec). Baris hasil `Fixture.hardwareStock.p16.a[4].sku` dan `Fixture.hardwareStock.p16.a[1].sku` diturunkan dari Tabel A (`Fixture.hardwareStock.p16.a[1].brand` bertipe Handheld Reader).
