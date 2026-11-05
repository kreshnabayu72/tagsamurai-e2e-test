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
- Baseline jumlah entri Event Log tab To Be Returned dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama dan dibaca ulang pada langkah 13 sesudah pemulihan fixture (butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 5); entri Changelog `Replace` per aset (langkah 17); entri TAG Log Global (langkah 5, 17); entri Event Log To Be Returned (Method `Assigned`) (langkah 5, 17).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag To Be Returned `RF-00071`, `RF-00088`, `NF-00092`, status Tag di registri Global, aset, dan laporan ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: status Tag di registri Global dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1111: Tag To Be Returned dipasang lewat Pair TAG

1. Buka Popup Detail yang memuat aset AST-0300 (Not Paired Yet, TAG Type RFID)
2. Klik `Show` di samping `Not Paired Yet`
3. Pilih row action "Pair TAG" pada aset AST-0300
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00071`
5. Klik [Submit]
6. Tunggu aksi selesai (dialog "Pair TAG" tertutup dan tombol aktif kembali)
7. Buka tab "To Be Returned"
8. Verifikasi baris RF-00088 tetap tampil di tabel To Be Returned
9. Verifikasi baris RF-00071 tidak lagi ada di tabel To Be Returned
10. Klik tombol "Event Log"
11. Verifikasi satu entri RF-00071 dengan Method "Assigned", Final Status "Paired" (badge severity info), dan Received By pelaku Pair TAG

### TC-FA-TAG-1112: Tag To Be Returned dipasang lewat Replace

12. Tutup Modal Event Log, lalu pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned dan kembali ke tab Paired
13. Catat jumlah entri Event Log tab To Be Returned untuk RF-00071 sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
14. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant B untuk membuka Popup Detail
15. Pilih row action "Replace TAG" pada Excavator 20 Ton - 11
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00071`
17. Klik [Submit]
18. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
19. Buka tab "To Be Returned"
20. Verifikasi baris RF-00088 tetap tampil di tabel To Be Returned
21. Verifikasi baris RF-00071 hilang dari tabel To Be Returned
22. Klik tombol "Event Log"
23. Verifikasi satu entri baru RF-00071 (selisih jumlah entri terhadap baseline langkah 13) dengan Method "Assigned" dan Final Status "Paired"

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 6, 12, 13 dan 18 (menutup modal dan memulihkan Tag To Be Returned lewat fixture antar TC, S-09). Langkah 6 dan 18 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi pindah surface.
- Absence baris RF-00071 pada TC-FA-TAG-1111 a dan TC-FA-TAG-1112 a: didahului `Verifikasi` baris RF-00088 tetap tampil di tabel To Be Returned yang sama sebagai anchor positif (bagian 8b butir 2).
- TC-FA-TAG-1108 dan TC-FA-TAG-1109 ada di spec 280.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 5); entri Changelog `Replace` per aset (langkah 17); entri TAG Log Global (langkah 5, 17); entri Event Log To Be Returned (Method `Assigned`) (langkah 5, 17).
- Temuan untuk QA:
  - TC-FA-TAG-1111 Post Condition ('Tag RF-00071 berstatus Paired pada AST-0300 di registri Global; satu entri TAG Log Global Paired dengan Previous Status To be Returned') tidak punya langkah observasi di TC; tidak diasersi.
  - TC-FA-TAG-1111 menyebut aset AST-0300 tanpa Asset Name dan group; spec membuka Popup Detail yang memuat aset itu dan butuh kunci fixture untuk menemukannya.
  - TC-FA-TAG-1111 dan 1112 tidak menyebut nama tampil pelaku Pair TAG/Replace (Received By); spec memakai nama tampil akun aktor dari fixture.
