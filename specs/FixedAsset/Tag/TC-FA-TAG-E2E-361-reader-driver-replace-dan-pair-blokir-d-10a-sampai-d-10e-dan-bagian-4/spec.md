---
id: TC-FA-TAG-E2E-361-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-4
title: "Kondisi Reader: Alert Error Inline Scan Replacement TAG dan Banner Reader Terputus di Dialog Replace, Pair, dan Batch Replace"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-524
  - TC-FA-TAG-526
  - TC-FA-TAG-527
  - TC-FA-TAG-525
  - TC-FA-TAG-528
coverage:
  web: automated
---

# Kondisi Reader: Alert Error Inline Scan Replacement TAG dan Banner Reader Terputus di Dialog Replace, Pair, dan Batch Replace

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): emulator driver reader (simulator reader USB, lihat `suite.md`) yang mengatur kondisi reader di tengah dialog: driver reader lokal tidak terdeteksi, driver terpasang tetapi reader mati, reader diputus koneksinya setelah dialog dibuka, dan kondisi normal (satu reader RFID/NFC tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader); pindai kode lewat simulator; seed idempotent aset dan stok Tag lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired; AST-0221 'Excavator 20 Ton - 221' (Group Plant A) punya satu Tag RFID `RF-00140` berstatus Paired; AST-0051 'Excavator 20 Ton - 51' (Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet). Stok Global: Tag RFID `RF-00412` dan `RF-00415` berstatus Available, Tag NFC `NF-00500` berstatus Available. Spec ini tidak menekan [Submit], jadi tidak ada data yang tersimpan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan kondisi reader ke normal dan stok Tag ke keadaan awal lewat fixture backend. Spec ini tidak mengubah state global lain. Suite serial (`parallel: false`).

## Test Steps

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'

### TC-FA-TAG-524: Scan the Replacement TAG saat driver belum terpasang

3. Ubah kondisi reader: driver reader lokal tidak terdeteksi
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
5. Verifikasi Alert error inline berisi "USB driver not detected. Please install the reader driver software."
6. Verifikasi slot `RFID TAG` tetap `Not scanned`

### TC-FA-TAG-526: scan berhasil berikutnya membersihkan Alert

7. Pulihkan driver lalu klik ButtonScan `Scan RFID` pada slot `RFID TAG` dan pindai Tag `RF-00412`
8. Verifikasi Alert error inline hilang
9. Verifikasi slot `RFID TAG` menampilkan `RF-00412` dengan badge `Verified`

### TC-FA-TAG-527: reader terputus setelah Dialog Replace TAG dibuka

10. Putuskan koneksi reader
11. Verifikasi Alert warning "Connect a TAG reader to scan." tampil di dialog
12. Verifikasi tombol Scan pada baris `RF-00130` dan slot `RFID TAG` tetap tampil namun Disabled
13. Klik `✕` pada Dialog Replace TAG
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik [Leave]

### TC-FA-TAG-525: Scan di Dialog Pair TAG saat reader tidak merespons

16. Pulihkan kondisi reader: satu reader tersambung, driver terpasang, reader aktif
17. Klik `Show` di samping `Not Paired Yet`
18. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
19. Ubah kondisi reader: driver terpasang tetapi reader mati
20. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
21. Verifikasi Alert error inline berisi "Reader not responding. Ensure device is powered on and cable connected securely."
22. Verifikasi slot `RFID TAG` tetap `Not scanned`
23. Klik `✕` pada Dialog Pair TAG

### TC-FA-TAG-528: sesi Batch Replace TAG saat reader terputus

24. Pulihkan kondisi reader: satu reader tersambung, driver terpasang, reader aktif
25. Tutup Popup Detail
26. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
27. Centang baris 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221'
28. Klik Bulk `Batch Replace TAG`
29. Putuskan koneksi reader
30. Verifikasi Alert warning "Connect a TAG reader to scan." tampil di dialog sesi
31. Verifikasi tombol Scan Disabled namun [Skip] tetap tersedia

## Notes

- Spec harness eksternal simulator reader (kelas d); objek uji adalah kondisi reader. Urutan TC di dalam spec: 524, 526, 527, 525, 528 agar tiga TC pertama memakai satu Dialog Replace TAG.
- Langkah 3 sampai 6 menghasilkan keadaan yang sama dengan langkah pembuka TC-FA-TAG-526 (buka dialog, ubah kondisi reader, klik ButtonScan sehingga Alert error inline tampil karena driver belum terpasang), sehingga TC-FA-TAG-526 memakai keadaan akhir TC-FA-TAG-524 dan langkah itu tidak diulang. TC-FA-TAG-527 memakai Dialog Replace TAG yang sama (reader dipulihkan pada langkah 7).
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 dan 2 (membuka Popup Detail dan dialog), 3, 10, 16, 19, 24, 29 (mengatur kondisi reader), 13 sampai 15 (menutup form dirty, S-08), 17 dan 18 (membuka daftar Not Paired Yet dan Dialog Pair TAG), 23 (menutup Dialog Pair TAG yang tidak dirty), 25 sampai 28 (membuka sesi Batch Replace).
- Anchor positif absence (bagian 8b butir 2): Alert pada langkah 5 mendahului asersi slot tetap `Not scanned` pada langkah 6; Alert pada langkah 21 mendahului langkah 22.
- Pembagian TC lintas spec: TC-FA-TAG-508 sampai TC-FA-TAG-514 ada di spec 358, TC-FA-TAG-515 sampai TC-FA-TAG-519 di spec 359, TC-FA-TAG-520 sampai TC-FA-TAG-523 di spec 360, TC-FA-TAG-529 dan TC-FA-TAG-530 di spec 362.
- Temuan untuk QA:
  - TC-FA-TAG-526 langkah 5 menggabungkan "Pulihkan driver", klik ButtonScan, dan pindai dalam satu langkah; spec mengikuti pola itu pada langkah 7.
  - TC-FA-TAG-527 dan TC-FA-TAG-528 tidak menyebut cara memutus koneksi reader selain "simulasi lewat emulator driver reader"; spec memakai kemampuan emulator itu.
  - TC-FA-TAG-524 dan TC-FA-TAG-525 tidak punya Post Condition; TC-FA-TAG-527 tidak menyebut dialog menjadi dirty setelah pindaian pada langkah 7; spec menutupnya lewat langkah 13 sampai 15.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
