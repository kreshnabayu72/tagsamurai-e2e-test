---
id: TC-AC-ACHS-E2E-283-lintas-modul-device-allocation-dan-asersi-negatif
title: "Lintas Modul: Device Allocation dan Asersi Negatif"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-563
  - TC-AC-ACHS-583
  - TC-AC-ACHS-584
coverage:
  web: automated
---

# Lintas Modul: Device Allocation dan Asersi Negatif

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor pertama: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua (TC-584 butir b): Client penerima notifikasi Rejected (akun Client disediakan tim FE; tidak ada di Pre-setup TC). Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22 dan #27; suite serial `parallel: false` (lihat suite.md).
- Pelaku lintas modul lewat sesi API aktor (kemampuan disediakan tim BE/FE; tidak ada endpoint di spec): Principal yang menjalankan alokasi kuota Category Smart Fixed Reader ke Distributor di Device Allocation (jumlah alokasi tidak ditentukan TC; dipilih tim FE) untuk TC-563; Approver Principal yang menolak (Reject) Subject Activation Collision `SN-E2E-{runId}-283A` untuk TC-584 (sumber TC-184). Sumber TC modul asal Device Allocation: tidak disebut TC.
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai read-only: SKU `Fixture.hardwareStock.p16.a[3].sku` (Pre-setup #16, #27), SKU `Fixture.hardwareStock.p16.a[4].sku` dengan Total Registered 25 = Available 18 + In Use 7, unit Waiting for Approval `Fixture.hardwareStock.p17.e[28].deviceName`, dan unit Rejected `Fixture.hardwareStock.p21.c[6].matchedIdentifier` (Pre-setup #17).
- Data milik spec (S-06, S-12; target aksi tulis, di-seed hook `before` lewat sesi API aktor dengan struktur yang sama dengan Subject Pre-setup #21 Tabel C baris ke-9 yang digantikannya, disediakan tim BE/FE tanpa endpoint karangan; kunci fixture-nya belum ada): Subject Activation Collision pending `SN-E2E-{runId}-283A` untuk Fixed Reader tanpa SKU (Existing Record Active, requester Client `Fixture.hardwareStock.p23.client[6].name`) yang ditolak pada TC-584 (sumber TC-184). Data Pre-setup #16 sampai #22 dan #27 tidak diubah spec ini.
- State global yang diubah: alokasi kuota Category Smart Fixed Reader di Device Allocation (TC-563, langkah 27). Pemulihan: hook `after` membatalkan alokasi milik spec secara idempotent; kemampuan pembatalan dan pemulihan kuota ke keadaan awal disediakan tim FE/BE dan belum ada.
- Cleanup (R-08): hook `after` menghapus secara idempotent Subject milik spec `SN-E2E-{runId}-283A` dan membatalkan alokasi kuota di atas.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `skuSfr` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available (5 milik Distributor #10, 3 milik Distributor #11) | `Fixture.hardwareStock.p16.a[3].sku` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `unitWfa` | #17 (Tabel E baris N = 28) | Device Name unit Waiting for Approval pada `skuLong` | `Fixture.hardwareStock.p17.e[28].deviceName` |
| `snRej` | #17, #21 (Tabel C baris ke-6) | Serial Number unit Rejected pada `skuLong`; sekaligus Matched Identifier Subject Register Duplicate pending pada `skuShort` (Existing Record Rejected) | `Fixture.hardwareStock.p21.c[6].matchedIdentifier` |
| `idAcFixed` | data milik spec (struktur #21 Tabel C baris ke-9) | Matched Identifier Subject Activation Collision pending milik spec untuk Fixed Reader tanpa SKU (Existing Record Active, requester Client ke-6) | `SN-E2E-{runId}-283A` |
| `client6` | #23 (urutan penulisan daftar Client, butir ke-6) | Nama Client ke-6 pada daftar Client Pre-setup #23 | `Fixture.hardwareStock.p23.client[6].name` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |


## Test Steps

### TC-AC-ACHS-583: Unit Waiting for Approval dan Rejected tidak dihitung

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Klik Tab `Available`
3. Catat Summary bar (Total Registered, Available, In Use)
4. Verifikasi Total Registered `25` sama dengan Available `18` ditambah In Use `7`
5. Verifikasi baris Waiting for Approval `Fixture.hardwareStock.p17.e[28].deviceName` ada di Tab Available
6. Verifikasi baris Waiting for Approval tidak dihitung dalam Total Registered
7. Cari unit Rejected `Fixture.hardwareStock.p21.c[6].matchedIdentifier` pada Tab Available dan Tab In Use: ketik Search `Fixture.hardwareStock.p21.c[6].matchedIdentifier`, tekan Enter
8. Verifikasi Tab Available menampilkan `No results found`
9. Klik Tab `In Use`
10. Verifikasi Tab In Use menampilkan `No results found` (unit Rejected tidak ada di mana pun)
11. Klik `(←)` pada kotak Search

### TC-AC-ACHS-584: Asersi negatif Must NOT lintas modul

12. Klik Tab `Available`
13. Verifikasi sedikitnya satu baris unit tampil di Tab Available (pembanding)

Untuk setiap baris unit pada halaman pertama Tab Available, lakukan langkah 14 sampai 15:

14. Klik `(⋯)` pada baris unit
15. Verifikasi row action unit tidak memuat Recall, Edit, atau ubah nilai daya (row action `Hardware Log` tampil sebagai pembanding)

16. Klik Tab `In Use`
17. Verifikasi sedikitnya satu baris unit tampil di Tab In Use (pembanding)

Untuk setiap baris unit pada halaman pertama Tab In Use, lakukan langkah 14 sampai 15:

18. Approver Principal menolak (Reject) Subject Activation Collision `SN-E2E-{runId}-283A` dengan Approval Note `Alasan uji` lewat sesi API hingga keputusan tersimpan; tunggu aksi selesai
19. Logout, lalu login sebagai Client pemohon Subject itu (`Fixture.hardwareStock.p23.client[6].name`); tunggu aksi selesai
20. Buka panel Notifikasi Client
21. Verifikasi notifikasi Rejected tampil
22. Verifikasi notifikasi Rejected bersifat umum dan tidak memuat nama Client atau langganan lain
23. Logout, lalu login sebagai Total Control `Fixture.hardwareStock.account.p01.totalControl.fullName`; tunggu aksi selesai

### TC-AC-ACHS-563: Alokasi kuota di Device Allocation

24. Buka Hardware > Stock
25. Catat baris SKU `Fixture.hardwareStock.p16.a[3].sku` (Total Registered, Available, In Use)
26. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[3].sku`, lalu catat Summary bar
27. Principal menjalankan alokasi kuota Category Smart Fixed Reader ke Distributor di Device Allocation lewat sesi API hingga tersimpan; tunggu aksi selesai
28. Muat ulang halaman (F5)
29. Verifikasi Summary bar Stock Detail: Total Registered, Available, In Use tidak berubah dari nilai langkah 26
30. Verifikasi tidak ada banner kuota
31. Verifikasi tidak ada kolom Allocated
32. Verifikasi unit pada Tab Available tetap berstatus `Available`
33. Klik segmen breadcrumb `Stock`
34. Verifikasi Stock List baris SKU `Fixture.hardwareStock.p16.a[3].sku`: Total Registered, Available, In Use tidak berubah dari nilai langkah 25

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-563, 583, 584). Tidak ada TC hanya-BE di spec ini.
- Konfirmasi keyword Search terhadap nilai penuh Pre-setup (#8): Search `Fixture.hardwareStock.p21.c[6].matchedIdentifier` memakai Matched Identifier penuh Tabel C baris ke-6 (Pre-setup #21), yang sama dengan Serial Number unit Rejected pada Pre-setup #17. Tidak ada perbedaan.
- Urutan menyimpang dari TC: TC-583 di awal (baca murni), TC-584 sebelum TC-563 supaya ganti akun ke Client dan kembali ke Total Control terjadi satu kali; TC-563 mengubah state kuota dan di akhir.
- Langkah 14 sampai 15 diulang dua kali: untuk setiap baris unit pada halaman pertama Tab Available (sebelum langkah 16) dan Tab In Use (sesudah langkah 17) (parameter: baris pada tabel yang tampil); ambang langkah dihitung dengan ekspansi (butir 8b nomor 7). Dengan ekspansi spec ini melebihi sekitar 35 langkah; alasannya: tiga TC lintas modul satu dataset SKU RFD40 dan SFR, dan penambahan langkah hanya berasal dari perulangan baris yang sama (maksimum 10 baris per tab).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 9, 12, 16, 24, 26, 33 (navigasi dan pindah tab; langkah TC "Pastikan Tab `Available` aktif" ditulis `Klik Tab` pada langkah 2, `[KEPUTUSAN 2026-11-02]`), 3 dan 25 (baseline), 7 (Search untuk menemukan baris target, R-16), 11 (mengosongkan Search lewat `(←)`), 18 dan 27 (pelaku lewat sesi API, "Tunggu aksi selesai", R-20), 19 dan 23 (ganti akun), 20 (membuka panel Notifikasi), 28 (memuat ulang).
- Anchor positif asersi absence (butir 8b nomor 2): langkah 5 untuk langkah 8 dan 10 (`No results found` hasil Search); langkah 13 untuk langkah 15 (Tab Available) dan langkah 17 untuk langkah 15 (Tab In Use); langkah 21 untuk langkah 22.
- Temuan untuk QA:
  - TC-563 tidak menyebut jumlah alokasi, pelaku, maupun sumber TC modul Device Allocation; spec memakai pelaku Principal lewat sesi API dengan jumlah ditentukan tim FE.
  - TC-584 butir b menyebut notifikasi Rejected ke Client tanpa menyebut akun Client dan surface notifikasi Client; spec memakai panel Notifikasi Client dan Subject `SN-E2E-{runId}-283A` (pemohon `Fixture.hardwareStock.p23.client[6].name`, Pre-setup #21 Tabel C) sebagai sumber penolakan (TC-184).
  - TC-583 butir c ("unit Rejected tidak ada di mana pun") tidak menyebut Serial Number unit Rejected; spec memakai `Fixture.hardwareStock.p21.c[6].matchedIdentifier` dari Pre-setup #17.
  - TC-584 menyebut "seluruh row action Tab Available dan Tab In Use"; spec membatasi pada baris halaman pertama.
  - Seeding Subject milik spec (`SN-E2E-{runId}-283A`) dan pembatalan alokasi kuota TC-563 di hook `after` tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim BE/FE dan kunci fixture-nya belum ada.
