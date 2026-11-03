---
id: TC-FA-CAT-E2E-061-auto-generate-code-token-whitelist-potong-15-karakter-bagian-1
title: "Auto-generate Code: Token Alfabetik, Numerik Murni, dan Campuran (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-145
  - TC-FA-CAT-146
  - TC-FA-CAT-147
coverage:
  web: automated
---

# Auto-generate Code: Token Alfabetik, Numerik Murni, dan Campuran (Bagian 1)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; tidak ada baris seed yang diubah.
- Data yang dibuat spec lewat UI (Category Name literal tanpa suffix karena Code hasil generate diturunkan dari nama itu; ini pengecualian nama literal atas S-12, dan suite berjalan serial). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | TC | Category Name | Code hasil generate yang diharapkan |
  |---|---|---|
  | TC-145 | `Office Furniture` | `OF` |
  | TC-146 | `Mouse 2 Pro` | `M2P` |
  | TC-147 | `A1B Series` | `AS` |

- Hook `before` menghapus sisa kategori ber-Name atau ber-Code di atas dari run lain atau spec lain agar dedup tidak mengubah hasil generate (R-13); hook `after` menghapus ketiga kategori yang dibuat spec (disediakan tim FE).
- Kemampuan teknis: pembacaan kolom Code pada tabel Categories List.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-145: Auto-generate Code: token alfabetik menjadi inisial kapital

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Office Furniture` dan biarkan Code kosong
3. Klik `[Submit]`
4. Verifikasi toast `Success, category has been created.`
5. Ketik Search `Office Furniture`, tekan Enter
6. Verifikasi baris `Office Furniture` tampil di tabel (kategori tersimpan)
7. Verifikasi kolom Code baris `Office Furniture` berisi `OF` (inisial `O` dan `F`)
8. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
9. Klik `(←)` pada kotak Search

### TC-FA-CAT-146: Auto-generate Code: token numerik murni passthrough utuh

10. Klik `[+] Category` pada sidebar
11. Isi Category Name `Mouse 2 Pro` dan biarkan Code kosong
12. Klik `[Submit]`
13. Verifikasi toast `Success, category has been created.`
14. Ketik Search `Mouse 2 Pro`, tekan Enter
15. Verifikasi baris `Mouse 2 Pro` tampil di tabel (kategori tersimpan)
16. Verifikasi kolom Code baris `Mouse 2 Pro` berisi `M2P` (`M` dari Mouse, `2` utuh, `P` dari Pro)
17. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
18. Klik `(←)` pada kotak Search

### TC-FA-CAT-147: Auto-generate Code: token campuran memakai karakter pertama kapital

19. Klik `[+] Category` pada sidebar
20. Isi Category Name `A1B Series` dan biarkan Code kosong
21. Klik `[Submit]`
22. Verifikasi toast `Success, category has been created.`
23. Ketik Search `A1B Series`, tekan Enter
24. Verifikasi baris `A1B Series` tampil di tabel (kategori tersimpan)
25. Verifikasi kolom Code baris `A1B Series` berisi `AS` (token `A1B` menjadi `A` dan `Series` menjadi `S`)
26. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
27. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-145, TC-146, dan TC-147 ada di spec ini; TC-148 dan TC-149 ada di spec 062.
- Nama literal tanpa suffix (S-12, pengecualian khusus): Code diturunkan dari Category Name, sehingga suffix `{runId}` akan mengubah Code yang diuji. Syaratnya dipenuhi lewat Prerequisites (pembersihan di `before`, cleanup di `after`, suite serial).
- Langkah penghubung (S-03, tanpa awalan Verifikasi): Search untuk menemukan baris hasil (R-16) dan mengosongkan Search lewat `(←)` sebelum TC berikutnya (S-09).
- Temuan untuk QA:
  - TC-145, TC-146, dan TC-147 Post Condition (Changelog menulis satu baris Create Field `Category Name`; Code hasil generate tidak menulis baris tersendiri) tanpa langkah observasi di TC sehingga tidak diasersi (S-01).
  - Ketiga TC menyatakan "kategori tersimpan" pada Expected a tanpa menyebut cara memeriksanya; spec memeriksa kemunculan baris di tabel.
  - Nama literal yang sama dapat dipakai TC pada spec lain (mis. `Office Furniture` pada TC pembuatan kategori); keunikan antar-spec dijaga oleh `parallel: false` dan cleanup, bukan oleh suffix.
