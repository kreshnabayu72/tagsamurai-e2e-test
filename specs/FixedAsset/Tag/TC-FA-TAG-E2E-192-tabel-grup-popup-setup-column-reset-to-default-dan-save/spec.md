---
id: TC-FA-TAG-E2E-192-tabel-grup-popup-setup-column-reset-to-default-dan-save
title: "Tabel Grup: Reset to Default pada Popup Setup Column Baru Permanen setelah Save"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-757
coverage:
  web: automated
---

# Tabel Grup: Reset to Default pada Popup Setup Column Baru Permanen setelah Save

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel grup di cache browser (kolom Reported disembunyikan dan disimpan, lalu direset ke default dan disimpan); penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini.

## Test Steps

### TC-FA-TAG-757

1. Sembunyikan kolom Reported lewat Setup Column lalu `[Save]` (precondition TC, tidak diasersi): klik header kolom terakhir `⋯` pada tabel grup, `Setup Column...`, hilangkan centang Reported, `[Save]`
2. Klik header kolom terakhir `⋯` pada tabel grup
3. Klik `Setup Column...`
4. Klik `[Reset to Default]`
5. Verifikasi ketujuh kolom tercentang dalam urutan default
6. Verifikasi tabel grup menampilkan ketujuh kolom (pratinjau)
7. Klik `[Save]`
8. Verifikasi konfigurasi default tersimpan (popup tertutup dan tabel grup menampilkan ketujuh kolom)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-757). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column tabel grup ada di spec 183 (TC-FA-TAG-752 s.d. 756), spec 192 (TC-FA-TAG-757), dan spec 184 (TC-FA-TAG-758 s.d. 759).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 1 (menyiapkan precondition kolom Reported tersembunyi dan tersimpan).
- Temuan untuk QA:
  - Precondition TC-FA-TAG-757 (kolom Reported sudah disembunyikan dan disimpan) tidak diasersi; spec menyiapkannya lewat Setup Column di langkah penghubung.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
