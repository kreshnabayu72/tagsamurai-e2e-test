---
id: TC-FA-TAG-E2E-058-dialog-replace-tag-screening-blok-info-dan-bagian-tag-to-bagian-1
title: "Dialog Replace TAG: Screening Header, Footer, Blok Info Aset, dan Status Aset (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-266
  - TC-FA-TAG-267
  - TC-FA-TAG-268
  - TC-FA-TAG-269
  - TC-FA-TAG-270
coverage:
  web: automated
---

# Dialog Replace TAG: Screening Header, Footer, Blok Info Aset, dan Status Aset (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220) dengan satu Tag RFID `RF-00130` berstatus Paired, TAG Type Asset Name RFID, berfoto, Group `Line 1` (anak dari Plant A), Brand `Caterpillar`, Model/Type `320 GC`, Asset Status Available (keadaan awal TC-FA-TAG-266 sampai 268). Atribut aset diubah fixture BE sebelum TC-FA-TAG-269 (tanpa foto, Brand dan Model/Type kosong) dan sebelum TC-FA-TAG-270 (berstatus Assigned dan punya laporan Tag terbuka); pemulihan atribut di hook `after`.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415` Available, Tag NFC `NF-00500` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-266: Screening Dialog Replace TAG: header, layer, dan footer

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00130` dengan reader
3. Verifikasi dialog Replace TAG (Size MD) terbuka di atas tab Paired tanpa Breadcrumb dan tanpa pindah halaman
4. Verifikasi header dialog hanya `Replace TAG`
5. Verifikasi footer dialog memuat tombol [Cancel] dan [Submit]
6. Klik backdrop di luar dialog
7. Verifikasi dialog tidak tertutup oleh klik backdrop

### TC-FA-TAG-267: Screening blok info Dialog Replace TAG: baris atas aset

8. Klik [Cancel] pada dialog Replace TAG
9. Klik tombol scan `Replace TAG` di toolbar tab Paired
10. Pindai Tag `RF-00130` dengan reader
11. Arahkan kursor ke ikon tipe Tag pada baris atas blok info
12. Verifikasi thumbnail foto aset tampil di kiri tanpa kontrol unggah foto
13. Verifikasi judul `Excavator 20 Ton - 220`
14. Verifikasi Asset ID `AST-0220` tampil di bawah judul dengan teks lebih kecil dan warna sekunder
15. Verifikasi Divider vertikal dan satu ikon tipe Tag tampil setelah Asset ID
16. Verifikasi tooltip ikon Tag `RFID · RF-00130`
17. Verifikasi baris atas tidak memuat TAG Code sebagai teks, ikon peringatan Non-standard, maupun penanda `Scanned`

### TC-FA-TAG-268: Screening blok info Dialog Replace TAG: grid Brand, Model/Type, Group, Asset Status

18. Klik [Cancel] pada dialog Replace TAG
19. Klik tombol scan `Replace TAG` di toolbar tab Paired
20. Pindai Tag `RF-00130` dengan reader
21. Arahkan kursor ke badge Group pada grid info
22. Verifikasi grid `Label: Value` 2 kolom dengan urutan label `Brand`, `Model/Type`, `Group`, `Asset Status`
23. Verifikasi `Brand` dan `Model/Type` berupa Badge Dark bernilai `Caterpillar` dan `320 GC`
24. Verifikasi `Group` berupa Badge Primary
25. Verifikasi hover badge Group menampilkan hierarki penuh `Plant A > Line 1`
26. Verifikasi `Asset Status` berupa badge `Available`

### TC-FA-TAG-269: Blok info Dialog Replace TAG pada aset tanpa foto, Brand, dan Model/Type

27. Klik [Cancel] pada dialog Replace TAG
28. Atur aset AST-0220 lewat fixture BE: tanpa foto, Brand kosong, Model/Type kosong
29. Klik tombol scan `Replace TAG` di toolbar tab Paired
30. Pindai Tag `RF-00130` dengan reader
31. Verifikasi thumbnail tampil kosong
32. Verifikasi `Brand` dan `Model/Type` tampil `—`

### TC-FA-TAG-270: Blok info Dialog Replace TAG: Asset Status multi-badge diurut A-Z

33. Klik [Cancel] pada dialog Replace TAG
34. Atur aset AST-0220 lewat fixture BE: Asset Status Assigned dan punya laporan Tag terbuka (badge Tag Reported)
35. Klik tombol scan `Replace TAG` di toolbar tab Paired
36. Pindai Tag `RF-00130` dengan reader
37. Verifikasi sel `Asset Status` memuat dua badge berurutan A-Z: `Assigned` lalu `Tag Reported`
38. Klik [Cancel] pada dialog Replace TAG

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC dan di akhir spec; pengaturan atribut aset AST-0220 lewat fixture BE sebelum TC-FA-TAG-269 dan TC-FA-TAG-270. Hover pada ikon Tag dan badge Group adalah aksi pemicu tooltip.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Alasan di atas sekitar 35 langkah: semua blok satu kelas (fungsional), satu dialog dan satu dataset aset; kelima TC berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; tambahan langkah berasal dari langkah penghubung antar-TC.
- Temuan untuk QA:
  - TC-FA-TAG-266 sampai 268 menyebut Group aset berbeda (Plant A pada 266 dan 267, `Line 1` anak Plant A pada 268) untuk aset yang sama; spec memakai satu keadaan awal (Group `Line 1`).
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Tidak ada Post Condition pada TC-FA-TAG-266 sampai 270.
