---
id: TC-GS-UCF-E2E-001-screening-tabel-layout-tooltip-aksesibilitas-dan-urutan-default
title: "Screening Tab Custom Field: Layout 3 Zona, Tooltip Ikon, Nama Aksesibel, dan Urutan Default Field Name A-Z"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-2
  - TC-GS-UCF-5
  - TC-GS-UCF-396
  - TC-GS-UCF-6
coverage:
  web: automated
---

# Screening Tab Custom Field: Layout 3 Zona, Tooltip Ikon, Nama Aksesibel, dan Urutan Default Field Name A-Z

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings (precondition TC-GS-UCF-2: "Global Settings dibuka"); TC-GS-UCF-2 membuka tab Custom Field lewat langkah 1 dan 2. TC-GS-UCF-5, 6, dan 396 berjalan pada tab yang sama sesudahnya.
- Data Pre-setup Client A (6 field, tetap di environment, hanya dibaca, tanpa suffix): `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date`.
- Population D-01 (8 field: `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`): di-seed lewat API di hook `before` (idempotent, dilewati bila sudah ada) sehingga tabel berisi tepat 14 field (precondition TC-GS-UCF-2, 6, 396). Nama literal tanpa suffix karena asersi urutan A-Z dan jumlah 14 (pengecualian S-12 butir (i)); fixture baru `Fixture.customFieldUser.population`. Spec ini tidak mengubah atau menghapus field mana pun; hook `after` hanya menghapus field Population yang dibuat hook `before` spec ini.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: hover; fokus keyboard; pembacaan nama aksesibel (accessible name) elemen; pembacaan jumlah baris dan urutan sel tabel.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-2: Screening tab Custom Field oleh Total Control

1. Klik menu Global Settings > User di sidebar
2. Klik tab Custom Field
3. Amati tab dari atas ke bawah tanpa mengisi atau mengklik apa pun
4. Verifikasi Header: Breadcrumb `User > Custom Field`
5. Verifikasi Header: trigger Guided Tooltip `[?]` tampil di sebelah kanan Breadcrumb
6. Verifikasi segmen `User` pada Breadcrumb tidak dapat diklik (label statis)
7. Verifikasi segmen `Custom Field` pada Breadcrumb tidak dapat diklik (label statis)
8. Verifikasi Header: tab `User List | Position | Division | Custom Field` tampil dengan `Custom Field` aktif
9. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog | [+ Custom Field]` tampil
10. Verifikasi Table Tools tidak memiliki kontrol Setup Column
11. Verifikasi Body: kolom `Checkbox | Active (sortable) | Field Name (sortable) | Data Type (sortable) | Value Setting (sortable) | Placeholder (sortable) | Required (sortable) | Modified By (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable)`
12. Klik header kolom Column Visibility (⋯)
13. Verifikasi Overlay Column Visibility terbuka
14. Tutup Overlay Column Visibility dengan menekan Esc
15. Verifikasi Body: 10 baris pertama dari 14 field tampil
16. Verifikasi Body: setiap baris pada halaman 1 menampilkan Placeholder terisi nilai efektif (tidak kosong)
17. Verifikasi Body: sel Value Setting baris `Employee Grade` menampilkan `—`
18. Verifikasi Footer: Pagination default 10 per halaman
19. Buka pilihan ukuran halaman pada Pagination
20. Verifikasi Footer: opsi ukuran halaman 10, 25, 50, dan 100
21. Tutup pilihan ukuran halaman dengan menekan Esc
22. Verifikasi tidak ada Page Title terpisah di bawah Breadcrumb
23. Verifikasi tidak ada Detail page

### TC-GS-UCF-5: Hover icon Table Tools dan header kolom Actions menampilkan tooltip

24. Arahkan kursor ke icon Search
25. Verifikasi tooltip `Search`
26. Arahkan kursor ke icon Filter
27. Verifikasi tooltip `Filter`
28. Arahkan kursor ke icon Download
29. Verifikasi tooltip `Download`
30. Arahkan kursor ke icon Changelog
31. Verifikasi tooltip `Changelog`
32. Arahkan kursor ke header kolom Column Visibility (⋯)
33. Verifikasi tooltip `Column Visibility`
34. Pindahkan kursor keluar dari Table Tools dan header tabel

### TC-GS-UCF-6: Urutan default tabel adalah Field Name A-Z tanpa membedakan huruf besar kecil

35. Amati urutan baris halaman 1 dan indikator sort tanpa menyentuh header sort (tab Custom Field sudah terbuka dari TC-GS-UCF-2)
36. Verifikasi halaman 1 berurut Field Name A-Z case-insensitive: `Annual Target`, `badge number`, `Birth Date`, `Blood Type`, `Bonus`, `Cost Center`, `Emergency Phone`, `Employee Grade`, `Job Description`, `Joining Date`
37. Verifikasi tidak ada kolom yang menampilkan panah sort aktif
38. Pindah ke halaman 2 lewat Pagination
39. Verifikasi halaman 2 berisi `Office Phone`, `Shirt Size`, `Tax ID`, `Work Notes`
40. Kembali ke halaman 1 lewat Pagination

### TC-GS-UCF-396: Accessibility tab Custom Field, kontrol hanya-icon memiliki nama aksesibel

41. Periksa nama aksesibel icon Search pada Table Tools
42. Verifikasi icon Search memiliki nama aksesibel tidak kosong
43. Periksa nama aksesibel icon Filter
44. Verifikasi icon Filter memiliki nama aksesibel tidak kosong
45. Periksa nama aksesibel icon Download
46. Verifikasi icon Download memiliki nama aksesibel tidak kosong
47. Periksa nama aksesibel icon Changelog
48. Verifikasi icon Changelog memiliki nama aksesibel tidak kosong
49. Periksa nama aksesibel header kolom Column Visibility (⋯)
50. Verifikasi header kolom Column Visibility (⋯) memiliki nama aksesibel tidak kosong
51. Periksa nama aksesibel tombol `⋯` pada baris `Cost Center`
52. Verifikasi tombol `⋯` baris `Cost Center` memiliki nama aksesibel tidak kosong
53. Klik `[+ Custom Field]`
54. Periksa nama aksesibel icon `[✕]` pada header popup
55. Verifikasi icon `[✕]` memiliki nama aksesibel tidak kosong
56. Periksa nama aksesibel icon `[ℹ]` di samping label Data Type
57. Verifikasi icon `[ℹ]` memiliki nama aksesibel tidak kosong
58. Klik icon `[✕]` pada header popup (form belum diisi sehingga tertutup tanpa dialog `Unsaved Changes`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Seluruh asersi adalah baca tab (screening), tanpa aksi yang mengubah data.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 2, 5, 6, 396. TC-GS-UCF-6 (tanpa menyentuh header sort) ditaruh sebelum TC yang mengubah state tabel (tidak ada TC di spec ini yang menyortir). TC-GS-UCF-396 membuka form Create sebagai kejadian terakhir dan menutupnya sekali (langkah 53 dan 58); form kosong tidak dirty sehingga tidak memunculkan dialog `Unsaved Changes` (bagian 3 prinsip 6).
- Langkah 1 dan 2 TC-GS-UCF-2 dijalankan di spec ini sebagai satu-satunya navigasi sidebar; navigasi antar-tab dan reset sidebar diuji di spec 003. Langkah 1 TC-GS-UCF-6 ("Buka tab Custom Field") sudah terpenuhi oleh langkah 2 spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 (mengamati tab), langkah 12 dan 14 (klik header Column Visibility lalu tutup Overlay dengan Esc; Expected b TC-GS-UCF-2 menyebut header klik membuka Overlay Column Visibility), langkah 19 dan 21 (membuka dan menutup pilihan ukuran halaman untuk mengamati opsi), langkah 34 (melepas kursor dari Table Tools), langkah 38 dan 40 (pindah halaman; langkah 40 mengembalikan halaman 1 supaya baris `Cost Center` pada TC-GS-UCF-396 ada di halaman aktif), dan langkah 58 (menutup popup).
- Langkah 16 (Placeholder tidak kosong pada setiap baris halaman 1) memuat kuantor "setiap" dan didahului langkah 15 yang membuktikan 10 baris tampil sebagai pembanding (bagian 8b butir 2). Langkah 10 (tidak ada kontrol Setup Column) beranchor Table Tools yang sudah diverifikasi tampil pada langkah 9.
- Langkah 17 memakai baris `Employee Grade` (Text) sebagai wakil "sel Value Setting kosong tampil `—`" karena TC-GS-UCF-2 c tidak menyebut baris tertentu.
- Langkah 22 dan 23 adalah dua klausa Expected e TC-GS-UCF-2 ("tidak ada Page Title terpisah" dan "tidak ada Detail page"). Modul ini tidak memiliki halaman Detail (catatan TC: PRD §4.1a, tidak ada row action Detail), sehingga "tidak ada Detail page" diasersi dari struktur tab (tidak ada halaman Detail terpisah di bawah Breadcrumb); tidak ada klik baris karena TC tidak memberi langkahnya.
- Spec melewati sekitar 35 langkah (58 langkah). Seluruhnya satu kelas (screening baca tab Custom Field, satu akun, tanpa mengubah data) dan tiap blok TC berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain. Sebagian besar langkah adalah pasangan aksi hover atau periksa dan `Verifikasi` pada TC-GS-UCF-5 dan 396.
- Temuan untuk QA:
  - TC-GS-UCF-2 d menyebut opsi page size "10/25/50/100" tanpa menyebut cara membukanya; spec membuka pilihan ukuran halaman pada Pagination (langkah 19) dan menutupnya dengan Esc.
  - TC-GS-UCF-2 Expected a.i menyebut "kedua segmen tidak dapat diklik" tanpa langkah klik; spec mengasersi keduanya sebagai label statis tanpa mengklik (contoh Position mengklik segmen). Menunggu konfirmasi QA bila klik juga diharapkan.
  - TC-GS-UCF-2 Expected c ("Placeholder terisi nilai efektif") tidak menyebut baris tertentu; spec mengasersi bahwa tiap baris halaman 1 tidak kosong, dan nilai efektif per baris diuji di spec 002 (TC-GS-UCF-16 dan 17).
  - TC-GS-UCF-396 langkah 3 menyebut tombol `⋯` pada baris `Cost Center` tanpa menyebut halamannya; spec mengasumsikan baris itu ada di halaman 1 (urutan default).
  - TC-GS-UCF-1 (Population) membangun 8 field lewat UI di spec 018; spec ini memakai seed API idempotent yang sama secara literal (nama dan jumlah 14 diasersi) dan tidak bergantung pada hasil spec 018.
