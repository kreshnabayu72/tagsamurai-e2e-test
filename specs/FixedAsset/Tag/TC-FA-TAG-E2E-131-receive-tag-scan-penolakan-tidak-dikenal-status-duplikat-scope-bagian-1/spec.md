---
id: TC-FA-TAG-E2E-131-receive-tag-scan-penolakan-tidak-dikenal-status-duplikat-scope-bagian-1
title: "Receive TAG: penolakan scan untuk kode tidak dikenal, status bukan To Be Returned, duplikat, dan scope group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-543
  - TC-FA-TAG-544
  - TC-FA-TAG-545
  - TC-FA-TAG-546
  - TC-FA-TAG-547
  - TC-FA-TAG-548
coverage:
  web: automated
---

# Receive TAG: penolakan scan untuk kode tidak dikenal, status bukan To Be Returned, duplikat, dan scope group

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (langkah 22): Manage asset & TAG dengan Update di group Disposal Center (`manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TAG_UP_DC_PASSWORD`. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada):
  - Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
  - Kode `RF-99999` tidak ada di registri Global.
  - Kode `QR-00300` belum pernah dicetak lewat Print QR (tidak terdaftar di registri Global).
  - Tag `RF-00500` berstatus Available di Global.
  - Tag `RF-00130` berstatus Paired pada aset AST-0020.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader). Semua pindaian ditolak atau hanya menambah daftar sesi tanpa [Receive], jadi tidak ada state global yang berubah.
- Nilai literal Pre-setup (`RF-00071`, `NF-00092`, `RF-99999`, `QR-00300`, `RF-00500`, `RF-00130`, AST-0020) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik tab `To Be Returned`.
2. Klik tombol "Receive TAG".

### TC-543: Kode tidak dikenal di Global

3. Pindai kode `RF-99999` dengan reader.
4. Verifikasi error inline "Error, can't recognize TAG." tampil.
5. Verifikasi daftar sesi tidak bertambah.
6. Verifikasi penghitung tetap "0 TAGs scanned".

### TC-545: Tag berstatus Available

7. Pindai Tag `RF-00500` dengan reader.
8. Verifikasi error inline "This TAG is not in the To Be Returned list." tampil.
9. Verifikasi daftar sesi tidak bertambah.

### TC-544: Kode QR yang belum pernah dicetak

10. Pindai kode `QR-00300` dengan reader.
11. Verifikasi error inline "Error, can't recognize TAG." tampil.
12. Verifikasi daftar sesi tidak bertambah.

### TC-546: Tag berstatus Paired

13. Pindai Tag `RF-00130` dengan reader.
14. Verifikasi error inline "This TAG is not in the To Be Returned list." tampil.
15. Verifikasi daftar sesi tidak bertambah.

### TC-547: Tag yang sama dua kali dalam sesi

16. Pindai Tag `RF-00071` dengan reader.
17. Pindai Tag `RF-00071` sekali lagi dengan reader.
18. Verifikasi error inline "This TAG has already been scanned." tampil.
19. Verifikasi daftar sesi tetap memuat satu baris `RF-00071`.
20. Verifikasi penghitung "1 TAG scanned".
21. Klik tombol [Cancel].

### TC-548: Return Group di luar group Update

22. Ganti akun: Logout, lalu login sebagai Manage asset & TAG dengan Update di group Disposal Center.
23. Buka Fixed Asset > TAG > To Be Returned.
24. Klik tombol "Receive TAG".
25. Pindai Tag `NF-00092` (Return Group HQ Warehouse, di luar group Update) dengan reader.
26. Verifikasi error inline "You don't have access to this TAG's group." tampil.
27. Verifikasi daftar sesi tidak bertambah.
28. Klik tombol [Cancel].

## Notes

- Urutan TC diubah menjadi TC-543, TC-545, TC-544, TC-546, TC-547, TC-548 supaya dua error inline yang identik tidak berurutan (R-12); TC-547 memasukkan `RF-00071` ke daftar sehingga ditempatkan terakhir di akun pertama (S-09, S-10).
- Langkah penghubung: langkah 1 dan 2 membuka tab dan dialog (halaman TAG dibuka hook `beforeEach`); langkah 21 dan 28 menutup dialog. Langkah 22 adalah ganti akun eksplisit.
- Anchor absence daftar sesi tidak bertambah: error inline yang diasersi tepat sebelumnya (langkah 4, 8, 11, 14, 26); penghitung "0 TAGs scanned" pada langkah 6 dan "1 TAG scanned" pada langkah 20 menjadi anchor angka.
- A-15: nilai literal Pre-setup (`RF-00071`, `NF-00092`, `RF-99999`, `QR-00300`, `RF-00500`, `RF-00130`, AST-0020) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Kode `QR-00300` berstatus berlawanan antar TC: belum pernah dicetak di TC-544 dan sudah dicetak (Available) di TC-1444 (spec 132); pemulihan berlangsung di hook `before` dan `after` tiap spec.
