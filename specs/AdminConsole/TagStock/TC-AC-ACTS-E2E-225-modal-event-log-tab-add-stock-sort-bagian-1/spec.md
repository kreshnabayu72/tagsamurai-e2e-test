---
id: TC-AC-ACTS-E2E-225-modal-event-log-tab-add-stock-sort-bagian-1
title: "Modal Event Log Tab Add Stock: Sort 3-State Per Kelas Kolom (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-482
  - TC-AC-ACTS-483
  - TC-AC-ACTS-484
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Sort 3-State Per Kelas Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Tabel "Kolom sort kelas teks Tab Add Stock":

  | Kolom | Urutan Ascending |
  |---|---|
  | `Activity` | A-Z |
  | `Hardware` | A-Z |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Verifikasi tabel memuat sedikitnya satu baris sesi

### TC-AC-ACTS-482: Sort 3-state kelas tanggal di modal Event Log (Tab Add Stock): Date

5. Klik header kolom `Date` sekali
6. Verifikasi urutan kolom `Date` Ascending (↑) (Oldest First)
7. Klik header kolom `Date` kedua kali
8. Verifikasi urutan kolom `Date` Descending (↓), terbalik dari urutan Ascending
9. Klik header kolom `Date` ketiga kali
10. Verifikasi indikator sort kolom `Date` hilang dan tabel kembali ke urutan default Date Newest First

### TC-AC-ACTS-483: Sort 3-state kelas teks di modal Event Log (Tab Add Stock): Activity, Hardware

Langkah 11 sampai 16 diulang untuk setiap baris tabel "Kolom sort kelas teks Tab Add Stock" pada Prerequisites (2 iterasi).

11. Klik header kolom `<Kolom>` sekali
12. Verifikasi urutan kolom `<Kolom>` Ascending (↑) (<Urutan Ascending>)
13. Klik header kolom `<Kolom>` kedua kali
14. Verifikasi urutan kolom `<Kolom>` Descending (↓), terbalik dari urutan Ascending
15. Klik header kolom `<Kolom>` ketiga kali
16. Verifikasi indikator sort kolom `<Kolom>` hilang dan tabel kembali ke urutan default Date Newest First

### TC-AC-ACTS-484: Sort 3-state kelas user di modal Event Log (Tab Add Stock): Modified By

17. Klik header kolom `Modified By` sekali
18. Verifikasi urutan kolom `Modified By` Ascending (↑) (A-Z menurut nama lengkap user)
19. Klik header kolom `Modified By` kedua kali
20. Verifikasi urutan kolom `Modified By` Descending (↓), terbalik dari urutan Ascending
21. Klik header kolom `Modified By` ketiga kali
22. Verifikasi indikator sort kolom `Modified By` hilang dan tabel kembali ke urutan default Date Newest First

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Perulangan bagian 8b butir 7: langkah 11 sampai 16 diulang untuk setiap baris tabel "Kolom sort kelas teks Tab Add Stock" (2 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
