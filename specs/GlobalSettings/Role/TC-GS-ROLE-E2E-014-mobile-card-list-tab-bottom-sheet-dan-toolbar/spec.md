---
id: TC-GS-ROLE-E2E-014-mobile-card-list-tab-bottom-sheet-dan-toolbar
title: "Mobile Card List Role: Tab Total Control, Tab Read Only, Tab System, Toolbar, dan Bottom Sheet"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-285
  - TC-GS-ROLE-286
  - TC-GS-ROLE-287
coverage:
  web: automated
  mobile: automated
---

# Mobile Card List Role: Tab Total Control, Tab Read Only, Tab System, Toolbar, dan Bottom Sheet

## Prerequisites

- Mode: FE+BE.
- Perangkat: satu perangkat Android uji (kelompok Android uji A sampai E, perangkat fisik bersama) dengan aplikasi Android native terpasang. Spec menulis `parallel: false` karena perangkat dipakai bersama; suite ini juga serial.
- Akun aktor: Total Control (Ahmad Fauzi) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login di aplikasi mobile sekali di hook `before`. Akun kedua pada langkah terakhir: Client uji B (Pre-setup #14, hanya Default User sebagai Total Control), email disediakan tim FE, kredensial `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Layar awal spec: Role & Permission > Tab Total Control di aplikasi mobile dibuka di hook `beforeEach`.
- Flag Guided Tooltip: spec mobile tidak memakai hook flag suite (lihat `suite.md`, Hook suite) dan tidak menguji Guided Tooltip.
- Data Pre-setup yang dibaca: Dewi Lestari (Total Control, Inactive; Staff, Finance; Pre-setup #3), Rina Putri (Read Only, Inactive; HR Manager, HR; Pre-setup #4), Budi Santoso (Default User; Pre-setup #2), Ahmad Fauzi (aktor; Pre-setup #1), Detail "Manage TAG" (Pre-setup #10) dengan kolom Users N ≥ 2 pada client utama dan tepat 1 user pada Client uji B. Nilai N dibaca dari seeding. Spec tidak membuat, mengubah, atau menghapus data; popup dan modal dibuka lalu ditutup tanpa Assign.
- Kemampuan teknis: tap dan hover (atau long hover untuk tooltip nama lengkap) pada perangkat Android; login ke client berbeda di aplikasi mobile.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-285: Card Tab Total Control dan Tab Read Only

1. Verifikasi tabel tampil sebagai Card List
2. Verifikasi tabel horizontal tidak tampil
3. Verifikasi baris 1 card Dewi Lestari menampilkan komponen user tebal ikon user generik dan "Dewi L" serta icon `[⋯]`
4. Hover komponen user pada card Dewi Lestari
5. Verifikasi tooltip nama lengkap "Dewi Lestari" tampil
6. Verifikasi baris 2 card Dewi Lestari adalah "Staff · Finance"
7. Verifikasi baris 3 card Dewi Lestari menampilkan Status "Inactive"
8. Tap `[⋯]` pada card Dewi Lestari
9. Verifikasi `[⋯]` hanya berisi Remove
10. Tutup menu `[⋯]`
11. Klik Tab Read Only
12. Verifikasi baris 1 card Rina Putri adalah "Rina P"
13. Verifikasi baris 2 card Rina Putri adalah "HR Manager · HR"
14. Verifikasi baris 3 card Rina Putri adalah "Inactive"
15. Tap `[⋯]` pada card Rina Putri
16. Verifikasi `[⋯]` berisi Remove
17. Tutup menu `[⋯]`
18. Klik Tab Total Control
19. Tap `[⋯]` pada card Budi Santoso
20. Verifikasi item Remove tampil Disabled
21. Tutup menu `[⋯]`
22. Tap `[⋯]` pada card Ahmad Fauzi
23. Verifikasi item Remove tampil Disabled
24. Tutup menu `[⋯]`

### TC-GS-ROLE-287: Popup Table User Picker dan Modal Changelog tampil sebagai bottom sheet

25. Tap `[+ Assign]` pada Tab Total Control
26. Verifikasi Popup Assign Total Control tampil sebagai bottom sheet
27. Tutup Popup Assign Total Control
28. Tap `[Changelog]`
29. Verifikasi Modal "Changelog: Role & Permission > Total Control" tampil sebagai bottom sheet
30. Tutup Modal Changelog
31. Klik Tab System
32. Tap `[⋯]` pada card "Manage TAG", lalu tap Detail
33. Tap `[+ Assign]` pada Detail
34. Verifikasi Popup Assign Role tampil sebagai bottom sheet
35. Tutup Popup Assign Role
36. Kembali ke Role & Permission > Tab System dengan tombol Back perangkat

### TC-GS-ROLE-286: Card Tab System dan toolbar mobile

37. Klik Tab Total Control
38. Verifikasi icon `[Changelog]` tampil di header di samping `[🔍]` dan `[⋯]`
39. Verifikasi `[+ Assign]` tampil di bawah toolbar dan di atas card list
40. Tap `[⋯]` toolbar
41. Verifikasi bottom sheet toolbar berisi Column Visibility, Filter, dan Download
42. Tutup bottom sheet toolbar
43. Tap `[🔍]`
44. Verifikasi search bar inline terbuka
45. Klik `(←)` pada kotak Search
46. Klik Tab System
47. Verifikasi baris 1 card "Manage TAG" adalah "Manage TAG" dengan icon `[⋯]`
48. Verifikasi baris 2 card "Manage TAG" adalah "[N] users" sesuai kolom Users
49. Tap `[⋯]` toolbar Tab System
50. Verifikasi bottom sheet Tab System berisi Column Visibility dan Download
51. Verifikasi bottom sheet Tab System tidak berisi Filter
52. Tutup bottom sheet toolbar
53. Verifikasi `[+ Assign]` tidak tampil pada Tab System
54. Tap `[⋯]` pada card "Manage TAG"
55. Verifikasi `[⋯]` card berisi Detail
56. Tutup menu `[⋯]`
57. Logout, lalu login ke Client uji B
58. Buka Role & Permission > Tab System di aplikasi mobile
59. Verifikasi baris 2 card "Manage TAG" adalah "1 user"

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (59 langkah) karena tiga TC berada di satu kelas harness (mobile Android, card list dan toolbar, tanpa tulis data); tiap blok berdiri sendiri (membuka tab atau halaman sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-ROLE-287 dijalankan sebelum TC-GS-ROLE-286 karena langkah terakhir TC-GS-ROLE-286 (langkah 57 sampai 59) berganti ke Client uji B dan spec berakhir di akun itu; dengan urutan ini seluruh langkah akun utama selesai lebih dulu.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): tutup menu atau bottom sheet atau popup (langkah 10, 17, 21, 24, 27, 30, 35, 42, 52, 56), klik Tab Read Only, Tab Total Control, dan Tab System (langkah 11, 18, 31, 37, 46), kembali ke Tab System dengan tombol Back perangkat (langkah 36), tutup search bar (langkah 45), dan logout lalu login ke Client uji B (langkah 57).
- Langkah 2 (tabel horizontal tidak tampil) didahului langkah 1 (Card List tampil) sebagai anchor positif; langkah 51 dan 53 (Filter dan `[+ Assign]` tidak ada) didahului langkah 50 serta langkah 47 dan 48 sebagai anchor.
- Kombinasi role yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-GS-ROLE-285 dan TC-GS-ROLE-288 menyebut "hover" untuk nama lengkap pada perangkat sentuh; TC tidak menyatakan gesture pengganti, spec memakai hover (kemampuan disediakan tim FE).
  - TC-GS-ROLE-285 tidak menyatakan halaman tempat card Dewi Lestari, Rina Putri, Budi Santoso, dan Ahmad Fauzi berada; spec mengasumsikan card tampil pada halaman 1 urutan default.
  - TC-GS-ROLE-286 Expected e menyatakan Tab System "tidak ada [+ Assign]" dan tanpa Filter; icon Changelog di Tab System tidak disebut sehingga tidak diasersi.
  - TC-GS-ROLE-286 Client uji B: email akun disediakan tim FE (Pre-setup #14 tidak memuat email).
  - TC-GS-ROLE-287 tidak menyatakan cara menutup bottom sheet; spec menutupnya tanpa asersi.
  - Guided Tooltip di aplikasi mobile tidak dinyatakan TC; hook flag suite tidak berlaku untuk spec mobile, dan bila walkthrough tampil di perangkat, kemampuan menyetel flag disediakan tim FE/BE.
