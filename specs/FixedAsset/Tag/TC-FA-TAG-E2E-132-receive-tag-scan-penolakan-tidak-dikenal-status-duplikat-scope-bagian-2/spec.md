---
id: TC-FA-TAG-E2E-132-receive-tag-scan-penolakan-tidak-dikenal-status-duplikat-scope-bagian-2
title: "Receive TAG: penolakan Tag QR belum terpasang, Supply Asset, dan User TAG, lalu Tag valid tetap diproses"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-549
  - TC-FA-TAG-1444
  - TC-FA-TAG-1474
  - TC-FA-TAG-1475
coverage:
  web: automated
---

# Receive TAG: penolakan Tag QR belum terpasang, Supply Asset, dan User TAG, lalu Tag valid tetap diproses

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada):
  - Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
  - Kode `QR-00300` sudah dicetak lewat Print QR (berstatus Available) dan belum terpasang pada aset mana pun.
  - Tag `SA-00020` terdaftar di produk Supply Asset (stok dan SKU).
  - Tag `UT-00010` adalah User TAG milik Global Settings > User.
  - Tag `RF-00500` berstatus Available di Global.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); pemulihan status Tag ke To be Returned lewat fixture backend.
- State global yang dipulihkan: TC-549 menerima `RF-00071` (menjadi Available di registri Global dan menambah entri Event Log To Be Returned serta TAG Log Global yang tidak dapat dihapus). Status `RF-00071` dipulihkan ke To be Returned lewat fixture backend di hook `after`; entri log tetap bertambah.
- Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, `QR-00300`, `SA-00020`, `UT-00010`, `RF-00500`) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik tab `To Be Returned`.
2. Klik tombol "Receive TAG".

### TC-1444: Kode QR sudah dicetak tetapi belum terpasang

3. Pindai kode `QR-00300` dengan reader.
4. Verifikasi error inline "This TAG is not in the To Be Returned list." tampil.
5. Verifikasi daftar sesi tidak bertambah.

### TC-1474: Tag milik produk Supply Asset

6. Pindai kode `SA-00020` dengan reader.
7. Verifikasi pesan inline "This TAG is used by Supply Asset." tampil di Dialog Receive TAG.
8. Verifikasi pesan V-30 "This TAG is not in the To Be Returned list." tidak tampil.
9. Verifikasi `SA-00020` tidak masuk daftar sesi.
10. Verifikasi teks penghitung tetap "0 TAGs scanned".

### TC-1475: User TAG

11. Pindai kode `UT-00010` dengan reader.
12. Verifikasi pesan inline "This TAG is not in the To Be Returned list." tampil di Dialog Receive TAG.
13. Verifikasi pesan S-19 "This TAG is used by [Product]." tidak tampil.
14. Verifikasi `UT-00010` tidak masuk daftar sesi.
15. Verifikasi teks penghitung tetap "0 TAGs scanned".

### TC-549: Tag yang ditolak tidak ikut diproses

16. Pindai Tag `RF-00500` (ditolak) dengan reader.
17. Pindai Tag `RF-00071` dengan reader.
18. Klik tombol [Receive].
19. Verifikasi Toast "Success, TAG has been received." tampil.
20. Verifikasi baris `RF-00088` dan `NF-00092` tetap ada di tabel.
21. Verifikasi baris `RF-00071` tidak ada lagi di tabel.

## Notes

- Urutan TC diubah menjadi TC-1444, TC-1474, TC-1475, TC-549: tiga TC penolakan memakai satu dialog tanpa mengubah state, sedangkan TC-549 menerima `RF-00071` (S-10); pesan inline berurutan berbeda sehingga tidak butuh pembersih (R-12).
- Langkah penghubung: langkah 1 dan 2 membuka tab dan dialog (halaman TAG dibuka hook `beforeEach`). Tag yang ditolak (langkah 16) tidak punya Verifikasi sendiri karena Expected TC-549 tidak memuatnya.
- Anchor absence: langkah 4, 7, dan 12 (pesan inline yang tampil) menjadi anchor langkah 5, 8 sampai 10, dan 13 sampai 15; langkah 19 menjadi anchor langkah 21.
- A-15: nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, `QR-00300`, `SA-00020`, `UT-00010`, `RF-00500`) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan tercatat di Prerequisites spec ini.
- Temuan untuk QA:
  - Kode `QR-00300` berstatus berlawanan antar TC: sudah dicetak (Available) di TC-1444 dan belum pernah dicetak di TC-544 (spec 131).
  - Post Condition TC-549 ("Status Tag RF-00500 tidak berubah dan tidak ada entri Event Log untuknya") tidak punya langkah observasi di TC dan tidak diasersi; Post Condition "Tidak ada data yang berubah" TC-1474 dan TC-1475 juga tidak diasersi.
