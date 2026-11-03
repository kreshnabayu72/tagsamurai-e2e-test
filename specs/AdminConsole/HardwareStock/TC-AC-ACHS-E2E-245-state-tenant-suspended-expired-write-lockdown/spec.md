---
id: TC-AC-ACHS-E2E-245-state-tenant-suspended-expired-write-lockdown
title: "State Tenant Suspended dan Expired: Write Lockdown Add Stock, Sync, Delete, dan Approvals"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-108
  - TC-AC-ACHS-109
  - TC-AC-ACHS-158
  - TC-AC-ACHS-168
  - TC-AC-ACHS-199
  - TC-AC-ACHS-200
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Write Lockdown Add Stock, Sync, Delete, dan Approvals

## Prerequisites

- Mode: FE+BE.
- Akun default suite: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun eksplisit: Distributor Pre-setup No 10, role Manage hardware stock, Local Registration aktif, `distributorCakra_automated_qaTeam1@qwertysystem.net` (Pre-setup No 10); password memakai nama env `AC_<ROLE>_PASSWORD` yang ditetapkan tim FE (belum terdaftar; lihat Temuan untuk QA).
- State global yang diubah (kelas h; pelaku dan mekanisme mengubah status entitas tidak disebut TC, sehingga disediakan tim FE/BE lewat sesi API aktor): status Suspended entitas Distributor Pre-setup No 10 (No 10b), status Expired entitas Principal (No 10c), status Suspended entitas Distributor Pre-setup No 12 (No 12b) lalu diaktifkan kembali. Setiap status dipulihkan ke aktif di langkah penghubung sesudah bloknya dan di hook `after` spec ini (tetap jalan walau spec gagal di tengah). Suite berjalan serial.
- Efek pada Pre-setup: TC-199 menyetujui Subject Register Duplicate `{subjectWfa}` sehingga Subject berpindah ke Tab History dan unit `{snWfa28}` menjadi Available (Data Dinamis TC-180); pemulihan baseline dijamin fixture backend yang disediakan tim FE/BE dan dinyatakan di suite.md. Spec ini dijalankan sesudah spec baca (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): simulator reader USB (service driver mock Handheld Reader, Pre-setup No 25) untuk Sync Serial Number `{snSync}` pada TC-158; membaca state data (unit, Subject) lewat fixture BE; pembaca berkas CSV hasil Download.
- Data Pre-setup (hanya dibaca kecuali disebut di atas): unit `{snCakraFx}` milik Distributor Pre-setup No 10 (No 27), Subject Register Duplicate `{subjectWfa}` milik Distributor Pre-setup No 12 Local Registration nonaktif (No 12, 21). Data Dinamis: Serial Number `SN-SUSP-{runId}-245` dan `SN-EXP-{runId}-245` (tidak tersimpan karena ditolak). Serial Number Sync `{snSync}` dari TC (tidak tersimpan karena ditolak).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `{snWfa28}` | #17 Tabel E baris N = 28 | Serial Number unit Waiting for Approval SKU Long Range, milik Distributor Pre-setup #12 | `Fixture.hardwareStock.p17.e[28].serialNumber` |
| `{subjectWfa}` | #21 Tabel C baris 10 | Matched Identifier Subject Register Duplicate pending untuk unit Waiting for Approval (sama dengan Serial Number unit N = 28) | `Fixture.hardwareStock.p21.c[10].matchedIdentifier` |
| `{snSync}` | #25 | Serial Number perangkat simulasi driver mock untuk Sync (TC-158) | `Fixture.hardwareStock.p25.syncSerial` |
| `{snCakraFx}` | #27 | Serial Number unit Available pertama SKU Smart Fixed Reader milik Distributor Pre-setup #10 | `Fixture.hardwareStock.p27.fx[1].serialNumber` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen untuk akun default suite. Flag halaman Stock List dan Stock Detail akun Distributor disetel true di hook `before` spec ini dan dipulihkan di hook `after`; kemampuan disediakan tim FE/BE.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Distributor Pre-setup No 10 berstatus Suspended (TC-AC-ACHS-108, 158, 168)

1. Setel entitas Distributor Pre-setup No 10 berstatus Suspended (Pre-setup No 10b)
2. Logout, lalu login sebagai Distributor (Pre-setup No 10)
3. Klik menu Hardware > Stock di sidebar
4. Klik `(⋯)` pada baris `{skuFx}`, klik opsi `Add Stock`
5. Ketik `SN-SUSP-{runId}-245` di textarea Serial Numbers
6. Klik `[Submit]`
7. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
8. Klik `[Cancel]`
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik `[Leave]`
11. Ketik Search `SN-SUSP-{runId}-245`, tekan Enter
12. Verifikasi empty state `No results found` (tidak ada unit `SN-SUSP-{runId}-245` tersimpan)
13. Klik `(←)` pada kotak Search
14. Verifikasi Stock Detail berfungsi: sedikitnya satu baris unit tampil
15. Klik icon Download, pilih `Download as CSV`
16. Verifikasi Download berfungsi: berkas CSV terunduh
17. Klik segmen breadcrumb `Stock`
18. Verifikasi Stock List berfungsi: sedikitnya satu baris SKU tampil
19. Klik `(⋯)` pada baris `{skuLong}`, klik opsi `Add Stock`
20. Sinkronkan unit `{snSync}` lewat `[Sync]` dengan simulator reader USB
21. Klik `[Submit]`
22. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
23. Klik `[Cancel]`
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik `[Leave]`
26. Ketik Search `{snSync}`, tekan Enter
27. Verifikasi empty state `No results found` (tidak ada unit `{snSync}` tersimpan)
28. Klik segmen breadcrumb `Stock`
29. Klik `(⋯)` pada baris `{skuFx}`, klik row action `Detail`
30. Ketik Search Serial Number `{snCakraFx}`, tekan Enter
31. Klik `(⋯)` pada baris unit milik Distributor Pre-setup No 10, klik `Delete`, klik `[Delete]`
32. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
33. Verifikasi unit `{snCakraFx}` tetap ada pada Tab Available
34. Pulihkan entitas Distributor Pre-setup No 10 menjadi aktif

### Principal berstatus Expired (TC-AC-ACHS-109, 200)

35. Logout, lalu login sebagai Total Control (Pre-setup No 1)
36. Setel entitas Principal berstatus Expired (Pre-setup No 10c)
37. Klik menu Hardware > Stock di sidebar
38. Klik `(⋯)` pada baris `{skuFx}`, klik opsi `Add Stock`
39. Ketik `SN-EXP-{runId}-245` di textarea Serial Numbers
40. Klik `[Submit]`
41. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
42. Klik `[Cancel]`
43. Verifikasi dialog `Unsaved Changes` tampil
44. Klik `[Leave]`
45. Ketik Search `SN-EXP-{runId}-245`, tekan Enter
46. Verifikasi empty state `No results found` (tidak ada unit `SN-EXP-{runId}-245` tersimpan)
47. Klik menu Approvals > Hardware Stock di sidebar
48. Pastikan Tab Active aktif
49. Klik row action `Review` pada Subject `{subjectWfa}`
50. Pilih radio `Approve`
51. Klik `[Submit]`
52. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
53. Verifikasi state data: Subject `{subjectWfa}` tetap pending
54. Klik `[Cancel]` pada dialog Detail Approval
55. Pulihkan entitas Principal menjadi aktif

### Approve atas unit milik Distributor Suspended (TC-AC-ACHS-199)

56. Klik menu Approvals > Hardware Stock di sidebar
57. Pastikan Tab Active aktif
58. Klik row action `Review` pada Subject `{subjectWfa}`
59. Setel entitas Distributor Pre-setup No 12 berstatus Suspended (Pre-setup No 12b)
60. Pilih radio `Approve`, klik `[Submit]`
61. Verifikasi toast error "The distributor that owns this unit is not active."
62. Verifikasi state data: Subject dan unit `{snWfa28}` tetap `Waiting for Approval`
63. Aktifkan kembali entitas Distributor Pre-setup No 12
64. Klik `[Submit]` kembali dengan radio `Approve` terpilih
65. Verifikasi toast "Success, duplicate has been approved."
66. Klik Tab `History`
67. Verifikasi Subject `{subjectWfa}` tampil dengan Approval `Approved` meskipun toggle Local Registration Distributor Pre-setup No 12 nonaktif

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-108, 109, 158, 168, 199, 200). Tidak ada TC hanya-BE di spec ini.
- Kelas h (state tenant, write lockdown). TC dari Add Stock manual, Sync, Delete, dan Approvals dikumpulkan di satu spec; Read tetap berfungsi (TC-108).
- P-7: TC-158 inheren membutuhkan simulator reader USB (kelas d, Sync dengan driver mock Pre-setup No 25) bersama konteks state tenant (kelas h) dalam alurnya sendiri; ia berada di spec kelas h ini. Blok tanpa USB (TC-108, 109, 168, 199, 200) tidak memakai simulator.
- Urutan TC pada spec: Distributor Suspended (TC-108, 158, 168), Principal Expired (TC-109, 200), lalu TC-199 terakhir karena TC-199 menyetujui Subject `{subjectWfa}` sedangkan TC-200 mensyaratkan Subject itu masih pending (TC-200 mendahului TC-199).
- Spec memuat Step ganti akun eksplisit (langkah 2 dan 35); bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal keras karena tiap blok menyetel dan memulihkan status entitasnya sendiri.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): menyetel dan memulihkan status entitas (langkah 34 dan langkah sejenis), Step ganti akun, `[Cancel]` lalu `[Leave]` untuk menutup form Add Stock yang dirty (dialog `Unsaved Changes` diwajibkan S-08), Search untuk memeriksa tidak adanya unit tersimpan atau menemukan baris target (R-16), dan klik menu sidebar atau breadcrumb. `[Cancel]` pada dialog Detail Approval menutup dialog yang tersisa sebelum aksi berikutnya (S-09).
- Spec di atas smell 35 langkah (67 langkah). Alasan: semua blok satu kelas harness (state tenant, kelas h) yang berbagi pola yang sama (set status entitas, aksi tulis ditolak, pulihkan), keenam TC berdiri sendiri dengan pemulihan status sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Tidak ada literal Pre-setup: spec merujuk lewat tabel Parameter Pre-setup sehingga tidak memerlukan pengecualian S-12. `{snSync}` adalah Serial Number perangkat simulasi dari TC-158 (data driver mock No 25), bukan record Pre-setup yang dibaca dari tabel; nilai persisnya disetel pada simulator oleh tim FE/BE.
  - TC-108, 109, 158, dan 168 Expected b ("tidak ada unit tersimpan" dan "unit tetap ada") tidak memberi langkah observasi pada Langkah Uji; spec mengobservasinya lewat Search di Stock Detail.
  - TC-199 menyebut Pre-setup No 12b (Distributor Pre-setup No 12 Suspended) dan Expected c "Approve berhasil" mengubah baseline Approvals; Subject `{subjectWfa}` tidak bisa dipulihkan dari UI. Pemulihan harus dijamin fixture backend (S-06).
  - TC-199 Expected d ("Toggle Local Registration yang nonaktif tidak menghalangi Approve atau Reject") hanya teramati lewat keberhasilan Approve; Reject tidak diuji TC ini.
  - TC-199 langkah 7 ("Ulangi Approve") tidak menyebut apakah dialog masih terbuka sesudah toast error; spec mengasumsikan dialog tetap terbuka dengan radio `Approve` terpilih.
  - TC-168 langkah 3 tidak menyebut dialog konfirmasi Delete; spec tidak mengasersi isi dialog, hanya toast dan unit tetap ada.
  - TC-158 mensyaratkan Distributor yang Suspended menjalankan Sync lewat simulator USB; TC-158 tidak menyebut Expected untuk hasil Sync pada layar sebelum Submit (tabel Synced Units) dan hanya mengasersi toast serta tidak adanya unit tersimpan.
  - Nama pelaku dan mekanisme mengubah status Suspended atau Expired entitas tidak disebut TC, PRD, atau LLD yang dibaca; disediakan tim FE/BE (S-13).
  - Password akun Distributor memakai nama env `AC_<ROLE>_PASSWORD` yang belum terdaftar; diminta dari tim FE.
