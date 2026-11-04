---
id: TC-FA-TDC-E2E-205-sinkron-tab-asset-class-activity-log-approval-dan-lifecycle-aset
title: "Sinkronisasi Lintas Modul: Tab Asset Class, Activity Log, Approvals, Asset Name, dan Lifecycle Aset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-770
  - TC-FA-TDC-777
  - TC-FA-TDC-778
  - TC-FA-TDC-784
  - TC-FA-TDC-785
  - TC-FA-TDC-786
coverage:
  web: automated
---

# Sinkronisasi Lintas Modul: Tab Asset Class, Activity Log, Approvals, Asset Name, dan Lifecycle Aset

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleData`, fixture belum ada): sembilan class Example Data PRD dengan tabel dalam satu halaman (9 baris, 10 baris per halaman) sehingga baris target tidak dicari lewat Search. Kondisi yang dipakai: NB-4 Active, Used By 0, tanpa Last Posted Tax Year (TC-770, 784, 785, 786); NB-2 (`Bukan bangunan – Kelompok 2`, Useful Life 8, Used By 3 oleh tiga Asset Class) dengan aset pada ketiga Asset Class: 18 aset berlifecycle Active dan 2 aset berlifecycle bukan Active (TC-777, 778). Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data fixture BE (disediakan tim FE/BE, kunci `approvalsPending`): halaman Approvals memuat dua permintaan pending sebagai anchor (TC-786).
- Data uji: TC-777 dan TC-778 mengubah Useful Life NB-2 dari 8 menjadi 10 untuk membuka dialog Save Changes (tidak disimpan).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class, Asset Class pemakai, dan aset berdasarkan lifecycle lewat API; mengubah lifecycle satu aset ke bukan Active lewat modul Asset; membaca jumlah entri Changelog dan Activity Log serta jumlah versi class lewat kemampuan baca BE tepat sebelum aksi (8b.10); halaman Reports & Logs > Activity Log tab User Action, Settings > Asset Master > Asset Name, dan Approvals.
- State global yang diubah: status Active NB-4 (dinonaktifkan pada TC-770 dan TC-784, dipulihkan pada langkah 42 dan oleh hook `after`) dan lifecycle satu aset NB-2 (TC-778). Dipulihkan di hook `after` lewat seeding ulang data di atas.

## Test Steps

### TC-FA-TDC-785: Tax Depreciation Class dipilih lewat Asset Class dan tidak tersedia sebagai field pada Asset Name

1. Buka Settings > Accounting > Asset Class
2. Klik `+ Asset Class`
3. Verifikasi Drawer Create Asset Class memuat field Tax Depreciation Class
4. Klik `[×]` pada header Drawer Create Asset Class
5. Buka Settings > Asset Master > Asset Name
6. Klik tombol Create
7. Verifikasi form Create Asset Name memuat field Asset Name
8. Verifikasi form Create Asset Name tidak memuat field berlabel Tax Depreciation Class
9. Tutup form Create Asset Name lewat `[×]`

### TC-FA-TDC-770: Berpindah dari tab Asset Class kembali ke tab Tax Depreciation Class menampilkan data terbaru

10. Buka Settings > Accounting > Asset Class
11. Klik tab Tax Depreciation Class
12. Verifikasi tab Tax Depreciation Class terbuka
13. Klik toggle `Active` baris NB-4
14. Klik `[Deactivate]` pada dialog konfirmasi hingga status NB-4 berhasil tersimpan
15. Klik tab Asset Class
16. Klik tab Tax Depreciation Class
17. Verifikasi tab Tax Depreciation Class terbuka
18. Verifikasi toggle `Active` baris NB-4 bernilai Off

### TC-FA-TDC-777: Pratinjau dampak menghitung hanya aset dengan lifecycle Active

19. Catat jumlah versi NB-2 dan jumlah entri Changelog Tax Depreciation Class lewat kemampuan baca BE
20. Klik Class Code NB-2
21. Ubah Useful Life dari `8` menjadi `10`
22. Klik `[Save]`
23. Verifikasi baris "Asset classes affected" pada blok pratinjau dampak bernilai 3
24. Verifikasi baris "Active assets affected" bernilai 18
25. Verifikasi aset yang lifecycle-nya bukan Active tidak dihitung pada "Active assets affected" (bernilai 18, bukan 20)
26. Klik `[Cancel]` pada dialog Save Changes
27. Verifikasi dialog Save Changes tertutup
28. Verifikasi jumlah versi NB-2 sama dengan catatan sebelum `[Save]`
29. Verifikasi jumlah entri Changelog Tax Depreciation Class sama dengan catatan sebelum `[Save]`
30. Klik `[×]` pada header Drawer Edit
31. Verifikasi dialog `Unsaved Changes` tampil
32. Klik `[Leave]`

### TC-FA-TDC-778: Jumlah aset aktif terdampak mengikuti perubahan lifecycle aset

33. Ubah lifecycle satu aset pada Asset Class pemakai NB-2 menjadi bukan Active lewat modul Asset
34. Klik Class Code NB-2
35. Ubah Useful Life dari `8` menjadi `10`
36. Klik `[Save]`
37. Verifikasi baris "Active assets affected" pada blok pratinjau dampak bernilai 17
38. Klik `[Cancel]` pada dialog Save Changes
39. Klik `[×]` pada header Drawer Edit
40. Verifikasi dialog `Unsaved Changes` tampil
41. Klik `[Leave]`

### TC-FA-TDC-786: Perubahan di halaman ini berlaku langsung tanpa permintaan approval

42. Pulihkan NB-4 menjadi Active lewat seeding API dan seed dua permintaan pending di Approvals, lalu muat ulang halaman
43. Klik toggle `Active` baris NB-4
44. Klik `[Deactivate]` pada dialog konfirmasi
45. Verifikasi toggle NB-4 berubah ke Off segera setelah konfirmasi
46. Klik toggle `Active` baris NB-4
47. Klik `[Activate]` pada dialog konfirmasi
48. Verifikasi toggle NB-4 berubah ke On segera setelah konfirmasi
49. Buka halaman Approvals
50. Verifikasi halaman Approvals memuat dua permintaan pending anchor
51. Verifikasi halaman Approvals tidak memuat permintaan baru terkait Tax Depreciation Class

### TC-FA-TDC-784: Aksi Deactivate class tampil di Activity Log FAMS dengan Object Tax Depreciation Class

52. Buka Settings > Accounting > Tax Depreciation Class
53. Catat jumlah entri Activity Log tab User Action lewat kemampuan baca BE
54. Klik toggle `Active` baris NB-4
55. Klik `[Deactivate]` pada dialog konfirmasi hingga status NB-4 berhasil tersimpan
56. Buka Reports & Logs > Activity Log
57. Klik tab User Action
58. Verifikasi jumlah entri Activity Log bertambah satu dari catatan sebelum aksi
59. Verifikasi baris terbaru memuat Action `Edit`, Object `Tax Depreciation Class`, Name `NB-4`, Field `Status`, Old Value `Active`, New Value `Inactive`, dan Modified By user aktor

## Notes

- Urutan TC di spec: 785, 770, 777, 778, 786, 784. TC-785 dan TC-770 mensyaratkan NB-4 Active; TC-770 menonaktifkan NB-4 sehingga TC-786 dan TC-784 didahului pemulihan seeding NB-4 Active (langkah 42), dan TC-784 menonaktifkan NB-4 pada akhir spec.
- Langkah penghubung (S-03): langkah 1, 5, 10, 15, 49, 52, 56, 57 (berpindah halaman atau tab), langkah 4, 9, 30 sampai 32, 38 sampai 41 (menutup Drawer, form, atau dialog, S-08), langkah 19, 33, 42, 53 (pembacaan baseline dan seeding, tanpa asersi).
- Langkah 28 dan 29 (jumlah versi dan entri Changelog tetap) mengasersi Expected c TC-777 ("tidak ada versi baru dan tidak ada log") dengan selisih terhadap baseline langkah 19 (S-12). Spec absence (kelas g) tidak memuat TC-777 dan Expected TC-777 menyebut "log" tanpa menyebut surface (lihat Temuan), sehingga asersi berbaseline dilakukan di spec ini pada surface Changelog yang disebut TC pada modul ini.
- Langkah 58 dan 59: jumlah entri Activity Log dibaca sebelum aksi (langkah 53) dan selisihnya dibuktikan sebelum membaca baris terbaru (S-12, S-14, 8b.10); bila beberapa entri baru jatuh dalam menit yang sama, asersi memakai himpunan baris teratas sebanyak selisih tanpa mengandalkan urutan di antaranya.
- Asersi tambahan di luar Expected TC (S-03): langkah 27 (dialog Save Changes tertutup) tidak ada di Expected TC-777; ditulis sebagai anchor bahwa `[Cancel]` sudah diproses sebelum jumlah versi dan entri Changelog dibaca pada langkah 28 dan 29.
- Langkah 51 mengasersi absence permintaan baru di Approvals dengan anchor positif langkah 50 (dua permintaan pending yang di-seed, 8b.2).
- Alasan di atas ~35 langkah (59 langkah): satu topik (sinkronisasi tab Tax Depreciation Class dengan modul lain: Asset Class, Asset Name, Asset, Approvals, dan Activity Log). Blok NB-4 tersambung: blok TC-FA-TDC-770 menonaktifkan NB-4 (langkah 13 sampai 18), langkah 42 memulihkan NB-4 menjadi Active untuk blok TC-FA-TDC-786, dan blok 786 berakhir dengan NB-4 Active yang menjadi precondition blok TC-FA-TDC-784 (langkah 54). Blok 785, 777, dan 778 tidak bergantung pada blok lain (777 dan 778 tidak menyimpan perubahan); blok 786 dan 784 bergantung pada langkah 42, dan blok 784 bergantung pada blok 786.
- Temuan untuk QA:
  - TC-777 Expected c ("tidak ada versi baru dan tidak ada log") tidak menyebut surface log; spec memakai Changelog Tax Depreciation Class (langkah 29) dan jumlah versi (langkah 28). System Log dan Activity Log tidak diperiksa.
  - TC-777 Expected d menyebut "status lifecycle lain tidak disebut namanya"; spec hanya mengasersi bahwa nilai 18 bukan 20.
  - TC-778 tidak menyebut lifecycle tujuan aset yang diubah; spec memakai "bukan Active" dan cara mengubahnya disediakan tim FE/BE lewat modul Asset.
  - TC-784 Expected menyebut Modified By "user aktor" tanpa nama; spec menulisnya apa adanya karena akun Total Control tidak punya nama tertulis di TC.
  - TC-784, 785, 786 tidak menyebut jalur menu untuk halaman Approvals dan form Create Asset Name selain "Buka halaman Approvals" dan "Klik tombol Create"; spec mengikuti TC.
  - TC-786 tidak menyebut label tombol konfirmasi; spec memakai `[Deactivate]` dan `[Activate]` menurut D-01 dan D-03 PRD.
  - TC-785 tidak menyebut cara membuktikan bahwa field tidak ada selain "tidak memuat field berlabel Tax Depreciation Class"; spec mengasersi form Create Asset Name memuat field Asset Name lebih dulu sebagai anchor.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
