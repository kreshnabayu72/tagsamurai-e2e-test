---
id: TC-AC-ACAL-E2E-031-sort-tab-user-action-kolom-modified-by-dan-tipe-campuran
title: "Sort Tab User Action: Kolom, Modified By, dan Tipe Campuran"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-100
  - TC-AC-ACAL-101
  - TC-AC-ACAL-102
  - TC-AC-ACAL-103
coverage:
  web: automated
---

# Sort Tab User Action: Kolom, Modified By, dan Tipe Campuran

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 12; nama literal menurut Lampiran A butir A-3, seeding idempotent, tidak dihapus): akun admin `Dewi Lestari` dan `Dewi Larasati` (keduanya tampil `Dewi L`) sebagai pelaku entri. Tidak ada Data Dinamis.
- Data log Tab User Action (seed BE; Date berada pada satu hari yang ditetapkan tim FE, bukan 17 sampai 20 Jun 2026 yang dipakai data Filter Date; Name bersuffix `{runId}-031`, `{runId}` hanya digit). Sedikitnya dua nilai distinct tiap kolom diasersi (S-11):

  | Kode | Waktu | Action | Object | Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|---|---|
  | r1 | `09:00` | `Create` | `Distributor` | `Alfa {runId}-031` | `Company Name` | `100` | `5` | `Dewi Lestari` |
  | r2 | `10:00` | `Edit` | `Client` | `Beta {runId}-031` | `PIC Name` | `25` | `40` | `Dewi Larasati` |
  | r3 | `11:00` | `Delete` | `Brand` | `Cemara {runId}-031` | `Brand Name` | `Active` | `Suspended` | `Dewi Lestari` |
  | r4 | `12:00` | `Suspend` | `Partner` | `Delta {runId}-031` | `Status` | `budi` | `archive` | `Dewi Larasati` |
  | r5 | `13:00` | `Cancel` | `Subscription` | `Epsilon {runId}-031` | `Plan` | `—` | `—` | `Dewi Lestari` |

- Urutan relatif baris r1 sampai r5 diasersi (bukan posisi mutlak) karena tabel audit trail memuat entri dari run dan spec lain. Urutan default (netral) baris seed adalah Date terbaru di atas: r5, r4, r3, r2, r1.
- Data uji TC-AC-ACAL-101 (urutan baris seed per kolom):

  | Kolom | Urutan A-Z | Urutan Z-A |
  |---|---|---|
  | Action | r5, r1, r3, r2, r4 | r4, r2, r3, r1, r5 |
  | Object | r3, r2, r1, r4, r5 | r5, r4, r1, r2, r3 |
  | Name | r1, r2, r3, r4, r5 | r5, r4, r3, r2, r1 |
  | Field | r3, r1, r2, r5, r4 | r4, r5, r2, r1, r3 |

- Data uji TC-AC-ACAL-103 (campuran angka, teks huruf besar kecil, dan nilai kosong `—`):

  | Kolom | Urutan ↑ | Urutan ↓ |
  |---|---|---|
  | Old Value | r2 (`25`), r1 (`100`), r3 (`Active`), r4 (`budi`), r5 (`—`) | r5 (`—`), r4 (`budi`), r3 (`Active`), r1 (`100`), r2 (`25`) |
  | New Value | r1 (`5`), r2 (`40`), r4 (`archive`), r3 (`Suspended`), r5 (`—`) | r5 (`—`), r3 (`Suspended`), r4 (`archive`), r2 (`40`), r1 (`5`) |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri User Action dengan Date, Modified By, dan nilai kolom pada tabel Data log (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan); menelusuri halaman bila baris tidak berada di halaman pertama.
- State global: sort dan Search direset hook `beforeEach` suite pada spec berikutnya; spec menutup Search di langkah 30. Entri User Action tidak dapat dihapus dan tetap ada sebagai snapshot.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Admin Console > Activity Log > User Action
2. Ketik Search `{runId}-031`, tekan Enter
3. Verifikasi baris r1, r2, r3, r4, dan r5 tampil

### TC-AC-ACAL-100: Sort Date siklus tiga tahap

4. Klik ikon sort Date
5. Verifikasi ikon sort Date `↑`
6. Verifikasi baris r1, r2, r3, r4, r5 berurutan Oldest First
7. Klik ikon sort Date lagi
8. Verifikasi ikon sort Date `↓`
9. Verifikasi baris r5, r4, r3, r2, r1 berurutan Newest First
10. Klik ikon sort Date lagi
11. Verifikasi ikon sort Date netral
12. Verifikasi baris kembali ke default Date terbaru di atas (r5, r4, r3, r2, r1)

### TC-AC-ACAL-101: Sort alfabetis Action, Object, Name, Field

13. Untuk setiap baris tabel Data uji TC-AC-ACAL-101 (langkah 13 sampai 19): klik ikon sort kolom
14. Verifikasi baris r1 sampai r5 berurutan A-Z sesuai kolom "Urutan A-Z"
15. Klik ikon sort kolom lagi
16. Verifikasi baris r1 sampai r5 berurutan Z-A sesuai kolom "Urutan Z-A"
17. Klik ikon sort kolom lagi
18. Verifikasi sort kolom netral
19. Verifikasi baris kembali ke default Date terbaru di atas (r5, r4, r3, r2, r1)

### TC-AC-ACAL-102: Sort Modified By berdasarkan nama lengkap

20. Klik ikon sort Modified By (ascending)
21. Verifikasi baris `Dewi Larasati` (r2 dan r4) berada di atas baris `Dewi Lestari` (r1, r3, dan r5)
22. Klik ikon sort Modified By dua kali lagi hingga netral

### TC-AC-ACAL-103: Sort Old Value dan New Value, campuran tipe data

23. Untuk setiap baris tabel Data uji TC-AC-ACAL-103 (langkah 23 sampai 29): klik ikon sort kolom
24. Verifikasi baris r1 sampai r5 berurutan sesuai kolom "Urutan ↑"
25. Klik ikon sort kolom lagi
26. Verifikasi baris r1 sampai r5 berurutan sesuai kolom "Urutan ↓"
27. Klik ikon sort kolom lagi
28. Verifikasi sort kolom netral
29. Verifikasi baris kembali ke default Date terbaru di atas (r5, r4, r3, r2, r1)

### Pemulihan state

30. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4b, Tab User Action). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `{runId}-031` membatasi tabel ke baris seed supaya baris teramati berada pada halaman yang sama (langkah 2, S-14), pemulihan sort Modified By (langkah 22), dan penutupan Search (langkah 30, hook `after` sebagai cadangan). Langkah 3 adalah pembanding generik sebelum asersi urutan.
- Langkah 13 sampai 19 berulang untuk setiap baris tabel Data uji TC-AC-ACAL-101 (empat iterasi) dan langkah 23 sampai 29 untuk setiap baris tabel Data uji TC-AC-ACAL-103 (dua iterasi), sesuai bagian 8b butir 7.
- Spec memiliki 30 langkah nominal dan 58 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Sort Tab User Action pada akun dan dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari dua perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri User Action (Date, Modified By, Old Value, New Value) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-101 tidak menetapkan data uji kolom Action, Object, Name, dan Field; nilai pada Data log adalah pilihan spec dengan sedikitnya dua nilai distinct tiap kolom (S-11). TC-AC-ACAL-103 hanya menetapkan nilai Old Value dan New Value; pasangan nilai itu dipetakan ke lima entri seed r1 sampai r5.
  - TC-AC-ACAL-102 tidak menyebut entri selain pelaku `Dewi Lestari` dan `Dewi Larasati`; spec mengidentifikasi baris lewat Name bersuffix dan tidak memakai tooltip Modified By.
