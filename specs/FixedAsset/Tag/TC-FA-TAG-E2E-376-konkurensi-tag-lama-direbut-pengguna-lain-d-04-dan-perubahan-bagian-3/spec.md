---
id: TC-FA-TAG-E2E-376-konkurensi-tag-lama-direbut-pengguna-lain-d-04-dan-perubahan-bagian-3
title: "Konkurensi: Aset In Disposal Process Setelah Dialog Replace Dibuka dan Aset Sudah Dipasangkan Pengguna Lain Sebelum Submit Pair"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1339
  - TC-FA-TAG-1351
coverage:
  web: automated
---

# Konkurensi: Aset In Disposal Process Setelah Dialog Replace Dibuka dan Aset Sudah Dipasangkan Pengguna Lain Sebelum Submit Pair

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Pelaku kedua (transaksi disposal dan pengguna lain yang memasangkan Tag; tidak ada di Pre-setup TC, disediakan tim FE) bertindak lewat sesi API aktor (lihat `suite.md`); sesi ini hanya mengubah state tanpa asersi di sesinya.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader (lihat `suite.md`); sesi API pelaku kedua yang mengubah aset menjadi In Disposal Process dan memasangkan Tag ke aset; seed dan pemulihan idempotent aset serta stok Tag lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired; AST-0051 'Excavator 20 Ton - 51' (Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet). Stok Global: Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan AST-0220, AST-0051, dan stok Tag ke keadaan awal lewat fixture backend. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1339: aset menjadi In Disposal Process

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Transaksi disposal mengubah aset menjadi In Disposal Process hingga perubahan tersimpan (sesi API)
5. Klik [Submit]
6. Verifikasi dialog judul "Cannot Replace TAG", body "This asset is in disposal process or already disposed.", tombol [OK]
7. Verifikasi tidak ada mutasi dari Submit: Toast "Success, TAG has been replaced." tidak tampil
8. Klik [OK]
9. Klik `✕` pada Dialog Replace TAG
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik [Leave]
12. Pulihkan AST-0220 ke keadaan awal lewat fixture backend

### TC-FA-TAG-1351: Pair saat aset sudah dipasangkan pengguna lain

13. Klik `Show` di samping `Not Paired Yet`
14. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
16. Pengguna lain memasangkan Tag `RF-00415` ke aset yang sama hingga pemasangan tersimpan (sesi API)
17. Klik [Submit]
18. Verifikasi Toast "Error, failed to pair TAG."
19. Verifikasi Dialog Pair TAG tetap terbuka
20. Klik `✕` pada Dialog Pair TAG
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik [Leave]
23. Tutup Popup Detail
24. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
25. Verifikasi baris 'Excavator 20 Ton - 51' memuat Tag `RF-00415` dari pengguna lain
26. Verifikasi baris 'Excavator 20 Ton - 51' tidak memuat Tag `RF-00412`

## Notes

- Spec konkurensi dengan pelaku kedua lewat sesi API (bukan kelas c, tidak memakai `P-2`); langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 dan 2, 13 dan 14 (membuka popup, daftar Not Paired Yet, dan dialog), 9 sampai 11 dan 20 sampai 22 (menutup form dirty, S-08), 12 (memulihkan state lewat fixture, S-09), 23 dan 24 (menutup dan membuka kembali popup agar daftar dimuat ulang).
- Asersi "tidak ada mutasi" pada langkah 7 diamati sebagai Toast sukses penggantian tidak tampil setelah dialog blok tampil (langkah 6 menjadi anchor positif); TC tidak memberi cara observasi lain (S-03). Langkah 25 (baris memuat `RF-00415`) mendahului langkah 26 sebagai anchor positif absence (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-TAG-1332 sampai TC-FA-TAG-1335 ada di spec 374, TC-FA-TAG-1336, TC-FA-TAG-1337, dan TC-FA-TAG-1338 di spec 375.
- Temuan untuk QA:
  - TC-FA-TAG-1339 berlabel Manual Only (dua sesi pengguna paralel); spec tetap ditulis dengan pelaku kedua lewat sesi API.
  - TC-FA-TAG-1351 tidak menyebut cara mengamati "Tag `RF-00412` tidak dipasang ke aset"; spec mengamatinya lewat baris aset di Popup Detail setelah dimuat ulang (langkah 23 sampai 26).
  - TC-FA-TAG-1339 dan TC-FA-TAG-1351 menyebut Post Condition ("Tag `RF-00130` tetap Paired", "Aset tetap memiliki Tag `RF-00415`") tanpa langkah observasi tersendiri; hanya yang setara dengan Expected diasersi.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
