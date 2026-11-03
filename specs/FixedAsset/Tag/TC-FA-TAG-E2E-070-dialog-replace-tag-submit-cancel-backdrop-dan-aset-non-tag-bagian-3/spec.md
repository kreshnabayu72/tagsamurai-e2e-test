---
id: TC-FA-TAG-E2E-070-dialog-replace-tag-submit-cancel-backdrop-dan-aset-non-tag-bagian-3
title: "Dialog Replace TAG: Esc pada Konfirmasi D-09, Submit Disabled Tanpa Tag Tercentang, dan Aset Non-TAG (Bagian 3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-317
  - TC-FA-TAG-1352
  - TC-FA-TAG-1441
coverage:
  web: automated
---

# Dialog Replace TAG: Esc pada Konfirmasi D-09, Submit Disabled Tanpa Tag Tercentang, dan Aset Non-TAG (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00130` Paired; 'Excavator 20 Ton - 244' (AST-0244, TAG Type Asset Name RFID) dengan Tag RFID `RF-00132` dan Tag QR `QR-00232` (Non-standard) Paired; 'Forklift Manual - 61' (AST-0161, Group Plant A, Asset Name Non-TAG) dengan Tag QR `QR-00251` Paired.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` Available.
- Kemampuan teknis tambahan: pemantau request jaringan browser untuk mengasersi tidak ada request terkirim (TC-FA-TAG-1352).
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1441: Esc pada dialog konfirmasi D-09 setara Cancel dan mempertahankan isian Dialog Replace TAG

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00412` dengan reader
5. Klik [Cancel] pada dialog Replace TAG
6. Tekan Esc pada dialog `Discard Replacement`
7. Verifikasi dialog konfirmasi menutup
8. Verifikasi dialog Replace TAG tetap terbuka dengan slot `RFID TAG` menampilkan `RF-00412`
9. Verifikasi slot `RFID TAG` menampilkan badge `Verified`
10. Klik [Cancel] pada dialog Replace TAG
11. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
12. Klik [Discard]

### TC-FA-TAG-1352: Submit Replace pada aset multi-Tag tanpa Tag tercentang

13. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 244'
14. Pastikan tidak ada Tag tercentang di daftar lepas (hilangkan centang bila ada)
15. Verifikasi tombol [Submit] Disabled dan tetap tampil
16. Klik [Submit]
17. Verifikasi klik [Submit] tidak mengirim permintaan
18. Verifikasi dialog Replace TAG tetap terbuka
19. Klik [Cancel] pada dialog Replace TAG

### TC-FA-TAG-317: Aset Non-TAG: bagian Replacement TAG menampilkan empty state S-43 dan Submit hanya melepas Tag

20. Tutup Popup Detail Assets
21. Klik Asset Name 'Forklift Manual' pada baris grup Plant A untuk membuka Popup Detail
22. Klik row action `Replace TAG` pada baris 'Forklift Manual - 61'
23. Verifikasi bagian `Replacement TAG` tetap tampil tanpa slot dengan teks "No replacement needed."
24. Verifikasi baris Tag `QR-00251` tanpa checkbox
25. Verifikasi baris Tag `QR-00251` otomatis terpilih
26. Klik [Submit]
27. Verifikasi toast "Success, TAG has been replaced."
28. Verifikasi dialog menutup

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC; dialog TC-FA-TAG-1441 yang terisi ditutup lewat [Cancel], verifikasi dialog `Discard Replacement`, dan [Discard]; urutan TC-FA-TAG-317 dipindah ke akhir karena memakai Popup 'Forklift Manual', sedangkan dua TC lain memakai Popup 'Excavator 20 Ton'.
- Pembagian TC lintas spec: TC-FA-TAG-309 sampai 316 ada di spec 068 dan 069.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Post Condition TC-FA-TAG-317 (Tag `QR-00251` keluar dari registri Global, aset tidak lagi punya Tag Paired) dan TC-FA-TAG-1352 (kedua Tag tetap Paired) tidak punya langkah observasi dan tidak diasersi.
  - Expected butir b TC-FA-TAG-1352 ('klik [Submit] tidak mengirim permintaan') mensyaratkan pemantauan request; kemampuan itu disediakan tim FE (S-13).
