---
id: TC-AC-ACAL-E2E-028-isi-kolom-tab-user-action-pola-per-jenis-aksi
title: "Isi Kolom Tab User Action: Pola Per Jenis Aksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-88
coverage:
  web: automated
---

# Isi Kolom Tab User Action: Pola Per Jenis Aksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 15; seed BE, nilai literal, hanya dibaca dan tidak diubah; nama literal menurut Lampiran A butir A-3 (S-12): data Pre-setup No 13 sampai 15 hanya dibaca, seeding idempotent): entri `Duplicate Approved` Object `Hardware` Name `SN-ZEBRA-FX9600-000108` Field `Status` Old Value `—` New Value `Available` Modified By `Rina Wijaya` (tampil `Rina W`).
- Data log Tab User Action (contoh PRD §4.1.2; seed BE, Pre-setup No 10). Name entri bersuffix `{runId}-028` (`{runId}` hanya digit) supaya baris teramati unik; nilai Old Value dan New Value mengikuti TC:

  | Kode | Kata Search (Name) | Action | Object | Name | Field | Old Value | New Value | Plain text | Modified By |
  |---|---|---|---|---|---|---|---|---|---|
  | a | `PT Maju Bersama {runId}-028` | `Create` | `Distributor` | `PT Maju Bersama {runId}-028` | `Company Name` | `—` | `PT Maju Bersama {runId}-028` | `-` | `-` |
  | b | `PT Sejahtera {runId}-028` | `Edit` | `Client` | `PT Sejahtera {runId}-028` | `PIC Name` | `Budi Santoso` | `Rina Putri` | `-` | `-` |
  | c | `Acme {runId}-028` | `Delete` | `Brand` | `Acme {runId}-028` | `Brand Name` | `Acme {runId}-028` | `—` | `-` | `-` |
  | d | `Partner Suspend {runId}-028` | `Suspend` | `Partner` | `Partner Suspend {runId}-028` | `Status` | `Active` | `Suspended` | `-` | `-` |
  | e | `Partner Reassign {runId}-028` | `Reassign` | `Partner` | `Partner Reassign {runId}-028` | `Distributor` | `PT Maju Bersama` | `PT Global Tech` | `-` | `-` |
  | f | `Distributor Kirim Ulang {runId}-028` | `Resend Activation Email` | `Distributor` | `Distributor Kirim Ulang {runId}-028` | `Email` | `—` | `admin@maju.com` | `-` | `-` |
  | g | `Langganan Batal {runId}-028` | `Cancel` | `Subscription` | `Langganan Batal {runId}-028` | `Status` | `Active` | `Archive` | `v` | `-` |
  | h | `SN-ZEBRA-FX9600-000108` | `Duplicate Approved` | `Hardware` | `SN-ZEBRA-FX9600-000108` | `Status` | `—` | `Available` | `-` | `Rina W` |

  Kolom "Plain text" bertanda `v` berarti Action dan Object diasersi plain text (bukan badge); kolom "Modified By" bertanda `-` dilewati.
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri User Action dengan Action, Object, Name, Field, Old Value, dan New Value pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan); menelusuri halaman bila baris tidak berada di halaman pertama.
- Entri User Action tidak dapat dihapus dan tetap ada sebagai snapshot. Tidak ada state global yang diubah selain Search yang ditutup di akhir spec.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action

### TC-AC-ACAL-88: Isi kolom dan pola nilai per jenis aksi

2. Untuk setiap baris tabel Data log Tab User Action (langkah 2 sampai 6): ketik Search kata Search (Name), tekan Enter
3. Verifikasi baris entri menampilkan Action, Object, Name, Field, Old Value, dan New Value sesuai tabel
4. Verifikasi Action dan Object baris itu tampil sebagai plain text, bukan badge (baris bertanda `-` pada kolom "Plain text" dilewati)
5. Verifikasi Modified By baris itu tampil sesuai tabel (baris bertanda `-` pada kolom "Modified By" dilewati)
6. Klik `✕` pada Search, tekan Enter

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4b, Tab User Action). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search Name untuk menemukan baris entri di tabel audit trail yang tumbuh (langkah 2, S-14) dan pengosongan Search (langkah 6).
- Langkah 2 sampai 6 berulang untuk setiap baris tabel Data log Tab User Action (delapan iterasi, bagian 8b butir 7).
- Spec memiliki 6 langkah nominal dan 41 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (isi kolom Tab User Action pada akun dan dataset yang sama), dan ekspansi berasal dari satu perulangan per baris data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri User Action (contoh PRD §4.1.2) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-88 menulis Name literal (`PT Maju Bersama`, `PT Sejahtera`, `Acme`); spec memakai Name bersuffix `{runId}-028` (S-12), sehingga Name dan New Value baris a serta Old Value baris c ikut bersuffix.
  - TC-AC-ACAL-88 tidak menyebut Name dan Modified By baris d, e, f, g; spec memakai Name bersuffix sebagai pilihan spec dan tidak mengasersi Modified By selain baris h.
