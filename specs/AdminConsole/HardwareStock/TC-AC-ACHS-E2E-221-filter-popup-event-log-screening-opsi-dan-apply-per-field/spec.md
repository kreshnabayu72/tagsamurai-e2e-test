---
id: TC-AC-ACHS-E2E-221-filter-popup-event-log-screening-opsi-dan-apply-per-field
title: "Filter Popup Event Log: Screening, Opsi, dan Apply per Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-473
  - TC-AC-ACHS-474
  - TC-AC-ACHS-475
  - TC-AC-ACHS-476
coverage:
  web: automated
---

# Filter Popup Event Log: Screening, Opsi, dan Apply per Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Spec membuka Stock Detail dan popup Event Log sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #20 TC (Tabel B), SKU `Fixture.hardwareStock.p16.a[4].sku` (Handheld Reader - Long Range) memiliki 12 sesi Event Log pada Pre-setup (Tabel B baris #1 sampai #12); baris dikenali lewat kolom Date. Event Log adalah audit trail permanen dan spec lain dapat menambah sesi pada SKU ini, sehingga total tanpa filter tidak diasersi absolut (S-12): hook `before` membaca jumlah sesi sebagai `{nEventLog}` (baseline) lewat kemampuan baca dan footer tanpa filter membaca `Showing 1–10 of {nEventLog} entries`. Baris dirujuk lewat nomor baris Tabel B: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel B (`Fixture.hardwareStock.p20.b[n]`) pada urutan default (Date terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup.
- Asersi literal hasil Search/Filter (mis. "3 baris: #1, #5, #9") bergantung pada baseline Pre-setup #20 yang utuh: spec ini spec baca-saja (nomor di bawah 240) yang berjalan sebelum spec penulis ke SKU yang sama (243, 264, 267, 272 sampai 274, 277, dan seterusnya), dan Pre-setup #20 di-reseed sebelum run suite (`suite.md` bagian Urutan jalan dan Seeding ulang).
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
  | Nama singkat akun user Distributor #10 | #10 | user Distributor; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
  | Nama singkat akun user Distributor #11 | #11 | user Distributor; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |
  | Keyword pencarian internal dropdown Modified By | #10 dan #20 Tabel B | diturunkan dari `Fixture.hardwareStock.account.p10.distributorCakra.shortName`: tiga huruf pertama nama depan; cocok hanya dengan opsi user Distributor #10 | `Fixture.hardwareStock.derived.firstThreeLettersDistributorCakra` |
- Format tanggal dan jam General Settings: bawaan yang tampil pada Pre-setup (nilai Date dibaca dari fixture Pre-setup); spec tidak mengubahnya.
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman yang dipakai suite (lihat suite.md).
- State global: tidak ada yang diubah. Suite serial: `parallel: false` (lihat suite.md).
- Parameter Opsi (langkah 15 sampai 18):

| No | Field | Placeholder | Opsi |
|---|---|---|---|
| 1 | Activity | `All activities` | `Add Stock`, `Delete Stock` (2 opsi) |
| 2 | Modified By | `All users` | `Fixture.hardwareStock.account.p10.distributorCakra.shortName`, `Fixture.hardwareStock.account.p11.distributorMitra.shortName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` (3 opsi) |

- Parameter Apply (langkah 28 sampai 33). Kolom Hasil memuat nilai kolom Date baris hasil:

| No | Field | Nilai | Hasil |
|---|---|---|---|
| 1 | Activity | `Delete Stock` | 3 baris: #1, #5, #9 |
| 2 | Modified By | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` | 4 baris: #3, #6, #9, #12 |

## Test Steps

1. Ketik Search `Fixture.hardwareStock.p16.a[4].sku`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
3. Klik Tab `Available`
4. Klik icon `[Event Log]` di toolbar

### TC-AC-ACHS-473: Screening Filter Panel

5. Hover icon Filter
6. Verifikasi tooltip `Filter`
7. Klik icon Filter
8. Verifikasi ikon Filter menjadi gelap saat panel terbuka
9. Verifikasi field pertama: Date (date range picker, placeholder `Select date`)
10. Verifikasi field kedua: Activity (multi-select searchable, placeholder `All activities`)
11. Verifikasi field ketiga: Modified By (multi-select searchable, placeholder `All users`)
12. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
13. Verifikasi tidak ada field Photo maupun identifier teks

### TC-AC-ACHS-474: Screening isi opsi dropdown Filter kelas multi

14. Untuk setiap baris tabel Parameter Opsi (2 baris), lakukan langkah 15 sampai 18
15. Buka dropdown field baris tersebut
16. Verifikasi opsi sesuai kolom Opsi baris tersebut dan bersumber DISTINCT dari baris tabel
17. Verifikasi kotak pencarian internal ada
18. Tutup dropdown field baris tersebut
19. Buka dropdown Modified By
20. Ketik `Fixture.hardwareStock.derived.firstThreeLettersDistributorCakra` pada kotak pencarian internal
21. Verifikasi daftar menyempit hanya memuat opsi yang mengandung `Fixture.hardwareStock.derived.firstThreeLettersDistributorCakra`: `Fixture.hardwareStock.account.p10.distributorCakra.shortName`
22. Ganti isi kotak pencarian internal dengan `Fixture.hardwareStock.derived.firstThreeLettersDistributorCakra` huruf kecil
23. Verifikasi daftar opsi identik dengan hasil pada langkah 21 (case-insensitive)
24. Ganti isi kotak pencarian internal dengan `zzqx-tidak-ada`
25. Verifikasi teks `No results found`
26. Tutup dropdown Modified By

### TC-AC-ACHS-475: Filter kelas multi, Apply per field

27. Untuk setiap baris tabel Parameter Apply (2 baris), lakukan langkah 28 sampai 33
28. Isi field baris tersebut dengan nilai baris tersebut
29. Klik `[Apply]`
30. Verifikasi tabel sesuai kolom Hasil baris tersebut
31. Klik `[Clear Field]`
32. Klik `[Apply]`
33. Verifikasi tabel kembali ke seluruh baris: footer `Showing 1–10 of {nEventLog} entries`

### TC-AC-ACHS-476: Filter kelas date, Apply per field

34. Isi field Date dengan rentang Start = tanggal Date #10, End = tanggal Date #6 (Start ≠ End)
35. Klik `[Apply]`
36. Verifikasi tabel menampilkan 5 baris: #6, #7, #8, #9, #10
37. Klik `[Clear Field]`
38. Klik `[Apply]`
39. Verifikasi tabel kembali ke seluruh baris: footer `Showing 1–10 of {nEventLog} entries`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-473 sampai 476). Tidak ada TC hanya-BE di spec ini.
- Langkah 2 sampai 4 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Langkah penghubung (bukan dari langkah TC): langkah 1 (Search SKU untuk menemukan baris SKU sebelum row action `Detail`, R-16 dan S-03), langkah 3 (`Klik Tab Available`, dari langkah TC "Pastikan Tab Available aktif"), langkah 18 dan 26 (menutup dropdown). Loop langkah 14: langkah 15 sampai 18 diulang untuk setiap baris tabel Parameter Opsi (2 baris, 2 kali). Loop langkah 27: langkah 28 sampai 33 diulang untuk setiap baris tabel Parameter Apply (2 baris, 2 kali). Langkah 19 sampai 25 mengamati pencarian internal dropdown pada Modified By, field dengan opsi terbanyak. Filter Panel tetap terbuka sesudah `[Apply]` (ditunjukkan TC-AC-ACHS-484, panel ditutup dengan klik icon Filter).
- Spec ini di atas 35 langkah (39 langkah nominal). Alasan: seluruh blok memakai satu Filter Panel dan satu dataset read-only (Event Log satu SKU), tiap iterasi berdiri sendiri dan diakhiri `[Clear Field]` dan `[Apply]`, dan topik Filter satu dataset digabung sesuai prinsip 1.
- Konfirmasi (#8): kata kunci dropdown diturunkan dari tiga huruf pertama nama depan user Distributor Pre-setup #10 (sesuai TC-474 langkah 7, "3 huruf pertama salah satu opsi"), bukan nilai kolom penuh; pada tiga opsi Modified By Tabel B hanya opsi user #10 yang memuatnya (substring, case-insensitive). Tidak ada perbedaan.
- Total Event Log (S-12): angka 12 adalah Pre-setup #20 dan spec tidak mengasersi angka absolut; `{nEventLog}` dibaca hook `before` sebelum aksi pertama dan asersi pagination/footer tanpa filter diturunkan darinya. Hasil Filter yang menyaring (mis. "3 baris: #1, #5, #9") tetap literal karena spec baca-saja ini berjalan di baseline Pre-setup #20 yang utuh (urutan jalan dan reseed di `suite.md`), bukan karena data tidak bisa berubah. Risiko: bila urutan jalan tidak dijaga atau reseed dilewati, spec penulis ke SKU yang sama (mis. 264) dapat menambah baris `Add Stock`/`Delete Stock` dan asersi literal ini gagal. TC-466, 472, dan 475 menulis angka literal (Temuan sumber, tidak diubah di spec ini).
- Temuan untuk QA:
  - TC-474 langkah 7 ("Ketik 3 huruf pertama salah satu opsi") tidak menyebut field; spec memakai Modified By dengan `Fixture.hardwareStock.derived.firstThreeLettersDistributorCakra`. Expected f (keyword tanpa kecocokan menampilkan `No results found`) tidak punya langkah di TC; spec menambah keyword `zzqx-tidak-ada` (S-03).
  - TC-476 tidak menyebut cara memilih rentang di date range picker; spec menulis "isi field dengan rentang" tanpa mengarang interaksi picker.
  - Populasi Pre-setup #20 dirujuk lewat nomor baris Tabel B (`#n` = `Fixture.hardwareStock.p20.b[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nilai literal Pre-setup di spec dan tanpa pengecualian S-12. Angka 12 sesi adalah populasi Pre-setup #20 dan tidak diasersi absolut: total tanpa filter memakai baseline relatif `{nEventLog}` (S-12, keputusan 2026-11-02). Literal yang tetap ada adalah teks UI nyata (placeholder, `Add Stock`, `Delete Stock`, `Delete`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
