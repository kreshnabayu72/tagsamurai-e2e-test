---
id: TC-FA-TAG-E2E-052-overlay-scan-pemblokiran-dialog-d-01-d-06-d-08-dan-urutan-bagian-1
title: "Overlay Scan Replace TAG: Dialog Blok D-01 Aset Disposal dan D-08 Stok RFID Habis, serta Urutan Pemeriksaan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-240
  - TC-FA-TAG-241
  - TC-FA-TAG-244
  - TC-FA-TAG-262
coverage:
  web: automated
---

# Overlay Scan Replace TAG: Dialog Blok D-01 Aset Disposal dan D-08 Stok RFID Habis, serta Urutan Pemeriksaan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dalam keadaan satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin. Seed idempotent aset, Tag, Asset Status, dan stok Tag per tipe di registri Global lewat fixture backend.
- Data aset dan Tag (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis):
  - AST-0022 'Excavator 20 Ton - 22' (Group Plant A, TAG Type Asset Name RFID): masih punya Tag RFID `RF-00142` berstatus Paired; Asset Status awal In Disposal Process (TC-FA-TAG-240), diubah menjadi Disposed pada langkah 6.
  - AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID): satu Tag RFID `RF-00330` berstatus Paired.
  - Stok Global awal: Tag RFID `RF-00412` dan `RF-00415` berstatus Available, Tag NFC `NF-00500` berstatus Available; diubah menjadi tidak ada Tag RFID berstatus Available pada langkah 12.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Asset Status AST-0022, stok Tag RFID di registri Global, dan data aset serta Tag di atas ke keadaan awal. Spec ini tidak menekan `[Submit]`.
- State global: stok Tag RFID di registri Global dan Asset Status AST-0022 diubah spec ini. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 6, 12) yang menyiapkan atau memulihkan state.

## Test Steps

### TC-FA-TAG-240: aset In Disposal Process

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00142` dengan simulator reader
3. Verifikasi dialog judul `Cannot Replace TAG`, body `This asset is in disposal process or already disposed.`, tombol `[OK]`
4. Verifikasi Dialog Replace TAG tidak terbuka
5. Klik `[OK]`

### TC-FA-TAG-241: aset Disposed

6. Ubah Asset Status AST-0022 menjadi Disposed lewat fixture BE hingga perubahan tersimpan
7. Klik tombol scan `Replace TAG` di toolbar tab Paired
8. Pindai Tag `RF-00142` dengan simulator reader
9. Verifikasi dialog judul `Cannot Replace TAG`, body `This asset is in disposal process or already disposed.`, tombol `[OK]`
10. Verifikasi Dialog Replace TAG tidak terbuka
11. Klik `[OK]`

### TC-FA-TAG-244: stok RFID habis

12. Ubah stok Global sehingga tidak ada Tag RFID berstatus Available lewat fixture BE hingga perubahan tersimpan
13. Klik tombol scan `Replace TAG` di toolbar tab Paired
14. Pindai Tag `RF-00330` dengan simulator reader
15. Verifikasi dialog judul `Cannot Replace TAG`, body `No available RFID TAG in stock. Activate TAG in Global Settings > TAG.`, tombol `[OK]`
16. Verifikasi Dialog Replace TAG tidak terbuka
17. Klik `[OK]`

### TC-FA-TAG-262: urutan pemeriksaan D-01 sebelum D-08

18. Klik tombol scan `Replace TAG` di toolbar tab Paired
19. Pindai Tag `RF-00142` dengan simulator reader
20. Verifikasi dialog judul `Cannot Replace TAG`, body `This asset is in disposal process or already disposed.`, tombol `[OK]`
21. Verifikasi dialog dengan body `No available RFID TAG in stock. Activate TAG in Global Settings > TAG.` tidak tampil

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): 5, 11, dan 17 (menutup dialog blok lewat `[OK]`), 6 dan 12 (mengubah state lewat fixture BE sebagai precondition TC berikutnya). TC-FA-TAG-242, TC-FA-TAG-243, dan TC-FA-TAG-261 ada di spec 056; TC-FA-TAG-1456 ada di spec 053.
- Absence dialog (langkah 4, 10, 16, 21): didahului Verifikasi dialog blok yang diharapkan tampil (langkah 3, 9, 15, 20) sebagai anchor positif (bagian 8b butir 2).
- Langkah 21: dialog D-08 dikenali dari teks body yang disebut TC-FA-TAG-244; TC-FA-TAG-262 tidak menyebut cara membedakan dialog selain teks.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 6, 12) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - TC-FA-TAG-240 dan TC-FA-TAG-241 memakai AST-0022 dengan Asset Status berbeda tanpa menyebut cara mengubahnya; spec menuliskannya sebagai langkah fixture BE (langkah 6). TC-FA-TAG-262 memakai AST-0022 dengan status Disposed; urutan TC sumber 240, 241, 244, 262 dipertahankan.
  - TC-FA-TAG-262 mengandalkan stok RFID 0 yang dibangun pada TC-FA-TAG-244 (langkah 12).
  - Tidak ada Post Condition TC yang punya langkah observasi pada spec ini ("Tidak ada data yang berubah" tidak diasersi).
  - Teks dialog `Cannot Replace TAG` pada TC-FA-TAG-240 dan TC-FA-TAG-241 identik; perbedaan hanya pada Asset Status aset.
