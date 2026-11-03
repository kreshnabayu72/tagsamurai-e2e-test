---
id: TC-FA-TAG-E2E-141-receive-tag-pengembalian-tidak-dapat-dibatalkan-dan-hasil-receive-manually
title: "Receive TAG: pengembalian tidak dapat dibatalkan, dan hasil Receive TAG berbeda dari Receive Manually"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-569
  - TC-FA-TAG-1380
coverage:
  web: automated
---

# Receive TAG: pengembalian tidak dapat dibatalkan, dan hasil Receive TAG berbeda dari Receive Manually

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); pemulihan status Tag ke To be Returned lewat fixture backend.
- State global yang dipulihkan: Receive TAG menjadikan Tag Available dan Receive Manually menjadikannya Damaged/Missing di registri Global; keduanya menambah entri Event Log To Be Returned dan TAG Log Global yang tidak dapat dihapus. Status Tag dipulihkan ke To be Returned lewat fixture backend di hook `before` dan `after` serta pada langkah 15; entri log tetap bertambah.

## Test Steps

1. Klik tab `To Be Returned`.

### TC-569: Pengembalian Tag tidak dapat dibatalkan setelah Receive

2. Klik tombol "Receive TAG".
3. Verifikasi Alert Dialog "Receive TAG" berbunyi "Received TAGs leave FAMS and become Available in Global Settings. This can't be undone."
4. Pindai Tag `RF-00071` dengan reader.
5. Klik tombol [Receive].
6. Verifikasi baris `RF-00088` tampil di tabel To Be Returned.
7. Buka menu aksi baris `RF-00088`.
8. Verifikasi tab To Be Returned dan menu aksi baris lain tidak memuat kontrol pembatalan atau undo untuk `RF-00071`.
9. Tutup menu aksi dengan tombol Esc.
10. Klik "Event Log".
11. Verifikasi entri `RF-00071` tampil di Modal "Event Log: To Be Returned".
12. Verifikasi Event Log tidak memuat kontrol pembatalan atau undo untuk `RF-00071`.
13. Verifikasi entri `RF-00071` hanya-baca tanpa aksi baris.
14. Tutup Modal "Event Log: To Be Returned".
15. Pulihkan Tag `RF-00071` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-1380: Receive Manually tidak menghasilkan Available dan Receive TAG tidak menghasilkan Damaged/Missing

16. Klik tombol "Receive TAG".
17. Pindai Tag `RF-00071` dengan reader.
18. Klik tombol [Receive].
19. Tunggu aksi selesai (Dialog "Receive TAG" menutup).
20. Buka menu aksi baris `RF-00088`.
21. Klik "Receive Manually".
22. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
23. Klik tombol [Submit].
24. Tunggu aksi selesai (Dialog "Receive Manually" menutup).
25. Buka Global Settings > TAG.
26. Ketik Search `RF-00071`, tekan Enter.
27. Verifikasi `RF-00071` berstatus Available (bukan Damaged/Missing).
28. Ganti isi kotak search dengan `RF-00088`, tekan Enter.
29. Verifikasi `RF-00088` berstatus Damaged/Missing (bukan Available).

## Notes

- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 9 dan 14 menutup menu dan modal; langkah 15 memulihkan state antar TC (S-09); langkah 19 dan 24 menunggu aksi selesai sebelum pindah surface (bagian 8b butir 8); langkah 26 dan 28 adalah Search untuk menemukan baris target (R-16).
- Anchor langkah 6 (baris `RF-00088` tampil) dan langkah 11 (entri `RF-00071` tampil) menjadi anchor absence langkah 8, 12, dan 13; anchor itu tidak ada di Expected TC.
- Pembagian TC lintas spec: TC-567 dan TC-568 ada di spec 133.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Expected a TC-569 menggabungkan tab To Be Returned dan Event Log dalam satu butir; spec memecahnya per surface (langkah 8 dan langkah 12).
  - Langkah 1 TC-1380 "Receive TAG RF-00071 sampai selesai" tidak punya Expected sendiri; spec menuliskan langkah lengkapnya (langkah 16 sampai 19) dan "Receive Manually RF-00088" (langkah 20 sampai 24).
