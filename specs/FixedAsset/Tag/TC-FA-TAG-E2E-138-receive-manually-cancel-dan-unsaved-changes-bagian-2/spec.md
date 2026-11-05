---
id: TC-FA-TAG-E2E-138-receive-manually-cancel-dan-unsaved-changes-bagian-2
title: "Receive Manually: Cancel dan Leave pada Unsaved Changes, serta ikon close pada dialog belum terisi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-591
  - TC-FA-TAG-592
  - TC-FA-TAG-593
  - TC-FA-TAG-594
coverage:
  web: automated
---

# Receive Manually: Cancel dan Leave pada Unsaved Changes, serta ikon close pada dialog belum terisi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.). Spec tidak menekan [Submit], jadi status Tag tidak berubah.
- Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

1. Klik tab `To Be Returned`.
2. Buka menu aksi baris `RF-00071`.
3. Klik "Receive Manually".
4. Isi Textarea "Note" dengan "Tag rusak saat serah terima".

### TC-591: Cancel pada Unsaved Changes

5. Klik ikon close pada header dialog.
6. Verifikasi dialog "Unsaved Changes" tampil.
7. Klik tombol [Cancel] pada dialog "Unsaved Changes".
8. Verifikasi dialog "Unsaved Changes" menutup.
9. Verifikasi dialog Receive Manually tetap terbuka dengan isian yang sama.

### TC-592: Leave pada Unsaved Changes

10. Klik ikon close pada header dialog.
11. Verifikasi dialog "Unsaved Changes" tampil.
12. Klik tombol [Leave] pada dialog "Unsaved Changes".
13. Verifikasi dialog "Unsaved Changes" menutup.
14. Verifikasi dialog Receive Manually menutup.
15. Verifikasi tidak ada toast.

### TC-593: Ikon close pada dialog belum terisi

16. Buka menu aksi baris `RF-00071`.
17. Klik "Receive Manually".
18. Klik ikon close pada header dialog.
19. Verifikasi dialog menutup langsung tanpa dialog "Unsaved Changes".

### TC-594: Isian dikosongkan kembali

20. Buka menu aksi baris `RF-00071`.
21. Klik "Receive Manually".
22. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
23. Kosongkan kembali isian yang tadi diisi.
24. Klik ikon close pada header dialog.
25. Verifikasi dialog menutup langsung tanpa dialog "Unsaved Changes".

## Notes

- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG). Dialog dari langkah 3 dan isian langkah 4 dipakai TC-591 dan TC-592. Langkah 6 dan 11 (dialog "Unsaved Changes" tampil) dituliskan sesuai S-08; di TC-591 dan TC-592 Expected TC tidak memuatnya.
- Anchor absence: langkah 14 untuk langkah 15 (dialog menutup).
- Pembagian TC lintas spec: TC-582 sampai TC-590 ada di spec 137; TC-595 dan TC-596 ada di spec 139.
- A-15: nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Post Condition TC-591 sampai TC-594 ("Tag RF-00071 tetap To Be Returned dan tidak ada entri Event Log atau TAG Log baru") tidak punya langkah observasi di TC dan tidak diasersi.
