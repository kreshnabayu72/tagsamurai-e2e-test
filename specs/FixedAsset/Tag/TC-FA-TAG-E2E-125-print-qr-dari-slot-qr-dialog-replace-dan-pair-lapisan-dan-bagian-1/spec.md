---
id: TC-FA-TAG-E2E-125-print-qr-dari-slot-qr-dialog-replace-dan-pair-lapisan-dan-bagian-1
title: "Print QR dari slot QR Dialog Replace TAG: lapisan di atas dialog, backdrop, Start Print, dan penutupan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-503
  - TC-FA-TAG-505
  - TC-FA-TAG-506
coverage:
  web: automated
---

# Print QR dari slot QR Dialog Replace TAG: lapisan di atas dialog, backdrop, Start Print, dan penutupan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend, dipulihkan di hook `before` dan `after`; fixture `fixed-asset-tag.json` belum ada):
  - Aset `Label Printer - 72` (AST-0172, Group Plant A, TAG Type Asset Name QR) punya satu Tag QR `QR-00290` berstatus Paired.
  - Kode QR `QR-00700` berstatus Available (dibuat backend saat Start Print sebelumnya, belum Paired).
- Kemampuan teknis (disediakan tim FE/BE):
  - Simulator reader RFID/NFC USB: satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader.
  - Dialog cetak browser (tingkat OS) yang teramati dan ditutup oleh harness.
- Nilai literal Pre-setup (`Label Printer - 72`, AST-0172, `QR-00290`, `QR-00700`) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: batch kode QR dari `Start Print` (sebanyak Quantity, terdaftar `Available` di registri Global) beserta data cetak (langkah 9).

## Test Steps

1. Klik Asset Name `Label Printer` pada baris grup Plant A untuk membuka Popup Detail.
2. Klik row action `Replace TAG` pada baris `Label Printer - 72`.

### TC-506: Klik backdrop pada Dialog Print QR dari Dialog Replace TAG

3. Klik tombol `Print QR` pada slot `QR TAG`.
4. Klik area backdrop di luar Dialog Print QR.
5. Verifikasi Dialog Print QR tetap terbuka di atas Dialog Replace TAG.
6. Klik [Cancel] pada Dialog Print QR.

### TC-505: Start Print dari Dialog Replace TAG

7. Klik tombol `Print QR` pada slot `QR TAG`.
8. Isi `Quantity` dengan 2.
9. Klik [Start Print].
10. Verifikasi Toast "Success, QR labels have been sent to print."
11. Tutup dialog cetak browser.
12. Verifikasi Dialog Print QR menutup.
13. Verifikasi Dialog Replace TAG tetap terbuka.
14. Verifikasi isian Dialog Replace TAG utuh.

### TC-503: Print QR dari slot QR setelah kode dipindai, lalu Cancel

15. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai kode `QR-00700`.
16. Klik tombol `Print QR` pada slot `QR TAG`.
17. Verifikasi Dialog Print QR tampil di atas Dialog Replace TAG.
18. Klik [Cancel] pada Dialog Print QR.
19. Verifikasi Dialog Print QR menutup.
20. Verifikasi Dialog Replace TAG masih terbuka.
21. Verifikasi slot `QR TAG` menampilkan `QR-00700`.
22. Verifikasi slot `QR TAG` berbadge `Verified`.
23. Klik ikon close (✕) pada Dialog Replace TAG.
24. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil.
25. Klik [Discard].
26. Tutup Popup Detail.

## Notes

- Urutan TC diubah menjadi TC-506, TC-505, TC-503: TC-506 dan TC-505 memakai Dialog Replace TAG yang belum terisi, sedangkan TC-503 memindai `QR-00700` sehingga dialog menjadi dirty dan harus ditutup lewat konfirmasi `Discard Replacement` (D-09) di akhir (S-10). Langkah 1 dan 2 dipakai ketiga TC dengan satu pembukaan Popup Detail dan Dialog Replace TAG.
- Langkah penghubung: langkah 6 dan 18 menutup Dialog Print QR; langkah 11 menutup dialog cetak browser; langkah 23 sampai 26 menutup Dialog Replace TAG yang dirty dan Popup Detail.
- Pembagian TC lintas spec: TC-504 ada di spec 140; TC-507 dan TC-1443 ada di spec 126.
- A-15: nilai literal Pre-setup (`Label Printer - 72`, AST-0172, `QR-00290`, `QR-00700`) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: batch kode QR dari `Start Print` (sebanyak Quantity, terdaftar `Available` di registri Global) beserta data cetak (langkah 9).
- Temuan untuk QA:
  - TC-505: Precondition tidak menyebut isian apa pun pada Dialog Replace TAG, sehingga "isian utuh" pada Expected b ambigu; spec memverifikasi sesuai kalimat TC.
  - Post Condition TC-505 ("Dua kode QR dibuat backend") tidak punya langkah observasi di TC dan tidak diasersi.
