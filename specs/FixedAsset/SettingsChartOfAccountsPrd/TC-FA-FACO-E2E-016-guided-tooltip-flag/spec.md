---
id: TC-FA-FACO-E2E-016-guided-tooltip-flag
title: "Guided Tooltip muncul sekali per akun pengguna dan tidak muncul lagi sesudah selesai"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.7#b1", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#b1": 6
  "EB-TBL-10": [2, 4, 9, 11, 15, 19, 23, 25, 29]
anchor: [2, 8, 14, 18, 21, 28]
coverage:
  web: automated
---

# Guided Tooltip muncul sekali per akun pengguna dan tidak muncul lagi sesudah selesai

## Prerequisites
- Aktor: Pengguna Tur A (DU-016-1) dan Pengguna Tur B (DU-016-2), dua pengguna yang berbeda.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-016-1: Pengguna Tur A, nama `Pengguna Tur A {runId}`, role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2. Belum pernah membuka halaman Chart of Accounts, sehingga flag tur belum disetel.
  - DU-016-2: Pengguna Tur B, nama `Pengguna Tur B {runId}`, role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2. Belum pernah membuka halaman Chart of Accounts, sehingga flag tur belum disetel.
- Kondisi:
  - Platform web, tampilan desktop.

## Test Steps
### Tur muncul otomatis di kunjungan pertama dan flag disetel sesudah Skip
1. Pengguna Tur A membuka Settings > Accounting > Chart of Accounts untuk pertama kali
2. Verifikasi Guided Tooltip tampil otomatis dengan judul `Account Code` pada step pertama dari enam step
3. Klik `[Skip]`
4. Verifikasi Guided Tooltip tidak tampil lagi sesudah `[Skip]`
5. Arahkan kursor ke tombol `[?]` di kanan Breadcrumb
6. Verifikasi tombol `[?]` tampil di kanan Breadcrumb dengan tooltip `Show guide`

### Flag bertahan sesudah muat ulang halaman dan replay tidak mereset flag
7. Muat ulang halaman
8. Verifikasi header kolom `Account Code` tampil di halaman Chart of Accounts
9. Verifikasi Guided Tooltip tidak tampil sesudah muat ulang halaman
10. Klik tombol `[?]` di kanan Breadcrumb
11. Verifikasi Guided Tooltip tampil dari step pertama dengan judul `Account Code`
12. Klik `[Skip]`
13. Muat ulang halaman
14. Verifikasi header kolom `Account Code` tampil sesudah muat ulang kedua
15. Verifikasi Guided Tooltip tidak tampil sesudah replay dan muat ulang karena flag tidak direset

### Flag mengikuti akun pengguna di browser lain
16. Pengguna Tur A masuk di browser lain dengan profil baru tanpa penyimpanan lokal
17. Buka Settings > Accounting > Chart of Accounts di browser lain
18. Verifikasi header kolom `Account Code` tampil di browser lain
19. Verifikasi Guided Tooltip tidak tampil di browser lain karena flag tersimpan di akun

### Keluar tanpa selesai tidak menyetel flag dan Done menyetelnya
20. Pengguna Tur B membuka Settings > Accounting > Chart of Accounts untuk pertama kali
21. Verifikasi Guided Tooltip tampil otomatis dengan judul `Account Code` pada step pertama
22. Muat ulang halaman saat Guided Tooltip masih terbuka
23. Verifikasi Guided Tooltip tampil kembali dengan judul `Account Code` karena flag belum disetel
24. Klik `[Next]` sebanyak lima kali sampai step terakhir
25. Verifikasi tombol `[Done]` tampil pada step terakhir
26. Klik `[Done]`
27. Muat ulang halaman
28. Verifikasi header kolom `Account Code` tampil sesudah `[Done]`
29. Verifikasi Guided Tooltip tidak tampil sesudah `[Done]` dan muat ulang halaman
