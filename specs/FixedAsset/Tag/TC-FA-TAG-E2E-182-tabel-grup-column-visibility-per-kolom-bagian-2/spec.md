---
id: TC-FA-TAG-E2E-182-tabel-grup-column-visibility-per-kolom-bagian-2
title: "Tabel Grup: Column Visibility per Kolom (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-748
  - TC-FA-TAG-749
  - TC-FA-TAG-750
  - TC-FA-TAG-751
coverage:
  web: automated
---

# Tabel Grup: Column Visibility per Kolom (Bagian 2)

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

- State yang diubah dan pemulihannya: konfigurasi kolom tabel grup di cache browser (tujuh kolom terakhir diubah menjadi satu kolom); penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom di browser lewat Column Visibility (langkah 2, 5, 9, 12, 16, 19, 23, 24, 25, 26, 27, 28), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-748

1. Klik header kolom terakhir `⋯` pada tabel grup
2. Hilangkan centang kolom Reported
3. Verifikasi kolom Reported tidak tampil pada tabel grup
4. Verifikasi perubahan langsung diterapkan tanpa tombol Save
5. Centang kembali kolom Reported
6. Verifikasi kolom Reported tampil kembali pada posisinya

### TC-FA-TAG-749

7. Tekan Esc untuk menutup overlay Column Visibility
8. Klik header kolom terakhir `⋯` pada tabel grup
9. Hilangkan centang kolom Non-standard
10. Verifikasi kolom Non-standard tidak tampil pada tabel grup
11. Verifikasi perubahan langsung diterapkan tanpa tombol Save
12. Centang kembali kolom Non-standard
13. Verifikasi kolom Non-standard tampil kembali pada posisinya

### TC-FA-TAG-750

14. Tekan Esc untuk menutup overlay Column Visibility
15. Klik header kolom terakhir `⋯` pada tabel grup
16. Hilangkan centang kolom Not Paired Yet
17. Verifikasi kolom Not Paired Yet tidak tampil pada tabel grup
18. Verifikasi perubahan langsung diterapkan tanpa tombol Save
19. Centang kembali kolom Not Paired Yet
20. Verifikasi kolom Not Paired Yet tampil kembali pada posisinya

### TC-FA-TAG-751

21. Tekan Esc untuk menutup overlay Column Visibility
22. Klik header kolom terakhir `⋯` pada tabel grup
23. Hilangkan centang kolom Group
24. Hilangkan centang kolom TAG Type
25. Hilangkan centang kolom Total Assets
26. Hilangkan centang kolom Reported
27. Hilangkan centang kolom Non-standard
28. Hilangkan centang kolom Not Paired Yet
29. Arahkan pointer ke checkbox kolom yang tersisa (Asset Name)
30. Verifikasi checkbox kolom Asset Name disabled (tetap tampil)
31. Verifikasi tooltip `At least one column must remain visible.` tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-748, TC-FA-TAG-749, TC-FA-TAG-750, TC-FA-TAG-751). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Column Visibility tabel grup ada di spec 181 (TC-FA-TAG-743 s.d. 747) dan spec 182 (TC-FA-TAG-748 s.d. 751).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 7, 14, 21 (menutup overlay Column Visibility dengan Esc sebelum TC berikutnya).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom di browser lewat Column Visibility (langkah 2, 5, 9, 12, 16, 19, 23, 24, 25, 26, 27, 28), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Langkah TC-FA-TAG-748 s.d. 751 dimulai dengan klik header `⋯`; overlay dari TC sebelumnya ditutup lebih dulu lewat Esc agar klik header membuka overlay.
  - TC-FA-TAG-751 tidak menyebut kolom mana yang tersisa; spec menyisakan `Asset Name` (enam kolom lain dihilangkan centangnya satu per satu).
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
