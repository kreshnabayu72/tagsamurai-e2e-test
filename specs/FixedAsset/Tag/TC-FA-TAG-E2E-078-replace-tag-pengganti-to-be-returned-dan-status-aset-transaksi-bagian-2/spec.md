---
id: TC-FA-TAG-E2E-078-replace-tag-pengganti-to-be-returned-dan-status-aset-transaksi-bagian-2
title: "Replace: Aset Berstatus Menunggu Serah Terima atau Approval, In Transfer Process, Sesi Opname Berjalan, dan Under Maintenance Berjalan Normal (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-350
  - TC-FA-TAG-351
  - TC-FA-TAG-352
  - TC-FA-TAG-353
coverage:
  web: automated
---

# Replace: Aset Berstatus Menunggu Serah Terima atau Approval, In Transfer Process, Sesi Opname Berjalan, dan Under Maintenance Berjalan Normal (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag RFID `RF-00130` Paired; status aset diatur fixture BE per baris tabel di bawah. Tag `RF-00412` Available (stok Global, dipakai sebagai precondition TC).
- Tabel "Status aset" (parameter langkah yang diulang):

| TC | Status aset |
|---|---|
| TC-FA-TAG-350 | Menunggu serah terima atau approval transaksi |
| TC-FA-TAG-351 | In Transfer Process |
| TC-FA-TAG-352 | dalam sesi opname yang berjalan |
| TC-FA-TAG-353 | Under Maintenance |

- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Replace pada aset dengan status transaksi berjalan (TC-FA-TAG-350, TC-FA-TAG-351, TC-FA-TAG-352, TC-FA-TAG-353)

1. Untuk setiap baris tabel "Status aset" pada Prerequisites, lakukan langkah 2 sampai 12
2. Atur lewat fixture BE: aset AST-0220 berstatus sesuai kolom "Status aset" baris yang sedang dijalankan, dengan satu Tag RFID `RF-00130` Paired dan Tag `RF-00412` Available
3. Muat ulang halaman Fixed Asset > TAG > Paired
4. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
5. Verifikasi row action `Replace TAG` pada baris 'Excavator 20 Ton - 220' Enabled
6. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
7. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
8. Pindai Tag `RF-00412` dengan reader
9. Klik [Submit]
10. Verifikasi toast "Success, TAG has been replaced."
11. Verifikasi dialog menutup
12. Tutup Popup Detail Assets

## Notes

- Langkah penghubung (S-03): Atur status aset lewat fixture BE, muat ulang halaman, dan tutup Popup Detail Assets pada tiap iterasi; langkah yang diulang per baris tabel adalah langkah 2 sampai 12.
- Pembagian TC lintas spec: TC-FA-TAG-345 sampai 347 ada di spec 077 dan TC-FA-TAG-348, 349, dan 354 ada di spec 079.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Alasan di atas sekitar 35 langkah: satu blok identik diulang untuk tiap baris tabel "Status aset" (langkah 2 sampai 12, bagian 8b butir 7); parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat, dan tiap `Verifikasi` tetap satu per klausa.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Post Condition (status Tag di registri Global, entri TAG Log, Changelog, dan modul terdampak) tidak punya langkah observasi di TC dan tidak diasersi: TC-FA-TAG-350 sampai 353 (Tag `RF-00412` Paired pada AST-0220 dan status aset tidak berubah).
  - TC-FA-TAG-350 dan 352 menulis status aset sebagai frasa deskriptif ('Menunggu serah terima atau approval transaksi', 'dalam sesi opname yang berjalan') yang bukan nilai status baku; fixture BE perlu pemetaan ke nilai status aset yang berlaku.
