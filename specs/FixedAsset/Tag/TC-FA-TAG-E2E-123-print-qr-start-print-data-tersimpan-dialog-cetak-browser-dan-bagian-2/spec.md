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
- Data Dinamis (dibuat di hook `before`, dibersihkan di hook `after`):
  - Aset Not Paired Yet `Print QR Aset-{runId}-123` (TAG Type Asset Name QR) pada Group milik spec. Precondition TC tidak menyebut aset ini (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE):
  - Dialog cetak browser (tingkat OS) yang teramati dan dibatalkan oleh harness.
  - Pembacaan kode QR hasil Start Print dari registri Global lewat fixture backend, untuk dipindai pada langkah 11.
  - Simulator reader RFID/NFC USB: satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader.
  - Pembersihan kode QR hasil cetak dari registri Global lewat fixture backend.
- State global yang dipulihkan: dua kode QR yang dibuat spec ini dihapus dari registri Global di hook `after`.

## Test Steps

1. Klik tombol `Print QR` di toolbar tab Paired.
2. Isi `Quantity` dengan 2.
3. Klik [Start Print].
4. Batalkan dialog cetak browser.
5. Verifikasi Dialog Print QR menutup.
6. Verifikasi tombol `Print QR` tampil di toolbar tab Paired.
7. Verifikasi tidak ada pencetakan ulang otomatis (dialog cetak browser tidak terbuka lagi).
8. Klik Asset Name `Print QR Aset-{runId}-123` pada baris grupnya untuk membuka Popup Detail.
9. Klik `Show` di samping `Not Paired Yet`.
10. Klik row action `Replace TAG` pada baris aset `Print QR Aset-{runId}-123`.
11. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai salah satu kode QR hasil cetak.
12. Verifikasi kode QR hasil cetak diterima pada slot `QR TAG` sebagai Tag Available.
13. Klik ikon close (✕) pada Dialog Replace TAG.
14. Verifikasi dialog `Unsaved Changes` tampil.
15. Klik [Leave].
16. Tutup Popup Detail.

## Notes

- Langkah penghubung: langkah 13 sampai 16 menutup Dialog Replace TAG yang dirty dan Popup Detail.
- Anchor positif (S-03): langkah 6 menjadi anchor absence di langkah 7; anchor itu tidak ada di Expected TC.
- Temuan untuk QA:
  - Precondition TC-498 tidak menyebut aset Not Paired Yet, Group, maupun TAG Type Asset Name yang dipakai pada langkah 5 TC; spec memakai aset milik spec dengan TAG Type Asset Name QR (pilihan spec).
  - Langkah 5 TC memakai row action `Replace TAG` pada aset Not Paired Yet, sedangkan TC lain (TC-504, TC-507) memakai `Pair TAG` untuk aset Not Paired Yet; spec mengikuti TC.
  - Expected c TC-498 ("diterima sebagai Tag Available pada slot QR") tidak menyebut tampilan slot; spec memverifikasi sesuai kalimat TC.
  - TC-498 diberi label Manual Only karena dialog cetak browser tingkat OS; spec tetap memuatnya dengan kemampuan di Prerequisites.
  - Post Condition "Kode QR tetap tersimpan di backend" tidak punya langkah observasi di TC (hanya terobservasi lewat penerimaan di slot QR) dan tidak diasersi terpisah.
