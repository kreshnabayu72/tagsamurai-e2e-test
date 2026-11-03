---
id: TC-FA-FAAL-E2E-013-read-only-search-filter-download
title: "Read Only: Search, Filter, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-52
  - TC-FA-FAAL-53
  - TC-FA-FAAL-54
coverage:
  web: automated
---

# Read Only: Search, Filter, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Read Only (Pre-setup #2), `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_RO_PASSWORD`.
- Login akun aktor pertama (Read Only) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, tab Session). Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Env var `FA_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11) dan Tab User Action UA-01 sampai UA-15 (Pre-setup #12, total 15 baris), dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE).
- Kemampuan teknis disediakan tim FE: penangkap unduhan browser dan parser CSV (butir "Kemampuan teknis tambahan" di `suite.md`) untuk TC-FA-FAAL-54.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun aktor.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nilai data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-52: Read Only menjalankan Search di Tab Session

1. Klik icon Filter
2. Pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date
3. Klik `[Apply]`
4. Verifikasi Read Only: sedikitnya satu baris tampil pada tabel Tab Session
5. Ketik Search `Budi`, tekan Enter
6. Verifikasi Read Only: tabel hanya menampilkan baris SS-06 (Budi Santoso)
7. Verifikasi Read Only: teks pagination `Showing 1–1 of 1 entries`
8. Klik `(←)` pada kotak Search

### TC-FA-FAAL-53: Read Only menjalankan Filter di Tab User Action

9. Klik tab User Action
10. Verifikasi Read Only: sedikitnya satu baris tampil pada tabel Tab User Action
11. Klik icon Filter
12. Pilih `Delete` pada field Action
13. Klik `[Apply]`
14. Verifikasi Read Only: tabel hanya menampilkan baris UA-03 (Delete Categories)
15. Verifikasi Read Only: icon Filter menampilkan badge titik
16. Klik menu `Activity Log` pada sidebar Reports & Logs (mereset Search, Filter, dan Sort)

### TC-FA-FAAL-54: Read Only menjalankan Download di Tab User Action

17. Klik tab User Action
18. Klik icon Filter
19. Pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date
20. Klik `[Apply]`
21. Klik icon Download
22. Pilih `Download as CSV`
23. Verifikasi Read Only: tidak ada toast
24. Verifikasi Read Only: berkas `Activity-Log-User-Action.csv` terunduh
25. Verifikasi Read Only: berkas memuat 15 baris data

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 sampai 3 dan 18 sampai 20 (menerapkan Filter Date Jendela Seed sesuai precondition d TC-FA-FAAL-52 dan 54), langkah 8 (mengosongkan Search), langkah 9 dan 17 (klik tab User Action untuk precondition TC), dan langkah 16 (mereset Filter sebelum Download).
- Pembanding asersi universal (bagian 8b butir 2): langkah 4 dan 10 membuktikan baris ada di tabel sebelum asersi "hanya baris SS-06" dan "hanya baris UA-03".
- Langkah 23 (absence toast) diletakkan segera setelah pemicu `Download as CSV` dan sebelum asersi berkas (bagian 8b butir 11); langkah 22 menjadi anchor positif yang buktinya langkah 24.
- Langkah 25 (jumlah baris berkas) membutuhkan parser CSV; nama berkas dan jumlah baris adalah asersi fungsional (bagian 3 prinsip 13f).
- Temuan untuk QA:
  - TC-FA-FAAL-54 Expected butir a menyebut berkas "memuat 15 baris data" tanpa menyebut apakah header dihitung; spec membaca 15 sebagai baris data di luar header.
  - TC-FA-FAAL-52 sampai 54 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
