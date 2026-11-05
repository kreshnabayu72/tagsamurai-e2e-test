---
id: TC-FA-TAG-E2E-183-tabel-grup-popup-setup-column-save-reset-reorder-dan-pin-bagian-1
title: "Tabel Grup: Popup Setup Column, Screening, Pratinjau, Save, dan Batal (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-752
  - TC-FA-TAG-753
  - TC-FA-TAG-754
  - TC-FA-TAG-755
  - TC-FA-TAG-756
coverage:
  web: automated
---

# Tabel Grup: Popup Setup Column, Screening, Pratinjau, Save, dan Batal (Bagian 1)

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

- State yang diubah dan pemulihannya: konfigurasi kolom tabel grup di cache browser (kolom Not Paired Yet disembunyikan dan disimpan di TC-FA-TAG-754); penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 10).

## Test Steps

### TC-FA-TAG-752

1. Klik header kolom terakhir `⋯` pada tabel grup
2. Klik `Setup Column...`
3. Verifikasi Popup Setup Column memuat header: judul `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan ikon close
4. Verifikasi body Popup Setup Column memuat tujuh kolom dengan checkbox tercentang, drag handle, dan kontrol pin
5. Verifikasi tidak ada kolom curated pada body Popup Setup Column
6. Verifikasi footer Popup Setup Column memuat `[Reset to Default]` dan `[Save]`, tanpa `[Cancel]`

### TC-FA-TAG-753

7. Hilangkan centang kolom Not Paired Yet
8. Verifikasi tabel di balik popup langsung tidak menampilkan kolom Not Paired Yet (pratinjau)
9. Verifikasi perubahan belum tersimpan sampai `[Save]` (popup masih terbuka dan `[Save]` belum diklik)

### TC-FA-TAG-754

10. Klik `[Save]`
11. Verifikasi Popup Setup Column tertutup
12. Muat ulang halaman
13. Verifikasi kolom Asset Name tetap tampil setelah muat ulang
14. Verifikasi kolom Not Paired Yet tidak tampil setelah muat ulang (cache browser)

### TC-FA-TAG-755

15. Klik header kolom terakhir `⋯` pada tabel grup
16. Klik `Setup Column...`
17. Hilangkan centang kolom Reported
18. Klik ikon close pada Popup Setup Column
19. Verifikasi Popup Setup Column tertutup
20. Verifikasi kolom Reported tetap tampil

### TC-FA-TAG-756

21. Klik header kolom terakhir `⋯` pada tabel grup
22. Klik `Setup Column...`
23. Hilangkan centang kolom Reported
24. Tekan Esc
25. Verifikasi Popup Setup Column tertutup
26. Verifikasi kolom Reported tetap tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-752, TC-FA-TAG-753, TC-FA-TAG-754, TC-FA-TAG-755, TC-FA-TAG-756). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column tabel grup ada di spec 183 (TC-FA-TAG-752 s.d. 756), spec 192 (TC-FA-TAG-757), dan spec 184 (TC-FA-TAG-758 s.d. 759).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 10).
- Temuan untuk QA:
  - TC-FA-TAG-753 dan TC-FA-TAG-754 dimulai dengan aksi yang sama (membuka Setup Column dan menghilangkan centang Not Paired Yet); `[Save]` TC-FA-TAG-754 dilakukan pada popup yang sama dengan pratinjau TC-FA-TAG-753 tanpa membukanya ulang.
  - TC-FA-TAG-753 butir b ("Belum tersimpan sampai `[Save]`") tidak memberi cara mengamati keadaan belum tersimpan; spec mengasersi popup masih terbuka dan `[Save]` belum diklik.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
