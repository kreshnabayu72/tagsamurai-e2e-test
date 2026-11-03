---
id: TC-FA-RP-E2E-165-tab-group-manager-setup-column-2
title: "Tab Group Manager: Setup Column (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-554
  - TC-FA-RP-555
coverage:
  web: automated
---

# Tab Group Manager: Setup Column (2/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE). Tiap iterasi pin memulihkan pin pada langkah 19; urutan kolom hasil seret dibiarkan sampai hook `after`.
- Tabel Kolom Hideable-tampil (TC-FA-RP-554 dan TC-FA-RP-555): `Name`, `Group`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`.

## Test Steps

### Geser urutan kolom kelas Hideable-tampil (TC-FA-RP-554)

1. Klik Tab `Group Manager`
2. Untuk setiap baris pada Tabel Kolom Hideable-tampil, lakukan langkah 3 sampai 9
3. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
4. Seret kolom ke posisi paling akhir pada daftar
5. Verifikasi kolom berada di posisi paling akhir pada Live Preview
6. Klik `[Save]`
7. Verifikasi tabel memakai urutan kolom yang sama dengan Live Preview
8. Muat ulang halaman (F5)
9. Verifikasi urutan kolom tetap

### Pin dan unpin kolom kelas Hideable-tampil (TC-FA-RP-555)

10. Untuk setiap baris pada Tabel Kolom Hideable-tampil, lakukan langkah 11 sampai 20
11. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
12. Klik ikon Pin pada kolom
13. Verifikasi ikon Pin aktif pada Live Preview
14. Klik `[Save]`
15. Scroll tabel horizontal
16. Verifikasi kolom membeku (sticky)
17. Muat ulang halaman (F5)
18. Verifikasi kolom tetap ter-pin
19. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, klik ikon Pin kolom itu lagi, lalu klik `[Save]`
20. Verifikasi pembekuan terlepas

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 3 sampai 9 dan 11 sampai 20 adalah blok berulang dengan parameter pada Tabel Kolom Hideable-tampil (tujuh iterasi tiap blok); nominal 20 langkah, ekspansi 2 + 7 x 7 + 1 + 7 x 10 = 122. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #38), dan tiap iterasi berdiri sendiri karena pin dilepas di akhir iterasi. Langkah yang diulang: 3 sampai 9 dan 11 sampai 20.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); membuka popup Setup Column (langkah 3, 11); scroll horizontal (langkah 15); langkah 4 menyeret kolom ke posisi akhir dan langkah 12 mengeklik Pin sebagai aksi TC.
- Temuan untuk QA:
  - TC-FA-RP-554 menyeret tiap kolom ke posisi paling akhir tanpa memulihkan urutan antar iterasi; spec membiarkan urutan hasil seret dan mengasersi posisi paling akhir tiap iterasi.
  - TC-FA-RP-555 Expected "membeku (sticky)" saat scroll horizontal tidak menyebut lebar viewport yang membuat tabel dapat discroll; spec mengasumsikan lebar tabel cukup untuk scroll horizontal (viewport dikelola tim FE).
