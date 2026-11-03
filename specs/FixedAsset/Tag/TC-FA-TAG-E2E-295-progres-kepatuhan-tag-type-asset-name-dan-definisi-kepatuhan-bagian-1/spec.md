---
id: TC-FA-TAG-E2E-295-progres-kepatuhan-tag-type-asset-name-dan-definisi-kepatuhan-bagian-1
title: "Progres Kepatuhan TAG Type pada Detail Asset Name dan Definisi Kepatuhan, Bagian 1"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1137
  - TC-FA-TAG-1138
  - TC-FA-TAG-1152
  - TC-FA-TAG-1497
  - TC-FA-TAG-1498
  - TC-FA-TAG-1499
coverage:
  web: automated
---

# Progres Kepatuhan TAG Type pada Detail Asset Name dan Definisi Kepatuhan, Bagian 1

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): Asset Name 'Excavator 20 Ton' (RFID) dengan 40 aset Active dalam scope client (Plant A 20 dan Plant B 20; 33 patuh sebelum perubahan: 18 aset Plant A dan 15 aset Plant B, 5 aset Plant B Non-standard); pada TC-FA-TAG-1152: 39 aset ber-Tag RFID dan 'Excavator 20 Ton - 42' (Plant A) ber-Tag QR `QR-00230` (Non-standard); Asset Name `Drill Press` dengan 1 aset ber-Tag QR; `Multi Type Item` (RFID dan NFC) dengan 4 aset Active (aset 1 ber-Tag Paired RFID dan NFC; aset 2 hanya RFID; aset 3 Not Paired Yet; aset 4 RFID, NFC, dan QR dengan QR Non-standard); `Non-TAG Pallet` (Non-TAG) dengan 3 aset Active (aset 1 dan 2 tanpa Tag; aset 3 ber-Tag Paired QR); `GPS Only Unit` (GPS saja) dengan 2 aset Active (aset 1 tanpa Tag; aset 2 ber-Tag Paired RFID).
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: TAG Type Asset Name 'Excavator 20 Ton' dan 'Drill Press'. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1137: progres kepatuhan tampil di Asset Name setelah perubahan (jamak)

1. Buka Fixed Asset > Settings > Asset Name
2. Klik nama Asset Name `Excavator 20 Ton` untuk membuka Detail Asset Name
3. Verifikasi progres kepatuhan TAG Type sebelum perubahan tampil `33 / 40 assets match the TAG type`
4. Tutup popup Detail Asset Name
5. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Excavator 20 Ton' dari RFID menjadi NFC hingga perubahan tersimpan
6. Klik nama Asset Name `Excavator 20 Ton` untuk membuka Detail Asset Name
7. Verifikasi progres kepatuhan TAG Type setelah perubahan tampil `0 / 40 assets match the TAG type`: `[N]` = 40 menghitung seluruh aset Active Asset Name Excavator 20 Ton dalam scope client (Plant A 20 dan Plant B 20), tidak dipotong per group

### TC-FA-TAG-1138: progres kepatuhan dengan bentuk tunggal untuk satu aset

8. Tutup popup Detail Asset Name
9. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Drill Press' dari QR menjadi RFID hingga perubahan tersimpan
10. Klik nama Asset Name `Drill Press` untuk membuka Detail Asset Name
11. Verifikasi progres kepatuhan TAG Type tampil `0 / 1 asset matches the TAG type` (bentuk tunggal; Tag QR menjadi Non-standard dan belum ada Tag RFID)

### TC-FA-TAG-1152: progres kepatuhan bertambah setelah Tag Non-standard diganti

12. Pulihkan TAG Type 'Excavator 20 Ton' ke RFID dan data aset lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
13. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
14. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 42'
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
16. Klik [Submit]
17. Buka Fixed Asset > Settings > Asset Name
18. Klik nama Asset Name `Excavator 20 Ton` untuk membuka Detail Asset Name
19. Verifikasi progres kepatuhan TAG Type menampilkan `40 / 40 assets match the TAG type`: `[N]` = 40 menghitung seluruh aset Active Asset Name itu dalam scope client (Plant A dan Plant B), tidak dipotong per group

### TC-FA-TAG-1497: aset patuh hanya bila tidak Non-standard dan memiliki Tag Paired untuk setiap tipe yang dituntut

20. Tutup popup Detail Asset Name
21. Klik nama Asset Name `Multi Type Item` untuk membuka Detail Asset Name
22. Verifikasi progres kepatuhan TAG Type tampil `1 / 4 assets match the TAG type`
23. Verifikasi aset 2 (hanya sebagian tipe yang dituntut), aset 3 (Not Paired Yet), dan aset 4 (ber-Tag Non-standard) tidak terhitung patuh

### TC-FA-TAG-1498: Asset Name Non-TAG, aset tanpa Tag patuh dan aset ber-Tag Paired tidak

24. Tutup popup Detail Asset Name
25. Klik nama Asset Name `Non-TAG Pallet` untuk membuka Detail Asset Name
26. Verifikasi progres kepatuhan TAG Type tampil `2 / 3 assets match the TAG type`
27. Verifikasi aset 3 tidak terhitung karena Tag Paired pada Asset Name Non-TAG Non-standard
28. Verifikasi aset 1 dan aset 2 terhitung walau tanpa Tag karena Asset Name tidak menuntut tipe Tag

### TC-FA-TAG-1499: Asset Name yang hanya bertipe GPS

29. Tutup popup Detail Asset Name
30. Klik nama Asset Name `GPS Only Unit` untuk membuka Detail Asset Name
31. Verifikasi progres kepatuhan TAG Type tampil `2 / 2 assets match the TAG type`
32. Verifikasi aset 2 terhitung karena tipe GPS belum dievaluasi sehingga Tag RFID-nya tidak Non-standard
33. Verifikasi aset 1 terhitung karena Asset Name tidak menuntut tipe yang dikelola menu TAG

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 4, 8, 12, 20, 24 dan 29 (menutup popup Detail Asset Name, memulihkan data lewat fixture antar TC, S-09).
- TC-FA-TAG-1500 ada di spec 296.
- Temuan untuk QA:
  - TC-FA-TAG-1137 dan 1138 langkah TC ke-1 mengubah TAG Type lewat Modul Asset Name; spec memicunya lewat sesi API karena objek uji adalah progres kepatuhan, bukan form Asset Name.
  - TC-FA-TAG-1152 Expected menulis '(sebelumnya 39 / 40)' sebagai keterangan; spec tidak mengasersi nilai sebelumnya (tidak ada langkah observasi di TC).
  - TC-FA-TAG-1137 sampai 1499 tidak punya Post Condition yang perlu diasersi di luar Expected.
