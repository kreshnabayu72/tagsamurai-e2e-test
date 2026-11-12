---
id: TC-FA-TAG-E2E-280-pencatatan-receive-event-log-tag-log-global-dan-assigned-paired-bagian-2
title: "Pencatatan Receive: TAG Log Global untuk Receive Manually dan Receive Manually Bulk, Bagian 2"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1108
  - TC-FA-TAG-1109
coverage:
  web: automated
---

# Pencatatan Receive: TAG Log Global untuk Receive Manually dan Receive Manually Bulk, Bagian 2

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Manage asset & TAG dengan Update di group Disposal Center [UP_DC] `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_UP_DC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Akses menu Global Settings > TAG oleh akun aktor pertama [UP_DC] (membuka Popup TAG Log Tag `RF-00071` pada langkah 8 sampai 12, serta Tag `RF-00071` dan `RF-00088` pada langkah 20 sampai 26) tidak tertulis di Tabel Pre-setup TC untuk akun itu; akses tersebut disediakan tim FE/BE sebagai kemampuan akun (tanpa email atau env tambahan di luar akun [UP_DC] di atas), dan spec ini hanya membukanya tanpa mengubah capability akun.
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix) Tag To Be Returned: [RFID] `RF-00071` (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group 'Disposal Center', Current Holder Dedi K.); [RFID] `RF-00088` ('Excavator 20 Ton - 5', 'Disposal Center', Dedi K.); [NFC] `NF-00092` ('Laptop Pro 14 - 8', 'HQ Warehouse', Rina T.).
- Nama tampil akun aktor tidak tertulis di Pre-setup TC; kolom "Received By" dan Modified By diasersi dengan nama tampil akun aktor yang dibaca fixture (format [First Name] [Last Initial], R-14).
- Baseline jumlah entri TAG Log Tag yang diamati dibaca lewat kemampuan baca (disediakan tim FE/BE) pada langkah 2 sebelum aksi pemicu TC-FA-TAG-1108 dan pada langkah 14 sesudah pemulihan fixture sebelum aksi pemicu TC-FA-TAG-1109 (butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Manual`) (langkah 6, 18); entri TAG Log Global `Marked Damaged/Missing` (langkah 6, 18).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag To Be Returned `RF-00071`, `RF-00088`, `NF-00092`, status Tag di registri Global, aset, dan laporan ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: status Tag di registri Global dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1108: Receive Manually menulis TAG Log Global "Marked Damaged/Missing"

1. Buka tab To Be Returned
2. Catat jumlah entri TAG Log "Marked Damaged/Missing" untuk Tag RF-00071 sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
3. Buka menu aksi baris RF-00071
4. Klik "Receive Manually"
5. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
6. Klik tombol [Submit]
7. Tunggu aksi selesai (dialog "Receive Manually" tertutup dan tombol aktif kembali)
8. Buka Global Settings > TAG
9. Ketik Search `RF-00071`, tekan Enter
10. Buka Popup TAG Log Tag `RF-00071`
11. Verifikasi satu entri baru bertitle "TAG Marked Damaged/Missing by [PIC]" (selisih jumlah entri terhadap baseline langkah 2) dengan PIC pelaku Receive Manually
12. Verifikasi entri memuat Previous Status "To be Returned" dan Note "Tag rusak saat serah terima"

### TC-FA-TAG-1109: Receive Manually Bulk menulis satu entri TAG Log per Tag dengan Note yang sama

13. Pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
14. Catat jumlah entri TAG Log "Marked Damaged/Missing" untuk Tag RF-00071 dan Tag RF-00088 sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
15. Centang baris RF-00071 dan RF-00088
16. Klik Bulk Action "Receive Manually"
17. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
18. Klik tombol [Submit]
19. Tunggu aksi selesai (dialog "Receive Manually" tertutup dan tombol aktif kembali)
20. Buka Global Settings > TAG
21. Ketik Search `RF-00071`, tekan Enter
22. Buka Popup TAG Log Tag `RF-00071`
23. Verifikasi Tag `RF-00071` memuat tepat satu entri baru "Marked Damaged/Missing" (selisih jumlah entri terhadap baseline langkah 14) dengan Note "Tag rusak saat serah terima"
24. Tutup Popup TAG Log, lalu ganti isi kotak Search dengan `RF-00088`, tekan Enter
25. Buka Popup TAG Log Tag `RF-00088`
26. Verifikasi Tag `RF-00088` memuat tepat satu entri baru "Marked Damaged/Missing" (selisih jumlah entri terhadap baseline langkah 14) dengan Note "Tag rusak saat serah terima"

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 2, 7, 9, 13, 14, 19, 21 dan 24 (mencatat baseline sebelum pemicu; memulihkan Tag To Be Returned lewat fixture, mencari baris target di registri lewat Search, menutup popup, R-16). Langkah 7 dan 19 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi pindah surface.
- TC-FA-TAG-1111 dan TC-FA-TAG-1112 ada di spec 304.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Manual`) (langkah 6, 18); entri TAG Log Global `Marked Damaged/Missing` (langkah 6, 18).
- Temuan untuk QA:
  - TC-FA-TAG-1108 dan 1109 menulis title "TAG Marked Damaged/Missing by [PIC]" dengan placeholder [PIC]; spec mengasersi PIC sebagai nama pelaku Receive Manually.
  - TC-FA-TAG-1108 dan 1109 tidak menyebut baseline entri TAG Log; spec memakai selisih jumlah entri "Marked Damaged/Missing" Tag itu terhadap baseline per TC dan Note (S-12, butir A-18).
  - TC-FA-TAG-1108 dan 1109 menulis langkah membuka Popup TAG Log di Global Settings > TAG untuk Role Manage asset & TAG dengan Update di group Disposal Center, tetapi akses menu Global Settings > TAG tidak tercatat untuk akun itu di Tabel Data Uji Pre-setup TC; spec mengasumsikan akses itu disediakan tim FE/BE dan tidak mengganti akun.
