---
id: TC-FA-TAG-E2E-055-overlay-scan-tag-status-dilarang-tidak-dikenal-dan-milik-bagian-2
title: "Overlay Scan Replace TAG: Pesan Inline untuk Tag Tidak Dikenal dan Tag Milik Produk Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-253
  - TC-FA-TAG-254
  - TC-FA-TAG-255
  - TC-FA-TAG-256
  - TC-FA-TAG-264
coverage:
  web: automated
---

# Overlay Scan Replace TAG: Pesan Inline untuk Tag Tidak Dikenal dan Tag Milik Produk Lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dalam keadaan satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin. Seed idempotent registri Global dan produk lain lewat fixture backend.
- Data kode Tag (tanpa suffix `{runId}` karena asersi bergantung pada kode persis; tidak ada yang Paired di FAMS):
  - `RF-09999`: belum diaktivasi di Global.
  - `QR-09999`: tidak pernah dibuat lewat Start Print dan tidak terpasang di registri Global.
  - `SA-00020`: Tag milik produk Supply Asset, terdaftar di produk Supply Asset.
  - `UT-00010`: User TAG terdaftar di produk User Management.
- Pemulihan di hook `after`: kembalikan registri Global dan data produk lain ke keadaan awal bila seeding mengubahnya. Spec ini tidak mengubah data bisnis.
- State global: tidak ada. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-253: Tag tidak dikenal

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai kode `RF-09999` dengan simulator reader
3. Verifikasi pesan inline pada ButtonScan `Error, can't recognize TAG.`
4. Verifikasi overlay scan tetap terbuka
5. Verifikasi tidak ada dialog yang tampil
6. Klik ikon close overlay

### TC-FA-TAG-254: kode QR yang tidak pernah dicetak

7. Klik tombol scan `Replace TAG` di toolbar tab Paired
8. Pindai kode `QR-09999` dengan simulator reader
9. Verifikasi pesan inline pada ButtonScan `Error, can't recognize TAG.`
10. Verifikasi overlay scan tetap terbuka
11. Klik ikon close overlay

### TC-FA-TAG-255: Tag milik produk Supply Asset

12. Klik tombol scan `Replace TAG` di toolbar tab Paired
13. Pindai kode `SA-00020` dengan simulator reader
14. Verifikasi pesan inline pada ButtonScan `This TAG is used by Supply Asset.`
15. Verifikasi overlay scan tetap terbuka
16. Verifikasi tidak ada dialog yang tampil
17. Klik ikon close overlay

### TC-FA-TAG-256: User TAG

18. Klik tombol scan `Replace TAG` di toolbar tab Paired
19. Pindai kode `UT-00010` dengan simulator reader
20. Verifikasi pesan inline pada ButtonScan `This TAG is used by User Management.`
21. Verifikasi overlay scan tetap terbuka
22. Verifikasi tidak ada dialog yang tampil
23. Klik ikon close overlay

### TC-FA-TAG-264: urutan pemeriksaan S-19 sebelum D-07

24. Klik tombol scan `Replace TAG` di toolbar tab Paired
25. Pindai kode `SA-00020` dengan simulator reader
26. Verifikasi pesan inline `This TAG is used by Supply Asset.`
27. Verifikasi dialog dengan body `SA-00020 is not paired to an asset.` tidak tampil

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-TAG-246 sampai TC-FA-TAG-252 ada di spec 054.
- Langkah penghubung (tanpa awalan `Verifikasi`): 6, 11, 17, dan 23 (menutup overlay lewat ikon close sebelum scan berikutnya, karena overlay tetap terbuka sesudah pesan inline).
- Absence dialog (langkah 5, 16, 22, dan 27) didahului Verifikasi pesan inline dan overlay yang tampil (langkah 3 sampai 4, 14 sampai 15, 20 sampai 21, dan 26) sebagai anchor positif (bagian 8b butir 2). Dialog D-07 pada langkah 27 dikenali dari teks body yang disebut TC-FA-TAG-246 (`<kode> is not paired to an asset.`).
- Temuan untuk QA:
  - TC-FA-TAG-253 dan TC-FA-TAG-254 Expected tidak menyebut apakah pesan inline hilang sendiri atau saat pindai berikutnya; spec hanya mengasersi pesan dan overlay terbuka.
  - TC-FA-TAG-254 Expected tidak punya butir "tidak ada dialog" (berbeda dengan TC-FA-TAG-253); spec mengikuti TC.
  - Tidak ada Post Condition TC yang punya langkah observasi pada spec ini ("Tidak ada data yang berubah" tidak diasersi).
  - Registri produk Supply Asset dan User Management untuk `SA-00020` dan `UT-00010` tidak punya mekanisme seeding yang disebut TC atau PRD yang dibaca; spec menuliskannya sebagai kemampuan seed lewat fixture BE yang disediakan tim FE/BE.
  - Nilai literal Pre-setup (kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada kode persis; Lampiran A belum memuat butir untuk modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
