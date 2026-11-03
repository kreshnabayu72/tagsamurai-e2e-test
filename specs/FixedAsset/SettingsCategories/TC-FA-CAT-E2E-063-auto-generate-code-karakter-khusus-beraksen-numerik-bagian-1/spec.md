---
id: TC-FA-CAT-E2E-063-auto-generate-code-karakter-khusus-beraksen-numerik-bagian-1
title: "Auto-generate Code: Nama Satu Karakter, Karakter Khusus, dan Huruf Beraksen (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-150
  - TC-FA-CAT-151
  - TC-FA-CAT-152
coverage:
  web: automated
---

# Auto-generate Code: Nama Satu Karakter, Karakter Khusus, dan Huruf Beraksen (Bagian 1)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; tidak ada baris seed yang diubah.
- Data yang dibuat spec lewat UI (Category Name literal tanpa suffix karena Code hasil generate diturunkan dari nama itu; ini pengecualian nama literal atas S-12, dan suite berjalan serial). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | TC | Category Name | Code hasil generate yang diharapkan |
  |---|---|---|
  | TC-150 | `A` | `A` |
  | TC-151 | `(Gaming) & Laptop` | `GL` |
  | TC-152 | `Éclair Café` | `CC` |

- Nama 1 karakter `A` (TC-150) sah tanpa suffix dengan syarat: seeding idempotent (dilewati bila sudah ada), cleanup hanya menghapus kategori yang dibuat spec ini, suite berjalan serial, dan nama berbeda dari nama 1 karakter spec lain pada entitas yang sama (disediakan tim FE).
- Hook `before` menghapus sisa kategori ber-Name atau ber-Code di atas dari run lain atau spec lain agar dedup tidak mengubah hasil generate (R-13); hook `after` menghapus ketiga kategori yang dibuat spec (disediakan tim FE).
- Kemampuan teknis: pembacaan kolom Code pada tabel Categories List; input karakter non-ASCII (`É`, `é`) pada Category Name.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-150: Auto-generate Code: nama satu karakter menghasilkan Code satu karakter

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `A` dan biarkan Code kosong
3. Klik `[Submit]`
4. Verifikasi toast `Success, category has been created.`
5. Ketik Search `A`, tekan Enter
6. Verifikasi baris `A` tampil di tabel (kategori tersimpan)
7. Verifikasi kolom Code baris `A` berisi `A` (kandidat `A` dan fallback `A`)
8. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
9. Klik `(←)` pada kotak Search

### TC-FA-CAT-151: Auto-generate Code: karakter di depan token yang tidak lolos whitelist diabaikan dan token tanpa karakter lolos dilewati

10. Klik `[+] Category` pada sidebar
11. Isi Category Name `(Gaming) & Laptop` dan biarkan Code kosong
12. Klik `[Submit]`
13. Verifikasi toast `Success, category has been created.`
14. Ketik Search `(Gaming) & Laptop`, tekan Enter
15. Verifikasi baris `(Gaming) & Laptop` tampil di tabel (kategori tersimpan)
16. Verifikasi kolom Code baris `(Gaming) & Laptop` berisi `GL` (`(` pada `(Gaming)` diabaikan sehingga `G`; token `&` dilewati; `L` dari Laptop)
17. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
18. Klik `(←)` pada kotak Search

### TC-FA-CAT-152: Auto-generate Code: huruf beraksen yang tidak lolos whitelist diabaikan

19. Klik `[+] Category` pada sidebar
20. Isi Category Name `Éclair Café` dan biarkan Code kosong
21. Klik `[Submit]`
22. Verifikasi toast `Success, category has been created.`
23. Ketik Search `Éclair Café`, tekan Enter
24. Verifikasi baris `Éclair Café` tampil di tabel (kategori tersimpan)
25. Verifikasi kolom Code baris `Éclair Café` berisi `CC` (`É` tidak lolos whitelist sehingga karakter pertama yang lolos pada `Éclair` adalah `C`, dan `C` dari `Café`)
26. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
27. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-150, TC-151, dan TC-152 ada di spec ini; TC-153 dan TC-154 ada di spec 064.
- Nama literal tanpa suffix (S-12, pengecualian khusus): Code diturunkan dari Category Name, sehingga suffix `{runId}` akan mengubah Code yang diuji. Syaratnya dipenuhi lewat Prerequisites.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): Search untuk menemukan baris hasil (R-16) dan mengosongkan Search lewat `(←)` sebelum TC berikutnya (S-09).
- Temuan untuk QA:
  - TC-150 Search `A` mencocokkan banyak baris (substring pada Category Name, Code, dan kolom searchable lain). TC tidak menyatakan cara menemukan baris bernama persis `A`; spec mengasumsikan baris `A` tampil pada halaman hasil Search dan memerlukan penetapan tim FE bila hasil melebihi satu halaman.
  - TC-150, TC-151, dan TC-152 Post Condition (Changelog menulis satu baris Create Field `Category Name`; Code hasil generate tidak menulis baris tersendiri) tanpa langkah observasi di TC sehingga tidak diasersi (S-01).
  - TC-151 dan TC-152 menyatakan "kategori tersimpan" pada Expected a tanpa menyebut cara memeriksanya; spec memeriksa kemunculan baris di tabel.
