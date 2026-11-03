---
id: TC-FA-TAG-E2E-303-pencatatan-tag-log-replace-tag-qr-lama-keluar-dari-registri
title: "Pencatatan TAG Log Replace: Tag QR Lama Keluar dari Registri"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1098
coverage:
  web: automated
---

# Pencatatan TAG Log Replace: Tag QR Lama Keluar dari Registri

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 42' (AST-0042, Plant A, RFID) dengan Tag QR `QR-00230` Paired (Non-standard).
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1098: Tag QR lama yang diganti tidak punya entri TAG Log

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 42'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Klik [Submit]
5. Buka Global Settings > TAG
6. Ketik Search `QR-00230`, tekan Enter
7. Verifikasi Illustration `No results found`: pencarian `QR-00230` tidak menemukan Tag di registri
8. Verifikasi tidak ada entri TAG Log untuk `QR-00230`

## Notes

- Mode: FE+BE.
- Tidak ada langkah penghubung; TC-FA-TAG-1098 adalah satu-satunya TC spec ini. TC-FA-TAG-1095 sampai 1097 ada di spec 277.
- Absence (pencarian `QR-00230` tanpa hasil) memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-1098 Expected b ('Tidak ada entri TAG Log untuk QR-00230') tidak punya langkah observasi terpisah dari pencarian registri; spec menuliskannya sebagai satu `Verifikasi` yang bergantung pada hasil pencarian.
  - TC-FA-TAG-1098 Post Condition ('Tag QR lama keluar dari registri bersama riwayatnya') sama dengan Expected a yang diasersi.
