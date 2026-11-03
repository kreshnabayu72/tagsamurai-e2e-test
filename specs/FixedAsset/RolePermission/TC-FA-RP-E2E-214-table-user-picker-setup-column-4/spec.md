---
id: TC-FA-RP-E2E-214-table-user-picker-setup-column-4
title: "Table User Picker: Setup Column (4/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-697
  - TC-FA-RP-698
  - TC-FA-RP-699
coverage:
  web: automated
---

# Table User Picker: Setup Column (4/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #41 (kandidat popup Assign Total Control, 12 kandidat). Pre-setup #36, #37, dan #17 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data; Pre-setup di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; pin dilepas di akhir tiap iterasi TC 697 dan dikembalikan ke default oleh `[Reset to Default]` yang menjadi objek uji TC 698; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Tabel Kolom Curated-tersembunyi (TC 697): `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`.

## Test Steps

### Pin dan unpin kolom Curated-tersembunyi (TC 697)

1. Klik `[+ Assign]`.
2. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi, lakukan langkah 3 sampai 14.
3. Klik header `(⋯)`, lalu klik `Setup Column...`.
4. Klik ikon Pin pada kolom.
5. Verifikasi ikon Pin aktif pada Live Preview.
6. Klik `[Save]`.
7. Scroll tabel horizontal.
8. Verifikasi kolom membeku (sticky).
9. Muat ulang halaman (F5), lalu klik `[+ Assign]` kembali.
10. Buka popup Setup Column.
11. Verifikasi kolom tetap ter-pin.
12. Klik ikon Pin kolom itu lagi, lalu klik `[Save]`.
13. Scroll tabel horizontal.
14. Verifikasi pembekuan terlepas.

### Reset to Default (TC 698)

15. Klik header `(⋯)`, lalu klik `Setup Column...`.
16. Hapus centang kolom `Division`.
17. Seret kolom `Position` ke posisi paling akhir pada daftar.
18. Klik ikon Pin pada kolom `Name`.
19. Klik `[Save]`.
20. Klik header `(⋯)`, lalu klik `Setup Column...`.
21. Klik `[Reset to Default]`.
22. Klik `[Save]`.
23. Muat ulang halaman (F5), klik `[+ Assign]` kembali, lalu buka popup Setup Column.
24. Verifikasi kolom `Division` tampil kembali dan tercentang.
25. Verifikasi kolom `Position` kembali ke urutan semula.
26. Verifikasi kolom `Name` tidak ter-pin.

### Tutup popup Setup Column membuang perubahan (TC 699)

27. Klik `(X)` untuk menutup popup Setup Column.
28. Klik header `(⋯)`, lalu klik `Setup Column...`.
29. Hapus centang kolom `Email`.
30. Klik `(X)`.
31. Verifikasi perubahan preview dibatalkan dan tabel memakai konfigurasi tersimpan terakhir (kolom `Email` tetap tampil).
32. Klik header `(⋯)`, lalu klik `Setup Column...`.
33. Hapus centang kolom `Email`.
34. Tekan Esc.
35. Verifikasi perubahan preview dibatalkan dan tabel memakai konfigurasi tersimpan terakhir (kolom `Email` tetap tampil).
36. Tutup popup Assign.

## Notes

- Alasan di atas 35 langkah: langkah 3 sampai 14 adalah blok berulang dengan parameter pada tabel Prerequisites (tujuh iterasi); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena pin dilepas di akhir iterasi. Langkah yang diulang: 3 sampai 14. Tanpa ekspansi, spec berisi 36 langkah.
- Langkah penghubung (S-03): langkah 2 (kepala perulangan), 27 (menutup popup Setup Column tanpa menyimpan), dan 36 (menutup popup Assign). Langkah 13 (scroll) mendahului asersi pembekuan terlepas (S-14).
- TC 698 butir tunggal Expected ("kembali ke default awal ... dan persisten setelah F5") diasersi sesudah F5 dan pembukaan ulang popup (langkah 24 sampai 26), sehingga persistensi ikut teramati.
- TC 699 butir Expected tunggal ("perubahan preview dibatalkan dan tabel memakai konfigurasi tersimpan terakhir") ditulis sebagai satu `Verifikasi` per penutupan (langkah 31 dan 35); kolom `Email` dipilih sebagai "satu centang" yang diubah.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 697 mengasersi pembekuan (sticky) untuk kolom curated yang secara bawaan tidak tercentang tanpa menyebut bahwa kolom lebih dulu ditampilkan; spec mengikuti TC.
  - TC 698 dan 699 tidak menyebut kolom yang dipilih untuk "satu centang" (TC 699); spec memilih `Email`.
  - TC 697 sampai 699 tidak menyebut apakah popup Assign tetap terbuka sesudah `[Save]` Setup Column; spec mengasumsikan popup Assign tetap terbuka.
