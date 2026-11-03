---
id: TC-FA-RP-E2E-217-table-user-picker-pagination-state-dan-kombinasi-2
title: "Table User Picker: Pagination, state, dan kombinasi (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-705
  - TC-FA-RP-706
  - TC-FA-RP-707
  - TC-FA-RP-708
coverage:
  web: automated
---

# Table User Picker: Pagination, state, dan kombinasi (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #41 (kandidat popup Assign Total Control, 12 kandidat: Citra Lestari (Division `HR`), Dimas Pranata (Division `IT Operations`), Endah Susanti (Division `Procurement`), Gunawan Halim, Hesti Rahma, Joko Santoso, Indra Kusuma, Dewi Anggraini, Maya Anggraeni, Yoga Pratama (`Inactive`), Gilang Prakoso, Hana Permata) dan #36 (Tab Total Control terisi sembilan baris, termasuk Rina Wulandari, sebagai tabel utama di belakang popup). Pre-setup #37 dan #17 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data; Pre-setup di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Nilai nomor halaman untuk "melebihi jumlah halaman" (TC 705): `99`.

## Test Steps

### Kasus tepi nomor halaman (TC 705)

1. Klik `[+ Assign]`.
2. Masukkan nomor halaman `0` pada input nomor halaman, tekan Enter.
3. Verifikasi nomor halaman tidak valid diabaikan dan popup tetap di halaman 1.
4. Masukkan nomor halaman `99` pada input nomor halaman, tekan Enter.
5. Verifikasi nomor halaman tidak valid diabaikan dan popup tetap di halaman 1.
6. Masukkan teks `abc` pada input nomor halaman, tekan Enter.
7. Verifikasi nomor halaman tidak valid diabaikan dan popup tetap di halaman 1.

### Search popup tidak terpengaruh Search tabel utama (TC 706)

8. Tutup popup Assign.
9. Ketik Search `rina`, tekan Enter pada tabel utama Tab `Total Control`.
10. Verifikasi tabel utama tersaring `rina`: sedikitnya satu baris tampil dan setiap baris yang tampil cocok dengan `rina`.
11. Klik `[+ Assign]`.
12. Verifikasi daftar kandidat tidak tersaring oleh keyword tabel: kandidat `Citra Lestari` dan `Dimas Pranata` tampil.
13. Ketik Search `endah`, tekan Enter pada popup.
14. Tutup popup Assign.
15. Verifikasi tabel di belakang popup masih tersaring `rina`: sedikitnya satu baris tampil dan setiap baris yang tampil cocok dengan `rina`.
16. Klik `(←)` pada kotak Search tabel utama.

### Menutup popup mereset Search, Filter, dan Sort (TC 707)

17. Klik `[+ Assign]`.
18. Terapkan Filter Division `IT Operations` (klik ikon Filter, pilih opsi `IT Operations` pada field Division, klik `[Apply]`).
19. Klik header kolom Name dua kali (Name descending).
20. Ketik Search `endah`, tekan Enter.
21. Tutup popup Assign, lalu klik `[+ Assign]` kembali.
22. Verifikasi popup terbuka dengan state awal: Search kosong, tanpa Filter, Sort Name A-Z.

### Kombinasi Search, Filter, dan Sort (TC 708)

23. Ketik Search `a`, tekan Enter.
24. Terapkan Filter Status `Active` (klik ikon Filter, pilih opsi `Active` pada field Status, klik `[Apply]`).
25. Klik header kolom Name dua kali (Name descending).
26. Verifikasi daftar menampilkan irisan Search `a` dan Filter Status `Active`: sedikitnya satu baris tampil dan setiap baris berstatus `Active`.
27. Verifikasi urutan baris Name descending.
28. Tutup popup Assign.

## Notes

- Langkah penghubung (S-03): langkah 8 (menutup popup agar tabel utama dapat dicari), 9 (Search tabel utama `rina` sebagai precondition TC 706), 16 (mengosongkan Search tabel utama), dan 28 (menutup popup Assign). Langkah 10 adalah `Verifikasi` tambahan sebagai anchor positif atas Search tabel utama (alasan di Temuan untuk QA). Langkah 2, 4, dan 6 menambah Enter yang tidak disebut TC 705, mengikuti TC 746 (Enter tiap nilai).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 705 tidak menyebut nilai "melebihi jumlah halaman" dan tidak menyebut tombol Enter; spec memilih `99` dan Enter.
  - TC 706 butir b ("tabel di belakang masih tersaring `rina`") tidak punya pembanding bahwa pencarian sudah berlaku sebelum popup dibuka; spec menambah `Verifikasi` langkah 10 sebagai anchor positif.
  - TC 708 menyebut "irisan Search dan Filter" tanpa baris spesifik; spec mengasersi status `Active` dan urutan Name descending tanpa menyebut nama baris.
