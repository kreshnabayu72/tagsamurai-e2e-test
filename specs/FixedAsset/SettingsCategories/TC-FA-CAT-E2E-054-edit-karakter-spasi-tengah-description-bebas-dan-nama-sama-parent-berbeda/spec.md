---
id: TC-FA-CAT-E2E-054-edit-karakter-spasi-tengah-description-bebas-dan-nama-sama-parent-berbeda
title: "Edit Category: Reserved Word dengan Dua Spasi, Karakter Bebas pada Description dan Name, serta Nama Sama di Parent Berbeda"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-535
  - TC-FA-CAT-537
  - TC-FA-CAT-532
  - TC-FA-CAT-632
coverage:
  web: automated
---

# Edit Category: Reserved Word dengan Dua Spasi, Karakter Bebas pada Description dan Name, serta Nama Sama di Parent Berbeda

## Prerequisites

- Mode: FE+BE (backend nyata; nilai tersimpan diasersi lewat UI, Changelog, dan pembacaan state BE).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data milik spec (seed lewat API di hook `before`, disediakan tim FE/BE): kategori L1 leaf `Furniture {runId}-054` (Code `FURN054`, Total Asset 0) menjadi target Edit pada TC-FA-CAT-535, 537, 532; parent `Peripheral Own {runId}-054` dengan anak `Keyboard {runId}-054` (Code `KB054`) menjadi target Edit pada TC-FA-CAT-632; parent `Electronics Own {runId}-054` dengan anak `Laptop {runId}-054` adalah nama pembanding di parent berbeda (S-06). Semua blok menyimpan perubahan. Pemulihan `Furniture {runId}-054` dan `Keyboard {runId}-054` (Name, Code, Description) ke nilai seed lewat API dijalankan sebagai langkah penghubung sesudah tiap blok yang menyimpan; hook `after` menghapus seluruh data milik spec. Hook `before` juga membersihkan kategori ber-Code literal `FURN054` dan `KB054` yang tersisa dari run sebelumnya sebelum seed. Data Pre-setup #20 tidak diubah. Efek: entri Changelog CatMain bertambah (audit trail permanen; hanya selisih terhadap baseline yang diasersi); suite berjalan serial.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline, S-12) dan membaca state BE kategori; disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-535: Dua spasi di tengah nama reserved tidak dinormalisasi sehingga diterima

1. Klik elipsis (⋯) pada baris `Furniture {runId}-054` > `Edit`
2. Ubah Category Name menjadi `All  Categories` (dua spasi di tengah)
3. Klik `[Save]`
4. Verifikasi tidak ada error reserved word
5. Verifikasi toast `Success, category has been updated.` tampil
6. Verifikasi nama tersimpan `All  Categories` dengan dua spasi di tengah (dibaca dari state BE)
7. Pulihkan `Furniture {runId}-054` ke nilai seed lewat API dan muat ulang halaman Categories

### TC-FA-CAT-537: Description menerima karakter bebas tanpa batasan karakter

8. Klik elipsis (⋯) pada baris `Furniture {runId}-054` > `Edit`
9. Isi Description `Catatan @#%& (uji) / 100% <ok>`
10. Klik `[Save]`
11. Verifikasi toast `Success, category has been updated.` tampil
12. Buka Popup Detail `Furniture {runId}-054` lewat elipsis (⋯) pada baris `Furniture {runId}-054` > `Detail`
13. Verifikasi Description tampil persis `Catatan @#%& (uji) / 100% <ok>` di Popup Detail
14. Klik icon close (✕) pada Popup Detail
15. Pulihkan `Furniture {runId}-054` ke nilai seed lewat API

### TC-FA-CAT-532: Tanda baca dan simbol umum diizinkan pada Category Name

16. Klik elipsis (⋯) pada baris `Furniture {runId}-054` > `Edit`
17. Isi Category Name `IT & Network (Core) - 2/3: A+B`
18. Klik `[Save]`
19. Verifikasi nilai tersimpan persis `IT & Network (Core) - 2/3: A+B` tanpa error karakter terlarang
20. Verifikasi toast `Success, category has been updated.` tampil
21. Pulihkan `Furniture {runId}-054` ke nilai seed lewat API

### TC-FA-CAT-632: Category Name sama dengan kategori di parent berbeda diterima

22. Catat baseline jumlah entri Changelog kategori (N1)
23. Klik node `Peripheral Own {runId}-054` di Sidebar Category Tree
24. Klik elipsis (⋯) pada baris `Keyboard {runId}-054` > `Edit`
25. Ubah Category Name menjadi `Laptop {runId}-054` (nama yang sudah ada di bawah `Electronics Own {runId}-054`)
26. Klik `[Save]`
27. Verifikasi tidak ada error duplikat
28. Verifikasi toast `Success, category has been updated.` tampil
29. Verifikasi `Keyboard {runId}-054` tampil sebagai `Laptop {runId}-054` di bawah `Peripheral Own {runId}-054`
30. Verifikasi Code `KB054` tidak berubah
31. Klik icon Changelog di Table Tools
32. Verifikasi jumlah entri Changelog bertambah satu dari N1 dan entri baru berupa satu baris Edit Field `Category Name` Old Value `Keyboard {runId}-054` New Value `Laptop {runId}-054`
33. Tutup modal Changelog
34. Pulihkan `Keyboard {runId}-054` ke nilai seed lewat API
35. Klik node `All Categories` di Sidebar Category Tree

## Notes

- Mode: FE+BE. Empat blok berdiri sendiri (Edit yang berhasil disimpan dengan nilai batas bebas) sehingga jumlah langkah (35) berada di sekitar batas.
- Langkah penghubung (S-03, S-09): langkah 7, 15, 21, 34 (memulihkan target ke nilai awal; langkah 7 disusul muat ulang halaman Categories agar daftar memakai nama seed sebelum langkah 8), langkah 14 (menutup Popup Detail), langkah 22, 31, 33 (baseline log, membuka dan menutup Changelog), langkah 23 dan 35 (memilih node `Peripheral Own {runId}-054` lalu kembali ke `All Categories`).
- Temuan untuk QA:
  - TC-FA-CAT-535 tidak menyebut cara membaca "nama tersimpan" dengan dua spasi di tengah (spasi ganda tidak terlihat di tabel); spec membacanya dari state BE sebagai kemampuan disediakan tim FE/BE.
  - TC-FA-CAT-532 menyatakan nilai tersimpan "persis seperti diketik" tanpa langkah observasi; spec memakai tampilan baris sesudah Save.
  - TC-FA-CAT-535, 537, 532, dan 632 menyebut baris Pre-setup `Furniture`, `Keyboard`, dan `Laptop` sebagai target atau pembanding; spec memakai kategori milik spec bersuffix `{runId}-054` (S-06) agar data Pre-setup tidak berubah.
