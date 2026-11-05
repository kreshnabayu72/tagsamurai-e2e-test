---
id: TC-FA-TAG-E2E-066-dialog-replace-tag-scan-tag-pengganti-penolakan-v-07-v-08-v-23-bagian-2
title: "Dialog Replace TAG: Scan Tag Pengganti, Penolakan Waiting for Approval, Tidak Dikenal, QR Tidak Pernah Dicetak, dan User TAG (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-298
  - TC-FA-TAG-299
  - TC-FA-TAG-300
  - TC-FA-TAG-301
  - TC-FA-TAG-302
coverage:
  web: automated
---

# Dialog Replace TAG: Scan Tag Pengganti, Penolakan Waiting for Approval, Tidak Dikenal, QR Tidak Pernah Dicetak, dan User TAG (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00330` Paired; 'Label Printer - 72' (AST-0172, TAG Type Asset Name QR) dengan Tag QR `QR-00290` Paired; Tag RFID `RF-00604` Waiting for Approval; kode `RF-09999` belum diaktivasi di Global; kode `QR-09999` tidak pernah dibuat lewat Start Print; Tag QR `QR-00700` Available (dibuat backend saat Start Print sebelumnya, belum Paired); User TAG `UT-00010` terdaftar di Global dan berlaku di client ini.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: tidak ada yang diubah (spec hanya membaca); tidak ada Replace yang di-submit sehingga stok Tag per tipe di registri Global dan status Tag tidak berubah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-298: Tag pengganti berstatus Waiting for Approval ditolak V-07

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00604` dengan reader
5. Verifikasi error inline "RF-00604 is not available (Waiting for Approval)."
6. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-299: Tag pengganti tidak dikenal ditolak V-23

7. Klik [Cancel] pada dialog Replace TAG
8. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
9. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
10. Pindai Tag `RF-09999` dengan reader
11. Verifikasi error inline "Error, can't recognize TAG."
12. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-302: Tag pengganti User TAG ditolak V-24

13. Klik [Cancel] pada dialog Replace TAG
14. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
16. Pindai Tag `UT-00010` dengan reader
17. Verifikasi error inline "This is a user TAG. Scan an asset TAG."
18. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-300: Kode QR yang tidak pernah dicetak ditolak V-23 pada slot QR

19. Klik [Cancel] pada dialog Replace TAG
20. Tutup Popup Detail Assets
21. Klik Asset Name 'Label Printer' pada baris grup Plant A untuk membuka Popup Detail
22. Klik row action `Replace TAG` pada baris 'Label Printer - 72'
23. Klik ButtonScan `Scan QR` pada slot `QR TAG`
24. Pindai Tag `QR-09999` dengan reader
25. Verifikasi error inline "Error, can't recognize TAG."
26. Verifikasi slot `QR TAG` tetap `Not scanned`

### TC-FA-TAG-301: Kode QR hasil Start Print diterima sebagai Tag Available pada slot QR

27. Klik [Cancel] pada dialog Replace TAG
28. Klik row action `Replace TAG` pada baris 'Label Printer - 72'
29. Klik ButtonScan `Scan QR` pada slot `QR TAG`
30. Pindai Tag `QR-00700` dengan reader
31. Verifikasi slot `QR TAG` menampilkan kode `QR-00700`
32. Verifikasi slot `QR TAG` menampilkan badge `Verified`
33. Verifikasi pesan "Error, can't recognize TAG." tidak tampil
34. Klik [Cancel] pada dialog Replace TAG
35. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
36. Klik [Discard]

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC; TC-FA-TAG-300 dan 301 dipindah ke akhir karena memakai Popup 'Label Printer' dan slot QR, sedangkan tiga TC lain memakai Popup 'Excavator 20 Ton'; TC-FA-TAG-301 menyisakan slot terisi (dirty) sehingga ditutup lewat [Cancel], verifikasi dialog `Discard Replacement`, dan [Discard].
- Pembagian TC lintas spec: TC-FA-TAG-293 sampai 297 ada di spec 065 dan TC-FA-TAG-303 sampai 306 ada di spec 067.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Alasan di atas sekitar 35 langkah: semua blok satu kelas (fungsional, penolakan scan), satu dialog dan dataset aset yang sama; lima TC berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; tambahan langkah berasal dari penghubung antar-TC.
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Post Condition 'Tidak ada data yang berubah' pada TC-FA-TAG-298 sampai 300 dan 302 tidak punya langkah observasi dan tidak diasersi.
