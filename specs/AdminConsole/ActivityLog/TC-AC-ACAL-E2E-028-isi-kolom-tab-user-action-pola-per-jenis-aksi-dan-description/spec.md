---
id: TC-AC-ACAL-E2E-028-isi-kolom-tab-user-action-pola-per-jenis-aksi-dan-description
title: "Isi Kolom Tab User Action: Pola Per Jenis Aksi dan Kolom Description"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-88
  - TC-AC-ACAL-184
coverage:
  web: automated
---

# Isi Kolom Tab User Action: Pola Per Jenis Aksi dan Kolom Description

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 15; seed BE, nilai literal, hanya dibaca dan tidak diubah; nama literal menurut Lampiran A butir A-3 (S-12): data Pre-setup No 13 sampai 15 hanya dibaca, seeding idempotent): entri `Duplicate Approved` Object `Hardware` Name `SN-ZEBRA-FX9600-000108` Modified By `Rina Wijaya` (tampil `Rina W`) dengan Description `Approved by Rina Wijaya (Total Control — requester)`.
- Data log Tab User Action (contoh PRD §4.1.2; seed BE, Pre-setup No 10). Name entri bersuffix `{runId}-028` (`{runId}` hanya digit) supaya baris teramati unik; nilai Old Value dan New Value mengikuti TC:

  | Kode | Kata Search (Name) | Action | Object | Name | Field | Old Value | New Value | Description | Plain text | Modified By |
  |---|---|---|---|---|---|---|---|---|---|---|
  | a | `PT Maju Bersama {runId}-028` | `Create` | `Distributor` | `PT Maju Bersama {runId}-028` | `Company Name` | `—` | `PT Maju Bersama {runId}-028` | `—` | `-` | `-` |
  | b | `PT Sejahtera {runId}-028` | `Edit` | `Client` | `PT Sejahtera {runId}-028` | `PIC Name` | `Budi Santoso` | `Rina Putri` | `—` | `-` | `-` |
  | c | `Acme {runId}-028` | `Delete` | `Brand` | `Acme {runId}-028` | `Brand Name` | `Acme {runId}-028` | `—` | `—` | `-` | `-` |
  | d | `Partner Suspend {runId}-028` | `Suspend` | `Partner` | `Partner Suspend {runId}-028` | `Status` | `Active` | `Suspended` | `—` | `-` | `-` |
  | e | `Partner Reassign {runId}-028` | `Reassign` | `Partner` | `Partner Reassign {runId}-028` | `Distributor` | `PT Maju Bersama` | `PT Global Tech` | `—` | `-` | `-` |
  | f | `Distributor Kirim Ulang {runId}-028` | `Resend Activation Email` | `Distributor` | `Distributor Kirim Ulang {runId}-028` | `Email` | `—` | `admin@maju.com` | `—` | `-` | `-` |
  | g | `Langganan Batal {runId}-028` | `Cancel` | `Subscription` | `Langganan Batal {runId}-028` | `Status` | `Active` | `Archive` | `—` | `v` | `-` |
  | h | `SN-ZEBRA-FX9600-000108` | `Duplicate Approved` | `Hardware` | `SN-ZEBRA-FX9600-000108` | `Status` | `—` | `Available` | `Approved by Rina Wijaya (Total Control — requester)` | `-` | `Rina W` |

  Kolom "Plain text" bertanda `v` berarti Action dan Object diasersi plain text (bukan badge); kolom "Modified By" bertanda `-` dilewati.
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri User Action dengan Action, Object, Name, Field, Old Value, New Value, dan Description pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan); menelusuri halaman bila baris tidak berada di halaman pertama.
- Entri User Action tidak dapat dihapus dan tetap ada sebagai snapshot. Tidak ada state global yang diubah selain Search yang ditutup di akhir spec.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action

### TC-AC-ACAL-88: Isi kolom dan pola nilai per jenis aksi

2. Untuk setiap baris tabel Data log Tab User Action (langkah 2 sampai 6): ketik Search kata Search (Name), tekan Enter
3. Verifikasi baris entri menampilkan Action, Object, Name, Field, Old Value, New Value, dan Description sesuai tabel
4. Verifikasi Action dan Object baris itu tampil sebagai plain text, bukan badge (baris bertanda `-` pada kolom "Plain text" dilewati)
5. Verifikasi Modified By baris itu tampil sesuai tabel (baris bertanda `-` pada kolom "Modified By" dilewati)
6. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-184: Kolom Description

7. Verifikasi kolom `Description` berada setelah kolom `New Value` dan sebelum kolom `Modified By`
8. Ketik Search `SN-ZEBRA-FX9600-000108`, tekan Enter
9. Verifikasi sel Description entri `Duplicate Approved` menampilkan `Approved by Rina Wijaya (Total Control — requester)` apa adanya sebagai plain text
10. Ganti isi kotak search dengan `PT Sejahtera {runId}-028`, tekan Enter
11. Verifikasi sel Description entri `Edit` Client tampil `—`
12. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel
13. Klik icon Filter
14. Verifikasi panel Filter tampil dengan field `Action`
15. Verifikasi Filter Panel tidak memiliki field Description
16. Tutup Filter Panel tanpa [Apply] dengan klik icon Filter

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4b, Tab User Action). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search Name untuk menemukan baris entri di tabel audit trail yang tumbuh (langkah 2, 8, 10, S-14), pengosongan Search (langkah 6), penutupan Search (langkah 12), dan penutupan Filter Panel tanpa [Apply] (langkah 16, supaya spec tidak berakhir dengan Filter Panel terbuka; S-03). Langkah 14 adalah anchor positif (field lain tampil) untuk asersi absence field Description.
- Langkah 2 sampai 6 berulang untuk setiap baris tabel Data log Tab User Action (delapan iterasi, bagian 8b butir 7).
- Spec memiliki 16 langkah nominal dan 51 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (isi kolom Tab User Action pada akun dan dataset yang sama), kedua TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari satu perulangan per baris data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri User Action (contoh PRD §4.1.2) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-88 menulis Name literal (`PT Maju Bersama`, `PT Sejahtera`, `Acme`); spec memakai Name bersuffix `{runId}-028` (S-12), sehingga Name dan New Value baris a serta Old Value baris c ikut bersuffix.
  - TC-AC-ACAL-88 tidak menyebut Name dan Modified By baris d, e, f, g; spec memakai Name bersuffix sebagai pilihan spec dan tidak mengasersi Modified By selain baris h.
  - Kolom Description baris a sampai g tampil `—` (TC-AC-ACAL-88 Expected h) tumpang tindih dengan TC-AC-ACAL-184 Expected b; spec mengasersinya di kedua TC.
