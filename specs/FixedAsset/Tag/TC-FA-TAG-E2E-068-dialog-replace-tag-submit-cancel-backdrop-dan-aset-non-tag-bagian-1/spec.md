---
id: TC-FA-TAG-E2E-068-dialog-replace-tag-submit-cancel-backdrop-dan-aset-non-tag-bagian-1
title: "Dialog Replace TAG: Submit Normal, Submit Tanpa Tag Pengganti (V-28), dan Cancel Dialog Kosong atau Terisi (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-309
  - TC-FA-TAG-310
  - TC-FA-TAG-311
  - TC-FA-TAG-312
coverage:
  web: automated
---

# Dialog Replace TAG: Submit Normal, Submit Tanpa Tag Pengganti (V-28), dan Cancel Dialog Kosong atau Terisi (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag RFID `RF-00330` Paired. Fixture BE memulihkan `RF-00330` Paired dan `RF-00412` Available sebelum TC-FA-TAG-310 (Submit TC-FA-TAG-309 mengubahnya).
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5); entri TAG Log Global (langkah 5). Aksi tulis pada langkah 13 ditolak dan tidak menambah entri.

## Test Steps

### TC-FA-TAG-309: Submit Replace Tag RFID normal terscan menyimpan penggantian

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00330` dengan reader
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00412` dengan reader
5. Klik [Submit]
6. Verifikasi toast "Success, TAG has been replaced."
7. Verifikasi dialog Replace TAG menutup
8. Verifikasi pengguna tetap di tab Paired
9. Verifikasi tabel Paired dimuat ulang

### TC-FA-TAG-310: Submit tanpa Tag pengganti terverifikasi menampilkan teks error V-28

10. Pulihkan lewat fixture BE: Tag `RF-00330` Paired pada AST-0220 dan Tag `RF-00412` Available
11. Klik tombol scan `Replace TAG` di toolbar tab Paired
12. Pindai Tag `RF-00330` dengan reader
13. Klik [Submit]
14. Verifikasi teks error inline "Please verify the replacement TAG" tampil di atas tombol
15. Verifikasi dialog tetap terbuka
16. Verifikasi tidak ada Toast sukses
17. Klik [Cancel] pada dialog Replace TAG

### TC-FA-TAG-311: Cancel pada dialog yang belum terisi menutup dialog langsung

18. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
19. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
20. Klik [Cancel] pada dialog Replace TAG
21. Verifikasi dialog menutup tanpa dialog konfirmasi
22. Verifikasi pengguna tetap di tab Paired

### TC-FA-TAG-312: Cancel pada dialog yang sudah terisi menampilkan konfirmasi D-09

23. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
24. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
25. Pindai Tag `RF-00412` dengan reader
26. Klik [Cancel] pada dialog Replace TAG
27. Verifikasi dialog judul "Discard Replacement", body "Discard this replacement? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
28. Verifikasi dialog Replace TAG masih terbuka di bawah konfirmasi
29. Klik [Discard]
30. Tutup Popup Detail Assets

## Notes

- Langkah penghubung (S-03): Pemulihan data lewat fixture BE sebelum TC-FA-TAG-310; [Cancel] menutup dialog yang hanya berisi Tag lama terpindai; [Discard] dan penutupan Popup Detail Assets di akhir spec memulihkan halaman. TC-FA-TAG-311 dan 312 memakai satu pembukaan Popup Detail (Popup tetap terbuka di bawah dialog).
- Pembagian TC lintas spec: TC-FA-TAG-313 sampai 316 ada di spec 069 dan TC-FA-TAG-317 ada di spec 070.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5); entri TAG Log Global (langkah 5). Aksi tulis pada langkah 13 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Post Condition TC-FA-TAG-309 (status `RF-00412` Paired dan `RF-00330` Available di registri Global, tidak masuk To Be Returned, TAG Log) dan TC-FA-TAG-310 (tidak ada entri Changelog baru) tidak punya langkah observasi di TC dan tidak diasersi.
