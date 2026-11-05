---
id: TC-FA-TAG-E2E-062-dialog-replace-tag-pemilihan-tag-centang-dan-slot-pengganti-bagian-2
title: "Dialog Replace TAG: Tag Non-standard Tidak Tercentang Otomatis dan Slot Tipe Wajib yang Masih Kosong (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-281
  - TC-FA-TAG-282
coverage:
  web: automated
---

# Dialog Replace TAG: Tag Non-standard Tidak Tercentang Otomatis dan Slot Tipe Wajib yang Masih Kosong (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 244' (AST-0244, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00332` (bertipe sesuai) dan Tag QR `QR-00432` (Non-standard) Paired; 'Excavator 20 Ton - 45' (AST-0045, TAG Type Asset Name RFID dan NFC) dengan Tag NFC `NF-00093` (bertipe sesuai) dan Tag QR `QR-00233` (Non-standard) Paired, tanpa Tag RFID.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 6); entri TAG Log Global (langkah 6).

## Test Steps

### TC-FA-TAG-281: Tag Non-standard tidak tercentang otomatis dan tetap Paired bila tidak dicentang

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00332` dengan reader
3. Verifikasi checkbox `QR-00432` tidak tercentang awal
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
5. Pindai Tag `RF-00412` dengan reader
6. Klik [Submit]
7. Verifikasi toast "Success, TAG has been replaced."
8. Verifikasi (baca lewat fixture BE) Tag `QR-00432` tetap Paired pada 'Excavator 20 Ton - 244'
9. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
10. Verifikasi baris 'Excavator 20 Ton - 244' tetap menampilkan ikon peringatan Non-standard pada `QR-00432`

### TC-FA-TAG-282: Tag Non-standard yang terpindai mendapat slot bertipe wajib Asset Name yang masih kosong

11. Tutup Popup Detail Assets
12. Klik tombol scan `Replace TAG` di toolbar tab Paired
13. Pindai Tag `QR-00233` dengan reader
14. Verifikasi baris `QR-00233` tercentang
15. Verifikasi baris `NF-00093` tidak tercentang
16. Verifikasi bagian `Replacement TAG` memuat satu slot `RFID TAG` (tipe wajib Asset Name yang masih kosong)
17. Verifikasi (baca lewat fixture BE) Tag `NF-00093` tidak tersentuh dan tetap Paired
18. Klik [Cancel] pada dialog Replace TAG

## Notes

- Langkah penghubung (S-03): Popup Detail Assets dibuka untuk mengamati baris aset sesudah Submit dan ditutup sebelum TC-FA-TAG-282 yang memakai overlay scan; [Cancel] menutup dialog di akhir spec.
- Pembagian TC lintas spec: TC-FA-TAG-276 sampai 280 ada di spec 061.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 6); entri TAG Log Global (langkah 6).
- Temuan untuk QA:
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - Expected butir c TC-FA-TAG-281 dan Post Condition butir a dan b tumpang tindih (Tag `QR-00432` tetap Paired); spec mengasersi butir Expected c lewat fixture BE dan UI, Post Condition lainnya tidak punya langkah observasi.
