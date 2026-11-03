---
id: TC-FA-TAG-E2E-137-receive-manually-cancel-dan-unsaved-changes-bagian-1
title: "Receive Manually: Cancel kosong, backdrop, dan Unsaved Changes lewat Cancel, ikon close, dan Esc"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-582
  - TC-FA-TAG-586
  - TC-FA-TAG-588
  - TC-FA-TAG-589
  - TC-FA-TAG-590
coverage:
  web: automated
---

# Receive Manually: Cancel kosong, backdrop, dan Unsaved Changes lewat Cancel, ikon close, dan Esc

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.). Spec tidak menekan [Submit], jadi status Tag tidak berubah.

## Test Steps

1. Klik tab `To Be Returned`.

### TC-582: Cancel pada dialog kosong

2. Buka menu aksi baris `RF-00071`.
3. Klik "Receive Manually".
4. Klik tombol [Cancel].
5. Verifikasi dialog menutup langsung tanpa dialog konfirmasi.
6. Verifikasi baris `RF-00071` tetap ada di tabel.

### TC-586: Klik backdrop

7. Buka menu aksi baris `RF-00071`.
8. Klik "Receive Manually".
9. Klik area backdrop di luar dialog.
10. Verifikasi dialog tetap terbuka.

### TC-588: Cancel pada dialog terisi

11. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
12. Klik tombol [Cancel].
13. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave].
14. Verifikasi dialog Receive Manually tetap terbuka di bawahnya.
15. Klik tombol [Cancel] pada dialog "Unsaved Changes".

### TC-589: Ikon close pada dialog terisi

16. Klik ikon close pada header dialog.
17. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave].
18. Verifikasi dialog Receive Manually tetap terbuka di bawahnya.
19. Klik tombol [Cancel] pada dialog "Unsaved Changes".

### TC-590: Esc pada dialog terisi

20. Tekan tombol Esc.
21. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave].
22. Verifikasi dialog Receive Manually tetap terbuka di bawahnya.
23. Klik tombol [Leave] pada dialog "Unsaved Changes".

## Notes

- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG). Dialog Receive Manually dari langkah 8 dipakai TC-586, TC-588, TC-589, dan TC-590; langkah 15 dan 19 menutup dialog "Unsaved Changes" dengan [Cancel] sehingga isian tetap terisi untuk TC berikutnya, dan langkah 23 menutup keduanya dengan [Leave] (S-08).
- Pembagian TC lintas spec: TC-591 sampai TC-594 ada di spec 138; TC-595 dan TC-596 ada di spec 139.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Post Condition TC-588 sampai TC-590 ("Tag RF-00071 tetap To Be Returned dan tidak ada entri Event Log atau TAG Log baru") tidak punya langkah observasi di TC dan tidak diasersi.
