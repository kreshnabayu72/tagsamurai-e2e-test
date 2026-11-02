---
id: TC-FA-CAT-E2E-067-auto-generate-code-tier-2-lanjut-root-ruang-suffix-literal-cat-bagian-2
title: "Auto-generate Code: Suffix Tidak Dipotong dan Literal CAT (Bagian 2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-162
  - TC-FA-CAT-163
coverage:
  web: automated
---

# Auto-generate Code: Suffix Tidak Dipotong dan Literal CAT (Bagian 2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatCode (Pre-setup #34) dengan `{namaCompany}` client CatCode, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini (akun pertama spec bukan akun default suite); halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatCode (#34) keadaan dasar: kategori L1 `Dedup 1` sampai `Dedup 7` ber-Code `ELEC` sampai `ELEC7`, `Parent Kode`, `Parent Panjang`, `Parent Lima`, dan `Panjang 15` ber-Code `ABCDEFGHIJKLMNO`. Hook `before` memastikan keadaan dasar dan hook `after` memulihkannya lewat seed API (disediakan tim FE).
- Varian seed #34 per TC: TC-162 memakai keadaan dasar (Code `ABCDEFGHIJKLMNO` dipakai `Panjang 15`); TC-163 memakai varian Code `CAT` belum dipakai oleh kategori mana pun (seed API di langkah penghubung; disediakan tim FE, tanpa endpoint karangan).
- Data yang dibuat spec lewat UI (Category Name literal tanpa suffix karena Code hasil generate diturunkan dari nama itu; ini pengecualian nama literal atas S-12, dan suite berjalan serial). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | TC | Category Name | Code hasil generate yang diharapkan |
  |---|---|---|
  | TC-162 | `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa` | `ABCDEFGHIJKLMN2` |
  | TC-163 | `***` | `CAT` |
  | TC-163 | `---` | `CAT2` |

- Hook `before` menghapus sisa kategori ber-Name di atas dari run lain atau spec lain (R-13); hook `after` menghapus kategori yang dibuat spec (disediakan tim FE).
- Kemampuan teknis: pembacaan kolom Code pada tabel Categories List.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-162: Auto-generate Code: suffix angka tidak dipotong sehingga bagian kandidat dipotong seperlunya

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa` dan biarkan Code kosong
3. Klik `[Submit]`
4. Verifikasi toast `Success, category has been created.`
5. Ketik Search `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa`, tekan Enter
6. Verifikasi baris `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa` tampil di tabel (kategori tersimpan)
7. Verifikasi kolom Code baris `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa` berisi `ABCDEFGHIJKLMN2` (kandidat `ABCDEFGHIJKLMNO` sudah dipakai `Panjang 15`; kandidat dipotong ke 14 karakter agar dengan suffix `2` total 15 karakter)
8. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
9. Klik `(←)` pada kotak Search

### TC-FA-CAT-163: Auto-generate Code: nama tanpa karakter lolos whitelist memakai kandidat literal CAT

10. Hapus kategori hasil TC-162 dan siapkan varian #34: Code `CAT` belum dipakai (seed API), lalu muat ulang halaman
11. Klik `[+] Category` pada sidebar
12. Isi Category Name `***` dan biarkan Code kosong
13. Klik `[Submit]`
14. Verifikasi toast `Success, category has been created.` untuk submit pertama
15. Tunggu toast lama hilang otomatis
16. Buka popup lagi: klik `[+] Category` pada sidebar
17. Isi Category Name `---` dan biarkan Code kosong
18. Klik `[Submit]`
19. Verifikasi toast `Success, category has been created.` untuk submit kedua
20. Ketik Search `***`, tekan Enter
21. Verifikasi baris `***` tampil di tabel dengan Code `CAT` (kandidat dan fallback kosong sehingga memakai literal `CAT`)
22. Ganti isi kotak search dengan `---`, tekan Enter
23. Verifikasi baris `---` tampil di tabel dengan Code `CAT2` (dedup Tier 1 pada literal `CAT`)
24. Verifikasi Code tersimpan pada kedua baris tidak kosong
25. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-162 dan TC-163 ada di spec ini; TC-155 sampai TC-158 ada di spec 065; TC-159, TC-160, dan TC-161 ada di spec 066.
- Nama literal tanpa suffix (S-12, pengecualian khusus): Code diturunkan dari Category Name, sehingga suffix `{runId}` akan mengubah Code yang diuji. Syaratnya dipenuhi lewat Prerequisites.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): penyiapan varian seed dan penghapusan kategori sebelumnya; memuat ulang halaman; menunggu toast lama hilang otomatis sebelum asersi toast kedua; Search untuk menemukan baris hasil (R-16); mengosongkan Search lewat `(←)` (S-09).
- Urutan Expected TC-163: butir a (kedua toast) ditulis sebagai satu `Verifikasi` setelah masing-masing submit; butir c ("Code tersimpan tidak pernah kosong") ditulis sebagai `Verifikasi` setelah kedua baris diamati.
- Temuan untuk QA:
  - TC-162 menyebut nama `Panjang 15` sebagai pemegang Code `ABCDEFGHIJKLMNO` dan menyebut "kandidat dipotong ke 14 karakter"; hasil `ABCDEFGHIJKLMN2` diharapkan persis seperti di TC.
  - TC-163 mengetik `***` dan `---` pada Search; TC tidak menyatakan apakah Search memperlakukan karakter tersebut secara literal.
  - Seluruh TC Post Condition (Changelog menulis satu baris Create Field `Category Name`; Code hasil generate tidak menulis baris tersendiri) tanpa langkah observasi di TC sehingga tidak diasersi (S-01). TC-163 tidak memiliki Post Condition.
  - Varian seed per TC (Pre-setup #34) mengubah data bersama; mekanisme penyiapan dan pemulihan tidak tertulis di TC dan disediakan tim FE (S-13).
