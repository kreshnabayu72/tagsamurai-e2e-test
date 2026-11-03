---
id: TC-FA-RP-E2E-175-tab-system-search-setup-column-download-dan-state-3
title: "Tab System: Search, Setup Column, Download, dan state (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-584
  - TC-FA-RP-585
  - TC-FA-RP-586
  - TC-FA-RP-587
coverage:
  web: automated
---

# Tab System: Search, Setup Column, Download, dan state (3/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #39 (Tab System memuat 9 Global Role dan 7 Group Role). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE). `[Reset to Default]` pada langkah 16 adalah aksi TC-FA-RP-585, bukan pemulihan.
- Tabel Kolom Hideable-tampil (TC-FA-RP-584): `Role Name`, `Users`.

## Test Steps

### Pin dan unpin kolom kelas Hideable-tampil (TC-FA-RP-584)

1. Klik Tab `System`
2. Untuk setiap baris pada Tabel Kolom Hideable-tampil, lakukan langkah 3 sampai 12
3. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
4. Klik ikon Pin pada kolom
5. Verifikasi ikon Pin aktif pada Live Preview
6. Klik `[Save]`
7. Scroll tabel horizontal
8. Verifikasi kolom membeku (sticky)
9. Muat ulang halaman (F5)
10. Verifikasi kolom tetap ter-pin
11. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, klik ikon Pin kolom itu lagi, lalu klik `[Save]`
12. Verifikasi pembekuan terlepas

### Reset to Default (TC-FA-RP-585)

13. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
14. Hapus centang kolom `Users`, seret kolom `Role Name` ke posisi paling akhir pada daftar, klik ikon Pin pada kolom `Role Name`, lalu klik `[Save]`
15. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
16. Klik `[Reset to Default]` lalu `[Save]`
17. Verifikasi kolom `Users` tampil kembali pada tabel
18. Verifikasi kolom `Role Name` kembali ke urutan semula
19. Verifikasi kolom `Role Name` tidak ter-pin
20. Muat ulang halaman (F5)
21. Verifikasi susunan kolom default tetap (persisten setelah F5)

### Tutup popup lewat `(X)` atau Esc membuang perubahan (TC-FA-RP-586)

22. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, lalu hapus centang kolom `Users`
23. Klik `(X)`
24. Verifikasi perubahan preview dibatalkan
25. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Users` tampil)
26. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, lalu hapus centang kolom `Users`
27. Tekan Esc
28. Verifikasi perubahan preview dibatalkan
29. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Users` tampil)

### Guard satu kolom tersisa (TC-FA-RP-587)

30. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
31. Hapus centang semua kolom kecuali satu
32. Hover checkbox kolom terakhir
33. Verifikasi checkbox kolom terakhir Disabled dengan tooltip `At least one column must remain visible.`
34. Klik `(X)` untuk menutup popup

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 3 sampai 12 adalah blok berulang dengan parameter pada Tabel Kolom Hideable-tampil (dua iterasi); nominal 34 langkah, ekspansi 44. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #39), dan tiap iterasi berdiri sendiri karena pin dilepas di akhir iterasi. Langkah yang diulang: 3 sampai 12.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); membuka popup Setup Column (langkah 3, 13, 15, 22, 26, 30); scroll horizontal (langkah 7); menutup popup (langkah 34).
- Temuan untuk QA:
  - TC-FA-RP-585 menyeret `Role Name` ke posisi paling akhir setelah `Users` tidak dicentang (satu kolom tersisa pada Live Preview); posisi paling akhir tidak teramati berbeda; spec tetap mengikuti urutan aksi TC.
  - TC-FA-RP-586 tidak menyebut kolom yang diubah; spec memakai kolom `Users`.
  - TC-FA-RP-584 sampai TC-FA-RP-587 tidak menyebut tab aktif setelah F5; spec mengasumsikan Tab `System` tetap aktif.
