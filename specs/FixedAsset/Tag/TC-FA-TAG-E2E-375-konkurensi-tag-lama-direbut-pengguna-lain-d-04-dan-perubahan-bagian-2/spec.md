---
id: TC-FA-TAG-E2E-375-konkurensi-tag-lama-direbut-pengguna-lain-d-04-dan-perubahan-bagian-2
title: "Konkurensi: Plan Berubah, Tag Pengganti Direbut Pengguna Lain, dan Dua Pengguna Memindai Tag Pengganti yang Sama"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1336
  - TC-FA-TAG-1337
  - TC-FA-TAG-1338
coverage:
  web: automated
---

# Konkurensi: Plan Berubah, Tag Pengganti Direbut Pengguna Lain, dan Dua Pengguna Memindai Tag Pengganti yang Sama

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Pelaku kedua (admin pengubah plan Client, pengguna lain yang memasangkan Tag, dan pengguna B pada TC-FA-TAG-1338; tidak ada di Pre-setup TC, disediakan tim FE) bertindak lewat sesi API aktor (lihat `suite.md`); sesi ini hanya mengubah state tanpa asersi di sesinya. Pengguna B tidak membuka sesi UI.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader (lihat `suite.md`); sesi API pelaku kedua yang menurunkan plan Client sehingga Tag RFID terkunci, memasangkan Tag ke aset lain, serta memindai dan mengirim Replace sebagai pengguna B; seed dan pemulihan idempotent aset, stok Tag, dan plan Client lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired; AST-0221 'Excavator 20 Ton - 221' (AST-0221, Group Plant A, TAG Type RFID) punya Tag RFID `RF-00140` Paired. Client berada di plan yang mengizinkan Tag RFID dan NFC. Stok Global: Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan plan Client ke plan yang mengizinkan Tag RFID dan NFC, AST-0220, AST-0221, dan stok Tag ke keadaan awal lewat fixture backend. State global: plan Client diubah pada langkah 4 dan dipulihkan pada langkah 10. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1336: plan berubah antara dialog dibuka dan Submit

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Admin menurunkan plan Client sehingga Tag RFID terkunci hingga perubahan plan tersimpan (sesi API)
5. Klik [Submit]
6. Verifikasi dialog judul "Asset TAG Has Changed", body "AST-0220 TAG has changed since this page was opened.", tombol [Update Data]
7. Verifikasi tidak ada mutasi dari Submit: Toast "Success, TAG has been replaced." tidak tampil
8. Klik [Update Data]
9. Klik `✕` pada Dialog Replace TAG
10. Pulihkan plan Client dan AST-0220 ke keadaan awal lewat fixture backend

### TC-FA-TAG-1337: Tag pengganti direbut sesi lain

11. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
12. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
13. Pengguna lain memasangkan `RF-00412` ke aset lain hingga pemasangan tersimpan (sesi API)
14. Klik [Submit]
15. Verifikasi dialog judul "Cannot Pair TAG", body "RF-00412 is no longer available. Scan another TAG.", tombol [OK]
16. Klik [OK]
17. Verifikasi dialog kembali ke bagian Scan the Replacement TAG dengan slot `RFID TAG` `Not scanned`
18. Klik `✕` pada Dialog Replace TAG
19. Pulihkan AST-0220 dan stok Tag ke keadaan awal lewat fixture backend

### TC-FA-TAG-1338: dua pengguna memindai Tag pengganti yang sama

20. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
21. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
22. Verifikasi slot `RFID TAG` menampilkan `RF-00412` dengan badge `Verified`
23. Pengguna B memindai `RF-00412` untuk Replace aset 'Excavator 20 Ton - 221' hingga pindaian diterima (sesi API)
24. Klik [Submit]
25. Verifikasi Toast "Success, TAG has been replaced." tampil
26. Pengguna B mengirim Submit Replace aset 'Excavator 20 Ton - 221' dengan Tag `RF-00412` hingga respons server diterima (sesi API)
27. Verifikasi Submit pengguna B ditolak dan Tag `RF-00412` tetap Paired pada 'Excavator 20 Ton - 220'

## Notes

- Spec konkurensi dengan pelaku kedua lewat sesi API (bukan kelas c, tidak memakai `P-2`); langkah pemicu ditulis "... hingga ... tersimpan" atau "... hingga ... diterima" (R-20). Pengguna B pada TC-FA-TAG-1338 memakai sesi API sesuai keputusan pelaku kedua.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 dan 2 (membuka popup dan dialog), 8 dan 9, 18 (menutup dialog setelah D-04 atau D-03), 10, 19 (memulihkan state lewat fixture, S-09), 11 dan 20 (membuka kembali dialog).
- Asersi "tidak ada mutasi" pada langkah 7 diamati sebagai Toast sukses penggantian tidak tampil setelah dialog D-04 tampil (langkah 6 menjadi anchor positif); TC tidak memberi cara observasi lain (S-03).
- Pembagian TC lintas spec: TC-FA-TAG-1332 sampai TC-FA-TAG-1335 ada di spec 374, TC-FA-TAG-1339 dan TC-FA-TAG-1351 di spec 376.
- Temuan untuk QA:
  - TC-FA-TAG-1338 mengharapkan pindaian `RF-00412` diterima di dua dialog (badge `Verified`) dan dialog "Cannot Pair TAG" pada pengguna B; dengan pengguna B lewat sesi API, hanya sisi pengguna A yang diasersi di UI (langkah 22 dan 25), sedangkan butir dialog pengguna B tidak dapat diasersi sebagai dialog. Langkah 27 mengasersi penolakan Submit pengguna B dan keadaan data sebagai gantinya. Perlu keputusan bila dialog pengguna B harus diasersi lewat sesi UI kedua (kelas c).
  - TC-FA-TAG-1336 sampai TC-FA-TAG-1338 berlabel Manual Only (dua sesi pengguna paralel); spec tetap ditulis dengan pelaku kedua lewat sesi API.
  - TC-FA-TAG-1338 Post Condition menyebut "`RF-00412` Paired pada 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221' tidak berubah", yang bertentangan dengan Expected c (Submit pengguna B ditolak); spec mengasersi RF-00412 tetap Paired pada 220 saja.
  - TC-FA-TAG-1336 tidak menyebut jenis plan setelah diturunkan; spec menulisnya sebagai plan yang mengunci Tag RFID.
  - TC-FA-TAG-1337 menyebut Post Condition ("Tag `RF-00130` tetap Paired") tanpa langkah observasi; tidak diasersi.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
