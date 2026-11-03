---
id: TC-FA-TAG-E2E-083-replace-tag-combined-slot-validasi-v-25-v-26-dan-submit-bagian-3
title: "Replace dengan Tag Combined: Caption Tag Sama, Scan Current TAG, dan Pilih Komponen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-366
  - TC-FA-TAG-369
  - TC-FA-TAG-370
coverage:
  web: automated
---

# Replace dengan Tag Combined: Caption Tag Sama, Scan Current TAG, dan Pilih Komponen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 60' (AST-0060, Group Plant A, TAG Type Asset Name RFID dan QR) dengan satu Tag combined Paired RFID `RF-00800` + QR `QR-00800`; 'Excavator 20 Ton - 61' (AST-0061, TAG Type Asset Name RFID, NFC, dan QR) dengan Tag combined Paired RFID `RF-00801` + QR `QR-00801` dan Tag NFC `NF-00096` Paired.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: tidak ada Replace yang di-submit sehingga status Tag tidak berubah; fixture backend tetap memulihkan data di hook `before` dan `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-366: Tag pengganti combined yang memuat kode Tag lama menampilkan caption S-33

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 60'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `QR-00800` dengan reader
5. Verifikasi caption "This TAG is the same as the current TAG."
6. Verifikasi slot `RFID TAG` dan `QR TAG` tetap `Not scanned`

### TC-FA-TAG-369: Scan Current TAG pada Tag lama combined menandai komponen di daftar lepas sebagai Scanned

7. Klik [Cancel] pada dialog Replace TAG
8. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 60'
9. Klik ButtonScan `Scan RFID` pada baris combined
10. Pindai Tag `RF-00800` dengan reader
11. Verifikasi setiap komponen Tag combined yang ada di daftar lepas ditandai `Scanned`

### TC-FA-TAG-370: Memilih satu komponen Tag lama combined mencentang semua komponen, membatalkan membatalkan semuanya

12. Klik [Cancel] pada dialog Replace TAG
13. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 61'
14. Centang baris `RF-00801`
15. Verifikasi baris `RF-00801` dan `QR-00801` keduanya tercentang
16. Hapus centang baris `QR-00801`
17. Verifikasi kedua baris tidak tercentang
18. Verifikasi baris `NF-00096` tidak berubah
19. Klik [Cancel] pada dialog Replace TAG
20. Tutup Popup Detail Assets

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC (langkah 7, 12, dan 19); TC-FA-TAG-370 berurutan dengan TC-FA-TAG-366 dan 369 karena memakai Popup 'Excavator 20 Ton'; Popup Detail ditutup pada langkah 20.
- Pembagian TC lintas spec: TC-FA-TAG-355 sampai 364 ada di spec 081 dan 082; TC-FA-TAG-367 dan 368 ada di spec 382.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name atau di akhir.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Judul TC-FA-TAG-370 memuat pengulangan kata ('membatalkan membatalkan'); spec mengikuti judul sebagai nama blok.
  - Expected TC-FA-TAG-370 merujuk 'Setelah langkah 2' dan 'Setelah langkah 3' padahal aksi centang dan hapus centang adalah langkah 3 dan 4 di TC; spec memetakan asersi ke aksi yang bersesuaian.
  - Tidak ada Post Condition pada TC-FA-TAG-366, 369, dan 370.
