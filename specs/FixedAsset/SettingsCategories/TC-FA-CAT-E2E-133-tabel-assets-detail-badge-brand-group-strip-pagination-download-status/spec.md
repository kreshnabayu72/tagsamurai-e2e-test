---
id: TC-FA-CAT-E2E-133-tabel-assets-detail-badge-brand-group-strip-pagination-download-status
title: "Tabel Assets Popup Detail: Badge Brand, Model/Type, dan Group, Strip Sel Kosong, Pagination, Download, serta Status Multi-Badge"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-433
  - TC-FA-CAT-434
  - TC-FA-CAT-435
  - TC-FA-CAT-436
  - TC-FA-CAT-437
  - TC-FA-CAT-438
coverage:
  web: automated
---

# Tabel Assets Popup Detail: Badge Brand, Model/Type, dan Group, Strip Sel Kosong, Pagination, Download, serta Status Multi-Badge

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- Kemampuan teknis: membaca isi berkas unduhan XLSX (kolom, jumlah baris); disediakan tim FE.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-433: Badge Brand dan Model/Type memotong nama di atas 25 karakter

3. Verifikasi badge Brand `Dell` tampil penuh tanpa hover khusus
4. Verifikasi badge Brand panjang tampil `Hewlett Pack..se Indonesia` (12 huruf pertama + `..` + 12 huruf terakhir)
5. Hover badge Brand `Hewlett Pack..se Indonesia`
6. Verifikasi hover menampilkan nama penuh `Hewlett Packard Enterprise Indonesia`
7. Verifikasi badge Model/Type panjang tampil `Elite Dragon.. Notebook PC` (pola sama)
8. Hover badge Model/Type `Elite Dragon.. Notebook PC`
9. Verifikasi hover menampilkan nama penuh `Elite Dragonfly G3 Notebook PC`
10. Verifikasi badge Model/Type berseverity dark

### TC-FA-CAT-434: Badge Group menampilkan hierarki penuh pada hover

11. Hover badge Group `Head Office > Floor 1 > Room 301`
12. Verifikasi hover menampilkan hierarki penuh `Head Office > Floor 1 > Room 301`
13. Hover badge Group panjang `Jakarta Sela..ution Center`
14. Verifikasi hover menampilkan hierarki penuh `Region Jawa > Jakarta Selatan Distribution Center`
15. Verifikasi badge Group panjang tampil `Jakarta Sela..ution Center` (12 huruf pertama + `..` + 12 huruf terakhir dari nama leaf)
16. Verifikasi badge Group berseverity primary

### TC-FA-CAT-436: Pagination tabel Assets

17. Verifikasi tabel Assets menampilkan 10 baris pada halaman 1
18. Verifikasi 12 aset terbagi dalam 2 halaman
19. Klik dropdown page size
20. Verifikasi opsi page size 10, 25, 50, 100
21. Pilih page size 25
22. Verifikasi tabel menampilkan 12 baris
23. Pilih kembali page size 10

### TC-FA-CAT-435: Sel Brand, Model/Type, dan Group kosong tampil strip

24. Ketik Search `Laptop HP - 4`, tekan Enter
25. Verifikasi sel Brand, Model/Type, dan Group baris `Laptop HP - 4` menampilkan `—`
26. Klik `(←)` pada kotak Search

### TC-FA-CAT-438: Sel Status multi-badge

27. Verifikasi sel Status baris aset ber-Status gabungan `Borrowed` + `Damaged` menampilkan badge hasil Aturan Resolusi Tampilan Status (Custody dengan overlay Condition) dengan palette badge platform

### TC-FA-CAT-437: Download tabel Assets

28. Klik Download > `Download as XLSX`
29. Verifikasi tidak ada toast sukses
30. Verifikasi berkas `Category-Assets.xlsx` terunduh
31. Buka berkas `Category-Assets.xlsx`
32. Verifikasi berkas berisi 12 aset
33. Verifikasi berkas memuat kolom yang visible pada tabel Assets

## Notes

- Mode: FE+BE. Spec memuat enam TC pada satu tabel Assets Popup Detail `Laptop`; Popup Detail dibuka sekali (langkah 1 dan 2) dan dipakai untuk seluruh blok sehingga langkah 33 berada di sekitar batas 35 tanpa pembukaan berulang.
- Urutan blok: TC-FA-CAT-436 didahulukan sebelum TC-FA-CAT-435 supaya hasil Search tidak mengubah halaman yang dihitung pagination.
- Tanpa toast pada unduhan (langkah 29) diasersi segera setelah klik Download dan sebelum `Verifikasi` berkas terunduh; klik format menjadi anchor positif yang buktinya menyusul pada langkah 30 (bagian 8b butir 11 dan butir 5).
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah 23 (mengembalikan page size ke 10), langkah 24 (Search untuk menemukan baris `Laptop HP - 4`, R-16), dan langkah 26 (menutup Search).
- Temuan untuk QA:
  - TC-FA-CAT-435 menyuruh "cari baris aset `Laptop HP - 4`" tanpa cara mencari; spec memakai Search.
  - TC-FA-CAT-438 hanya menyebut "aset ber-Status `Borrowed` + `Damaged`" tanpa nama aset; spec menunjuk baris dengan status gabungan itu sesuai Pre-setup #22.
  - TC-FA-CAT-437 berlabel HINT `f` (binary buffer) dan berada di spec fungsional ini; TC-FA-CAT-593 dan TC-FA-CAT-613 menguji isi berkas lebih dalam di spec lain.
