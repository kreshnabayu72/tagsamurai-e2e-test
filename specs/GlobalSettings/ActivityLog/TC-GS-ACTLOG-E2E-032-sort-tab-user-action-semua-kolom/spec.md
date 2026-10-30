---
id: TC-GS-ACTLOG-E2E-032-sort-tab-user-action-semua-kolom
title: "Sort Tab User Action: Semua Kolom"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-175
  - TC-GS-ACTLOG-176
  - TC-GS-ACTLOG-177
  - TC-GS-ACTLOG-178
  - TC-GS-ACTLOG-179
coverage:
  web: automated
---

# Sort Tab User Action: Semua Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas log-terbatas segar milik spec ini, `Fixture.activityLog.entitasLog032` (entitas uji dengan log User Action terbatas, Tabel Data Uji Pre-setup baris 13; disediakan tim FE/BE, email ditetapkan tim FE), kredensial `Spectra.env.GS_LIMITLOG_TC_PASSWORD` (semua akun Total Control entitas log-terbatas berbagi password ini). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Activity Log > tab User Action.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md). Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun `Fixture.activityLog.entitasLog032` dan halaman Global Settings > Activity Log (kemampuan disediakan tim FE/BE).
- Environment variable: `GS_LIMITLOG_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Alasan entitas log-terbatas: urutan sort yang diasersi (mis. Old Value `2`, `5`, `10`, `Finance`, `Marketing`, `—`; Date dari `10 Jun 2026` sampai `15 Jun 2026`) hanya dapat diverifikasi bila himpunan nilai log kolom diketahui dan tertutup, dan entri bertanggal Juni 2026 tidak dapat dihasilkan aksi nyata. Entitas ini dipakai hanya oleh spec 032.
- Kemampuan teknis (disediakan tim FE/BE, tanpa mengarang endpoint): seed BE enam entri User Action berikut pada entitas log-terbatas di hook `before` (log tidak dapat diubah atau dihapus, ACTLOG-LOGIC-01; nilai Old Value dan New Value sengaja hanya dari himpunan `2`, `5`, `10`, `Finance`, `Marketing`, `—` agar urutan numerik, teks, dan kosong teramati). Entitas segar, sehingga keadaan log sebelum spec berjalan adalah persis enam entri ini:

| Baris | Date | Action | Object | Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|---|
| R1 | 10 Jun 2026, 16:45 | `Create` | `Brand` | `Acme` | `Name` | `2` | `5` | `Dewi Lestari{runId}` |
| R2 | 11 Jun 2026, 09:10 | `Edit` | `Measurement` | `Siti Nurbaya` | `Name` | `10` | `2` | `Dewi Larasati{runId}` |
| R3 | 12 Jun 2026, 13:30 | `Delete` | `User` | `Acme` | `Division` | `5` | `10` | `Hendra Pratama` |
| R4 | 14 Jun 2026, 14:05 | `Edit` | `User` | `Siti Nurbaya` | `Division` | `Finance` | `Marketing` | `Wulan` |
| R5 | 15 Jun 2026, 10:20 | `Create` | `Measurement` | `Acme` | `Name` | `Marketing` | `Finance` | `Dewi Lestari{runId}` |
| R6 | 13 Jun 2026, 08:00 | `Import` | `Brand` | `—` | `—` | `—` | `—` | `Hendra Pratama` |

  Nama literal `Dewi Lestari{runId}` dan `Dewi Larasati{runId}` memakai sufiks run yang dirapatkan ke nama belakang, sehingga singkatan sel tetap `Dewi L` dan urutan nama lengkap (`Dewi Larasati{runId}` sebelum `Dewi Lestari{runId}`) tidak berubah. Modified By tampil `Dewi L` untuk `Dewi Lestari{runId}` dan `Dewi Larasati{runId}`, `Hendra P`, `Wulan`; nama lengkap tampil di hover (PRD activity-log.md §4.1.2). Teks Date mengikuti General Settings Date Format entitas (nilai Pre-setup); asersi urutan Date mengidentifikasi baris lewat R1 sampai R6, bukan teks format.
- Tabel "Urutan sort yang diharapkan" (parameter pengulangan langkah 1 sampai 9; daftar R-baris dan nilai dibaca dari atas ke bawah; asersi pada nilai yang tercantum, urutan relatif sesuai tabel):

| Kolom | TC | Klik 1 `(↑)` | Klik 2 `(↓)` | Cara membaca nilai |
|---|---|---|---|---|
| Date | TC-GS-ACTLOG-175 | Oldest First: R1 di atas, R5 di bawah | Newest First: R5 di atas, R1 di bawah | identifikasi baris R1 sampai R6 (teks format tidak diasersi) |
| Action | TC-GS-ACTLOG-176 | `Create`, `Delete`, `Edit` | `Edit`, `Delete`, `Create` | teks sel |
| Object | TC-GS-ACTLOG-176 | `Brand`, `Measurement`, `User` | `User`, `Measurement`, `Brand` | teks sel |
| Name | TC-GS-ACTLOG-177 | `Acme`, `Siti Nurbaya`, lalu baris `—` (R6) di paling bawah | baris `—` (R6) di paling atas, lalu `Siti Nurbaya`, `Acme` | teks sel |
| Field | TC-GS-ACTLOG-177 | `Division`, `Name`, lalu baris `—` (R6) di paling bawah | baris `—` (R6) di paling atas, lalu `Name`, `Division` | teks sel |
| Old Value | TC-GS-ACTLOG-178 | `2`, `5`, `10` (angka natural), `Finance`, `Marketing`, lalu `—` (R6) di paling bawah | `—` (R6), `Marketing`, `Finance`, `10`, `5`, `2` | teks sel |
| New Value | TC-GS-ACTLOG-178 | `2`, `5`, `10`, `Finance`, `Marketing`, lalu `—` (R6) di paling bawah | `—` (R6), `Marketing`, `Finance`, `10`, `5`, `2` | teks sel |
| Modified By | TC-GS-ACTLOG-179 | nama lengkap `Dewi Larasati{runId}`, `Dewi Lestari{runId}`, `Hendra Pratama`, `Wulan` | `Wulan`, `Hendra Pratama`, `Dewi Lestari{runId}`, `Dewi Larasati{runId}` | nama lengkap dari hover sel (`Dewi Lestari{runId}` dan `Dewi Larasati{runId}` sama-sama tampil `Dewi L`) |

  Klik 3 pada semua kolom: indikator sort tidak aktif dan urutan kembali ke urutan default tabel (Date terbaru di atas: R5 di atas, R1 di bawah). Pada kolom Action, baris `Import` (R6) berada setelah `Edit` saat ascending dan sebelum `Edit` saat descending; asersi hanya pada urutan relatif `Create`, `Delete`, `Edit`.
- State global: sort tabel User Action dikembalikan ke default oleh klik ketiga tiap kolom; tidak ada state lain yang diubah. Cleanup: tidak ada data yang dibuat spec ini.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-175 sampai 179: Sort 3 klik tiap kolom Tab User Action

1. Untuk setiap baris tabel "Urutan sort yang diharapkan" (langkah 1 sampai 9): klik header kolom pada kolom "Kolom"
2. Verifikasi indikator `(↑)` aktif pada kolom itu
3. Verifikasi urutan baris sesuai kolom "Klik 1" tabel itu, dibaca sesuai kolom "Cara membaca nilai"
4. Klik header kolom itu lagi
5. Verifikasi indikator `(↓)` aktif pada kolom itu
6. Verifikasi urutan baris sesuai kolom "Klik 2" tabel itu, dibaca sesuai kolom "Cara membaca nilai"
7. Klik header kolom itu untuk ketiga kali
8. Verifikasi indikator sort tidak aktif pada kolom itu
9. Verifikasi urutan baris kembali ke urutan default tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Pembagian langkah ke TC lewat kolom "TC" pada tabel "Urutan sort yang diharapkan": kolom Date = TC-GS-ACTLOG-175, Action dan Object = TC-GS-ACTLOG-176, Name dan Field = TC-GS-ACTLOG-177, Old Value dan New Value = TC-GS-ACTLOG-178, Modified By = TC-GS-ACTLOG-179. Urutan baris tabel mengikuti urutan TC sumber.
- Alasan spec di atas smell 35 langkah: 9 langkah nominal, sekitar 72 langkah dieksekusi (langkah 1 sampai 9 diulang untuk delapan kolom). Semua iterasi satu topik (Sort Tab User Action), satu akun, satu entitas, satu dataset seed, tanpa kelas harness lain; klik ketiga tiap kolom mengembalikan sort ke default sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Pengulangan: langkah 1 sampai 9 diulang untuk delapan baris tabel "Urutan sort yang diharapkan"; tiap iterasi mengulang `Verifikasi` langkah 2, 3, 5, 6, 8, 9, sehingga tiap kolom (delapan) punya `Verifikasi` indikator dan urutan sendiri.
- Tidak ada langkah penghubung: klik ketiga tiap kolom (langkah 7) mengembalikan sort ke default sehingga kolom berikutnya dimulai dari keadaan awal, sesuai Expected c TC masing-masing.
- Asersi tambahan di luar Expected TC: tidak ada.
- Pembagian TC: TC-GS-ACTLOG-175 sampai 179 seluruhnya ada di spec ini.
- Temuan untuk QA:
  - TC-GS-ACTLOG-177 menyebut entri `Import` dengan Name `—`, sedangkan TC-GS-ACTLOG-176 mendaftar Action hanya `Create`, `Delete`, `Edit`; spec menambah baris `Import` (R6) dan mengasersi urutan relatif ketiga nilai pada TC-GS-ACTLOG-176.
  - TC-GS-ACTLOG-175 menulis tanggal `10 Jun 2026, 16:45` sedangkan TC-GS-ACTLOG-154 menyebut Date Format `DD MMM YY`; teks Date tampil mengikuti General Settings Date Format entitas. Spec mengidentifikasi baris lewat R1 sampai R6.
  - TC-GS-ACTLOG-178 menyebut nilai `2`, `10`, `5`, `Finance`, `Marketing` pada Old Value dan New Value tanpa kombinasi Action dan Object; kombinasi pada seed (mis. `Delete` `User` `Division` Old Value `5`) adalah data sintetis pilihan spec, bukan hasil modul sumber.
  - TC-GS-ACTLOG-179 menyebut `Dewi Lestari{runId}` dan `Dewi Larasati{runId}` sama-sama tampil `Dewi L`; asersi urutan nama lengkap membutuhkan hover tiap sel.
