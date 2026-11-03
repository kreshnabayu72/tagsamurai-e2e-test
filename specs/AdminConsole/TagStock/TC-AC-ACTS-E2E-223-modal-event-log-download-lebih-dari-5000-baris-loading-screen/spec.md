---
id: TC-AC-ACTS-E2E-223-modal-event-log-download-lebih-dari-5000-baris-loading-screen
title: "Modal Event Log: Download Lebih dari 5.000 Baris Memakai Loading Screen lalu Langsung Terunduh"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-111
coverage:
  web: automated
---

# Modal Event Log: Download Lebih dari 5.000 Baris Memakai Loading Screen lalu Langsung Terunduh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed: dataset Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid` lebih dari 5.000 baris (5.001 baris, seed lewat API), dipulihkan di hook `after`. Berkas hasil unduhan tidak dibuka (hanya loading screen dan keberadaan unduhan diasersi).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembaca nama berkas unduhan di browser, disediakan tim FE.
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`

### TC-AC-ACTS-111: Download lebih dari 5.000 baris memakai loading screen lalu langsung terunduh

3. Klik icon `[Event Log]` di toolbar Tab Available
4. Verifikasi sedikitnya satu baris sesi tampil pada Tab Add Stock (dataset sesi lebih dari 5.000 baris di-seed lewat API)
5. Klik icon Download, pilih `Download as CSV`
6. Verifikasi loading screen tampil sampai file siap
7. Verifikasi tidak ada toast informasi, notifikasi in-app, atau job background
8. Verifikasi file langsung terunduh setelah loading screen selesai

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16) dan langkah 2 (row action `Detail`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Spec ini memuat satu TC kelas e (volume 5.001 baris); isi sel berkas (kelas f) tidak diasersi.
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-111 tidak menyebut cara mengamati "file langsung terunduh" dan "tidak ada job background"; spec mengasersi keberadaan berkas terunduh dan tidak adanya toast atau notifikasi in-app.
