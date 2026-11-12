---
id: TC-FA-TAG-E2E-365-reader-driver-receive-tag-blokir-dan-alert-inline-bagian-3
title: "Kondisi Reader: Alert Waiting for Approval di Dialog Receive TAG Hilang Setelah Scan Berikutnya Berhasil"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-561
  - TC-FA-TAG-562
coverage:
  web: automated
---

# Kondisi Reader: Alert Waiting for Approval di Dialog Receive TAG Hilang Setelah Scan Berikutnya Berhasil

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): emulator driver reader (simulator reader USB, lihat `suite.md`) yang mengatur kondisi reader di tengah dialog: reader berstatus Waiting for Approval; reader dimatikan; reader dipulihkan ke normal (satu reader RFID/NFC tersambung, aktif, sudah disinkronkan di Global Settings > Handheld Reader); pindai kode lewat simulator. Seed idempotent Tag To Be Returned lewat fixture backend.
- Data Pre-setup Tag To Be Returned (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.). Spec ini tidak menekan [Receive], jadi Tag tidak berubah.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader ke normal. Spec ini tidak mengubah state global lain. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-561: Waiting for Approval

1. Buka Fixed Asset > TAG > To Be Returned
2. Klik tombol "Receive TAG"
3. Ubah kondisi reader menjadi: reader berstatus Waiting for Approval
4. Klik ButtonScan "Scan TAG" di dalam dialog
5. Verifikasi Alert error inline berisi "This reader is waiting for approval. Try again after it is approved." tampil di dalam dialog
6. Verifikasi tidak ada kode yang terbaca dan daftar sesi tidak berubah

### TC-FA-TAG-562: Alert hilang setelah scan berikutnya berhasil

7. Matikan reader lalu klik ButtonScan "Scan TAG" hingga Alert error inline tampil
8. Pulihkan reader
9. Pindai Tag RF-00071
10. Verifikasi Alert error inline hilang
11. Verifikasi Tag RF-00071 masuk daftar sesi dan penghitung menampilkan "1 TAG scanned"
12. Klik [Cancel]

## Notes

- Spec harness eksternal simulator reader (kelas d); objek uji adalah kondisi reader pada dialog Receive TAG.
- TC-FA-TAG-562 memakai Dialog Receive TAG yang sama dengan TC-FA-TAG-561 (langkah 2); langkah 7 mematikan reader dan memicu Alert baru.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 dan 2 (membuka tab dan dialog), 3 dan 8 (mengatur kondisi reader), 12 (menutup dialog lewat [Cancel]).
- Anchor positif absence (bagian 8b butir 2): Alert pada langkah 5 mendahului asersi langkah 6. Asersi langkah 10 (Alert hilang) didahului langkah 7 (Alert tampil) sebagai kondisi awalnya.
- Pembagian TC lintas spec: TC-FA-TAG-550 sampai TC-FA-TAG-555 ada di spec 363, TC-FA-TAG-556 sampai TC-FA-TAG-560 di spec 364.
- A-15: nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-561 dan TC-FA-TAG-562 berlabel Manual Only (kondisi hardware reader dan driver USB fisik); spec tetap ditulis dengan emulator driver reader sebagai kemampuan yang disediakan tim FE/BE.
  - TC-FA-TAG-562 langkah 3 ("Matikan reader lalu klik ButtonScan hingga Alert error inline tampil") menggabungkan aksi dan hasil; spec mengikuti pola itu pada langkah 7 tanpa `Verifikasi` terpisah.
  - TC-FA-TAG-562 tidak menyebut cara menutup dialog setelah Tag dipindai dan tidak menyebut apakah dialog `Unsaved Changes` muncul; spec menutupnya lewat [Cancel] pada langkah 12 tanpa asersi dialog tersebut.
