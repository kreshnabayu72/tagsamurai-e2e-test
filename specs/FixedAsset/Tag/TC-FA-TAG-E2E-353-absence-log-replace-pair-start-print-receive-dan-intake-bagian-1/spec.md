---
id: TC-FA-TAG-E2E-353-absence-log-replace-pair-start-print-receive-dan-intake-bagian-1
title: "Absence Log: Submit Replace Ditolak dan Start Print Berhasil Tidak Menulis Changelog, Activity Log, dan System Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1088
  - TC-FA-TAG-1090
  - TC-FA-TAG-1094
coverage:
  web: automated
---

# Absence Log: Submit Replace Ditolak dan Start Print Berhasil Tidak Menulis Changelog, Activity Log, dan System Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader (lihat `suite.md`); kemampuan baca jumlah entri Changelog Paired TAG, Activity Log, dan System Log sebelum aksi (baseline, S-12); penanganan dialog cetak browser (tingkat OS) yang ditutup tanpa mencetak; seed idempotent aset dan stok Tag lewat fixture backend.
- Data aset dan Tag (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00330` berstatus Paired. Stok Global: Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Parameter: Quantity Print QR = 2.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data aset 'Excavator 20 Ton - 220' dan stok Tag ke keadaan awal lewat fixture backend. Spec ini tidak menyimpan hasil Replace; batch QR dari Start Print tidak dipulihkan fixture (lihat butir A-15).
- State global: tidak ada yang diubah selain batch QR dari Start Print (langkah 17, 27) yang tidak dipulihkan fixture. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: batch QR berstatus `Available` dari Start Print dengan Quantity 2 (langkah 17, 27); Start Print tidak menulis entri Changelog, Activity Log, maupun System Log (TC-FA-TAG-1090, 1094). Aksi tulis pada langkah 4 (Submit Replace tanpa Tag pengganti) ditolak dan [Discard] pada langkah 8 tidak menyimpan penggantian, sehingga tidak menambah entri.

## Test Steps

### TC-FA-TAG-1088: Submit ditolak V-28 dan dialog di-Discard

1. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N1)
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
3. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
4. Klik [Submit] tanpa memindai Tag pengganti
5. Verifikasi "Please verify the replacement TAG" tampil
6. Klik [Cancel]
7. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
8. Klik [Discard]
9. Tutup Popup Detail
10. Klik tombol `Changelog` di toolbar tab Paired
11. Verifikasi Modal Changelog tampil dan memuat sedikitnya satu entri lain
12. Verifikasi Modal Changelog tidak memuat entri baru untuk 'Excavator 20 Ton - 220' (jumlah entri sama dengan N1)
13. Tutup Modal Changelog

### TC-FA-TAG-1090: Start Print berhasil tidak menulis Changelog

14. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N2)
15. Klik tombol `Print QR`
16. Isi `Quantity` dengan 2
17. Klik [Start Print]
18. Tutup dialog cetak browser tanpa mencetak
19. Klik tombol `Changelog` di toolbar tab Paired
20. Verifikasi Modal Changelog tampil dan memuat sedikitnya satu entri lain
21. Verifikasi jumlah entri Changelog sama dengan N2
22. Verifikasi Modal Changelog tidak memuat entri dengan Action Print QR
23. Tutup Modal Changelog

### TC-FA-TAG-1094: Start Print berhasil tidak menulis Activity Log dan System Log

24. Catat baseline jumlah entri Activity Log lewat kemampuan baca (N3)
25. Klik tombol `Print QR` pada tab Paired
26. Isi `Quantity` dengan 2
27. Klik [Start Print]
28. Tutup dialog cetak browser tanpa mencetak
29. Buka Admin Console > Activity Log
30. Verifikasi Activity Log tampil dan memuat sedikitnya satu entri lain
31. Verifikasi jumlah entri Activity Log sama dengan N3
32. Buka Global Settings > User > Detail user pelaku > tab System Log
33. Verifikasi tab System Log tampil dan memuat sedikitnya satu entri lain
34. Verifikasi System Log pelaku tidak memuat entri Print QR

## Notes

- Spec absence (kelas g, S-05). Pemicu (Submit Replace yang ditolak, Start Print) bukan objek uji; `P-5` butir (a). Tiap TC punya baseline sendiri (langkah 1, 14, 24).
- Langkah penghubung (tanpa awalan `Verifikasi`): 9 dan 13 (menutup popup dan modal), 18 dan 28 (menutup dialog cetak browser), baseline 1, 14, 24, dan 29, 32 (navigasi ke surface log). Langkah 7 (Verifikasi dialog `Discard Replacement`, A-16 butir i) tidak ada di Expected TC dan ditambahkan oleh konvensi untuk menutup dialog Replace yang terisi lewat [Cancel].
- Anchor positif absence (bagian 8b butir 2): langkah 5 dan 11 (TC-1088), langkah 20 (TC-1090), langkah 30 dan 33 (TC-1094). Anchor berupa entri lain pada surface yang sama adalah tambahan di luar Expected TC (S-03); alasannya agar hasil kosong bukan karena surface belum dimuat.
- Total entri Changelog, Activity Log, dan System Log tidak diasersi sebagai angka absolut (S-12); semua asersi jumlah memakai selisih terhadap baseline N1, N2, N3.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: batch QR berstatus `Available` dari Start Print dengan Quantity 2 (langkah 17, 27); Start Print tidak menulis entri Changelog, Activity Log, maupun System Log (TC-FA-TAG-1090, 1094). Aksi tulis pada langkah 4 (Submit Replace tanpa Tag pengganti) ditolak dan [Discard] pada langkah 8 tidak menyimpan penggantian, sehingga tidak menambah entri.
- Temuan untuk QA:
  - TC-FA-TAG-1088 menulis "Setelah langkah 2 'Please verify the replacement TAG' tampil", padahal pesan itu hasil [Submit] tanpa pindaian (langkah 3 TC). Spec menaruh `Verifikasi` setelah [Submit] (langkah 5).
  - TC-FA-TAG-1090 dan TC-FA-TAG-1094 berlabel Manual Only karena dialog cetak browser tingkat OS; spec tetap ditulis dengan kemampuan penanganan dialog cetak sebagai kebutuhan teknis.
  - TC-FA-TAG-1090 dan TC-FA-TAG-1094 tidak menyebut cara menutup dialog cetak browser setelah [Start Print]; spec menambah langkah penghubung 18 dan 28.
  - TC-FA-TAG-1094 menulis "Detail user pelaku" tanpa menyebut nama pelaku; spec memakai akun aktor Total Control.
  - TC-FA-TAG-1088 dan TC-FA-TAG-1090 menyebut "Tidak ada entri Changelog baru" sebagai Post Condition tanpa langkah observasi tersendiri selain Expected; tidak diasersi di luar Expected.
