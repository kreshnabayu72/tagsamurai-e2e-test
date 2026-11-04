---
id: TC-AC-DS-E2E-193-log-absence-api-ditolak-dan-promosi-default
title: "Absence Log: Request API Ditolak dan Promosi Default Otomatis Tidak Menulis Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-478
  - TC-AC-DS-495
  - TC-AC-DS-515
  - TC-AC-DS-520
  - TC-AC-DS-523
coverage:
  web: automated
---

# Absence Log: Request API Ditolak dan Promosi Default Otomatis Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun penolak: Read Only Principal PT Arunika Prima (Rina Wijaya) `readOnlySku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_RO_PASSWORD` (Pre-setup #3), dipakai hanya lewat klien HTTP dengan token `Rina Wijaya` (sesi API aktor, login API password, bukan sesi web; disediakan tim BE/FE) pada langkah 2 dan langkah 17 sampai 19.
- Akun penolak kedua: Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Dewi Lestari, Modified By `Dewi L`) `totalControlDist_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10): token `totalControlDist` untuk request pada langkah 34 dan 35, dan login UI pada langkah 31 untuk membaca System Log dan Activity Log Distributor (ganti akun eksplisit; sesi kembali ke Principal pada langkah 42).
- Token sesi API tiap akun penolak diperoleh sebelum baseline log dicatat, sehingga entri yang timbul dari penerbitan token bukan bagian dari selisih jumlah entri.
- Data Pre-setup: SKU inti `HHR-ARC-100` (2 foto, foto kedua default) dan `TAG-ARC-OBJ` serta seed (#29, #30), pohon Category (#25), Device Name (#26), Brand Principal (#27), file foto uji (#37), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33). Nilai dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: SKU `API-LOG-02` (formulir pembuatan valid) dikirim pada TC-AC-DS-495 dan ditolak sehingga tidak tercipta (kode literal sesuai TC; lihat Temuan untuk QA). Hook `before` menghapus `API-LOG-02` bila ada.
- Data yang diubah (target aksi tulis): SKU Pre-setup `HHR-ARC-100` (foto kedua yang default dihapus pada TC-AC-DS-478). TC menetapkan baris ini sebagai Pre-setup bersama; pemulihan ke dua foto semula dengan foto kedua default dijamin fixture BE (disediakan tim FE/BE) di hook `before` dan `after`, termasuk penghapusan entri Changelog yang ditambahkan spec agar Pre-setup #33 kembali 35 entri. Efek: Last Modified `HHR-ARC-100` berubah. Request yang ditolak pada TC-AC-DS-495, 515, 520, dan 523 tidak mengubah data.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server (multipart/form-data) dengan token sesi API aktor akun yang disebut; ID record SKU target (`{id}`) dibaca lewat fixture BE (TC tidak menyebut caranya); pemulihan data di atas; pembacaan jumlah entri (baseline) Changelog Principal, System Log `Rina Wijaya`, `Dewi Lestari`, dan `Jane Setiawan`, dan Activity Log tab User Action sebelum aksi (audit trail permanen; 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-495: Request API langsung yang ditolak tidak menulis log

1. Catat baseline jumlah entri Changelog Principal, System Log `Rina Wijaya`, dan Activity Log tab User Action
2. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `Rina Wijaya` (Read Only) dengan formulir pembuatan valid (`sku` `API-LOG-02`) dan tunggu respons
3. Verifikasi respons request ditolak dengan status 403
4. Muat ulang halaman
5. Ketik Search `API-LOG-02`, tekan Enter
6. Verifikasi List menampilkan "No results found" sehingga SKU `API-LOG-02` tidak ada pada List
7. Klik `(←)` pada kotak Search, lalu klik ikon Changelog
8. Verifikasi modal "Changelog: Device SKU" tampil
9. Verifikasi Changelog tidak menambah entri baru (jumlah entri sama dengan baseline langkah 1)
10. Buka Settings > User, cari user `readOnlySku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
11. Verifikasi tab System Log `Rina Wijaya` tampil
12. Verifikasi System Log `Rina Wijaya` tidak menambah entri baru (jumlah entri sama dengan baseline langkah 1)
13. Buka Activity Log, buka tab User Action
14. Verifikasi Activity Log tidak menambah entri baru (jumlah entri sama dengan baseline langkah 1)

### Pemulihan state antar TC

15. Buka Settings > Device > Device SKU

### TC-AC-DS-515: Tiga request API Read Only yang ditolak tidak menulis log

16. Catat baseline jumlah entri Changelog Principal, System Log `Rina Wijaya`, dan Activity Log tab User Action
17. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `readOnlySku`
18. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `readOnlySku`
19. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `TAG-ARC-OBJ` lewat klien HTTP dengan token `readOnlySku`
20. Verifikasi ketiga request ditolak dengan status 403
21. Klik ikon Changelog
22. Verifikasi modal "Changelog: Device SKU" tampil
23. Verifikasi Changelog tidak menambah entri baru (jumlah entri sama dengan baseline langkah 16)
24. Buka Settings > User, cari user `readOnlySku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
25. Verifikasi tab System Log `Rina Wijaya` tampil
26. Verifikasi System Log `Rina Wijaya` tidak menambah entri baru (jumlah entri sama dengan baseline langkah 16)
27. Buka Activity Log, buka tab User Action
28. Verifikasi Activity Log tidak menambah entri baru (jumlah entri sama dengan baseline langkah 16)

### Pemulihan state antar TC

29. Buka Settings > Device > Device SKU

### TC-AC-DS-520: Request API Distributor atas SKU Principal yang ditolak tidak menulis log

30. Klik ikon Changelog, catat jumlah entri Changelog Principal sebagai baseline N_CL, lalu tutup modal
31. Logout lalu login sebagai Total Control Distributor PT Cakra Distribusi (`totalControlDist_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DIST_PASSWORD`)
32. Buka Settings > User, cari user `totalControlDist_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`), buka Detail, buka tab System Log, catat jumlah entri sebagai baseline N_SL
33. Buka Activity Log, buka tab User Action, catat jumlah entri sebagai baseline N_AL
34. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `TAG-ARC-OBJ` (SKU Principal) lewat klien HTTP dengan token `totalControlDist` (formulir Edit lengkap: `sku`, `deviceNameId`, `brandId`, `model`, dan `defaultImage` berisi nilai tersimpan `TAG-ARC-OBJ`)
35. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `TAG-ARC-OBJ` (SKU Principal) lewat klien HTTP dengan token `totalControlDist`
36. Verifikasi kedua request ditolak dengan status 403 karena SKU Principal bukan milik Distributor (kepemilikan baris mengikuti `entity-isolation.md` §18.6)
37. Buka Settings > User, cari user `totalControlDist_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
38. Verifikasi tab System Log `Dewi Lestari` tampil
39. Verifikasi System Log `Dewi Lestari` tidak menambah entri baru (jumlah entri sama dengan baseline N_SL langkah 32)
40. Buka Activity Log, buka tab User Action
41. Verifikasi Activity Log tidak menambah entri baru (jumlah entri sama dengan baseline N_AL langkah 33)
42. Logout lalu login sebagai Total Control Principal PT Arunika Prima (`totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD`)
43. Buka halaman `Settings > Device > Device SKU`
44. Klik ikon Changelog
45. Verifikasi modal "Changelog: Device SKU" tampil
46. Verifikasi Changelog Principal tidak menambah entri baru (jumlah entri sama dengan baseline N_CL langkah 30)

### Pemulihan state antar TC

47. Buka Settings > Device > Device SKU

### TC-AC-DS-523: Request API ubah field terkunci yang ditolak tidak menulis log

48. Catat baseline jumlah entri Changelog Principal, System Log `Jane Setiawan`, dan Activity Log tab User Action
49. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `HHR-ARC-100` lewat klien HTTP dengan token `totalControlSku` dengan `sku` `HHR-ARC-199`, `model` `H199`, dan `rangeType` `Short Range` (formulir Edit lengkap: `sku`, `deviceNameId`, `brandId`, `model`, dan `defaultImage` berisi nilai tersimpan kecuali field yang disebut)
50. Verifikasi respons ditolak dengan status 422
51. Klik ikon Changelog
52. Verifikasi modal "Changelog: Device SKU" tampil
53. Verifikasi Changelog tidak menambah entri baru untuk `HHR-ARC-100` (jumlah entri sama dengan baseline langkah 48)
54. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
55. Verifikasi tab System Log `Jane Setiawan` tampil
56. Verifikasi System Log `Jane Setiawan` tidak menambah entri baru untuk `HHR-ARC-100` (jumlah entri sama dengan baseline langkah 48)
57. Buka Activity Log, buka tab User Action
58. Verifikasi Activity Log tidak menambah entri baru untuk `HHR-ARC-100` (jumlah entri sama dengan baseline langkah 48)

### Pemulihan state antar TC

59. Buka Settings > Device > Device SKU

### TC-AC-DS-478: Promosi default otomatis akibat penghapusan foto default tidak dicatat sebagai entri tersendiri

60. Catat baseline jumlah entri Changelog Principal
61. Ketik Search `HHR-ARC-100`, tekan Enter
62. Klik ⋯ pada baris `HHR-ARC-100`, pilih `Edit`
63. Verifikasi Popup Edit SKU tampil dengan field terisi
64. Hapus foto default (foto kedua) sehingga foto pertama otomatis menjadi default
65. Klik `[Save]`
66. Tunggu aksi selesai: Popup Edit SKU tertutup
67. Klik ikon Changelog
68. Verifikasi modal "Changelog: Device SKU" tampil dengan satu entri Field `Photo` (Old Value `—`, New Value `—`) untuk aksi hapus foto yang dilakukan pengguna (jumlah entri bertambah tepat 1 dari baseline langkah 60)
69. Verifikasi di antara entri baru (satu baris teratas sesuai selisih +1 langkah 68) tidak ada entri `Photo — Set as default` untuk promosi otomatis foto tersisa

### Pemulihan state akhir

70. Tutup modal Changelog; klik `(←)` pada kotak Search; pulihkan foto `HHR-ARC-100` ke dua foto semula dengan foto kedua default lewat fixture BE

## Notes

- P-5: spec ini adalah spec absence (kelas g, bagian 3 prinsip 13 butir g). Pemicu kelas a pada TC-AC-DS-495, 515, 520, dan 523 (request langsung yang ditolak) hanya membentuk kondisi yang diasersi tidak tercatat (S-05, `P-5` butir a); kelas a murni untuk respons ada di spec 160 (TC-515), 161 (TC-520), dan 162 (TC-523). Tiap TC punya baseline sendiri (langkah 1, 16, 30 sampai 33, 48, 60). Pemicu pada TC-AC-DS-478 (hapus foto default) adalah aksi pengguna biasa.
- Asersi absence didahului anchor positif (8b butir 2): respons 403 (langkah 3, 20, 36) dan 422 (langkah 50), "No results found" Search (langkah 6), modal Changelog tampil (langkah 8, 22, 45, 52), tab System Log tampil (langkah 11, 25, 38, 55), dan entri Photo yang tampil (langkah 68) sebelum asersi absence atau jumlah.
- TC-AC-DS-495, 515, 520, dan 523 hanya mengasersi hasil request yang ditolak (status respons dan jumlah entri log); perilaku FE atas respons itu tidak diasersi (8b butir 1). Request langsung memakai klien HTTP, bukan browser.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 16, 30, 32, 33, 48, dan 60 (baseline, S-12), langkah 5 dan 61 (Search untuk menemukan baris target, R-16), langkah 15, 29, 47, 59, dan 70 (S-03, S-09), serta langkah 31 dan 42 (ganti akun eksplisit demi membaca System Log dan Activity Log Distributor lalu Changelog Principal; sesi berakhir di akun default suite).
- Pembagian TC lintas spec (S-05): TC-AC-DS-206, 482, dan 484 (absence atas Edit tanpa perubahan dan field terkunci) ada di spec 151. TC-AC-DS-515 (Expected butir a dan b: status respons dan state data), TC-AC-DS-520 (Expected butir a dan b), dan TC-AC-DS-523 (Expected butir a) diasersi di spec 160, 161, dan 162; Expected log (515 butir c, 520 butir c, 523 butir b) diasersi di spec ini dengan request penolakan, user, dan baseline sendiri.
- Pengecualian S-12 A-11: `HHR-ARC-100` dan `TAG-ARC-OBJ` adalah SKU Pre-setup bernama literal tanpa suffix (dinyatakan di `suite.md`); `HHR-ARC-100` dipulihkan fixture BE setelah TC-AC-DS-478. `API-LOG-02` mengikuti kode literal TC dan tidak pernah tersimpan.
- Spec melebihi sekitar 35 langkah (70 langkah); alasan: semua blok satu kelas harness (g, absence log) dan berdiri sendiri karena state dipulihkan antar blok, kegagalan satu blok tidak membuat blok lain kehilangan makna; tiap blok punya pemicu, akun, dan baseline log sendiri, dan sebagian besar langkah adalah blok baca-log berpola (buka surface, `Verifikasi` jumlah entri).
- Langkah 69 dibatasi pada entri baru (selisih +1 dari baseline langkah 60, dibaca pada baris teratas), bukan seluruh Changelog, karena Pre-setup #33 sudah memuat entri `Photo — Set as default` (seed lama).
- Temuan untuk QA:
  - S-15: Expected TC 495 butir b menyebut "tidak ada entri baru" pada System Log `Rina Wijaya` tanpa anchor positif yang dijamin (log akun Read Only mungkin kosong); spec memakai tab System Log tampil dan selisih jumlah entri terhadap baseline.
  - S-15: TC 495 langkah 4, TC 515 langkah 4, dan TC 523 langkah 2 menyebut "sesi pengamat" Total Control; spec memakai sesi default suite (Jane Setiawan, Pre-setup #1) tanpa ganti akun.
  - S-15: TC 520 langkah 7 membaca Changelog Principal sesudah login Principal sementara aktor utama Distributor; spec mencatat baseline Changelog Principal lebih dulu, lalu login Distributor untuk baseline dan pembacaan System Log dan Activity Log, lalu kembali ke Principal untuk membaca Changelog.
  - S-15: TC 523 Expected butir b menyebut "tidak memuat entri baru untuk `HHR-ARC-100`" pada System Log dan Activity Log tanpa cara menyaring per SKU; spec membandingkan jumlah entri tiap surface terhadap baseline.
  - S-06: TC menghapus foto pada baris Pre-setup bersama; pemulihan bergantung fixture BE yang belum ada.
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Rina Wijaya`, `Dewi Lestari`, dan `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; `Fixture.settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`, `AC_DS_RO_PASSWORD`, `AC_DS_DIST_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
