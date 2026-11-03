---
id: TC-AC-ACAL-E2E-029-search-tab-user-action-siklus-kotak-modified-by-kolom-date-dan-nilai-di-luar-kolom
title: "Search Tab User Action: Siklus Kotak, Modified By, Kolom Date, dan Nilai di Luar Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-89
  - TC-AC-ACAL-91
  - TC-AC-ACAL-92
  - TC-AC-ACAL-94
coverage:
  web: automated
---

# Search Tab User Action: Siklus Kotak, Modified By, Kolom Date, dan Nilai di Luar Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 12; nama literal menurut Lampiran A butir A-3, seeding idempotent, tidak dihapus, hanya dibaca): akun `Hendra Pratama` (tampil `Hendra P`) sebagai pelaku entri i.
- Data log Tab User Action (contoh PRD §4.1.2; seed BE dibuat di hook `before` sebagai entri terbaru sehingga berada di halaman pertama; Name bersuffix `{runId}-029`, `{runId}` hanya digit):

  | Kode | Action | Object | Name | Field | Old Value | New Value | Modified By | Date |
  |---|---|---|---|---|---|---|---|---|
  | d | `Suspend` | `Partner` | `Partner Suspend {runId}-029` | `Status` | `Active` | `Suspended` | ditetapkan tim FE | terbaru |
  | f | `Resend Activation Email` | `Distributor` | `Distributor Kirim Ulang {runId}-029` | `Email` | `—` | `admin@maju.com` | ditetapkan tim FE | terbaru |
  | i | `Edit` | `Client` | `Klien Hendra {runId}-029` | `PIC Name` | `Sari Dewi` | `Sari Dewanti` | `Hendra Pratama` | terbaru |
  | j | `Edit` | `Client` | `Klien Tanggal {runId}-029` | `PIC Name` | `Sari Dewi` | `Sari Dewanti` | ditetapkan tim FE | `18 Jun 2026` (zona waktu tampilan General Settings) |
  | k | `Edit` | `Brand` | `Brand Log {runId}-029` | `Brand Name` | `Alfa` | `Beta` | ditetapkan tim FE | terbaru; nama tabel log internal `brand_logs` |

  Entri j dan k dipakai sebagai precondition TC, tidak diasersi pada langkah mana pun.

  Nilai `brand_logs` bukan substring Action, Object, Name, Field, Old Value, New Value, Description, atau Modified By entri mana pun.
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri User Action dengan Date, Modified By, dan nilai kolom pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan).
- State global: tidak ada yang diubah. Entri User Action tidak dapat dihapus dan tetap ada sebagai snapshot.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action

### TC-AC-ACAL-89: Siklus kotak Search

2. Verifikasi tabel menampilkan sedikitnya satu baris
3. Klik icon Search
4. Verifikasi input Search terbuka
5. Verifikasi kursor fokus di input Search
6. Verifikasi placeholder input Search `Search user action log...`
7. Ketik `Partner` di kotak Search tanpa menekan Enter
8. Verifikasi icon `✕` muncul di kotak Search
9. Verifikasi tabel belum tersaring (baris f dengan Name `Distributor Kirim Ulang {runId}-029` masih tampil)
10. Tekan Enter
11. Verifikasi tabel tersaring (baris d dengan Name `Partner Suspend {runId}-029` tampil dan baris f tidak tampil)
12. Klik `✕` pada kotak Search
13. Verifikasi input Search kosong
14. Verifikasi tabel tetap hasil `Partner` (baris f tidak tampil)
15. Tekan Enter pada input kosong
16. Verifikasi tabel kembali ke semua data (baris d dan baris f tampil)
17. Klik `←` pada kotak Search
18. Verifikasi input Search tertutup
19. Verifikasi tabel langsung kembali ke semua data (baris d dan baris f tampil)

### TC-AC-ACAL-91: Search Modified By mencocokkan nama lengkap

20. Ketik Search `pratama`, tekan Enter
21. Verifikasi baris i (Modified By `Hendra P`) ditemukan
22. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-92: Kolom Date tidak dapat dicari

23. Ketik Search `18 Jun 2026`, tekan Enter
24. Verifikasi tampil `No results found`
25. Klik `✕` pada Search, tekan Enter

### TC-AC-ACAL-94: Search tidak mencocokkan nilai di luar kolom tabel

26. Ketik Search `brand_logs`, tekan Enter
27. Verifikasi tampil `No results found`
28. Klik `✕` pada Search, tekan Enter

### Pemulihan state

29. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-89, 91, 92, 94; bagian 4b, Tab User Action). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengosongan Search (langkah 22, 25, 28) dan penutupan Search di langkah 29 (hook `after` sebagai cadangan). Langkah 2 adalah pembanding generik sebelum asersi.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri User Action (Date, Modified By, Field, Old Value, New Value, nama tabel log internal) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-92 mensyaratkan entri bertanggal `18 Jun 2026`, tanggal yang sama dengan data Filter Date TC-AC-ACAL-98/99 (spec 034); entri seed spec ini dapat muncul pada hasil Filter Date `18 Jun 2026` spec lain dan tidak dapat dihapus. Asersi "hanya" di spec Filter Date sebaiknya dibatasi User atau Name.
  - TC-AC-ACAL-91 menamai pelaku `Hendra Pratama` tanpa menyebut entri yang dikerjakannya; spec memakai entri i milik spec.
