---
id: TC-FA-TAG-E2E-063-dialog-replace-tag-scan-current-tag-badge-dan-penolakan-bagian-1
title: "Dialog Replace TAG: Scan Current TAG, Badge Scanned atau Not scanned, dan Penolakan Tag Lama Salah (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-283
  - TC-FA-TAG-284
  - TC-FA-TAG-285
  - TC-FA-TAG-286
  - TC-FA-TAG-287
coverage:
  web: automated
---

# Dialog Replace TAG: Scan Current TAG, Badge Scanned atau Not scanned, dan Penolakan Tag Lama Salah (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00130` Paired; 'Excavator 20 Ton - 42' (AST-0042) dengan Tag QR `QR-00230` Paired (Non-standard); 'Excavator 20 Ton - 244' (AST-0244) dengan Tag RFID `RF-00132` dan Tag QR `QR-00232` (Non-standard) Paired; 'Laptop Pro 14 - 8' (AST-0108, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00092` dan Tag QR `QR-00300` Paired.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-283: Scan Current TAG pada Tag RFID memberi tanda terverifikasi dan badge Scanned

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada baris `RF-00130`
4. Verifikasi baris `RF-00130` berbadge `Not scanned` sebelum dipindai
5. Pindai Tag `RF-00130` dengan reader
6. Verifikasi baris `RF-00130` menampilkan tanda centang
7. Verifikasi baris `RF-00130` berbadge `Scanned` di kanan tombol Scan

### TC-FA-TAG-285: Tag RFID terpilih yang tidak dipindai berbadge Not scanned (peringatan)

8. Klik [Cancel] pada dialog Replace TAG
9. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
10. Verifikasi baris `RF-00130` otomatis terpilih
11. Verifikasi baris `RF-00130` berbadge `Not scanned` dengan gaya peringatan
12. Verifikasi tombol ButtonScan `Scan RFID` tersedia pada baris itu

### TC-FA-TAG-286: Tag QR di daftar lepas tidak punya tombol Scan dan tidak berbadge status

13. Klik [Cancel] pada dialog Replace TAG
14. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 42'
15. Verifikasi baris `QR-00230` tampil di `TAG to replace` tanpa tombol Scan
16. Verifikasi baris `QR-00230` tidak berbadge `Scanned` maupun `Not scanned`

### TC-FA-TAG-287: Scan Current TAG: Tag Paired di aset yang sama tetapi tidak di daftar lepas ditolak V-29

17. Klik [Cancel] pada dialog Replace TAG
18. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 244'
19. Centang baris `RF-00132`
20. Klik ButtonScan `Scan RFID` pada baris `RF-00132`
21. Pindai Tag `QR-00232` dengan reader
22. Verifikasi error inline "This TAG is not in the list to replace."
23. Verifikasi baris `RF-00132` tetap berbadge `Not scanned`
24. Verifikasi tidak ada Tag yang mendapat status terverifikasi

### TC-FA-TAG-284: Scan Current TAG pada Tag NFC memberi badge Scanned

25. Klik [Cancel] pada dialog Replace TAG
26. Tutup Popup Detail Assets
27. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
28. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
29. Centang baris `NF-00092`
30. Klik ButtonScan `Scan NFC` pada baris `NF-00092`
31. Pindai Tag `NF-00092` dengan reader
32. Verifikasi baris `NF-00092` berbadge `Scanned`
33. Klik [Cancel] pada dialog Replace TAG

## Notes

- Langkah penghubung (S-03): [Cancel] menutup dialog Replace TAG antar-TC; TC-FA-TAG-284 dipindah ke akhir karena memakai Popup Detail 'Laptop Pro 14', sedangkan empat TC lain memakai Popup 'Excavator 20 Ton'; Popup 'Excavator 20 Ton' ditutup sebelum membuka Popup 'Laptop Pro 14'.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec menganggap dialog itu belum terisi dan tertutup langsung (selaras TC-FA-TAG-311).
  - TC-FA-TAG-287 menyebut Post Condition 'Tidak ada data yang berubah' tanpa langkah observasi; tidak diasersi.
