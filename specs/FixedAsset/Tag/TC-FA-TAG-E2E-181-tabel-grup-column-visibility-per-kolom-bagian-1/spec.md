---
id: TC-FA-TAG-E2E-181-tabel-grup-column-visibility-per-kolom-bagian-1
title: "Tabel Grup: Column Visibility per Kolom (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-743
  - TC-FA-TAG-744
  - TC-FA-TAG-745
  - TC-FA-TAG-746
  - TC-FA-TAG-747
coverage:
  web: automated
---

# Tabel Grup: Column Visibility per Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel grup di cache browser; penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini.

## Test Steps

### TC-FA-TAG-743

1. Klik header kolom terakhir `⋯` pada tabel grup
2. Verifikasi overlay Column Visibility menampilkan tujuh kolom dengan checkbox tercentang: Asset Name, Group, TAG Type, Total Assets, Reported, Non-standard, Not Paired Yet
3. Verifikasi tiap kolom pada overlay dapat di-reorder (drag and drop)
4. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-FA-TAG-744

5. Tekan Esc untuk menutup overlay Column Visibility
6. Klik header kolom terakhir `⋯` pada tabel grup
7. Hilangkan centang kolom Asset Name
8. Verifikasi kolom Asset Name tidak tampil pada tabel grup
9. Verifikasi perubahan langsung diterapkan tanpa tombol Save
10. Centang kembali kolom Asset Name
11. Verifikasi kolom Asset Name tampil kembali pada posisinya

### TC-FA-TAG-745

12. Tekan Esc untuk menutup overlay Column Visibility
13. Klik header kolom terakhir `⋯` pada tabel grup
14. Hilangkan centang kolom Group
15. Verifikasi kolom Group tidak tampil pada tabel grup
16. Verifikasi perubahan langsung diterapkan tanpa tombol Save
17. Centang kembali kolom Group
18. Verifikasi kolom Group tampil kembali pada posisinya

### TC-FA-TAG-746

19. Tekan Esc untuk menutup overlay Column Visibility
20. Klik header kolom terakhir `⋯` pada tabel grup
21. Hilangkan centang kolom TAG Type
22. Verifikasi kolom TAG Type tidak tampil pada tabel grup
23. Verifikasi perubahan langsung diterapkan tanpa tombol Save
24. Centang kembali kolom TAG Type
25. Verifikasi kolom TAG Type tampil kembali pada posisinya

### TC-FA-TAG-747

26. Tekan Esc untuk menutup overlay Column Visibility
27. Klik header kolom terakhir `⋯` pada tabel grup
28. Hilangkan centang kolom Total Assets
29. Verifikasi kolom Total Assets tidak tampil pada tabel grup
30. Verifikasi perubahan langsung diterapkan tanpa tombol Save
31. Centang kembali kolom Total Assets
32. Verifikasi kolom Total Assets tampil kembali pada posisinya

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-743, TC-FA-TAG-744, TC-FA-TAG-745, TC-FA-TAG-746, TC-FA-TAG-747). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Column Visibility tabel grup ada di spec 181 (TC-FA-TAG-743 s.d. 747) dan spec 182 (TC-FA-TAG-748 s.d. 751).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 5, 12, 19, 26 (menutup overlay Column Visibility dengan Esc sebelum TC berikutnya).
- Temuan untuk QA:
  - Langkah TC-FA-TAG-744 s.d. 747 dimulai dengan klik header `⋯`; overlay dari TC sebelumnya ditutup lebih dulu lewat Esc agar klik header membuka overlay (bukan menutupnya).
  - TC-FA-TAG-744 s.d. 747 menulis "perubahan langsung diterapkan tanpa tombol Save" tanpa cara mengamati; spec mengasersi bahwa overlay tidak memiliki tombol Save.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
