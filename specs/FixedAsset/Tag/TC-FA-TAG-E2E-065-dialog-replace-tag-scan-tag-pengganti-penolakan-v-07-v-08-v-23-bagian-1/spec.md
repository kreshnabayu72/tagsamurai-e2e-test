---
id: TC-FA-TAG-E2E-065-dialog-replace-tag-scan-tag-pengganti-penolakan-v-07-v-08-v-23-bagian-1
title: "Dialog Replace TAG: Scan Tag Pengganti, Verified, dan Penolakan Status Paired, Reserved, Retired, Damaged/Missing, Waiting for Approval (Bagian 1)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-293
  - TC-FA-TAG-294
  - TC-FA-TAG-295
  - TC-FA-TAG-296
  - TC-FA-TAG-297
coverage:
  web: automated
---

# Dialog Replace TAG: Scan Tag Pengganti, Verified, dan Penolakan Status Paired, Reserved, Retired, Damaged/Missing, Waiting for Approval (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00330` Paired; 'Excavator 20 Ton - 211' (AST-0211) dengan Tag RFID `RF-00301` Paired; Tag RFID `RF-00601` Reserved (dipegang aset Draft); Tag RFID `RF-00602` Retired; Tag RFID `RF-00603` Damaged/Missing.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: tidak ada yang diubah (spec hanya membaca); tidak ada Replace yang di-submit sehingga stok Tag per tipe di registri Global dan status Tag tidak berubah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-294: Tag pengganti berstatus Paired di aset lain ditolak V-07

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00301` dengan reader
5. Verifikasi error inline "RF-00301 is not available (Paired)."
6. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-295: Tag pengganti berstatus Reserved ditolak V-07

7. Klik [Cancel] pada dialog Replace TAG
8. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
9. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
10. Pindai Tag `RF-00601` dengan reader
11. Verifikasi error inline "RF-00601 is not available (Reserved)."
12. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-296: Tag pengganti RFID berstatus Retired ditolak V-07

13. Klik [Cancel] pada dialog Replace TAG
14. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
16. Pindai Tag `RF-00602` dengan reader
17. Verifikasi error inline "RF-00602 is not available (Retired)."
18. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-297: Tag pengganti berstatus Damaged/Missing ditolak V-07

19. Klik [Cancel] pada dialog Replace TAG
20. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
21. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
22. Pindai Tag `RF-00603` dengan reader
23. Verifikasi error inline "RF-00603 is not available (Damaged/Missing)."
24. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-293: Slot Replacement TAG menampilkan kode terpindai dan badge Verified

25. Klik [Cancel] pada dialog Replace TAG
26. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
27. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
28. Pindai Tag `RF-00412` dengan reader
29. Verifikasi slot `RFID TAG` menampilkan kode `RF-00412`
30. Verifikasi slot `RFID TAG` menampilkan badge `Verified`
31. Klik [Cancel] pada dialog Replace TAG
32. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
33. Klik [Discard]

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC; TC-FA-TAG-293 dipindah ke akhir karena menyisakan slot terisi (dirty), ditutup lewat [Cancel], verifikasi dialog `Discard Replacement`, dan [Discard].
- Pembagian TC lintas spec: TC-FA-TAG-298 sampai 302 ada di spec 066 dan TC-FA-TAG-303 sampai 306 ada di spec 067.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Post Condition 'Tidak ada data yang berubah' pada TC-FA-TAG-294 sampai 297 tidak punya langkah observasi dan tidak diasersi.
