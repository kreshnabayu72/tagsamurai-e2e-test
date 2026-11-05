---
id: TC-FA-TAG-E2E-082-replace-tag-combined-slot-validasi-v-25-v-26-dan-submit-bagian-2
title: "Replace dengan Tag Combined: Pindai Mengisi Semua Slot Komponen dan Penolakan Pola Tidak Cocok, Komponen Tidak Dikenal, Reserved, User TAG, atau Tidak Berlaku"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-357
  - TC-FA-TAG-358
  - TC-FA-TAG-361
  - TC-FA-TAG-362
  - TC-FA-TAG-363
  - TC-FA-TAG-364
  - TC-FA-TAG-355
coverage:
  web: automated
---

# Replace dengan Tag Combined: Pindai Mengisi Semua Slot Komponen dan Penolakan Pola Tidak Cocok, Komponen Tidak Dikenal, Reserved, User TAG, atau Tidak Berlaku

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Laptop Pro 14 - 8' (AST-0108, Group Plant A, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00292` dan Tag QR `QR-00300` Paired, bertipe sesuai. Tag combined (satu unit, status Available): NFC+QR `NF-00810` / `QR-00810`; RFID+QR `RF-00811` / `QR-00811`; RFID+NFC+QR `RF-00812` / `NF-00812` / `QR-00812`; Combined RFID+QR `RF-00813` dengan komponen QR `QR-09801` yang tidak dikenal registri; Combined RFID+QR `RF-00814` dengan komponen QR `QR-00814` berstatus Reserved; Combined RFID+NFC `RF-00815` / `NF-00815` dengan komponen NFC `NF-00815` yang merupakan User TAG; Combined RFID+QR `RF-00816` dengan komponen QR `QR-00816` tidak berlaku di client ini.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: tidak ada yang diubah (spec hanya membaca); tidak ada Replace yang di-submit sehingga stok Tag per tipe di registri Global dan status Tag tidak berubah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-357: Tag combined dengan pola tidak sesuai slot terbuka ditolak V-26

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
3. Centang baris `NF-00292` dan baris `QR-00300`
4. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
5. Pindai Tag `RF-00811` dengan reader
6. Verifikasi error inline "This combined TAG doesn't match the open slots."
7. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Not scanned`

### TC-FA-TAG-358: Tag combined dengan komponen lebih banyak daripada slot terbuka ditolak V-26

8. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
9. Pindai Tag `RF-00812` dengan reader
10. Verifikasi error inline "This combined TAG doesn't match the open slots."
11. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Not scanned`

### TC-FA-TAG-361: Tag combined yang komponen tidak dikenal menolak seluruh scan tanpa slot terisi sebagian

12. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
13. Pindai Tag `RF-00813` dengan reader
14. Verifikasi error inline "Error, can't recognize TAG." untuk komponen yang gagal
15. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Not scanned` (tidak ada slot terisi sebagian)

### TC-FA-TAG-362: Tag combined yang komponen berstatus Reserved menolak seluruh scan tanpa slot terisi sebagian

16. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
17. Pindai Tag `RF-00814` dengan reader
18. Verifikasi error inline "QR-00814 is not available (Reserved)." untuk komponen yang gagal
19. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Not scanned` (tidak ada slot terisi sebagian)

### TC-FA-TAG-363: Tag combined yang komponen User TAG menolak seluruh scan tanpa slot terisi sebagian

20. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
21. Pindai Tag `RF-00815` dengan reader
22. Verifikasi error inline "This is a user TAG. Scan an asset TAG." untuk komponen yang gagal
23. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Not scanned` (tidak ada slot terisi sebagian)

### TC-FA-TAG-364: Tag combined yang komponen tidak berlaku di client ini menolak seluruh scan tanpa slot terisi sebagian

24. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
25. Pindai Tag `RF-00816` dengan reader
26. Verifikasi error inline "Error, TAG isn't authorized. Please contact Admin." untuk komponen yang gagal
27. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Not scanned` (tidak ada slot terisi sebagian)

### TC-FA-TAG-355: Tag combined sesuai dua slot mengisi semua slot komponen dalam satu pindaian

28. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
29. Pindai Tag `NF-00810` dengan reader
30. Verifikasi slot `NFC TAG` menampilkan tanda centang dan badge `Verified` dari satu pindaian
31. Verifikasi slot `QR TAG` menampilkan tanda centang dan badge `Verified` dari satu pindaian
32. Verifikasi tidak ada error inline
33. Klik [Cancel] pada dialog Replace TAG
34. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
35. Klik [Discard]

## Notes

- Langkah penghubung (S-03): Tujuh TC memakai dialog yang sama: sesudah penolakan kedua slot kembali `Not scanned` sehingga keadaan awalnya identik dengan keadaan awal TC berikutnya (baris `NF-00292` dan `QR-00300` tercentang), dan TC berikutnya hanya mengulang klik ButtonScan dan pindai; TC-FA-TAG-355 berada di akhir karena menyisakan slot terisi (dirty), ditutup lewat [Cancel], verifikasi dialog `Discard Replacement`, dan [Discard].
- Pembagian TC lintas spec: TC-FA-TAG-356, 359, dan 360 ada di spec 081 dan TC-FA-TAG-366 sampai 370 ada di spec 083.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC-FA-TAG-361 sampai 364 menyebut kode combined `RF-00813` sampai `RF-00816` dengan komponen QR/NFC bermasalah tetapi tidak menyatakan kode komponen lain yang membentuk unit combined yang sama; spec mengikuti data TC apa adanya (kode combined yang dipindai).
  - TC-FA-TAG-362 dan 364 menyebut combined 'RFID+QR' yang dipindai pada slot NFC sementara Expected hanya menyebut komponen QR yang gagal; spec mengikuti Expected TC.
  - Tidak ada Post Condition berobservasi: 'Tidak ada data yang berubah' pada TC-FA-TAG-357, 358, dan 361 sampai 364 tidak punya langkah observasi dan tidak diasersi.
