---
id: TC-FA-CAT-E2E-062-auto-generate-code-token-whitelist-potong-15-karakter-bagian-2
title: "Auto-generate Code: Pemisah Token dan Fallback 6 Karakter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-148
  - TC-FA-CAT-149
coverage:
  web: automated
---

# Auto-generate Code: Pemisah Token dan Fallback 6 Karakter (Bagian 2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; tidak ada baris seed yang diubah.
- Data yang dibuat spec lewat UI (Category Name literal tanpa suffix karena Code hasil generate diturunkan dari nama itu; ini pengecualian nama literal atas S-12, dan suite berjalan serial). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | TC | Category Name | Code hasil generate yang diharapkan |
  |---|---|---|
  | TC-148 | `Wi-Fi/Router_Pro` | `WFRP` |
  | TC-149 | `Furnishing` | `FURNIS` |

- Hook `before` menghapus sisa kategori ber-Name atau ber-Code di atas dari run lain atau spec lain agar dedup tidak mengubah hasil generate (R-13); hook `after` menghapus kedua kategori yang dibuat spec (disediakan tim FE).
- Kemampuan teknis: pembacaan kolom Code pada tabel Categories List.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-148: Auto-generate Code: pemisah spasi, hubung, garis bawah, dan garis miring memecah token

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Wi-Fi/Router_Pro` dan biarkan Code kosong
3. Klik `[Submit]`
4. Verifikasi toast `Success, category has been created.`
5. Ketik Search `Wi-Fi/Router_Pro`, tekan Enter
6. Verifikasi baris `Wi-Fi/Router_Pro` tampil di tabel (kategori tersimpan)
7. Verifikasi kolom Code baris `Wi-Fi/Router_Pro` berisi `WFRP` (empat token `Wi`, `Fi`, `Router`, `Pro`)
8. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
9. Klik `(←)` pada kotak Search

### TC-FA-CAT-149: Auto-generate Code: kandidat kurang dari 2 karakter memakai 6 karakter alfanumerik pertama

10. Klik `[+] Category` pada sidebar
11. Isi Category Name `Furnishing` dan biarkan Code kosong
12. Klik `[Submit]`
13. Verifikasi toast `Success, category has been created.`
14. Ketik Search `Furnishing`, tekan Enter
15. Verifikasi baris `Furnishing` tampil di tabel (kategori tersimpan)
16. Verifikasi kolom Code baris `Furnishing` berisi `FURNIS` (kandidat `F` kurang dari 2 karakter sehingga fallback 6 karakter pertama nama)
17. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
18. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-148 dan TC-149 ada di spec ini; TC-145, TC-146, dan TC-147 ada di spec 061.
- Nama literal tanpa suffix (S-12, pengecualian khusus): Code diturunkan dari Category Name, sehingga suffix `{runId}` akan mengubah Code yang diuji. Syaratnya dipenuhi lewat Prerequisites (pembersihan di `before`, cleanup di `after`, suite serial).
- Langkah penghubung (S-03, tanpa awalan Verifikasi): Search untuk menemukan baris hasil (R-16) dan mengosongkan Search lewat `(←)` sebelum TC berikutnya (S-09).
- Temuan untuk QA:
  - TC-148 dan TC-149 Post Condition (Changelog menulis satu baris Create Field `Category Name`; Code hasil generate tidak menulis baris tersendiri) tanpa langkah observasi di TC sehingga tidak diasersi (S-01).
  - Kedua TC menyatakan "kategori tersimpan" pada Expected a tanpa menyebut cara memeriksanya; spec memeriksa kemunculan baris di tabel.
  - Search `Wi-Fi/Router_Pro` memakai karakter khusus; TC tidak menyatakan apakah Search memperlakukan `/` dan `-` secara literal.
