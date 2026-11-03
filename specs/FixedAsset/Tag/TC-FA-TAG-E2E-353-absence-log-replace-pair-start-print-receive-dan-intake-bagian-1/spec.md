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
- Data aset dan Tag (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired. Stok Global: Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Parameter: Quantity Print QR = 2.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data aset 'Excavator 20 Ton - 220' dan stok Tag ke keadaan awal lewat fixture backend. Spec ini tidak menyimpan hasil Replace atau cetak.
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1088: Submit ditolak V-28 dan dialog di-Discard

1. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N1)
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
3. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
4. Klik [Submit] tanpa memindai Tag pengganti
5. Verifikasi "Please verify the replacement TAG" tampil
6. Klik [Cancel]
7. Klik [Discard]
8. Tutup Popup Detail
9. Klik tombol `Changelog` di toolbar tab Paired
10. Verifikasi Modal Changelog tampil dan memuat sedikitnya satu entri lain
11. Verifikasi Modal Changelog tidak memuat entri baru untuk 'Excavator 20 Ton - 220' (jumlah entri sama dengan N1)
12. Tutup Modal Changelog

### TC-FA-TAG-1090: Start Print berhasil tidak menulis Changelog

13. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N2)
14. Klik tombol `Print QR`
15. Isi `Quantity` dengan 2
16. Klik [Start Print]
17. Tutup dialog cetak browser tanpa mencetak
18. Klik tombol `Changelog` di toolbar tab Paired
19. Verifikasi Modal Changelog tampil dan memuat sedikitnya satu entri lain
20. Verifikasi jumlah entri Changelog sama dengan N2
21. Verifikasi Modal Changelog tidak memuat entri dengan Action Print QR
22. Tutup Modal Changelog

### TC-FA-TAG-1094: Start Print berhasil tidak menulis Activity Log dan System Log

23. Catat baseline jumlah entri Activity Log lewat kemampuan baca (N3)
24. Klik tombol `Print QR` pada tab Paired
25. Isi `Quantity` dengan 2
26. Klik [Start Print]
27. Tutup dialog cetak browser tanpa mencetak
28. Buka Admin Console > Activity Log
29. Verifikasi Activity Log tampil dan memuat sedikitnya satu entri lain
30. Verifikasi jumlah entri Activity Log sama dengan N3
31. Buka Global Settings > User > Detail user pelaku > tab System Log
32. Verifikasi tab System Log tampil dan memuat sedikitnya satu entri lain
33. Verifikasi System Log pelaku tidak memuat entri Print QR

## Notes

- Spec absence (kelas g, S-05). Pemicu (Submit Replace yang ditolak, Start Print) bukan objek uji; `P-5` butir (a). Tiap TC punya baseline sendiri (langkah 1, 13, 23).
- Langkah penghubung (tanpa awalan `Verifikasi`): 8 dan 12 (menutup popup dan modal), 17 dan 27 (menutup dialog cetak browser), baseline 1, 13, 23, dan 28, 31 (navigasi ke surface log).
- Anchor positif absence (bagian 8b butir 2): langkah 5 dan 10 (TC-1088), langkah 19 (TC-1090), langkah 29 dan 32 (TC-1094). Anchor berupa entri lain pada surface yang sama adalah tambahan di luar Expected TC (S-03); alasannya agar hasil kosong bukan karena surface belum dimuat.
- Total entri Changelog, Activity Log, dan System Log tidak diasersi sebagai angka absolut (S-12); semua asersi jumlah memakai selisih terhadap baseline N1, N2, N3.
- Temuan untuk QA:
  - TC-FA-TAG-1088 menulis "Setelah langkah 2 'Please verify the replacement TAG' tampil", padahal pesan itu hasil [Submit] tanpa pindaian (langkah 3 TC). Spec menaruh `Verifikasi` setelah [Submit] (langkah 5).
  - TC-FA-TAG-1090 dan TC-FA-TAG-1094 berlabel Manual Only karena dialog cetak browser tingkat OS; spec tetap ditulis dengan kemampuan penanganan dialog cetak sebagai kebutuhan teknis.
  - TC-FA-TAG-1090 dan TC-FA-TAG-1094 tidak menyebut cara menutup dialog cetak browser setelah [Start Print]; spec menambah langkah penghubung 17 dan 27.
  - TC-FA-TAG-1094 menulis "Detail user pelaku" tanpa menyebut nama pelaku; spec memakai akun aktor Total Control.
  - TC-FA-TAG-1088 dan TC-FA-TAG-1090 menyebut "Tidak ada entri Changelog baru" sebagai Post Condition tanpa langkah observasi tersendiri selain Expected; tidak diasersi di luar Expected.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
