---
id: TC-FA-TAG-E2E-051-overlay-scan-replace-screening-dan-identifikasi-aset-paired
title: "Overlay Scan Replace TAG: Screening dan Identifikasi Aset dari Tag Paired"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-236
  - TC-FA-TAG-237
  - TC-FA-TAG-238
  - TC-FA-TAG-239
  - TC-FA-TAG-258
  - TC-FA-TAG-265
coverage:
  web: automated
---

# Overlay Scan Replace TAG: Screening dan Identifikasi Aset dari Tag Paired

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dalam keadaan satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin. Seed idempotent aset dan Tag per status registri lewat fixture backend.
- Data aset dan Tag (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis):
  - AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID): satu Tag RFID `RF-00330` berstatus Paired.
  - AST-0060 'Excavator 20 Ton - 60' (Group Plant A, TAG Type Asset Name RFID dan QR): satu Tag combined Paired, RFID `RF-00800` dan QR `QR-00800` (satu unit).
  - AST-0221 'Excavator 20 Ton - 221' (Group Plant A, Asset Status In Transfer Process, TAG Type Asset Name RFID): satu Tag RFID `RF-00140` berstatus Paired.
  - AST-0042 'Excavator 20 Ton - 42' (Group Plant A, TAG Type Asset Name RFID): satu Tag QR `QR-00230` berstatus Paired (Non-standard).
  - Stok Global: Tag RFID `RF-00412` dan `RF-00415` berstatus Available, Tag NFC `NF-00500` berstatus Available.
- Pemulihan di hook `after`: kembalikan data aset dan Tag di atas serta stok Global ke keadaan awal bila seeding mengubahnya. Spec ini tidak menekan `[Submit]` sehingga tidak mengubah data bisnis.
- State global: stok Tag per tipe di registri Global dibaca dari seed (tidak diubah). Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-236: screening overlay scan

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Verifikasi overlay scan terbuka di atas tab Paired
3. Verifikasi ButtonScan overlay dalam state Scanning
4. Verifikasi overlay punya ikon close
5. Verifikasi overlay tidak memuat kolom pencarian aset manual maupun unggah foto aset
6. Klik ikon close overlay

### TC-FA-TAG-237: Tag RFID Paired pada aset satu Tag

7. Klik tombol scan `Replace TAG` di toolbar tab Paired
8. Pindai Tag `RF-00330` dengan simulator reader
9. Verifikasi overlay scan menutup
10. Verifikasi Dialog Replace TAG terbuka di atas tab Paired dengan judul aset 'Excavator 20 Ton - 220' dan Asset ID AST-0220
11. Verifikasi bagian `TAG to replace` memuat Tag `RF-00330` tanpa checkbox
12. Verifikasi Tag `RF-00330` otomatis terpilih
13. Verifikasi Tag `RF-00330` berlabel `Scanned`
14. Verifikasi Dialog Replace TAG tidak memuat langkah Identify
15. Tutup Dialog Replace TAG tanpa menekan `[Submit]`

### TC-FA-TAG-238: Tag Paired bertipe combined

16. Klik tombol scan `Replace TAG` di toolbar tab Paired
17. Pindai Tag `RF-00800` dengan simulator reader
18. Verifikasi overlay menutup dan Dialog Replace TAG terbuka untuk aset 'Excavator 20 Ton - 60'
19. Verifikasi semua komponen Tag combined (`RF-00800` dan `QR-00800`) tercentang awal di bagian `TAG to replace`
20. Tutup Dialog Replace TAG tanpa menekan `[Submit]`

### TC-FA-TAG-239: aset In Transfer Process

21. Klik tombol scan `Replace TAG` di toolbar tab Paired
22. Pindai Tag `RF-00140` dengan simulator reader
23. Verifikasi overlay menutup dan Dialog Replace TAG terbuka untuk aset 'Excavator 20 Ton - 221'
24. Verifikasi tidak ada dialog blok yang tampil
25. Tutup Dialog Replace TAG tanpa menekan `[Submit]`

### TC-FA-TAG-258: menutup overlay tanpa Tag terbaca

26. Klik tombol scan `Replace TAG` di toolbar tab Paired
27. Klik ikon close overlay tanpa memindai apa pun
28. Verifikasi overlay scan menutup dan user tetap di tab Paired
29. Verifikasi tidak ada dialog yang tampil

### TC-FA-TAG-265: Tag QR Paired

30. Klik tombol scan `Replace TAG` di toolbar tab Paired
31. Pindai Tag `QR-00230` dengan simulator reader
32. Verifikasi overlay menutup dan Dialog Replace TAG terbuka untuk 'Excavator 20 Ton - 42'
33. Verifikasi baris Tag `QR-00230` di `TAG to replace` otomatis terpilih tanpa checkbox
34. Verifikasi baris Tag QR tidak berbadge `Scanned` maupun `Not scanned` dan tanpa tombol Scan

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): 6, 15, 20, dan 25 (menutup overlay dan Dialog Replace TAG tanpa Submit).
- Perubahan urutan Expected (R-03, bagian 8b butir 2): pada TC-FA-TAG-236 butir c (ButtonScan Scanning dan ikon close) ditulis sebelum butir b (overlay tidak memuat pencarian dan unggah foto) sebagai anchor positif untuk absence; pada TC-FA-TAG-237 butir d ditulis sebelum butir c, dengan alasan yang sama.
- Langkah 29: absence dialog didahului langkah 28 (tab Paired tampil sesudah overlay menutup) sebagai anchor. Langkah 14 dan 24 didahului langkah 10 dan 23 (dialog yang diharapkan tampil).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-258 Post Condition ("Tag RF-00330 tetap Paired" dan "tidak ada entri Changelog baru") tidak punya langkah observasi di TC; tidak diasersi dan tidak diklaim teruji (S-01, S-05).
  - TC-FA-TAG-236 Expected b memakai kata "Must NOT" untuk dua elemen; spec menuliskannya sebagai tidak memuat kolom pencarian aset manual maupun unggah foto aset.
  - TC-FA-TAG-237 Expected c ("Dialog tidak memuat langkah Identify") tidak menyebut elemen yang menandai langkah Identify; spec mengasersi hanya ketiadaan langkah itu.
  - TC-FA-TAG-237, TC-FA-TAG-238, TC-FA-TAG-239, dan TC-FA-TAG-258 tidak menyebut cara menutup Dialog Replace TAG tanpa Submit dan apakah dialog `Unsaved Changes` muncul; spec menuliskan penutupan sebagai langkah penghubung.
  - TC-FA-TAG-239 menyebut Asset Status "In Transfer Process" untuk AST-0221 tanpa cara mengaturnya; spec menuliskannya sebagai seed lewat fixture BE.
  - Simulator reader dipakai sebagai langkah rutin (bukan objek uji); mekanisme simulator tidak didefinisikan di TC maupun PRD yang dibaca.
