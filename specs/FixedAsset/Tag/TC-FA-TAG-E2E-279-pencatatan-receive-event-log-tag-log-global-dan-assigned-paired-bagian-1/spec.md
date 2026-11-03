---
id: TC-FA-TAG-E2E-279-pencatatan-receive-event-log-tag-log-global-dan-assigned-paired-bagian-1
title: "Pencatatan Receive: Event Log dan TAG Log Global untuk Receive TAG dan Receive Manually, Bagian 1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1103
  - TC-FA-TAG-1104
  - TC-FA-TAG-1105
  - TC-FA-TAG-1107
coverage:
  web: automated
---

# Pencatatan Receive: Event Log dan TAG Log Global untuk Receive TAG dan Receive Manually, Bagian 1

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Manage asset & TAG dengan Update di group Disposal Center [UP_DC] `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_UP_DC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix) Tag To Be Returned: [RFID] `RF-00071` (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group 'Disposal Center', Current Holder Dedi K.); [RFID] `RF-00088` ('Excavator 20 Ton - 5', 'Disposal Center', Dedi K.); [NFC] `NF-00092` ('Laptop Pro 14 - 8', 'HQ Warehouse', Rina T.).
- Nama tampil akun aktor tidak tertulis di Pre-setup TC; kolom "Received By" dan Modified By diasersi dengan nama tampil akun aktor yang dibaca fixture (format [First Name] [Last Initial], R-14).
- Baseline jumlah entri Event Log tab To Be Returned dan TAG Log Tag yang diamati dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag To Be Returned `RF-00071`, `RF-00088`, `NF-00092`, status Tag di registri Global, aset, dan laporan ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: status Tag di registri Global dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1103: Receive TAG menulis entri Event Log lengkap

1. Buka tab To Be Returned
2. Klik tombol "Receive TAG"
3. Pindai Tag RF-00071
4. Klik tombol [Receive]
5. Klik tombol "Event Log"
6. Verifikasi satu entri baru untuk RF-00071 dengan Received At (waktu penerimaan sesuai General Settings), TAG Code RF-00071, Last Asset "Excavator 20 Ton - 2", Return Group "Disposal Center", Handed Over By "Dedi K."
7. Verifikasi kolom Received By entri itu berisi nama pelaku Receive TAG (pengguna login)
8. Verifikasi kolom Method "Scan" dan Final Status "Available"

### TC-FA-TAG-1104: Receive dua Tag menulis tepat dua entri tanpa duplikat

9. Tutup Modal Event Log, lalu pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
10. Klik tombol "Receive TAG"
11. Pindai Tag RF-00071 dan RF-00088
12. Klik tombol [Receive]
13. Klik tombol "Event Log"
14. Verifikasi Event Log memuat tepat satu entri untuk RF-00071 dan tepat satu entri untuk RF-00088, keduanya Method "Scan" dan Final Status "Available"
15. Verifikasi jumlah entri Event Log bertambah tepat dua terhadap baseline

### TC-FA-TAG-1105: Receive TAG menulis entri TAG Log Global "Received"

16. Tutup Modal Event Log, lalu pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
17. Klik tombol "Receive TAG"
18. Pindai Tag RF-00071
19. Klik tombol [Receive]
20. Buka Global Settings > TAG
21. Ketik Search `RF-00071`, tekan Enter
22. Buka Popup TAG Log Tag `RF-00071`
23. Verifikasi entri baru bertitle "TAG Received by [PIC]" dengan PIC pelaku Receive TAG
24. Verifikasi entri memuat Previous Status "To be Returned" menjadi "Available" dan Return Group "Disposal Center"

### TC-FA-TAG-1107: Receive Manually menulis entri Event Log tanpa kolom Note

25. Pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
26. Buka menu aksi baris RF-00071
27. Klik "Receive Manually"
28. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
29. Klik tombol [Submit]
30. Klik tombol "Event Log"
31. Verifikasi satu entri baru untuk RF-00071 dengan Method "Manual", Final Status "Damaged/Missing", Handed Over By "Dedi K.", dan Received By pelaku Receive Manually
32. Verifikasi Note "Tag rusak saat serah terima" tidak tampil di entri

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 9, 16, 21 dan 25 (menutup modal, memulihkan Tag To Be Returned lewat fixture antar TC, S-09; mencari baris target RF-00071 di registri lewat Search, R-16).
- Temuan untuk QA:
  - TC-FA-TAG-1103 sampai 1107 tidak menyebut nama tampil akun aktor (pelaku Receive); asersi Received By memakai nama tampil akun aktor dari fixture.
  - TC-FA-TAG-1105 mengharapkan title "TAG Received by [PIC]" dengan placeholder [PIC] tanpa nilai; spec mengasersi PIC sebagai nama pelaku.
  - TC-FA-TAG-1103 sampai 1107 tidak menyebut baseline entri Event Log; spec memakai selisih jumlah entri terhadap baseline (S-12).
  - TC-FA-TAG-1107 Expected b ('Note tidak tampil di entri') tidak menyebut kolom yang diamati; spec mengasersi tidak ada kolom Note pada entri Event Log.
