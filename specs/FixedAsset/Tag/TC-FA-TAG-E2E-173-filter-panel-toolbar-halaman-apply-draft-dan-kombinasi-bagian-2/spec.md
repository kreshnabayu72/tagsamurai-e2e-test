---
id: TC-FA-TAG-E2E-173-filter-panel-toolbar-halaman-apply-draft-dan-kombinasi-bagian-2
title: "Filter Panel Toolbar Halaman: Halaman 1 dan Kombinasi Search, Filter, Sort (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-698
  - TC-FA-TAG-699
  - TC-FA-TAG-700
  - TC-FA-TAG-701
coverage:
  web: automated
---

# Filter Panel Toolbar Halaman: Halaman 1 dan Kombinasi Search, Filter, Sort (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Grup tambahan milik spec untuk TC-FA-TAG-698 (delapan grup di luar dataset sehingga tabel grup lebih dari 10 baris). Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |
| Grup tambahan TC-FA-TAG-698 | Delapan grup tambahan milik spec, nama tidak memuat `Excavator`, `Forklift`, `Laptop`, atau `Ton`, bersuffix `{runId}-173-<n>`; dibuat sebelum TC-FA-TAG-698 dan dihapus sebelum TC-FA-TAG-699 | `grupTambahan173` |

- State yang diubah dan pemulihannya: grup tambahan dibuat sebelum TC-FA-TAG-698 dan dihapus sesudahnya; hook `after` menghapusnya bila masih ada.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1, 9) yang menyiapkan atau memulihkan state.

## Test Steps

### TC-FA-TAG-698

1. Buat delapan grup tambahan lewat fixture backend hingga tersimpan, lalu muat ulang halaman
2. Verifikasi paginasi tabel grup memuat lebih dari satu halaman
3. Pindah ke halaman 2
4. Verifikasi tabel grup menampilkan halaman 2
5. Klik ikon Filter
6. Pilih Asset Name 'Excavator 20 Ton'
7. Klik `[Apply]`
8. Verifikasi tabel menampilkan halaman 1 dari hasil filter
9. Hapus delapan grup tambahan lewat fixture backend hingga tersimpan, lalu klik menu Fixed Asset > TAG di sidebar (mereset Search, Sort, dan Filter)

### TC-FA-TAG-699

10. Ketik Search `Excavator`, tekan Enter
11. Klik ikon Filter
12. Isi Reported Min `1`
13. Klik `[Apply]`
14. Verifikasi hanya baris Excavator 20 Ton / Plant B yang tampil (cocok dengan Search dan Reported >= 1)

### TC-FA-TAG-700

15. Klik menu Fixed Asset > TAG di sidebar (mereset Search, Sort, dan Filter)
16. Ketik Search `Excavator`, tekan Enter
17. Klik ikon Filter
18. Isi Reported Min `5`
19. Klik `[Apply]`
20. Verifikasi `No results found` tampil
21. Klik `[Clear Field]`
22. Klik `[Apply]`
23. Verifikasi dua baris Excavator 20 Ton tampil (Search masih aktif)

### TC-FA-TAG-701

24. Klik menu Fixed Asset > TAG di sidebar (mereset Search, Sort, dan Filter)
25. Ketik Search `Ton`, tekan Enter
26. Klik header kolom Non-standard
27. Verifikasi baris hasil Search terurut Non-standard menaik (Excavator 20 Ton / Plant A 0, Excavator 20 Ton / Plant B 5)
28. Klik header kolom Non-standard sekali lagi
29. Verifikasi baris hasil Search terurut Non-standard menurun (Excavator 20 Ton / Plant B 5, Excavator 20 Ton / Plant A 0)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-698, TC-FA-TAG-699, TC-FA-TAG-700, TC-FA-TAG-701). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Filter Panel toolbar halaman ada di spec 172 (TC-FA-TAG-692 s.d. 696), spec 191 (TC-FA-TAG-697), dan spec 173 (TC-FA-TAG-698 s.d. 701).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 1, 9, 15, 24 (seeding dan penghapusan grup tambahan serta pembukaan menu Fixed Asset > TAG di sidebar untuk mereset Search, Sort, dan Filter).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1, 9) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - Judul TC-FA-TAG-701 menyebut kombinasi Search, Filter, dan Sort, tetapi langkah dan Expected-nya hanya memakai Search dan Sort; spec mengikuti langkah TC.
  - TC-FA-TAG-698 mensyaratkan lebih dari 10 baris grup, sedangkan TC lain di spec ini menegaskan jumlah baris dataset; grup tambahan dibuat hanya untuk TC-FA-TAG-698. Jumlah grup tambahan dan cara pembuatannya tidak disebut TC.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
