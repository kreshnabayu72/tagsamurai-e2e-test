---
id: TC-FA-TAG-E2E-294-sinkron-lintas-modul-registri-global-asset-detail-dan-stok-bagian-3
title: "Sinkron Lintas Modul: Tag Combined di-Separate saat Submit Replace"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1153
coverage:
  web: automated
---

# Sinkron Lintas Modul: Tag Combined di-Separate saat Submit Replace

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 60' (AST-0060, Plant A, RFID dan QR) dengan Tag combined Paired RFID `RF-00800` + QR `QR-00800`. Stok Global: Tag RFID `RF-00412` dan Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Event Log Combined TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before`; entri dicari lewat Tag `RF-00800` dan sumber Replace (S-12).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1153: Tag lama combined di-Separate saat Submit dengan sumber Replace

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 60'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
5. Klik [Submit]
6. Buka Global Settings > Tag Combine > Event Log
7. Verifikasi Event Log Combined TAG memuat entri Separate untuk Tag `RF-00800` dengan sumber Replace

## Notes

- Mode: FE+BE.
- Tidak ada langkah penghubung; seluruh langkah berasal dari TC.
- Temuan untuk QA:
  - TC-FA-TAG-1153 tidak menyebut baris yang diamati dalam Event Log Combined TAG (kolom Source/Action); spec mengikuti teks Expected 'entri Separate dengan sumber Replace'.
  - TC-FA-TAG-1153 tidak punya Post Condition yang perlu diasersi di luar Expected.
