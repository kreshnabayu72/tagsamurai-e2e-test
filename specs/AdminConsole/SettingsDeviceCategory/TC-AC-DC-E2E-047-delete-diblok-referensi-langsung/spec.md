---
id: TC-AC-DC-E2E-047-delete-diblok-referensi-langsung
title: "Delete Category: Diblok oleh Device Name Pengacu pada Node, Descendant, dan Daftar Panjang"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-134
  - TC-AC-DC-136
  - TC-AC-DC-137
  - TC-AC-DC-138
coverage:
  web: automated
---

# Delete Category: Diblok oleh Device Name Pengacu pada Node, Descendant, dan Daftar Panjang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup yang hanya dibaca dan tidak pernah diubah (Delete selalu diblokir guard; pengecualian S-06 untuk Pre-setup in-use yang dirancang TC untuk blokir): pohon #14 node `Industrial Scanner` dengan anak `Rugged` dan `Rugged Kit`, `Dipakai Leaf`, `Referensi Banyak`, di bawah `Hardware` > `Handheld Reader`; Device Name Pre-setup #15 `TS-200` (Category `Rugged`), `TS-210` (`Rugged Kit`), `HR-100` (`Dipakai Leaf`), dan `RB-01` sampai `RB-12` (`Referensi Banyak`). Nama node dan Device Name dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE). Spec tidak membuat data dan tidak menjalankan aksi tulis; Last Updated node dan Device Name tidak berubah.
- Kemampuan teknis: jumlah total entri Changelog dibaca sebagai baseline sebelum aksi (kemampuan baca jumlah total disediakan tim FE/BE) karena nama node Pre-setup dipakai juga oleh entri spec lain.

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Catat jumlah total entri Changelog sebagai baseline
4. Klik `[×]` pada modal Changelog

### Delete diblok oleh Device Name pada descendant (TC-134)

5. Hover node `Industrial Scanner`, klik aksi Delete
6. Verifikasi dialog blok muncul langsung dengan judul "Cannot Delete Category"
7. Verifikasi isi dialog memuat bullet `TS-200` (pada `Rugged`) dan `TS-210` (pada `Rugged Kit`) saja
8. Verifikasi isi dialog diakhiri "This category (or one of its subcategories) is still used by a device name. Remove the reference before deleting."
9. Verifikasi hanya satu tombol `[OK]`
10. Klik `[OK]`
11. Verifikasi node `Industrial Scanner`, `Rugged`, dan `Rugged Kit` tetap ada tanpa penghapusan sebagian

### Delete leaf yang dirujuk langsung (TC-136) dan tombol OK (TC-138)

12. Hover node `Dipakai Leaf`, klik aksi Delete
13. Verifikasi dialog blok "Cannot Delete Category" memuat bullet `HR-100`
14. Verifikasi isi dialog memuat teks "This category (or one of its subcategories) is still used by a device name. Remove the reference before deleting."
15. Klik `[OK]`
16. Verifikasi dialog tertutup
17. Verifikasi tree tidak berubah dan node `Dipakai Leaf` tetap ada
18. Verifikasi tidak ada toast

### Dialog blok menampilkan semua Device Name pengacu (TC-137)

19. Hover node `Referensi Banyak`, klik aksi Delete
20. Gulir daftar bullet di dalam dialog
21. Verifikasi seluruh 12 Device Name pengacu (`RB-01` sampai `RB-12`) tampil sebagai bullet terpisah dalam daftar scrollable
22. Verifikasi tidak ada ringkasan jumlah dan tidak ada teks "and [N] more"
23. Verifikasi hanya satu tombol `[OK]`
24. Klik `[OK]`

### Pemeriksaan akhir tidak ada entri baru

25. Klik ikon Changelog pada header Sidebar Category
26. Verifikasi jumlah total entri Changelog sama dengan baseline
27. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 4 dan 27 (menutup modal Changelog), langkah 10, 15, 24 (`[OK]` menutup dialog blok; langkah 15 juga bagian Expected TC-138).
- S-05: klausa "tidak ada entri log" pada TC-134, TC-136, TC-138 dinyatakan sebagai asersi jumlah dengan baseline (langkah 3 dan 26), bukan asersi absence kelas g.
- Verifikasi absence pada langkah 18 memakai dialog blok yang baru tertutup pada langkah 16 sebagai anchor.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada nama literal Pre-setup #14 dan #15 (`Industrial Scanner`, `TS-200`, `TS-210`, `Dipakai Leaf`, `HR-100`, `Referensi Banyak`, `RB-01` sampai `RB-12`) yang hanya dibaca; tidak ada data milik spec yang dapat menggantikannya tanpa mengubah teks bullet yang dijadikan Expected oleh TC.
  - TC-134 menyatakan fixture dinamis `IND-1` tidak ada pada TC ini; spec mengasersi daftar bullet hanya `TS-200` dan `TS-210`, yang mencakup ketiadaan `IND-1`.
  - Daftar bullet pada TC-134 tidak menyebut urutan; spec tidak mengasersi urutan bullet.
