---
id: TC-AC-ACHS-E2E-133-sort-tab-available
title: "Sort Stock Detail Tab Available: Siklus 3-State Semua Kolom, Urutan Default, Kolom Non-Sortable, dan Search Tidak Direset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-285
  - TC-AC-ACHS-286
  - TC-AC-ACHS-287
  - TC-AC-ACHS-288
  - TC-AC-ACHS-289
  - TC-AC-ACHS-290
  - TC-AC-ACHS-291
  - TC-AC-ACHS-292
coverage:
  web: automated
---

# Sort Stock Detail Tab Available: Siklus 3-State Semua Kolom, Urutan Default, Kolom Non-Sortable, dan Search Tidak Direset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List; flag halaman Stock Detail disetel dengan cara yang sama (disediakan tim FE; lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): SKU `Fixture.hardwareStock.p16.a[4].sku` (Long Range) dengan 18 unit Available dan 1 unit Waiting for Approval (#17, Tabel E: `Fixture.hardwareStock.p17.e[10].deviceName` sampai `Fixture.hardwareStock.p17.e[28].deviceName`; Tab Available 19 baris) dan General Settings #15 (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | Device Name unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 10, Tabel E (#17) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | Device Name unit 11 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 11, Tabel E (#17) | `Fixture.hardwareStock.p17.e[11].deviceName` |
  | Device Name unit 12 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 12, Tabel E (#17) | `Fixture.hardwareStock.p17.e[12].deviceName` |
  | Device Name unit 17 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 17, Tabel E (#17) | `Fixture.hardwareStock.p17.e[17].deviceName` |
  | Device Name unit 18 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 18, Tabel E (#17) | `Fixture.hardwareStock.p17.e[18].deviceName` |
  | Device Name unit 19 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 19, Tabel E (#17) | `Fixture.hardwareStock.p17.e[19].deviceName` |
  | Device Name unit 20 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 20, Tabel E (#17) | `Fixture.hardwareStock.p17.e[20].deviceName` |
  | Device Name unit 21 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 21, Tabel E (#17) | `Fixture.hardwareStock.p17.e[21].deviceName` |
  | Device Name unit 23 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 23, Tabel E (#17) | `Fixture.hardwareStock.p17.e[23].deviceName` |
  | Device Name unit 24 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 24, Tabel E (#17) | `Fixture.hardwareStock.p17.e[24].deviceName` |
  | Device Name unit 25 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 25, Tabel E (#17) | `Fixture.hardwareStock.p17.e[25].deviceName` |
  | Device Name unit 26 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 26, Tabel E (#17) | `Fixture.hardwareStock.p17.e[26].deviceName` |
  | Device Name unit 27 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 27, Tabel E (#17) | `Fixture.hardwareStock.p17.e[27].deviceName` |
  | Device Name unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | Nilai turunan searchDeviceNameU20 | turunan dari `Fixture.hardwareStock.p17.e[20].deviceName` | keyword Search: bagian Device Name unit 20 Tabel E yang juga cocok dengan unit 21 sampai 28 (`Scanner - 2`; 9 baris; sama dengan keyword TC-AC-ACHS-263) | `Fixture.hardwareStock.derived.searchDeviceNameU20` |
- Urutan default (netral, Registered At Newest First): tiga baris teratas `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`.
- Data uji TC-AC-ACHS-285 sampai TC-AC-ACHS-289 (siklus 3-state; klik #3 setiap kolom kembali netral dengan tiga baris teratas urutan default; kelas kolom: 285 teks, 286 badge, 287 tanggal, 288 pengguna, 289 angka). Untuk Min Power dan Max Power seluruh unit bernilai sama (`-20 dBm` dan `30 dBm`) sehingga urutan Ascending dan Descending mengikuti urutan default:

  | No | TC | Kolom | Tiga teratas Ascending (`↑`) | Tiga teratas Descending (`↓`) |
  |---|---|---|---|---|
  | 1 | 285 | Device Name | `Fixture.hardwareStock.p17.e[10].deviceName`, `Fixture.hardwareStock.p17.e[11].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName` | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName` |
  | 2 | 285 | Serial Number | `Fixture.hardwareStock.p17.e[10].deviceName`, `Fixture.hardwareStock.p17.e[11].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName` | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName` |
  | 3 | 286 | Status | `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName` | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName` |
  | 4 | 287 | Registered At | `Fixture.hardwareStock.p17.e[10].deviceName`, `Fixture.hardwareStock.p17.e[11].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName` | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName` |
  | 5 | 288 | Registered By | `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName` | `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[23].deviceName`, `Fixture.hardwareStock.p17.e[20].deviceName` |
  | 6 | 289 | Min Power | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName` | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName` |
  | 7 | 289 | Max Power | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName` | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName` |
  | 8 | 289 | Current Power | `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[18].deviceName`, `Fixture.hardwareStock.p17.e[19].deviceName` | `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[17].deviceName` |

- State global yang diubah: indikator sort dan Search dipulihkan ke netral pada akhir tiap TC. Preferensi kolom tidak diubah.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab Available aktif

### TC-AC-ACHS-285 sampai 289: Siklus 3-state per kolom

3. Untuk setiap baris tabel Data uji TC-AC-ACHS-285 sampai 289 (langkah 3 sampai 10): klik header kolom sekali
4. Verifikasi indikator Ascending (`↑`) aktif pada kolom
5. Verifikasi tiga baris teratas sesuai kolom "Ascending"
6. Klik header kolom lagi
7. Verifikasi indikator Descending (`↓`) aktif pada kolom
8. Verifikasi tiga baris teratas sesuai kolom "Descending"
9. Klik header kolom sekali lagi
10. Verifikasi kolom kembali netral dengan urutan default (tiga baris teratas `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`)

### TC-AC-ACHS-290: Urutan default

11. Verifikasi urutan default: lima baris teratas `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`
12. Klik header Registered At tiga kali sampai netral
13. Verifikasi urutan sama dengan urutan default (lima baris teratas sama)

### TC-AC-ACHS-291: Kolom Actions non-sortable

14. Verifikasi kolom Actions tidak punya ikon sort
15. Klik header kolom Actions `(⋯)`
16. Verifikasi urutan baris tidak berubah (lima baris teratas urutan default)
17. Verifikasi overlay `Column Visibility` terbuka
18. Tutup overlay Column Visibility

### TC-AC-ACHS-292: Sort tidak mereset Search dan Filter saat ganti kolom

19. Ketik Search `Fixture.hardwareStock.derived.searchDeviceNameU20`, tekan Enter
20. Klik header Registered At (Ascending)
21. Klik header Serial Number (Ascending)
22. Verifikasi keyword `Fixture.hardwareStock.derived.searchDeviceNameU20` tetap terisi di kotak Search
23. Verifikasi tabel hanya berisi hasil search: 9 baris
24. Verifikasi indikator Registered At kembali netral
25. Verifikasi indikator Serial Number Ascending aktif
26. Klik header Serial Number dua kali sampai netral, klik `✕` pada Search, tekan Enter


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi S-12 (keyword Search, #8): keyword turunan `Fixture.hardwareStock.derived.*` pada spec ini adalah substring yang sama dengan keyword literal TC (bukan nilai kolom penuh): `Scanner - 2` (TC-AC-ACHS-263). Dicocokkan dengan Tabel E Pre-setup #17 (Device Name unit 20 sampai 28 = 9 baris); himpunan hasil identik dengan hasil di TC. Tidak ada perbedaan.
- Langkah 3 sampai 10 berulang untuk setiap baris tabel Data uji (delapan kolom; bagian 8b butir 7). TC-AC-ACHS-285 sampai 289 berbagi satu perulangan karena langkahnya identik dan hanya kolom yang berbeda.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Pastikan Tab Available aktif", pengembalian sort ke netral, pengosongan Search, dan penutupan overlay Column Visibility.
- Spec memiliki 26 langkah nominal dan 82 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Sort Stock Detail Tab Available pada akun dan dataset read-only yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari satu perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-292 Expected b menyebut lima baris teratas `Handheld Scanner - 28`, `Handheld Scanner - 27`, `Handheld Scanner - 26`, `Handheld Scanner - 25`, `Handheld Scanner - 24`, yaitu urutan menurun, sedangkan Expected c menyatakan Serial Number Ascending sebagai sort terakhir; kedua klausa bertentangan. Spec tidak mengasersi lima baris teratas dan hanya mengasersi 9 baris hasil search (langkah 23) serta indikator sort (langkah 24 dan 25); QA diminta mengoreksi Expected TC.
  - TC-AC-ACHS-289 Expected untuk Min Power dan Max Power menyatakan seluruh unit bernilai sama sehingga urutan mengikuti urutan default; asersi sort pada dua kolom itu terbatas pada indikator dan urutan default (S-11: asersi sort memerlukan dua nilai distinct pada kolom; kolom ini tidak punya).
  - TC-AC-ACHS-289 Current Power Ascending menaruh `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[18].deviceName`, `Fixture.hardwareStock.p17.e[19].deviceName` (Current Power 20 dBm) dan unit Waiting for Approval (`—`) di akhir, sedangkan Descending menaruh `Fixture.hardwareStock.p17.e[28].deviceName` (`—`) di awal; spec mengasersi sesuai Expected TC.
