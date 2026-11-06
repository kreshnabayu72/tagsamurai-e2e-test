---
id: TC-FA-TAG-E2E-275-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-4
title: "Entri Changelog Lama Tidak Berubah setelah Tag Diganti Lagi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1089
coverage:
  web: automated
---

# Entri Changelog Lama Tidak Berubah setelah Tag Diganti Lagi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00330` Paired.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4, 9); entri TAG Log Global (langkah 4, 9). Jumlah entri Changelog dibaca sebagai baseline lewat kemampuan baca; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1089: dua Replace berurutan pada aset yang sama

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Klik [Submit]
5. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
6. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
7. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
8. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
9. Klik [Submit]
10. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
11. Klik tombol `Changelog` di toolbar tab Paired
12. Verifikasi dua entri tampil: entri terbaru Old Value `[RFID] RF-00412` ke New Value `[RFID] RF-00415` dan entri sebelumnya tetap Old Value `[RFID] RF-00330` ke New Value `[RFID] RF-00412`
13. Verifikasi Modal Changelog tidak memuat kontrol edit atau hapus pada entri

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 5 dan 10 ("Tunggu aksi selesai", bagian 8b butir 8, karena sesudahnya terjadi pindah surface); selebihnya berasal dari TC.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4, 9); entri TAG Log Global (langkah 4, 9).
- Temuan untuk QA:
  - TC-FA-TAG-1089 Post Condition ('Entri Changelog bersifat snapshot dan tidak berubah') sama dengan Expected a yang diasersi; tidak ada langkah observasi tambahan.
