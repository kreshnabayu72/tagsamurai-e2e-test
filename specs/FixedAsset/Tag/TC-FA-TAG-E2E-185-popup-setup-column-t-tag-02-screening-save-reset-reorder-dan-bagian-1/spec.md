---
id: TC-FA-TAG-E2E-185-popup-setup-column-t-tag-02-screening-save-reset-reorder-dan-bagian-1
title: "Popup Setup Column T-TAG-02: Screening, Pratinjau, Save, dan Batal (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1414
  - TC-FA-TAG-1415
  - TC-FA-TAG-1416
  - TC-FA-TAG-1417
coverage:
  web: automated
---

# Popup Setup Column T-TAG-02: Screening, Pratinjau, Save, dan Batal (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Custom Field Active milik tenant (sedikitnya satu) untuk kolom curated tambahan. Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |
| Isi Popup Detail | Grup 'Excavator 20 Ton' / Plant B memuat 20 aset | `asetAcuanPlantB` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel T-TAG-02 di cache browser (kolom Model/Type disembunyikan dan disimpan di TC-FA-TAG-1416); penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 16).

## Test Steps

### TC-FA-TAG-1414

1. Klik Asset Name 'Excavator 20 Ton' pada baris Plant B untuk membuka Popup Detail
2. Klik header kolom terakhir `⋯` pada tabel T-TAG-02
3. Klik `Setup Column...`
4. Verifikasi Popup Setup Column memuat header: judul `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan ikon close
5. Verifikasi delapan kolom default tercentang (Name, Asset ID, TAG Code, Brand, Model/Type, Group, Status, Last Updated)
6. Verifikasi kolom curated tidak tercentang (Measurement, Category, Label, Transactional Policy, Last Scanned, Asset Value (Commercial), Asset Value (Fiscal), Warranty Expiry, dan satu kolom per Custom Field Active)
7. Verifikasi tiap kolom punya drag handle dan kontrol pin
8. Verifikasi footer memuat `[Reset to Default]` dan `[Save]`, tanpa `[Cancel]`

### TC-FA-TAG-1415

9. Hilangkan centang kolom Brand
10. Verifikasi tabel di balik popup langsung tidak menampilkan kolom Brand (pratinjau)
11. Verifikasi perubahan belum tersimpan sampai `[Save]` (popup masih terbuka dan `[Save]` belum diklik)

### TC-FA-TAG-1416

12. Klik ikon close pada Popup Setup Column (membuang perubahan TC sebelumnya)
13. Klik header kolom terakhir `⋯` pada tabel T-TAG-02
14. Klik `Setup Column...`
15. Hilangkan centang kolom Model/Type
16. Klik `[Save]`
17. Verifikasi Popup Setup Column tertutup
18. Verifikasi kolom Model/Type tidak tampil pada tabel T-TAG-02
19. Muat ulang halaman
20. Klik Asset Name 'Excavator 20 Ton' pada baris Plant B untuk membuka Popup Detail
21. Verifikasi kolom TAG Code tetap tampil pada tabel T-TAG-02
22. Verifikasi kolom Model/Type tetap tidak tampil pada tabel T-TAG-02 (cache browser)

### TC-FA-TAG-1417

23. Klik header kolom terakhir `⋯` pada tabel T-TAG-02
24. Klik `Setup Column...`
25. Hilangkan centang kolom Group
26. Klik ikon close pada Popup Setup Column
27. Verifikasi Popup Setup Column tertutup
28. Verifikasi kolom Group tetap tampil pada tabel T-TAG-02

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1414, TC-FA-TAG-1415, TC-FA-TAG-1416, TC-FA-TAG-1417). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column T-TAG-02 ada di spec 185 (TC-FA-TAG-1414 s.d. 1417) dan spec 186 (TC-FA-TAG-1418 s.d. 1421).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 12 (menutup popup dengan ikon close sebelum TC-FA-TAG-1416 agar draft TC-FA-TAG-1415 dibuang).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 16).
- Temuan untuk QA:
  - TC-FA-TAG-1414 dan TC-FA-TAG-1415 s.d. 1417 dibuka lewat Popup Detail yang sama; Popup Detail tetap terbuka antara TC-FA-TAG-1414 dan TC-FA-TAG-1417 kecuali dimuat ulang di TC-FA-TAG-1416, sehingga langkah pembuka Popup Detail tidak diulang di TC-FA-TAG-1415 dan TC-FA-TAG-1417.
  - TC-FA-TAG-1415 butir b ("Perubahan belum tersimpan sampai `[Save]`") tidak memberi cara mengamati keadaan belum tersimpan; spec mengasersi popup masih terbuka dan `[Save]` belum diklik.
  - TC-FA-TAG-1414 tidak menyebut jumlah Custom Field Active; spec mengasersi kolom curated sesuai daftar di TC.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
