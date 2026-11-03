---
id: TC-FA-TAG-E2E-297-derivasi-non-standard-reported-dan-not-paired-yet-bagian-1
title: "Derivasi Non-standard, Reported, dan Not Paired Yet: Dihitung Ulang dan Aturan Non-standard, Bagian 1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-143
  - TC-FA-TAG-1316
  - TC-FA-TAG-1318
  - TC-FA-TAG-1319
  - TC-FA-TAG-1320
  - TC-FA-TAG-1321
  - TC-FA-TAG-1322
  - TC-FA-TAG-1323
coverage:
  web: automated
---

# Derivasi Non-standard, Reported, dan Not Paired Yet: Dihitung Ulang dan Aturan Non-standard, Bagian 1

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data Pre-setup tab Paired (TC): Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC dan QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B memuat lima aset acuan: AST-0011 ('Excavator 20 Ton - 11'), AST-0020 ('- 20'), AST-0021 ('- 21'), AST-0043 ('- 43'), AST-0044 ('- 44').
- Data tambahan (TC, tanpa suffix): aset AST-0043 dengan satu Tag QR `QR-00231` Paired (Excavator 20 Ton / Plant B, RFID); aset AST-0300 dengan dua Tag QR Paired pada Excavator 20 Ton (RFID); aset AST-0044 dengan `RF-00132` (RFID, sesuai) dan `QR-00232` (tidak sesuai); Asset Name `Beacon Unit` (BLE saja) dengan aset ber-Tag RFID Paired; Asset Name `Tracker Unit` (RFID dan BLE) dengan aset ber-Tag NFC Paired.
- Kemampuan teknis (disediakan tim FE/BE): membaca state backend (status Tag dan laporan) tanpa UI hanya untuk butir Expected TC yang menyebutnya (S-11).
- Baseline nilai Non-standard baris grup dan kartu `Non-standard` dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` (S-12).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: TAG Type Asset Name, data aset/Tag/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-143: Reported dan Non-standard dihitung ulang server setiap data dimuat

1. Catat nilai baris Excavator 20 Ton / Plant B dan kartu Non-standard sebelum perubahan
2. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Excavator 20 Ton' dari RFID menjadi NFC sehingga jumlah Non-standard berubah hingga perubahan tersimpan
3. Muat ulang halaman TAG tab Paired (F5)
4. Verifikasi nilai Non-standard baris Excavator 20 Ton / Plant B mengikuti hasil hitung terbaru tanpa langkah sinkron manual
5. Verifikasi tidak ada salinan status Tag atau flag Non-standard dan Reported yang tersimpan di FAMS (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1316: nilai kartu dan baris grup mengikuti data terbaru setelah perubahan oleh pengguna lain

6. Pulihkan TAG Type 'Excavator 20 Ton' ke RFID lewat fixture backend, lalu muat ulang halaman TAG tab Paired
7. Pelaku kedua (Total Control) lewat sesi API mengganti satu Tag Non-standard di Excavator 20 Ton / Plant B hingga penggantian tersimpan
8. Muat ulang halaman TAG tab Paired (F5)
9. Verifikasi Non-standard baris Excavator 20 Ton / Plant B berkurang 1
10. Verifikasi kartu `Non-standard` berkurang 1

### TC-FA-TAG-1318: Tag Paired yang tipenya tidak ada pada TAG Type Asset Name terhitung Non-standard

11. Pulihkan data lewat fixture backend, lalu muat ulang halaman TAG tab Paired
12. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
13. Verifikasi `QR-00231` pada baris AST-0043 bertanda ikon peringatan Non-standard
14. Verifikasi AST-0043 terhitung dalam `Non-standard` (5 pada blok info)

### TC-FA-TAG-1319: aset dengan dua Tag Non-standard dihitung satu aset

15. Tutup Popup Detail, lalu pulihkan data lewat fixture backend (AST-0300 dengan dua Tag QR Paired, tanpa aset Non-standard lain pada grup), lalu muat ulang halaman TAG tab Paired
16. Verifikasi Non-standard baris grup = 1 (dihitung per aset, bukan per Tag)

### TC-FA-TAG-1320: aset dengan Tag sesuai dan Tag Non-standard terhitung Non-standard

17. Pulihkan data lewat fixture backend (AST-0044 dengan `RF-00132` dan `QR-00232`), lalu muat ulang halaman TAG tab Paired
18. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
19. Verifikasi hanya `QR-00232` bertanda ikon peringatan pada baris AST-0044
20. Verifikasi AST-0044 terhitung Non-standard

### TC-FA-TAG-1321: pada Asset Name Non-TAG setiap Tag Paired adalah Non-standard

21. Tutup Popup Detail, lalu pulihkan data lewat fixture backend, lalu muat ulang halaman TAG tab Paired
22. Klik Asset Name `Forklift Manual` pada baris Plant A untuk membuka Popup Detail
23. Verifikasi Non-standard = 3, sama dengan jumlah aset ber-Tag pada Forklift Manual / Plant A
24. Verifikasi setiap Tag Paired pada Popup Detail bertanda ikon peringatan Non-standard

### TC-FA-TAG-1322: Asset Name yang hanya menuntut BLE atau GPS tidak menjadikan Tag lain Non-standard

25. Tutup Popup Detail, lalu pulihkan data lewat fixture backend (Asset Name Beacon Unit dengan TAG Type BLE saja dan aset ber-Tag RFID Paired), lalu muat ulang halaman TAG tab Paired
26. Verifikasi Non-standard baris Beacon Unit = 0
27. Klik Asset Name `Beacon Unit` untuk membuka Popup Detail
28. Verifikasi Tag RFID pada baris Beacon Unit tidak bertanda ikon peringatan

### TC-FA-TAG-1323: Asset Name RFID dan BLE, Tag NFC tetap Non-standard

29. Tutup Popup Detail, lalu pulihkan data lewat fixture backend (Asset Name Tracker Unit dengan TAG Type RFID dan BLE dan aset ber-Tag NFC Paired), lalu muat ulang halaman TAG tab Paired
30. Klik Asset Name `Tracker Unit` untuk membuka Popup Detail
31. Verifikasi Tag NFC bertanda ikon peringatan Non-standard
32. Verifikasi Tag NFC terhitung pada kolom Non-standard baris Tracker Unit

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 1, 6, 11, 15, 17, 21, 25 dan 29 (mencatat nilai awal, memulihkan data lewat fixture antar TC dan menutup popup, S-09; memuat ulang halaman setelah fixture).
- Pemicu TC-FA-TAG-143 dan 1316 memakai pelaku kedua lewat sesi API karena hanya memicu perubahan state dan tidak diasersi di sesinya (R-20).
- Temuan untuk QA:
  - TC-FA-TAG-1319 menyebut baris grup tanpa menyebut Asset Name dan Group; AST-0300 juga dipakai TC-FA-TAG-1111 sebagai aset Not Paired Yet dengan TAG Type RFID. Spec memakai grup Excavator 20 Ton / Plant A dan data aset dari fixture.
  - TC-FA-TAG-1322 dan 1323 menyebut Asset Name Beacon Unit dan Tracker Unit tanpa Group; TC-FA-TAG-1481 memakai Beacon Unit / Plant A dengan tipe BLE dan GPS. Spec memakai Group dari fixture.
  - TC-FA-TAG-143 Expected b ('tidak ada salinan status Tag atau flag Non-standard/Reported tersimpan di FAMS') tidak dapat diamati di UI; spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa endpoint karangan.
  - TC-FA-TAG-1316 langkah TC ke-1 ('Pengguna lain mengganti satu Tag Non-standard') tidak menyebut pengguna dan Tag; spec memakai pelaku kedua lewat sesi API dan fixture memilih Tag Non-standard.
  - TC-FA-TAG-1318 menyebut 'QR-00231 bertanda ikon peringatan Non-standard' tanpa teks tooltip; spec mengasersi ikon peringatan saja.
