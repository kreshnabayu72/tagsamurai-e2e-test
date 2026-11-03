---
id: TC-FA-RP-E2E-146-tab-total-control-setup-column-2
title: "Tab Total Control: Setup Column (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-506
  - TC-FA-RP-507
coverage:
  web: automated
---

# Tab Total Control: Setup Column (2/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column (urutan dan Pin) disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Hideable-tampil: `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`.
- Tabel menyediakan area scroll horizontal untuk asersi pembekuan kolom (TC 507); lebar viewport yang membuat scroll horizontal muncul disediakan tim FE.

## Test Steps

### Geser urutan kolom Hideable-tampil (TC 506)

1. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 2 sampai 8.
2. Buka popup Setup Column.
3. Seret kolom ke posisi paling akhir pada daftar.
4. Verifikasi kolom berada di posisi paling akhir pada Live Preview.
5. Klik `[Save]`.
6. Verifikasi tabel memakai urutan kolom yang sama dengan Live Preview.
7. Muat ulang halaman (F5).
8. Verifikasi urutan kolom tabel tetap.
9. Klik Tab `Read Only`.
10. Untuk setiap kolom pada Tabel Kolom Hideable-tampil pada Tab Read Only, ulangi langkah 2 sampai 8 (hasil identik dengan Tab Total Control).

### Pin dan unpin kolom Hideable-tampil (TC 507)

11. Klik Tab `Total Control`.
12. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 13 sampai 22.
13. Buka popup Setup Column.
14. Klik ikon Pin pada kolom.
15. Verifikasi ikon Pin aktif pada Live Preview.
16. Klik `[Save]`.
17. Scroll tabel horizontal.
18. Verifikasi kolom membeku (sticky) saat scroll horizontal.
19. Muat ulang halaman (F5).
20. Verifikasi kolom tetap ter-pin.
21. Buka popup Setup Column, klik ikon Pin kolom itu lagi, lalu klik `[Save]`.
22. Verifikasi pembekuan kolom terlepas.
23. Klik Tab `Read Only`.
24. Untuk setiap kolom pada Tabel Kolom Hideable-tampil pada Tab Read Only, ulangi langkah 13 sampai 22 (hasil identik dengan Tab Total Control).

## Notes

- Alasan di atas 35 langkah: langkah 2 sampai 8 dan langkah 13 sampai 22 adalah blok berulang dengan parameter pada tabel Prerequisites (masing-masing enam iterasi pada Tab Total Control dan enam pada Tab Read Only); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri. Langkah yang diulang: 2 sampai 8 dan 13 sampai 22.
- Langkah penghubung (S-03): langkah 1, 2, 3, 5, 7, 9 sampai 14, 16, 17, 19, 21, 23, dan 24. Langkah 9, 11, dan 23 berpindah tab; langkah 21 membuka ulang popup untuk melepas Pin sesuai TC.
- Temuan untuk QA:
  - TC 506 tidak menyebut cara mengembalikan urutan kolom antar iterasi; urutan kolom baru dibentuk ulang tiap iterasi dari konfigurasi iterasi sebelumnya dan seluruhnya dibuang di hook `after`.
  - TC 507 mengasersi pembekuan kolom saat scroll horizontal tanpa menyebut lebar viewport; kemampuan itu ditulis di Prerequisites sebagai disediakan tim FE.
