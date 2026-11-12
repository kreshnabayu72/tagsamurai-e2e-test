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
- Akses menu Global Settings > TAG oleh akun aktor pertama [UP_DC] (membuka Popup TAG Log Tag `RF-00071` pada langkah 23 sampai 27) tidak tertulis di Tabel Pre-setup TC untuk akun itu; akses tersebut disediakan tim FE/BE sebagai kemampuan akun (tanpa email atau env tambahan di luar akun [UP_DC] di atas), dan spec ini hanya membukanya tanpa mengubah capability akun.
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix) Tag To Be Returned: [RFID] `RF-00071` (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group 'Disposal Center', Current Holder Dedi K.); [RFID] `RF-00088` ('Excavator 20 Ton - 5', 'Disposal Center', Dedi K.); [NFC] `NF-00092` ('Laptop Pro 14 - 8', 'HQ Warehouse', Rina T.).
- Nama tampil akun aktor tidak tertulis di Pre-setup TC; kolom "Received By" dan Modified By diasersi dengan nama tampil akun aktor yang dibaca fixture (format [First Name] [Last Initial], R-14).
- Baseline jumlah entri Event Log tab To Be Returned dan TAG Log Tag yang diamati dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama dan dibaca ulang pada langkah 11, 19, dan 29 sesudah pemulihan fixture (butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Waktu penerimaan dicatat pada langkah 5 sesudah [Receive]; kolom Received At dibandingkan dengan waktu itu dengan toleransi satu menit; jam server dan jam browser sinkron (S-12).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Scan`) (langkah 4, 14, 22); entri TAG Log Global `Received` (langkah 4, 14, 22); entri Event Log To Be Returned (Method `Manual`) (langkah 33); entri TAG Log Global `Marked Damaged/Missing` (langkah 33).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag To Be Returned `RF-00071`, `RF-00088`, `NF-00092`, status Tag di registri Global, aset, dan laporan ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: status Tag di registri Global dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1103: Receive TAG menulis entri Event Log lengkap

1. Buka tab To Be Returned
2. Klik tombol "Receive TAG"
3. Pindai Tag RF-00071
4. Klik tombol [Receive]
5. Catat waktu saat ini (jam browser) sebagai waktu penerimaan
6. Klik tombol "Event Log"
7. Verifikasi satu entri baru untuk RF-00071 dengan Received At (waktu penerimaan sesuai General Settings, sama dengan waktu yang dicatat pada langkah 5 dengan toleransi satu menit), TAG Code RF-00071, Last Asset "Excavator 20 Ton - 2", Return Group "Disposal Center", Handed Over By "Dedi K."
8. Verifikasi kolom Received By entri itu berisi nama pelaku Receive TAG (pengguna login)
9. Verifikasi kolom Method "Scan" dan Final Status "Available"

### TC-FA-TAG-1104: Receive dua Tag menulis tepat dua entri tanpa duplikat

10. Tutup Modal Event Log, lalu pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
11. Catat jumlah entri Event Log tab To Be Returned (total, serta untuk RF-00071 dan RF-00088) sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
12. Klik tombol "Receive TAG"
13. Pindai Tag RF-00071 dan RF-00088
14. Klik tombol [Receive]
15. Klik tombol "Event Log"
16. Verifikasi Event Log memuat tepat satu entri baru untuk RF-00071 dan tepat satu entri baru untuk RF-00088 terhadap baseline per Tag langkah 11, keduanya Method "Scan" dan Final Status "Available"
17. Verifikasi jumlah entri Event Log bertambah tepat dua terhadap baseline yang dicatat pada langkah 11

### TC-FA-TAG-1105: Receive TAG menulis entri TAG Log Global "Received"

18. Tutup Modal Event Log, lalu pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
19. Catat jumlah entri TAG Log Tag RF-00071 sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
20. Klik tombol "Receive TAG"
21. Pindai Tag RF-00071
22. Klik tombol [Receive]
23. Buka Global Settings > TAG
24. Ketik Search `RF-00071`, tekan Enter
25. Buka Popup TAG Log Tag `RF-00071`
26. Verifikasi entri baru bertitle "TAG Received by [PIC]" dengan PIC pelaku Receive TAG
27. Verifikasi entri memuat Previous Status "To be Returned" menjadi "Available" dan Return Group "Disposal Center"

### TC-FA-TAG-1107: Receive Manually menulis entri Event Log tanpa kolom Note

28. Pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
29. Catat jumlah entri Event Log tab To Be Returned untuk RF-00071 sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
30. Buka menu aksi baris RF-00071
31. Klik "Receive Manually"
32. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
33. Klik tombol [Submit]
34. Klik tombol "Event Log"
35. Verifikasi satu entri baru untuk RF-00071 dengan Method "Manual", Final Status "Damaged/Missing", Handed Over By "Dedi K.", dan Received By pelaku Receive Manually
36. Verifikasi Note "Tag rusak saat serah terima" tidak tampil di entri

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 5, 10, 11, 18, 19, 24, 28 dan 29 (mencatat waktu penerimaan; menutup modal, memulihkan Tag To Be Returned lewat fixture antar TC, S-09; mencari baris target RF-00071 di registri lewat Search, R-16).
- Alasan spec ini tetap di atas 35 langkah secara nominal (36 langkah): menurut hitungan bagian 3 prinsip 13, blok baca-log berpola, yaitu buka surface, cari entri, lalu `Verifikasi` kolom log (langkah 6 sampai 9, 15 sampai 17, 23 sampai 27, dan 34 sampai 36), tidak dihitung ke ambang 35 langkah, sehingga hitungan efektif 21 langkah; bila hanya langkah buka surface dan cari entri (6, 15, 23, 24, 25, 34) yang dikecualikan, hitungannya tetap 30 langkah. Keempat blok satu kelas harness (FE+BE dengan simulator reader sebagai langkah rutin) dan berdiri sendiri: tiap blok sesudah yang pertama dimulai dari pemulihan Tag To Be Returned lewat fixture (langkah 10, 18, 28) dan membaca baseline sendiri (langkah 11, 19, 29), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Scan`) (langkah 4, 14, 22); entri TAG Log Global `Received` (langkah 4, 14, 22); entri Event Log To Be Returned (Method `Manual`) (langkah 33); entri TAG Log Global `Marked Damaged/Missing` (langkah 33).
- Temuan untuk QA:
  - TC-FA-TAG-1103 sampai 1107 tidak menyebut nama tampil akun aktor (pelaku Receive); asersi Received By memakai nama tampil akun aktor dari fixture.
  - TC-FA-TAG-1105 mengharapkan title "TAG Received by [PIC]" dengan placeholder [PIC] tanpa nilai; spec mengasersi PIC sebagai nama pelaku.
  - TC-FA-TAG-1103 sampai 1107 tidak menyebut baseline entri Event Log; spec memakai selisih jumlah entri terhadap baseline (S-12).
  - TC-FA-TAG-1107 Expected b ('Note tidak tampil di entri') tidak menyebut kolom yang diamati; spec mengasersi tidak ada kolom Note pada entri Event Log.
  - TC-FA-TAG-1105 menulis langkah 'Buka Global Settings > TAG, cari RF-00071, lalu buka Popup TAG Log Tag itu' untuk Role Manage asset & TAG dengan Update di group Disposal Center, tetapi akses menu Global Settings > TAG tidak tercatat untuk akun itu di Tabel Data Uji Pre-setup TC; spec mengasumsikan akses itu disediakan tim FE/BE dan tidak mengganti akun.
