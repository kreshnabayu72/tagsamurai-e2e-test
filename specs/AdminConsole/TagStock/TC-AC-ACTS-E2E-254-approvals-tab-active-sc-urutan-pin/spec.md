---
id: TC-AC-ACTS-E2E-254-approvals-tab-active-sc-urutan-pin
title: "Approvals Tab Active: Setup Column: Geser Urutan serta Pin dan Unpin"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-596
  - TC-AC-ACTS-597
coverage:
  web: automated
---

# Approvals Tab Active: Setup Column: Geser Urutan serta Pin dan Unpin

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

### TC-AC-ACTS-596: Setup Column Approvals > TAG Stock > Tab Active: geser urutan kolom (kelas Hideable)

3. Klik header kolom Column Visibility (⋯)
4. Klik `[Setup Column]`
5. Geser kolom `Type` ke bawah kolom `Device Name (SKU)`
6. Klik `[Save]`
7. Verifikasi Live Preview dan tabel mengikuti urutan baru (`Device Name (SKU)` sebelum `Type`) setelah Save
8. Muat ulang halaman (F5)
9. Verifikasi urutan baru bertahan setelah F5

### TC-AC-ACTS-597: Setup Column Approvals > TAG Stock > Tab Active: pin dan unpin kolom (kelas Hideable)

10. Klik header kolom Column Visibility (⋯)
11. Klik `[Setup Column]`
12. Klik icon Pin kolom `Type`
13. Klik `[Save]`
14. Scroll tabel secara horizontal
15. Verifikasi kolom `Type` yang ter-pin tetap diam di sisi kiri saat scroll horizontal
16. Klik header kolom Column Visibility (⋯)
17. Klik `[Setup Column]`
18. Klik icon Pin kolom `Type` lagi (unpin), klik `[Save]`
19. Scroll tabel secara horizontal
20. Verifikasi setelah unpin kolom `Type` ikut bergeser lagi

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
