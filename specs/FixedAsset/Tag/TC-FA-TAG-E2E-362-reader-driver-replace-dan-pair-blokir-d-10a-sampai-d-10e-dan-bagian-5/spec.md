---
id: TC-FA-TAG-E2E-362-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-5
title: "Kondisi Reader: Banner Reader Terputus di Dialog Pair TAG dan Urutan Pemeriksaan Reader Sebelum Driver"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-529
  - TC-FA-TAG-530
coverage:
  web: automated
---

# Kondisi Reader: Banner Reader Terputus di Dialog Pair TAG dan Urutan Pemeriksaan Reader Sebelum Driver

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): emulator driver reader (simulator reader USB, lihat `suite.md`) yang mengatur kondisi reader: diputus koneksinya setelah dialog dibuka; reader tidak tersambung sekaligus driver reader lokal tidak terdeteksi; kondisi normal (satu reader RFID/NFC tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader). Seed idempotent aset dan Tag lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0051 'Excavator 20 Ton - 51' (Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet); Tag RFID `RF-00412` berstatus Available; AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00330` berstatus Paired. Spec ini tidak mengubah data.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader ke normal. Spec ini tidak mengubah state global lain. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-529: Dialog Pair TAG saat reader terputus

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
2. Klik `Show` di samping `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
4. Putuskan koneksi reader
5. Verifikasi banner Alert warning "Connect a TAG reader to scan." tampil di dialog
6. Verifikasi tombol `Scan RFID` tetap tampil namun Disabled
7. Klik `✕` pada Dialog Pair TAG
8. Tutup Popup Detail

### TC-FA-TAG-530: reader tidak terhubung lebih dulu daripada driver

9. Atur kondisi reader: reader tidak tersambung ke komputer dan driver reader lokal tidak terdeteksi
10. Arahkan kursor ke tombol scan `Replace TAG` di toolbar tab Paired
11. Verifikasi tombol `Replace TAG` Disabled dengan tooltip "Connect a TAG reader to replace."
12. Klik tombol scan `Replace TAG` di toolbar tab Paired
13. Verifikasi dialog D-10a tidak tampil

## Notes

- Spec harness eksternal simulator reader (kelas d); objek uji adalah kondisi reader.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 sampai 3 (membuka Popup Detail dan Dialog Pair TAG), 4 dan 9 (mengatur kondisi reader), 7 dan 8 (menutup dialog yang tidak dirty dan popup), 10 (hover), 12 (klik yang menjadi pemicu asersi absence).
- Anchor positif absence (bagian 8b butir 2): langkah 11 (tombol Disabled dengan tooltip tampil) mendahului asersi dialog D-10a tidak tampil pada langkah 13.
- Pembagian TC lintas spec: TC-FA-TAG-508 sampai TC-FA-TAG-514 ada di spec 358, TC-FA-TAG-515 sampai TC-FA-TAG-519 di spec 359, TC-FA-TAG-520 sampai TC-FA-TAG-523 di spec 360, TC-FA-TAG-524 sampai TC-FA-TAG-528 di spec 361.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-529 tidak menyebut Dialog Pair TAG menjadi dirty atau tidak; karena tidak ada kode yang dipindai, spec menutupnya dengan `✕` tanpa dialog `Unsaved Changes`.
  - TC-FA-TAG-530 tidak menyebut dialog D-10a dengan judul dan isi; spec hanya mengasersi dialog D-10a tidak tampil seperti Expected b.
