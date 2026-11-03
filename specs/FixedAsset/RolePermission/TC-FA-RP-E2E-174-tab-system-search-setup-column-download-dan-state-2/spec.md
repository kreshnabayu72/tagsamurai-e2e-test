---
id: TC-FA-RP-E2E-174-tab-system-search-setup-column-download-dan-state-2
title: "Tab System: Search, Setup Column, Download, dan state (2/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-581
  - TC-FA-RP-582
  - TC-FA-RP-583
coverage:
  web: automated
---

# Tab System: Search, Setup Column, Download, dan state (2/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #39 (Tab System memuat 9 Global Role dan 7 Group Role). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan tiap iterasi dengan centang ulang; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE). Urutan kolom hasil seret dibiarkan sampai hook `after`.
- Tabel Kolom Hideable-tampil (TC-FA-RP-582 dan TC-FA-RP-583): `Role Name`, `Users`.

## Test Steps

### Popup Setup Column tiga zona (TC-FA-RP-581)

1. Klik Tab `System`
2. Klik header `(⋯)` kolom Column Visibility
3. Klik `Setup Column...`
4. Verifikasi zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `(X)`
5. Verifikasi zona Body: daftar kolom dengan checkbox, drag handle, ikon Pin, dan Live Preview tabel
6. Verifikasi zona Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan; tidak ada `[Cancel]`
7. Klik `(X)` untuk menutup popup

### Ceklis dan unceklis kolom kelas Hideable-tampil (TC-FA-RP-582)

8. Untuk setiap baris pada Tabel Kolom Hideable-tampil, lakukan langkah 9 sampai 18
9. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
10. Hapus centang kolom
11. Verifikasi Live Preview tidak lagi menampilkan kolom
12. Klik `[Save]`
13. Verifikasi tabel tidak menampilkan kolom
14. Muat ulang halaman (F5), lalu buka kembali popup Setup Column
15. Verifikasi kolom tetap tidak tampil pada tabel
16. Verifikasi checkbox kolom tidak tercentang
17. Centang kembali kolom, lalu klik `[Save]`
18. Verifikasi kolom tampil kembali pada tabel

### Geser urutan kolom kelas Hideable-tampil (TC-FA-RP-583)

19. Untuk setiap baris pada Tabel Kolom Hideable-tampil, lakukan langkah 20 sampai 26
20. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
21. Seret kolom ke posisi paling akhir pada daftar
22. Verifikasi kolom berada di posisi paling akhir pada Live Preview
23. Klik `[Save]`
24. Verifikasi tabel memakai urutan kolom yang sama dengan Live Preview
25. Muat ulang halaman (F5)
26. Verifikasi urutan kolom tetap

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 9 sampai 18 dan 20 sampai 26 adalah blok berulang dengan parameter pada Tabel Kolom Hideable-tampil (dua iterasi tiap blok); nominal 26 langkah, ekspansi 43. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #39), dan tiap iterasi berdiri sendiri karena centang dipulihkan di akhir iterasi. Langkah yang diulang: 9 sampai 18 dan 20 sampai 26.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); membuka overlay dan popup (langkah 2, 3, 9, 20); menutup popup dengan `(X)` (langkah 7); membuka kembali popup setelah F5 digabung pada langkah 14 sesuai TC.
- Temuan untuk QA:
  - TC-FA-RP-582 dan TC-FA-RP-583 tidak menyebut tab aktif setelah F5; spec mengasumsikan Tab `System` tetap aktif setelah F5.
  - TC-FA-RP-583 menyeret tiap kolom ke posisi paling akhir pada daftar dua kolom; untuk kolom yang sudah berada di posisi akhir TC tidak menjelaskan perubahan yang teramati; spec mengasersi posisi paling akhir tiap iterasi.
