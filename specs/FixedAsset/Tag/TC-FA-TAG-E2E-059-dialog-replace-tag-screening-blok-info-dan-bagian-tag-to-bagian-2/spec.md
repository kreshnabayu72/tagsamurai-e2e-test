---
id: TC-FA-TAG-E2E-059-dialog-replace-tag-screening-blok-info-dan-bagian-tag-to-bagian-2
title: "Dialog Replace TAG: Screening Bagian TAG to replace, Replacement TAG, dan Slot per Tipe Tag (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-271
  - TC-FA-TAG-272
  - TC-FA-TAG-273
  - TC-FA-TAG-274
  - TC-FA-TAG-275
coverage:
  web: automated
---

# Dialog Replace TAG: Screening Bagian TAG to replace, Replacement TAG, dan Slot per Tipe Tag (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 244' (AST-0244, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00332` dan Tag QR `QR-00432` (Non-standard) Paired; 'Excavator 20 Ton - 42' (AST-0042) dengan Tag QR `QR-00230` Paired (Non-standard); 'Excavator 20 Ton - 220' (AST-0220) dengan Tag RFID `RF-00330` Paired; 'Laptop Pro 14 - 8' (AST-0108, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00292` dan Tag QR `QR-00300` Paired; 'Label Printer - 72' (AST-0172, TAG Type Asset Name QR) dengan Tag QR `QR-00290` Paired.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, dan Tag QR `QR-00701` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: tidak ada yang diubah (spec hanya membaca); tidak ada Replace yang di-submit sehingga stok Tag per tipe di registri Global dan status Tag tidak berubah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-271: Screening bagian TAG to replace: judul, teks bantu S-34, dan urutan kolom baris

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00332` dengan reader
3. Verifikasi judul bagian `TAG to replace` tanpa nomor
4. Verifikasi teks bantu di bawah judul "Select the TAGs to replace. Scan each TAG you take off if you can. A TAG that is not scanned becomes Damaged/Missing."
5. Verifikasi tanpa baris judul kolom
6. Verifikasi tiap baris berurutan: checkbox, ikon tipe dan TAG Code, tombol Scan, badge status
7. Verifikasi baris `QR-00432` menampilkan ikon peringatan Non-standard
8. Verifikasi baris `RF-00332` berbadge `Scanned` di kanan tombol Scan

### TC-FA-TAG-272: Hover ikon peringatan Non-standard pada baris TAG to replace

9. Klik [Cancel] pada dialog Replace TAG
10. Klik tombol scan `Replace TAG` di toolbar tab Paired
11. Pindai Tag `QR-00230` dengan reader
12. Arahkan kursor ke ikon peringatan di samping `QR-00230`
13. Verifikasi tooltip "This TAG type is not required by the asset name."

### TC-FA-TAG-273: Screening bagian Replacement TAG: judul, Divider, dan slot

14. Klik [Cancel] pada dialog Replace TAG
15. Klik tombol scan `Replace TAG` di toolbar tab Paired
16. Pindai Tag `RF-00330` dengan reader
17. Verifikasi Divider horizontal memisahkan `TAG to replace` dan `Replacement TAG`
18. Verifikasi judul bagian `Replacement TAG` bertanda wajib (*)
19. Verifikasi satu slot dengan label `RFID TAG`, ButtonScan `Scan RFID`, dan status `Not scanned`
20. Verifikasi teks error inline V-28 belum tampil

### TC-FA-TAG-274: Slot Replacement TAG bertipe NFC memakai tombol Scan NFC

21. Klik [Cancel] pada dialog Replace TAG
22. Klik tombol scan `Replace TAG` di toolbar tab Paired
23. Pindai Tag `NF-00292` dengan reader
24. Verifikasi slot `NFC TAG` menampilkan ButtonScan berlabel `Scan NFC`
25. Verifikasi slot lain tidak tampil karena hanya Tag `NF-00292` di daftar lepas

### TC-FA-TAG-275: Slot Replacement TAG bertipe QR memuat tombol Print QR di kiri Scan QR

26. Klik [Cancel] pada dialog Replace TAG
27. Klik tombol scan `Replace TAG` di toolbar tab Paired
28. Pindai Tag `QR-00290` dengan reader
29. Verifikasi slot `QR TAG` menampilkan tombol `Print QR` (Button Outline dengan ikon PrinterLine) di sebelah kiri ButtonScan `Scan QR`
30. Klik [Cancel] pada dialog Replace TAG

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC dan di akhir spec; hover pada ikon peringatan adalah aksi pemicu tooltip.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Tidak ada Post Condition pada TC-FA-TAG-271 sampai 275.
