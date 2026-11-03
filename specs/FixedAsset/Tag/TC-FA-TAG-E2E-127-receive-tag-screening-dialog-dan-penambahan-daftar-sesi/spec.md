---
id: TC-FA-TAG-E2E-127-receive-tag-screening-dialog-dan-penambahan-daftar-sesi
title: "Receive TAG: screening Dialog dan penambahan Tag ke daftar sesi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-531
  - TC-FA-TAG-532
  - TC-FA-TAG-533
  - TC-FA-TAG-534
  - TC-FA-TAG-535
coverage:
  web: automated
---

# Receive TAG: screening Dialog dan penambahan Tag ke daftar sesi

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (langkah 27): Manage asset & TAG dengan Update di group Disposal Center (`manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TAG_UP_DC_PASSWORD`. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada):
  - Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
  - Tag `RF-00099` To Be Returned dengan Return Group anak dari Disposal Center (untuk akun kedua).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); memindai Tag di dialog tidak mengubah status Tag, jadi tidak ada state global yang berubah.

## Test Steps

1. Klik tab `To Be Returned`.
2. Klik tombol "Receive TAG".

### TC-531: Screening Dialog Receive TAG saat daftar sesi kosong

3. Verifikasi Dialog "Receive TAG" (Size LG) terbuka di atas tab To Be Returned.
4. Verifikasi Alert info tampil dengan teks "Received TAGs leave FAMS and become Available in Global Settings. This can't be undone."
5. Verifikasi teks penghitung di kiri atas daftar berbunyi "0 TAGs scanned".
6. Verifikasi ButtonScan "Scan TAG" di kanan teks penghitung dalam keadaan aktif.
7. Verifikasi daftar sesi menampilkan empty state "Scan a TAG to add it to the list."
8. Verifikasi footer berisi tombol [Cancel] dan [Receive].
9. Verifikasi tombol [Receive] Disabled (tetap tampil).
10. Verifikasi label tombol [Receive] tanpa angka penghitung.
11. Verifikasi daftar sesi bukan DataTable: tidak ada Setup Column, Search, Filter, maupun Sort.

### TC-532: Memindai satu Tag To Be Returned

12. Pindai Tag `RF-00071` dengan reader.
13. Verifikasi daftar sesi menampilkan satu baris: ikon tipe RFID, TAG Code "RF-00071", "Excavator 20 Ton - 2", "Disposal Center", "Dedi K."
14. Verifikasi penghitung berubah menjadi "1 TAG scanned".
15. Verifikasi empty state "Scan a TAG to add it to the list." tidak tampil lagi.
16. Verifikasi tombol [Receive] Enabled.
17. Verifikasi baris sesi tidak memiliki tombol aksi per baris.

### TC-533: Memindai dua Tag berbeda

18. Pindai Tag `RF-00088` dengan reader.
19. Verifikasi daftar sesi memuat dua baris: `RF-00071` dan `RF-00088`.
20. Verifikasi penghitung menampilkan "2 TAGs scanned".

### TC-534: Memindai Tag NFC

21. Klik tombol [Cancel].
22. Klik tombol "Receive TAG".
23. Pindai Tag `NF-00092` dengan reader.
24. Verifikasi daftar sesi menampilkan satu baris dengan ikon tipe NFC, TAG Code "NF-00092", "Laptop Pro 14 - 8", "HQ Warehouse", "Rina T."
25. Verifikasi penghitung "1 TAG scanned".
26. Klik tombol [Cancel].

### TC-535: Return Group descendant dari group Update

27. Ganti akun: Logout, lalu login sebagai Manage asset & TAG dengan Update di group Disposal Center.
28. Buka Fixed Asset > TAG > To Be Returned.
29. Klik tombol "Receive TAG".
30. Pindai Tag `RF-00099` dengan reader.
31. Verifikasi Tag `RF-00099` masuk daftar sesi.
32. Verifikasi penghitung menjadi "1 TAG scanned".
33. Klik tombol [Cancel].

## Notes

- Langkah penghubung: langkah 1 dan 2 membuka tab dan dialog (TC menulis "Buka Fixed Asset > TAG > To Be Returned" sedangkan halaman dibuka hook `beforeEach`); langkah 21 dan 22 membersihkan daftar sesi sebelum TC-534 (S-09); langkah 26 dan 33 menutup dialog.
- Langkah 27 adalah ganti akun eksplisit; akun pertama login di hook `before`.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, `RF-00099`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - TC-535 tidak menyebut nama aset, tipe, dan Current Holder `RF-00099`; Expected hanya masuk daftar dan penghitung.
