---
id: TC-AC-ACTS-E2E-231-modal-event-log-tab-add-stock-sc-ceklis
title: "Modal Event Log Tab Add Stock: Setup Column: Ceklis dan Unceklis Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-502
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Setup Column: Ceklis dan Unceklis Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Tabel "Kolom Hideable Tab Add Stock":

  | Kolom |
  |---|
  | `Date` |
  | `Activity` |
  | `Success` |
  | `Waiting for Approval` |
  | `Failed` |
  | `Hardware` |
  | `Modified By` |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pemulihan Setup Column: hook `before` dan `after` menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- State global: konfigurasi kolom Setup Column yang disimpan spec dipulihkan di hook `before` dan `after` (menghapus preferensi kolom di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-502: Setup Column modal Event Log (Tab Add Stock): ceklis dan unceklis kolom (kelas Hideable)

4. Klik header kolom Column Visibility (⋯)
5. Klik `[Setup Column]`
Langkah 6 sampai 9 diulang untuk setiap baris tabel "Kolom Hideable Tab Add Stock" pada Prerequisites (7 iterasi).

6. Hilangkan centang kolom `<Kolom>` di Setup Column
7. Verifikasi preview langsung menyembunyikan kolom `<Kolom>`
8. Centang kembali kolom `<Kolom>`
9. Verifikasi preview langsung menampilkan kolom `<Kolom>` kembali
10. Hilangkan centang kolom `Date` dan `Activity`, klik `[Save]`
11. Verifikasi kolom `Date` dan `Activity` hilang dari tabel
12. Muat ulang halaman (F5)
13. Verifikasi kolom `Date` dan `Activity` tetap hilang setelah F5
14. Klik header kolom Column Visibility (⋯)
15. Klik `[Setup Column]`
16. Centang kembali kolom `Date` dan `Activity`, klik `[Save]`
17. Verifikasi kolom `Date` dan `Activity` tampil lagi di tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Perulangan bagian 8b butir 7: langkah 6 sampai 9 diulang untuk setiap baris tabel "Kolom Hideable Tab Add Stock" (7 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Alasan di atas sekitar 35 langkah: spec ini 41 langkah dihitung dengan ekspansi; seluruh blok memakai satu kelas harness dan satu dataset seed, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang diulang per baris tabel sah menurut bagian 8b butir 7.
- Temuan untuk QA (S-15):
