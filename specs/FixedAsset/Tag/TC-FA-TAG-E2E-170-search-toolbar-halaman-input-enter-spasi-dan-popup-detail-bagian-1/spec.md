---
id: TC-FA-TAG-E2E-170-search-toolbar-halaman-input-enter-spasi-dan-popup-detail-bagian-1
title: "Search Toolbar Halaman: Input, Enter, dan Spasi (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-680
  - TC-FA-TAG-681
  - TC-FA-TAG-682
  - TC-FA-TAG-683
  - TC-FA-TAG-684
  - TC-FA-TAG-685
coverage:
  web: automated
---

# Search Toolbar Halaman: Input, Enter, dan Spasi (Bagian 1)

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

## Test Steps

### TC-FA-TAG-680

1. Klik ikon Search pada Table Tools
2. Verifikasi input Search tampil dengan placeholder `Search TAG code, asset ID, asset name...`
3. Verifikasi ikon Search berubah menjadi ikon close/arrow

### TC-FA-TAG-681

4. Ketik `Forklift` di kotak Search tanpa menekan Enter
5. Verifikasi tabel grup masih memuat empat baris
6. Tekan Enter
7. Verifikasi hanya baris Forklift Manual / Plant A yang tampil

### TC-FA-TAG-682

8. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)
9. Ketik Search `  Forklift  ` (spasi di awal dan akhir), tekan Enter
10. Verifikasi hasil sama dengan kata kunci `Forklift`: hanya Forklift Manual / Plant A yang tampil
11. Verifikasi isi kotak Search tetap sama seperti yang diketik (`  Forklift  `)

### TC-FA-TAG-683

12. Ganti isi kotak Search dengan `Forklift`, tekan Enter
13. Ganti isi kotak Search dengan tiga spasi, tekan Enter
14. Verifikasi empat baris grup tampil kembali
15. Verifikasi tidak ada pesan yang tampil

### TC-FA-TAG-684

16. Ganti isi kotak Search dengan `fork`, tekan Enter
17. Verifikasi `fork` menemukan Forklift Manual / Plant A (substring, tidak membedakan huruf besar kecil)
18. Ganti isi kotak Search dengan `LIFT`, tekan Enter
19. Verifikasi `LIFT` menemukan Forklift Manual / Plant A (substring di tengah kata)

### TC-FA-TAG-685

20. Ganti isi kotak Search dengan `Laptop Pro`, tekan Enter
21. Verifikasi `Laptop Pro` menemukan Laptop Pro 14 / HQ
22. Ganti isi kotak Search dengan `Laptop  Pro` (dua spasi), tekan Enter
23. Verifikasi `No results found` tampil karena spasi di tengah kata kunci tidak disentuh
24. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-680, TC-FA-TAG-681, TC-FA-TAG-682, TC-FA-TAG-683, TC-FA-TAG-684, TC-FA-TAG-685). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Search toolbar halaman ada di spec 170 (TC-FA-TAG-680 s.d. 685) dan spec 171 (TC-FA-TAG-686 s.d. 691).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 8, 24 (menutup input Search dan mereset tabel sebelum TC-FA-TAG-682 dan di akhir spec).
- Temuan untuk QA:
  - TC-FA-TAG-682 mensyaratkan isi kotak Search "tetap sama seperti yang diketik" tanpa menyebut cara membacanya; spec membaca nilai input apa adanya (termasuk spasi di awal dan akhir).
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
