---
id: TC-AC-ACHS-E2E-262-sync-klik-ganda-dan-badge-basi-akibat-sesi-lain
title: "Sync: Klik Ganda Submit dan Badge Basi Akibat Sesi Lain"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-151
  - TC-AC-ACHS-154
  - TC-AC-ACHS-155
coverage:
  web: automated
---

# Sync: Klik Ganda Submit dan Badge Basi Akibat Sesi Lain

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List untuk akun aktor suite, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`). Flag Guided Tooltip halaman Stock List akun {accAa} dan halaman Approvals Hardware Stock akun {accObs} disetel true di hook `before` spec ini dan dipulihkan di hook `after`.
- Login di hook `before` spec ini: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`); halaman Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua dan sesi pengamat login lewat Step ganti akun (langkah 14 dan 40); hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji: Total Control (TC-151, langkah 1 sampai 13); Additional Approver dengan capability Create, {accAa}, `Fixture.hardwareStock.account.p06.additionalApproverCreate.email` (Pre-setup #6; `Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`) untuk TC-154 dan TC-155 sebagai requester Sync (langkah 14 sampai 39); Total Control lain, {accObs}, anggota pool approver (Pre-setup #2; `Spectra.env.AC_DEFAULT_USER_PASSWORD`) untuk sesi pengamat Approvals TC-154 dan TC-155 (langkah 40 sampai 51).
- Kelas harness: d (simulator reader USB, Pre-setup #25).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{accAa}` | #6 | Akun Additional Approver dengan capability Create; requester Sync TC-154 dan TC-155, bukan pengamat Approvals (Subject permohonannya tidak tampil di inbox Tab Active-nya, PRD §9.2 "3.2a") | `Fixture.hardwareStock.account.p06.additionalApproverCreate.email`, `Fixture.hardwareStock.account.p06.additionalApproverCreate.fullName` |
| `{accObs}` | #2 | Akun Total Control lain (tier Total Control permanen), anggota pool approver; sesi pengamat Approvals TC-154 dan TC-155 | `Fixture.hardwareStock.account.p02.defaultUser.email`, `Fixture.hardwareStock.account.p02.defaultUser.fullName` |
| `{skuRfd}` | #16, #17, #18 (Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 18 Available dan 7 In Use | `Fixture.hardwareStock.p16.a[4].sku` |
| `{skuBulk}` | #16, #24 (Tabel A baris 8) | kode SKU Smart Fixed Reader dengan 120 unit Available | `Fixture.hardwareStock.p16.a[8].sku` |

- Data Pre-setup: SKU `{skuRfd}` (Pre-setup #16); service driver mock (Pre-setup #25).
- Data Dinamis (suffix `{runId}-262`): perangkat simulasi `SN-ZEBRA-RFD40-100121-{runId}-262` (TC-151, disimpan), `SN-ZEBRA-RFD40-100131-{runId}-262` (TC-154, menjadi Waiting for Approval), `SN-ZEBRA-RFD40-100141-{runId}-262` (TC-155, disimpan), serta dua unit Available milik spec pada SKU lain `{skuBulk}`: `SN-STALE154-{runId}-262` (dibuat sesi lain, TC-154) dan `SN-STALE155-{runId}-262` (dibuat dan dihapus sesi lain, TC-155). Unit milik spec menggantikan unit Pre-setup #24 (Serial Number ke-15 SKU 120 unit) supaya unit Pre-setup tidak dihapus (S-06).
- Kemampuan teknis (disediakan tim FE/BE): simulator USB Pre-setup #25; penahanan respons Submit (langkah 6, hanya pemicu state UI, dilepas pada langkah 11); sesi API aktor yang membuat dan menghapus unit (padanan "sesi lain", endpoint tidak disebut TC, PRD, atau LLD, S-13); fixture BE yang membersihkan unit, Subject Register Duplicate pending, dan unit Waiting for Approval bersuffix `-262` di hook `after` (mekanismenya tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA).
- Efek pada Pre-setup: hitungan baris SKU {skuRfd} dan antrean Approvals Tab Active berubah selama spec berjalan; dipulihkan hook `after`.

## Test Steps

### TC-AC-ACHS-151: Klik ganda cepat pada [Submit] Sync

1. Atur simulator: perangkat `SN-ZEBRA-RFD40-100121-{runId}-262` terhubung
2. Ketik Search `{skuRfd}`, tekan Enter
3. Klik `(⋯)` pada baris SKU `{skuRfd}`
4. Klik opsi `Add Stock`
5. Klik `[Sync]`
6. Pasang penahanan respons Submit
7. Klik `[Submit]` dua kali cepat
8. Verifikasi `[Submit]` menampilkan spinner
9. Verifikasi `[Submit]` disabled
10. Verifikasi `[Sync]` dan `(⋯)` disabled selama request
11. Tunggu toast lama hilang otomatis, lalu lepas penahanan respons Submit
12. Verifikasi hanya satu toast sukses tampil
13. Verifikasi hanya satu unit `SN-ZEBRA-RFD40-100121-{runId}-262` tersimpan di Tab Available

### TC-AC-ACHS-154: Badge Sync OK tetapi SN didaftarkan sesi lain

14. Logout, lalu login sebagai Additional Approver {accAa} (`Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`)
15. Buka Hardware > Stock lewat sidebar
16. Atur simulator: perangkat `SN-ZEBRA-RFD40-100131-{runId}-262` terhubung
17. Ketik Search `{skuRfd}`, tekan Enter
18. Klik `(⋯)` pada baris SKU `{skuRfd}`
19. Klik opsi `Add Stock`
20. Klik `[Sync]`
21. Verifikasi Status baris `SN-ZEBRA-RFD40-100131-{runId}-262` `OK`
22. Daftarkan `SN-ZEBRA-RFD40-100131-{runId}-262` pada SKU `{skuBulk}` lewat sesi API aktor hingga unit tersimpan
23. Klik `[Submit]`
24. Verifikasi dialog D-02 tidak tampil (badge masih OK)
25. Verifikasi toast sukses "Success, unit has been sent for approval."
26. Verifikasi unit `SN-ZEBRA-RFD40-100131-{runId}-262` tampil `Waiting for Approval`

### TC-AC-ACHS-155: Badge Waiting for Approval tetapi unit rujukan dihapus

27. Buat unit Available `SN-STALE155-{runId}-262` pada SKU `{skuBulk}` lewat sesi API aktor hingga unit tersimpan
28. Atur simulator: perangkat `SN-STALE155-{runId}-262` terhubung
29. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuRfd}` (form baru)
30. Klik `[Sync]`
31. Verifikasi Status baris `SN-STALE155-{runId}-262` `Waiting for Approval`
32. Atur simulator: perangkat `SN-ZEBRA-RFD40-100141-{runId}-262` terhubung
33. Klik `[Sync]`
34. Hapus unit `SN-STALE155-{runId}-262` lewat sesi API aktor hingga unit terhapus
35. Klik `[Submit]`
36. Verifikasi dialog D-02 tetap tampil karena badge Sync
37. Klik `[Continue]`
38. Verifikasi toast sukses "Success, unit has been added to stock."
39. Verifikasi kedua unit `SN-STALE155-{runId}-262` dan `SN-ZEBRA-RFD40-100141-{runId}-262` berstatus `Available`
### TC-AC-ACHS-154 dan TC-AC-ACHS-155: Pengamatan Approvals oleh sesi pengamat

40. Logout, lalu login sebagai Total Control lain (sesi pengamat, anggota pool approver) `{accObs}` (`Spectra.env.AC_DEFAULT_USER_PASSWORD`); tunggu aksi selesai
41. Buka Approvals > Hardware Stock
42. Klik Tab `Active`
43. Ketik Search `SN-ZEBRA-RFD40-100131-{runId}-262`, tekan Enter
44. Verifikasi Subject pending `SN-ZEBRA-RFD40-100131-{runId}-262` tampil di Tab Active sesi pengamat
45. Klik `(←)` pada kotak Search
46. Ketik Search `SN-STALE155-{runId}-262`, tekan Enter
47. Verifikasi empty state `No results found` (tidak ada Subject baru untuk `SN-STALE155-{runId}-262`)
48. Klik `(←)` pada kotak Search
49. Ketik Search `SN-ZEBRA-RFD40-100141-{runId}-262`, tekan Enter
50. Verifikasi empty state `No results found` (tidak ada Subject baru untuk `SN-ZEBRA-RFD40-100141-{runId}-262`)
51. Klik `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-151, 154, 155). Tidak ada TC hanya-BE di spec ini.
- Spec memuat Step ganti akun eksplisit (langkah 14 dan 40) dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah beda akun kasus b); kelas harness tunggal (d). Pelaku "sesi lain" memakai sesi API aktor, tanpa `P-2`. Kata "Manual Only" pada kolom Automation TC-154 dan TC-155 bukan alasan mengeluarkan TC.
- Spec di atas smell 35 langkah (51 langkah). Alasan: tiga TC satu kelas (Sync, race klik ganda dan badge basi) dengan satu SKU dan satu pelaku sesi lain; dipecah menggandakan simulator dan Step ganti akun.
- Langkah 6 (penahanan respons) bukan langkah TC-151; ditambahkan sebagai langkah penghubung supaya spinner teramati (S-03), dilepas pada langkah 11.
- TC-154 langkah 5 menyebut SKU lain tanpa nama; spec memakai `{skuBulk}`. TC-155 memakai unit Pre-setup #24 (Serial Number ke-15 SKU 120 unit); spec memakai unit milik spec `SN-STALE155-{runId}-262` supaya Pre-setup tidak terhapus (S-06). Langkah 27 sampai 28 adalah seeding yang dinyatakan di Prerequisites.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search (langkah 2, 17, 43, 46, 49), pengaturan simulator, `[Add Stock]` toolbar (langkah 29), pembuatan atau penghapusan unit lewat sesi API (langkah 22, 27, 34), pelepasan penahanan respons dan menunggu toast (langkah 11), logout dan login ganti akun serta navigasi (langkah 14, 15, 40), `[Continue]` (langkah 37), membuka Approvals dan Tab `Active` untuk observasi Subject (langkah 41, 42), dan menutup Search lewat `(←)` (langkah 45, 48, 51). Langkah 26 menyatakan unit `Waiting for Approval`; Subject pending TC-154 diamati sesi pengamat di langkah 43 sampai 44.
- Langkah 40 sampai 51 (sesi pengamat Total Control; Tab `Active` sebagai langkah penghubung S-03, bukan `Verifikasi` tab aktif) mengamati Expected c TC-154 (langkah 44) dan klausa "tidak ada Subject baru" TC-155 butir c (langkah 47 dan 50): Matched Identifier Subject yang dapat muncul adalah Serial Number unit stale dan perangkat OK; langkah 44 (Subject TC-154 tampil di Tab `Active` pengamat yang sama) menjadi anchor positif sebelum absence (butir 8b nomor 2). Pengamat bukan {accAa} karena Subject requester Additional Approver tidak tampil di inbox Tab `Active`-nya.
- Temuan untuk QA:
  - TC-154/155 Precondition e menyebut sesi pengamat "Total Control lain (Bagas Arunika)" tanpa kunci fixture; spec memakai Pre-setup #2 (`Fixture.hardwareStock.account.p02.defaultUser`, tier Total Control permanen) dan mengasumsikan akun itu anggota pool approver fixture #28; flag Guided Tooltip halaman Approvals Hardware Stock akun pengamat disetel hook `before` spec ini. TC tidak menyatakan keanggotaan pool itu.
  - Penghapusan unit Pre-setup oleh TC-155 mengubah Pre-setup #24; spec memakai unit milik spec.
  - TC-155 butir c ("tidak ada Subject baru") menyebut `SN-BULK-IX6-000015` dan `SN-ZEBRA-RFD40-100141`; spec mencari `SN-STALE155-{runId}-262` (pengganti unit milik spec) dan `SN-ZEBRA-RFD40-100141-{runId}-262`.
  - TC-151, 154, 155 tidak memuat Post Condition.
