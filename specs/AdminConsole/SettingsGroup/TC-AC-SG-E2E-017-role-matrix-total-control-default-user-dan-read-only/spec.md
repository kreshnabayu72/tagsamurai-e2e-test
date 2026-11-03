---
id: TC-AC-SG-E2E-017-role-matrix-total-control-default-user-dan-read-only
title: "Role Matrix: Total Control, Default User, dan Read Only pada Settings > Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-17
  - TC-AC-SG-60
  - TC-AC-SG-61
  - TC-AC-SG-62
  - TC-AC-SG-77
coverage:
  web: automated
---

# Role Matrix: Total Control, Default User, dan Read Only pada Settings > Group

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control entitas Principal (akun aktor pertama); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun (Pre-setup) | Env password |
|---|---|---|---|
| TC-AC-SG-60, 17 (bagian Total Control), 77 (bagian Total Control) | Total Control entitas Principal | #1 `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`) | `Spectra.env.AC_TC_PASSWORD` |
| TC-AC-SG-61 | Default User entitas Principal | #1 (email yang sama dengan Total Control; lihat Temuan untuk QA) | `Spectra.env.AC_SG_DU_PASSWORD` |
| TC-AC-SG-62, 17 (bagian Read Only), 77 (bagian Read Only) | Read Only entitas Principal | #2 `readOnlyGroup_automated_{namaCompany}@qwertysystem.net` (`Rina Wijaya`) | `Spectra.env.AC_SG_RO_PASSWORD` |
| TC-AC-SG-17 (bagian Manage group tanpa capability mutasi) | Manage group aktif tanpa Create/Update/Delete | #10 `manageGroupNone_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGNONE_PASSWORD` |

- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group, root `All Groups` tidak dihitung) dibaca saja; spec tidak menulis data.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Blok akun Total Control: TC-AC-SG-60, bagian Total Control TC-AC-SG-17 dan TC-AC-SG-77

1. Verifikasi `[+] Group`, pohon penuh, Search sidebar, angka Total User/Total Member (dapat diklik), Download, Changelog, kolom Checkbox, tombol `⋯`, dan ikon Column Visibility semuanya Show
2. Ketik Search `Region A`, tekan Enter
3. Klik ikon `⋯` pada baris `Region A`
4. Verifikasi Overlay Row Action memuat "+ Add Subgroup", "Edit", dan "Delete"
5. Tutup Overlay Row Action dengan Esc
6. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
7. Verifikasi label root di Sidebar Group Tree menampilkan "All Groups (14)" untuk Total Control
8. Verifikasi seluruh 14 node tampil pada tree untuk Total Control (tidak ada node tersembunyi atau disabled)
9. Catat urutan dan jumlah node Sidebar Group Tree dan baris tabel All Groups sebagai pembanding langkah 34

### Blok akun Default User: TC-AC-SG-61

10. Ganti akun: logout, lalu login sebagai Default User entitas Principal (`totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_DU_PASSWORD`)
11. Buka halaman `Settings > Group` lewat sidebar
12. Ketik Search `Region A`, tekan Enter
13. Klik ikon `⋯` pada baris `Region A`
14. Verifikasi `[+] Group` dan kolom Checkbox Show seperti Total Control
15. Verifikasi `⋯` menampilkan "+ Add Subgroup", "Edit", dan "Delete"
16. Tutup Overlay Row Action dengan Esc
17. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### Blok akun Read Only: TC-AC-SG-62, bagian Read Only TC-AC-SG-17 dan TC-AC-SG-77

18. Ganti akun: logout, lalu login sebagai Read Only entitas Principal (`readOnlyGroup_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_RO_PASSWORD`)
19. Buka halaman `Settings > Group` lewat sidebar
20. Verifikasi Hidden: `[+] Group`, kolom Checkbox, dan tombol `⋯` pada baris tabel dan node sidebar (bukan Disabled, tombolnya tidak dirender)
21. Verifikasi Show: pohon penuh, Search sidebar, angka Total User/Total Member, Download, Changelog, dan ikon Column Visibility
22. Ketik Search `Region A`, tekan Enter
23. Klik angka Total User baris `Region A`
24. Verifikasi popup Users terbuka
25. Tutup popup Users
26. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
27. Klik ikon Download pada toolbar
28. Verifikasi Download dapat dipakai (ikon enabled dan klik tidak menampilkan pesan error)
29. Klik ikon Changelog pada toolbar
30. Verifikasi Changelog dapat dipakai (Modal "Changelog: Group" tampil)
31. Tutup Modal "Changelog: Group"
32. Verifikasi label root di Sidebar Group Tree menampilkan "All Groups (14)" untuk Read Only
33. Verifikasi seluruh 14 node tampil pada tree untuk Read Only (tidak ada node tersembunyi atau disabled)
34. Verifikasi urutan dan jumlah node Sidebar Group Tree (14 node) dan baris tabel All Groups (14 baris) identik dengan yang dicatat pada langkah 9

### Blok akun Manage group tanpa capability mutasi: TC-AC-SG-17

35. Ganti akun: logout, lalu login sebagai Manage group tanpa capability mutasi (`manageGroupNone_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_MGNONE_PASSWORD`)
36. Buka halaman `Settings > Group` lewat sidebar
37. Verifikasi label root di Sidebar Group Tree menampilkan "All Groups (14)" untuk Manage group tanpa capability mutasi
38. Verifikasi seluruh 14 node tampil pada tree untuk Manage group tanpa capability mutasi (tidak ada node tersembunyi atau disabled)

## Notes

- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). TC-AC-SG-17 dan TC-AC-SG-77 melibatkan lebih dari satu aktor dan ditulis per blok aktor; urutan aktor diubah (Total Control lebih dulu, Read Only sesudahnya) untuk meminimalkan ganti akun, sehingga TC-AC-SG-77 membandingkan sisi Read Only dengan daftar yang dicatat pada blok Total Control (langkah 9 dan 34).
- Alasan di atas sekitar 35 langkah: satu halaman (Settings > Group), seluruhnya baca-saja; tiga blok akun berbagi satu pencatatan pembanding (langkah 9) yang dibandingkan pada langkah 34, sehingga pemisahan akan menggandakan seeding dan login tanpa menambah isolasi, dan tiap klausa Expected menjadi `Verifikasi` sendiri (S-01).
- Langkah penghubung (S-03, R-16): langkah 2 dan 12 (Search `Region A` untuk menemukan baris target karena tabel All Groups terbagi dua halaman), langkah 5 dan 16 (tutup overlay), langkah 6 dan 17 (klik `(←)` pada kotak Search, mengosongkan Search sesudah overlay ditutup), langkah 9 (mencatat daftar node dan baris sebagai pembanding), langkah 22 dan 26 (Search `Region A` untuk menemukan baris target sebelum klik angka Total User, lalu klik `(←)` pada kotak Search sesudah popup ditutup), langkah 25 dan 31 (tutup popup dan modal).
- Temuan untuk QA:
  - Pre-setup #1 memakai satu email untuk Total Control dan Default User (`Budi Santoso`); spec memakai `AC_SG_DU_PASSWORD` untuk blok Default User sesuai kode di `suite.md`. Bila kedua peran adalah akun yang sama, nilai password kedua env var identik; bila berbeda, email akun Default User perlu ditambahkan ke Pre-setup.
  - TC-AC-SG-62 Expected butir c "Download/Changelog dapat dipakai" tidak menyebut indikator teramati; spec mengasersi ikon Download enabled tanpa pesan error saat diklik dan Modal "Changelog: Group" tampil untuk Changelog.
  - TC-AC-SG-77 langkah 3 "Ulangi sebagai Total Control" tidak menyebut akun; spec memakai akun Total Control Pre-setup #1.
