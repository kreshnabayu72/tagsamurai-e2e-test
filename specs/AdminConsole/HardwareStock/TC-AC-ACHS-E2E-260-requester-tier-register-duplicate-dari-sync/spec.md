---
id: TC-AC-ACHS-E2E-260-requester-tier-register-duplicate-dari-sync
title: "Requester per Tier pada Register Duplicate dari Add Stock Sync"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-140
  - TC-AC-ACHS-141
  - TC-AC-ACHS-143
  - TC-AC-ACHS-144
  - TC-AC-ACHS-145
  - TC-AC-ACHS-146
coverage:
  web: automated
---

# Requester per Tier pada Register Duplicate dari Add Stock Sync

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List dan Approvals untuk akun aktor suite, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20, #24, dan #27. Suite serial (`parallel: false`). Flag Guided Tooltip akun selain Total Control disetel true di hook `before` spec ini dan dipulihkan di `after`.
- Login di hook `before` spec ini: Total Control {accTc} (baris pertama tabel); halaman Hardware > Stock dibuka hook `beforeEach` suite. Akun lain login lewat Step ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji (tier requester):

| Tier requester | Akun (Pre-setup) | Env password | Blok langkah |
|---|---|---|---|
| Total Control ({accTc}) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (#1) | `Spectra.env.AC_TC_PASSWORD` | 1 sampai 21 (TC-140), 74 sampai 77 (pengamat TC-145) |
| Default User ({accDu}) | `defaultUserPrincipal_automated_qaTeam1@qwertysystem.net` (#2) | `Spectra.env.AC_DEFAULT_USER_PASSWORD` | 22 sampai 36 (TC-141) |
| Create-Only ({accCr}) | `createOnlyPrincipal_automated_qaTeam1@qwertysystem.net` (#4) | `Spectra.env.AC_CREATE_ONLY_PASSWORD` | 37 sampai 47 (TC-146) |
| Additional Approver Create ({accAa}) | `additionalApproverCreatePrincipal_automated_qaTeam1@qwertysystem.net` (#6) | `Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD` | 48 sampai 62 (TC-143), 78 sampai 107 (TC-144) |
| Distributor Manage hardware stock, Local Registration aktif ({accCakra}) | `distributorCakra_automated_qaTeam1@qwertysystem.net` (#10) | `Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD` | 63 sampai 73 (TC-145) |

- Nama env password selain `AC_TC_PASSWORD` mengikuti pola `AC_<ROLE>_PASSWORD` dan ditetapkan tim FE; nama pastinya tidak tertulis di TC (lihat Temuan untuk QA).
- Kelas harness: d (simulator reader USB, Pre-setup #25).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{accTc}` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |
| `{accDu}` | #2 | Akun Principal Default User | `Fixture.hardwareStock.account.p02.defaultUser.email`, `Fixture.hardwareStock.account.p02.defaultUser.fullName` |
| `{accCr}` | #4 | Akun Principal Create-Only | `Fixture.hardwareStock.account.p04.createOnly.email`, `Fixture.hardwareStock.account.p04.createOnly.fullName` |
| `{accAa}` | #6 | Akun Additional Approver dengan capability Create (satu-satunya anggota pool approver pada fixture #28) | `Fixture.hardwareStock.account.p06.additionalApproverCreate.email`, `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName` |
| `{accCakra}` | #10 | Akun Distributor Manage hardware stock dengan Local Registration aktif | `Fixture.hardwareStock.account.p10.distributorCakra.email`, `Fixture.hardwareStock.account.p10.distributorCakra.fullName` |
| `{entCakra}` | #10 | Nama entitas Distributor PT Cakra Distribusi (company akun accCakra) | `Fixture.hardwareStock.p10.entityName` |
| `{skuFx}` | #16, #27 (Tabel A baris 3) | kode SKU Smart Fixed Reader dengan 8 unit Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{skuRfd}` | #16, #17, #18 (Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 18 Available dan 7 In Use | `Fixture.hardwareStock.p16.a[4].sku` |
| `{skuBulk}` | #16, #24 (Tabel A baris 8) | kode SKU Smart Fixed Reader dengan 120 unit Available | `Fixture.hardwareStock.p16.a[8].sku` |
| `{snBulk09}` | #24 | Serial Number unit Available urutan ke-9 (menurut Serial Number) pada skuBulk | `Fixture.hardwareStock.p24.bulk[9].serialNumber` |
| `{snBulk10}` | #24 | Serial Number unit Available urutan ke-10 pada skuBulk | `Fixture.hardwareStock.p24.bulk[10].serialNumber` |
| `{snBulk11}` | #24 | Serial Number unit Available urutan ke-11 pada skuBulk | `Fixture.hardwareStock.p24.bulk[11].serialNumber` |

  Atribut alias: `.company` = nama perusahaan akun; `.registeredBy` = nama pendek pada kolom Registered By.

- Data Pre-setup (hanya dibaca): SKU `{skuRfd}` (Pre-setup #16); unit Available `{snBulk09}`, `{snBulk10}`, dan `{snBulk11}` pada SKU `{skuBulk}` (Pre-setup #24) sebagai unit yang dicocokkan TC-143, 145, dan 146; service driver mock (Pre-setup #25); fixture pool approver yang hanya berisi {accAa} (Pre-setup #28) untuk TC-144.
- Data Dinamis (suffix `{runId}-260`): unit Rejected milik spec pada SKU `{skuFx}` `SN-REJ140-{runId}-260` (TC-140) dan `SN-REJ141-{runId}-260` (TC-141) menggantikan unit Rejected Pre-setup #27 pada skuFx (yang berubah menjadi Available setelah TC-140); unit Available milik spec pada SKU `{skuBulk}` `SN-E3-{runId}-260` menggantikan `{snBulk09}` pada TC-144 (unit itu sudah dipakai TC-143 yang membuat Subject pending); perangkat simulasi `SN-ZEBRA-RFD40-100091-{runId}-260` (OK, TC-140).
- Kemampuan teknis (disediakan tim FE/BE): simulator USB Pre-setup #25; fixture BE yang membuat unit berstatus Rejected dan unit Available milik spec (mekanisme tidak didefinisikan di TC, PRD, atau LLD); fixture pool approver Pre-setup #28 dan pemulihannya; fixture BE yang membersihkan unit Available hasil Add Stock, unit Waiting for Approval, dan Subject Register Duplicate pending bersuffix `-260` serta Subject untuk `{snBulk09}`, `{snBulk10}`, `{snBulk11}` di hook `after`.
- State global: pool Additional Approver dibatasi satu anggota pada langkah 78 dan dipulihkan pada langkah 107 serta hook `after` walau spec gagal di tengah. Suite berjalan serial.
- Efek pada Pre-setup: antrean Approvals Tab Active menambah Subject pending (TC-143, 145, 146) dan hitungan SKU {skuRfd}; dipulihkan hook `after`.

## Test Steps

### TC-AC-ACHS-140: Requester Total Control (E2a)

1. Buka Approvals > Hardware Stock
2. Catat jumlah entri Tab Active (info "Showing ... of N entries") sebagai baseline Active
3. Klik Tab History
4. Catat jumlah entri Tab History sebagai baseline History
5. Buka Hardware > Stock lewat sidebar
6. Ketik Search `{skuRfd}`, tekan Enter
7. Klik `(⋯)` pada baris SKU `{skuRfd}`
8. Klik opsi `Add Stock`
9. Atur simulator: perangkat `SN-REJ140-{runId}-260` (Rejected, badge Waiting for Approval)
10. Klik `[Sync]`
11. Atur simulator: perangkat `SN-ZEBRA-RFD40-100091-{runId}-260` (OK)
12. Klik `[Sync]`
13. Klik `[Submit]`
14. Verifikasi dialog D-02 berjudul `Partial Register` tetap tampil
15. Klik `[Continue]`
16. Verifikasi toast sukses "Success, unit has been added to stock." (bukan "Success, unit has been sent for approval.")
17. Verifikasi kedua unit berstatus `Available` pada Tab Available
18. Buka Approvals > Hardware Stock
19. Verifikasi jumlah entri Tab Active sama dengan baseline langkah 2 (tidak ada Subject baru)
20. Klik Tab History
21. Verifikasi jumlah entri Tab History sama dengan baseline langkah 4 (tidak ada Subject baru)

### TC-AC-ACHS-141: Requester Default User

22. Logout, lalu login sebagai Default User {accDu} (`Spectra.env.AC_DEFAULT_USER_PASSWORD`)
23. Buka Hardware > Stock lewat sidebar
24. Ketik Search `{skuRfd}`, tekan Enter
25. Klik `(⋯)` pada baris SKU `{skuRfd}`
26. Klik opsi `Add Stock`
27. Atur simulator: perangkat `SN-REJ141-{runId}-260` (Rejected)
28. Klik `[Sync]`
29. Klik `[Submit]`
30. Klik `[Send]`
31. Verifikasi toast sukses "Success, unit has been added to stock."
32. Verifikasi unit `SN-REJ141-{runId}-260` langsung `Available` pada Tab Available
33. Buka Approvals > Hardware Stock
34. Verifikasi Tab Active menampilkan sedikitnya satu baris
35. Ketik Search `SN-REJ141-{runId}-260`, tekan Enter
36. Verifikasi tanpa Subject (bypass E2a): hasil Search menampilkan empty state `No results found`

### TC-AC-ACHS-146: Requester Create-Only

37. Logout, lalu login sebagai Create-Only {accCr} (`Spectra.env.AC_CREATE_ONLY_PASSWORD`)
38. Buka Hardware > Stock lewat sidebar
39. Ketik Search `{skuRfd}`, tekan Enter
40. Klik `(⋯)` pada baris SKU `{skuRfd}`
41. Klik opsi `Add Stock`
42. Atur simulator: perangkat `{snBulk11}`
43. Klik `[Sync]`
44. Klik `[Submit]`
45. Klik `[Send]`
46. Verifikasi toast sukses "Success, unit has been sent for approval."
47. Verifikasi unit `{snBulk11}` berstatus `Waiting for Approval` dan tidak ada bypass

### TC-AC-ACHS-143: Requester Additional Approver dengan anggota pool lain

48. Logout, lalu login sebagai Additional Approver {accAa} (`Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`)
49. Buka Hardware > Stock lewat sidebar
50. Ketik Search `{skuRfd}`, tekan Enter
51. Klik `(⋯)` pada baris SKU `{skuRfd}`
52. Klik opsi `Add Stock`
53. Atur simulator: perangkat `{snBulk09}`
54. Klik `[Sync]`
55. Klik `[Submit]`
56. Klik `[Send]`
57. Verifikasi toast sukses "Success, unit has been sent for approval."
58. Verifikasi unit `{snBulk09}` berstatus `Waiting for Approval`
59. Buka Approvals > Hardware Stock Tab Active
60. Verifikasi Tab Active menampilkan sedikitnya satu baris
61. Ketik Search `{snBulk09}`, tekan Enter
62. Verifikasi Subject permohonan tidak tampil pada Tab Active aktor ini: hasil Search menampilkan empty state `No results found`

### TC-AC-ACHS-145: Requester Distributor

63. Logout, lalu login sebagai Distributor {accCakra} (`Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD`)
64. Buka Hardware > Stock lewat sidebar
65. Ketik Search `{skuRfd}`, tekan Enter
66. Klik `(⋯)` pada baris SKU `{skuRfd}`
67. Klik opsi `Add Stock`
68. Atur simulator: perangkat `{snBulk10}`
69. Klik `[Sync]`
70. Klik `[Submit]`
71. Klik `[Send]`
72. Verifikasi toast sukses "Success, unit has been sent for approval."
73. Verifikasi unit `{snBulk10}` berstatus `Waiting for Approval` pada Tab Available aktor Distributor
74. Tunggu aksi selesai, lalu logout dan login sebagai Total Control {accTc} (`Spectra.env.AC_TC_PASSWORD`)
75. Buka Approvals > Hardware Stock Tab Active
76. Ketik Search `{snBulk10}`, tekan Enter
77. Verifikasi Subject Register Duplicate dengan Requested By `{entCakra} (Distributor)` tampil

### TC-AC-ACHS-144: E3 auto-approve, requester satu-satunya anggota pool

78. Atur pool approver entitas Principal hanya berisi {accAa} (Pre-setup #28)
79. Logout, lalu login sebagai Additional Approver {accAa} (`Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`)
80. Buka Hardware > Stock lewat sidebar
81. Ketik Search `{skuRfd}`, tekan Enter
82. Catat Total Registered baris SKU `{skuRfd}` sebagai baseline E3
83. Klik `(⋯)` pada baris SKU `{skuRfd}`
84. Klik opsi `Add Stock`
85. Atur simulator: perangkat `SN-E3-{runId}-260`
86. Klik `[Sync]`
87. Klik `[Submit]`
88. Klik `[Send]`
89. Verifikasi toast sukses "Success, unit has been added to stock."
90. Verifikasi unit `SN-E3-{runId}-260` langsung `Available` tanpa antrean pada Tab Available
91. Verifikasi Total Registered bertambah 1 dari baseline langkah 82
92. Buka Approvals > Hardware Stock Tab History
93. Ketik Search `SN-E3-{runId}-260`, tekan Enter
94. Verifikasi baris Approval `Approved` dengan Approver `System`
95. Buka Admin Console > Activity Log
96. Terapkan Filter Object = `Hardware`
97. Cari entri terbaru dengan Name `SN-E3-{runId}-260`
98. Verifikasi entri `Duplicate Approved` dengan Modified By `System`
99. Verifikasi entri memuat teks `Approved by system (no independent approver)`
100. Buka Hardware > Stock lewat sidebar
101. Ketik Search `{skuRfd}`, tekan Enter, lalu klik row action `Detail` pada baris SKU
102. Ketik Search `SN-E3-{runId}-260` pada Tab Available, tekan Enter
103. Klik `(⋯)` pada baris hasil
104. Klik `Hardware Log`
105. Verifikasi Hardware Log unit memuat `Hardware Approved by System`
106. Tutup popup Hardware Log
107. Pulihkan pool approver entitas Principal ke keadaan awal

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-140, 141, 143, 144, 145, 146). Tidak ada TC hanya-BE di spec ini.
- Spec ini melewati sekitar 35 langkah (107 langkah). Alasan: satu topik (tier requester pada Register Duplicate dari Sync) dengan satu kelas harness (d); tiap tier butuh akun berbeda sehingga memakai Step ganti akun eksplisit, dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras (bagian 3, pemisah beda akun kasus b). Role Matrix varian A per blok role karena langkah tiap tier berbeda.
- Urutan blok: TC-140, 141, 146, 143, 145 pada pool default, lalu TC-144 paling akhir karena membatasi pool approver (state global); pemulihan pada langkah 107 dan hook `after`. Urutan ini berbeda dari nomor TC dan mengelompokkan akun.
- Penggantian data: TC-140 dan 141 memakai unit Rejected milik spec (bukan unit Rejected Pre-setup #27 pada skuFx) karena setelah TC-140 unit itu berstatus Available sehingga TC-141 tidak lagi memenuhi preconditionnya; TC-144 memakai unit milik spec karena `{snBulk09}` sudah dipakai TC-143 (Subject pending). Langkah 9 dan seluruh seeding adalah penggantian yang dicatat di sini (S-04, S-15).
- Langkah penghubung (aksi tanpa `Verifikasi`): baseline (langkah 2, 4, 82), Search untuk menemukan baris (langkah 6, 24, 35, 39, 50, 61, 65, 76, 81, 93, 101 sampai 102), pengaturan simulator, pemicu pool (langkah 78, 107), login (Step ganti akun) dan `Tunggu aksi selesai` (langkah 74), dan penutupan popup (langkah 106).
- Langkah 95 sampai 106 menambah navigasi untuk Expected TC-144 butir d dan e (Activity Log dan Hardware Log) karena langkah TC-144 hanya sampai Tab Available dan Tab History. Jalur ke Hardware Log mengikuti TC-547 (Detail, Search SN, `(⋯)`, `Hardware Log`).
- Temuan untuk QA:
  - TC-140 Post Condition (Activity Log `Duplicate Approved` Modified By `Fixture.hardwareStock.account.p01.totalControl.fullName` (nama lengkap, pengecualian Activity Log R-14), kuota stok bertambah) dan TC-143 Post Condition (notifikasi ke approver pool lain), TC-145 Post Condition tidak punya langkah observasi dan tidak diasersi.
  - TC-143 dan TC-144 memakai Serial Number `{snBulk09}` yang sama; setelah TC-143 unit itu punya Subject pending sehingga TC-144 tidak dapat memakainya pada run yang sama.
  - TC-140 dan TC-141 memakai unit Rejected Pre-setup #27 pada skuFx (Rejected) yang berubah menjadi Available setelah TC-140.
  - TC-141 langkah 5 menyebut `[Send]` untuk unit yang bukan varian "semua baris Waiting for Approval" jelas; spec memakai `[Send]` sesuai langkah TC.
  - TC-146 tidak menyebut cara mengamati "tidak ada bypass" selain status `Waiting for Approval`.
  - Nama env password selain `AC_TC_PASSWORD` tidak tertulis di TC; disediakan tim FE.
  - Mekanisme membuat unit Rejected dan memulihkan pool approver tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
