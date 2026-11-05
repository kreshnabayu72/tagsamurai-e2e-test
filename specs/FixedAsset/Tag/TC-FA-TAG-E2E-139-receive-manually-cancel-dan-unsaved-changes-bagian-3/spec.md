---
id: TC-FA-TAG-E2E-139-receive-manually-cancel-dan-unsaved-changes-bagian-3
title: "Receive Manually: muat ulang halaman memicu konfirmasi bawaan browser dan dialog terisi Note dianggap terisi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-595
  - TC-FA-TAG-596
coverage:
  web: automated
---

# Receive Manually: muat ulang halaman memicu konfirmasi bawaan browser dan dialog terisi Note dianggap terisi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.). Spec tidak menekan [Submit], jadi status Tag tidak berubah.
- Kemampuan teknis (disediakan tim FE): penanganan dialog `beforeunload` bawaan browser (teramati dan dibatalkan sehingga halaman tidak dimuat ulang).
- Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

1. Klik tab `To Be Returned`.
2. Buka menu aksi baris `RF-00071`.
3. Klik "Receive Manually".
4. Isi Textarea "Note" dengan "Tag rusak saat serah terima".

### TC-595: Refresh halaman saat dialog terisi

5. Tekan F5 untuk memuat ulang halaman.
6. Verifikasi konfirmasi bawaan browser (beforeunload) muncul sebelum halaman dimuat ulang.
7. Batalkan muat ulang (tetap di halaman).

### TC-596: Dialog yang hanya terisi Note dianggap terisi

8. Klik ikon close pada header dialog.
9. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave].
10. Verifikasi dialog Receive Manually tetap terbuka di bawahnya.
11. Klik tombol [Leave] pada dialog "Unsaved Changes".

## Notes

- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG). Dialog dan isian langkah 2 sampai 4 dipakai TC-595 dan TC-596; langkah 7 membatalkan muat ulang supaya dialog tetap terbuka; langkah 11 menutup keduanya (S-08).
- Pembagian TC lintas spec: TC-582 sampai TC-590 ada di spec 137; TC-591 sampai TC-594 ada di spec 138.
- A-15: nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Post Condition TC-595 dan TC-596 ("Tag RF-00071 tetap To Be Returned dan tidak ada entri Event Log atau TAG Log baru") tidak punya langkah observasi di TC dan tidak diasersi.
