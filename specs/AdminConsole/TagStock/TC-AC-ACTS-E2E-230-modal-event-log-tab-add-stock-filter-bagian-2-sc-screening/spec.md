---
id: TC-AC-ACTS-E2E-230-modal-event-log-tab-add-stock-filter-bagian-2-sc-screening
title: "Modal Event Log Tab Add Stock: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-498
  - TC-AC-ACTS-499
  - TC-AC-ACTS-500
  - TC-AC-ACTS-501
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-498: Isi opsi dropdown Filter modal Event Log (Tab Add Stock) = DISTINCT data tabel

4. Klik icon Filter, buka dropdown `Activity`
5. Verifikasi opsi `Activity` hanya berisi nilai yang ada di baris tabel saat ini (`Add Stock`, `Delete Stock`)
6. Verifikasi nilai yang tidak muncul di tabel tidak menjadi opsi
7. Tutup dropdown `Activity` dengan Esc

### TC-AC-ACTS-499: Kombinasi AND dua field Filter di modal Event Log (Tab Add Stock)

8. Verifikasi sedikitnya satu baris sesi tampil pada tabel
9. Pilih `Add Stock` pada `Activity` dan `Budi S` pada `Modified By`, klik `[Apply]`
10. Verifikasi hanya baris yang memenuhi kedua kriteria (Activity `Add Stock` dan Modified By `Budi S`) tampil
11. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACTS-500: Setup Column modal Event Log (Tab Add Stock): screening Overlay Column Visibility

12. Klik header kolom Column Visibility (⋯)
13. Verifikasi Overlay memuat tombol `[Setup Column]` dan daftar kolom berurutan `Date`, `Activity`, `Success`, `Waiting for Approval`, `Failed`, `Hardware`, `Modified By`
14. Verifikasi setiap kolom pada Overlay berstatus checkbox checked dan enabled (Hideable) dengan drag handle
15. Verifikasi Overlay tidak menutup tabel (tanpa backdrop)

### TC-AC-ACTS-501: Setup Column modal Event Log (Tab Add Stock): screening Popup Setup Column dan Live Preview

16. Klik `[Setup Column]`
17. Verifikasi header Popup Setup Column memuat title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol close (X)
18. Verifikasi body Popup memuat daftar kolom `Date`, `Activity`, `Success`, `Waiting for Approval`, `Failed`, `Hardware`, `Modified By` dengan checkbox, drag handle, icon Pin, dan Live Preview urutan header
19. Verifikasi footer Popup memuat `[Reset to Default]` dan `[Save]` rata kanan, tanpa `[Cancel]`
20. Tutup Popup Setup Column dengan klik (X)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; mengosongkan Filter lewat `[Clear Field]` dan `[Apply]`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
