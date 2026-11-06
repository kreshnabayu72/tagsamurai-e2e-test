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
- Baseline jumlah entri Event Log To Be Returned untuk `RF-00071` dibaca pada langkah 2 lewat kemampuan baca (disediakan tim FE/BE), sebelum pemicu [Receive] langkah 6; Event Log bersifat permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18 (S-12, S-14).
- State global yang dipulihkan: Receive TAG menjadikan Tag Available dan Receive Manually menjadikannya Damaged/Missing di registri Global; keduanya menambah entri Event Log To Be Returned dan TAG Log Global yang tidak dapat dihapus. Status Tag dipulihkan ke To be Returned lewat fixture backend di hook `before` dan `after` serta pada langkah 16; entri log tetap bertambah.
- Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik tab `To Be Returned`.
2. Catat jumlah entri Event Log To Be Returned untuk `RF-00071` sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE).

### TC-569: Pengembalian Tag tidak dapat dibatalkan setelah Receive

3. Klik tombol "Receive TAG".
4. Verifikasi Alert Dialog "Receive TAG" berbunyi "Received TAGs leave FAMS and become Available in Global Settings. This can't be undone."
5. Pindai Tag `RF-00071` dengan reader.
6. Klik tombol [Receive].
7. Verifikasi baris `RF-00088` tampil di tabel To Be Returned.
8. Buka menu aksi baris `RF-00088`.
9. Verifikasi tab To Be Returned dan menu aksi baris lain tidak memuat kontrol pembatalan atau undo untuk `RF-00071`.
10. Tutup menu aksi dengan tombol Esc.
11. Klik "Event Log".
12. Verifikasi satu entri baru `RF-00071` tampil di Modal "Event Log: To Be Returned" (selisih jumlah entri terhadap baseline langkah 2).
13. Verifikasi Event Log tidak memuat kontrol pembatalan atau undo untuk `RF-00071`.
14. Verifikasi entri `RF-00071` hanya-baca tanpa aksi baris.
15. Tutup Modal "Event Log: To Be Returned".
16. Pulihkan Tag `RF-00071` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-1380: Receive Manually tidak menghasilkan Available dan Receive TAG tidak menghasilkan Damaged/Missing

17. Klik tombol "Receive TAG".
18. Pindai Tag `RF-00071` dengan reader.
19. Klik tombol [Receive].
20. Tunggu aksi selesai (Dialog "Receive TAG" menutup).
21. Buka menu aksi baris `RF-00088`.
22. Klik "Receive Manually".
23. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
24. Klik tombol [Submit].
25. Tunggu aksi selesai (Dialog "Receive Manually" menutup).
26. Buka Global Settings > TAG.
27. Ketik Search `RF-00071`, tekan Enter.
28. Verifikasi `RF-00071` berstatus Available (bukan Damaged/Missing).
29. Ganti isi kotak search dengan `RF-00088`, tekan Enter.
30. Verifikasi `RF-00088` berstatus Damaged/Missing (bukan Available).

## Notes

- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 2 mencatat baseline Event Log (butir A-18); langkah 10 dan 15 menutup menu dan modal; langkah 16 memulihkan state antar TC (S-09); langkah 20 dan 25 menunggu aksi selesai sebelum pindah surface (bagian 8b butir 8); langkah 27 dan 29 adalah Search untuk menemukan baris target (R-16).
- Anchor langkah 7 (baris `RF-00088` tampil) dan langkah 12 (entri `RF-00071` tampil) menjadi anchor absence langkah 9, 13, dan 14; anchor itu tidak ada di Expected TC.
- Pembagian TC lintas spec: TC-567 dan TC-568 ada di spec 133.
- A-15: nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan tercatat di Prerequisites spec ini.
- Temuan untuk QA:
  - Expected a TC-569 menggabungkan tab To Be Returned dan Event Log dalam satu butir; spec memecahnya per surface (langkah 9 dan langkah 13).
  - Langkah 1 TC-1380 "Receive TAG RF-00071 sampai selesai" tidak punya Expected sendiri; spec menuliskan langkah lengkapnya (langkah 17 sampai 20) dan "Receive Manually RF-00088" (langkah 21 sampai 25).
