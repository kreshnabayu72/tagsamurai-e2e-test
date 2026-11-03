---
id: TC-FA-TAG-E2E-140-print-qr-dari-slot-qr-dialog-pair-tag-menutup-lapisan-print-qr
title: "Print QR dari slot QR Dialog Pair TAG: lapisan di atas dialog dan penutupan mengembalikan isian"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-504
coverage:
  web: automated
---

# Print QR dari slot QR Dialog Pair TAG: lapisan di atas dialog dan penutupan mengembalikan isian

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada):
  - Aset `Server Rack 42U - 101` (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR) belum punya Tag Paired (Not Paired Yet).
  - Tag RFID `RF-00412` Available.
  - Kode QR `QR-00700` berstatus Available (dibuat backend saat Start Print sebelumnya, belum Paired); dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader).

## Test Steps

1. Klik Asset Name `Server Rack 42U` pada baris grup Plant A.
2. Klik `Show` di samping `Not Paired Yet`.
3. Klik row action `Pair TAG` pada baris `Server Rack 42U - 101`.
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`.
5. Klik tombol `Print QR` pada slot `QR TAG`.
6. Verifikasi Dialog Print QR tampil di atas Dialog Pair TAG.
7. Klik ikon close pada Dialog Print QR.
8. Verifikasi Dialog Print QR menutup.
9. Verifikasi Dialog Pair TAG masih terbuka.
10. Verifikasi slot `RFID TAG` menampilkan `RF-00412`.
11. Verifikasi slot `RFID TAG` berbadge `Verified`.
12. Verifikasi dialog konfirmasi D-11 tidak tampil.
13. Klik ikon close (✕) pada Dialog Pair TAG.
14. Verifikasi dialog `Unsaved Changes` tampil.
15. Klik [Leave].
16. Tutup Popup Detail.

## Notes

- Langkah penghubung: langkah 13 sampai 16 menutup Dialog Pair TAG yang dirty dan Popup Detail. Langkah 9 menjadi anchor absence langkah 12.
- Pembagian TC lintas spec: TC-503, TC-505, TC-506 ada di spec 125; TC-507 dan TC-1443 ada di spec 126.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`Server Rack 42U - 101`, AST-0101, `RF-00412`, `QR-00700`) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Precondition d TC-504 (`QR-00700`) tidak dipakai pada langkah TC.
