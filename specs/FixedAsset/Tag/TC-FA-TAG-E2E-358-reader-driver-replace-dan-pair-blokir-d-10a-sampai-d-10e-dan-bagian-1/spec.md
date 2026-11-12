---
id: TC-FA-TAG-E2E-358-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-1
title: "Kondisi Reader: Tombol Replace TAG Disabled dan Dialog Blok D-10a sampai D-10e pada Toolbar dan Row Action"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-508
  - TC-FA-TAG-509
  - TC-FA-TAG-510
  - TC-FA-TAG-511
  - TC-FA-TAG-512
  - TC-FA-TAG-513
  - TC-FA-TAG-514
coverage:
  web: automated
---

# Kondisi Reader: Tombol Replace TAG Disabled dan Dialog Blok D-10a sampai D-10e pada Toolbar dan Row Action

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): emulator driver reader (simulator reader USB, lihat `suite.md`) yang mengatur kondisi reader: tidak tersambung ke komputer; driver reader lokal tidak terdeteksi; driver terpasang tetapi reader mati atau kabel tidak terpasang erat; dua reader tersambung bersamaan; reader terbaca tetapi Serial Number belum diaktivasi ([Sync] belum dijalankan) di Global Settings > Handheld Reader; reader berstatus Waiting for Approval. Seed idempotent aset lewat fixture backend.
- Data aset (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00330` berstatus Paired. Spec ini tidak mengubah data aset.
- Tabel 1 (parameter langkah 7 sampai 12):

| TC | Kondisi reader | Isi dialog blok |
|---|---|---|
| TC-FA-TAG-509 | Driver reader lokal tidak terdeteksi | USB driver not detected. Please install the reader driver software. |
| TC-FA-TAG-510 | Driver terpasang tetapi reader mati atau kabel tidak terpasang erat | Reader not responding. Ensure device is powered on and cable connected securely. |
| TC-FA-TAG-511 | Dua reader tersambung bersamaan | Connect only one reader at a time. |
| TC-FA-TAG-512 | Reader terbaca tetapi Serial Number belum diaktivasi ([Sync] belum dijalankan) | This reader is not activated. Activate it in Global Settings > Handheld Reader first. |
| TC-FA-TAG-513 | Reader berstatus Waiting for Approval | This reader is waiting for approval. Try again after it is approved. |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader ke normal (satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan). Spec ini tidak mengubah state global lain. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-508: reader tidak tersambung

1. Atur kondisi reader: reader tidak tersambung ke komputer
2. Arahkan kursor ke tombol scan `Replace TAG` di toolbar tab Paired
3. Verifikasi tombol `Replace TAG` tetap tampil (visible) namun berstatus Disabled
4. Verifikasi tooltip "Connect a TAG reader to replace." tampil
5. Klik tombol scan `Replace TAG` di toolbar tab Paired
6. Verifikasi klik tidak membuka overlay scan

### TC-FA-TAG-509 sampai TC-FA-TAG-513: dialog blok toolbar

Untuk setiap baris Tabel 1 (langkah 7 sampai 12):

7. Atur kondisi reader sesuai kolom Kondisi reader
8. Verifikasi tombol scan `Replace TAG` di toolbar Enabled (tidak Disabled)
9. Klik tombol scan `Replace TAG` di toolbar tab Paired
10. Verifikasi dialog judul "Cannot Replace TAG", body sesuai kolom Isi dialog blok, tombol [OK]
11. Verifikasi overlay scan dan Dialog Replace TAG tidak terbuka
12. Klik [OK]

### TC-FA-TAG-514: row action dengan driver belum terpasang

13. Atur kondisi reader: driver reader lokal tidak terdeteksi
14. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
15. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
16. Verifikasi dialog judul "Cannot Replace TAG", body "USB driver not detected. Please install the reader driver software.", tombol [OK]
17. Verifikasi Dialog Replace TAG tidak terbuka
18. Klik [OK]

## Notes

- Spec harness eksternal simulator reader (kelas d); objek uji adalah kondisi reader.
- Langkah yang diulang per baris tabel (bagian 8b butir 7): 7 sampai 12. Parameter tiap iterasi ada di Tabel 1 pada `## Prerequisites`; `Verifikasi` yang diulang tetap satu per klausa (S-01). Ekspansi: 6 + 5 x 6 + 6 = 42 langkah.
- Alasan melewati sekitar 35 langkah (bagian 3 prinsip 13): semua blok berada pada satu kelas harness (kondisi reader pada permukaan Replace TAG) dan berdiri sendiri; kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna karena tiap iterasi mengatur kondisi reader sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1, 7, 13 (mengatur kondisi reader), 2 (hover), 12 dan 18 (menutup dialog blok lewat [OK]), 14 (membuka Popup Detail).
- Anchor positif absence (bagian 8b butir 2): langkah 3 dan 4 untuk langkah 6; langkah 10 untuk langkah 11; langkah 16 untuk langkah 17 (dialog blok tampil sebagai anchor).
- Pembagian TC lintas spec: TC-FA-TAG-515 sampai TC-FA-TAG-519 ada di spec 359, TC-FA-TAG-520 sampai TC-FA-TAG-523 di spec 360, TC-FA-TAG-524 sampai TC-FA-TAG-528 di spec 361, TC-FA-TAG-529 dan TC-FA-TAG-530 di spec 362.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-509 sampai TC-FA-TAG-513 menyebut "Tidak ada kode terbaca dan tidak ada perubahan data" sebagai Post Condition tanpa langkah observasi; tidak diasersi.
  - TC-FA-TAG-508 tidak menyebut cara membuat kondisi "Reader tidak tersambung" selain precondition; spec memakai emulator driver reader seperti TC lain.
