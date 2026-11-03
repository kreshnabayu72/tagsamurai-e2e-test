---
id: TC-FA-TAG-E2E-172-filter-panel-toolbar-halaman-apply-draft-dan-kombinasi-bagian-1
title: "Filter Panel Toolbar Halaman: Buka, Screening, Apply, dan Clear Field (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-692
  - TC-FA-TAG-693
  - TC-FA-TAG-694
  - TC-FA-TAG-695
  - TC-FA-TAG-696
coverage:
  web: automated
---

# Filter Panel Toolbar Halaman: Buka, Screening, Apply, dan Clear Field (Bagian 1)

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

### TC-FA-TAG-692

1. Klik ikon Filter pada Table Tools
2. Verifikasi Filter Panel tampil di bawah Table Tools
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi footer panel memuat `[Clear Field]` (kiri) dan `[Apply]` (kanan)

### TC-FA-TAG-693

5. Verifikasi field T-TAG-01 pada Filter Panel: `Asset Name` ("All asset names"), `Group` ("All groups", tombol Tree Picker), `Total Assets`, `Reported`, `Non-standard`, dan `Not Paired Yet` (masing-masing "Min" / "Max")
6. Verifikasi field T-TAG-02 pada Filter Panel: `TAG Type` ("All types"), `Brand` ("All brands"), `Model/Type` ("All models"), `Measurement` ("All units"), `Category` ("All categories", Tree Picker), `Label` ("All labels"), `Status` ("All statuses"), `Transactional Policy` ("All transactions"), `Last Scanned` ("Select date"), `Asset Value (Commercial)` dan `Asset Value (Fiscal)` ("Min" / "Max"), `Warranty Expiry` ("Select date"), `Last Updated` ("Select date"), dan satu field per Custom Field Active yang punya Filter
7. Verifikasi hanya ada satu field `TAG Type`; tipe pada Asset Name tidak menjadi field filter terpisah
8. Verifikasi field `Measurement`, `Category`, `Label`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry` tetap ada di Filter Panel walau kolom curated bersangkutan Hidden pada tabel

### TC-FA-TAG-694

9. Pilih TAG Type `NFC`
10. Klik `[Apply]`
11. Verifikasi tabel grup memuat Laptop Pro 14 / HQ (grup yang memuat baris detail dengan Tag bertipe NFC)
12. Verifikasi Excavator 20 Ton / Plant A tidak tampil
13. Klik Asset Name 'Laptop Pro 14' pada baris HQ
14. Verifikasi Popup Detail memuat sedikitnya satu baris dan setiap baris detail memiliki minimal satu Tag bertipe NFC
15. Tutup Popup Detail
16. Klik `[Clear Field]`
17. Klik `[Apply]`

### TC-FA-TAG-695

18. Pilih Asset Name 'Forklift Manual'
19. Verifikasi empat baris grup tetap tampil (filter belum diterapkan)
20. Klik `[Apply]`
21. Verifikasi hanya baris Forklift Manual / Plant A yang tampil
22. Verifikasi ikon Filter menampilkan badge titik indikator aktif

### TC-FA-TAG-696

23. Klik `[Clear Field]`
24. Klik `[Apply]`
25. Pilih Asset Name 'Forklift Manual'
26. Klik `[Apply]`
27. Verifikasi badge titik tampil pada ikon Filter
28. Klik `[Clear Field]`
29. Klik `[Apply]`
30. Verifikasi badge titik hilang dari ikon Filter
31. Verifikasi empat baris grup tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-692, TC-FA-TAG-693, TC-FA-TAG-694, TC-FA-TAG-695, TC-FA-TAG-696). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Filter Panel toolbar halaman ada di spec 172 (TC-FA-TAG-692 s.d. 696), spec 191 (TC-FA-TAG-697), dan spec 173 (TC-FA-TAG-698 s.d. 701).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 15, 16, 17, 23, 24 (menutup Popup Detail dan membersihkan filter (`[Clear Field]` lalu `[Apply]`) sebelum TC berikutnya mengandalkan tabel tanpa filter).
- Temuan untuk QA:
  - TC-FA-TAG-693 butir d ("Field tetap ada walau kolom curated Hidden pada tabel") tidak menyebut tabel mana dan cara mengamati status kolom curated; spec mengasersi keberadaan field tersebut dan tidak mengasersi status kolom pada tabel.
  - TC-FA-TAG-694 butir b memakai "setiap baris detail" tanpa jumlah baris pembanding; spec menambah pembanding generik "sedikitnya satu baris" sesuai kaidah asersi universal.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
