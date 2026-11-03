---
id: TC-AC-ACTS-E2E-229-modal-event-log-tab-add-stock-filter-bagian-1
title: "Modal Event Log Tab Add Stock: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-495
  - TC-AC-ACTS-496
  - TC-AC-ACTS-497
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `dateRangeEnd` = tanggal akhir rentang yang mencakup sebagian baris seed; `dateRangeStart` = tanggal awal rentang yang mencakup sebagian baris seed; `dateSingle` = satu tanggal tempat sedikitnya satu baris seed berada; `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Tabel "Opsi filter dropdown Tab Add Stock":

  | Field | Opsi |
  |---|---|
  | `Activity` | `Add Stock` |
  | `Hardware` | `Zebra RFD40 (SN-2201)` |
  | `Modified By` | `Budi S` |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-495: Screening Filter Panel modal Event Log (Tab Add Stock)

4. Klik icon Filter
5. Verifikasi field Filter berurutan sesuai kolom: Date [Select date], Activity [All activities], Hardware [All hardware], Modified By [All users]
6. Verifikasi dropdown bertipe multi-select searchable dan field tanggal bertipe date range picker
7. Verifikasi tombol footer `[Clear Field]` (kiri) dan `[Apply]` (kanan)
8. Verifikasi icon Filter berubah gelap saat panel terbuka
9. Verifikasi kolom Success, Waiting for Approval, dan Failed tidak punya field Filter

### TC-AC-ACTS-496: Filter dropdown multi-select di modal Event Log (Tab Add Stock): Activity, Hardware, Modified By

10. Verifikasi sedikitnya satu baris dengan Activity `Add Stock` dan satu baris dengan Activity `Delete Stock` tampil pada tabel
Langkah 11 sampai 14 diulang untuk setiap baris tabel "Opsi filter dropdown Tab Add Stock" pada Prerequisites (3 iterasi).

11. Pilih opsi `<Opsi>` pada field `<Field>`, klik `[Apply]`
12. Verifikasi hanya baris dengan nilai `<Opsi>` pada kolom `<Field>` tampil
13. Klik `[Clear Field]`, klik `[Apply]`
14. Verifikasi semua baris kembali tampil

### TC-AC-ACTS-497: Filter date range di modal Event Log (Tab Add Stock): Date

15. Verifikasi field tanggal (Date) menampilkan placeholder `Select date` sebelum dipilih
16. Pilih rentang tanggal `Fixture.tagStock.dateRangeStart` sampai `Fixture.tagStock.dateRangeEnd` pada field tanggal (Date), klik `[Apply]`
17. Verifikasi tabel hanya memuat baris dalam rentang inklusif (startDate <= tanggal <= endDate)
18. Klik icon Filter, pilih rentang tanggal Start = End = `Fixture.tagStock.dateSingle` pada field tanggal (Date), klik `[Apply]`
19. Verifikasi tabel hanya menampilkan baris pada hari `Fixture.tagStock.dateSingle`
20. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): mengosongkan Filter lewat `[Clear Field]` dan `[Apply]`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Perulangan bagian 8b butir 7: langkah 11 sampai 14 diulang untuk setiap baris tabel "Opsi filter dropdown Tab Add Stock" (3 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Temuan untuk QA (S-15):
