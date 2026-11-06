---
id: TC-FA-TAG-E2E-191-filter-panel-toolbar-halaman-tutup-tanpa-apply-membuang-draft
title: "Filter Panel Toolbar Halaman: Menutup Panel tanpa Apply Membuang Draft"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-697
coverage:
  web: automated
---

# Filter Panel Toolbar Halaman: Menutup Panel tanpa Apply Membuang Draft

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |

- State yang diubah dan pemulihannya: tidak ada perubahan data bisnis (aksi hanya membaca); data seed tambahan (bila ada) dihapus di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-697

1. Klik ikon Filter
2. Pilih Asset Name 'Forklift Manual' tanpa Apply
3. Klik ikon Filter lagi untuk menutup panel
4. Klik ikon Filter lagi untuk membuka panel
5. Verifikasi field Asset Name kosong
6. Verifikasi tabel tetap memuat empat baris grup

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-697). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Filter Panel toolbar halaman ada di spec 172 (TC-FA-TAG-692 s.d. 696), spec 191 (TC-FA-TAG-697), dan spec 173 (TC-FA-TAG-698 s.d. 701).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
