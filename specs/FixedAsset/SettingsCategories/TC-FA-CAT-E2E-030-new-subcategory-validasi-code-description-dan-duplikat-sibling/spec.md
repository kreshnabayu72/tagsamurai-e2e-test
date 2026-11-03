---
id: TC-FA-CAT-E2E-030-new-subcategory-validasi-code-description-dan-duplikat-sibling
title: "New Subcategory: Duplikat Nama Sibling, Duplikat Code, Whitelist Code, serta Batas Panjang Code dan Description"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-91
  - TC-FA-CAT-101
  - TC-FA-CAT-102
  - TC-FA-CAT-103
  - TC-FA-CAT-104
coverage:
  web: automated
---

# New Subcategory: Duplikat Nama Sibling, Duplikat Code, Whitelist Code, serta Batas Panjang Code dan Description

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), dibaca: parent `Peripheral` (Internal) dengan anak `Keyboard` (Code `PERI-KB`) dan `Mouse`; `Laptop` dengan Code `ELEC-LT` di parent berbeda.
- Data Dinamis (dibuat spec): subcategory `Code Max sub {runId}-030` (Code 15 karakter `A`) dan `Desc Max sub {runId}-030` (Description 360 karakter `D`). Hook `before` menghapus sisa kategori ber-Code 15 karakter `A` di bawah `Peripheral`; hook `after` menghapus kedua subcategory. Seed dan pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-91: Nama duplikat di antara sibling ditolak real-time

1. Klik elipsis (⋯) pada baris `Peripheral` > `+ Add Subcategory`
2. Ketik Category Name `Keyboard`, lalu tunggu 500ms tanpa berpindah fokus
3. Verifikasi pesan `Category name already exists` tampil sekitar 500ms setelah berhenti mengetik tanpa menunggu kursor keluar dari field
4. Klik `[Submit]`
5. Verifikasi Submit diblok: popup tetap terbuka
6. Kosongkan field Category Name

### TC-FA-CAT-103: Code duplikat di seluruh client ditolak real-time

7. Isi Category Name `Dup Code Sub {runId}-030`
8. Ketik Code `ELEC-LT`, lalu tunggu 500ms
9. Verifikasi pesan `Code already exists` tampil sekitar 500ms setelah berhenti mengetik (keunikan per client, bukan per parent)
10. Klik `[Submit]`
11. Verifikasi Submit diblok: popup tetap terbuka
12. Kosongkan field Category Name dan Code

### TC-FA-CAT-102: Karakter di luar whitelist pada Code

13. Ketik Code `AB C!`
14. Verifikasi pesan `Code contains invalid characters` tampil langsung saat mengetik
15. Verifikasi karakter tidak diblok (field Code menampilkan `AB C!`)
16. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` digantikan oleh pesan error selama error aktif
17. Kosongkan field Code

### TC-FA-CAT-101: Code 15 dan 16 karakter

18. Isi Category Name `Code Max sub {runId}-030`
19. Isi Code 15 karakter `A`
20. Klik `[Submit]`
21. Klik node `Peripheral` di Sidebar Category Tree
22. Verifikasi kategori `Code Max sub {runId}-030` tersimpan dengan Code 15 karakter `A` (diterima)
23. Klik elipsis (⋯) pada node `Peripheral` di sidebar > `+ Add Subcategory`
24. Isi Category Name `Code Max16 sub {runId}-030` dan Code 16 karakter `A`
25. Verifikasi pesan `Max. 15 characters` tampil langsung saat melebihi batas
26. Klik `[Submit]`
27. Verifikasi Submit diblok: popup tetap terbuka
28. Klik `✕` pada popup
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`

### TC-FA-CAT-104: Description 360 dan 361 karakter

31. Klik elipsis (⋯) pada node `Peripheral` di sidebar > `+ Add Subcategory`
32. Isi Category Name `Desc Max sub {runId}-030` dan Description 360 karakter `D`
33. Klik `[Submit]`
34. Verifikasi kategori `Desc Max sub {runId}-030` tersimpan dengan Description 360 karakter (diterima)
35. Klik elipsis (⋯) pada node `Peripheral` di sidebar > `+ Add Subcategory`
36. Isi Category Name `Desc Max361 sub {runId}-030` dan Description 361 karakter `D`
37. Verifikasi pesan `Max. 360 characters` tampil langsung
38. Klik `[Submit]`
39. Verifikasi Submit diblok: popup tetap terbuka
40. Klik `✕` pada popup
41. Verifikasi dialog `Unsaved Changes` tampil
42. Klik `[Leave]`

## Notes

- Alasan di atas sekitar 35 langkah: kelima TC bertopik sama (validasi field New Subcategory pada parent `Peripheral`), setiap blok TC dimulai dari popup kosong dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan pemisahan hanya menambah login serta cleanup.
- Langkah penghubung (S-03): langkah 6, 12, 17 (mengosongkan field antar-TC, R-12); langkah 21 (membaca hasil di node `Peripheral`); langkah 28 sampai 30 dan 40 sampai 42 (menutup form dirty, S-08).
- Pembukaan popup berikutnya memakai elipsis node sidebar `Peripheral` karena node itu sedang terpilih; TC menyebut "baris `Peripheral`".
- Temuan untuk QA:
  - TC-103 mengklik `[Submit]` tanpa menyebut Category Name wajib; spec mengisi Category Name `Dup Code Sub {runId}-030` agar yang menahan Submit adalah Code duplikat.
  - TC-102 menyebut "helper text digantikan pesan error" tanpa menulis teks helper; spec memakai teks helper dari TC-FA-CAT-525.
  - TC-91, 101, 103, 104 menyebut "Submit diblok" tanpa wujud pemblokiran; spec mengasersi popup tetap terbuka.
  - TC-101 dan TC-104 tidak menyebut Category Name untuk percobaan 16 dan 361 karakter; spec mengisinya agar hanya batas panjang yang menahan Submit.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
