---
id: TC-FA-TAG-E2E-360-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-3
title: "Kondisi Reader: Alert Error Inline Scan Current TAG di Dialog Replace TAG untuk Reader Mati, Dua Reader, Belum Sinkron, dan Waiting for Approval"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-520
  - TC-FA-TAG-521
  - TC-FA-TAG-522
  - TC-FA-TAG-523
coverage:
  web: automated
---

# Kondisi Reader: Alert Error Inline Scan Current TAG di Dialog Replace TAG untuk Reader Mati, Dua Reader, Belum Sinkron, dan Waiting for Approval

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): emulator driver reader (simulator reader USB, lihat `suite.md`) yang mengatur kondisi reader di tengah dialog: driver terpasang tetapi reader mati atau kabel tidak terpasang erat; dua reader tersambung bersamaan; reader terbaca tetapi Serial Number belum diaktivasi ([Sync] belum dijalankan) di Global Settings > Handheld Reader; reader berstatus Waiting for Approval; kondisi awal normal (satu reader RFID/NFC tersambung, driver terpasang, reader aktif, sudah disinkronkan). Seed idempotent aset lewat fixture backend.
- Data aset (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00330` berstatus Paired. Spec ini tidak mengubah data aset.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader ke normal. Spec ini tidak mengubah state global lain. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'

### TC-FA-TAG-520: reader tidak merespons

3. Ubah kondisi reader: driver terpasang tetapi reader mati atau kabel tidak terpasang erat
4. Klik ButtonScan `Scan RFID` pada baris `RF-00330`
5. Verifikasi Alert error inline pada dialog berisi "Reader not responding. Ensure device is powered on and cable connected securely."
6. Verifikasi tidak ada kode yang terbaca dan baris `RF-00330` tetap berbadge `Not scanned`
7. Verifikasi dialog blok tidak tampil

### TC-FA-TAG-521: lebih dari satu reader

8. Ubah kondisi reader: dua reader tersambung bersamaan
9. Klik ButtonScan `Scan RFID` pada baris `RF-00330`
10. Verifikasi Alert error inline pada dialog berisi "Connect only one reader at a time."
11. Verifikasi tidak ada kode yang terbaca dan baris `RF-00330` tetap berbadge `Not scanned`
12. Verifikasi dialog blok tidak tampil

### TC-FA-TAG-522: reader belum sinkron

13. Ubah kondisi reader: reader terbaca tetapi Serial Number belum diaktivasi ([Sync] belum dijalankan)
14. Klik ButtonScan `Scan RFID` pada baris `RF-00330`
15. Verifikasi Alert error inline pada dialog berisi "This reader is not activated. Activate it in Global Settings > Handheld Reader first."
16. Verifikasi tidak ada kode yang terbaca dan baris `RF-00330` tetap berbadge `Not scanned`
17. Verifikasi dialog blok tidak tampil

### TC-FA-TAG-523: reader menunggu approval

18. Ubah kondisi reader: reader berstatus Waiting for Approval
19. Klik ButtonScan `Scan RFID` pada baris `RF-00330`
20. Verifikasi Alert error inline pada dialog berisi "This reader is waiting for approval. Try again after it is approved."
21. Verifikasi tidak ada kode yang terbaca dan baris `RF-00330` tetap berbadge `Not scanned`
22. Verifikasi dialog blok tidak tampil

## Notes

- Spec harness eksternal simulator reader (kelas d); objek uji adalah kondisi reader.
- Langkah 1 dan 2 dilakukan sekali karena Dialog Replace TAG tetap terbuka di antara TC (tidak ada pindaian sukses, jadi dialog tidak dirty). Langkah penghubung (tanpa awalan `Verifikasi`): 1 dan 2 (membuka Popup Detail dan dialog), 3, 8, 13, 18 (mengubah kondisi reader pada TC; menjadi bagian dari langkah TC, bukan asersi).
- Anchor positif absence (bagian 8b butir 2): Alert error inline pada langkah 5, 10, 15, 20 mendahului asersi absence dialog blok pada langkah 7, 12, 17, 22.
- Pembagian TC lintas spec: TC-FA-TAG-508 sampai TC-FA-TAG-514 ada di spec 358, TC-FA-TAG-515 sampai TC-FA-TAG-519 di spec 359, TC-FA-TAG-524 sampai TC-FA-TAG-528 di spec 361, TC-FA-TAG-529 dan TC-FA-TAG-530 di spec 362.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-520 sampai TC-FA-TAG-523 menyebut "Tidak ada perubahan data" sebagai Post Condition tanpa langkah observasi; tidak diasersi.
  - TC-FA-TAG-521 sampai TC-FA-TAG-523 mengulang langkah 1 dan 2 serta kondisi awal reader normal pada precondition; spec memakai dialog yang sama dan mengubah kondisi reader langsung dari kondisi TC sebelumnya.
