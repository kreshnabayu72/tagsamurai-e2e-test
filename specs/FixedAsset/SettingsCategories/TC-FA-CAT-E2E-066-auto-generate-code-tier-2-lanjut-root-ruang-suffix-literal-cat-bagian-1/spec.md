---
id: TC-FA-CAT-E2E-066-auto-generate-code-tier-2-lanjut-root-ruang-suffix-literal-cat-bagian-1
title: "Auto-generate Code: Tier 2 Lanjut Suffix, Kategori Root, dan Prefix Parent Tanpa Ruang (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-159
  - TC-FA-CAT-160
  - TC-FA-CAT-161
coverage:
  web: automated
---

# Auto-generate Code: Tier 2 Lanjut Suffix, Kategori Root, dan Prefix Parent Tanpa Ruang (Bagian 1)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatCode (Pre-setup #34) dengan `{namaCompany}` client CatCode, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini (akun pertama spec bukan akun default suite); halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatCode (#34) keadaan dasar: kategori L1 `Dedup 1` sampai `Dedup 7` ber-Code `ELEC` sampai `ELEC7`, `Parent Kode` (Code `PAR`, internal), `Parent Panjang` (Code `PARENTCODE0001`, 14 karakter), `Parent Lima` (Code `PRNT1`), dan `Panjang 15` (Code `ABCDEFGHIJKLMNO`). Hook `before` memastikan keadaan dasar dan hook `after` memulihkannya lewat seed API (disediakan tim FE).
- Varian seed #34 per TC (diatur lewat seed API di langkah penghubung; disediakan tim FE, tanpa endpoint karangan):

  | TC | Code yang sudah dipakai | Parent |
  |---|---|---|
  | TC-159 | `ELEC` sampai `ELEC7` dan `PAR-ELEC` | `Parent Kode` |
  | TC-160 | `ELEC` sampai `ELEC7` | root |
  | TC-161 | `ELEC` sampai `ELEC7` | `Parent Panjang` |

- Data yang dibuat spec lewat UI: kategori `Elec` (Category Name literal tanpa suffix karena Code hasil generate diturunkan dari nama itu; ini pengecualian nama literal atas S-12, dan suite berjalan serial). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE). Hook `before` menghapus sisa kategori `Elec` dari run lain atau spec lain (R-13); setiap TC menghapus `Elec` TC sebelumnya lewat seed API sebelum varian berikutnya; hook `after` menghapus sisa.
- Kemampuan teknis: pembacaan kolom Code pada tabel Categories List.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-159: Auto-generate Code: kombinasi Tier 2 yang bentrok lanjut suffix angka

1. Hapus kategori `Elec` sisa dan siapkan varian #34: Code `ELEC` sampai `ELEC7` dan `PAR-ELEC` terpakai (seed API), lalu muat ulang halaman
2. Klik node `All Categories` di sidebar
3. Ketik Search `Parent Kode`, tekan Enter
4. Klik elipsis (⋯) pada baris `Parent Kode` > `+ Add Subcategory`
5. Isi Category Name `Elec` dan biarkan Code kosong
6. Klik `[Submit]`
7. Verifikasi toast `Success, category has been created.`
8. Klik node `Parent Kode` di sidebar
9. Verifikasi baris `Elec` tampil di tabel (kategori tersimpan)
10. Verifikasi kolom Code baris `Elec` berisi `PAR-ELEC2` (`PAR-ELEC` sudah dipakai sehingga suffix angka berlanjut di atas kombinasi Tier 2)
11. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user

### TC-FA-CAT-160: Auto-generate Code: kategori root tanpa parent tidak memakai Tier 2 dan suffix berlanjut

12. Hapus kategori `Elec` hasil TC sebelumnya dan siapkan varian #34: Code `ELEC` sampai `ELEC7` terpakai (seed API), lalu muat ulang halaman
13. Klik node `All Categories` di sidebar
14. Klik `[+] Category` pada sidebar
15. Isi Category Name `Elec` dan biarkan Code kosong
16. Klik `[Submit]`
17. Verifikasi toast `Success, category has been created.`
18. Ketik Search `Elec`, tekan Enter
19. Verifikasi baris `Elec` tampil di tabel (kategori tersimpan)
20. Verifikasi kolom Code baris `Elec` berisi `ELEC8` (root tanpa parent sehingga Tier 2 dilewati dan suffix berlanjut sampai bebas)
21. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
22. Klik `(←)` pada kotak Search

### TC-FA-CAT-161: Auto-generate Code: Tier 2 dilewati bila prefix parent tidak menyisakan ruang satu karakter

23. Hapus kategori `Elec` hasil TC sebelumnya dan siapkan varian #34: Code `ELEC` sampai `ELEC7` terpakai (seed API), lalu muat ulang halaman
24. Klik node `All Categories` di sidebar
25. Ketik Search `Parent Panjang`, tekan Enter
26. Klik elipsis (⋯) pada baris `Parent Panjang` > `+ Add Subcategory`
27. Isi Category Name `Elec` dan biarkan Code kosong
28. Klik `[Submit]`
29. Verifikasi toast `Success, category has been created.`
30. Klik node `Parent Panjang` di sidebar
31. Verifikasi baris `Elec` tampil di tabel (kategori tersimpan)
32. Verifikasi kolom Code baris `Elec` berisi `ELEC8` (`Parent Panjang` ber-Code `PARENTCODE0001` (14 karakter) sehingga `[Parent Code]-` memakai 15 karakter dan tidak menyisakan ruang)
33. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-159, TC-160, dan TC-161 ada di spec ini; TC-155 sampai TC-158 ada di spec 065; TC-162 dan TC-163 ada di spec 067.
- Nama literal `Elec` tanpa suffix (S-12, pengecualian khusus): Code diturunkan dari Category Name, sehingga suffix `{runId}` akan mengubah Code yang diuji. Syaratnya dipenuhi lewat Prerequisites.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): penyiapan varian seed dan penghapusan `Elec` sebelumnya; memuat ulang halaman; memilih node `All Categories` agar Search atau `[+] Category` bekerja di root; Search untuk menemukan baris target (R-16); memilih node parent agar tabel menampilkan anak hasil Submit (Search di root tidak menampilkan anak, S-14); mengosongkan Search lewat `(←)` (S-09).
- Temuan untuk QA:
  - TC-159 dan TC-161 tidak menyebut navigasi ke node parent untuk melihat baris hasil; spec menambah langkah memilih node parent.
  - TC-160 tidak menyebut apakah kategori `Elec` sisa dari TC sebelumnya (anak `Parent Kode`, Code `PAR-ELEC2`) masih ada; spec menghapusnya sebelum varian berikutnya agar dedup root tidak terpengaruh.
  - TC-161 Expected b menyebut `[Parent Code]-` memakai 15 karakter; `PARENTCODE0001-` memang 15 karakter sehingga tidak menyisakan ruang (konsisten dengan TC).
  - Seluruh TC Post Condition (Changelog menulis satu baris Create Field `Category Name`; Code hasil generate tidak menulis baris tersendiri) tanpa langkah observasi di TC sehingga tidak diasersi (S-01).
  - Varian seed per TC (Pre-setup #34) mengubah data bersama; mekanisme penyiapan dan pemulihan tidak tertulis di TC dan disediakan tim FE (S-13).
