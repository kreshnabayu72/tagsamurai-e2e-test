---
id: TC-FA-TAG-E2E-359-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-2
title: "Kondisi Reader: Dialog Blok Batch Replace dan Pair TAG serta Alert Error Inline Scan Current TAG"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-515
  - TC-FA-TAG-516
  - TC-FA-TAG-517
  - TC-FA-TAG-518
  - TC-FA-TAG-519
coverage:
  web: automated
---

# Kondisi Reader: Dialog Blok Batch Replace dan Pair TAG serta Alert Error Inline Scan Current TAG

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): emulator driver reader (simulator reader USB, lihat `suite.md`) yang mengatur kondisi reader: driver reader lokal tidak terdeteksi; driver terpasang tetapi reader mati; dua reader tersambung bersamaan; reader terbaca tetapi Serial Number belum diaktivasi ([Sync] belum dijalankan) di Global Settings > Handheld Reader; kondisi normal (satu reader RFID/NFC tersambung, driver terpasang, reader aktif, sudah disinkronkan). Seed idempotent aset lewat fixture backend.
- Data aset (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00330` berstatus Paired; AST-0051 'Excavator 20 Ton - 51' (Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet). Spec ini tidak mengubah data aset.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader ke normal. Spec ini tidak mengubah state global lain. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-515: Batch Replace dengan reader tidak merespons

1. Atur kondisi reader: driver terpasang tetapi reader mati
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
3. Centang baris 'Excavator 20 Ton - 220'
4. Klik Bulk `Batch Replace TAG`
5. Verifikasi dialog judul "Cannot Replace TAG", body "Reader not responding. Ensure device is powered on and cable connected securely.", tombol [OK]
6. Verifikasi Dialog Replace TAG tidak terbuka
7. Klik [OK]
8. Hapus centang baris 'Excavator 20 Ton - 220'

### TC-FA-TAG-516 sampai TC-FA-TAG-518: Pair TAG pada row action

9. Klik `Show` di samping `Not Paired Yet`
10. Atur kondisi reader: driver reader lokal tidak terdeteksi
11. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
12. Verifikasi dialog judul "Cannot Pair TAG", body "USB driver not detected. Please install the reader driver software.", tombol [OK]
13. Verifikasi Dialog Pair TAG tidak terbuka
14. Klik [OK]
15. Atur kondisi reader: dua reader tersambung bersamaan
16. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
17. Verifikasi dialog judul "Cannot Pair TAG", body "Connect only one reader at a time.", tombol [OK]
18. Verifikasi Dialog Pair TAG tidak terbuka
19. Klik [OK]
20. Atur kondisi reader: reader terbaca tetapi Serial Number belum diaktivasi ([Sync] belum dijalankan)
21. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
22. Verifikasi dialog judul "Cannot Pair TAG", body "This reader is not activated. Activate it in Global Settings > Handheld Reader first.", tombol [OK]
23. Klik [OK]

### TC-FA-TAG-519: Alert error inline pada Scan Current TAG

24. Atur kondisi reader: normal (satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan)
25. Tutup Popup Detail
26. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
27. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
28. Ubah kondisi reader: driver reader lokal tidak terdeteksi
29. Klik ButtonScan `Scan RFID` pada baris `RF-00330`
30. Verifikasi Alert error inline pada dialog berisi "USB driver not detected. Please install the reader driver software."
31. Verifikasi tidak ada kode yang terbaca dan baris `RF-00330` tetap berbadge `Not scanned`
32. Verifikasi dialog blok tidak tampil

## Notes

- Spec harness eksternal simulator reader (kelas d); objek uji adalah kondisi reader.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1, 10, 15, 20, 24, 28 (mengatur kondisi reader), 2, 3, 8 (membuka popup, memilih dan melepas baris), 9 (menampilkan daftar Not Paired Yet), 7, 14, 19, 23 (menutup dialog blok lewat [OK]), 25 dan 26 (menutup dan membuka kembali Popup Detail).
- Anchor positif absence (bagian 8b butir 2): langkah 5 untuk langkah 6; langkah 12 untuk 13; langkah 17 untuk 18; langkah 22 tanpa asersi dialog Pair tidak terbuka (tidak ada di Expected TC); langkah 30 untuk langkah 31 dan 32.
- Pembagian TC lintas spec: TC-FA-TAG-508 sampai TC-FA-TAG-514 ada di spec 358, TC-FA-TAG-520 sampai TC-FA-TAG-523 di spec 360, TC-FA-TAG-524 sampai TC-FA-TAG-528 di spec 361, TC-FA-TAG-529 dan TC-FA-TAG-530 di spec 362.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-516 sampai TC-FA-TAG-518 mengulang langkah buka `Show` di samping `Not Paired Yet` per TC; spec membukanya sekali (langkah 9) karena daftar tetap tampil di antara TC.
  - TC-FA-TAG-518 tidak menyebut Dialog Pair TAG tidak terbuka (hanya judul, body, dan [OK]) seperti TC-FA-TAG-516 dan TC-FA-TAG-517; spec mengikuti TC dan tidak mengasersinya.
  - TC-FA-TAG-515 sampai TC-FA-TAG-519 menyebut "Tidak ada perubahan data" sebagai Post Condition (TC-FA-TAG-519) tanpa langkah observasi; tidak diasersi.
