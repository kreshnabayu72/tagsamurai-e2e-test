---
id: TC-FA-CAT-E2E-033-add-subcategory-sukses-leaf-ke-internal-dan-keluar-empty-state
title: "Add Subcategory Sukses: Leaf Menjadi Internal, Aset Existing Tidak Berubah, dan Keluar dari Empty State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-111
  - TC-FA-CAT-112
  - TC-FA-CAT-530
coverage:
  web: automated
---

# Add Subcategory Sukses: Leaf Menjadi Internal, Aset Existing Tidak Berubah, dan Keluar dari Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data milik spec (seed lewat API di hook `before`, disediakan tim FE/BE): leaf L1 `Vehicle {runId}-033` (Total Asset 0), leaf L1 `Monitor {runId}-033` (Total Asset 0, tanpa anak), serta kategori L1 Internal `Electronics Own {runId}-033` dengan anak leaf `Laptop {runId}-033` (12 aset terhitung; ditunjuk Asset Name `Laptop Dell {runId}-033` dan `Laptop HP {runId}-033`).
- Data Pre-setup #20 (CatMain) tidak ditulis: `Laptop`, `Electronics`, dan Asset Name Pre-setup #21 tidak dipakai; seluruh target aksi tulis memakai data milik spec di atas (S-06). Spec menulis ke client CatMain sehingga entri Changelog CatMain bertambah (audit trail permanen; tidak ada asersi jumlah).
- Data Dinamis (dibuat spec): `Truck {runId}-033` (Code `TRK`), `Gaming Laptop {runId}-033` (Code `GLAP`), `Monitor Stand {runId}-033` (Code `MONST`). Hook `before` menghapus sisa kategori ber-Code `TRK`, `GLAP`, `MONST`; hook `after` menghapusnya beserta seluruh data milik spec (kategori seed dan Asset Name-nya).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-111: Leaf menjadi Internal dan parent di-expand

1. Catat Modified By dan Last Updated baris `Vehicle {runId}-033` (baseline)
2. Klik elipsis (⋯) pada baris `Vehicle {runId}-033` > `+ Add Subcategory`
3. Isi Category Name `Truck {runId}-033` dan Code `TRK`
4. Klik `[Submit]`
5. Verifikasi toast `Success, category has been created.` tampil
6. Verifikasi `Vehicle {runId}-033` menjadi Internal seketika
7. Verifikasi node parent di sidebar di-expand sehingga `Truck {runId}-033` terlihat
8. Verifikasi seleksi sidebar tidak berubah (tetap `All Categories`)
9. Verifikasi tabel dan Total Asset di-refresh
10. Verifikasi Modified By baris `Vehicle {runId}-033` sama dengan baseline
11. Verifikasi Last Updated baris `Vehicle {runId}-033` sama dengan baseline

### TC-FA-CAT-112: Transisi Leaf ke Internal tidak memengaruhi aset existing

12. Klik node `Electronics Own {runId}-033` di Sidebar Category Tree
13. Buka Popup Detail `Laptop {runId}-033`, catat Total Asset dan 12 aset pada tabel Assets, lalu tutup Popup Detail
14. Klik elipsis (⋯) pada baris `Laptop {runId}-033` > `+ Add Subcategory`
15. Klik `[Add Subcategory]` pada dialog heads-up
16. Isi Category Name `Gaming Laptop {runId}-033` dan Code `GLAP`
17. Klik `[Submit]`
18. Buka Popup Detail `Laptop {runId}-033`
19. Verifikasi `Laptop {runId}-033` menjadi Internal
20. Verifikasi tabel Assets Popup Detail `Laptop {runId}-033` tetap memuat 12 aset yang sama
21. Verifikasi aset tidak dipindahkan, tidak terkunci, dan tidak berubah
22. Verifikasi Total Asset `Laptop {runId}-033` tetap `12`
23. Tutup Popup Detail

### TC-FA-CAT-530: Keluar dari empty state S-12

24. Klik node `Monitor {runId}-033` (leaf) di sidebar
25. Verifikasi empty state S-12 `No subcategory yet` tampil
26. Klik elipsis (⋯) pada node `Monitor {runId}-033` di sidebar > `+ Add Subcategory`
27. Isi Category Name `Monitor Stand {runId}-033` dan Code `MONST`
28. Klik `[Submit]`
29. Verifikasi toast `Success, category has been created.` tampil
30. Verifikasi empty state `No subcategory yet` hilang
31. Verifikasi tabel menampilkan baris `Monitor Stand {runId}-033`
32. Verifikasi Category Context Header tetap `Monitor {runId}-033`
33. Verifikasi `Monitor {runId}-033` menjadi Internal dan node `Monitor Stand {runId}-033` terlihat di sidebar

## Notes

- Langkah penghubung (S-03): langkah 1 dan 13 (mencatat baseline/nilai awal), 12 (membuka node parent `Electronics Own {runId}-033`), 23 (menutup Popup Detail).
- Heads-up D-05 muncul karena `Laptop {runId}-033` ditunjuk Asset Name (TC-112 langkah 2); teks dialog diasersi di spec 041.
- Post Condition TC-111 dan TC-112 diperiksa hanya bila punya Expected padanan; Changelog satu baris `Vehicle › Truck` pada TC-111 tidak punya langkah observasi di TC sehingga tidak diasersi.
- Temuan untuk QA:
  - TC-111/112/530 memakai data Pre-setup (`Vehicle`, `Monitor`, `Laptop`) yang berubah permanen; spec memakai kategori milik spec setara (S-06), termasuk `Laptop {runId}-033` dengan 12 aset terhitung dan Asset Name yang disediakan tim FE/BE; tidak ada data Pre-setup yang diubah.
  - TC-111 menyebut Post Condition Changelog tanpa langkah observasi.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
