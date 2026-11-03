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
- State global: tidak ada yang diubah; sort, filter, dan ukuran halaman dipulihkan pada langkah 28 dan 45 sampai 48. Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Klik Tab `Available`
3. Klik icon `[Event Log]` di toolbar

### TC-AC-ACHS-503: Default 10 baris, opsi 10/25/50/100, info jumlah

4. Verifikasi tabel menampilkan default 10 baris per halaman
5. Verifikasi info `Showing 1–10 of {nEventLog} entries`
6. Buka dropdown rows per page
7. Verifikasi opsi rows per page: 10, 25, 50, 100 (tanpa opsi All)
8. Tutup dropdown rows per page dengan `Esc`

### TC-AC-ACHS-504: Next/Prev, input nomor halaman, ganti page size kembali ke halaman 1

9. Klik `Next`
10. Verifikasi halaman 2 terbuka: `Showing 11–{nEventLog} of {nEventLog} entries`
11. Isi input halaman `1`, tekan Enter
12. Verifikasi kembali ke halaman 1: `Showing 1–10 of {nEventLog} entries`
13. Klik `Next`
14. Pilih rows per page 25
15. Verifikasi mengganti page size kembali ke halaman 1: `Showing 1–{nEventLog} of {nEventLog} entries`
16. Pilih rows per page 10

### TC-AC-ACHS-505: Input nomor halaman tidak valid diabaikan

17. Isi input halaman `0`, tekan Enter
18. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of {nEventLog} entries`
19. Isi input halaman `6` (melebihi halaman terakhir), tekan Enter
20. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of {nEventLog} entries`
21. Isi input halaman `abc`, tekan Enter
22. Verifikasi tabel tetap di halaman 1: `Showing 1–10 of {nEventLog} entries`

### TC-AC-ACHS-506: Search kembali ke halaman 1, ganti sort tetap di halaman sekarang

23. Klik `Next`
24. Ketik Search `Delete`, tekan Enter
25. Verifikasi halaman kembali ke 1: `Showing 1–3 of 3 entries`
26. Klik header kolom Success sekali
27. Verifikasi nomor halaman tidak berubah: tetap halaman 1, `Showing 1–3 of 3 entries`
28. Klik header kolom Success dua kali sampai netral

### TC-AC-ACHS-507: Kombinasi empat kontrol Search + Filter + Sort + Pagination, recovery dari 0 hasil

29. Ganti isi kotak search dengan `Delete`, tekan Enter
30. Klik icon Filter
31. Isi Modified By = `Fixture.hardwareStock.account.p10.distributorCakra.shortName`, klik `[Apply]`
32. Klik header kolom Date sekali (Ascending)
33. Pilih rows per page 25
34. Verifikasi Search berlaku: keyword `Delete` tetap terisi
35. Verifikasi Filter berlaku: badge titik tampil pada ikon Filter
36. Verifikasi Sort berlaku: indikator Ascending pada Date
37. Verifikasi Pagination berlaku: rows per page 25
38. Ganti isi kotak search dengan `zzqx-tidak-ada`, tekan Enter
39. Verifikasi kombinasi tanpa hasil menampilkan `No results found`
40. Kosongkan isi kotak search, tekan Enter
41. Verifikasi baris sesuai Filter, 4 baris: #3, #6, #9, #12
42. Verifikasi Sort masih aktif: indikator Ascending pada Date
43. Verifikasi page size masih aktif: rows per page 25
44. Verifikasi Filter masih aktif: badge titik tampil pada ikon Filter
45. Klik `[Clear Field]`, lalu klik `[Apply]`
46. Klik header kolom Date dua kali sampai netral
47. Pilih rows per page 10
48. Klik icon `(←)`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-503 sampai 507). Tidak ada TC hanya-BE di spec ini.
- Langkah 1 sampai 3 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Langkah penghubung (bukan dari langkah TC): langkah 2 (`Klik Tab Available`, dari langkah TC "Pastikan Tab Available aktif"), langkah 8 (menutup dropdown), langkah 16 (mengembalikan ukuran halaman 10), langkah 23 (membuka halaman 2 sebagai precondition TC-506), langkah 28 dan 45 sampai 48 (memulihkan sort, filter, ukuran halaman, dan kotak Search, S-09). Langkah 29 mengganti isi kotak Search yang masih berisi `Delete` dari TC-506.
- Spec ini di atas 35 langkah (48 langkah nominal). Alasan: lima TC memakai satu footer pagination dan satu dataset read-only (Event Log satu SKU), tiap TC berdiri sendiri karena sort, filter, dan ukuran halaman dipulihkan di antaranya, dan topik Pagination satu dataset digabung sesuai prinsip 1.
- Total Event Log (S-12): angka 12 adalah Pre-setup #20 dan spec tidak mengasersi angka absolut; `{nEventLog}` dibaca hook `before` sebelum aksi pertama dan asersi pagination/footer tanpa filter diturunkan darinya. Footer hasil Search/Filter yang menyaring (mis. `Showing 1–3 of 3 entries`) tetap literal karena hasil filter deterministik dari Tabel B.
- Temuan untuk QA:
  - TC-506 langkah 5 dan 7 ("Kembali ke halaman 2 jika ada") bersifat bersyarat; Search `Delete` menghasilkan 3 baris sehingga halaman 2 tidak ada. Spec mengamati sort di halaman 1 (tetap halaman 1) dan tidak menulis langkah bersyarat. Judul TC menyebut Apply Filter kembali ke halaman 1 tetapi langkah dan Expected hanya memuat Search.
  - TC-504 langkah 7 ("klik Next jika ada halaman berikutnya") bersifat bersyarat dan pada ukuran halaman 25 tidak ada halaman berikutnya; spec menjalankan Next pada ukuran halaman 10 (langkah 13) lalu mengganti ukuran halaman ke 25 untuk mengamati kembali ke halaman 1. Langkah 8 TC ("pada halaman 2 ganti rows per page ke 10") tidak dapat dijalankan sesudah ukuran 25; spec memakai urutan yang bermakna.
  - TC-507 tidak menyebut Filter, Sort, dan page size yang dipakai; spec memilih Modified By = `Fixture.hardwareStock.account.p10.distributorCakra.shortName`, sort Date Ascending, dan 25 baris per halaman. Baris hasil pemulihan (4 baris) berasal dari Expected TC-475.
  - Nilai `6` pada TC-505 mengasumsikan 2 halaman (`{nEventLog}` antara 11 dan 20, 10 baris per halaman).
  - Populasi Pre-setup #20 dirujuk lewat nomor baris Tabel B (`#n` = `Fixture.hardwareStock.p20.b[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nilai literal Pre-setup di spec dan tanpa pengecualian S-12. Angka 12 sesi adalah populasi Pre-setup #20 dan tidak diasersi absolut: total tanpa filter memakai baseline relatif `{nEventLog}` (S-12, keputusan 2026-11-02). Literal yang tetap ada adalah teks UI nyata (placeholder, `Add Stock`, `Delete Stock`, `Delete`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
