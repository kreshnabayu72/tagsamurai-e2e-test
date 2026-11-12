---
id: TC-FA-TAG-E2E-186-popup-setup-column-t-tag-02-screening-save-reset-reorder-dan-bagian-2
title: "Popup Setup Column T-TAG-02: Esc, Reset, Reorder, dan Pin (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1418
  - TC-FA-TAG-1419
  - TC-FA-TAG-1420
  - TC-FA-TAG-1421
coverage:
  web: automated
---

# Popup Setup Column T-TAG-02: Esc, Reset, Reorder, dan Pin (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Pengubahan ukuran viewport browser (mempersempit lalu memulihkan). Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |
| Isi Popup Detail | Grup 'Excavator 20 Ton' / Plant B memuat 20 aset | `asetAcuanPlantB` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel T-TAG-02 di cache browser (disembunyikan, ditampilkan, diurutkan ulang, dan di-pin); penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini. Viewport dipulihkan oleh langkah penghubung.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 9, 15, 20, 26).

## Test Steps

### TC-FA-TAG-1418

1. Klik Asset Name 'Excavator 20 Ton' pada baris Plant B untuk membuka Popup Detail
2. Klik header kolom terakhir `⋯` pada tabel T-TAG-02
3. Klik `Setup Column...`
4. Hilangkan centang kolom Group
5. Tekan Esc
6. Verifikasi Popup Setup Column tertutup
7. Verifikasi kolom Group tetap tampil pada tabel T-TAG-02
8. Verifikasi Popup Detail tetap terbuka

### TC-FA-TAG-1419

9. Sembunyikan kolom Brand dan tampilkan kolom curated Measurement lewat Setup Column, lalu `[Save]` (precondition TC, tidak diasersi)
10. Klik header kolom terakhir `⋯` pada tabel T-TAG-02
11. Klik `Setup Column...`
12. Klik `[Reset to Default]`
13. Verifikasi kedelapan kolom default tercentang dalam urutan default dan kolom curated tidak tercentang
14. Verifikasi tabel T-TAG-02 menampilkan kolom default (pratinjau)
15. Klik `[Save]`
16. Verifikasi konfigurasi default tersimpan (popup tertutup dan tabel menampilkan kolom default)

### TC-FA-TAG-1420

17. Klik header kolom terakhir `⋯` pada tabel T-TAG-02
18. Klik `Setup Column...`
19. Seret kolom Group ke posisi sebelum Brand
20. Klik `[Save]`
21. Verifikasi urutan kolom tabel T-TAG-02 menjadi Group lalu Brand

### TC-FA-TAG-1421

22. Persempit viewport sehingga tabel T-TAG-02 perlu scroll horizontal
23. Klik header kolom terakhir `⋯` pada tabel T-TAG-02
24. Klik `Setup Column...`
25. Pin kolom Name
26. Klik `[Save]`
27. Scroll tabel T-TAG-02 secara horizontal
28. Verifikasi kolom Name tetap di posisinya saat scroll
29. Pulihkan ukuran viewport

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1418, TC-FA-TAG-1419, TC-FA-TAG-1420, TC-FA-TAG-1421). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column T-TAG-02 ada di spec 185 (TC-FA-TAG-1414 s.d. 1417) dan spec 186 (TC-FA-TAG-1418 s.d. 1421).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 9, 22, 29 (menyiapkan precondition TC-FA-TAG-1419 lewat Setup Column serta mempersempit dan memulihkan viewport).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 9, 15, 20, 26).
- Temuan untuk QA:
  - Popup Detail dibuka sekali di TC-FA-TAG-1418 dan tetap terbuka sampai akhir spec; langkah pembuka tidak diulang di TC berikutnya.
  - Precondition TC-FA-TAG-1419 (kolom Brand disembunyikan dan Measurement ditampilkan lalu disimpan) tidak diasersi; spec menyiapkannya lewat Setup Column di langkah penghubung.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
