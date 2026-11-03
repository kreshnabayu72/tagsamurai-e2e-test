---
id: TC-FA-TAG-E2E-133-receive-tag-konflik-sesi-lain-tidak-dapat-dibatalkan-dan-hasil-bagian-1
title: "Receive TAG: Tag sudah diterima atau dipasang pengguna lain sebelum [Receive]"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-567
  - TC-FA-TAG-568
coverage:
  web: automated
---

# Receive TAG: Tag sudah diterima atau dipasang pengguna lain sebelum [Receive]

## Prerequisites

- Mode: FE+BE
- Akun Pengguna A (sesi UI): Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Pengguna B (pelaku kedua): sesi API (lihat `suite.md`), tanpa asersi di sesinya. Akun Pengguna B disediakan tim FE (tidak ada di Pre-setup TC; lihat Temuan untuk QA) dan berhak mengubah Tag.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun Pengguna A (lihat `suite.md`).
- Data:
  - Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
  - Dinamis (dibuat di hook `before`, dibersihkan di hook `after`): aset Not Paired Yet `Aset Uji Pair-{runId}-133` (TAG Type Asset Name RFID) untuk Pair TAG Pengguna B di TC-568; Precondition TC-568 tidak menyebutnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); pemicu Pengguna B lewat sesi API (Receive TAG dan Pair TAG); pembacaan status Tag dari backend untuk Expected status; pemulihan status Tag dan pelepasan pasangan Tag lewat fixture backend.
- State global yang dipulihkan: Receive mengubah Tag menjadi Available di registri Global dan menambah entri Event Log To Be Returned serta TAG Log Global yang tidak dapat dihapus; Pair TAG memasangkan `RF-00088`. Status Tag dan pasangan dipulihkan lewat fixture backend di hook `before` dan `after` serta pada langkah 14; entri log tetap bertambah.

## Test Steps

1. Klik tab `To Be Returned`.

### TC-567: Tag sudah diterima sesi lain

2. Pengguna A: klik tombol "Receive TAG".
3. Pengguna A: pindai Tag `RF-00071` dengan reader.
4. Pengguna A: pindai Tag `RF-00088` dengan reader.
5. Pengguna B (sesi API): Receive TAG `RF-00088` hingga Tag berstatus Available tersimpan.
6. Pengguna A: klik tombol [Receive].
7. Verifikasi Toast "Error, failed to receive TAG." tampil.
8. Verifikasi baris `RF-00088` di daftar sesi menampilkan caption inline "This TAG is not in the To Be Returned list."
9. Verifikasi baris `RF-00071` hilang dari tabel To Be Returned.
10. Verifikasi `RF-00071` keluar dari daftar sesi.
11. Verifikasi `RF-00088` tetap di daftar sesi Dialog Receive TAG.
12. Verifikasi dialog tetap terbuka.
13. Klik tombol [Cancel].
14. Pulihkan Tag `RF-00071` dan `RF-00088` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-568: Tag dalam sesi sudah dipasang ke aset

15. Pengguna A: klik tombol "Receive TAG".
16. Pengguna A: pindai Tag `RF-00071` dengan reader.
17. Pengguna A: pindai Tag `RF-00088` dengan reader.
18. Pengguna B (sesi API): Pair TAG `RF-00088` ke aset `Aset Uji Pair-{runId}-133` hingga Tag berstatus Paired tersimpan.
19. Pengguna A: klik tombol [Receive].
20. Verifikasi `RF-00088` ditolak server dengan caption inline "This TAG is not in the To Be Returned list."
21. Verifikasi `RF-00088` tetap di daftar sesi Dialog Receive TAG.
22. Verifikasi status `RF-00088` tetap Paired.
23. Verifikasi `RF-00071` diproses menjadi Available.
24. Verifikasi `RF-00071` keluar dari tabel To Be Returned.
25. Verifikasi `RF-00071` keluar dari daftar sesi.
26. Klik tombol [Cancel].

## Notes

- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 13 dan 26 menutup dialog; langkah 14 memulihkan state antar TC (S-09).
- Pengguna B memakai sesi API sehingga bukan kelas c; langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Pembagian TC lintas spec: TC-569 dan TC-1380 ada di spec 141; TC-1460 dan TC-1469 ada di spec 134.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - TC-567 dan TC-568 menyebut "Pengguna B" tanpa akun, dan TC-568 tidak menyebut aset Not Paired Yet untuk Pair TAG; spec memakai akun "disediakan tim FE" dan aset milik spec.
  - Post Condition TC-567 (Event Log: satu entri `RF-00088` dari Pengguna B dan satu entri `RF-00071`, tanpa entri tambahan dari Pengguna A) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-567 dan TC-568 diberi label Manual Only karena "dua sesi/pengguna paralel"; spec memakai sesi API untuk Pengguna B.
