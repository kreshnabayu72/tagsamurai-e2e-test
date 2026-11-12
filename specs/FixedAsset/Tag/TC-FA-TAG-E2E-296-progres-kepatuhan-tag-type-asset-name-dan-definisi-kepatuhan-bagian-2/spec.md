---
id: TC-FA-TAG-E2E-296-progres-kepatuhan-tag-type-asset-name-dan-definisi-kepatuhan-bagian-2
title: "Progres Kepatuhan TAG Type Tidak Tampil bila Jumlah Aset N Sama dengan 0"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1500
coverage:
  web: automated
---

# Progres Kepatuhan TAG Type Tidak Tampil bila Jumlah Aset N Sama dengan 0

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix): Asset Name `Empty Pallet` tanpa aset; Asset Name `Draft Only Pallet` hanya memiliki 2 aset berlifecycle Draft (`[N]` = 0 untuk keduanya).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data seed ke keadaan awal lewat fixture backend dan sesi ke akun default suite.
- State global: tidak ada yang diubah spec ini. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1500: baris progres tidak tampil bila [N] = 0

1. Buka Fixed Asset > Settings > Asset Name
2. Klik nama Asset Name `Empty Pallet` untuk membuka Detail Asset Name
3. Verifikasi Detail Asset Name `Empty Pallet` tampil dengan nilai TAG Type
4. Verifikasi baris progres kepatuhan TAG Type tidak tampil pada `Empty Pallet`
5. Verifikasi tidak ada teks `0 / 0` dan tidak ada ruang kosong di bawah nilai TAG Type `Empty Pallet`
6. Tutup popup Detail Asset Name
7. Klik nama Asset Name `Draft Only Pallet` untuk membuka Detail Asset Name
8. Verifikasi Detail Asset Name `Draft Only Pallet` tampil dengan nilai TAG Type
9. Verifikasi baris progres kepatuhan TAG Type tidak tampil pada `Draft Only Pallet` (aset Draft tidak masuk himpunan)
10. Verifikasi tidak ada teks `0 / 0` dan tidak ada ruang kosong di bawah nilai TAG Type `Draft Only Pallet`

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 6 (menutup popup Detail Asset Name). TC-FA-TAG-1137, 1138, 1152, 1497, 1498, dan 1499 ada di spec 295.
- Absence baris progres: didahului `Verifikasi` Detail Asset Name dengan nilai TAG Type tampil sebagai anchor positif (bagian 8b butir 2).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1500 Expected b ('tidak ada ruang kosong di bawah nilai TAG Type') tidak punya ukuran terukur; spec mengasersi sesuai teks TC.
  - TC-FA-TAG-1500 tidak punya Post Condition yang perlu diasersi di luar Expected.
