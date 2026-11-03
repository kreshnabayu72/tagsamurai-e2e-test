---
id: TC-FA-RP-E2E-167-tab-group-manager-setup-column-4
title: "Tab Group Manager: Setup Column (4/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-558
  - TC-FA-RP-559
  - TC-FA-RP-560
  - TC-FA-RP-561
coverage:
  web: automated
---

# Tab Group Manager: Setup Column (4/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE). `[Reset to Default]` pada langkah 17 adalah aksi TC-FA-RP-559, bukan pemulihan.
- Tabel Kolom curated-tersembunyi (TC-FA-RP-558): `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`.

## Test Steps

### Pin dan unpin kolom kelas Curated-tersembunyi (TC-FA-RP-558)

1. Klik Tab `Group Manager`
2. Untuk setiap baris pada Tabel Kolom curated-tersembunyi, lakukan langkah 3 sampai 13
3. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
4. Centang kolom agar tampil pada Live Preview
5. Klik ikon Pin pada kolom
6. Verifikasi ikon Pin aktif pada Live Preview
7. Klik `[Save]`
8. Scroll tabel horizontal
9. Verifikasi kolom membeku (sticky)
10. Muat ulang halaman (F5)
11. Verifikasi kolom tetap ter-pin
12. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, klik ikon Pin kolom itu lagi, lalu klik `[Save]`
13. Verifikasi pembekuan terlepas

### Reset to Default (TC-FA-RP-559)

14. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
15. Hapus centang kolom `Division`, seret kolom `Position` ke posisi paling akhir pada daftar, klik ikon Pin pada kolom `Name`, lalu klik `[Save]`
16. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
17. Klik `[Reset to Default]` lalu `[Save]`
18. Verifikasi kolom `Division` tampil kembali pada tabel
19. Verifikasi kolom `Position` kembali ke urutan semula
20. Verifikasi kolom `Name` tidak ter-pin
21. Muat ulang halaman (F5)
22. Verifikasi susunan kolom default tetap (persisten setelah F5)

### Tutup popup lewat `(X)` atau Esc membuang perubahan (TC-FA-RP-560)

23. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, lalu hapus centang kolom `Division`
24. Klik `(X)`
25. Verifikasi perubahan preview dibatalkan
26. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Division` tampil)
27. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, lalu hapus centang kolom `Division`
28. Tekan Esc
29. Verifikasi perubahan preview dibatalkan
30. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Division` tampil)

### Guard satu kolom tersisa (TC-FA-RP-561)

31. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
32. Hapus centang semua kolom kecuali satu
33. Hover checkbox kolom terakhir
34. Verifikasi checkbox kolom terakhir Disabled dengan tooltip `At least one column must remain visible.`
35. Klik `(X)` untuk menutup popup

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 3 sampai 13 adalah blok berulang dengan parameter pada Tabel Kolom curated-tersembunyi (lima iterasi); nominal 35 langkah, ekspansi 79. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #38), dan tiap iterasi berdiri sendiri karena pin dilepas di akhir iterasi. Langkah yang diulang: 3 sampai 13.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); membuka popup Setup Column (langkah 3, 14, 16, 23, 27, 31); langkah 4 mencentang kolom agar tampil sebelum di-pin; scroll horizontal (langkah 8); menutup popup (langkah 35).
- Langkah 32 menyisakan satu kolom pada popup yang tidak disimpan; langkah 35 menutup popup lewat `(X)` sehingga perubahan dibuang dan konfigurasi tersimpan tidak berubah.
- Temuan untuk QA:
  - TC-FA-RP-559 Expected ("kembali ke default awal ... dan persisten setelah F5") digabung pada satu butir; spec memecahnya menjadi tiga klausa kolom (langkah 18 sampai 20) dan satu klausa persistensi (langkah 22).
  - TC-FA-RP-560 tidak menyebut kolom yang diubah; spec memakai kolom `Division`.
  - TC-FA-RP-561 langkah 3 ("hapus centang semua kolom kecuali satu") tidak menyebut kolom yang tersisa; spec tidak mengasersi kolom tertentu pada Disabled.
