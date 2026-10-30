---
id: TC-GS-DIV-E2E-060-changelog-pagination-page-size
title: "Modal Changelog: Pagination dan Page Size"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-210
coverage:
  web: automated
---

# Modal Changelog: Pagination dan Page Size

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`):
  - Population D-02 oleh Sari Dewi (seeding Division lewat API, setara TC-GS-DIV-30): 26 Division dengan nama dan Code literal Accounting (`ACC`), Administration (`ADM`), Audit (`AUD`), Business Development (`BD`), Corporate Communication (`CCM`), Customer Service (`CSV`), Data Analytics (`DA`), Engineering (`ENG`), Facilities (`FAC`), General Affairs (`GA`), Information Technology (`IT`), Internal Control (`IC`), Logistics (`LOG`), Marketing (`MKT`), Procurement (`PRC`), Product Management (`PM`), Production (`PRD`), Quality Assurance (`QA`), Research and Development (`RND`), Risk Management (`RSK`), Sales (`SLS`), Security (`SEC`), Strategy (`STR`), Supply Chain (`SC`), Training (`TRN`), Warehouse (`WH`). Seed idempotent: nama yang sudah ada dilewati; cleanup hanya menghapus yang dibuat spec ini. Tiap Create mencatat entri Changelog Action Create oleh `Sari D` (Old Value `—`). Menghasilkan 26 entri Create.
  - 30 Division pembantu `Log Page {NN} {runId}-060` (NN = 01 sampai 30) dibuat oleh Sari Dewi, menambah 30 entri Create (satu entri per Create, TC-GS-DIV-235). Total 26 (Population) + 30 (pembantu) = 56 entri Create, sehingga riwayat lebih dari 50 entri (precondition d).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division Population yang dibuat spec ini dan 30 Division `Log Page {NN} {runId}-060`. Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6), Population (26), dan 30 Division pembantu (disediakan tim FE).
- Kemampuan teknis: membuka dropdown page size dan memilih opsi; menghitung baris pada halaman.
- Precondition TC-GS-DIV-210: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog lebih dari 50 entri.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite serial (`parallel: false`) karena Population D-02 bernama literal dan dipakai bersama spec lain.
- State global yang dipulihkan: tidak ada (spec hanya membaca).

## Test Steps

### TC-GS-DIV-210: Pagination Modal Changelog: default 10 dan pilihan 10, 25, 50, 100

1. Klik icon Changelog di Table Tools
2. Verifikasi halaman 1 memuat 10 baris (default 10 baris per halaman)
3. Buka dropdown page size
4. Verifikasi opsi page size `10`, `25`, `50`, dan `100`
5. Verifikasi tidak ada opsi `All`
6. Pilih page size 25
7. Verifikasi halaman memuat 25 baris
8. Pilih page size 50
9. Verifikasi halaman memuat 50 baris
10. Pilih page size 100
11. Verifikasi halaman memuat sampai 100 baris

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Satu TC; urutan langkah mengikuti TC (default 10 diamati sebelum page size diubah).
- Langkah 3 sampai 5 (membuka dropdown page size dan memeriksa opsi `10`, `25`, `50`, `100` tanpa `All`) berasal dari judul dan Expected b TC ("tanpa opsi All"); TC tidak punya langkah eksplisit untuk membuka dropdown.
- Langkah 11 memakai frasa "sampai 100 baris" persis Expected b: total entri bisa kurang dari 100, sehingga halaman memuat seluruh entri.
- Asersi jumlah baris 10, 25, 50 bergantung pada riwayat lebih dari 50 entri (precondition d), disediakan seeding di Prerequisites.
- Temuan untuk QA: (1) Expected b untuk 100 baris ("sampai 100") tidak membedakan total kurang dari 100; spec mengasersi batas atas.
