---
id: TC-FA-TAG-E2E-061-dialog-replace-tag-pemilihan-tag-centang-dan-slot-pengganti-bagian-1
title: "Dialog Replace TAG: Pemilihan Tag (Centang) dan Slot Pengganti Mengikuti Pilihan (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-276
  - TC-FA-TAG-277
  - TC-FA-TAG-278
  - TC-FA-TAG-279
  - TC-FA-TAG-280
coverage:
  web: automated
---

# Dialog Replace TAG: Pemilihan Tag (Centang) dan Slot Pengganti Mengikuti Pilihan (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag RFID `RF-00330` Paired; 'Excavator 20 Ton - 244' (AST-0244, TAG Type Asset Name RFID) dengan Tag RFID `RF-00332` (bertipe sesuai) dan Tag QR `QR-00432` (Non-standard) Paired; 'Laptop Pro 14 - 8' (AST-0108, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00292` dan Tag QR `QR-00300` Paired.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, dan Tag QR `QR-00701` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: tidak ada yang diubah (spec hanya membaca); tidak ada Replace yang di-submit sehingga stok Tag per tipe di registri Global dan status Tag tidak berubah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-276: Aset satu Tag: baris Tag tanpa checkbox, otomatis terpilih, dan berlabel Scanned

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00330` dengan reader
3. Verifikasi bagian `TAG to replace` memuat satu baris `RF-00330` tanpa checkbox
4. Verifikasi Tag `RF-00330` otomatis terpilih
5. Verifikasi Tag `RF-00330` berbadge `Scanned`
6. Verifikasi bagian `Replacement TAG` memuat satu slot RFID

### TC-FA-TAG-277: Aset beberapa Tag lewat overlay: Tag terpindai tercentang awal, semua checkbox aktif

7. Klik [Cancel] pada dialog Replace TAG
8. Klik tombol scan `Replace TAG` di toolbar tab Paired
9. Pindai Tag `RF-00332` dengan reader
10. Verifikasi baris `RF-00332` tercentang
11. Verifikasi baris `RF-00332` berbadge `Scanned`
12. Verifikasi baris `QR-00432` tidak tercentang
13. Verifikasi kedua checkbox tampil dan aktif (tidak ada yang terkunci)
14. Verifikasi bagian `Replacement TAG` memuat satu slot RFID

### TC-FA-TAG-279: Mencentang Tag kedua menambah slot pengganti dan menghitung ulang daftar pasang

15. Klik [Cancel] pada dialog Replace TAG
16. Klik tombol scan `Replace TAG` di toolbar tab Paired
17. Pindai Tag `NF-00292` dengan reader
18. Centang checkbox baris `QR-00300`
19. Verifikasi daftar lepas menjadi `NF-00292` dan `QR-00300`
20. Verifikasi bagian `Replacement TAG` menampilkan dua slot: `NFC TAG` dan `QR TAG`

### TC-FA-TAG-280: Membatalkan centang Tag terpindai menghapus slot pengganti Tag itu

21. Hapus centang checkbox baris `NF-00292`
22. Verifikasi baris `NF-00292` tidak tercentang
23. Verifikasi daftar pasang hanya satu slot `QR TAG`
24. Verifikasi slot `NFC TAG` hilang

### TC-FA-TAG-278: Aset beberapa Tag lewat row action: tidak ada Tag tercentang awal dan tidak ada Tag terverifikasi

25. Klik [Cancel] pada dialog Replace TAG
26. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
27. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 244'
28. Verifikasi dialog Replace TAG terbuka langsung tanpa overlay scan
29. Verifikasi checkbox `RF-00332` dan `QR-00432` tidak tercentang
30. Verifikasi kedua checkbox aktif
31. Verifikasi tidak ada baris berbadge `Scanned`
32. Klik [Cancel] pada dialog Replace TAG

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC dan di akhir spec; TC-FA-TAG-280 melanjutkan dialog TC-FA-TAG-279 karena keadaan awalnya identik, sehingga hanya langkah hapus centang yang ditambahkan; urutan TC-FA-TAG-278 dipindah ke akhir karena memakai jalur row action, sedangkan empat TC lain memakai overlay scan.
- Pembagian TC lintas spec: TC-FA-TAG-281 dan 282 ada di spec 062.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Tidak ada Post Condition pada TC-FA-TAG-276 sampai 280.
