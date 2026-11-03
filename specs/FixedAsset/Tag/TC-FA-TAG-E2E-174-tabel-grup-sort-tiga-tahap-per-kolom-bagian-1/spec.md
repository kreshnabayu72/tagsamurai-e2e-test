---
id: TC-FA-TAG-E2E-174-tabel-grup-sort-tiga-tahap-per-kolom-bagian-1
title: "Tabel Grup: Sort Tiga Tahap Kolom Asset Name, Group, TAG Type, Total Assets, dan Reported (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-702
  - TC-FA-TAG-703
  - TC-FA-TAG-704
  - TC-FA-TAG-705
  - TC-FA-TAG-706
coverage:
  web: automated
---

# Tabel Grup: Sort Tiga Tahap Kolom Asset Name, Group, TAG Type, Total Assets, dan Reported (Bagian 1)

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

- State yang diubah dan pemulihannya: tidak ada perubahan data bisnis (aksi hanya membaca); tiap TC berakhir pada klik ketiga sehingga sort kembali nonaktif.

## Test Steps

### TC-FA-TAG-702

1. Klik header kolom Asset Name
2. Verifikasi indikator naik aktif pada kolom Asset Name dan urutan: Excavator 20 Ton (Plant A, Plant B), Forklift Manual, Laptop Pro 14
3. Klik header kolom Asset Name sekali lagi
4. Verifikasi indikator turun aktif pada kolom Asset Name dan urutan: Laptop Pro 14, Forklift Manual, Excavator 20 Ton (dua baris)
5. Klik header kolom Asset Name sekali lagi
6. Verifikasi indikator sort nonaktif dan urutan kembali ke bawaan Asset Name A-Z

### TC-FA-TAG-703

7. Klik header kolom Group
8. Verifikasi indikator naik aktif pada kolom Group dan urutan: HQ (Laptop Pro 14), Plant A (Excavator 20 Ton lalu Forklift Manual), Plant B (Excavator 20 Ton)
9. Klik header kolom Group sekali lagi
10. Verifikasi indikator turun aktif pada kolom Group dan urutan: Plant B (Excavator 20 Ton), Plant A (Excavator 20 Ton lalu Forklift Manual), HQ (Laptop Pro 14)
11. Klik header kolom Group sekali lagi
12. Verifikasi indikator sort nonaktif dan urutan kembali ke bawaan Asset Name A-Z

### TC-FA-TAG-704

13. Klik header kolom TAG Type
14. Verifikasi indikator naik aktif pada kolom TAG Type dan urutan: NFC dan QR (Laptop Pro 14), Non TAG (Forklift Manual), RFID (Excavator 20 Ton dua baris)
15. Klik header kolom TAG Type sekali lagi
16. Verifikasi indikator turun aktif pada kolom TAG Type dan urutan: RFID (Excavator 20 Ton dua baris), Non TAG (Forklift Manual), NFC dan QR (Laptop Pro 14)
17. Klik header kolom TAG Type sekali lagi
18. Verifikasi indikator sort nonaktif dan urutan kembali ke bawaan Asset Name A-Z

### TC-FA-TAG-705

19. Klik header kolom Total Assets
20. Verifikasi indikator naik aktif pada kolom Total Assets dan urutan: Forklift Manual (10), Excavator 20 Ton (20, dua baris), Laptop Pro 14 (25)
21. Klik header kolom Total Assets sekali lagi
22. Verifikasi indikator turun aktif pada kolom Total Assets dan urutan: Laptop Pro 14 (25), Excavator 20 Ton (20, dua baris), Forklift Manual (10)
23. Klik header kolom Total Assets sekali lagi
24. Verifikasi indikator sort nonaktif dan urutan kembali ke bawaan Asset Name A-Z

### TC-FA-TAG-706

25. Klik header kolom Reported
26. Verifikasi indikator naik aktif pada kolom Reported dan urutan: Excavator 20 Ton / Plant A (0), Forklift Manual (0), Laptop Pro 14 (1), Excavator 20 Ton / Plant B (2)
27. Klik header kolom Reported sekali lagi
28. Verifikasi indikator turun aktif pada kolom Reported dan urutan: Excavator 20 Ton / Plant B (2), Laptop Pro 14 (1), Excavator 20 Ton / Plant A (0), Forklift Manual (0)
29. Klik header kolom Reported sekali lagi
30. Verifikasi indikator sort nonaktif dan urutan kembali ke bawaan Asset Name A-Z

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-702, TC-FA-TAG-703, TC-FA-TAG-704, TC-FA-TAG-705, TC-FA-TAG-706). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sort tiga tahap per kolom ada di spec 174 (TC-FA-TAG-702 s.d. 706) dan spec 175 (TC-FA-TAG-707 s.d. 711).
- Temuan untuk QA:
  - Expected tiap tahap sort pada TC-FA-TAG-702 s.d. 706 menggabungkan indikator sort dan urutan baris dalam satu butir; spec menulisnya sebagai satu Verifikasi per butir TC (indikator dan urutan dalam satu pernyataan).
  - TC-FA-TAG-706 menyebut dua baris dengan nilai Reported sama (0) tanpa aturan urutan kedua; spec mengikuti urutan yang tertulis di TC.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
