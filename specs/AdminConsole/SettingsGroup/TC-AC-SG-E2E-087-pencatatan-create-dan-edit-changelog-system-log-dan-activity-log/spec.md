---
id: TC-AC-SG-E2E-087-pencatatan-create-dan-edit-changelog-system-log-dan-activity-log
title: "Pencatatan Create dan Edit Group: Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-325
  - TC-AC-SG-326
  - TC-AC-SG-327
  - TC-AC-SG-340
coverage:
  web: automated
---

# Pencatatan Create dan Edit Group: Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke Activity Log Admin Console dan ke Settings > User > Detail akun aktor > Tab System Log tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before`, dihapus hook `after`; setiap nama bersuffix `{runId}-087`): `Region B {runId}-087` (level 1), `Region C Satu {runId}-087` (level 1), `Region C Dua {runId}-087` (level 1), semuanya tanpa entitas. Pohon Uji Utama (Pre-setup #16) tidak diubah.
- Data yang dibuat langkah spec: `Region Log Satu {runId}-087` (level 1) dan `Branch Log {runId}-087` (anak `Region B {runId}-087`), serta hasil rename `Region C Log {runId}-087` dan `Region C Sys {runId}-087`.
- Changelog, Activity Log, dan System Log adalah audit trail permanen. Entri dikenali lewat nama group bersuffix unik (baseline nol, S-12); entri induk `Region B {runId}-087` dibandingkan terhadap baseline yang dicatat sebelum aksi.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan group; disediakan tim FE/BE). Jam server dan jam browser sinkron; tidak ada asersi tanggal.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-325: Create group level 1 menghasilkan satu entri Changelog, System Log, dan Activity Log

1. Klik `[+] Group` di Sidebar Group Tree
2. Ketik `Region Log Satu {runId}-087` lalu klik `[Submit]`
3. Tunggu hingga entri log muncul
4. Klik ikon Changelog pada toolbar
5. Verifikasi Modal "Changelog: Group" memuat tepat 1 entri untuk Group Name `Region Log Satu {runId}-087`
6. Verifikasi entri itu: Action `Create`, Group Name `Region Log Satu {runId}-087`, Field `Group Name`, Old Value `—`, New Value `Region Log Satu {runId}-087`, Modified By `Budi S`
7. Tutup Modal Changelog dengan `✕`
8. Buka Activity Log Admin Console dan saring Object `Group`
9. Verifikasi Activity Log memuat 1 entri dengan Action `Create`, Object `Group`, Name `Region Log Satu {runId}-087`, dan target entity entitas Principal (pemilik tree)
10. Buka Settings > User > Detail akun aktor > Tab System Log
11. Verifikasi System Log aktor memuat 1 entri dengan Action `Create`, Object `Group`, Name `Region Log Satu {runId}-087`

### TC-AC-SG-326: Create subgroup menghasilkan satu entri Changelog

12. Buka Settings > Group lewat sidebar, lalu klik node `All Groups` di Sidebar Group Tree
13. Ketik Search `{runId}-087` pada toolbar tabel utama, tekan Enter
14. Catat Modified By dan Last Updated baris `Region B {runId}-087` pada tabel All Groups
15. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel
16. Klik ikon Changelog pada toolbar
17. Catat jumlah entri untuk Group Name `Region B {runId}-087` sebagai baseline
18. Tutup Modal Changelog dengan `✕`
19. Klik ikon `⋯` pada node `Region B {runId}-087` di sidebar lalu `+ Add Subgroup`
20. Ketik `Branch Log {runId}-087` lalu klik `[Submit]`
21. Tunggu hingga entri log muncul
22. Klik ikon Changelog pada toolbar
23. Verifikasi Modal "Changelog: Group" memuat tepat 1 entri baru untuk Group Name `Branch Log {runId}-087`
24. Verifikasi entri itu: Action `Create`, Group Name `Branch Log {runId}-087`, Field `Group Name`, Old Value `—`, New Value `Branch Log {runId}-087`
25. Verifikasi jumlah entri untuk Group Name `Region B {runId}-087` sama dengan baseline (tidak ada entri tambahan untuk parent)
26. Tutup Modal Changelog dengan `✕`
27. Klik node `All Groups` di Sidebar Group Tree
28. Ketik Search `{runId}-087` pada toolbar tabel utama, tekan Enter
29. Verifikasi Modified By dan Last Updated baris `Region B {runId}-087` sama dengan nilai yang dicatat sebelum Add Subgroup
30. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

### TC-AC-SG-327: Edit group menghasilkan satu entri Changelog dengan Old Value dan New Value

31. Klik ikon `⋯` pada node `Region C Satu {runId}-087` di sidebar lalu `Edit`
32. Ubah nama menjadi `Region C Log {runId}-087` lalu klik `[Save]`
33. Tunggu hingga entri log muncul
34. Klik ikon Changelog pada toolbar
35. Verifikasi Modal "Changelog: Group" memuat tepat 1 entri baru untuk Group Name `Region C Log {runId}-087`
36. Verifikasi entri itu: Action `Edit`, Group Name `Region C Log {runId}-087`, Field `Group Name`, Old Value `Region C Satu {runId}-087`, New Value `Region C Log {runId}-087`
37. Tutup Modal Changelog dengan `✕`
38. Buka Activity Log Admin Console dan saring Object `Group`
39. Verifikasi Activity Log memuat entri Action `Edit` untuk Name `Region C Log {runId}-087` dengan Old `Region C Satu {runId}-087` dan New `Region C Log {runId}-087`
40. Buka Settings > User > Detail akun aktor > Tab System Log
41. Verifikasi System Log aktor memuat entri Action `Edit` untuk Name `Region C Log {runId}-087` dengan Old `Region C Satu {runId}-087` dan New `Region C Log {runId}-087`

### TC-AC-SG-340: System Log tercatat di halaman user aktor dengan Name = group

42. Buka Settings > Group lewat sidebar
43. Klik ikon `⋯` pada node `Region C Dua {runId}-087` di sidebar lalu `Edit`
44. Ubah nama menjadi `Region C Sys {runId}-087` lalu klik `[Save]`
45. Tunggu hingga entri log muncul
46. Buka Settings > User > Detail akun aktor > Tab System Log
47. Verifikasi System Log aktor memuat entri Action `Edit`, Object `Group`, Name `Region C Sys {runId}-087`, Field `Group Name`, Old `Region C Dua {runId}-087`, New `Region C Sys {runId}-087`

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): membuka kembali Settings > Group dan memilih node `All Groups`, mencatat nilai dan baseline, menutup Modal Changelog dengan `✕`, serta menunggu entri log muncul (pencatatan bersifat eventual).
- Langkah penghubung (S-03, S-14): langkah 13 dan 28 (Search `{runId}-087` agar baris `Region B {runId}-087` terbaca; tabel All Groups berisi 18 group sehingga baris target tidak dijamin di halaman 1) dan langkah 15 dan 30 (klik `(←)` untuk menutup input dan mereset tabel).
- Pembagian TC: TC-AC-SG-328 dan TC-AC-SG-125 (Edit tanpa perubahan) ada di spec 090. TC-AC-SG-329 sampai 337 ada di spec 088 dan 091.
- S-05: TC-AC-SG-326 memuat klausa "tidak ada entri tambahan untuk parent `Region B`" dan "Modified By dan Last Updated tidak berubah"; keduanya ditulis sebagai hitungan berbaseline dan perbandingan terhadap nilai yang dicatat, bukan asersi absence kelas g.
- Alasan di atas sekitar 35 langkah: seluruh langkah satu topik (pencatatan Create dan Edit) dan satu harness (tiga surface audit trail). Langkah membaca surface log berpola (buka surface, cari entri, `Verifikasi` kolom log) terjadi di langkah 4 sampai 11, 16 sampai 18, 22 sampai 26, 34 sampai 41, dan 46 sampai 47 dan tidak dihitung menurut bagian 3 (prinsip 13, Smell); tanpa blok baca-log spec berada di bawah 35 langkah.
- Modified By diasersi berformat `[First Name] [Last Initial]` (R-14): nama tampil aktor `Budi Santoso` menjadi `Budi S`.
- Pemulihan: group milik spec dihapus hook `after` lewat Fixture BE; Pohon Uji Utama tidak disentuh.
- Temuan untuk QA:
  - TC-AC-SG-325 Expected butir b menyebut "target entity entitas pemilik tree" tanpa nama entitas; spec memakai entitas Principal.
  - Edit `Region C` pada TC-AC-SG-327 dan TC-AC-SG-340 menarget node Pre-setup yang sama; spec memakai dua node milik spec (`Region C Satu` dan `Region C Dua`) agar tiap TC punya baseline sendiri (S-06); TC memakai nama Pre-setup `Region C` dan `Region B`.
