---
id: TC-AC-ACTS-E2E-236-modal-event-log-tab-add-stock-download-hover-user
title: "Modal Event Log Tab Add Stock: Download CSV dan XLSX; Hover Nama User"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-514
  - TC-AC-ACTS-515
  - TC-AC-ACTS-517
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Download CSV dan XLSX; Hover Nama User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Berkas hasil unduhan diasersi nama dan ekstensinya saja; isi sel berkas XLSX (kelas f) ada di spec 260.
- Nama user `Sari D` dan `Sari Dewi` (Data Uji Dinamis #3) ada pada sesi seed.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembaca nama berkas unduhan di browser, disediakan tim FE.
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-514: Download modal Event Log (Tab Add Stock) sebagai CSV: nama file dan extension

4. Klik icon Download, pilih `Download as CSV`
5. Verifikasi tidak muncul toast sukses
6. Verifikasi file terunduh bernama `TAG-Stock-Event-Log-RFID-ASSET-CORE-R5.csv`

### TC-AC-ACTS-515: Download modal Event Log (Tab Add Stock) sebagai XLSX: nama file dan extension

7. Klik icon Download, pilih `Download as XLSX`
8. Verifikasi tidak muncul toast sukses
9. Verifikasi file terunduh bernama `TAG-Stock-Event-Log-RFID-ASSET-CORE-R5.xlsx`

### TC-AC-ACTS-517: Hover nama user kolom `Modified By` di modal Event Log (Tab Add Stock)

10. Hover nama user `Sari D` di kolom `Modified By`
11. Verifikasi kolom `Modified By` menampilkan `Sari D` (first name lengkap dan inisial last name)
12. Verifikasi tooltip menampilkan nama lengkap `Sari Dewi`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Isi sel berkas XLSX Tab Add Stock (TC-AC-ACTS-516) ada di spec 260.
- Temuan untuk QA (S-15):
