---
id: TC-FA-CAT-E2E-002-navigasi-sidebar-tree-dan-context-header
title: "Perilaku Klik Node Sidebar, Category Context Header, dan Empty State Leaf"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-5
  - TC-FA-CAT-6
  - TC-FA-CAT-7
  - TC-FA-CAT-8
  - TC-FA-CAT-9
coverage:
  web: automated
---

# Perilaku Klik Node Sidebar, Category Context Header, dan Empty State Leaf

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise): 15 kategori; L1 `Accessory`, `Default Category`, `Electronics` (anak `Laptop`, `Monitor`), `Furniture`, `Peripheral` (anak `Keyboard`, `Mouse`), `Spare Part`, `Tools`, `Vehicle`. Spec hanya membaca; tidak membuat atau mengubah data.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-5: Urutan node sidebar alfabetis A-Z per level parent

1. Klik toggle expand-all pada header sidebar
2. Verifikasi node L1 berurut: `Accessory`, `Default Category`, `Electronics`, `Furniture`, `Peripheral`, `Spare Part`, `Tools`, `Vehicle`
3. Verifikasi anak `Electronics` berurut `Laptop` lalu `Monitor`
4. Verifikasi anak `Peripheral` berurut `Keyboard` lalu `Mouse`

### TC-FA-CAT-7: Klik All Categories menampilkan level 1 dan header agregat distinct seluruh tree

5. Klik node `Electronics`
6. Klik root `All Categories`
7. Verifikasi tabel menampilkan hanya kategori level 1 (8 baris L1 sesuai Pre-setup #20)
8. Verifikasi Category Context Header menampilkan teks `All Categories`
9. Verifikasi Category Context Header menampilkan Total Asset agregat distinct seluruh tree (aset yang menunjuk beberapa node dihitung sekali)
10. Verifikasi Total Asset agregat tampil sebagai teks biasa tanpa tautan
11. Catat Total Asset pada baris `Electronics` di tabel L1

### TC-FA-CAT-6: Klik node sidebar memfilter tabel ke direct children saja dan memperbarui Context Header

12. Klik node `Electronics` di sidebar
13. Verifikasi tabel memuat tepat dua baris direct children: `Laptop` dan `Monitor`
14. Verifikasi tabel tidak memuat kategori L1 lain dan tidak memuat descendant lebih dalam
15. Verifikasi Category Context Header menampilkan nama exact `Electronics` (bukan full path)
16. Verifikasi Total Asset pada Category Context Header `0` (exact-match node itu sendiri, bukan agregat 12 aset `Laptop`)
17. Verifikasi Total Asset pada Category Context Header sama dengan angka yang dicatat pada langkah 11 (baris `Electronics` pada tabel L1)
18. Klik node `Laptop` (leaf)
19. Verifikasi Category Context Header menampilkan `Laptop` dengan Total Asset `12`
20. Verifikasi tabel menampilkan empty state S-12

### TC-FA-CAT-8: Klik node yang sudah terpilih tidak melakukan apa pun

21. Klik node `Electronics`
22. Catat tampilan tabel, Category Context Header, dan seleksi sidebar
23. Klik node `Electronics` sekali lagi
24. Verifikasi tampilan tabel, Category Context Header, dan seleksi sidebar tidak berubah dari yang dicatat
25. Verifikasi state tabel (Search, Sort, Filter) tetap
26. Verifikasi tidak ada toast atau dialog

### TC-FA-CAT-9: Node leaf tanpa subkategori menampilkan empty state S-12

27. Klik node `Monitor` (leaf) di sidebar
28. Verifikasi area tabel menampilkan ilustrasi, Title `No subcategory yet`, dan Description `This category does not have any subcategories.`
29. Verifikasi tidak ada tombol CTA create di empty state
30. Verifikasi Category Context Header menampilkan `Monitor` dengan Total Asset `0`

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Penyimpangan urutan (S-10): TC-FA-CAT-7 diletakkan sebelum TC-FA-CAT-6 agar Total Asset baris `Electronics` pada tabel L1 sudah dicatat (langkah 11, tanpa `Verifikasi`) sebelum dibandingkan dengan Category Context Header pada TC-FA-CAT-6. Urutan akhir: TC-FA-CAT-5, 7, 6, 8, 9. Sidebar dibiarkan terbuka penuh (expand-all dari TC-FA-CAT-5) karena TC-FA-CAT-9 membutuhkan node `Monitor` terlihat.
- Langkah 11 adalah langkah pencatatan (S-03).
- Temuan untuk QA:
  - TC-FA-CAT-6 butir b menyebut angka Total Asset `Electronics` sama dengan baris pada tabel L1 tanpa langkah menuju tabel L1; spec membandingkannya dengan angka yang dicatat di TC-FA-CAT-7 (S-14).
  - TC-FA-CAT-7 butir b tidak menyebut nilai Total Asset agregat; spec memverifikasi bahwa agregat distinct tampil sebagai teks biasa tanpa tautan, tanpa angka.
  - TC-FA-CAT-6 butir c menyebut empty state S-12 tanpa copy; copy `No subcategory yet` dan `This category does not have any subcategories.` diasersi di TC-FA-CAT-9.
  - TC-FA-CAT-8 butir b (state Search/Sort/Filter tetap) tidak menetapkan state sebelum klik kedua; spec memeriksa state default tidak berubah.
- Ukuran spec 30 langkah, di bawah ambang sekitar 35.
