---
id: TC-AC-ACAL-E2E-055-search-dan-sort-kolom-description-tab-user-action
title: "Search dan Sort Kolom Description Tab User Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-185
coverage:
  web: automated
---

# Search dan Sort Kolom Description Tab User Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 15; nama literal menurut Lampiran A butir A-3 (S-12): data Pre-setup No 13 sampai 15 hanya dibaca, seeding idempotent): entri `Duplicate Approved` Object `Hardware` h1 (Name `SN-ZEBRA-FX9600-000108`, Description `Approved by Rina Wijaya (Total Control — requester)`) dan h2 (Name `SN-BULK-IX6-000009`, Modified By `System`, Description `Approved by system (no independent approver)`). Date h1 lebih baru daripada Date h2 (urutan seed ditetapkan tim FE).
- Data log Tab User Action (contoh PRD §4.1.2; seed BE dibuat di hook `before` sebagai entri terbaru sehingga berada di halaman pertama; Name bersuffix `{runId}-055`, `{runId}` hanya digit):

  | Kode | Action | Object | Name | Field | Old Value | New Value | Modified By | Date |
  |---|---|---|---|---|---|---|---|---|
  | a | `Create` | `Distributor` | `PT Maju Bersama {runId}-055` | `Company Name` | `—` | `PT Maju Bersama {runId}-055` | ditetapkan tim FE | terbaru |
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri User Action dengan Date, Modified By, dan nilai kolom pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan).
- State global: tidak ada yang diubah. Entri User Action tidak dapat dihapus dan tetap ada sebagai snapshot.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action

### TC-AC-ACAL-185: Search dan Sort kolom Description

2. Ketik Search `independent approver`, tekan Enter
3. Verifikasi hanya entri h2 dengan Description `Approved by system (no independent approver)` yang tampil (entri h1 tidak tampil)
4. Klik `✕` pada Search, tekan Enter
5. Verifikasi tabel kembali ke semua data (baris a dengan Name `PT Maju Bersama {runId}-055` tampil)
6. Ketik Search `REQUESTER`, tekan Enter
7. Verifikasi hanya entri h1 dengan Description `Approved by Rina Wijaya (Total Control — requester)` yang tampil (entri h2 tidak tampil)
8. Klik `✕` pada Search, tekan Enter
9. Verifikasi tabel kembali ke semua data (baris a tampil)
10. Ganti isi kotak search dengan `Approved by`, tekan Enter
11. Klik ikon sort Description
12. Verifikasi ikon sort Description `↑`
13. Verifikasi entri h1 (Description `Approved by Rina Wijaya (Total Control — requester)`) berada di atas entri h2 (Description `Approved by system (no independent approver)`)
14. Klik ikon sort Description lagi
15. Verifikasi ikon sort Description `↓`
16. Verifikasi entri h2 berada di atas entri h1
17. Klik ikon sort Description lagi
18. Verifikasi ikon sort Description netral
19. Verifikasi baris kembali berurutan Date terbaru di atas (entri h1 di atas entri h2)

### Pemulihan state

20. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-185; bagian 4b, Tab User Action). Tidak ada TC hanya-BE di spec ini. TC-AC-ACAL-185 mencakup Search dan Sort kolom Description sekaligus.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengosongan Search (langkah 4, 8), Search `Approved by` sebagai pembatas ke baris ber-Description sehingga urutan sort teramati pada halaman yang sama (langkah 10, S-14), dan penutupan Search di langkah 20 (hook `after` sebagai cadangan). Langkah 5 dan 9 adalah pembanding generik atau anchor positif sebelum asersi absence. Langkah 12, 15, dan 18 (ikon sort `↑`, `↓`, netral) adalah asersi tambahan di luar Expected e TC-AC-ACAL-185, yang hanya menyebut urutan baris; langkah 13, 16, dan 19 mengasersi urutan itu (S-03).
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri User Action (Date, Modified By, Field, Old Value, New Value, nama tabel log internal) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-185 tidak menyebut Date entri `Duplicate Approved`; asersi netral kembali Date terbaru di atas memakai asumsi Date h1 lebih baru daripada h2 (Prerequisites). Search `Approved by` pada langkah 10 adalah pembatas spec, bukan langkah TC.
