---
id: TC-GS-ROLE-E2E-012-mobile-detail-selection-mode-header-import-data-toggle-dan-pagination
title: "Mobile Detail Role: Header Import data, Keluar dari Selection Mode, Toggle Inert, dan Pagination Card List"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-288
  - TC-GS-ROLE-310
  - TC-GS-ROLE-311
  - TC-GS-ROLE-312
coverage:
  web: automated
  mobile: automated
---

# Mobile Detail Role: Header Import data, Keluar dari Selection Mode, Toggle Inert, dan Pagination Card List

## Prerequisites

- Mode: FE+BE.
- Perangkat: satu perangkat Android uji (kelompok Android uji A sampai E, perangkat fisik bersama) dengan aplikasi Android native terpasang. Spec menulis `parallel: false` karena perangkat dipakai bersama; suite ini juga serial.
- Akun aktor: Total Control (Ahmad Fauzi) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login di aplikasi mobile sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Layar awal spec: Role & Permission > Tab System di aplikasi mobile dibuka di hook `beforeEach`.
- Flag Guided Tooltip: spec mobile tidak memakai hook flag suite (lihat `suite.md`, Hook suite) dan tidak menguji Guided Tooltip.
- Data Pre-setup yang dibaca: Doni Pratama dengan baris role Import data (Create, Read) dan Manage TAG (Pre-setup #10); Siti Nurhaliza dengan baris role Manage TAG (Pre-setup #4); Detail "Manage hardware" berisi lebih dari 101 baris eligible (Pre-setup #17). Spec tidak membuat, mengubah, atau menghapus data; toggle dan aksi `[Remove]` tidak dijalankan.
- Kemampuan teknis: long-press, tap, dan hover (atau long hover untuk tooltip nama lengkap) pada perangkat Android; membaca jumlah entri Changelog "Manage TAG" (disediakan tim FE/BE; cara membuka Modal Changelog Detail di mobile tidak disebut di TC dan PRD); tombol Back perangkat Android untuk kembali ke Tab System.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-288: Detail Import data menampilkan header breadcrumb tanpa Back serta toggle Create dan Read saja

1. Tap `[⋯]` pada card "Import data", lalu tap Detail
2. Verifikasi Breadcrumb header adalah "Role & Permission > System > Detail"
3. Verifikasi Title header adalah "Import data"
4. Verifikasi link "← Back" terpisah tidak ada
5. Verifikasi baris 1 card Doni Pratama menampilkan ikon user generik dan "Doni P"
6. Hover komponen user pada card Doni Pratama
7. Verifikasi tooltip nama lengkap "Doni Pratama" tampil
8. Verifikasi toggle Create tampil pada card Doni Pratama
9. Verifikasi toggle Read tampil pada card Doni Pratama
10. Verifikasi toggle Read checked
11. Verifikasi toggle Read disabled
12. Verifikasi baris toggle Update dan Delete tidak ada pada card Doni Pratama
13. Tap `[⋯]` pada card Doni Pratama
14. Verifikasi `[⋯]` hanya berisi Remove
15. Tutup menu `[⋯]`
16. Kembali ke Role & Permission > Tab System dengan tombol Back perangkat

### TC-GS-ROLE-310: Keluar dari selection mode lewat [✕] dan lewat uncheck seluruh card

17. Tap `[⋯]` pada card "Manage TAG", lalu tap Detail
18. Long-press card Doni Pratama
19. Tap `[✕]` pada Floating Bottom Bulk Bar
20. Verifikasi seluruh seleksi dibatalkan dan checkbox card hilang
21. Verifikasi Floating Bottom Bulk Bar hilang
22. Long-press card Doni Pratama lagi
23. Verifikasi selection mode aktif dengan counter "1 Selected"
24. Tap card Doni Pratama untuk menghapus centang
25. Verifikasi counter "0 Selected"
26. Verifikasi checkbox card hilang
27. Verifikasi Floating Bottom Bulk Bar hilang

### TC-GS-ROLE-311: Toggle C/R/U/D inert selama selection mode dan ketuk card memilih atau melepas card

28. Catat nilai toggle Update card Doni Pratama dan card Siti Nurhaliza
29. Catat jumlah entri Changelog "Manage TAG"
30. Long-press card Doni Pratama
31. Verifikasi selection mode aktif
32. Verifikasi card Doni Pratama terpilih
33. Verifikasi counter "1 Selected"
34. Tap toggle Update pada card Doni Pratama
35. Tap toggle Update pada card Siti Nurhaliza
36. Verifikasi toggle Update card Doni Pratama sama dengan nilai tercatat
37. Verifikasi toggle Update card Siti Nurhaliza sama dengan nilai tercatat
38. Verifikasi tidak ada dialog yang tampil
39. Verifikasi tidak ada toast yang tampil
40. Tap card Siti Nurhaliza di luar toggle
41. Verifikasi card Siti Nurhaliza terpilih
42. Verifikasi counter "2 Selected"
43. Tap card Siti Nurhaliza sekali lagi
44. Verifikasi card Siti Nurhaliza terlepas
45. Verifikasi counter "1 Selected"
46. Tap `[✕]` pada Floating Bottom Bulk Bar
47. Verifikasi jumlah entri Changelog "Manage TAG" sama dengan jumlah tercatat
48. Kembali ke Role & Permission > Tab System dengan tombol Back perangkat

### TC-GS-ROLE-312: Card list memakai Pagination default 10 dan Select All hanya memilih card halaman aktif

49. Tap `[⋯]` pada card "Manage hardware", lalu tap Detail
50. Verifikasi 10 card tampil pada halaman pertama
51. Verifikasi Pagination tampil
52. Long-press satu card
53. Tap `[Select All]`
54. Verifikasi seluruh card pada halaman aktif yang checkbox-nya enabled tercentang
55. Verifikasi counter "[N] Selected" sama dengan jumlah card tercentang itu
56. Verifikasi N tidak lebih dari 10
57. Verifikasi N tidak sama dengan total baris eligible Detail "Manage hardware"
58. Tap `[✕]` pada Floating Bottom Bulk Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (58 langkah) karena empat TC berada di satu kelas harness (mobile Android, Detail role, tanpa tulis data); tiap blok membuka Detail sendiri dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok TC-GS-ROLE-310 dan TC-GS-ROLE-311 memakai Detail "Manage TAG" yang sama dan keduanya mengakhiri selection mode sebelum blok berikutnya (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 15 (tutup menu), langkah 16 dan 48 (kembali ke Tab System dengan tombol Back perangkat), langkah 28 dan 29 (baseline nilai toggle dan Changelog sebelum aksi), langkah 46 dan 58 (`[✕]` mengakhiri selection mode).
- Langkah 28 dan 29 menjadi baseline untuk asersi "toggle tidak berubah" dan "tidak ada entri baru di Changelog" (langkah 36, 37, dan 47); Modal Changelog dibuka dan ditutup di sekitar langkah 29 dan 47.
- Langkah 1, 17, dan 49 membuka Detail lewat `[⋯]` card Tab System (TC-GS-ROLE-286 f: `[⋯]` card berisi Detail).
- Langkah 50 sampai 57: N = jumlah card tercentang (Expected b TC-GS-ROLE-312); "tidak sama dengan total baris eligible" dibaca dari seeding (lebih dari 101 baris), bukan dari satu halaman tabel (bagian 8b butir 10).
- Temuan untuk QA:
  - TC-GS-ROLE-288 dan TC-GS-ROLE-285 menyebut "hover" untuk nama lengkap pada perangkat sentuh; TC tidak menyatakan gesture pengganti, spec memakai hover (kemampuan disediakan tim FE).
  - TC-GS-ROLE-311 Expected b menyebut "tidak ada request" saat toggle diketuk; request jaringan tidak teramati dari sisi perangkat sehingga tidak diasersi (yang diasersi: nilai toggle, dialog, toast, dan Changelog).
  - TC-GS-ROLE-311 tidak memberi cara membuka Changelog "Manage TAG" di mobile Detail (TC-GS-ROLE-287 hanya membuka Changelog dari Tab Total Control).
  - TC-GS-ROLE-288, TC-GS-ROLE-310, TC-GS-ROLE-311, dan TC-GS-ROLE-312 tidak menyatakan cara kembali dari Detail ke Tab System (header tanpa link "← Back", TC-GS-ROLE-288 Expected e); spec memakai tombol Back perangkat.
  - TC-GS-ROLE-312 membutuhkan lebih dari 101 baris eligible (kelas volume data) tetapi berada di spec mobile ini sesuai pembagian TC.
  - TC-GS-ROLE-310 Expected c menyebut counter "0 Selected" sekaligus selection mode berakhir; spec mengasersi counter lebih dulu lalu checkbox dan bar hilang.
  - Guided Tooltip di aplikasi mobile tidak dinyatakan TC; hook flag suite tidak berlaku untuk spec mobile, dan bila walkthrough tampil di perangkat, kemampuan menyetel flag disediakan tim FE/BE.
