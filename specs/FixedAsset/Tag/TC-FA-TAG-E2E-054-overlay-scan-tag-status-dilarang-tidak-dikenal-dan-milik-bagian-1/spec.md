---
id: TC-FA-TAG-E2E-054-overlay-scan-tag-status-dilarang-tidak-dikenal-dan-milik-bagian-1
title: "Overlay Scan Replace TAG: Dialog Blok D-07 untuk Tag Berstatus Tidak Paired"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-246
  - TC-FA-TAG-247
  - TC-FA-TAG-248
  - TC-FA-TAG-249
  - TC-FA-TAG-250
  - TC-FA-TAG-251
  - TC-FA-TAG-252
coverage:
  web: automated
---

# Overlay Scan Replace TAG: Dialog Blok D-07 untuk Tag Berstatus Tidak Paired

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dalam keadaan satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin. Seed idempotent Tag per status registri Global lewat fixture backend.
- Data Tag di registri Global (tanpa suffix `{runId}` karena asersi bergantung pada kode persis; tidak ada Tag yang Paired):
  - `RF-00600` RFID berstatus Available
  - `RF-00601` RFID berstatus Reserved
  - `RF-00602` RFID berstatus Retired
  - `RF-00603` RFID berstatus Damaged/Missing
  - `RF-00071` RFID berstatus To be Returned
  - `RF-00604` RFID berstatus Waiting for Approval
  - `QR-00700` QR berstatus Available (dibuat backend saat Start Print sebelumnya, belum Paired)
- Pemulihan di hook `after`: kembalikan status Tag di atas ke keadaan awal bila seeding mengubahnya. Spec ini tidak menekan `[Submit]` dan tidak mengubah data bisnis.
- State global: tidak ada. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-246: Tag Available

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai kode `RF-00600` dengan simulator reader
3. Verifikasi dialog judul `Cannot Replace TAG`, body `RF-00600 is not paired to an asset.`, tombol `[OK]`
4. Verifikasi Dialog Replace TAG tidak terbuka
5. Klik `[OK]`

### TC-FA-TAG-247: Tag Reserved

6. Klik tombol scan `Replace TAG` di toolbar tab Paired
7. Pindai kode `RF-00601` dengan simulator reader
8. Verifikasi dialog judul `Cannot Replace TAG`, body `RF-00601 is not paired to an asset.`, tombol `[OK]`
9. Verifikasi Dialog Replace TAG tidak terbuka
10. Klik `[OK]`

### TC-FA-TAG-248: Tag Retired

11. Klik tombol scan `Replace TAG` di toolbar tab Paired
12. Pindai kode `RF-00602` dengan simulator reader
13. Verifikasi dialog judul `Cannot Replace TAG`, body `RF-00602 is not paired to an asset.`, tombol `[OK]`
14. Verifikasi Dialog Replace TAG tidak terbuka
15. Klik `[OK]`

### TC-FA-TAG-249: Tag Damaged/Missing

16. Klik tombol scan `Replace TAG` di toolbar tab Paired
17. Pindai kode `RF-00603` dengan simulator reader
18. Verifikasi dialog judul `Cannot Replace TAG`, body `RF-00603 is not paired to an asset.`, tombol `[OK]`
19. Verifikasi Dialog Replace TAG tidak terbuka
20. Klik `[OK]`

### TC-FA-TAG-250: Tag To be Returned

21. Klik tombol scan `Replace TAG` di toolbar tab Paired
22. Pindai kode `RF-00071` dengan simulator reader
23. Verifikasi dialog judul `Cannot Replace TAG`, body `RF-00071 is not paired to an asset.`, tombol `[OK]`
24. Verifikasi Dialog Replace TAG tidak terbuka
25. Klik `[OK]`

### TC-FA-TAG-251: Tag Waiting for Approval

26. Klik tombol scan `Replace TAG` di toolbar tab Paired
27. Pindai kode `RF-00604` dengan simulator reader
28. Verifikasi dialog judul `Cannot Replace TAG`, body `RF-00604 is not paired to an asset.`, tombol `[OK]`
29. Verifikasi Dialog Replace TAG tidak terbuka
30. Klik `[OK]`

### TC-FA-TAG-252: kode QR hasil Start Print yang belum terpasang

31. Klik tombol scan `Replace TAG` di toolbar tab Paired
32. Pindai kode `QR-00700` dengan simulator reader
33. Verifikasi dialog judul `Cannot Replace TAG`, body `QR-00700 is not paired to an asset.`, tombol `[OK]`
34. Verifikasi Dialog Replace TAG tidak terbuka

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular. Tujuh TC memakai blok yang sama dengan parameter kode Tag dan status di Prerequisites; TC-FA-TAG-253 sampai TC-FA-TAG-256 ada di spec 055.
- Langkah penghubung (tanpa awalan `Verifikasi`): 5, 10, 15, 20, 25, dan 30 (menutup dialog blok lewat `[OK]`).
- Absence (langkah 4, 9, 14, 19, 24, 29, dan 34) didahului Verifikasi dialog blok yang tampil (langkah 3, 8, 13, 18, 23, 28, dan 33) sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-250 memakai Tag `RF-00071` berstatus To be Returned; kode itu juga dipakai sebagai Tag To be Returned pada TC-FA-TAG-4 (Pre-setup tab To Be Returned). Spec membaca kode itu sebagai data Pre-setup yang sama.
  - Tidak ada Post Condition TC yang punya langkah observasi pada spec ini ("Tidak ada data yang berubah" tidak diasersi).
  - TC-FA-TAG-252 menyebut kode QR hasil Start Print "dibuat backend saat Start Print sebelumnya"; spec menuliskan pembuatannya sebagai seed lewat fixture BE karena Start Print bukan bagian langkah TC.
  - Nilai literal Pre-setup (kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada kode persis; Lampiran A belum memuat butir untuk modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
