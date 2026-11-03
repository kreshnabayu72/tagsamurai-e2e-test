---
id: TC-FA-TAG-E2E-130-receive-tag-cancel-backdrop-ikon-close-esc-dan-receive-disabled-bagian-2
title: "Receive TAG: Esc pada dialog berisi Tag terpindai menutup tanpa konfirmasi dan membuang sesi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1496
coverage:
  web: automated
---

# Receive TAG: Esc pada dialog berisi Tag terpindai menutup tanpa konfirmasi dan membuang sesi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader). Spec tidak menekan [Receive], jadi status Tag tidak berubah.

## Test Steps

1. Klik tab `To Be Returned`.
2. Klik tombol "Receive TAG".
3. Pindai Tag `RF-00071` dengan reader.
4. Tekan tombol Esc.
5. Verifikasi dialog menutup langsung tanpa dialog konfirmasi aplikasi apa pun (D-09, D-11, dan Unsaved Changes tidak tampil).
6. Verifikasi baris `RF-00071` masih ada di tabel To Be Returned.
7. Klik tombol "Receive TAG" lagi.
8. Verifikasi dialog yang dibuka ulang menampilkan penghitung "0 TAGs scanned".
9. Verifikasi dialog yang dibuka ulang menampilkan empty state "Scan a TAG to add it to the list."
10. Klik tombol [Cancel].

## Notes

- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 10 menutup dialog.
- Pembagian TC lintas spec: TC-539 sampai TC-542 dan TC-1495 ada di spec 129.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Post Condition TC-1496 ("Tag RF-00071 tetap To Be Returned; tidak ada entri Event Log maupun TAG Log baru") tidak punya langkah observasi di TC; hanya tabel yang diasersi.
