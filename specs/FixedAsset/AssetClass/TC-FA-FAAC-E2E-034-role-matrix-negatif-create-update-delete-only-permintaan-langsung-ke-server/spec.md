---
id: TC-FA-FAAC-E2E-034-role-matrix-negatif-create-update-delete-only-permintaan-langsung-ke-server
title: "Role Matrix Negatif: Create-Only, Update-Only, dan Delete-Only Tidak Dapat Menjalankan Aksi di Luar Hak (UI dan Permintaan Langsung ke Server)"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-598
  - TC-FA-FAAC-599
  - TC-FA-FAAC-600
sourceRules: ["§4.8#r3", "§4.8#r16", "§4.8#r17", "§4.8#r18", "§4.8#r20", "ST-32", "§3.9#r8", "§4.8#r14", "E-FAAC-78", "§9.3#r3", "§9.3#r4", "§4.8#r11", "§9.3#r2"]
smoke: []
dependsOn: []
trace:
  "§4.8#r3": [1, 19, 33]
  "§4.8#r16": [4, 23, 37]
  "§4.8#r17": [4, 23, 37]
  "§4.8#r18": [4, 23, 37]
  "§4.8#r20": [4, 23, 37]
  "ST-32": [7, 40]
  "§3.9#r8": [7, 40]
  "§4.8#r14": 8
  "E-FAAC-78": [11, 12, 13, 14, 15, 16, 27, 28, 29, 30, 43, 44, 45, 46]
  "§9.3#r3": [11, 12, 44]
  "§9.3#r4": [13, 28]
  "§4.8#r11": [20, 34]
  "§9.3#r2": [27, 43]
coverage:
  web: automated
---

# Role Matrix Negatif: Create-Only, Update-Only, dan Delete-Only Tidak Dapat Menjalankan Aksi di Luar Hak (UI dan Permintaan Langsung ke Server)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Create-Only) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Create-Only | `createOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_CO_PASSWORD` | TC-FA-FAAC-598 |
| Update-Only | `updateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_UO_PASSWORD` | TC-FA-FAAC-599 |
| Delete-Only | `deleteOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_DO_PASSWORD` | TC-FA-FAAC-600 |

- Env var: `FA_AC_CO_PASSWORD`, `FA_AC_UO_PASSWORD`, `FA_AC_DO_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Asset Class B-ANCHOR (Anchor Heavy Equipment, Active; seed Pre-setup, dependensi TC-FA-FAAC-87 dijalankan lewat seeding API). Dibaca, tidak diubah; permintaan yang ditolak tidak mengubah data. Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE).
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: ganti akun (logout lalu login); klien HTTP yang menyertakan sesi aktor ini (kemampuan disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca); kemampuan baca BE untuk jumlah Asset Class dan state B-ANCHOR (keberadaan, Class Name, status Active); hover pada elemen dan membaca tooltip.

## Test Steps

### TC-FA-FAAC-598

1. Verifikasi Table Tools (Search, Filter, Download, Changelog) dan tabel Asset Class tampil
2. Ketik Search `B-ANCHOR`, tekan Enter
3. Klik ikon ⋯ pada baris B-ANCHOR
4. Verifikasi menu ⋯ hanya memuat Duplicate (Edit dan Delete tidak ada)
5. Tutup menu ⋯
6. Arahkan kursor ke toggle Active baris B-ANCHOR
7. Verifikasi toggle kolom Active Disabled dengan tooltip "You don't have permission to edit."
8. Verifikasi kolom Checkbox dan Bulk Action Bar Hidden
9. Catat baseline lewat kemampuan baca BE (disediakan tim FE/BE): keberadaan, Class Name, dan status Active B-ANCHOR
10. Kirim permintaan Edit, Deactivate, dan Delete Asset Class B-ANCHOR langsung ke server tanpa melewati browser
11. Verifikasi respons server atas permintaan Edit ditolak dengan status 403
12. Verifikasi respons server atas permintaan Deactivate ditolak dengan status 403
13. Verifikasi respons server atas permintaan Delete ditolak dengan status 403
14. Verifikasi keberadaan B-ANCHOR tidak berubah dibanding baseline
15. Verifikasi Class Name B-ANCHOR tidak berubah dibanding baseline
16. Verifikasi status Active B-ANCHOR tidak berubah dibanding baseline

### TC-FA-FAAC-599

17. Ganti akun: logout, lalu login sebagai Update-Only
18. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
19. Verifikasi Table Tools (Search, Filter, Download, Changelog) dan tabel Asset Class tampil
20. Verifikasi Button [+ Asset Class] dan link "Use recommended classes" Hidden
21. Ketik Search `B-ANCHOR`, tekan Enter
22. Klik ikon ⋯ pada baris B-ANCHOR
23. Verifikasi menu ⋯ hanya memuat Edit (Duplicate dan Delete tidak ada)
24. Tutup menu ⋯
25. Catat baseline lewat kemampuan baca BE (disediakan tim FE/BE): jumlah Asset Class dan keberadaan B-ANCHOR
26. Kirim permintaan Create dan Delete Asset Class langsung ke server tanpa melewati browser
27. Verifikasi respons server atas permintaan Create ditolak dengan status 403
28. Verifikasi respons server atas permintaan Delete ditolak dengan status 403
29. Verifikasi jumlah Asset Class tidak berubah dibanding baseline
30. Verifikasi keberadaan B-ANCHOR tidak berubah dibanding baseline

### TC-FA-FAAC-600

31. Ganti akun: logout, lalu login sebagai Delete-Only
32. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
33. Verifikasi Table Tools (Search, Filter, Download, Changelog) dan tabel Asset Class tampil
34. Verifikasi Button [+ Asset Class] Hidden
35. Ketik Search `B-ANCHOR`, tekan Enter
36. Klik ikon ⋯ pada baris B-ANCHOR
37. Verifikasi menu ⋯ hanya memuat Delete (Edit dan Duplicate tidak ada)
38. Tutup menu ⋯
39. Arahkan kursor ke toggle Active baris B-ANCHOR
40. Verifikasi toggle kolom Active Disabled dengan tooltip "You don't have permission to edit."
41. Catat baseline lewat kemampuan baca BE (disediakan tim FE/BE): jumlah Asset Class dan Class Name B-ANCHOR
42. Kirim permintaan Create dan Edit Asset Class langsung ke server tanpa melewati browser
43. Verifikasi respons server atas permintaan Create ditolak dengan status 403
44. Verifikasi respons server atas permintaan Edit ditolak dengan status 403
45. Verifikasi jumlah Asset Class tidak berubah dibanding baseline
46. Verifikasi Class Name B-ANCHOR tidak berubah dibanding baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Spec defense-in-depth (kelas a) per role: UI diasersi tanpa kontrol yang tidak berhak, lalu permintaan langsung ke server diasersi ditolak 403.
- `K-1`: TC defense-in-depth dengan Expected respons API (status respons dan state data lewat fixture BE) tetap masuk spec FE+BE walau tumpang tindih dengan dokumen TC BE; TC granular tetap sumber dan tiap TC tepat satu spec.
- Pembagian TC lintas spec (S-05): TC-598, TC-599, dan TC-600 ada di spec ini (UI, status respons 403, dan state data) dan di spec 194 (klausa "tidak ada entri baru di Changelog Asset Class, System Log, maupun Activity Log" dengan permintaan yang sama sebagai pemicu serta baseline log sendiri). Spec ini tidak mengasersi log.
- Bagian 8b butir 1: langkah permintaan langsung ke server hanya mengasersi respons (status) dan state data lewat kemampuan baca BE; perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Spec ini melewati sekitar 35 langkah. Alasan: ketiga blok satu kelas (defense-in-depth per role) dan satu topik (aksi di luar hak ditolak), tiap blok role berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; tiap TC memuat klausa respons 403 per permintaan dan klausa state data per field yang masing-masing wajib punya `Verifikasi` sendiri (S-01).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 21, dan 35 (Search untuk menemukan baris target, R-16), langkah 5, 24, dan 38 (menutup menu ⋯, S-09), langkah 17 dan 31 (ganti akun), langkah 18 dan 32 (membuka tab Asset Class sesudah login ulang, S-07).
- Baseline state dicatat ulang sebelum aksi pemicu tiap TC (langkah 9, 25, dan 41) dan asersi memakai perbandingan terhadap baseline TC itu (S-12).
- Asersi Hidden UI didahului `Verifikasi` Table Tools dan tabel tampil sebagai anchor positif permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAC-598 sampai 600 tidak menyebut baris untuk row action; spec memakai B-ANCHOR (baris yang dipakai TC role matrix negatif sejenis) dan menemukannya lewat Search.
  - TC-FA-FAAC-599 menyebut link "Use recommended classes" Hidden, tetapi link itu hanya ada pada EmptyState tabel kosong sedangkan precondition tidak menyebut tabel kosong; asersi Hidden-nya (langkah 20) tidak membuktikan apa pun bila tabel berisi.
  - Endpoint dan bentuk permintaan langsung ke server tidak disebut TC maupun PRD; ditulis sebagai kemampuan yang disediakan tim FE/BE (S-13).
