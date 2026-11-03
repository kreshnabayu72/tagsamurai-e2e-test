---
id: TC-FA-RP-E2E-230-modal-changelog-pagination-download-kombinasi-dan-varian-3
title: "Modal Changelog: Pagination, Download, kombinasi, dan varian (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-752
  - TC-FA-RP-754
  - TC-FA-RP-756
  - TC-FA-RP-757
  - TC-FA-RP-758
coverage:
  web: automated
---

# Modal Changelog: Pagination, Download, kombinasi, dan varian (3/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed, sehingga entri seed dikenali lewat kombinasi Action, User Name, Old Value, New Value, dan Modified By di atas, dan asersi memakai urutan relatif, selisih terhadap baseline, atau hanya entri seed yang cocok. Spec ini tidak mengubah data.
- Kemampuan teknis: pembaca berkas unduhan (CSV dan XLSX) untuk memeriksa nama berkas dan baris; disediakan tim FE/BE.

## Test Steps

### Download: extension berkas mengikuti pilihan format (TC 752)

1. Klik ikon Changelog pada toolbar.
2. Klik ikon Download, lalu klik `Download as CSV`.
3. Klik ikon Download, lalu klik `Download as XLSX`.
4. Verifikasi berkas `Changelog-Role-Permission-Total-Control.csv` untuk pilihan CSV.
5. Verifikasi berkas `Changelog-Role-Permission-Total-Control.xlsx` untuk pilihan XLSX.

### Download dengan nol baris (TC 754)

6. Ketik Search `zzzz`, tekan Enter.
7. Verifikasi tombol Download tetap aktif.
8. Klik ikon Download, lalu klik `Download as CSV`.
9. Verifikasi berkas hanya memuat baris header kolom.
10. Klik ikon `(←)` pada kotak Search.

### Kombinasi penuh Search, Filter, Sort, dan Pagination (TC 756)

11. Ketik Search `assign`, tekan Enter.
12. Terapkan Filter Modified By `Siti Rahmawati` (klik ikon Filter, pilih opsi `Siti Rahmawati` pada field Modified By, klik `[Apply]`).
13. Klik header kolom User Name sekali (User Name ascending).
14. Ganti ukuran halaman menjadi 25.
15. Verifikasi tabel menampilkan, dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), hanya Assign Ahmad Fauzi lalu Assign Rina Wulandari: irisan Search `assign` dan Filter Modified By `Siti Rahmawati` dengan Sort User Name ascending.
16. Verifikasi ukuran halaman 25 berlaku bersamaan dengan kondisi lain.

### Lepas Filter saat Search dan Sort aktif (TC 757)

17. Pulihkan state: klik `[Clear Field]`, lalu klik `[Apply]`; klik ikon `(←)` pada kotak Search; klik header kolom User Name dua kali hingga sort kembali ke default.
18. Ketik Search `assign`, tekan Enter.
19. Terapkan Filter Modified By `Siti Rahmawati` (klik ikon Filter, pilih opsi `Siti Rahmawati` pada field Modified By, klik `[Apply]`).
20. Klik header kolom User Name sekali (User Name ascending).
21. Klik `[Clear Field]`, lalu klik `[Apply]`.
22. Verifikasi tabel menampilkan, dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), hanya Assign Ahmad Fauzi, Assign Budi Santoso, Assign Maya Anggraeni, lalu Assign Rina Wulandari dengan urutan relatif itu.
23. Verifikasi keyword Search `assign` dan Sort User Name ascending tetap aktif menyaring tabel.

### Kosongkan Search saat Filter dan Sort aktif (TC 758)

24. Pulihkan state: klik ikon `(←)` pada kotak Search; klik header kolom User Name dua kali hingga sort kembali ke default.
25. Ketik Search `assign`, tekan Enter.
26. Terapkan Filter Modified By `Siti Rahmawati` (klik ikon Filter, pilih opsi `Siti Rahmawati` pada field Modified By, klik `[Apply]`).
27. Klik header kolom User Name sekali (User Name ascending).
28. Kosongkan isi kotak search, tekan Enter.
29. Verifikasi tabel menampilkan, dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), hanya Assign Ahmad Fauzi, Auto-Revert Fitri Handayani, lalu Assign Rina Wulandari dengan urutan relatif itu.
30. Verifikasi kriteria Filter Modified By `Siti Rahmawati` dan Sort User Name ascending tetap aktif menyaring tabel.

## Notes

- Langkah penghubung (S-03): langkah 10 (mengosongkan Search sebelum TC 756), 17 dan 24 (memulihkan Search, Filter, dan Sort antar TC, sesuai S-09; satu aksi gabungan tanpa `Verifikasi`).
- Spec memuat lima TC berurutan pada modal yang sama (Download, kombinasi Search, Filter, Sort); batas sekitar 35 langkah tidak terlampaui (30 langkah).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- TC 753 (isi berkas), TC 751 dan TC 764 (Download gagal), serta TC 755 (di atas 5.000 baris) ada di spec lain.
- Temuan untuk QA:
  - TC 754 tidak punya Expected untuk keadaan tabel (empty state) sebelum Download; spec hanya mengasersi tombol Download aktif dan isi berkas.
  - TC 756 sampai 758 tidak menyatakan apakah panel Filter tetap terbuka sesudah `[Apply]`; spec mengasumsikan panel tetap terbuka.
