---
id: TC-FA-TAG-E2E-180-tabel-grup-format-sel-badge-ikon-dan-severity-bagian-2
title: "Tabel Grup: Total Assets Menyertakan Aset Not Paired Yet (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-742
coverage:
  web: automated
---

# Tabel Grup: Total Assets Menyertakan Aset Not Paired Yet (Bagian 2)

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
| Isi grup 'Excavator 20 Ton' / Plant A | 18 aset ber-Tag dan 2 aset Not Paired Yet (Total Assets 20) | `isiPlantA` |

- State yang diubah dan pemulihannya: tidak ada perubahan data bisnis (aksi hanya membaca); data seed tambahan (bila ada) dihapus di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-742

1. Verifikasi Total Assets 20 pada baris Excavator 20 Ton / Plant A sama dengan 18 aset ber-Tag ditambah 2 aset Not Paired Yet (Not Paired Yet 2)
2. Klik Asset Name 'Excavator 20 Ton' pada baris Plant A
3. Atur page size tabel T-TAG-02 menjadi 25
4. Verifikasi Popup Detail memuat 20 baris tabel T-TAG-02
5. Verifikasi dua baris di antaranya adalah aset Not Paired Yet dengan TAG Code `—`
6. Tutup Popup Detail

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-742). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik format sel tabel grup ada di spec 179 (TC-FA-TAG-731 s.d. 741) dan spec 180 (TC-FA-TAG-742).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 6 (menutup Popup Detail di akhir spec).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-742 menyebut "page size 25" tanpa menyebut nama kontrol; spec menulis "atur page size tabel T-TAG-02 menjadi 25" tanpa mengarang label kontrol.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
