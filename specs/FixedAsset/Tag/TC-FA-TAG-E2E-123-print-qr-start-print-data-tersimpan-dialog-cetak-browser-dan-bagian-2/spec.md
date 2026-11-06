---
id: TC-FA-TAG-E2E-123-print-qr-start-print-data-tersimpan-dialog-cetak-browser-dan-bagian-2
title: "Print QR: membatalkan dialog cetak browser tidak membatalkan kode QR yang sudah dibuat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-498
coverage:
  web: automated
---

# Print QR: membatalkan dialog cetak browser tidak membatalkan kode QR yang sudah dibuat

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (precondition TC-498 butir c, pengecualian S-06/S-12 butir A-15): aset 'Label Printer - 71' (AST-0171, Group Plant A, TAG Type Asset Name QR saja) belum punya Tag Paired (Not Paired Yet); dipakai tanpa suffix `{runId}` karena nama aset menjadi objek langkah; aset hanya dibuka di Dialog Pair TAG lalu ditutup lewat Discard Pairing tanpa [Submit], sehingga tidak diubah; seeding idempotent dan pemulihan lewat fixture backend (fixture `fixed-asset-tag.json` belum ada).
- Kemampuan teknis (disediakan tim FE/BE):
  - Dialog cetak browser (tingkat OS) yang teramati dan dibatalkan oleh harness.
  - Pembacaan kode QR hasil Start Print dari registri Global lewat fixture backend, untuk dipindai pada langkah 11.
  - Simulator reader RFID/NFC USB: satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader.
- Efek yang tidak terpulihkan: batch kode QR dari `Start Print` (sebanyak Quantity, terdaftar `Available` di registri Global) beserta data cetak (langkah 3).

## Test Steps

1. Klik tombol `Print QR` di toolbar tab Paired.
2. Isi `Quantity` dengan 2.
3. Klik [Start Print].
4. Batalkan dialog cetak browser.
5. Verifikasi Dialog Print QR menutup.
6. Verifikasi tombol `Print QR` tampil di toolbar tab Paired.
7. Verifikasi tidak ada pencetakan ulang otomatis (dialog cetak browser tidak terbuka lagi).
8. Klik Asset Name 'Label Printer' pada baris grup Plant A untuk membuka Popup Detail.
9. Klik `Show` di samping `Not Paired Yet`.
10. Klik row action `Pair TAG` pada baris 'Label Printer - 71'.
11. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai salah satu kode QR hasil cetak.
12. Verifikasi slot `QR TAG` pada Dialog Pair TAG menampilkan kode QR hasil cetak.
13. Verifikasi slot `QR TAG` menampilkan badge `Verified`.
14. Verifikasi pesan "Error, can't recognize TAG." tidak tampil.
15. Klik ikon close (✕) pada Dialog Pair TAG.
16. Verifikasi dialog `Discard Pairing` dengan body "Discard this pairing? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil.
17. Klik [Discard].
18. Tutup Popup Detail.

## Notes

- Langkah penghubung: langkah 15 sampai 18 menutup Dialog Pair TAG yang dirty dan Popup Detail.
- Anchor positif (S-03): langkah 6 menjadi anchor absence di langkah 7; anchor itu tidak ada di Expected TC.
- A-15: aset Pre-setup 'Label Printer - 71' dipakai tanpa suffix `{runId}` (nama aset menjadi objek langkah); Pair TAG tidak di-Submit karena Dialog Pair TAG ditutup lewat Discard Pairing, sehingga aset tidak diubah.
- Temuan untuk QA:
  - Post Condition "Kode QR tetap tersimpan di backend" tidak punya langkah observasi di TC (hanya terobservasi lewat penerimaan di slot QR) dan tidak diasersi terpisah.
