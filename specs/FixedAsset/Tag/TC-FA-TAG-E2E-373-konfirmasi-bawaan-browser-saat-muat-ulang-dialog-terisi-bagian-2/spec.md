---
id: TC-FA-TAG-E2E-373-konfirmasi-bawaan-browser-saat-muat-ulang-dialog-terisi-bagian-2
title: "Muat Ulang: Konfirmasi Bawaan Browser pada Dialog Receive TAG dan Sesi Pair Terisi, Tidak Muncul pada Dialog Kosong dan Setelah Submit"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1466
  - TC-FA-TAG-1467
  - TC-FA-TAG-1484
  - TC-FA-TAG-1468
coverage:
  web: automated
---

# Muat Ulang: Konfirmasi Bawaan Browser pada Dialog Receive TAG dan Sesi Pair Terisi, Tidak Muncul pada Dialog Kosong dan Setelah Submit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): penanganan dialog `beforeunload` bawaan browser (mendeteksi kemunculan atau ketidakmunculannya, memilih tetap di halaman, dan memilih muat ulang; tercantum juga di `suite.md`); simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader; seed idempotent aset, Tag To Be Returned, dan stok Tag lewat fixture backend.
- Data Pre-setup Tag To Be Returned (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.). Tiga aset Not Paired Yet di Group Plant A dengan TAG Type Asset Name RFID: AST-0051 'Excavator 20 Ton - 51', AST-0052 'Excavator 20 Ton - 52', AST-0054 'Excavator 20 Ton - 54'. Stok Global: Tag RFID `RF-00412`, `RF-00415`, `RF-00416` berstatus Available.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset AST-0051, Tag `RF-00412`, Tag To Be Returned, dan kondisi reader ke keadaan awal lewat fixture backend (TC-FA-TAG-1468 memasangkan `RF-00412` ke AST-0051). Form dirty ditutup dengan memilih muat ulang pada konfirmasi bawaan browser (S-08). Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1466: Dialog Receive TAG berisi Tag terpindai

1. Buka Fixed Asset > TAG > To Be Returned
2. Klik tombol "Receive TAG"
3. Pindai Tag RF-00071
4. Muat ulang halaman (F5)
5. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
6. Pilih tetap di halaman pada konfirmasi bawaan browser
7. Verifikasi Dialog Receive TAG masih terbuka dan daftar sesi memuat RF-00071 dengan penghitung "1 TAG scanned"
8. Muat ulang halaman (F5)
9. Pilih muat ulang pada konfirmasi bawaan browser

### TC-FA-TAG-1467: Dialog Receive TAG kosong

10. Klik tombol "Receive TAG" tanpa memindai Tag
11. Muat ulang halaman (F5)
12. Verifikasi halaman dimuat ulang dan tab To Be Returned tampil tanpa Dialog Receive TAG
13. Verifikasi konfirmasi bawaan browser (beforeunload) tidak muncul

### TC-FA-TAG-1484: sesi Pair TAG beberapa aset terisi

14. Buka tab Paired
15. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
16. Klik `Show` di samping `Not Paired Yet`
17. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
18. Klik Bulk `Pair TAG`
19. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
20. Muat ulang halaman (F5)
21. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
22. Pilih tetap di halaman pada konfirmasi bawaan browser
23. Verifikasi sesi Pair TAG masih terbuka pada header `Pair TAG · Asset 1 of 3` dan slot `RFID TAG` menampilkan `RF-00412` dengan badge `Verified`
24. Muat ulang halaman (F5)
25. Pilih muat ulang pada konfirmasi bawaan browser

### TC-FA-TAG-1468: dialog Pair TAG setelah Submit sukses

26. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
27. Klik tombol teks `Show` di samping field `Not Paired Yet`
28. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
29. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
30. Klik tombol [Submit]
31. Verifikasi Toast "Success, TAG has been paired." tampil
32. Verifikasi Dialog Pair TAG menutup
33. Muat ulang halaman (F5)
34. Verifikasi halaman dimuat ulang dan halaman TAG tampil
35. Verifikasi konfirmasi bawaan browser (beforeunload) tidak muncul

## Notes

- Spec muat ulang dengan dialog `beforeunload` (kelas fungsional). Kemampuan menangani dialog itu tertulis di `## Prerequisites` sehingga reload sah menurut S-08.
- Urutan TC di dalam spec: 1466, 1467, 1484, 1468 (TC-FA-TAG-1468 terakhir karena [Submit] memasangkan `RF-00412` ke AST-0051 yang dipakai TC-FA-TAG-1484 sebagai aset Not Paired Yet).
- Langkah penghubung (tanpa awalan `Verifikasi`): 8 dan 9, 24 dan 25 (menutup form dirty dengan memuat ulang dan memilih muat ulang, S-08); 1, 2, 14 sampai 18, 26 sampai 28 (membuka tab, popup, dan dialog).
- Anchor positif absence (bagian 8b butir 2, R-21): pada TC-FA-TAG-1467 langkah 12 (halaman dimuat ulang dan tab To Be Returned tampil) mendahului langkah 13; pada TC-FA-TAG-1468 langkah 31 dan 32 (Toast sukses dan dialog menutup) serta langkah 34 (halaman TAG tampil setelah dimuat ulang) mendahului langkah 35. Langkah 34 adalah tambahan di luar Expected TC (S-03); alasannya agar absence konfirmasi bukan karena halaman belum dimuat.
- Pembagian TC lintas spec: TC-FA-TAG-1463, TC-FA-TAG-1464, dan TC-FA-TAG-1465 ada di spec 372.
- Temuan untuk QA:
  - TC-FA-TAG-1466 sampai TC-FA-TAG-1484 tidak menyebut cara menutup dialog yang terisi sesudah memilih tetap di halaman; spec menutupnya dengan memuat ulang halaman dan memilih muat ulang (langkah 8 dan 9, 24 dan 25).
  - TC-FA-TAG-1467 menyebut asersi absence `beforeunload` tanpa anchor lain selain pemicu reload; spec menaruh Expected b (halaman dimuat ulang) sebelum Expected a sebagai anchor.
  - TC-FA-TAG-1466 sampai TC-FA-TAG-1468 dan TC-FA-TAG-1484 menyebut Post Condition ("Tag RF-00071 tetap To Be Returned; tidak ada entri Event Log maupun TAG Log baru", "Tidak ada Tag yang dipasangkan") tanpa langkah observasi; tidak diasersi.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
