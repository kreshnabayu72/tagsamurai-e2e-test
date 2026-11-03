---
id: TC-AC-ACAL-E2E-054-search-tab-user-action-substring-per-kolom-dan-kolom-hidden
title: "Search Tab User Action: Substring per Kolom dan Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-90
  - TC-AC-ACAL-93
coverage:
  web: automated
---

# Search Tab User Action: Substring per Kolom dan Kolom Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data log Tab User Action (contoh PRD §4.1.2; seed BE dibuat di hook `before` sebagai entri terbaru sehingga berada di halaman pertama; Name bersuffix `{runId}-054`, `{runId}` hanya digit):

  | Kode | Action | Object | Name | Field | Old Value | New Value | Modified By | Date |
  |---|---|---|---|---|---|---|---|---|
  | a | `Create` | `Distributor` | `PT Maju Bersama {runId}-054` | `Company Name` | `—` | `PT Maju Bersama {runId}-054` | ditetapkan tim FE | terbaru |
  | b | `Edit` | `Client` | `PT Sejahtera {runId}-054` | `PIC Name` | `Budi Santoso` | `Rina Putri` | ditetapkan tim FE | terbaru |
  | f | `Resend Activation Email` | `Distributor` | `Distributor Kirim Ulang {runId}-054` | `Email` | `—` | `admin@maju.com` | ditetapkan tim FE | terbaru |
  | g | `Cancel` | `Subscription` | `Langganan Batal {runId}-054` | `Status` | `Active` | `Archive` | ditetapkan tim FE | terbaru |
- Data uji TC-AC-ACAL-90 (kata kunci per kolom):

  | Kolom | Kata kunci | Baris yang tampil |
  |---|---|---|
  | Action | `resend` | baris f (Action `Resend Activation Email`) |
  | Object | `subscription` | baris g (Object `Subscription`) |
  | Name | `maju` | baris a (Name `PT Maju Bersama {runId}-054`) |
  | Field | `pic name` | baris b (Field `PIC Name`) |
  | Old Value | `budi` | baris b (Old Value `Budi Santoso`) |
  | New Value | `RINA` | baris b (New Value `Rina Putri`) |
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri User Action dengan Date dan nilai kolom pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan).
- State global yang diubah: visibilitas kolom `Old Value` (langkah 5 sampai 14) dipulihkan di langkah 12; preferensi kolom di browser dihapus di hook `after` (kemampuan disediakan tim FE, didaftarkan di `suite.md`). Entri User Action tidak dapat dihapus dan tetap ada sebagai snapshot.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action

### TC-AC-ACAL-90: Search substring dan tidak membedakan huruf besar kecil per kolom

2. Untuk setiap baris tabel Data uji TC-AC-ACAL-90 (langkah 2 sampai 4): ketik Search kata kunci kolom, tekan Enter
3. Verifikasi baris pada kolom "Baris yang tampil" tampil
4. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-93: Kolom yang di-hide tidak ikut dicari

5. Klik header `⋯`
6. Hilangkan centang kolom `Old Value` di Overlay Column Visibility
7. Verifikasi kolom `Old Value` hilang dari tabel
8. Tutup Overlay Column Visibility
9. Verifikasi baris b dengan Name `PT Sejahtera {runId}-054` tampil
10. Ketik Search `Budi Santoso`, tekan Enter
11. Verifikasi baris yang hanya cocok di Old Value (baris b) tidak tampil
12. Klik header `⋯`, ceklis kembali kolom `Old Value` di Overlay Column Visibility, lalu tutup Overlay Column Visibility
13. Tekan Enter pada kotak Search berisi `Budi Santoso`
14. Verifikasi baris b kembali ditemukan
15. Klik `✕` pada Search, tekan Enter

### Pemulihan state

16. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-90, 93; bagian 4b, Tab User Action). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengosongan Search (langkah 4, 15), penutupan Overlay Column Visibility (langkah 8 dan 12), pemulihan visibilitas kolom (langkah 12), dan penutupan Search di langkah 16 (hook `after` sebagai cadangan). Langkah 9 adalah anchor positif sebelum asersi absence.
- Langkah 2 sampai 4 berulang untuk setiap baris tabel Data uji TC-AC-ACAL-90 (enam iterasi, bagian 8b butir 7); dengan ekspansi perulangan spec memuat 31 langkah.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri User Action (Date, Modified By, Field, Old Value, New Value, nama tabel log internal) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
