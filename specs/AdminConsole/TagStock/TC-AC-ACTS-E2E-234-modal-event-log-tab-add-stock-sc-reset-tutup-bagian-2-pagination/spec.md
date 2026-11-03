---
id: TC-AC-ACTS-E2E-234-modal-event-log-tab-add-stock-sc-reset-tutup-bagian-2-pagination
title: "Modal Event Log Tab Add Stock: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2)"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-508
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pemulihan Setup Column: hook `before` dan `after` menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- State global: konfigurasi kolom Setup Column yang disimpan spec dipulihkan di hook `before` dan `after` (menghapus preferensi kolom di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-508: Pin ke-4 diblokir di Setup Column modal Event Log (Tab Add Stock)

4. Klik header kolom Column Visibility (⋯)
5. Klik `[Setup Column]`
6. Klik icon Pin pada kolom `Date`, `Activity`, dan `Success` (3 kolom)
7. Arahkan kursor ke icon Pin kolom `Waiting for Approval` dan coba klik
8. Verifikasi icon Pin kolom `Waiting for Approval` disabled dan kolom tidak ter-pin
9. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
10. Unpin satu kolom yang ter-pin
11. Verifikasi icon Pin kolom lain aktif kembali
12. Tutup Popup Setup Column dengan klik (X)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay.
- Temuan untuk QA (S-15):
