---
id: TC-FA-TAG-E2E-177-tabel-grup-filter-per-kolom-dan-tree-picker-group-bagian-1
title: "Tabel Grup: Filter per Kolom Asset Name, Total Assets, Reported, Non-standard, dan Not Paired Yet (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-720
  - TC-FA-TAG-721
  - TC-FA-TAG-722
  - TC-FA-TAG-723
  - TC-FA-TAG-724
  - TC-FA-TAG-725
  - TC-FA-TAG-726
coverage:
  web: automated
---

# Tabel Grup: Filter per Kolom Asset Name, Total Assets, Reported, Non-standard, dan Not Paired Yet (Bagian 1)

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

- State yang diubah dan pemulihannya: tidak ada perubahan data bisnis (aksi hanya membaca); data seed tambahan (bila ada) dihapus di hook `after`. Spec berakhir dengan filter dari TC-FA-TAG-725 masih diterapkan; halaman dibuka ulang oleh hook `beforeEach` suite pada spec berikutnya.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-720

1. Klik ikon Filter
2. Klik field `Asset Name` ("All asset names")
3. Pilih 'Forklift Manual'
4. Klik `[Apply]`
5. Verifikasi hanya baris Forklift Manual / Plant A yang tampil

### TC-FA-TAG-721

6. Klik `[Clear Field]`
7. Isi Total Assets Min `20`
8. Isi Total Assets Max `25`
9. Klik `[Apply]`
10. Verifikasi Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, dan Laptop Pro 14 / HQ tampil
11. Verifikasi Forklift Manual (Total Assets 10) tidak tampil

### TC-FA-TAG-722

12. Klik `[Clear Field]`
13. Isi Reported Min `1`
14. Klik `[Apply]`
15. Verifikasi Excavator 20 Ton / Plant B (2) dan Laptop Pro 14 / HQ (1) tampil

### TC-FA-TAG-723

16. Klik `[Clear Field]`
17. Isi Non-standard Min `3`
18. Isi Non-standard Max `5`
19. Klik `[Apply]`
20. Verifikasi Excavator 20 Ton / Plant B (5) dan Forklift Manual / Plant A (3) tampil

### TC-FA-TAG-724

21. Klik `[Clear Field]`
22. Isi Not Paired Yet Max `0`
23. Klik `[Apply]`
24. Verifikasi Excavator 20 Ton / Plant B dan Forklift Manual / Plant A tampil

### TC-FA-TAG-725

25. Klik `[Clear Field]`
26. Pilih Asset Name 'Forklift Manual' dan 'Laptop Pro 14'
27. Klik `[Apply]`
28. Verifikasi Forklift Manual / Plant A dan Laptop Pro 14 / HQ tampil

### TC-FA-TAG-726

29. Klik `[Clear Field]`
30. Klik field `Asset Name`
31. Ketik `Lap` pada kotak cari opsi
32. Verifikasi `Lap` menyisakan opsi `Laptop Pro 14`
33. Ganti isi kotak cari opsi dengan `zzzz`
34. Verifikasi teks `No results found` tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-720, TC-FA-TAG-721, TC-FA-TAG-722, TC-FA-TAG-723, TC-FA-TAG-724, TC-FA-TAG-725, TC-FA-TAG-726). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Filter per kolom dan Tree Picker Group ada di spec 177 (TC-FA-TAG-720 s.d. 726) dan spec 178 (TC-FA-TAG-727 s.d. 730).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 6, 12, 16, 21, 25, 29 (membersihkan draft Filter Panel dengan `[Clear Field]` antar TC (filter lama tertimpa saat `[Apply]` berikutnya)).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-724 hanya mengisi Max `0` (tanpa Min); spec mengikuti langkah TC.
  - TC-FA-TAG-726 tidak menyebut apakah Filter Panel dalam keadaan bersih; spec membersihkan draft dengan `[Clear Field]` sebelum TC itu (langkah penghubung) dan tidak menerapkan filter dari TC itu.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
