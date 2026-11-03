---
id: TC-AC-ACTS-E2E-252-approvals-tab-active-filter-bagian-2-sc-screening
title: "Approvals Tab Active: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-591
  - TC-AC-ACTS-592
  - TC-AC-ACTS-593
  - TC-AC-ACTS-594
coverage:
  web: automated
---

# Approvals Tab Active: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pemulihan Setup Column: hook `before` dan `after` menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- State global: konfigurasi kolom Setup Column yang disimpan spec dipulihkan di hook `before` dan `after` (menghapus preferensi kolom di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-591: Isi opsi dropdown Filter Approvals > TAG Stock > Tab Active = DISTINCT data tabel

3. Klik icon Filter, buka dropdown `Type`
4. Verifikasi opsi `Type` hanya berisi nilai yang ada di baris tabel saat ini
5. Verifikasi nilai yang tidak muncul di tabel tidak menjadi opsi
6. Tutup dropdown `Type` dengan Esc

### TC-AC-ACTS-592: Kombinasi AND dua field Filter di Approvals > TAG Stock > Tab Active

7. Verifikasi sedikitnya satu baris Subject tampil pada tabel
8. Pilih `Register Duplicate` pada `Type` dan `RFID-ASSET-CORE-R5` pada `SKU`, klik `[Apply]`
9. Verifikasi hanya baris yang memenuhi kedua kriteria (Type `Register Duplicate` dan SKU `RFID-ASSET-CORE-R5`) tampil
10. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACTS-593: Setup Column Approvals > TAG Stock > Tab Active: screening Overlay Column Visibility

11. Klik header kolom Column Visibility (⋯)
12. Verifikasi Overlay memuat tombol `[Setup Column]` dan daftar kolom berurutan `Type`, `Device Name (SKU)`, `Category`, `Matched Identifier`, `Existing Record`, `Requested By`, `Requested At`
13. Verifikasi setiap kolom pada Overlay berstatus checkbox checked dan enabled (Hideable) dengan drag handle
14. Verifikasi Overlay tidak menutup tabel (tanpa backdrop)

### TC-AC-ACTS-594: Setup Column Approvals > TAG Stock > Tab Active: screening Popup Setup Column dan Live Preview

15. Klik `[Setup Column]`
16. Verifikasi header Popup Setup Column memuat title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol close (X)
17. Verifikasi body Popup memuat daftar kolom `Type`, `Device Name (SKU)`, `Category`, `Matched Identifier`, `Existing Record`, `Requested By`, `Requested At` dengan checkbox, drag handle, icon Pin, dan Live Preview urutan header
18. Verifikasi footer Popup memuat `[Reset to Default]` dan `[Save]` rata kanan, tanpa `[Cancel]`
19. Tutup Popup Setup Column dengan klik (X)

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; mengosongkan Filter lewat `[Clear Field]` dan `[Apply]`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
