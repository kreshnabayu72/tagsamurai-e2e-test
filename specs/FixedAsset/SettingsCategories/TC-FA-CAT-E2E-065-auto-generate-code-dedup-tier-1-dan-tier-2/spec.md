---
id: TC-FA-CAT-E2E-065-auto-generate-code-dedup-tier-1-dan-tier-2
title: "Auto-generate Code: Dedup Tier 1 (Suffix Angka) dan Beralih ke Tier 2 (Prefix Parent Code)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-155
  - TC-FA-CAT-156
  - TC-FA-CAT-157
  - TC-FA-CAT-158
coverage:
  web: automated
---

# Auto-generate Code: Dedup Tier 1 (Suffix Angka) dan Beralih ke Tier 2 (Prefix Parent Code)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatCode (Pre-setup #34) dengan `{namaCompany}` client CatCode, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini (akun pertama spec bukan akun default suite); halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatCode (#34) keadaan dasar: kategori L1 `Dedup 1` sampai `Dedup 7` ber-Code `ELEC` sampai `ELEC7`, `Parent Kode` (Code `PAR`, internal), `Parent Panjang` (Code `PARENTCODE0001`), `Parent Lima` (Code `PRNT1`), dan `Panjang 15` (Code `ABCDEFGHIJKLMNO`). Hook `before` memastikan keadaan dasar dan hook `after` memulihkannya lewat seed API (disediakan tim FE).
- Varian seed #34 per TC (diatur lewat seed API di langkah penghubung; disediakan tim FE, tanpa endpoint karangan):

  | TC | Code yang sudah dipakai | Parent |
  |---|---|---|
  | TC-155 | hanya `ELEC` | root |
  | TC-156 | `ELEC` sampai `ELEC4` | root |
  | TC-157 | `ELEC` sampai `ELEC6` | `Parent Kode` |
  | TC-158 | `ELEC` sampai `ELEC7` | `Parent Kode` |

- Data yang dibuat spec lewat UI: kategori `Elec` (Category Name literal tanpa suffix karena Code hasil generate diturunkan dari nama itu; ini pengecualian nama literal atas S-12, dan suite berjalan serial). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE). Hook `before` menghapus sisa kategori `Elec` dari run lain atau spec lain (R-13); setiap TC menghapus `Elec` TC sebelumnya lewat seed API sebelum varian berikutnya; hook `after` menghapus sisa.
- Kemampuan teknis: pembacaan kolom Code pada tabel Categories List.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-155: Auto-generate Code: bentrok keunikan memakai suffix angka mulai 2 (Tier 1)

1. Siapkan varian #34: hanya Code `ELEC` terpakai (seed API), lalu muat ulang halaman
2. Klik `[+] Category` pada sidebar
3. Isi Category Name `Elec` dan biarkan Code kosong
4. Klik `[Submit]`
5. Verifikasi toast `Success, category has been created.`
6. Ketik Search `Elec`, tekan Enter
7. Verifikasi baris `Elec` tampil di tabel (kategori tersimpan)
8. Verifikasi kolom Code baris `Elec` berisi `ELEC2` (kandidat `ELEC` sudah dipakai sehingga suffix angka tanpa pemisah mulai 2)
9. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
10. Klik `(←)` pada kotak Search

### TC-FA-CAT-156: Auto-generate Code: suffix naik berurutan sampai menemukan Code bebas

11. Hapus kategori `Elec` hasil TC sebelumnya dan siapkan varian #34: Code `ELEC` sampai `ELEC4` terpakai (seed API), lalu muat ulang halaman
12. Klik `[+] Category` pada sidebar
13. Isi Category Name `Elec` dan biarkan Code kosong
14. Klik `[Submit]`
15. Verifikasi toast `Success, category has been created.`
16. Ketik Search `Elec`, tekan Enter
17. Verifikasi baris `Elec` tampil di tabel (kategori tersimpan)
18. Verifikasi kolom Code baris `Elec` berisi `ELEC5` (`ELEC`, `ELEC2`, `ELEC3`, `ELEC4` sudah dipakai sehingga suffix berikutnya `5`)
19. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
20. Klik `(←)` pada kotak Search

### TC-FA-CAT-157: Auto-generate Code: suffix ke-6 masih Tier 1 walau parent punya Code

21. Hapus kategori `Elec` hasil TC sebelumnya dan siapkan varian #34: Code `ELEC` sampai `ELEC6` terpakai (seed API), lalu muat ulang halaman
22. Klik node `All Categories` di sidebar
23. Ketik Search `Parent Kode`, tekan Enter
24. Klik elipsis (⋯) pada baris `Parent Kode` > `+ Add Subcategory`
25. Isi Category Name `Elec` dan biarkan Code kosong
26. Klik `[Submit]`
27. Verifikasi toast `Success, category has been created.`
28. Klik node `Parent Kode` di sidebar
29. Verifikasi baris `Elec` tampil di tabel (kategori tersimpan)
30. Verifikasi kolom Code baris `Elec` berisi `ELEC7` (kandidat polos tidak dihitung sebagai percobaan dan suffix `2` sampai `6` bentrok, sehingga `ELEC7` adalah percobaan ke-6 Tier 1)
31. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user

### TC-FA-CAT-158: Auto-generate Code: Tier 1 gagal lebih dari 5 percobaan dan parent punya Code memakai prefix Parent Code (Tier 2)

32. Hapus kategori `Elec` hasil TC sebelumnya dan siapkan varian #34: Code `ELEC` sampai `ELEC7` terpakai (seed API), lalu muat ulang halaman
33. Klik node `All Categories` di sidebar
34. Ketik Search `Parent Kode`, tekan Enter
35. Klik elipsis (⋯) pada baris `Parent Kode` > `+ Add Subcategory`
36. Isi Category Name `Elec` dan biarkan Code kosong
37. Klik `[Submit]`
38. Verifikasi toast `Success, category has been created.`
39. Klik node `Parent Kode` di sidebar
40. Verifikasi baris `Elec` tampil di tabel (kategori tersimpan)
41. Verifikasi kolom Code baris `Elec` berisi `PAR-ELEC` (enam percobaan suffix `2` sampai `7` bentrok dan parent `Parent Kode` ber-Code `PAR`, sehingga Tier 2 `[Parent Code]-[Candidate]`)
42. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-155 sampai TC-158 ada di spec ini; TC-159, TC-160, dan TC-161 ada di spec 066; TC-162 dan TC-163 ada di spec 067.
- Spec ini melewati sekitar 35 langkah karena Expected ditulis per klausa (S-01) dan tiap blok menyiapkan varian seed sendiri. Keempat blok berkelas fungsional yang sama (dedup Code), masing-masing memakai varian seed dan kategori `Elec` sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Nama literal `Elec` tanpa suffix (S-12, pengecualian khusus): Code diturunkan dari Category Name, sehingga suffix `{runId}` akan mengubah Code yang diuji. Syaratnya dipenuhi lewat Prerequisites.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): penyiapan varian seed dan penghapusan `Elec` sebelumnya; memuat ulang halaman; memilih node `All Categories` agar Search mencari di root; Search untuk menemukan baris target (R-16); memilih node `Parent Kode` agar tabel menampilkan anak (subcategory) hasil Submit (Search di root tidak menampilkan anak, S-14); mengosongkan Search lewat `(←)` (S-09).
- Urutan TC-155 sampai TC-158 sama dengan urutan TC sumber; varian seed makin banyak Code terpakai sehingga penyiapan varian berikutnya tidak bergantung pada hasil TC sebelumnya.
- Temuan untuk QA:
  - TC-157 dan TC-158 tidak menyebut navigasi ke node `Parent Kode` untuk melihat baris hasil ("Perhatikan kolom Code pada baris hasil"); spec menambah langkah memilih node `Parent Kode`.
  - Search `Elec` pada TC-155 dan TC-156 turut mencocokkan baris `Dedup 1` dan seterusnya (Code `ELEC...` searchable); asersi hanya pada baris bernama `Elec`.
  - Seluruh TC Post Condition (Changelog menulis satu baris Create Field `Category Name`; Code hasil generate tidak menulis baris tersendiri) tanpa langkah observasi di TC sehingga tidak diasersi (S-01).
  - Varian seed per TC (Pre-setup #34) mengubah data bersama; mekanisme penyiapan dan pemulihan tidak tertulis di TC dan disediakan tim FE (S-13).
