---
id: TC-FA-TAG-E2E-069-dialog-replace-tag-submit-cancel-backdrop-dan-aset-non-tag-bagian-2
title: "Dialog Replace TAG: Konfirmasi Discard (D-09) lewat Cancel, Ikon Close, dan Klik Backdrop (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-313
  - TC-FA-TAG-314
  - TC-FA-TAG-315
  - TC-FA-TAG-316
coverage:
  web: automated
---

# Dialog Replace TAG: Konfirmasi Discard (D-09) lewat Cancel, Ikon Close, dan Klik Backdrop (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag RFID `RF-00130` Paired.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-313: Konfirmasi D-09 dengan [Cancel] mempertahankan isian dialog

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00412` dengan reader
5. Klik [Cancel] pada dialog Replace TAG
6. Klik [Cancel] pada dialog `Discard Replacement`
7. Verifikasi dialog konfirmasi menutup
8. Verifikasi dialog Replace TAG tetap terbuka dengan slot `RFID TAG` menampilkan `RF-00412`
9. Verifikasi slot `RFID TAG` menampilkan badge `Verified`

### TC-FA-TAG-314: Konfirmasi D-09 dengan [Discard] menutup dialog tanpa menyimpan

10. Klik [Cancel] pada dialog Replace TAG
11. Klik [Discard]
12. Verifikasi dialog konfirmasi dan dialog Replace TAG menutup
13. Verifikasi pengguna tetap di tab Paired

### TC-FA-TAG-315: Ikon close pada dialog yang sudah terisi menampilkan konfirmasi D-09

14. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
16. Pindai Tag `RF-00412` dengan reader
17. Klik ikon close dialog
18. Verifikasi dialog judul "Discard Replacement", body "Discard this replacement? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
19. Klik [Cancel] pada dialog `Discard Replacement`

### TC-FA-TAG-316: Klik backdrop tidak menutup Dialog Replace TAG yang sudah terisi

20. Klik area backdrop di luar dialog
21. Verifikasi dialog tetap terbuka dengan isian utuh
22. Verifikasi dialog konfirmasi tidak tampil
23. Klik [Cancel] pada dialog Replace TAG
24. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
25. Klik [Discard]
26. Tutup Popup Detail Assets

## Notes

- Langkah penghubung (S-03): TC-FA-TAG-314 melanjutkan dialog TC-FA-TAG-313 karena keadaan awalnya identik (slot terisi `RF-00412`); TC-FA-TAG-316 melanjutkan dialog TC-FA-TAG-315 sesudah konfirmasi dibatalkan; dialog terakhir ditutup lewat [Cancel], verifikasi dialog `Discard Replacement`, dan [Discard]; Popup Detail Assets ditutup di akhir spec.
- Pembagian TC lintas spec: TC-FA-TAG-309 sampai 312 ada di spec 068 dan TC-FA-TAG-317 ada di spec 070.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Post Condition TC-FA-TAG-314 (Tag `RF-00130` Paired, `RF-00412` Available, tidak ada entri Changelog baru) tidak punya langkah observasi dan tidak diasersi.
