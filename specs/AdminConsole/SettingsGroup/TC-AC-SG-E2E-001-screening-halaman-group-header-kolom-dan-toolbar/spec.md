---
id: TC-AC-SG-E2E-001-screening-halaman-group-header-kolom-dan-toolbar
title: "Screening Halaman Settings > Group: Tabel Utama, Group Context Header, Kolom, dan Toolbar"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-01
  - TC-AC-SG-02
  - TC-AC-SG-03
  - TC-AC-SG-04
coverage:
  web: automated
---

# Screening Halaman Settings > Group: Tabel Utama, Group Context Header, Kolom, dan Toolbar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group, root `All Groups` tidak dihitung) dan Total User per node (#17) yang menghasilkan agregat "Total User: 10" dan "Total Member: 12" (#19).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-001`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-01: Screening halaman Settings > Group dengan node All Groups terpilih

1. Susuri halaman dari atas ke bawah dan kiri ke kanan tanpa mengklik apa pun
2. Verifikasi Breadcrumb "Settings > Group" tampil di luar Card
3. Verifikasi tidak ada Page Title Header di bawah Breadcrumb
4. Verifikasi tombol `[?]` tampil tepat di sebelah kanan Breadcrumb
5. Verifikasi body kiri berisi `Card` (Outlined) tanpa title dan subtitle
6. Verifikasi Card memuat Group Context Header "All Groups"
7. Verifikasi Group Context Header menampilkan "Total User: 10"
8. Verifikasi Group Context Header menampilkan "Total Member: 12"
9. Verifikasi Toolbar menampilkan Search, Filter, Download, dan Changelog
10. Verifikasi Filter Panel tertutup
11. Verifikasi tabel memuat 14 group dengan 10 baris pada halaman 1
12. Verifikasi Pagination tampil
13. Verifikasi body kanan berisi `Card` (Outlined, With Title And Subtitle) Sidebar Group Tree dengan Title "Groups"
14. Verifikasi Subtitle Sidebar Group Tree "Select a group to filter the table."
15. Verifikasi baris pencarian tampil pada Sidebar Group Tree
16. Verifikasi tombol `[+] Group` tampil pada Sidebar Group Tree
17. Verifikasi seluruh node tree ter-expand
18. Verifikasi tree menampilkan "All Groups (14)" dalam keadaan aktif
19. Verifikasi Bulk Actions Bar tidak tampil (belum ada baris terpilih)
20. Verifikasi tidak ada tombol create di toolbar tabel

### TC-AC-SG-02: Screening Group Context Header pada node All Groups

21. Perhatikan Group Context Header di atas toolbar
22. Verifikasi Group Context Header menampilkan "All Groups"
23. Verifikasi Group Context Header menampilkan "Total User: 10" (agregat distinct lintas seluruh tree, bukan penjumlahan per node)
24. Verifikasi Group Context Header menampilkan "Total Member: 12" (agregat distinct lintas seluruh tree, bukan penjumlahan per node)
25. Klik angka "Total User" pada Group Context Header, lalu klik angka "Total Member"
26. Verifikasi angka pada Group Context Header tidak dapat diklik dan tidak membuka popup apa pun
27. Cari ikon ⋯ atau menu aksi pada Group Context Header
28. Verifikasi Group Context Header tidak memiliki ikon ⋯ atau menu aksi apa pun

### TC-AC-SG-03: Screening kolom tabel utama Group List

29. Perhatikan header tabel dari kiri ke kanan
30. Verifikasi kolom berurutan: Checkbox (paling kiri, pinned), Group, Total User, Total Member, Modified By, Last Updated, Actions `⋯` (paling kanan, pinned)
31. Verifikasi header kolom Group, Total User, Total Member, Modified By, dan Last Updated memiliki ikon sort
32. Verifikasi kolom Checkbox dan Actions tidak memiliki ikon sort
33. Verifikasi sel Total User dan Total Member berupa number link tanpa underline
34. Verifikasi sel Modified By berupa teks polos dengan format "[First Name] [Last Initial]"
35. Verifikasi sel Last Updated mengikuti format General Settings
36. Hover header kolom Total User dan Total Member
37. Verifikasi header tabel tidak wrap ke dua baris

### TC-AC-SG-04: Screening Toolbar tabel utama dan tooltip ikon

38. Verifikasi Toolbar rata kanan berurutan Search, Filter, Download, Changelog tanpa tombol create
39. Hover ikon Search
40. Verifikasi tooltip ikon pertama "Search"
41. Hover ikon Filter
42. Verifikasi tooltip ikon kedua "Filter"
43. Hover ikon Download
44. Verifikasi tooltip ikon ketiga "Download"
45. Hover ikon Changelog
46. Verifikasi tooltip ikon keempat "Changelog"
47. Hover header kolom Actions `⋯`
48. Verifikasi tooltip header kolom Actions "Column Visibility"
49. Cari tombol `[+] Group` atau tombol create lain pada toolbar tabel
50. Verifikasi tombol `[+] Group` hanya ada di Sidebar Group Tree
51. Verifikasi tidak ada tombol setara `[+] Group` di toolbar tabel

## Notes

- Ukuran spec (51 langkah, di atas smell sekitar 35 langkah): satu halaman, satu keadaan awal, seluruhnya baca-saja; empat blok TC screening tidak mengubah state sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan tiap klausa Expected menjadi `Verifikasi` sendiri (S-01). Tooltip empat ikon toolbar masing-masing satu pasangan hover dan `Verifikasi` karena tooltip adalah state sementara (bagian 8b butir 5).
- Langkah pembuka "Buka halaman `Settings > Group`" tiap TC dilakukan hook `beforeEach` suite; kondisi "halaman tampil dengan node `All Groups` terpilih" terbukti oleh langkah 18 dan 22.
- Langkah penghubung (S-03): langkah 1, 21, 27, 29, dan 49 mengamati tanpa asersi sendiri; asersinya ada pada `Verifikasi` sesudahnya.
- Urutan Expected TC-AC-SG-03 dan TC-AC-SG-04 mengikuti state (bagian 8b butir 5): langkah hover header kolom (langkah 36) ditulis sebelum `Verifikasi` header tidak wrap; Expected TC-AC-SG-04 butir a (urutan ikon) diasersi sebelum hover.
- Temuan untuk QA:
  - TC-AC-SG-03 langkah 3 (hover header kolom Total User dan Total Member) tidak punya Expected padanan; spec menuliskannya sebagai aksi tanpa asersi (langkah 36).
  - TC-AC-SG-01 Expected b menyebut "tabel 14 group (10 baris pada halaman 1)"; ukuran halaman default 10 diasersi dari klausa itu, bukan dari kolom lain TC.
