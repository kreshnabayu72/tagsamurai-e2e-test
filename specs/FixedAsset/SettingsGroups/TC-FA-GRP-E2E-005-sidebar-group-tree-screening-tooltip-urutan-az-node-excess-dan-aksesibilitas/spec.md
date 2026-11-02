---
id: TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas
title: "Sidebar Group Tree: Screening, Tooltip Dot Function, Urutan A-Z, Node Excess, dan Aksesibilitas ARIA Treeitem"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-10
  - TC-FA-GRP-11
  - TC-FA-GRP-14
  - TC-FA-GRP-42
  - TC-FA-GRP-43
  - TC-FA-GRP-967
coverage:
  web: automated
---

# Sidebar Group Tree: Screening, Tooltip Dot Function, Urutan A-Z, Node Excess, dan Aksesibilitas ARIA Treeitem

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9): Head Office (Function None) > Floor 2 > IT Department > Server Room; Warehouse A (Assignable); Disposal Yard (Disposal Group); Warehouse B (Assignable, Excess). Warehouse B tampil pada tabel halaman 1 (jumlah node level 1 tidak lebih dari 10).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`) untuk TC-FA-GRP-967; pohon ini milik spec, bukan Head Office Tabel A:

| TC | Nama TC | Nama seed | Keterangan |
|---|---|---|---|
| TC-FA-GRP-967 | Head Office | `Order Parent {runId}-005` | Level 1, Function None, berisi tiga child di bawah |
| TC-FA-GRP-967 | Floor 2 | `Floor 2 {runId}-005` | Child, Assignable, dibuat pertama |
| TC-FA-GRP-967 | Basement | `Basement {runId}-005` | Child, Assignable, dibuat kedua; di langkah 46 diubah menjadi `Zeta Basement {runId}-005` |
| TC-FA-GRP-967 | alpha Wing | `alpha Wing {runId}-005` | Child, Assignable, dibuat ketiga |

- Kemampuan teknis: fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-10: Screening Sidebar Group tree

1. Klik toggle expand-all pada sidebar
2. Verifikasi header sidebar memuat Title `Groups`, Search sidebar dengan placeholder `Search group or code...` sejajar toggle expand/collapse-all, dan tombol [+] Group
3. Verifikasi root virtual `All Groups` aktif secara default
4. Verifikasi node hierarkis Head Office, Floor 2, IT Department, Server Room dengan indentasi bertambah per level
5. Verifikasi dot Function berwarna primary untuk Assignable dan dark untuk Disposal Group
6. Verifikasi node Head Office (None) tanpa dot Function
7. Verifikasi tiap node memiliki elipsis (⋯)

### TC-FA-GRP-42: Aksesibilitas sidebar tree

8. Tekan Tab sampai fokus berada pada tree sidebar
9. Verifikasi node ber-role `treeitem` dengan `aria-level` sesuai depth
10. Verifikasi `aria-expanded` setiap node sesuai state expand-nya
11. Tekan panah bawah
12. Verifikasi fokus berpindah ke node berikutnya
13. Tekan panah kanan
14. Verifikasi fokus atau state expand berubah sesuai node yang difokuskan dan `aria-expanded` mengikutinya
15. Tekan panah bawah sampai fokus berada pada node Floor 2
16. Tekan Enter
17. Verifikasi node Floor 2 terpilih dan tabel menampilkan direct children Floor 2
18. Klik node `All Groups` di sidebar

### TC-FA-GRP-11: Tooltip dot Function

19. Hover dot Function Warehouse A
20. Verifikasi tooltip `Assignable` tampil
21. Hover dot Function Disposal Yard
22. Verifikasi tooltip `Disposal Group` tampil
23. Hover node Head Office
24. Verifikasi node Head Office tanpa dot Function sehingga tidak ada tooltip Function

### TC-FA-GRP-14: Node Excess di sidebar

25. Hover node Warehouse B
26. Verifikasi nama Warehouse B di-dim tanpa badge tambahan
27. Verifikasi tooltip `Read-only — over your plan's group limit` tampil
28. Klik elipsis (⋯) Warehouse B di sidebar
29. Verifikasi menu hanya memuat Detail dan Delete
30. Verifikasi Edit dan Add Subgroup tidak dirender pada menu
31. Tutup menu dengan Esc

### TC-FA-GRP-43: Tooltip Excess via keyboard focus

32. Tekan Tab sampai fokus berada pada nama Warehouse B di tabel, tanpa hover
33. Verifikasi tooltip `Read-only — over your plan's group limit` tampil saat fokus keyboard

### TC-FA-GRP-967: Urutan sibling A-Z

34. Klik toggle collapse-all pada sidebar
35. Klik chevron node `Order Parent {runId}-005` untuk expand
36. Verifikasi child urut `alpha Wing {runId}-005`, `Basement {runId}-005`, `Floor 2 {runId}-005` (A–Z, tidak case-sensitive, per parent)
37. Klik node `Order Parent {runId}-005` di sidebar
38. Klik header kolom Group 2× (sort Group Z→A)
39. Klik ikon `Filter`
40. Pilih Function `Assignable`
41. Klik [Apply]
42. Verifikasi urutan child di sidebar tetap `alpha Wing`, `Basement`, `Floor 2` (Sort dan Filter tabel tidak mengubah urutan sidebar)
43. Klik elipsis (⋯) node `Basement {runId}-005` di sidebar
44. Klik `Edit`
45. Ganti Group Name dengan `Zeta Basement {runId}-005`
46. Klik [Save]
47. Tunggu aksi selesai (modal Edit tertutup)
48. Muat ulang halaman dengan F5
49. Klik chevron node `Order Parent {runId}-005` untuk expand
50. Verifikasi `Zeta Basement {runId}-005` berada di posisi alfabetis terakhir, setelah `Floor 2 {runId}-005`

## Notes

- Spec melewati sekitar 35 langkah (50 langkah): seluruh blok adalah satu kelas (sidebar Group Tree) pada dataset yang sama, tiap blok berdiri sendiri, dan memisahnya hanya menggandakan login, hook, dan cleanup tanpa alur baru. Blok TC-FA-GRP-967 yang mengubah data milik spec berada paling akhir (S-10).
- Langkah penghubung (S-03): langkah 1 dan 34 (expand/collapse-all), langkah 18 (kembali ke `All Groups`), langkah 31 (tutup menu), langkah 35 dan 49 (expand node), langkah 37 (memilih node sebagai konteks Sort dan Filter), langkah 47 (tunggu aksi selesai, 8b butir 8).
- Pohon urutan sibling TC-FA-GRP-967 memakai parent milik spec (`Order Parent {runId}-005`), bukan Head Office Tabel A, agar Tabel A tidak berubah (S-06).
- Temuan untuk QA:
  - TC-FA-GRP-42 menyebut "panah bawah/kanan" tanpa semantik pergerakan fokus dan expand per tombol; langkah 14 mengasersi hasilnya secara umum.
  - TC-FA-GRP-967 menyebut child dibuat berurutan acak langsung di Head Office; spec memakai parent milik spec.
  - TC-FA-GRP-967 menyebut Filter di tabel tanpa nilai; spec memakai Function `Assignable` pada child Assignable seed.
