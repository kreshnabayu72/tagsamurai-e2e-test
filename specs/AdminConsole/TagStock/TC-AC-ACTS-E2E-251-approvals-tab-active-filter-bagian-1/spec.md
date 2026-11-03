---
id: TC-AC-ACTS-E2E-251-approvals-tab-active-filter-bagian-1
title: "Approvals Tab Active: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-588
  - TC-AC-ACTS-589
  - TC-AC-ACTS-590
coverage:
  web: automated
---

# Approvals Tab Active: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `dateRangeEnd` = tanggal akhir rentang yang mencakup sebagian baris seed; `dateRangeStart` = tanggal awal rentang yang mencakup sebagian baris seed; `dateSingle` = satu tanggal tempat sedikitnya satu baris seed berada; `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Tabel "Opsi filter dropdown Tab Active":

  | Field | Opsi |
  |---|---|
  | `Type` | `Register Duplicate` |
  | `SKU` | `RFID-ASSET-CORE-R5` |
  | `Category` | `RFID - Object TAG` |
  | `Requested By` | `PT Maju Bersama (Distributor)` |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-588: Screening Filter Panel Approvals > TAG Stock > Tab Active

3. Klik icon Filter
4. Verifikasi field Filter berurutan sesuai kolom: Type [All types], SKU [All SKUs], Category [All categories], Requested By [All requesters], Requested At [Select date]
5. Verifikasi dropdown bertipe multi-select searchable dan field tanggal bertipe date range picker
6. Verifikasi tombol footer `[Clear Field]` (kiri) dan `[Apply]` (kanan)
7. Verifikasi icon Filter berubah gelap saat panel terbuka

### TC-AC-ACTS-589: Filter dropdown multi-select di Approvals > TAG Stock > Tab Active: Type, SKU, Category, Requested By

8. Verifikasi sedikitnya satu baris dengan Type `Register Duplicate` dan satu baris dengan Type `Activation Collision` tampil pada tabel
Langkah 9 sampai 12 diulang untuk setiap baris tabel "Opsi filter dropdown Tab Active" pada Prerequisites (4 iterasi).

9. Pilih opsi `<Opsi>` pada field `<Field>`, klik `[Apply]`
10. Verifikasi hanya baris dengan nilai `<Opsi>` pada kolom `<Field>` tampil
11. Klik `[Clear Field]`, klik `[Apply]`
12. Verifikasi semua baris kembali tampil

### TC-AC-ACTS-590: Filter date range di Approvals > TAG Stock > Tab Active: Requested At

13. Verifikasi field tanggal (Requested At) menampilkan placeholder `Select date` sebelum dipilih
14. Pilih rentang tanggal `Fixture.tagStock.dateRangeStart` sampai `Fixture.tagStock.dateRangeEnd` pada field tanggal (Requested At), klik `[Apply]`
15. Verifikasi tabel hanya memuat baris dalam rentang inklusif (startDate <= tanggal <= endDate)
16. Klik icon Filter, pilih rentang tanggal Start = End = `Fixture.tagStock.dateSingle` pada field tanggal (Requested At), klik `[Apply]`
17. Verifikasi tabel hanya menampilkan baris pada hari `Fixture.tagStock.dateSingle`
18. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): mengosongkan Filter lewat `[Clear Field]` dan `[Apply]`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Perulangan bagian 8b butir 7: langkah 9 sampai 12 diulang untuk setiap baris tabel "Opsi filter dropdown Tab Active" (4 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
