---
id: TC-AC-ACHS-E2E-226-pagination-dan-kombinasi-popup-event-log
title: "Pagination dan Kombinasi Empat Kontrol Popup Event Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-503
  - TC-AC-ACHS-504
  - TC-AC-ACHS-505
  - TC-AC-ACHS-506
  - TC-AC-ACHS-507
coverage:
  web: automated
---

# Pagination dan Kombinasi Empat Kontrol Popup Event Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Spec membuka Stock Detail dan popup Event Log sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #20 TC (Tabel B), SKU `Fixture.hardwareStock.p16.a[4].sku` (Handheld Reader - Long Range) memiliki 12 sesi Event Log pada Pre-setup (Tabel B baris #1 sampai #12); baris dikenali lewat kolom Date. Event Log adalah audit trail permanen dan spec lain dapat menambah sesi pada SKU ini, sehingga total tanpa filter tidak diasersi absolut (S-12): hook `before` membaca jumlah sesi sebagai `{nEventLog}` (baseline) lewat kemampuan baca dan footer tanpa filter membaca `Showing 1–10 of {nEventLog} entries`. Spec mensyaratkan `{nEventLog}` antara 11 dan 20 (dua halaman pada ukuran halaman 10, satu halaman pada ukuran 25); Pre-setup #20 menyediakan 12. Baris dirujuk lewat nomor baris Tabel B: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel B (`Fixture.hardwareStock.p20.b[n]`) pada urutan default (Date terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup.
- Asersi literal hasil Search/Filter (mis. `Showing 1–3 of 3 entries`) bergantung pada baseline Pre-setup #20 yang utuh: spec ini spec baca-saja (nomor di bawah 240) yang berjalan sebelum spec penulis ke SKU yang sama (243, 264, 267, 272 sampai 274, 277, dan seterusnya), dan Pre-setup #20 di-reseed sebelum run suite (`suite.md` bagian Urutan jalan dan Seeding ulang).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU Handheld Reader Long Range | #16 Tabel A baris 4 | kode SKU Handheld Reader - Long Range (RFD40); pemilik Event Log Pre-setup #20 | `Fixture.hardwareStock.p16.a[4].sku` |
  | Date baris #n (n = 1 sampai 12) | #20 Tabel B | identitas baris hasil; urutan default Date terbaru lebih dulu; format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p20.b[n].date` |
  | Activity baris #n (n = 1 sampai 12) | #20 Tabel B | Delete Stock pada #1, #5, #9; Add Stock pada baris lain (9 baris) | `Fixture.hardwareStock.p20.b[n].activity` |
  | Modified By baris #n (n = 1 sampai 12) | #20 Tabel B | nama singkat user: akun Pre-setup #1 pada #1, #4, #7, #10; user Distributor Pre-setup #11 pada #2, #5, #8, #11; user Distributor Pre-setup #10 pada #3, #6, #9, #12 | `Fixture.hardwareStock.p20.b[n].modifiedBy` |
  | Jumlah sesi Event Log SKU Handheld Reader Long Range (`nEventLog`) | #20 | baseline relatif: jumlah sesi yang dibaca hook `before` lewat kemampuan baca (disediakan tim FE/BE) sebelum aksi pertama; Pre-setup #20 menyediakan 12 sesi tetapi angka itu tidak diasersi | dibaca saat run |
  | Nama singkat akun user Distributor #10 | #10 | user Distributor; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman yang dipakai suite (lihat suite.md).
- State global: tidak ada yang diubah; sort, filter, dan ukuran halaman dipulihkan pada langkah 29 dan 46 sampai 49. Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `Fixture.hardwareStock.p16.a[4].sku`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
3. Klik Tab `Available`
4. Klik icon `[Event Log]` di toolbar

### TC-AC-ACHS-503: Default 10 baris, opsi 10/25/50/100, info jumlah

5. Verifikasi tabel menampilkan default 10 baris per halaman
6. Verifikasi info `Showing 1–10 of {nEventLog} entries`
7. Buka dropdown rows per page
8. Verifikasi opsi rows per page: 10, 25, 50, 100 (tanpa opsi All)
9. Tutup dropdown rows per page dengan `Esc`

### TC-AC-ACHS-504: Next/Prev, input nomor halaman, ganti page size kembali ke halaman 1

10. Klik `Next`
11. Verifikasi halaman 2 terbuka: `Showing 11–{nEventLog} of {nEventLog} entries`
12. Isi input halaman `1`, tekan Enter
13. Verifikasi kembali ke halaman 1: `Showing 1–10 of {nEventLog} entries`
14. Klik `Next`
15. Pilih rows per page 25
16. Verifikasi mengganti page size kembali ke halaman 1: `Showing 1–{nEventLog} of {nEventLog} entries`
17. Pilih rows per page 10

### TC-AC-ACHS-505: Input nomor halaman tidak valid diabaikan

18. Isi input halaman `0`, tekan Enter
19. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of {nEventLog} entries`
20. Isi input halaman `6` (melebihi halaman terakhir), tekan Enter
21. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of {nEventLog} entries`
22. Isi input halaman `abc`, tekan Enter
23. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of {nEventLog} entries`

### TC-AC-ACHS-506: Search kembali ke halaman 1, ganti sort tetap di halaman sekarang

24. Klik `Next`
25. Ketik Search `Delete`, tekan Enter
26. Verifikasi halaman kembali ke 1: `Showing 1–3 of 3 entries`
27. Klik header kolom Success sekali
28. Verifikasi nomor halaman tidak berubah: tetap halaman 1, `Showing 1–3 of 3 entries`
29. Klik header kolom Success dua kali sampai netral

### TC-AC-ACHS-507: Kombinasi empat kontrol Search + Filter + Sort + Pagination, recovery dari 0 hasil

30. Ganti isi kotak search dengan `Delete`, tekan Enter
31. Klik icon Filter
32. Isi Modified By = `Fixture.hardwareStock.account.p10.distributorCakra.shortName`, klik `[Apply]`
33. Klik header kolom Date sekali (Ascending)
34. Pilih rows per page 25
35. Verifikasi Search berlaku: keyword `Delete` tetap terisi
36. Verifikasi Filter berlaku: badge titik tampil pada ikon Filter
37. Verifikasi Sort berlaku: indikator Ascending pada Date
38. Verifikasi Pagination berlaku: rows per page 25
39. Ganti isi kotak search dengan `zzqx-tidak-ada`, tekan Enter
40. Verifikasi kombinasi tanpa hasil menampilkan `No results found`
41. Kosongkan isi kotak search, tekan Enter
42. Verifikasi baris sesuai Filter, 4 baris: #3, #6, #9, #12
43. Verifikasi Sort masih aktif: indikator Ascending pada Date
44. Verifikasi page size masih aktif: rows per page 25
45. Verifikasi Filter masih aktif: badge titik tampil pada ikon Filter
46. Klik `[Clear Field]`, lalu klik `[Apply]`
47. Klik header kolom Date dua kali sampai netral
48. Pilih rows per page 10
49. Klik icon `(←)`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-503 sampai 507). Tidak ada TC hanya-BE di spec ini.
- Langkah 2 sampai 4 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Langkah penghubung (bukan dari langkah TC): langkah 1 (Search SKU untuk menemukan baris SKU sebelum row action `Detail`, R-16 dan S-03), langkah 3 (`Klik Tab Available`, dari langkah TC "Pastikan Tab Available aktif"), langkah 9 (menutup dropdown), langkah 17 (mengembalikan ukuran halaman 10), langkah 24 (membuka halaman 2 sebagai precondition TC-506), langkah 29 dan 46 sampai 49 (memulihkan sort, filter, ukuran halaman, dan kotak Search, S-09). Langkah 30 mengganti isi kotak Search yang masih berisi `Delete` dari TC-506.
- Spec ini di atas 35 langkah (49 langkah nominal). Alasan: lima TC memakai satu footer pagination dan satu dataset read-only (Event Log satu SKU), tiap TC berdiri sendiri karena sort, filter, dan ukuran halaman dipulihkan di antaranya, dan topik Pagination satu dataset digabung sesuai prinsip 1.
- Total Event Log (S-12): angka 12 adalah Pre-setup #20 dan spec tidak mengasersi angka absolut; `{nEventLog}` dibaca hook `before` sebelum aksi pertama dan asersi pagination/footer tanpa filter diturunkan darinya. Footer hasil Search/Filter yang menyaring (mis. `Showing 1–3 of 3 entries`) tetap literal karena spec baca-saja ini berjalan di baseline Pre-setup #20 yang utuh (urutan jalan dan reseed di `suite.md`), bukan karena data tidak bisa berubah. Risiko: bila urutan jalan tidak dijaga atau reseed dilewati, spec penulis ke SKU yang sama (mis. 264) dapat menambah baris `Add Stock`/`Delete Stock` dan asersi literal ini gagal. TC-466, 472, dan 475 menulis angka literal (Temuan sumber, tidak diubah di spec ini).
- Asersi tambahan di luar TC (S-03): footer hasil filter literal `Showing 1–3 of 3 entries` pada langkah 26 dan 28 tidak diminta TC-506 (Expected TC hanya "halaman kembali ke 1" dan nomor halaman tidak berubah). Footer itu ditulis literal karena baseline Pre-setup #20 utuh (urutan jalan suite.md), sedangkan total tanpa filter tetap relatif `{nEventLog}`.
- Temuan untuk QA:
  - TC-506 langkah 5 dan 7 ("Kembali ke halaman 2 jika ada") bersifat bersyarat; Search `Delete` menghasilkan 3 baris sehingga halaman 2 tidak ada. Spec mengamati sort di halaman 1 (tetap halaman 1) dan tidak menulis langkah bersyarat. Judul TC menyebut Apply Filter kembali ke halaman 1 tetapi langkah dan Expected hanya memuat Search.
  - TC-504 langkah 7 ("klik Next jika ada halaman berikutnya") bersifat bersyarat dan pada ukuran halaman 25 tidak ada halaman berikutnya; spec menjalankan Next pada ukuran halaman 10 (langkah 14) lalu mengganti ukuran halaman ke 25 untuk mengamati kembali ke halaman 1. Langkah 8 TC ("pada halaman 2 ganti rows per page ke 10") tidak dapat dijalankan sesudah ukuran 25; spec memakai urutan yang bermakna.
  - TC-507 tidak menyebut Filter, Sort, dan page size yang dipakai; spec memilih Modified By = `Fixture.hardwareStock.account.p10.distributorCakra.shortName`, sort Date Ascending, dan 25 baris per halaman. Baris hasil pemulihan (4 baris) berasal dari Expected TC-475.
  - Nilai `6` pada TC-505 mengasumsikan 2 halaman (`{nEventLog}` antara 11 dan 20, 10 baris per halaman).
  - Populasi Pre-setup #20 dirujuk lewat nomor baris Tabel B (`#n` = `Fixture.hardwareStock.p20.b[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nilai literal Pre-setup di spec dan tanpa pengecualian S-12. Angka 12 sesi adalah populasi Pre-setup #20 dan tidak diasersi absolut: total tanpa filter memakai baseline relatif `{nEventLog}` (S-12, keputusan 2026-11-02). Literal yang tetap ada adalah teks UI nyata (placeholder, `Add Stock`, `Delete Stock`, `Delete`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
