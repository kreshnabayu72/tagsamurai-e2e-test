---
id: TC-AC-ACHS-E2E-131-filter-tab-available-screening-opsi-dan-apply-per-field
title: "Filter Stock Detail Tab Available: Screening Panel, Isi Opsi, dan Apply per Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-271
  - TC-AC-ACHS-272
  - TC-AC-ACHS-273
  - TC-AC-ACHS-274
coverage:
  web: automated
---

# Filter Stock Detail Tab Available: Screening Panel, Isi Opsi, dan Apply per Field

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
  | Registered By unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Registered By unit 10 Tabel E (#17); pendaftar yang sama untuk unit 13, 16, 19, 22, 25 | `Fixture.hardwareStock.p17.e[10].registeredBy` |
  | Device Name unit 11 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 11, Tabel E (#17) | `Fixture.hardwareStock.p17.e[11].deviceName` |
  | Registered By unit 11 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Registered By unit 11 Tabel E (#17); pendaftar yang sama untuk unit 14, 17, 20, 23, 26 | `Fixture.hardwareStock.p17.e[11].registeredBy` |
  | Device Name unit 12 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 12, Tabel E (#17) | `Fixture.hardwareStock.p17.e[12].deviceName` |
  | Registered By unit 12 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Registered By unit 12 Tabel E (#17); pendaftar yang sama untuk unit 15, 18, 21, 24, 27 | `Fixture.hardwareStock.p17.e[12].registeredBy` |
  | Device Name unit 13 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 13, Tabel E (#17) | `Fixture.hardwareStock.p17.e[13].deviceName` |
  | Device Name unit 14 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 14, Tabel E (#17) | `Fixture.hardwareStock.p17.e[14].deviceName` |
  | Device Name unit 15 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 15, Tabel E (#17) | `Fixture.hardwareStock.p17.e[15].deviceName` |
  | Device Name unit 16 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 16, Tabel E (#17) | `Fixture.hardwareStock.p17.e[16].deviceName` |
  | Device Name unit 19 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 19, Tabel E (#17) | `Fixture.hardwareStock.p17.e[19].deviceName` |
  | Device Name unit 22 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 22, Tabel E (#17) | `Fixture.hardwareStock.p17.e[22].deviceName` |
  | Device Name unit 25 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 25, Tabel E (#17) | `Fixture.hardwareStock.p17.e[25].deviceName` |
  | Device Name unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | Registered By unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Registered By unit 28 Tabel E (#17), unit Waiting for Approval | `Fixture.hardwareStock.p17.e[28].registeredBy` |
  | Nilai turunan dropdownSearchRegisteredByU10 | turunan dari `Fixture.hardwareStock.p17.e[10].registeredBy` | keyword pencarian internal dropdown Registered By: 3 huruf pertama Registered By unit 10 Tabel E dalam huruf kecil (`ded`) | `Fixture.hardwareStock.derived.dropdownSearchRegisteredByU10` |
  | Nilai turunan registeredAtU10Date | turunan dari `Fixture.hardwareStock.p17.e[10].registeredAt` | bagian tanggal (tanpa jam) Registered At unit 10 Tabel E (`10 May 2026`) | `Fixture.hardwareStock.derived.registeredAtU10Date` |
  | Nilai turunan registeredAtU15Date | turunan dari `Fixture.hardwareStock.p17.e[15].registeredAt` | bagian tanggal (tanpa jam) Registered At unit 15 Tabel E (`15 May 2026`) | `Fixture.hardwareStock.derived.registeredAtU15Date` |
- Data uji TC-AC-ACHS-272 (isi opsi dropdown kelas multi; sumber opsi DISTINCT dari baris tabel):

  | No | Field | Placeholder | Opsi | Jumlah |
  |---|---|---|---|---|
  | 1 | Status | `All statuses` | `Available`, `Waiting for Approval` | 2 |
  | 2 | Registered By | `All users` | `Fixture.hardwareStock.p17.e[12].registeredBy`, `Fixture.hardwareStock.p17.e[10].registeredBy`, `Fixture.hardwareStock.p17.e[28].registeredBy`, `Fixture.hardwareStock.p17.e[11].registeredBy` | 4 |

- Data uji TC-AC-ACHS-273 (Apply kelas multi):

  | No | Field | Nilai | Hasil |
  |---|---|---|---|
  | 1 | Status | `Waiting for Approval` | 1 baris: `Fixture.hardwareStock.p17.e[28].deviceName` |
  | 2 | Registered By | `Fixture.hardwareStock.p17.e[10].registeredBy` | 6 baris: `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[19].deviceName`, `Fixture.hardwareStock.p17.e[16].deviceName`, `Fixture.hardwareStock.p17.e[13].deviceName`, `Fixture.hardwareStock.p17.e[10].deviceName` |

- Data uji TC-AC-ACHS-274 (Apply kelas date): Registered At rentang `Fixture.hardwareStock.derived.registeredAtU10Date` sampai `Fixture.hardwareStock.derived.registeredAtU15Date` (Start tidak sama dengan End); hasil 6 baris `Fixture.hardwareStock.p17.e[15].deviceName`, `Fixture.hardwareStock.p17.e[14].deviceName`, `Fixture.hardwareStock.p17.e[13].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName`, `Fixture.hardwareStock.p17.e[11].deviceName`, `Fixture.hardwareStock.p17.e[10].deviceName`.
- Pilihan spec: keyword pencarian internal dropdown pada TC-AC-ACHS-272 adalah `Fixture.hardwareStock.derived.dropdownSearchRegisteredByU10` pada dropdown Registered By (3 huruf pertama opsi `Fixture.hardwareStock.p17.e[10].registeredBy`, huruf kecil untuk menguji ketidakpekaan huruf besar kecil) dan `zzqx-tidak-ada` (tanpa kecocokan).
- State global yang diubah: tidak ada yang bertahan.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab Available aktif

### TC-AC-ACHS-271: Screening Filter Panel

3. Arahkan kursor ke icon Filter
4. Verifikasi tooltip `Filter`
5. Klik icon Filter
6. Verifikasi ikon Filter menjadi gelap saat panel terbuka
7. Verifikasi field Filter Panel berurutan sesuai urutan kolom tabel: Status (multi-select searchable, placeholder `All statuses`), Registered At (date range picker, placeholder `Select date`), Registered By (multi-select searchable, placeholder `All users`)
8. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
9. Verifikasi tidak ada field Photo atau identifier teks

### TC-AC-ACHS-272: Isi opsi dropdown Filter kelas multi

10. Untuk setiap baris tabel Data uji TC-AC-ACHS-272 (langkah 10 sampai 13): buka dropdown field pada Filter Panel
11. Verifikasi daftar opsi dropdown sesuai kolom "Opsi" dan "Jumlah"
12. Verifikasi kotak pencarian internal ada di dropdown
13. Tutup dropdown
14. Buka dropdown Registered By, ketik `Fixture.hardwareStock.derived.dropdownSearchRegisteredByU10` pada kotak pencarian internal
15. Verifikasi daftar opsi menyempit dan memuat `Fixture.hardwareStock.p17.e[10].registeredBy`
16. Ganti isi kotak pencarian internal dengan `zzqx-tidak-ada`
17. Verifikasi tampil teks `No results found` pada dropdown
18. Tutup dropdown Registered By

### TC-AC-ACHS-273: Apply kelas multi per field

19. Untuk setiap baris tabel Data uji TC-AC-ACHS-273 (langkah 19 sampai 22): pilih nilai pada dropdown field lalu klik `[Apply]`
20. Verifikasi jumlah baris dan baris sesuai kolom "Hasil"
21. Klik `[Clear Field]`, klik `[Apply]`
22. Verifikasi tabel kembali ke seluruh baris (info `Showing 1–10 of 19 entries`)

### TC-AC-ACHS-274: Apply kelas date

23. Isi field Registered At dengan rentang `Fixture.hardwareStock.derived.registeredAtU10Date` sampai `Fixture.hardwareStock.derived.registeredAtU15Date`, klik `[Apply]`
24. Verifikasi tabel menampilkan 6 baris: `Fixture.hardwareStock.p17.e[15].deviceName`, `Fixture.hardwareStock.p17.e[14].deviceName`, `Fixture.hardwareStock.p17.e[13].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName`, `Fixture.hardwareStock.p17.e[11].deviceName`, `Fixture.hardwareStock.p17.e[10].deviceName`
25. Klik `[Clear Field]`, klik `[Apply]`
26. Verifikasi tabel kembali ke seluruh baris (info `Showing 1–10 of 19 entries`)
27. Klik icon Filter untuk menutup panel


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah 10 sampai 13 dan 19 sampai 22 berulang untuk setiap baris tabel Data uji (dua iterasi masing-masing; bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): "Pastikan Tab Available aktif", penutupan dropdown (langkah 13), `[Clear Field]` lalu `[Apply]` antar-iterasi, dan penutupan panel Filter.
- Spec memiliki 27 langkah nominal dan 35 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Filter Stock Detail Tab Available pada akun dan dataset read-only yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari perulangan per field tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-272 tidak menyebut kata kunci pencarian internal; spec memilih `Fixture.hardwareStock.derived.dropdownSearchRegisteredByU10` dan `zzqx-tidak-ada` (pilihan spec).
