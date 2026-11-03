---
id: TC-FA-TAG-E2E-190-popup-setup-column-modal-changelog-reorder-dan-pin-bagian-2
title: "Popup Setup Column Modal Changelog: Pin Kolom saat Scroll Horizontal (Bagian 2)"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1430
coverage:
  web: automated
---

# Popup Setup Column Modal Changelog: Pin Kolom saat Scroll Horizontal (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed entri Changelog Paired TAG lewat fixture backend. Pengubahan ukuran viewport browser (mempersempit lalu memulihkan). Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Changelog Paired TAG | E1 26/10/26 10:02 Replace / Excavator 20 Ton - 50 / TAG / [NFC] NF-00090 / [RFID] RF-00420 / Sari W.; E2 26/10/26 10:02 Replace / Excavator 20 Ton - 50 / TAG / [QR] QR-00240 / — / Sari W.; E3 26/10/26 09:20 Replace / Excavator 20 Ton - 20 / TAG / [RFID] RF-00130 / [RFID] RF-00415 / Budi S.; E4 26/10/26 09:14 Replace / Excavator 20 Ton - 42 / TAG / [QR] QR-00230 / [RFID] RF-00412 / Budi S.; E5 25/10/26 16:40 Replace / Forklift Manual - 61 / TAG / [QR] QR-00251 / — / Dedi K.; E6 25/10/26 08:00 Report TAG / Excavator 20 Ton - 20 / Report Type / — / Damaged / Rina T. | `entriChangelog` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel Changelog di cache browser; penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini. Viewport dipulihkan oleh langkah penghubung.

## Test Steps

### TC-FA-TAG-1430

1. Persempit viewport sehingga tabel Changelog perlu scroll horizontal
2. Klik tombol `Changelog` pada Table Tools
3. Klik header kolom terakhir `⋯` pada tabel Changelog
4. Klik `Setup Column...`
5. Pin kolom Modified By
6. Klik `[Save]`
7. Scroll tabel Changelog secara horizontal
8. Verifikasi kolom Modified By tetap di posisinya saat scroll
9. Pulihkan ukuran viewport

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1430). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column Modal Changelog ada di spec 189 (TC-FA-TAG-971 s.d. 974 dan 1429) dan spec 190 (TC-FA-TAG-1430).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 1, 9 (mempersempit dan memulihkan viewport).
- Temuan untuk QA:
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
