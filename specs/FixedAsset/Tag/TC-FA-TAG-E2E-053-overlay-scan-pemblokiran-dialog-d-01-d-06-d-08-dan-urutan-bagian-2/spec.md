---
id: TC-FA-TAG-E2E-053-overlay-scan-pemblokiran-dialog-d-01-d-06-d-08-dan-urutan-bagian-2
title: "Overlay Scan Replace TAG: Dialog Blok D-08 untuk Tag Combined NFC dan QR Saat Stok Habis"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1456
coverage:
  web: automated
---

# Overlay Scan Replace TAG: Dialog Blok D-08 untuk Tag Combined NFC dan QR Saat Stok Habis

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dalam keadaan satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin. Seed idempotent aset, Tag combined, dan stok Tag per tipe di registri Global lewat fixture backend.
- Data aset dan Tag (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0130 'Laptop Pro 14 - 30' (Group HQ, TAG Type Asset Name NFC dan QR) punya Tag combined NFC+QR `NF-00820` / `QR-00820` berstatus Paired. Stok Global: tidak ada Tag NFC maupun QR berstatus Available (diatur di hook `before`, dipakai sebagai precondition TC).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan stok Tag NFC dan QR di registri Global serta data aset dan Tag ke keadaan awal. Spec ini tidak menekan `[Submit]`.
- State global: stok Tag NFC dan QR di registri Global diubah spec ini. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-1456: stok NFC dan QR 0 pada Tag combined

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag combined `NF-00820` dengan simulator reader
3. Verifikasi dialog judul `Cannot Replace TAG`, body `No available NFC and QR TAG in stock. Activate TAG in Global Settings > TAG.`, tombol `[OK]`
4. Verifikasi Dialog Replace TAG tidak terbuka
5. Klik `[OK]`

## Notes

- Mode: FE+BE. TC-FA-TAG-244 (stok RFID 0) ada di spec 052.
- Langkah penghubung (tanpa awalan `Verifikasi`): 5 (menutup dialog blok lewat `[OK]`).
- Langkah 4 (absence) didahului langkah 3 (dialog blok tampil) sebagai anchor positif (bagian 8b butir 2).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1456 Post Condition ("Tidak ada data yang berubah") tidak punya langkah observasi; tidak diasersi.
  - TC-FA-TAG-1456 tidak menyebut apakah pesan stok untuk Tag combined selalu menyebut urutan "NFC and QR"; spec mengikuti teks body di TC.
