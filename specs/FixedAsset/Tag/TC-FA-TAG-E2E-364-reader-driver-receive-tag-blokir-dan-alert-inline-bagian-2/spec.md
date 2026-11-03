---
id: TC-FA-TAG-E2E-364-reader-driver-receive-tag-blokir-dan-alert-inline-bagian-2
title: "Kondisi Reader: Dialog Blok D-10e dan Alert Error Inline Scan di Dialog Receive TAG"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-556
  - TC-FA-TAG-557
  - TC-FA-TAG-558
  - TC-FA-TAG-559
  - TC-FA-TAG-560
coverage:
  web: automated
---

# Kondisi Reader: Dialog Blok D-10e dan Alert Error Inline Scan di Dialog Receive TAG

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): emulator driver reader (simulator reader USB, lihat `suite.md`) yang mengatur kondisi reader di tengah dialog: reader berstatus Waiting for Approval; driver reader USB belum terpasang; driver terpasang tetapi reader mati atau kabel tidak terpasang erat; lebih dari satu reader tersambung; reader terbaca tetapi Serial Number belum diaktivasi (Sync belum dijalankan); kondisi normal (satu reader RFID/NFC tersambung, aktif, sudah disinkronkan di Global Settings > Handheld Reader). Seed idempotent Tag To Be Returned lewat fixture backend.
- Data Pre-setup Tag To Be Returned (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.). Spec ini tidak menerima Tag, sehingga data tidak berubah.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader ke normal. Spec ini tidak mengubah state global lain. Suite serial (`parallel: false`).

## Test Steps

1. Buka Fixed Asset > TAG > To Be Returned

### TC-FA-TAG-556: dialog blok D-10e

2. Atur kondisi reader: reader berstatus Waiting for Approval
3. Verifikasi tombol "Receive TAG" Enabled
4. Klik tombol "Receive TAG"
5. Verifikasi dialog blok judul "Cannot Receive TAG", isi "This reader is waiting for approval. Try again after it is approved.", dan tombol [OK]
6. Verifikasi dialog "Receive TAG" tidak terbuka
7. Verifikasi tidak ada perubahan data: tab To Be Returned tetap memuat RF-00071, RF-00088, dan NF-00092
8. Klik [OK]
9. Verifikasi dialog blok tertutup

### TC-FA-TAG-557 sampai TC-FA-TAG-560: Alert error inline di dalam dialog

10. Atur kondisi reader: normal (satu reader RFID/NFC tersambung, aktif, sudah disinkronkan)
11. Klik tombol "Receive TAG"
12. Ubah kondisi reader menjadi: driver reader USB belum terpasang di komputer
13. Klik ButtonScan "Scan TAG" di dalam dialog
14. Verifikasi Alert error inline berisi "USB driver not detected. Please install the reader driver software." tampil di dalam dialog
15. Verifikasi tidak ada kode yang terbaca dan daftar sesi tidak berubah
16. Ubah kondisi reader menjadi: driver terpasang tetapi reader mati atau kabel tidak terpasang erat
17. Klik ButtonScan "Scan TAG" di dalam dialog
18. Verifikasi Alert error inline berisi "Reader not responding. Ensure device is powered on and cable connected securely." tampil di dalam dialog
19. Verifikasi tidak ada kode yang terbaca dan daftar sesi tidak berubah
20. Ubah kondisi reader menjadi: lebih dari satu reader tersambung
21. Klik ButtonScan "Scan TAG" di dalam dialog
22. Verifikasi Alert error inline berisi "Connect only one reader at a time." tampil di dalam dialog
23. Verifikasi tidak ada kode yang terbaca dan daftar sesi tidak berubah
24. Ubah kondisi reader menjadi: reader terbaca tetapi Serial Number belum diaktivasi (Sync belum dijalankan)
25. Klik ButtonScan "Scan TAG" di dalam dialog
26. Verifikasi Alert error inline berisi "This reader is not activated. Activate it in Global Settings > Handheld Reader first." tampil di dalam dialog
27. Verifikasi tidak ada kode yang terbaca dan daftar sesi tidak berubah
28. Klik `✕` pada Dialog Receive TAG

## Notes

- Spec harness eksternal simulator reader (kelas d); objek uji adalah kondisi reader pada dialog Receive TAG.
- Langkah 11 sampai 27 memakai satu Dialog Receive TAG untuk empat TC karena tidak ada pindaian sukses (dialog tidak dirty); kondisi reader diubah langsung antar-TC.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 (membuka tab), 2, 10, 12, 16, 20, 24 (mengatur kondisi reader), 28 (menutup dialog yang tidak dirty).
- Anchor positif absence (bagian 8b butir 2): langkah 5 untuk langkah 6 dan 7; Alert pada langkah 14, 18, 22, 26 mendahului asersi "tidak ada kode yang terbaca dan daftar sesi tidak berubah" pada langkah 15, 19, 23, 27.
- Pembagian TC lintas spec: TC-FA-TAG-550 sampai TC-FA-TAG-555 ada di spec 363, TC-FA-TAG-561 dan TC-FA-TAG-562 di spec 365.
- Temuan untuk QA:
  - TC-FA-TAG-556 sampai TC-FA-TAG-561 berlabel Manual Only (kondisi hardware reader dan driver USB fisik); spec tetap ditulis dengan emulator driver reader sebagai kemampuan yang disediakan tim FE/BE.
  - TC-FA-TAG-556 menyebut "tidak ada perubahan data" dalam butir yang sama dengan "dialog Receive TAG tidak terbuka" tanpa cara observasi; spec mengobservasinya lewat isi tab To Be Returned (langkah 7).
  - Nilai literal Pre-setup (kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
