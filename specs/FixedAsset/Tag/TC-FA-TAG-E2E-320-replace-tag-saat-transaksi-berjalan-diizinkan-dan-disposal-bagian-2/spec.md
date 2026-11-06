---
id: TC-FA-TAG-E2E-320-replace-tag-saat-transaksi-berjalan-diizinkan-dan-disposal-bagian-2
title: "Replace TAG saat Transaksi Berjalan: Permanently Missing Diizinkan serta In Disposal Process dan Disposed Disabled"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1230
  - TC-FA-TAG-1231
  - TC-FA-TAG-1232
coverage:
  web: automated
---

# Replace TAG saat Transaksi Berjalan: Permanently Missing Diizinkan serta In Disposal Process dan Disposed Disabled

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dengan satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin; seed dan pemulihan idempotent aset, Tag per status registri (Paired, Available), transaksi, dan sesi opname lewat fixture backend; pembacaan state backend (status aset dan data transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Data (Pre-setup TC, literal): aset `AST-0020` ('Excavator 20 Ton - 20', Group Plant B) dengan Tag RFID `RF-00130` berstatus Paired; Tag RFID `RF-00500` berstatus Available di registri Global (TC-FA-TAG-1230). Keadaan awal di hook `before`: aset berstatus Permanently Missing. Langkah penghubung menyiapkan ulang status In Disposal Process dan Disposed untuk TC-FA-TAG-1231 dan 1232 (kedua TC itu tidak memerlukan Tag `RF-00500` dan reader).
- Nilai literal Pre-setup (aset `AST-0020` dan Tag `RF-00130`, `RF-00500`) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4); entri TAG Log Global (langkah 4).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset `AST-0020`, Tag `RF-00130` dan `RF-00500` (status registri Global), dan status reader simulator ke keadaan awal.
- State global: stok Tag RFID di registri Global dan status Tag pengganti diubah spec ini dan dipulihkan di hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1230: Replace TAG pada aset berstatus Permanently Missing diizinkan

1. Buka Popup Assets group Plant B
2. Pilih row action "Replace TAG" pada aset `Excavator 20 Ton - 20` (`AST-0020`)
3. Pindai Tag pengganti `RF-00500` (Available) dengan simulator reader
4. Klik `[Submit]`
5. Verifikasi toast "Success, TAG has been replaced." tampil

### TC-FA-TAG-1231: Replace TAG pada aset In Disposal Process Disabled

6. Tutup Popup Assets
7. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` dengan Tag `RF-00130` Paired berstatus In Disposal Process
8. Buka Popup Assets group Plant B
9. Arahkan kursor ke row action "Replace TAG" pada `Excavator 20 Ton - 20`
10. Verifikasi row action "Replace TAG" tetap tampil dalam keadaan Disabled
11. Verifikasi tooltip "This asset is in disposal process or already disposed." tampil

### TC-FA-TAG-1232: Replace TAG pada aset Disposed Disabled

12. Tutup Popup Assets
13. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` dengan Tag `RF-00130` Paired berstatus Disposed
14. Buka Popup Assets group Plant B
15. Arahkan kursor ke row action "Replace TAG" pada `Excavator 20 Ton - 20`
16. Verifikasi row action "Replace TAG" tetap tampil dalam keadaan Disabled
17. Verifikasi tooltip "This asset is in disposal process or already disposed." tampil

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1224 sampai 1229 ada di spec 319 dan 322.
- Langkah penghubung (tanpa awalan `Verifikasi`): 6, 7, 12, 13 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Verifikasi row action tetap tampil Disabled (langkah 10 dan 16) menjadi anchor positif bagi tooltip pada TC yang sama; tooltip diasersi sebelum kursor berpindah (bagian 8b butir 5).
- A-15: nilai literal Pre-setup (aset `AST-0020` dan Tag `RF-00130`, `RF-00500`) dipakai tanpa suffix `{runId}` karena precondition dan asersi TC bergantung pada kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4); entri TAG Log Global (langkah 4).
- Temuan untuk QA:
  - TC-FA-TAG-1230 Expected tidak menyebut keadaan setelah Replace selain toast; Post Condition kosong.
