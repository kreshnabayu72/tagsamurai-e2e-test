---
id: TC-AC-ACTS-E2E-237-modal-event-log-tab-audit-tag-screening-urutan
title: "Modal Event Log Tab Audit TAG: Screening Header, Kolom, Footer dan Urutan Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-906
  - TC-AC-ACTS-907
coverage:
  web: automated
---

# Modal Event Log Tab Audit TAG: Screening Header, Kolom, Footer dan Urutan Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Audit TAG SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Audit dengan sedikitnya dua nilai distinct pada tiap kolom (Found dan Not Found beragam; Not Found Action `Marked as Damaged/Missing` dan `Kept previous status`; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Sari D` dan pengguna lain). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Klik tab `Audit TAG`

### TC-AC-ACTS-906: Screening modal Event Log (Tab Audit TAG): header, kolom, footer

5. Verifikasi header modal memuat title `Event Log` dan tab `Audit TAG` aktif
6. Verifikasi Table Tools memuat `Search`, `Filter`, `Download`
7. Verifikasi kolom `Date`, `Found`, `Not Found`, `Not Found Action`, `Hardware`, `Modified By` sortable
8. Verifikasi kolom Column Visibility (⋯) tidak dapat disortir dan menu baris per baris memuat `Detail`
9. Verifikasi footer memuat pagination default 10 data per halaman

### TC-AC-ACTS-907: Default sort modal Event Log (Tab Audit TAG): Date Newest First

10. Klik tab `Add Stock`
11. Klik tab `Audit TAG`
12. Verifikasi baris terurut Date Newest First saat tab dibuka
13. Verifikasi tidak ada panah sort aktif pada kolom lain

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), langkah 3 (membuka modal Event Log), dan langkah 4 (memilih Tab `Audit TAG`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
