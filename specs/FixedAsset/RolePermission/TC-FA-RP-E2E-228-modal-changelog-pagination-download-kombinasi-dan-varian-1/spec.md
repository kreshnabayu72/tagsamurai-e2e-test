---
id: TC-FA-RP-E2E-228-modal-changelog-pagination-download-kombinasi-dan-varian-1
title: "Modal Changelog: Pagination, Download, kombinasi, dan varian (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-743
  - TC-FA-RP-744
  - TC-FA-RP-745
  - TC-FA-RP-746
coverage:
  web: automated
---

# Modal Changelog: Pagination, Download, kombinasi, dan varian (1/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed, sehingga entri seed dikenali lewat kombinasi Action, User Name, Old Value, New Value, dan Modified By di atas, dan asersi memakai urutan relatif, selisih terhadap baseline, atau hanya entri seed yang cocok. Spec ini tidak mengubah data.
- Tabel Nomor halaman tidak valid (TC 746): `0`; `N+1` (melebihi jumlah halaman; N = jumlah halaman baseline pada langkah 33); `abc` (bukan angka).

## Test Steps

### Pagination: default dan pilihan ukuran (TC 743)

1. Catat jumlah baris dan urutan baris list Tab `Total Control` pada halaman utama.
2. Klik ikon Changelog pada toolbar.
3. Verifikasi default 10 data per halaman: halaman 1 menampilkan paling banyak 10 baris.
4. Verifikasi info pagination menampilkan total entri audit trail saat ini.
5. Catat total entri pada info pagination sebagai baseline.
6. Buka Overlay Page Size.
7. Verifikasi pilihan ukuran 10, 25, 50, dan 100 tanpa opsi `All`.

### Pagination: ganti ukuran halaman dan sort (TC 744)

8. Tutup Overlay Page Size.
9. Catat total entri pada info pagination sebagai baseline.
10. Buka pilihan ukuran halaman pada pagination.
11. Verifikasi pilihan ukuran halaman 10, 25, 50, dan 100 (tanpa opsi `All`).
12. Verifikasi ukuran terpilih sebelum diganti: 10.
13. Pilih ukuran halaman 25.
14. Verifikasi info pagination menampilkan total yang sama dengan baseline langkah 9 dan ukuran halaman 25.
15. Verifikasi halaman 1 menampilkan sejumlah baris sebesar yang lebih kecil antara total baseline dan 25.
16. Klik header kolom User Name dua kali (User Name descending).
17. Verifikasi urutan relatif entri seed Pre-setup #42: Rina Wulandari, Maya Anggraeni, Fitri Handayani, Budi Santoso (Remove lalu Assign; tie-breaker default sort Date descending), Ahmad Fauzi.
18. Verifikasi total pada info pagination tetap sama dengan baseline langkah 9.

### Modal tertutup saat F5 dan dibuka dengan state default (TC 745)

19. Klik header kolom User Name sekali untuk mengembalikan sort ke default.
20. Catat total entri pada info pagination sebagai baseline.
21. Ketik Search `assign`, tekan Enter.
22. Terapkan Filter Modified By `Siti Rahmawati` (klik ikon Filter, pilih opsi `Siti Rahmawati` pada field Modified By, klik `[Apply]`).
23. Klik header kolom User Name dua kali (User Name descending).
24. Ganti ukuran halaman menjadi 25.
25. Muat ulang halaman (F5).
26. Verifikasi modal Changelog tertutup.
27. Verifikasi Tab `Total Control` tetap aktif.
28. Verifikasi kondisi list halaman utama tidak berubah dari yang dicatat pada langkah 1.
29. Klik ikon Changelog pada toolbar kembali.
30. Verifikasi modal terbuka dengan state default: Search kosong, tanpa Filter, Sort Date descending, dan ukuran halaman 10.
31. Verifikasi info pagination menampilkan total yang sama dengan baseline langkah 20 (tanpa Search dan Filter).
32. Verifikasi entri seed Assign Maya Anggraeni tampil di atas entri seed Pre-setup #42 lainnya (Date descending).

### Kasus tepi nomor halaman (TC 746)

33. Catat jumlah halaman N, total entri pada info pagination, dan baris halaman 1 sebagai baseline.
34. Untuk setiap baris pada tabel Nomor halaman tidak valid, lakukan langkah 35 sampai 36.
35. Masukkan nomor halaman pada input nomor halaman, tekan Enter.
36. Verifikasi nomor halaman diabaikan: tabel tetap di halaman 1 dengan baris yang sama seperti baseline langkah 33 dan total pada info pagination tetap sama dengan baseline.

## Notes

- Spec memuat 36 langkah (di atas 35 langkah): empat TC berurutan pada modal yang sama, dan tiap TC memerlukan langkah baseline sendiri (langkah 5, 9, 20, 33) sebelum asersi relatif terhadap baseline; blok langkah 35 sampai 36 berulang tiga iterasi pada tabel Prerequisites.
- Langkah penghubung (S-03): langkah 1 (mencatat kondisi list utama sebagai pembanding langkah 28), 5, 9, 20, dan 33 (mencatat baseline), 8 (menutup Overlay Page Size), 19 (mengembalikan sort ke default sebelum TC 745 membangun state-nya sendiri), dan 34 (kepala perulangan).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 745 butir a ("kondisi list halaman utama tidak berubah") tidak menyebut keadaan pembanding; spec mencatatnya pada langkah 1.
