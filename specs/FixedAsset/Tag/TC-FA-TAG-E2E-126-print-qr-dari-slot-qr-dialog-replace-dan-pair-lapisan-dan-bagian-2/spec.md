---
id: TC-FA-TAG-E2E-126-print-qr-dari-slot-qr-dialog-replace-dan-pair-lapisan-dan-bagian-2
title: "Print QR: Esc menutup lapisan paling atas dan kode QR hasil cetak diterima di Dialog Pair TAG"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-507
  - TC-FA-TAG-1443
coverage:
  web: automated
---

# Print QR: Esc menutup lapisan paling atas dan kode QR hasil cetak diterima di Dialog Pair TAG

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada):
  - Aset `Label Printer - 72` (AST-0172, Group Plant A, TAG Type Asset Name QR) punya satu Tag QR `QR-00290` berstatus Paired.
  - Aset `Label Printer - 71` (AST-0171, Group Plant A, TAG Type Asset Name QR saja) belum punya Tag Paired (Not Paired Yet).
  - Kode QR `QR-00700` berstatus Available (dibuat backend saat Start Print sebelumnya, belum Paired).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader).
- State global yang dipulihkan: Tag `QR-00700` yang dipasang ke `Label Printer - 71` pada langkah 19 dikembalikan ke Available dan `Label Printer - 71` ke Not Paired Yet lewat fixture backend di hook `after`.

## Test Steps

1. Klik Asset Name `Label Printer` pada baris grup Plant A untuk membuka Popup Detail.

### TC-1443: Esc pada Dialog Print QR di atas Dialog Replace TAG

2. Klik row action `Replace TAG` pada baris `Label Printer - 72`.
3. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai kode `QR-00700`.
4. Klik tombol `Print QR` pada slot `QR TAG`.
5. Tekan Esc.
6. Verifikasi Dialog Print QR menutup.
7. Verifikasi Dialog Replace TAG masih terbuka.
8. Verifikasi slot `QR TAG` menampilkan `QR-00700`.
9. Verifikasi slot `QR TAG` berbadge `Verified`.
10. Klik ikon close (✕) pada Dialog Replace TAG.
11. Verifikasi dialog `Unsaved Changes` tampil.
12. Klik [Leave].

### TC-507: Kode QR hasil cetak dipindai di Dialog Pair TAG

13. Klik `Show` di samping `Not Paired Yet`.
14. Klik row action `Pair TAG` pada baris `Label Printer - 71`.
15. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai kode `QR-00700`.
16. Verifikasi slot `QR TAG` menampilkan `QR-00700`.
17. Verifikasi slot `QR TAG` berbadge `Verified`.
18. Verifikasi tidak ada pesan "Error, can't recognize TAG."
19. Klik [Submit].
20. Verifikasi Toast "Success, TAG has been paired."
21. Tutup Popup Detail.

## Notes

- Urutan TC diubah menjadi TC-1443 lalu TC-507: TC-507 memasang `QR-00700` ke `Label Printer - 71` sehingga kode itu tidak lagi Available untuk TC-1443 (S-10). Popup Detail dibuka sekali di langkah 1 untuk keduanya.
- Langkah penghubung: langkah 10 sampai 12 menutup Dialog Replace TAG yang dirty; langkah 21 menutup Popup Detail.
- Anchor absence langkah 18: langkah 16 dan 17 (slot terisi dan terverifikasi).
- Pembagian TC lintas spec: TC-503, TC-505, TC-506 ada di spec 125; TC-504 ada di spec 140.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`Label Printer - 71`, `Label Printer - 72`, AST-0171, AST-0172, `QR-00290`, `QR-00700`) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Post Condition TC-507 ("Tag `QR-00700` Paired pada `Label Printer - 71`") tidak punya langkah observasi di TC dan tidak diasersi.
