---
id: TC-FA-CAT-E2E-200-sinkronisasi-asset-name-delete-setelah-pengalihan-category-locked-excess-dan-dropdown-category
title: "Sinkronisasi ke Asset Name: Delete Setelah Pengalihan Kategori, Category Locked pada Kategori Excess, dan Dropdown Category"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-485
  - TC-FA-CAT-482
  - TC-FA-CAT-483
coverage:
  web: automated
---

# Sinkronisasi ke Asset Name: Delete Setelah Pengalihan Kategori, Category Locked pada Kategori Excess, dan Dropdown Category

## Prerequisites

- Mode: FE+BE.
- Akun login hook `before` spec ini: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Satu ganti akun eksplisit pada langkah 13 ke Total Control client CatExcess (Pre-setup #31) dengan `Spectra.env.FA_TC_PASSWORD`.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data milik spec (di-seed hook `before` lewat API; kemampuan seed disediakan tim FE/BE; dibersihkan hook `after`: Asset Name lalu kategori), nama berakhiran `{runId}-200`, client CatMain: `Tools Del {runId}-200` (Code `TD200`, leaf) dengan Asset Name `Drill Del {runId}-200` menunjuknya, dan `Vehicle Del {runId}-200` (Code `VD200`, leaf) sebagai kategori tujuan pengalihan (TC-FA-CAT-485).
- Data Pre-setup client CatExcess (Pre-setup #31, plan Starter, cap 5, 9 kategori): `Electronics` (Internal, usable), `Office` (leaf usable), `Furniture` (leaf Excess, ditunjuk Asset Name `Office Chair`). TC-FA-CAT-482 mengubah Default Label Asset Name Pre-setup `Office Chair` karena status Excess tidak dapat dimiliki spec (S-06 pengecualian 2026-10-30): pemulihan Default Label ke nilai awal dijamin fixture backend (disediakan tim FE/BE) yang dijalankan di hook `before` dan `after`; efeknya (Last Updated Asset Name `Office Chair` dan entri audit trail Edit) tercatat di sini; suite berjalan serial (`parallel: false`).
- Kemampuan teknis: seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite (termasuk akun Total Control CatExcess).

## Test Steps

### TC-FA-CAT-485: Delete diizinkan setelah Asset Name dialihkan ke kategori lain

1. Buka Fixed Asset > Settings > Asset Master > Asset Name
2. Ketik Search `Drill Del {runId}-200`, tekan Enter
3. Klik elipsis (⋯) pada baris `Drill Del {runId}-200` > `Edit`
4. Pilih Category `Vehicle Del {runId}-200` pada `[Select Category]`
5. Klik `[Save]`
6. Tunggu aksi selesai (popup Edit tertutup)
7. Buka Fixed Asset > Settings > Categories
8. Klik elipsis (⋯) pada baris `Tools Del {runId}-200` > `Delete`
9. Verifikasi dialog D-09 tampil (bukan dialog blok D-07)
10. Klik `[Delete]` pada dialog
11. Verifikasi toast `Success, category has been deleted.`
12. Verifikasi `Tools Del {runId}-200` tidak lagi tampil di tabel

### TC-FA-CAT-482: Asset Name pada kategori Excess berstatus Category Locked dan Edit tanpa mengubah Category tetap diterima

13. Ganti akun: logout, lalu login sebagai Total Control (Pre-setup #1) client CatExcess dengan `Spectra.env.FA_TC_PASSWORD`
14. Buka Fixed Asset > Settings > Asset Master > Asset Name
15. Ketik Search `Office Chair`, tekan Enter
16. Verifikasi baris `Office Chair` (Category `Furniture` Excess) berstatus Category Locked
17. Klik elipsis (⋯) pada baris `Office Chair` > `Edit`
18. Ubah Default Label menjadi `Office Chair Label {runId}-200` tanpa mengubah Category
19. Klik `[Save]`
20. Verifikasi Edit diterima: popup Edit tertutup tanpa dialog blokir atau toast error
21. Buka Fixed Asset > Settings > Categories
22. Verifikasi aset existing tidak terpengaruh: Total Asset kategori `Furniture` tetap 5

### TC-FA-CAT-483: Dropdown Category Asset Name: node Internal dan Excess tidak dapat dipilih

23. Buka Fixed Asset > Settings > Asset Master > Asset Name
24. Klik `[+ Asset Name]`
25. Klik `[Select Category]`
26. Verifikasi `Electronics` (Internal) tampil sebagai pengelompokan tetapi tidak dapat dipilih
27. Verifikasi `Furniture` (Excess) tampil sebagai pengelompokan tetapi tidak dapat dipilih
28. Pilih `Office`
29. Verifikasi `Office` (leaf non-Excess) dapat dipilih dan Category terpilih adalah `Office`
30. Klik `✕` pada form `[+ Asset Name]`
31. Verifikasi dialog `Unsaved Changes` tampil
32. Klik `[Leave]`

## Notes

- Spec berisi TC-FA-CAT-485, TC-FA-CAT-482, dan TC-FA-CAT-483; TC-FA-CAT-481, TC-FA-CAT-484, dan TC-FA-CAT-572 ada di spec 170.
- Urutan TC: 485 (CatMain), lalu 482 dan 483 (CatExcess) agar satu ganti akun saja (S-10); TC-FA-CAT-485 menghapus data milik spec sehingga tidak ada data bergantung di blok sesudahnya.
- Langkah penghubung (S-03): langkah 2 dan 15 (Search untuk menemukan baris target), langkah 6 (menunggu aksi selesai sebelum pindah surface), langkah 7, 14, 21, 23 (membuka halaman), langkah 13 (ganti akun), langkah 21 (membuka Categories untuk membaca Total Asset), langkah 30 sampai 32 (menutup form dirty secara deterministik, S-08; `Verifikasi` dialog `Unsaved Changes` diwajibkan S-08 sehingga tidak dicatat sebagai asersi tambahan).
- Anchor langkah 12 (absence baris sesudah Delete): toast sukses langkah 11 (bagian 8b butir 2).
- Langkah 20 memakai definisi "Edit diterima" sebagai tidak adanya penolakan; TC tidak menyebut teks toast Edit Asset Name.
- Langkah 22 mengasersi "aset existing tidak terpengaruh" lewat Total Asset `Furniture` Pre-setup (5 aset); TC tidak menyebut cara cek lain.
- Temuan untuk QA:
  - TC-FA-CAT-482 menyebut Pre-setup #21 dan #31 sekaligus, tetapi Asset Name `Office Chair` menunjuk `Furniture` Excess hanya pada client CatExcess (#31); spec memakai client CatExcess.
  - TC-FA-CAT-482 Expected b ("aset existing tidak terpengaruh") tidak punya langkah observasi; spec memakai Total Asset kategori `Furniture`.
  - TC-FA-CAT-482 tidak menyebut label tombol simpan dan toast hasil; spec memakai `[Save]`.
  - TC-FA-CAT-485 tidak menyebut teks dialog D-09 selain kode; spec mengasersi kode D-09.
  - TC-FA-CAT-483 menyebut "Coba pilih" tanpa Expected untuk kondisi tersimpan; form ditutup lewat `✕` dan `[Leave]`.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
