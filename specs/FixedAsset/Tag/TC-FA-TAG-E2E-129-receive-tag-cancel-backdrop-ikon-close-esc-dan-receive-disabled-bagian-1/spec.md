---
id: TC-FA-TAG-E2E-129-receive-tag-cancel-backdrop-ikon-close-esc-dan-receive-disabled-bagian-1
title: "Receive TAG: Cancel, ikon close, backdrop, dan Receive Disabled saat daftar kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-539
  - TC-FA-TAG-540
  - TC-FA-TAG-541
  - TC-FA-TAG-542
  - TC-FA-TAG-1495
coverage:
  web: automated
---

# Receive TAG: Cancel, ikon close, backdrop, dan Receive Disabled saat daftar kosong

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader). Tidak ada kasus yang menekan [Receive] dengan hasil sukses, jadi status Tag tidak berubah.

## Test Steps

1. Klik tab `To Be Returned`.

### TC-539: Cancel pada dialog berisi Tag terpindai

2. Klik tombol "Receive TAG".
3. Pindai Tag `RF-00071` dengan reader.
4. Klik tombol [Cancel].
5. Verifikasi dialog menutup langsung tanpa dialog konfirmasi aplikasi apa pun (D-09, D-11, dan Unsaved Changes tidak tampil).
6. Verifikasi baris `RF-00071` masih ada di tabel To Be Returned.
7. Klik tombol "Receive TAG" lagi.
8. Verifikasi dialog yang dibuka ulang menampilkan penghitung "0 TAGs scanned".
9. Verifikasi dialog yang dibuka ulang menampilkan empty state "Scan a TAG to add it to the list."

### TC-540: Cancel pada dialog kosong

10. Klik tombol [Cancel].
11. Verifikasi dialog menutup.
12. Verifikasi user tetap di tab To Be Returned.
13. Verifikasi tabel tidak berubah (baris `RF-00071`, `RF-00088`, dan `NF-00092` tetap ada).

### TC-542: [Receive] Disabled saat daftar sesi kosong

14. Klik tombol "Receive TAG".
15. Coba klik tombol [Receive].
16. Verifikasi tombol [Receive] tampil dalam keadaan Disabled dan klik tidak menjalankan aksi.
17. Verifikasi tidak ada toast.

### TC-541: Klik backdrop

18. Pindai Tag `RF-00071` dengan reader.
19. Klik area backdrop di luar dialog.
20. Verifikasi dialog tetap terbuka.
21. Verifikasi daftar sesi tetap memuat `RF-00071`.

### TC-1495: Ikon close pada dialog berisi Tag terpindai

22. Klik ikon close pada header dialog.
23. Verifikasi dialog menutup langsung tanpa dialog konfirmasi aplikasi apa pun (D-09, D-11, dan Unsaved Changes tidak tampil).
24. Verifikasi baris `RF-00071` masih ada di tabel To Be Returned.
25. Klik tombol "Receive TAG" lagi.
26. Verifikasi dialog yang dibuka ulang menampilkan penghitung "0 TAGs scanned".
27. Verifikasi dialog yang dibuka ulang menampilkan empty state "Scan a TAG to add it to the list."
28. Klik tombol [Cancel].

## Notes

- Urutan TC diubah menjadi TC-539, TC-540, TC-542, TC-541, TC-1495: dialog hasil buka ulang TC-539 yang kosong dipakai TC-540 dan TC-542, lalu TC-541 dan TC-1495 memindai `RF-00071` sehingga daftar sesi terisi (S-09, S-10).
- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 28 menutup dialog. Langkah 16 menjadi anchor langkah 17 (absence toast).
- Pembagian TC lintas spec: TC-1496 ada di spec 130.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Post Condition TC-539 dan TC-1495 ("Tag RF-00071 tetap To Be Returned; tidak ada entri Event Log maupun TAG Log baru") tidak punya langkah observasi di TC; hanya tabel yang diasersi.
