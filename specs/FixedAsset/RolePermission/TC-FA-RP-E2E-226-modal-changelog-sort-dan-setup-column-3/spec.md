---
id: TC-FA-RP-E2E-226-modal-changelog-sort-dan-setup-column-3
title: "Modal Changelog: Sort dan Setup Column (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-737
  - TC-FA-RP-738
coverage:
  web: automated
---

# Modal Changelog: Sort dan Setup Column (3/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed. Spec ini tidak mengubah data.
- Konfigurasi kolom Setup Column disimpan di browser; pin dilepas di akhir tiap iterasi TC 738, dan hook `after` menghapus preferensi kolom di browser (urutan hasil TC 737 dan semua perubahan lain), bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Hideable-tampil: `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`.

## Test Steps

### Geser urutan kolom Hideable-tampil (TC 737)

1. Klik ikon Changelog pada toolbar.
2. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 3 sampai 9.
3. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
4. Seret kolom ke posisi paling akhir pada daftar.
5. Verifikasi kolom berada di posisi paling akhir pada Live Preview.
6. Klik `[Save]`.
7. Verifikasi tabel memakai urutan kolom yang sama.
8. Muat ulang halaman (F5), klik ikon Changelog pada toolbar kembali, lalu buka kembali popup Setup Column.
9. Verifikasi urutan kolom tetap.
10. Klik `(X)` untuk menutup popup Setup Column.

### Pin dan unpin kolom Hideable-tampil (TC 738)

11. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 12 sampai 23.
12. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
13. Klik ikon Pin pada kolom.
14. Verifikasi ikon Pin aktif pada Live Preview.
15. Klik `[Save]`.
16. Scroll tabel horizontal.
17. Verifikasi kolom membeku (sticky).
18. Muat ulang halaman (F5), lalu klik ikon Changelog pada toolbar kembali.
19. Buka popup Setup Column.
20. Verifikasi kolom tetap ter-pin.
21. Klik ikon Pin kolom itu lagi, lalu klik `[Save]`.
22. Scroll tabel horizontal.
23. Verifikasi pembekuan terlepas.
24. Tutup modal Changelog.

## Notes

- Alasan di atas 35 langkah: langkah 3 sampai 9 dan 12 sampai 23 adalah blok berulang dengan parameter pada tabel Prerequisites (tujuh iterasi tiap blok); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena pin dilepas di akhir iterasi. Langkah yang diulang: 3 sampai 9 dan 12 sampai 23.
- Langkah penghubung (S-03): langkah 2 dan 11 (kepala perulangan), 10 (menutup popup Setup Column tanpa menyimpan), 22 (scroll untuk mengamati pembekuan terlepas, S-14), dan 24 (menutup modal Changelog). Urutan hasil TC 737 tidak dipulihkan di dalam spec karena TC 738 tidak bergantung pada urutan.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 737 dan 738 tidak menyebut apakah modal Changelog tetap terbuka sesudah `[Save]` Setup Column; spec mengasumsikan modal tetap terbuka.
