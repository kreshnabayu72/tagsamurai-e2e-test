---
id: TC-FA-TAG-E2E-076-replace-efek-pada-perhitungan-non-standard-discard-dan-stok-bagian-2
title: "Replace: Discard Penggantian Membiarkan Aset Tetap Reported dan Non-standard, Stok Tetap Available, dan Tanpa Dokumen Approval (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-342
  - TC-FA-TAG-343
  - TC-FA-TAG-344
coverage:
  web: automated
---

# Replace: Discard Penggantian Membiarkan Aset Tetap Reported dan Non-standard, Stok Tetap Available, dan Tanpa Dokumen Approval (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 244' (AST-0244, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00332` (bertipe sesuai) dan Tag QR `QR-00432` (Non-standard) Paired, `QR-00432` punya laporan terbuka; 'Excavator 20 Ton - 220' (AST-0220) dengan Tag RFID `RF-00330` Paired.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` dan `NF-00501`, Tag QR `QR-00701` dan `QR-00702` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 24); entri TAG Log Global (langkah 24). Klik [Discard] pada langkah 8 dan 17 tidak menyimpan penggantian dan tidak menambah entri.

## Test Steps

### TC-FA-TAG-342: Discard penggantian membiarkan aset tetap Reported dan Non-standard

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 244'
3. Centang baris `QR-00432`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
5. Pindai Tag `RF-00412` dengan reader
6. Klik [Cancel] pada dialog Replace TAG
7. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
8. Klik [Discard]
9. Verifikasi dialog menutup
10. Verifikasi baris 'Excavator 20 Ton - 244' tetap berbadge `Tag Reported`
11. Verifikasi baris 'Excavator 20 Ton - 244' tetap menampilkan ikon Non-standard pada `QR-00432`

### TC-FA-TAG-343: Tag pengganti yang dipindai lalu di-Discard tetap Available (stok tidak dicadangkan)

12. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
14. Pindai Tag `RF-00412` dengan reader
15. Klik [Cancel] pada dialog Replace TAG
16. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
17. Klik [Discard]
18. Verifikasi dialog menutup tanpa penyimpanan

### TC-FA-TAG-344: Replace tidak membuat dokumen approval, jadwal, atau tugas

19. Tutup Popup Detail Assets
20. Klik tombol scan `Replace TAG` di toolbar tab Paired
21. Pindai Tag `RF-00330` dengan reader
22. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
23. Pindai Tag `RF-00412` dengan reader
24. Klik [Submit]
25. Verifikasi toast "Success, TAG has been replaced."
26. Verifikasi (baca lewat fixture BE) penggantian langsung berlaku: Tag `RF-00412` Paired pada 'Excavator 20 Ton - 220' tanpa status menunggu persetujuan
27. Buka halaman Approvals
28. Verifikasi Breadcrumb halaman Approvals tampil
29. Verifikasi Approvals tidak memuat subjek atau dokumen untuk penggantian Tag itu

## Notes

- Langkah penghubung (S-03): Popup Detail Assets ditutup sebelum memakai overlay scan; urutan TC-FA-TAG-344 (overlay scan) berada di akhir. `Verifikasi` Breadcrumb Approvals ditambahkan sebagai anchor positif asersi absence (bagian 8b butir 2); Cancel dan Discard pada TC-FA-TAG-342 dan 343 adalah langkah TC sendiri. Langkah 7 dan 16 (Verifikasi dialog `Discard Replacement` sebelum [Discard]) adalah asersi tambahan di luar Expected TC (S-03).
- Pembagian TC lintas spec: TC-FA-TAG-327 sampai 329 dan 341 ada di spec 075.
- A-15: nilai literal Pre-setup (nama aset, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 24); entri TAG Log Global (langkah 24). Klik [Discard] pada langkah 8 dan 17 tidak menyimpan penggantian dan tidak menambah entri.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Post Condition (status Tag di registri Global, entri TAG Log, Changelog, dan modul terdampak) tidak punya langkah observasi di TC dan tidak diasersi: TC-FA-TAG-342 (kedua Tag tetap Paired, laporan tetap terbuka), TC-FA-TAG-343 (`RF-00412` tetap Available di registri Global dan stok RFID Available tidak berkurang), TC-FA-TAG-344 (tidak ada jadwal, tugas, atau dokumen pengajuan).
  - Expected butir b TC-FA-TAG-344 ('penggantian langsung berlaku tanpa langkah persetujuan') tidak punya langkah observasi sendiri; spec mengasersinya lewat fixture BE.
  - TC-FA-TAG-343 menyebut stok Available sebagai Post Condition inti (judul 'stok tidak dicadangkan') tanpa langkah observasi; QA perlu menambah Expected atau langkah observasinya.
