---
id: TC-FA-TAG-E2E-060-dialog-replace-tag-screening-blok-info-dan-bagian-tag-to-bagian-3
title: "Dialog Replace TAG: Keselarasan Layout Kolom, Lebar Kolom Scan, dan Jarak Divider"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1449
coverage:
  web: automated
---

# Dialog Replace TAG: Keselarasan Layout Kolom, Lebar Kolom Scan, dan Jarak Divider

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 44' (AST-0044, Group Plant B, TAG Type Asset Name RFID) dengan Tag RFID `RF-00132` dan Tag QR `QR-00232` (Non-standard) Paired.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1449: Keselarasan layout Dialog Replace TAG

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant B untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 44'
3. Amati bagian `TAG to replace`, bagian `Replacement TAG`, dan blok info dialog
4. Verifikasi tidak ada baris judul kolom; kolom dipisahkan jarak (gap) saja
5. Verifikasi tiap kolom menempati posisi vertikal yang sama di setiap baris, termasuk ruang yang dicadangkan untuk baris Tag QR tanpa tombol Scan, sehingga semua baris sejajar
6. Verifikasi lebar kolom Scan sama di bagian `TAG to replace` dan bagian `Replacement TAG`
7. Verifikasi label dan nilai blok info rata kiri pada satu grid
8. Verifikasi jarak Divider antar bagian konsisten, begitu pula jarak antara judul bagian dan isinya
9. Klik [Cancel] pada dialog Replace TAG
10. Tutup Popup Detail Assets

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG dan Popup Detail Assets ditutup di akhir spec; langkah Amati adalah aksi pengamatan tanpa asersi.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Temuan untuk QA:
  - Tag `RF-00132` dan `QR-00232` pada TC-FA-TAG-1449 dipasang di aset AST-0044 (Plant B), sedangkan TC-FA-TAG-271 sampai 282 memasang kode yang sama di AST-0244 (Plant A); satu kode Tag tidak dapat Paired di dua aset sekaligus. Spec mengikuti TC dan fixture BE menyiapkan keduanya terpisah per spec.
  - Tidak ada Post Condition pada TC-FA-TAG-1449; asersi jarak dan kesejajaran bersifat visual (kemampuan ukur layout disediakan tim FE di tahap script).
