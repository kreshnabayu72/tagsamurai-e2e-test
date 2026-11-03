---
id: TC-AC-ACHS-E2E-243-defense-in-depth-request-langsung-dan-markup-serial-number
title: "Defense-in-Depth: Request Langsung Ditolak dan Serial Number Berisi Markup"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-570
  - TC-AC-ACHS-571
  - TC-AC-ACHS-572
  - TC-AC-ACHS-573
  - TC-AC-ACHS-574
  - TC-AC-ACHS-575
  - TC-AC-ACHS-576
  - TC-AC-ACHS-577
  - TC-AC-ACHS-595
  - TC-AC-ACHS-596
  - TC-AC-ACHS-597
  - TC-AC-ACHS-598
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Ditolak dan Serial Number Berisi Markup

## Prerequisites

- Mode: FE+BE.
- Akun sesi UI: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server memakai token sesi API aktor (login API password, token tidak dihitung sebagai sesi web; dinyatakan di suite.md) untuk aktor berikut, dengan password memakai nama env konkret per aktor (`suite.md`):
  - Partner `Fixture.hardwareStock.account.p14.partner.email` (No 14; `Spectra.env.AC_PARTNER_PASSWORD`).
  - Read Only `Fixture.hardwareStock.account.p03.readOnly.email` (No 3; `Spectra.env.AC_READ_ONLY_PASSWORD`).
  - Create-Only `Fixture.hardwareStock.account.p04.createOnly.email` (No 4; `Spectra.env.AC_CREATE_ONLY_PASSWORD`).
  - Distributor `Fixture.hardwareStock.account.p10.distributorCakra.email` (No 10; `Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD`).
  - Additional Approver dengan capability Create `Fixture.hardwareStock.account.p06.additionalApproverCreate.email` (No 6; `Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`).
  - Total Control (Pre-setup No 1) sebagai pelaku request langsung memakai token sesi API aktor default suite.
  - Kemampuan membaca state data lewat fixture BE (unit, Subject, Hardware Log) untuk asersi state; endpoint tidak dikarang spec.
- Data Pre-setup (hanya dibaca, dipakai TC-572): unit SKU `{skuFx}` `{snMitraFx}` milik Distributor Pre-setup No 11 dan `{snCakraFx}` milik Distributor Pre-setup No 10 (No 27). Target request tulis atau hapus langsung TC-571, 573, 574, dan 575 memakai data milik spec (butir berikut); unit dan Subject Pre-setup No 17 dan 21 tidak dihapus atau di-approve spec ini (S-06). Jumlah entri Approvals Tab Active (No 21) dicatat sebagai baseline sebelum tiap request yang diasersi tidak menambah Subject (S-12).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `{snAvailOwn}` | milik spec (struktur #17 Tabel E baris N = 10) | Serial Number unit Available SKU Long Range milik Principal, target Delete TC-571 dan TC-573 | `SN-DIRA-{runId}-243` |
| `{snMitraOwn}` | milik spec | Serial Number unit Available SKU Smart Fixed Reader milik Distributor Pre-setup #11, target Delete TC-573 | `SN-DIRM-{runId}-243` |
| `{snWfaOwn}` | milik spec (struktur #17 Tabel E baris N = 28) | Serial Number unit Waiting for Approval SKU Long Range milik Distributor Pre-setup #12, target Delete TC-574 | `SN-DIRW-{runId}-243` |
| `{subjectWfa}` | milik spec (struktur #21 Tabel C baris 10) | Matched Identifier Subject Register Duplicate pending untuk `{snWfaOwn}` (sama dengan Serial Number unit itu), target Approve TC-575 | `SN-DIRW-{runId}-243` |
| `{snCakraFx}` | #27 | Serial Number unit Available pertama SKU Smart Fixed Reader milik Distributor Pre-setup #10 | `Fixture.hardwareStock.p27.fx[1].serialNumber` |
| `{snMitraFx}` | #27 | Serial Number unit Available SKU Smart Fixed Reader milik Distributor Pre-setup #11 | `Fixture.hardwareStock.p27.fx[6].serialNumber` |

- Data milik spec (S-06, R-08, S-12; suffix `{runId}-243`): unit Available milik Principal `{snAvailOwn}` pada SKU `{skuLong}` (target Delete TC-571 dan TC-573), unit Available milik Distributor Pre-setup No 11 `{snMitraOwn}` pada SKU `{skuFx}` (target Delete TC-573), serta unit Waiting for Approval `{snWfaOwn}` pada SKU `{skuLong}` beserta Subject Register Duplicate pending `{subjectWfa}` (target Delete TC-574 dan Approve TC-575; Existing Record Available, requester Distributor Pre-setup No 12, struktur No 17 Tabel E baris N = 28 dan No 21 Tabel C baris 10) di-seed hook `before` lewat sesi API aktor (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD). Hook `after` menghapus semua data bersuffix `-243` yang masih ada (idempotent, juga bila spec gagal di tengah).
- Data Dinamis: Serial Number request tulis bersuffix per run, yaitu `SN-DIRP-{runId}-243`, `SN-DIRR-{runId}-243`, `SN-DIR-{runId}-243-0001` sampai `SN-DIR-{runId}-243-0101`, `SN-DIRS-{runId}-243-0001` sampai `SN-DIRS-{runId}-243-0101`, `SN-DIRN-{runId}-243`, `SN-DIRH-{runId}-243`, dan `<b>SN-XSS{runId}-243</b>` (TC-577 membuat unit tersimpan pada SKU `{skuFx}`; dihapus lewat sesi API di hook `after`). Subject Register Duplicate milik Additional Approver Pre-setup No 6 bersuffix (TC-576) disediakan tim FE/BE sebagai seed spec (serupa Pre-setup No 21d) dan dihapus di hook `after`.
- State global yang diubah: System Limit `register_asset_bulk_limit` diubah ke 100 (Pre-setup No 26) untuk TC-595 dan TC-596 oleh pelaku yang disediakan tim FE/BE, dipulihkan ke 1.000 di langkah penghubung dan di hook `after`. Suite berjalan serial.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-570: Request langsung Partner ditolak di gate permission

1. Kirim request langsung daftar Stock List dengan token sesi API Partner
2. Verifikasi respons 403 Forbidden
3. Verifikasi respons tidak mengembalikan data stok (bukan hasil kosong)
4. Kirim request langsung Add Stock dengan Serial Number `SN-DIRP-{runId}-243` memakai token sesi API Partner
5. Verifikasi respons 403 Forbidden
6. Verifikasi state data: unit `SN-DIRP-{runId}-243` tidak tersimpan

### TC-AC-ACHS-571: Request tulis langsung Read Only ditolak

7. Kirim request langsung Add Stock dengan Serial Number `SN-DIRR-{runId}-243` memakai token sesi API Read Only
8. Verifikasi respons 403 Forbidden
9. Kirim request langsung Delete untuk unit Available `{snAvailOwn}` memakai token sesi API Read Only
10. Verifikasi respons 403 Forbidden
11. Verifikasi state data: unit `SN-DIRR-{runId}-243` tidak ada
12. Verifikasi state data: unit Available `{snAvailOwn}` tetap ada

### TC-AC-ACHS-572: Distributor tidak dapat membaca unit atau Hardware Log di luar row scope

13. Kirim request langsung detail Tab Available SKU `{skuFx}` memakai token sesi API Distributor (Pre-setup No 10), baca daftar
14. Verifikasi respons memuat sedikitnya satu unit
15. Verifikasi setiap unit pada daftar milik Distributor Pre-setup No 10
16. Kirim request langsung Hardware Log untuk unit milik Distributor Pre-setup No 11 `{snMitraFx}` memakai token sesi API Distributor (Pre-setup No 10)
17. Verifikasi request Hardware Log unit di luar scope ditolak

### TC-AC-ACHS-573: Distributor menghapus unit milik pihak lain ditolak

18. Kirim request langsung Delete untuk unit milik Distributor Pre-setup No 11 `{snMitraOwn}` memakai token sesi API Distributor (Pre-setup No 10)
19. Verifikasi request ditolak
20. Kirim request langsung Delete untuk unit milik Principal `{snAvailOwn}` memakai token sesi API Distributor (Pre-setup No 10)
21. Verifikasi request ditolak
22. Verifikasi state data: unit `{snMitraOwn}` tetap ada
23. Verifikasi state data: unit `{snAvailOwn}` tetap ada

### TC-AC-ACHS-574: Delete langsung unit Waiting for Approval ditolak

24. Kirim request langsung Delete untuk unit `{snWfaOwn}` memakai token sesi API Total Control
25. Verifikasi request ditolak karena unit bukan Available
26. Verifikasi state data: unit `{snWfaOwn}` tetap ada
27. Verifikasi state data: Subject Register Duplicate `{subjectWfa}` tetap ada

### TC-AC-ACHS-575: Approve langsung aktor non-approver ditolak

28. Kirim request langsung Approve untuk Subject Register Duplicate `{subjectWfa}` memakai token sesi API Create-Only
29. Verifikasi respons 403 Forbidden
30. Kirim request langsung Approve untuk Subject yang sama memakai token sesi API Read Only
31. Verifikasi respons 403 Forbidden
32. Kirim request langsung Approve untuk Subject yang sama memakai token sesi API Distributor (Pre-setup No 10)
33. Verifikasi respons 403 Forbidden
34. Verifikasi state data: Subject `{subjectWfa}` tetap pending
35. Verifikasi state data: unit `{snWfaOwn}` tetap Waiting for Approval

### TC-AC-ACHS-576: Requester Additional Approver menyetujui permohonannya sendiri ditolak

36. Kirim request langsung Approve untuk Subject Register Duplicate milik sendiri (seed spec, pool memiliki anggota lain) memakai token sesi API Additional Approver (Pre-setup No 6)
37. Verifikasi respons 403 Forbidden
38. Verifikasi state data: Subject tetap pending
39. Verifikasi state data: tidak ada entri keputusan untuk Subject itu

### TC-AC-ACHS-577: Serial Number berisi markup dirender sebagai teks literal

40. Klik `(⋯)` pada baris `{skuFx}`, klik opsi `Add Stock`
41. Ketik `<b>SN-XSS{runId}-243</b>` di textarea Serial Numbers, klik `[Submit]`
42. Tunggu aksi selesai (halaman kembali ke Stock Detail Tab Available)
43. Ketik Search `<b>`, tekan Enter
44. Verifikasi Tab Available menampilkan baris dengan Serial Number literal `<b>SN-XSS{runId}-243</b>` tanpa format tebal
45. Verifikasi Search `<b>` mencocokkan baris itu sebagai teks biasa
46. Klik icon `[Event Log]`, klik Detail pada sesi Add Stock terbaru
47. Verifikasi popup Detail Event Log menampilkan Serial Number literal `<b>SN-XSS{runId}-243</b>` tanpa format tebal
48. Tutup popup dengan `Esc`
49. Buka Activity Log, cari entri Add Stock dengan Search `SN-XSS{runId}-243`
50. Verifikasi Activity Log menampilkan Serial Number literal `<b>SN-XSS{runId}-243</b>` tanpa format tebal

### TC-AC-ACHS-595: Request langsung Add Stock manual di atas limit ditolak seluruhnya

51. Ubah System Limit `register_asset_bulk_limit` menjadi 100; tunggu aksi selesai
52. Kirim request langsung Add Stock manual untuk SKU `{skuFx}` dengan 101 Serial Number `SN-DIR-{runId}-243-0001` sampai `SN-DIR-{runId}-243-0101` memakai token sesi API Total Control
53. Verifikasi respons menolak seluruh request dengan error validasi V-03
54. Verifikasi tidak ada baris yang dipotong atau diterima sebagian
55. Klik menu Hardware > Stock di sidebar
56. Klik `(⋯)` pada baris `{skuFx}`, klik row action `Detail`
57. Ketik Search `SN-DIR-{runId}`, tekan Enter
58. Verifikasi empty state `No results found` (tidak ada unit `SN-DIR-{runId}-*` tersimpan di Tab Available)

### TC-AC-ACHS-596: Request langsung Submit Add Stock Sync di atas limit ditolak seluruhnya

59. Klik menu Approvals > Hardware Stock di sidebar, lalu catat info pagination Tab Active (jumlah entri) sebagai baseline
60. Kirim request langsung Submit Add Stock Sync untuk SKU `{skuLong}` dengan 101 unit `SN-DIRS-{runId}-243-0001` sampai `SN-DIRS-{runId}-243-0101` beserta nilai Min/Max/Current Power memakai token sesi API Total Control
61. Verifikasi respons menolak seluruh request dengan error validasi V-18
62. Klik segmen breadcrumb `Stock`
63. Klik `(⋯)` pada baris `{skuLong}`, klik row action `Detail`
64. Ketik Search `SN-DIRS-{runId}`, tekan Enter
65. Verifikasi empty state `No results found` (tidak ada unit `SN-DIRS-{runId}-*` tersimpan di Tab Available)
66. Klik menu Approvals > Hardware Stock di sidebar
67. Verifikasi jumlah entri pada info pagination Tab Active sama dengan baseline langkah 59 (tidak ada Subject Register Duplicate baru)

### TC-AC-ACHS-597: Request langsung format Sync untuk SKU non-Handheld Reader ditolak

68. Kirim request langsung Submit Add Stock format Sync (Serial Number `SN-DIRN-{runId}-243` beserta nilai Min/Max/Current Power) untuk SKU `{skuFx}` memakai token sesi API Total Control
69. Verifikasi request ditolak karena format Sync tidak berlaku untuk SKU non-Handheld Reader
70. Klik menu Hardware > Stock di sidebar
71. Klik `(⋯)` pada baris `{skuFx}`, klik row action `Detail`
72. Ketik Search `SN-DIRN-{runId}`, tekan Enter
73. Verifikasi empty state `No results found` (unit `SN-DIRN-{runId}-243` tidak tersimpan)

### TC-AC-ACHS-598: Request langsung Add Stock manual untuk SKU Handheld Reader tidak menyimpan unit

74. Klik menu Approvals > Hardware Stock di sidebar, lalu catat info pagination Tab Active (jumlah entri) sebagai baseline
75. Kirim request langsung Add Stock manual (Serial Number `SN-DIRH-{runId}-243` tanpa data Sync) untuk SKU `{skuLong}` memakai token sesi API Total Control
76. Verifikasi request ditolak karena Add Stock Handheld Reader hanya lewat `[Sync]`
77. Klik segmen breadcrumb `Stock`
78. Klik `(⋯)` pada baris `{skuLong}`, klik row action `Detail`
79. Ketik Search `SN-DIRH-{runId}`, tekan Enter
80. Verifikasi empty state `No results found` (unit `SN-DIRH-{runId}-243` tidak tersimpan)
81. Klik menu Approvals > Hardware Stock di sidebar
82. Verifikasi jumlah entri pada info pagination Tab Active sama dengan baseline langkah 74 (tidak ada Subject Register Duplicate baru)
83. Pulihkan System Limit `register_asset_bulk_limit` ke 1.000

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-570, 571, 572, 573, 574, 575, 576, 577, 595, 596, 597, 598). Tidak ada TC hanya-BE di spec ini.
- K-1: TC-570 sampai TC-576 dan TC-595 sampai TC-598 adalah request langsung ke server (kelas a); Expected berupa respons API dan state data lewat fixture BE. Tidak ada `tc-hardware-stock-backend.md` untuk dicocokkan, sehingga semua TC masuk spec dan Expected ditulis sebatas yang tertulis di TC; perilaku FE pada request langsung tidak disalin (bagian 8b butir 1). Hanya status respons dan state data yang diasersi pada langkah request langsung; langkah UI (Search, Approvals) setelah request pada TC-595 sampai TC-598 adalah observasi state yang disebut Expected TC. TC-577 (injeksi markup) berjalan lewat UI karena objek ujinya perenderan teks.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 51 (mengubah System Limit sebelum TC-595, state global) dan langkah terakhir (memulihkan System Limit, juga dicadangkan di hook `after`), klik menu sidebar dan breadcrumb untuk berpindah surface, Search `SN-DIR...` untuk menemukan atau memastikan tidak adanya unit target (R-16), dan buka Detail Event Log pada TC-577.
- Spec di atas smell 35 langkah (83 langkah). Alasan: semua blok satu kelas harness (defense-in-depth, kelas a) dan berdiri sendiri, kegagalan satu request tidak membuat blok lain kehilangan makna, dan memecahnya per aksi menambah login, hook, dan cleanup (bagian 3 konvensi: kelas ringan satu spec per kelas per modul).
- S-05: Expected c TC-595 dan Expected c TC-596 ("Tidak ada sesi Event Log baru") adalah asersi absence log atas request langsung yang ditolak; asersi itu milik spec absence (kelas g) dan tidak diasersi di spec ini, tetapi di spec 281 (kedua TC juga ada di `sourceTc` spec 281 dengan pemicu request ditolak, baseline Event Log sendiri, dan anchor positif). Id TC tetap di `sourceTc` spec ini untuk Expected a dan b.
- Blok TC-577 (sukses) berada di tengah mengikuti urutan TC sumber; unit yang dibuatnya pada SKU `{skuFx}` tidak dibaca blok lain (blok lain mencari Serial Number bersuffix sendiri) dan dihapus hook `after`, sehingga tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-572 Expected b ("request Hardware Log unit di luar scope ditolak") tidak menyebut kode status; spec mengasersi penolakan tanpa kode. TC-573, 574, dan 597 sama (tanpa kode status).
  - TC-575 langkah 2 ("Ulangi dengan token Read Only dan token Distributor") tidak menyebut Subject; spec memakai Subject `{subjectWfa}`.
  - TC-576 mensyaratkan Subject Register Duplicate milik requester Additional Approver dengan pool berisi anggota lain tanpa menyebut sumbernya; spec memakai seed bersuffix spec (serupa Pre-setup No 21d) yang disediakan tim FE/BE.
  - TC-577 tidak menyebut kolom Activity Log tempat Serial Number tampil, tidak menyebut cara membuka Detail Event Log, dan memakai literal `<b>SN-XSS</b>` tanpa suffix; spec memakai suffix `{runId}` (S-12) dan Search `SN-XSS{runId}-243` di Activity Log.
  - TC-595 dan TC-596 Precondition menyebut Register Asset Bulk Limit = 100 (Pre-setup No 26, default 1.000); pelaku yang mengubah limit tidak disebut TC, sehingga disediakan tim FE/BE.
  - Population Stock tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup (`{snCakraFx}`, `{snMitraFx}`; target tulis memakai `{snAvailOwn}`, `{snMitraOwn}`, `{snWfaOwn}`, `{subjectWfa}` milik spec) sehingga tidak memerlukan pengecualian S-12. Serial Number `SN-DIR*`, `SN-XSS*` dan markup `<b>` adalah data buatan spec.
  - Mekanisme token sesi API aktor, klien HTTP, dan pembaca state BE tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan.
