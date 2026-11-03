---
id: TC-FA-RP-E2E-148-tab-total-control-setup-column-4
title: "Tab Total Control: Setup Column (4/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-510
  - TC-FA-RP-511
  - TC-FA-RP-512
coverage:
  web: automated
---

# Tab Total Control: Setup Column (4/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris), #37 (Tab Read Only empat baris), #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No`). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column (centang, urutan, dan Pin) disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` di luar TC 511 (kemampuan disediakan tim FE).
- Tabel Kolom Curated-tersembunyi: `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`.
- Tabel menyediakan area scroll horizontal untuk asersi pembekuan kolom (TC 510); lebar viewport yang membuat scroll horizontal muncul disediakan tim FE.

## Test Steps

### Pin dan unpin kolom Curated-tersembunyi (TC 510)

1. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi, lakukan langkah 2 sampai 13.
2. Buka popup Setup Column.
3. Centang kolom.
4. Klik ikon Pin pada kolom.
5. Verifikasi ikon Pin aktif pada Live Preview.
6. Klik `[Save]`.
7. Scroll tabel horizontal.
8. Verifikasi kolom membeku (sticky) saat scroll horizontal.
9. Muat ulang halaman (F5).
10. Verifikasi kolom tetap ter-pin.
11. Buka popup Setup Column, klik ikon Pin kolom itu lagi, lalu klik `[Save]`.
12. Verifikasi pembekuan kolom terlepas.
13. Buka popup Setup Column, hapus centang kolom, lalu klik `[Save]`.
14. Klik Tab `Read Only`.
15. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi pada Tab Read Only, ulangi langkah 2 sampai 13 (hasil identik dengan Tab Total Control).

### Reset to Default (TC 511)

16. Klik Tab `Total Control`.
17. Buka popup Setup Column.
18. Hapus centang kolom `Division`, seret kolom `Position` ke posisi paling akhir pada daftar, klik ikon Pin pada kolom `Name`, lalu klik `[Save]`.
19. Buka popup Setup Column.
20. Klik `[Reset to Default]`, lalu klik `[Save]`.
21. Verifikasi kolom `Division` tampil kembali.
22. Verifikasi kolom `Position` kembali ke urutan semula.
23. Verifikasi kolom `Name` tidak ter-pin.
24. Muat ulang halaman (F5).
25. Verifikasi susunan kolom default tetap persisten setelah F5.

### Tutup popup tanpa menyimpan (TC 512)

26. Buka popup Setup Column dan hapus centang kolom `Division`.
27. Klik `(X)`.
28. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Division` tetap tampil).
29. Buka popup Setup Column, hapus centang kolom `Division`, lalu tekan Esc.
30. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Division` tetap tampil).

## Notes

- Alasan di atas 35 langkah: langkah 2 sampai 13 adalah blok berulang dengan parameter pada tabel Prerequisites (delapan iterasi pada Tab Total Control dan delapan pada Tab Read Only); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena kolom dikembalikan ke tersembunyi di akhir iterasi. Langkah yang diulang: 2 sampai 13.
- Langkah penghubung (S-03): langkah 1 sampai 4, 6, 7, 9, 11, 13 sampai 20, 24, 26, 27, dan 29. Langkah 3 mencentang kolom Curated-tersembunyi sebelum di-Pin; langkah 13 memulihkan kolom ke keadaan tersembunyi (S-09). Langkah 20 memakai `[Reset to Default]` karena menjadi objek TC 511.
- Temuan untuk QA:
  - TC 511 menyebut "Susunan kolom kembali ke default awal" tanpa merinci urutan awal; spec mengasersi tiga perubahan yang diubah pada langkah 18.
  - TC 512 menutup popup lewat `(X)` dan Esc pada perubahan yang sama (centang `Division`); TC tidak menyebut kolom yang diubah.
