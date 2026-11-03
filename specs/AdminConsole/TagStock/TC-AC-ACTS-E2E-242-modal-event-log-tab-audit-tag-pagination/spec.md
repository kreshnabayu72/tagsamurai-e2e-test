---
id: TC-AC-ACTS-E2E-242-modal-event-log-tab-audit-tag-pagination
title: "Modal Event Log Tab Audit TAG: Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-919
coverage:
  web: automated
---

# Modal Event Log Tab Audit TAG: Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Audit TAG SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Audit dengan sedikitnya dua nilai distinct pada tiap kolom (Found dan Not Found beragam; Not Found Action `Marked as Damaged/Missing` dan `Kept previous status`; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Sari D` dan pengguna lain). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Data seed untuk pagination: sedikitnya 101 baris pada tabel yang diuji (seed lewat API), dipulihkan di hook `after`.
- Tabel "Page size Tab Audit TAG":

  | Ukuran |
  |---|
  | 25 |
  | 50 |
  | 100 |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Klik tab `Audit TAG`

### TC-AC-ACTS-919: Pagination modal Event Log (Tab Audit TAG): default 10, opsi 10/25/50/100, counter

5. Verifikasi footer pagination menampilkan default 10 baris per halaman
6. Verifikasi teks footer berformat `Showing [From]–[To] of [Total] entries`
7. Buka pilihan Rows per page
8. Verifikasi pilihan page size hanya 10, 25, 50, 100
Langkah 9 sampai 10 diulang untuk setiap baris tabel "Page size Tab Audit TAG" pada Prerequisites (3 iterasi).

9. Pilih page size `<Ukuran>`
10. Verifikasi jumlah baris yang tampil mengikuti page size `<Ukuran>`
11. Klik `[Next →]`
12. Verifikasi tabel berpindah ke halaman berikutnya
13. Klik `[← Prev]`
14. Verifikasi tabel kembali ke halaman sebelumnya

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), langkah 3 (membuka modal Event Log), dan langkah 4 (memilih Tab `Audit TAG`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Perulangan bagian 8b butir 7: langkah 9 sampai 10 diulang untuk setiap baris tabel "Page size Tab Audit TAG" (3 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-919 meminta sedikitnya 101 sesi Audit TAG (seed lewat API); spec ini berdiri sendiri dan dirujuk dari spec 263 (volume pagination permukaan lain).
