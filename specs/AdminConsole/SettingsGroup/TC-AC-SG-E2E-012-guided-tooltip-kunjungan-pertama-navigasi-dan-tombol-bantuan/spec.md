---
id: TC-AC-SG-E2E-012-guided-tooltip-kunjungan-pertama-navigasi-dan-tombol-bantuan
title: "Guided Tooltip Settings > Group: Kunjungan Pertama, Back/Skip, dan Tombol [?]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-46
  - TC-AC-SG-47
  - TC-AC-SG-48
coverage:
  web: automated
---

# Guided Tooltip Settings > Group: Kunjungan Pertama, Back/Skip, dan Tombol [?]

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Pengecualian atas hook suite: spec ini menguji Guided Tooltip sehingga mengatur flag `guided_tooltip_seen_ac-settings-group` sendiri sesudah hook (flag disetel belum `seen` sebelum tiap blok TC dan dipulihkan oleh hook `after` suite).
- Kemampuan teknis: Fixture BE untuk membaca dan menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` pada akun aktor; disediakan tim FE/BE (lihat `suite.md`).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-012`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global selain flag Guided Tooltip akun aktor yang dipulihkan hook suite.

## Test Steps

### TC-AC-SG-46: Guided Tooltip otomatis pada kunjungan pertama menampilkan 4 step

1. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
2. Muat ulang halaman Settings > Group dengan F5
3. Verifikasi walkthrough mulai otomatis dengan indikator "Step 1 of 4"
4. Verifikasi Step 1 menyorot Sidebar Group Tree
5. Verifikasi Step 1 Title "Group Tree"
6. Verifikasi Step 1 Description "Browse your group hierarchy here. Use the search to find a group, and click a node to filter the table to its subgroups."
7. Klik `[Next]`
8. Verifikasi Step 2 menyorot Table
9. Verifikasi Step 2 Title "Group Details"
10. Verifikasi Step 2 Description "Click the numbers in a row to see the users and entities assigned to that group. Available columns depend on your Column Visibility settings."
11. Klik `[Next]`
12. Verifikasi Step 3 menyorot header kolom Actions
13. Verifikasi Step 3 Title "Table Columns"
14. Verifikasi Step 3 Description "Choose which columns to show in the table."
15. Klik `[Next]`
16. Verifikasi Step 4 menyorot Toolbar Search dan Download
17. Verifikasi Step 4 Title "Search & Export"
18. Verifikasi Step 4 Description "Search groups across the table or export the current list."
19. Verifikasi tombol pada step terakhir berlabel `[Done]`
20. Klik `[Done]` untuk menutup walkthrough

### TC-AC-SG-47: Navigasi Back dan Skip pada Guided Tooltip

21. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
22. Muat ulang halaman Settings > Group dengan F5
23. Verifikasi tombol `[Back]` tidak tampil pada Step 1
24. Klik `[Next]`
25. Verifikasi tombol `[Back]` tampil pada Step 2
26. Klik `[Back]`
27. Verifikasi walkthrough kembali ke Step 1 dengan Title "Group Tree"
28. Klik `[Skip]`
29. Verifikasi walkthrough tertutup
30. Muat ulang halaman dengan F5
31. Verifikasi Breadcrumb "Settings > Group" tampil
32. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang
33. Verifikasi flag Guided Tooltip `seen` tersimpan untuk akun aktor

### TC-AC-SG-48: Tombol [?] di sebelah kanan Breadcrumb mengulang walkthrough dari Step 1

34. Setel flag Guided Tooltip `seen` untuk akun aktor lewat Fixture BE
35. Hover tombol `[?]` di sebelah kanan Breadcrumb
36. Verifikasi tooltip hover tombol `[?]` "Show guide"
37. Klik tombol `[?]`
38. Verifikasi walkthrough mulai dari Step 1 dengan Title "Group Tree" walau flag `seen` sudah ada
39. Verifikasi flag Guided Tooltip `seen` tidak di-reset (tetap `seen`)
40. Klik `[Skip]` untuk menutup walkthrough

## Notes

- Ukuran spec (40 langkah, di atas smell sekitar 35 langkah): satu halaman, satu komponen (Guided Tooltip), dan tiap blok TC dimulai dengan flag yang disetel ulang sehingga berdiri sendiri; tiap Title dan Description setiap step menjadi `Verifikasi` sendiri (S-01).
- Langkah penghubung (S-03, S-09): langkah 1, 21, dan 34 (menyetel flag sebelum tiap blok), langkah 20 dan 40 (menutup walkthrough sebelum blok berikutnya).
- Temuan untuk QA:
  - TC-AC-SG-47 Expected b menyebut "menandai seen"; TC tidak memberi langkah observasi flag. Spec membaca flag lewat Fixture BE (kemampuan disediakan tim FE/BE, langkah 33); begitu pula "flag seen tidak di-reset" pada TC-AC-SG-48 (langkah 39).
  - Mekanisme membaca dan menyetel flag Guided Tooltip tidak dijelaskan TC; disediakan tim FE/BE.
