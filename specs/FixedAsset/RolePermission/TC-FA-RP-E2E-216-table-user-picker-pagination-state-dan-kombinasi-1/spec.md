---
id: TC-FA-RP-E2E-216-table-user-picker-pagination-state-dan-kombinasi-1
title: "Table User Picker: Pagination, state, dan kombinasi (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-702
  - TC-FA-RP-703
  - TC-FA-RP-704
coverage:
  web: automated
---

# Table User Picker: Pagination, state, dan kombinasi (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #41 (kandidat popup Assign Total Control, 12 kandidat; di antaranya Yoga Pratama berstatus `Inactive`) dan #36 (Tab Total Control terisi sembilan baris, sebagai tabel utama di belakang popup). Pre-setup #37, #17, dan #23 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data; Pre-setup di-seed ulang di hook `before` dan dipulihkan di hook `after`.

## Test Steps

### Pagination: default dan pilihan ukuran (TC 702)

1. Klik `[+ Assign]`.
2. Verifikasi default 10 data per halaman.
3. Buka Overlay Page Size.
4. Verifikasi pilihan ukuran 10, 25, 50, dan 100 tanpa opsi `All`.
5. Tutup Overlay Page Size.

### Pagination: navigasi halaman dan ganti ukuran (TC 703)

6. Pindah ke halaman 2.
7. Verifikasi data halaman 2 berbeda dari halaman 1 dan melanjutkan urutannya.
8. Ganti ukuran halaman menjadi 25.
9. Verifikasi ganti ukuran halaman kembali ke halaman 1.
10. Catat nama baris pertama pada tabel kandidat.
11. Klik header kolom Name dua kali (Name descending).
12. Verifikasi baris diurutkan menurun menurut Name (Z-A, collation `en-US`, `foundation/process/prd-process/prd-conventions.md §9.7`).
13. Verifikasi nama baris pertama berbeda dari nama baris pertama yang dicatat pada langkah 10.
14. Verifikasi sort tetap pada halaman yang sedang dibuka.

### Popup tertutup saat F5 dan dibuka dengan state default (TC 704)

15. Tutup popup Assign.
16. Catat jumlah baris dan urutan baris list Tab `Total Control` pada halaman utama.
17. Klik `[+ Assign]`.
18. Ketik Search `a`, tekan Enter.
19. Terapkan Filter Status `Active` (klik ikon Filter, pilih opsi `Active` pada field Status, klik `[Apply]`).
20. Klik header kolom Name dua kali (Name descending).
21. Pindah ke halaman 2.
22. Muat ulang halaman (F5).
23. Verifikasi popup Table User Picker tertutup.
24. Verifikasi Tab `Total Control` tetap aktif.
25. Verifikasi kondisi list halaman utama tidak berubah dari yang dicatat pada langkah 16.
26. Klik `[+ Assign]` kembali.
27. Verifikasi popup terbuka dengan state default: Search kosong, tanpa Filter, Sort default, halaman 1, dan ukuran halaman default.
28. Tutup popup Assign.

## Notes

- Langkah penghubung (S-03): langkah 5 (menutup Overlay Page Size), 10 (mencatat baris pertama sebagai pembanding langkah 13), 15 (menutup popup Assign sehingga state popup kembali ke awal sebelum TC 704), 16 (mencatat kondisi list utama sebagai pembanding langkah 25), dan 28 (menutup popup Assign).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 703 butir c menyebut "nama baris pertama berbeda dari baris pertama sebelum sort" tanpa langkah mencatatnya; spec menambah langkah penghubung 10.
  - TC 704 butir a ("kondisi list halaman utama tidak berubah") tidak menyebut keadaan pembanding; spec mencatatnya pada langkah 16.
  - TC 704 langkah 3 meminta halaman 2 setelah Search `a` dan Filter `Active`; jumlah hasilnya bergantung data #41 dan hanya mencapai halaman 2 bila hasil lebih dari 10 baris.
