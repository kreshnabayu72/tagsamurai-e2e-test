---
id: TC-FA-TAG-E2E-134-receive-tag-konflik-sesi-lain-tidak-dapat-dibatalkan-dan-hasil-bagian-2
title: "Receive TAG: hasil parsial dan semua Tag gagal karena Tag diambil pengguna lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1460
  - TC-FA-TAG-1469
coverage:
  web: automated
---

# Receive TAG: hasil parsial dan semua Tag gagal karena Tag diambil pengguna lain

## Prerequisites

- Mode: FE+BE
- Akun Pengguna A (sesi UI): Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Pengguna B (pelaku kedua): sesi API (lihat `suite.md`), tanpa asersi di sesinya. Akun Pengguna B disediakan tim FE (tidak ada di Pre-setup TC; lihat Temuan untuk QA) dan berhak mengubah Tag.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun Pengguna A (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada):
  - Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `RF-00089` (RFID, `Excavator 20 Ton - 6`, Disposal Center, Dedi K.).
  - Aset `Excavator 20 Ton - 51` (AST-0051, Group Plant A, TAG Type Asset Name RFID) belum punya Tag Paired (Not Paired Yet).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); pemicu Pengguna B lewat sesi API (Receive TAG dan Pair TAG); pembacaan status Tag dari backend untuk Expected status; pemulihan status Tag dan pelepasan pasangan Tag lewat fixture backend.
- State global yang dipulihkan: Receive mengubah Tag menjadi Available di registri Global dan menambah entri Event Log To Be Returned serta TAG Log Global yang tidak dapat dihapus; Pair TAG memasangkan `RF-00089` ke `Excavator 20 Ton - 51`. Status Tag dan pasangan dipulihkan lewat fixture backend di hook `before` dan `after` serta pada langkah 19; entri log tetap bertambah.

## Test Steps

1. Klik tab `To Be Returned`.

### TC-1460: Hasil parsial

2. Pengguna A: klik tombol "Receive TAG".
3. Pengguna A: pindai Tag `RF-00071` dengan reader.
4. Pengguna A: pindai Tag `RF-00088` dengan reader.
5. Pengguna A: pindai Tag `RF-00089` dengan reader.
6. Pengguna B (sesi API): Receive TAG `RF-00088` hingga Tag berstatus Available tersimpan.
7. Pengguna B (sesi API): Pair TAG `RF-00089` ke aset `Excavator 20 Ton - 51` hingga Tag berstatus Paired tersimpan.
8. Pengguna A: klik tombol [Receive].
9. Verifikasi Toast "Error, failed to receive TAG." tampil.
10. Verifikasi Toast "Success, TAG has been received." tampil karena minimal satu Tag (`RF-00071`) berhasil diterima.
11. Verifikasi `RF-00071` keluar dari daftar sesi.
12. Verifikasi `RF-00071` keluar dari tabel To Be Returned.
13. Verifikasi `RF-00071` berstatus Available.
14. Verifikasi `RF-00088` tetap di daftar sesi dengan caption inline "This TAG is not in the To Be Returned list." pada barisnya.
15. Verifikasi `RF-00089` tetap di daftar sesi dengan caption inline "This TAG is not in the To Be Returned list."
16. Verifikasi Dialog Receive TAG tetap terbuka.
17. Verifikasi daftar sesi hanya memuat `RF-00088` dan `RF-00089`.
18. Klik tombol [Cancel].
19. Pulihkan Tag `RF-00088` dan `RF-00089` ke To Be Returned dan lepaskan pasangan `RF-00089` lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-1469: Semua Tag gagal

20. Pengguna A: klik tombol "Receive TAG".
21. Pengguna A: pindai Tag `RF-00088` dengan reader.
22. Pengguna A: pindai Tag `RF-00089` dengan reader.
23. Pengguna B (sesi API): Receive TAG `RF-00088` hingga Tag berstatus Available tersimpan.
24. Pengguna B (sesi API): Pair TAG `RF-00089` ke aset `Excavator 20 Ton - 51` hingga Tag berstatus Paired tersimpan.
25. Pengguna A: klik tombol [Receive].
26. Verifikasi Toast "Error, failed to receive TAG." tampil.
27. Verifikasi Toast "Success, TAG has been received." tidak tampil.
28. Verifikasi `RF-00088` tetap di daftar sesi dengan caption inline "This TAG is not in the To Be Returned list." pada barisnya.
29. Verifikasi `RF-00089` tetap di daftar sesi dengan caption inline "This TAG is not in the To Be Returned list."
30. Verifikasi Dialog Receive TAG tetap terbuka.
31. Verifikasi daftar sesi memuat `RF-00088` dan `RF-00089`.
32. Klik tombol [Cancel].

## Notes

- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 18 dan 32 menutup dialog; langkah 19 memulihkan state antar TC (S-09).
- Pengguna B memakai sesi API sehingga bukan kelas c; langkah pemicu ditulis "... hingga ... tersimpan" (R-20). Urutan Verifikasi TC-1460 menaruh kedua Toast lebih dulu karena state sementara (bagian 8b butir 5). Langkah 26 menjadi anchor absence langkah 27.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `RF-00089`, `Excavator 20 Ton - 51`, AST-0051) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - TC-1460 dan TC-1469 menyebut "Pengguna B" tanpa akun; spec memakai akun "disediakan tim FE".
  - Post Condition TC-1460 dan TC-1469 (Event Log: satu entri `RF-00071` dari Pengguna A, tanpa entri tambahan dari Pengguna A untuk `RF-00088` dan `RF-00089`) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-1460 dan TC-1469 diberi label Manual Only karena "dua sesi/pengguna paralel"; spec memakai sesi API untuk Pengguna B.
