---
id: TC-FA-DAMAGED-UI-119-dialog-cannot-report-damaged
title: "Dialog blok Cannot Report Damaged: pesan baku, daftar semua aset terpilih beserta keterangan dalam container scrollable, dan OK"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-12, "§4.2.4#p10", EB-FB-2@dialog-blok-report-damaged]
smoke: []
dependsOn: []
trace:
  D-DMG-12: [2, 3, 4, 5, 6, 7]
  "§4.2.4#p10": [3, 4, 5, 6, 7, 9, 10, 11]
  EB-FB-2@dialog-blok-report-damaged: [14, 15]
anchor: []
coverage:
  web: automated
---

# Dialog blok Cannot Report Damaged: pesan baku, daftar semua aset terpilih beserta keterangan dalam container scrollable, dan OK

## Prerequisites
- Aktor: Pelapor admin (Aktor Damaged pada Group aset) yang memilih aset dari Asset List.
- Layar awal: Dialog Cannot Report Damaged belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Cannot Report Damaged (D-DMG-12)
- Data:
  - DU-119-1: aset `Drill Bosch GSB - 6`, Asset ID `DRL-2026-0006`, sudah punya record berjalan, keterangan `Already reported damaged`.
  - DU-119-2: aset `Forklift Toyota 8FD - 1`, Asset ID `FLT-2026-0001`, berstatus Disposed, keterangan `Can't be reported damaged`.
  - DU-119-3: aset `Office Chair Ergo - 18`, Asset ID `CHR-2026-0018`, di luar Group tempat pengguna memegang Update, keterangan `Can't be reported damaged`.
  - DU-119-4: delapan aset `Office Chair Ergo - 1`, `Office Chair Ergo - 2`, `Office Chair Ergo - 3`, `Office Chair Ergo - 4`, `Office Chair Ergo - 5`, `Office Chair Ergo - 6`, `Office Chair Ergo - 7`, dan `Office Chair Ergo - 8`, seluruhnya tidak layak.
- Kondisi:
  - K1: aset terpilih DU-119-1, DU-119-2, dan DU-119-3 seluruhnya tidak layak saat `[Report Damaged]` diklik.
  - K2: aset terpilih DU-119-4 seluruhnya tidak layak, dengan daftar lebih panjang daripada tinggi dialog.

## Test Steps

### Isi dialog blok untuk semua aset tidak layak
1. Tampilkan Dialog Cannot Report Damaged dengan kondisi K1
2. Verifikasi judul dialog `Cannot Report Damaged`
3. Verifikasi pesan `None of the selected assets can be reported damaged.` tampil
4. Verifikasi aset `Drill Bosch GSB - 6` tampil dengan keterangan `Already reported damaged`
5. Verifikasi aset `Forklift Toyota 8FD - 1` tampil dengan keterangan `Can't be reported damaged`
6. Verifikasi aset `Office Chair Ergo - 18` tampil dengan keterangan `Can't be reported damaged`
7. Verifikasi tombol `[OK]` tampil pada dialog Cannot Report Damaged

### Daftar aset tidak diringkas dan bisa digulir
8. Tampilkan Dialog Cannot Report Damaged dengan kondisi K2
9. Verifikasi kedelapan aset `Office Chair Ergo - 1`, `Office Chair Ergo - 2`, `Office Chair Ergo - 3`, `Office Chair Ergo - 4`, `Office Chair Ergo - 5`, `Office Chair Ergo - 6`, `Office Chair Ergo - 7`, dan `Office Chair Ergo - 8` tampil seluruhnya pada dialog Cannot Report Damaged
10. Verifikasi daftar aset berada dalam wadah yang bisa digulir
11. Verifikasi tidak ada teks ringkasan jumlah aset pengganti daftar nama

### OK menutup dialog tanpa toast
12. Tampilkan Dialog Cannot Report Damaged dengan kondisi K1
13. Klik `[OK]`
14. Verifikasi dialog Cannot Report Damaged tertutup
15. Verifikasi tidak ada toast yang tampil sesudah `[OK]`
