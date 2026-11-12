---
id: TC-FA-TAG-E2E-188-popup-setup-column-tab-to-be-returned-dan-modal-event-log-bagian-2
title: "Popup Setup Column Modal Event Log: Reset, Reorder, dan Pin (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1426
  - TC-FA-TAG-1427
  - TC-FA-TAG-1428
coverage:
  web: automated
---

# Popup Setup Column Modal Event Log: Reset, Reorder, dan Pin (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned, Return Group, dan entri Event Log. Pengubahan ukuran viewport browser (mempersempit lalu memulihkan). Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Event Log | 27 Okt 2026 14:15 [RFID] RF-00093, Excavator 20 Ton - 5, Disposal Center, Dedi K., Budi S., Assigned, Paired; 26 Okt 2026 10:02 [RFID] RF-00071, Last Asset Excavator 20 Ton - 2, Return Group Disposal Center, Handed Over By Dedi K., Received By Budi S., Method Scan, Final Status Available; 26 Okt 2026 09:40 [NFC] NF-00092, Laptop Pro 14 - 8, HQ Warehouse, Rina T., Sari W., Manual, Damaged/Missing | `eventLogToBeReturned` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel Event Log di cache browser (disembunyikan lalu direset, diurutkan ulang, dan di-pin); penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini. Viewport dipulihkan oleh langkah penghubung.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 1, 7, 12, 18).

## Test Steps

### TC-FA-TAG-1426

1. Sembunyikan kolom Method pada Setup Column Modal Event Log lalu `[Save]` (precondition TC, tidak diasersi): buka Fixed Asset > TAG > To Be Returned, klik tombol "Event Log", klik header kolom terakhir `⋯`, `Setup Column...`, hilangkan centang Method, `[Save]`
2. Klik header kolom terakhir `⋯` pada tabel Event Log
3. Klik `Setup Column...`
4. Klik `[Reset to Default]`
5. Verifikasi kedelapan kolom tercentang dalam urutan default
6. Verifikasi tabel Event Log menampilkan kolom Method kembali (pratinjau)
7. Klik `[Save]`
8. Verifikasi konfigurasi default tersimpan (popup tertutup dan tabel Event Log menampilkan kolom default)

### TC-FA-TAG-1427

9. Klik header kolom terakhir `⋯` pada tabel Event Log
10. Klik `Setup Column...`
11. Seret kolom Method ke posisi sebelum Handed Over By
12. Klik `[Save]`
13. Verifikasi urutan kolom tabel Event Log menjadi Received At, TAG Code, Last Asset, Return Group, Method, Handed Over By, Received By, Final Status

### TC-FA-TAG-1428

14. Persempit viewport sehingga tabel Event Log perlu scroll horizontal
15. Klik header kolom terakhir `⋯` pada tabel Event Log
16. Klik `Setup Column...`
17. Pin kolom TAG Code
18. Klik `[Save]`
19. Scroll tabel Event Log secara horizontal
20. Verifikasi kolom TAG Code tetap di posisinya saat scroll
21. Pulihkan ukuran viewport

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1426, TC-FA-TAG-1427, TC-FA-TAG-1428). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column tab To Be Returned dan Modal Event Log ada di spec 187 (TC-FA-TAG-1422 s.d. 1425) dan spec 188 (TC-FA-TAG-1426 s.d. 1428).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 1, 14, 21 (menyiapkan precondition TC-FA-TAG-1426 serta mempersempit dan memulihkan viewport).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 1, 7, 12, 18).
- Temuan untuk QA:
  - Langkah pembuka TC-FA-TAG-1426 (membuka tab To Be Returned dan Modal Event Log) dan precondition kolom Method disembunyikan ditulis dalam satu langkah penghubung; Modal Event Log tetap terbuka sampai akhir spec.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
