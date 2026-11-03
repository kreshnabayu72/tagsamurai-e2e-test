---
id: TC-FA-TAG-E2E-176-tabel-grup-search-per-kolom
title: "Tabel Grup: Search per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-712
  - TC-FA-TAG-713
  - TC-FA-TAG-714
  - TC-FA-TAG-715
  - TC-FA-TAG-716
  - TC-FA-TAG-717
  - TC-FA-TAG-718
  - TC-FA-TAG-719
coverage:
  web: automated
---

# Tabel Grup: Search per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Penyembunyian dan penampilan kembali kolom lewat Column Visibility (tersimpan di cache browser). Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |
| Grup tambahan Crane Hydraulic | 'Crane Hydraulic' / Plant A / RFID / Total Assets 40 / Reported 7 / Non-standard 0 / Not Paired Yet 9; dibuat di langkah penghubung sebelum TC-FA-TAG-715 | `grupCrane` |
| Data uji terkontrol (TC-FA-TAG-715 s.d. 718) | Asset ID, nama aset, dan TAG Code pada dataset tidak memuat kata kunci `25`, `7`, `3`, dan `9`; hanya satu nilai kolom angka yang memuat tiap kata kunci | `dataTerkontrol` |

- State yang diubah dan pemulihannya: grup 'Crane Hydraulic' dibuat sebelum TC-FA-TAG-715 dan dihapus di hook `after`; kolom Group disembunyikan di TC-FA-TAG-719 dan ditampilkan kembali oleh langkah penghubung.

## Test Steps

### TC-FA-TAG-712

1. Ketik Search `Forklift`, tekan Enter
2. Verifikasi hanya baris Forklift Manual / Plant A yang tampil

### TC-FA-TAG-713

3. Ganti isi kotak Search dengan `HQ`, tekan Enter
4. Verifikasi hanya baris Laptop Pro 14 / HQ yang tampil

### TC-FA-TAG-714

5. Ganti isi kotak Search dengan `NFC`, tekan Enter
6. Verifikasi hanya baris Laptop Pro 14 / HQ yang tampil
7. Buat grup tambahan 'Crane Hydraulic' lewat fixture backend hingga tersimpan, lalu muat ulang halaman

### TC-FA-TAG-715

8. Ketik Search `25`, tekan Enter
9. Verifikasi hanya baris Laptop Pro 14 / HQ (Total Assets 25) yang tampil
10. Verifikasi baris grup lain tidak tampil

### TC-FA-TAG-716

11. Ganti isi kotak Search dengan `7`, tekan Enter
12. Verifikasi hanya baris Crane Hydraulic / Plant A (Reported 7) yang tampil
13. Verifikasi baris grup lain tidak tampil

### TC-FA-TAG-717

14. Ganti isi kotak Search dengan `3`, tekan Enter
15. Verifikasi hanya baris Forklift Manual / Plant A (Non-standard 3) yang tampil
16. Verifikasi baris grup lain tidak tampil

### TC-FA-TAG-718

17. Ganti isi kotak Search dengan `9`, tekan Enter
18. Verifikasi hanya baris Crane Hydraulic / Plant A (Not Paired Yet 9) yang tampil
19. Verifikasi baris grup lain tidak tampil

### TC-FA-TAG-719

20. Klik header kolom terakhir `⋯` pada tabel grup
21. Hilangkan centang kolom Group
22. Ganti isi kotak Search dengan `HQ`, tekan Enter
23. Verifikasi `No results found` tampil karena kolom Group sedang disembunyikan
24. Klik header kolom terakhir `⋯` pada tabel grup, lalu centang kembali kolom Group
25. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-712, TC-FA-TAG-713, TC-FA-TAG-714, TC-FA-TAG-715, TC-FA-TAG-716, TC-FA-TAG-717, TC-FA-TAG-718, TC-FA-TAG-719). Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 7, 24, 25 (seeding grup Crane Hydraulic, memulihkan kolom Group, dan mereset input Search).
- Temuan untuk QA:
  - TC-FA-TAG-715 s.d. 718 mensyaratkan Asset ID, nama aset, dan TAG Code tidak memuat kata kunci (`25`, `7`, `3`, `9`), padahal dataset Pre-setup grup 'Excavator 20 Ton' memuat aset ber-ID AST-0011, AST-0020, AST-0021, AST-0043, AST-0044 (antara lain memuat digit `3`); spec menuntut dataset terkontrol dari tim FE sesuai TC dan tidak menyentuh data Pre-setup.
  - TC-FA-TAG-719 meninggalkan konfigurasi kolom di cache browser; spec 176 tidak ada dalam daftar pemulihan kolom di hook suite, sehingga pemulihan dilakukan lewat langkah penghubung (menampilkan kolom Group kembali).
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
