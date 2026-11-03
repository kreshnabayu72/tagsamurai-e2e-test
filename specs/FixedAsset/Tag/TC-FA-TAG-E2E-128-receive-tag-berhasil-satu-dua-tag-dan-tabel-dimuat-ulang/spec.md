---
id: TC-FA-TAG-E2E-128-receive-tag-berhasil-satu-dua-tag-dan-tabel-dimuat-ulang
title: "Receive TAG: berhasil untuk satu dan dua Tag, dan tabel dimuat ulang dengan Search tetap"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-536
  - TC-FA-TAG-537
  - TC-FA-TAG-538
coverage:
  web: automated
---

# Receive TAG: berhasil untuk satu dan dua Tag, dan tabel dimuat ulang dengan Search tetap

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); pemulihan status Tag ke To be Returned lewat fixture backend.
- State global yang dipulihkan: Receive mengubah Tag menjadi Available di registri Global dan menambah entri Event Log To Be Returned serta TAG Log Global yang tidak dapat dihapus. Status Tag dipulihkan ke To be Returned lewat fixture backend di hook `before` dan `after` serta pada langkah 9 dan 18; entri log tetap bertambah.

## Test Steps

1. Klik tab `To Be Returned`.

### TC-536: Receive satu Tag

2. Klik tombol "Receive TAG".
3. Pindai Tag `RF-00071` dengan reader.
4. Klik tombol [Receive].
5. Verifikasi Toast "Success, TAG has been received." tampil.
6. Verifikasi Dialog "Receive TAG" menutup.
7. Verifikasi badge tab "To Be Returned" berkurang satu menjadi 2.
8. Verifikasi baris `RF-00071` tidak ada lagi di tabel To Be Returned.
9. Pulihkan Tag `RF-00071` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-537: Receive dua Tag

10. Klik tombol "Receive TAG".
11. Pindai Tag `RF-00071` dengan reader.
12. Pindai Tag `NF-00092` dengan reader.
13. Klik tombol [Receive].
14. Verifikasi Toast "Success, TAG has been received." tampil.
15. Verifikasi Dialog "Receive TAG" menutup.
16. Verifikasi baris `RF-00088` tetap ada di tabel.
17. Verifikasi baris `RF-00071` dan `NF-00092` tidak ada lagi di tabel.
18. Pulihkan Tag `RF-00071` dan `NF-00092` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-538: Tabel dimuat ulang mempertahankan Search

19. Ketik Search "Excavator", tekan Enter.
20. Klik tombol "Receive TAG".
21. Pindai Tag `RF-00071` dengan reader.
22. Klik tombol [Receive].
23. Verifikasi input Search tetap berisi "Excavator" setelah dialog menutup.
24. Verifikasi baris `RF-00088` tampil di tabel.
25. Verifikasi tabel hanya menampilkan baris yang cocok "Excavator" tanpa `RF-00071`.
26. Klik `(←)` pada kotak Search.

## Notes

- Langkah penghubung: langkah 9 dan 18 memulihkan Tag yang sudah diterima supaya TC berikutnya punya Tag To Be Returned (S-09); langkah 26 menutup input Search; langkah 19 adalah Search untuk menemukan baris target (R-16).
- Urutan Verifikasi TC-536: Toast lebih dulu karena state sementara (bagian 8b butir 5), lalu dialog menutup, badge, dan baris.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Post Condition TC-536 dan TC-537 (status Available di registri Global, entri Event Log, entri TAG Log Global) tidak punya langkah observasi di TC dan tidak diasersi.
  - Judul TC-538 menyebut "halaman aktif" tetapi Expected hanya mengasersi Search dan baris tabel; halaman aktif tidak diasersi.
