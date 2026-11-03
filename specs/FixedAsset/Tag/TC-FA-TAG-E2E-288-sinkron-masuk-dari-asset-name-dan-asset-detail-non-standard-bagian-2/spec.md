---
id: TC-FA-TAG-E2E-288-sinkron-masuk-dari-asset-name-dan-asset-detail-non-standard-bagian-2
title: "Sinkron Masuk dari Asset Detail: Tag Paired yang Dilepas Keluar dari Tab Paired"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1143
coverage:
  web: automated
---

# Sinkron Masuk dari Asset Detail: Tag Paired yang Dilepas Keluar dari Tab Paired

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): grup Excavator 20 Ton / Plant A (20 aset: 18 ber-Tag RFID dan 2 Not Paired Yet; TAG Type Asset Name RFID) dan Excavator 20 Ton / Plant B (20 aset); pemegang Update Plant A: Budi S.
- Data tambahan: aset A adalah satu aset ber-Tag RFID di Excavator 20 Ton / Plant A (kunci fixture disediakan).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: pairing Tag aset A. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1143: Tag Paired yang dilepas keluar dari tab Paired

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Catat Tag Paired milik aset A (aset dengan satu Tag RFID) pada Popup Detail
3. Pelaku kedua (Total Control) lewat sesi API melepas pairing Tag aset A hingga perubahan tersimpan
4. Muat ulang halaman TAG tab Paired (F5)
5. Verifikasi Total Assets baris Excavator 20 Ton / Plant A tidak berubah
6. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
7. Klik `Show` di samping `Not Paired Yet`
8. Verifikasi aset A tidak lagi memiliki Tag Paired: aset A muncul sebagai Not Paired Yet

## Notes

- Mode: FE+BE.
- Tidak ada langkah penghubung selain langkah dari TC. TC-FA-TAG-1133 sampai 1142 ada di spec 287.
- Temuan untuk QA:
  - TC-FA-TAG-1143 berjudul 'dilepas di Global' tetapi langkah TC ke-2 menulis 'lepas pairing Tag aset A lewat modul Asset Detail'; spec memakai pelaku kedua lewat sesi API tanpa menyebut modul pelepas.
  - TC-FA-TAG-1143 tidak menyebut cara melepas pairing di UI; mekanisme dicatat sebagai kemampuan disediakan tim FE/BE (S-13).
  - TC-FA-TAG-1143 Expected menyatakan 'muncul sebagai Not Paired Yet' dan 'Total Assets tidak berubah' dalam satu butir; spec memecahnya menjadi dua `Verifikasi` (S-01).
