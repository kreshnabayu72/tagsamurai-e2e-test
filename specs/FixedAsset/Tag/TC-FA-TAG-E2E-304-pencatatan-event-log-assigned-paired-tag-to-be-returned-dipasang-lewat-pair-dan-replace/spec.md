---
id: TC-FA-TAG-E2E-304-pencatatan-event-log-assigned-paired-tag-to-be-returned-dipasang-lewat-pair-dan-replace
title: "Pencatatan Event Log Assigned/Paired untuk Tag To Be Returned yang Dipasang lewat Pair TAG dan Replace"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1111
  - TC-FA-TAG-1112
coverage:
  web: automated
---

# Pencatatan Event Log Assigned/Paired untuk Tag To Be Returned yang Dipasang lewat Pair TAG dan Replace

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix) Tag To Be Returned: [RFID] `RF-00071` (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group 'Disposal Center', Current Holder Dedi K.); [RFID] `RF-00088` ('Excavator 20 Ton - 5', 'Disposal Center', Dedi K.); [NFC] `NF-00092` ('Laptop Pro 14 - 8', 'HQ Warehouse', Rina T.).
- Data tambahan (Pre-setup TC, tanpa suffix): aset AST-0300 Not Paired Yet dengan TAG Type RFID; aset AST-0011 ('Excavator 20 Ton - 11', Plant B) dengan Tag RFID `RF-00101` Paired.
- Nama tampil akun aktor tidak tertulis di Pre-setup TC; kolom "Received By" dan Modified By diasersi dengan nama tampil akun aktor yang dibaca fixture (format [First Name] [Last Initial], R-14).
- Baseline jumlah entri Event Log tab To Be Returned dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag To Be Returned `RF-00071`, `RF-00088`, `NF-00092`, status Tag di registri Global, aset, dan laporan ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: status Tag di registri Global dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1111: Tag To Be Returned dipasang lewat Pair TAG

1. Buka Popup Detail yang memuat aset AST-0300 (Not Paired Yet, TAG Type RFID)
2. Klik `Show` di samping `Not Paired Yet`
3. Pilih row action "Pair TAG" pada aset AST-0300
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00071`
5. Klik [Submit]
6. Buka tab "To Be Returned"
7. Verifikasi baris RF-00071 tidak lagi ada di tabel To Be Returned
8. Klik tombol "Event Log"
9. Verifikasi satu entri RF-00071 dengan Method "Assigned", Final Status "Paired" (badge severity info), dan Received By pelaku Pair TAG

### TC-FA-TAG-1112: Tag To Be Returned dipasang lewat Replace

10. Tutup Modal Event Log, lalu pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned dan kembali ke tab Paired
11. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant B untuk membuka Popup Detail
12. Pilih row action "Replace TAG" pada Excavator 20 Ton - 11
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00071`
14. Klik [Submit]
15. Buka tab "To Be Returned"
16. Verifikasi baris RF-00071 hilang dari tabel To Be Returned
17. Klik tombol "Event Log"
18. Verifikasi satu entri RF-00071 dengan Method "Assigned" dan Final Status "Paired"

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 10 (menutup modal dan memulihkan Tag To Be Returned lewat fixture antar TC, S-09).
- TC-FA-TAG-1108 dan TC-FA-TAG-1109 ada di spec 280.
- Temuan untuk QA:
  - TC-FA-TAG-1111 Post Condition ('Tag RF-00071 berstatus Paired pada AST-0300 di registri Global; satu entri TAG Log Global Paired dengan Previous Status To be Returned') tidak punya langkah observasi di TC; tidak diasersi.
  - TC-FA-TAG-1111 menyebut aset AST-0300 tanpa Asset Name dan group; spec membuka Popup Detail yang memuat aset itu dan butuh kunci fixture untuk menemukannya.
  - TC-FA-TAG-1111 dan 1112 tidak menyebut nama tampil pelaku Pair TAG/Replace (Received By); spec memakai nama tampil akun aktor dari fixture.
