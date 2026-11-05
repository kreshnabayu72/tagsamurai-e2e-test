---
id: TC-FA-TAG-E2E-363-reader-driver-receive-tag-blokir-dan-alert-inline-bagian-1
title: "Kondisi Reader: Tombol Receive TAG Disabled, Banner Reader Terputus, dan Dialog Blok D-10a sampai D-10d"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-550
  - TC-FA-TAG-551
  - TC-FA-TAG-552
  - TC-FA-TAG-553
  - TC-FA-TAG-554
  - TC-FA-TAG-555
coverage:
  web: automated
---

# Kondisi Reader: Tombol Receive TAG Disabled, Banner Reader Terputus, dan Dialog Blok D-10a sampai D-10d

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): emulator driver reader (simulator reader USB, lihat `suite.md`) yang mengatur kondisi reader: tidak ada reader tersambung; reader dicabut setelah dialog dibuka; driver reader USB belum terpasang; driver terpasang tetapi reader mati atau kabel tidak terpasang erat; lebih dari satu reader tersambung; reader terbaca tetapi Serial Number belum diaktivasi (Sync belum dijalankan); kondisi normal (satu reader RFID/NFC tersambung, aktif, sudah disinkronkan di Global Settings > Handheld Reader). Seed idempotent Tag To Be Returned lewat fixture backend.
- Data Pre-setup Tag To Be Returned (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.). Spec ini tidak menerima Tag, sehingga data tidak berubah.
- Tabel 1 (parameter langkah 14 sampai 21):

| TC | Kondisi reader | Isi dialog blok |
|---|---|---|
| TC-FA-TAG-552 | Driver reader USB belum terpasang di komputer | USB driver not detected. Please install the reader driver software. |
| TC-FA-TAG-553 | Driver terpasang tetapi reader mati atau kabel tidak terpasang erat | Reader not responding. Ensure device is powered on and cable connected securely. |
| TC-FA-TAG-554 | Lebih dari satu reader tersambung | Connect only one reader at a time. |
| TC-FA-TAG-555 | Reader terbaca tetapi Serial Number belum diaktivasi (Sync belum dijalankan) | This reader is not activated. Activate it in Global Settings > Handheld Reader first. |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader ke normal. Spec ini tidak mengubah state global lain. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Buka Fixed Asset > TAG > To Be Returned

### TC-FA-TAG-550: reader tidak terhubung

2. Atur kondisi reader: tidak ada reader yang tersambung ke komputer
3. Arahkan kursor ke tombol "Receive TAG" yang Disabled
4. Verifikasi tombol "Receive TAG" tetap tampil dalam keadaan Disabled
5. Verifikasi tooltip "Connect a TAG reader to scan." tampil
6. Klik tombol "Receive TAG"
7. Verifikasi dialog "Receive TAG" tidak terbuka

### TC-FA-TAG-551: reader terputus saat dialog terbuka

8. Atur kondisi reader: normal (satu reader RFID/NFC tersambung, aktif, sudah disinkronkan)
9. Klik tombol "Receive TAG"
10. Cabut reader dari komputer
11. Verifikasi Alert warning "Connect a TAG reader to scan." tampil di dalam dialog
12. Verifikasi ButtonScan "Scan TAG" tampil dalam keadaan Disabled
13. Klik `✕` pada Dialog Receive TAG

### TC-FA-TAG-552 sampai TC-FA-TAG-555: dialog blok

Untuk setiap baris Tabel 1 (langkah 14 sampai 21):

14. Atur kondisi reader sesuai kolom Kondisi reader
15. Verifikasi tombol "Receive TAG" Enabled
16. Klik tombol "Receive TAG"
17. Verifikasi dialog blok judul "Cannot Receive TAG", isi sesuai kolom Isi dialog blok, dan tombol [OK]
18. Verifikasi dialog "Receive TAG" tidak terbuka
19. Verifikasi tidak ada perubahan data: tab To Be Returned tetap memuat RF-00071, RF-00088, dan NF-00092
20. Klik [OK]
21. Verifikasi dialog blok tertutup

## Notes

- Spec harness eksternal simulator reader (kelas d); objek uji adalah kondisi reader pada dialog Receive TAG.
- Langkah yang diulang per baris tabel (bagian 8b butir 7): 14 sampai 21. Parameter tiap iterasi ada di Tabel 1 pada `## Prerequisites`; `Verifikasi` yang diulang tetap satu per klausa (S-01). Ekspansi: 1 + 6 + 6 + 4 x 8 = 45 langkah.
- Alasan melewati sekitar 35 langkah (bagian 3 prinsip 13): semua blok berada pada satu kelas harness (kondisi reader pada dialog Receive TAG) dan berdiri sendiri; tiap iterasi mengatur kondisi reader sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 (membuka tab), 2, 8, 10, 14 (mengatur kondisi reader), 3 (hover), 13 (menutup dialog yang tidak dirty).
- Anchor positif absence (bagian 8b butir 2): langkah 4 dan 5 untuk langkah 7; langkah 17 untuk langkah 18 dan 19.
- Pembagian TC lintas spec: TC-FA-TAG-556 sampai TC-FA-TAG-560 ada di spec 364, TC-FA-TAG-561 dan TC-FA-TAG-562 di spec 365.
- A-15: nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-550 dan TC-FA-TAG-551 berlabel Manual Only (kondisi hardware reader dan driver USB fisik); spec tetap ditulis dengan emulator driver reader sebagai kemampuan yang disediakan tim FE/BE.
  - TC-FA-TAG-552 sampai TC-FA-TAG-555 menyebut "tidak ada perubahan data" dalam butir yang sama dengan "dialog Receive TAG tidak terbuka" tanpa cara observasi; spec mengobservasinya lewat isi tab To Be Returned (langkah 19).
