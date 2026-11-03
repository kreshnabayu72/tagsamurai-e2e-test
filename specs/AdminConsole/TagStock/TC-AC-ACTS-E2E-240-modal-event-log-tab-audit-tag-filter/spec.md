---
id: TC-AC-ACTS-E2E-240-modal-event-log-tab-audit-tag-filter
title: "Modal Event Log Tab Audit TAG: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-914
  - TC-AC-ACTS-915
  - TC-AC-ACTS-916
coverage:
  web: automated
---

# Modal Event Log Tab Audit TAG: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `dateRangeEnd` = tanggal akhir rentang yang mencakup sebagian baris seed; `dateRangeStart` = tanggal awal rentang yang mencakup sebagian baris seed; `dateSingle` = satu tanggal tempat sedikitnya satu baris seed berada; `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Audit TAG SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Audit dengan sedikitnya dua nilai distinct pada tiap kolom (Found dan Not Found beragam; Not Found Action `Marked as Damaged/Missing` dan `Kept previous status`; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Sari D` dan pengguna lain). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Klik tab `Audit TAG`

### TC-AC-ACTS-914: Screening Filter Panel modal Event Log (Tab Audit TAG)

5. Klik icon Filter
6. Verifikasi field Filter berurutan sesuai kolom: Date [Select date], Not Found Action [All actions], Hardware [All hardware], Modified By [All users]
7. Verifikasi dropdown bertipe multi-select searchable dan field tanggal bertipe date range picker
8. Verifikasi tombol footer `[Clear Field]` (kiri) dan `[Apply]` (kanan)
9. Verifikasi kolom Found dan Not Found tidak punya field Filter

### TC-AC-ACTS-915: Filter dropdown multi-select di modal Event Log (Tab Audit TAG): Not Found Action, Hardware, Modified By

10. Verifikasi sedikitnya satu baris `Marked as Damaged/Missing` dan satu baris `Kept previous status` tampil pada tabel
11. Pilih opsi `Marked as Damaged/Missing` pada field `Not Found Action`, klik `[Apply]`
12. Verifikasi hanya baris `Marked as Damaged/Missing` tampil
13. Verifikasi opsi field `Not Found Action` mengikuti nilai yang ada di tabel (`Marked as Damaged/Missing`, `Kept previous status`)
14. Klik `[Clear Field]`, klik `[Apply]`
15. Pilih opsi `Zebra RFD40 (SN-2201)` pada field `Hardware`, klik `[Apply]`
16. Verifikasi hanya baris dengan reader `Zebra RFD40 (SN-2201)` tampil
17. Klik `[Clear Field]`, klik `[Apply]`
18. Pilih opsi `Sari D` pada field `Modified By`, klik `[Apply]`
19. Verifikasi hanya baris oleh `Sari D` tampil
20. Klik `[Clear Field]`, klik `[Apply]`
21. Verifikasi semua baris kembali tampil

### TC-AC-ACTS-916: Filter date range di modal Event Log (Tab Audit TAG): Date

22. Verifikasi field tanggal (Date) menampilkan placeholder `Select date` sebelum dipilih
23. Pilih rentang tanggal `Fixture.tagStock.dateRangeStart` sampai `Fixture.tagStock.dateRangeEnd` pada field tanggal (Date), klik `[Apply]`
24. Verifikasi tabel hanya memuat baris dalam rentang inklusif
25. Klik icon Filter, pilih rentang tanggal Start = End = `Fixture.tagStock.dateSingle` pada field tanggal (Date), klik `[Apply]`
26. Verifikasi tabel hanya menampilkan baris pada hari `Fixture.tagStock.dateSingle`
27. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), langkah 3 (membuka modal Event Log), dan langkah 4 (memilih Tab `Audit TAG`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): mengosongkan Filter lewat `[Clear Field]` dan `[Apply]`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
