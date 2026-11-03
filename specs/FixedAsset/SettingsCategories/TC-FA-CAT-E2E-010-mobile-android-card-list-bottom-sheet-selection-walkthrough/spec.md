---
id: TC-FA-CAT-E2E-010-mobile-android-card-list-bottom-sheet-selection-walkthrough
title: "Mobile Android: Card List, Bottom Sheet Tree, Selection Mode, dan Walkthrough"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-26
  - TC-FA-CAT-270
  - TC-FA-CAT-640
  - TC-FA-CAT-642
coverage:
  mobile: automated
---

# Mobile Android: Card List, Bottom Sheet Tree, Selection Mode, dan Walkthrough

## Prerequisites

- Mode: FE+BE. Platform: aplikasi mobile Android Fixed Asset > Settings > Categories.
- Perangkat atau emulator Android dengan aplikasi Fixed Asset TAG Samurai terpasang, serta kemampuan mengetuk, long-press, dan menekan elemen UI. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di aplikasi Android di hook `before` spec ini; spec ini membuka halaman Categories sendiri di aplikasi karena hook `beforeEach` suite membuka halaman web. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise): 15 kategori; L1 `Accessory`, `Default Category`, `Electronics` (anak `Laptop`, `Monitor`), `Furniture`, `Peripheral` (anak `Keyboard`, `Mouse`), `Spare Part`, `Tools`, `Vehicle`.
- Pengecualian atas butir Flag Guided Tooltip di `suite.md`: spec ini mengatur flag `guided_tooltip_seen_fa-settings-categories` sendiri sesudah hook (menghapus flag dengan langkah eksplisit); kemampuan mengatur dan menghapus flag disediakan tim FE/BE. Hook suite `after` memulihkan flag ke true. Spec memakai flag true untuk TC-FA-CAT-26 dan TC-FA-CAT-270, dan menghapusnya di langkah 21 serta di awal tiap iterasi langkah 28 sampai 33.
- Varian penutupan walkthrough Android (TC-FA-CAT-642):
  | Varian | Cara menutup walkthrough |
  |---|---|
  | Done | Ketuk `[Next]` sampai step terakhir lalu ketuk `[Done]` |
  | Skip | Ketuk `[Skip]` pada Step 1 |
  | Overlay | Ketuk overlay gelap pada Step 1 |
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.

## Test Steps

### TC-FA-CAT-26: Mobile Android: Card List mengganti tabel dengan field kunci dan Bottom Sheet Tree

1. Buka halaman Categories pada aplikasi Android
2. Verifikasi Mobile TopBar menampilkan `Settings > Categories`, icon buka Bottom Sheet Tree, dan icon Changelog di header halaman
3. Verifikasi Card List menggantikan tabel
4. Verifikasi tiap card memuat nama, Code, Total Asset, Modified By atau Updated, dan elipsis (⋯) tanpa checkbox permanen
5. Ketuk icon pohon di Mobile TopBar
6. Verifikasi Bottom Sheet Tree menampilkan seluruh hierarki untuk navigasi cepat
7. Ketuk node `Electronics` pada Bottom Sheet Tree
8. Verifikasi Category Context Chip menampilkan konteks node `Electronics`
9. Verifikasi card menampilkan direct children `Electronics`
10. Verifikasi tombol `[+ Category]` tetap terlihat di bawah toolbar dan di atas Card List

### TC-FA-CAT-270: Mobile Android: long-press masuk selection mode dengan Floating Bottom Bulk Bar

11. Ketuk icon pohon lalu ketuk root `All Categories` pada Bottom Sheet Tree
12. Long-press card `Vehicle`
13. Verifikasi selection mode aktif: checkbox muncul di kiri tiap card
14. Verifikasi Floating Bottom Bulk Bar tampil dengan (✕), counter, `Select All`, dan aksi Delete
15. Tap card `Tools`
16. Verifikasi tap card selama selection mode men-toggle checkbox
17. Verifikasi tap card tidak membuka Detail
18. Ketuk (✕) pada bar
19. Verifikasi selection mode berakhir
20. Verifikasi checkbox hilang

### TC-FA-CAT-640: Walkthrough dimulai saat drawer Bottom Sheet Tree tertutup (Android): drawer dibuka otomatis selama Step 1 dan Step 1 tidak dilewati

21. Hapus flag `guided_tooltip_seen_fa-settings-categories`
22. Buka ulang halaman Categories pada aplikasi Android dengan drawer Bottom Sheet Tree tertutup
23. Verifikasi drawer Bottom Sheet Tree terbuka otomatis sehingga target Sidebar Category Tree terlihat
24. Verifikasi walkthrough dimulai dari Step 1 (tidak dilewati ke Step 2) dengan indikator `Step 1 of 3`
25. Verifikasi Step 1 menyorot Sidebar Category Tree dengan Title `Category Tree` dan Description `Use this tree to navigate the category hierarchy and add new categories.`
26. Verifikasi penomor step tidak berubah akibat pembukaan drawer (tetap `Step 1 of 3`)
27. Ketuk `[Skip]`

### TC-FA-CAT-642: Setelah walkthrough selesai, di-skip, atau ditutup, drawer Bottom Sheet Tree kembali tertutup (Android)

28. Hapus flag `guided_tooltip_seen_fa-settings-categories`
29. Buka ulang halaman Categories pada aplikasi Android dengan drawer tertutup sehingga walkthrough muncul otomatis
30. Tutup walkthrough sesuai kolom "Cara menutup walkthrough" pada tabel Varian penutupan Android
31. Verifikasi walkthrough berakhir
32. Verifikasi drawer Bottom Sheet Tree kembali tertutup
33. Verifikasi drawer tidak tertinggal terbuka setelah tur

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Spec berjalan di aplikasi Android; `coverage.mobile: automated`.
- Langkah penghubung (S-03): langkah 11 (kembali ke konteks `All Categories` agar card `Vehicle` dan `Tools` tampil), langkah 27 (menutup walkthrough dengan `[Skip]`).
- Langkah berulang (bagian 8b butir 7): untuk setiap baris tabel Varian penutupan Android, ulangi langkah 28 sampai 33 (tiga iterasi: Done, Skip, Overlay). Ambang ukuran dihitung dengan ekspansi.
- Temuan untuk QA:
  - TC-FA-CAT-26 butir c: Bottom Sheet Tree menutup atau tidak setelah node dipilih tidak disebut TC; spec tidak mengasersinya.
  - TC-FA-CAT-642 menulis flag direset sebelum tiap varian; mekanisme reset disediakan tim FE/BE.
- Ukuran spec 33 langkah nominal (dengan ekspansi tiga iterasi sekitar 40), melewati sekitar 35 karena Expected dipecah per klausa (S-01). Seluruh blok satu platform dan satu dataset (Android, CatMain), tanpa aksi tulis; tiap blok berdiri sendiri lewat penghapusan flag atau konteks yang dipulihkan; spec tidak dipecah (konvensi bagian 3, batas ukuran).
