---
id: TC-FA-TAG-E2E-301-sinkron-masuk-disposal-tag-masuk-to-be-returned-dan-snapshot-bagian-2
title: "Sinkron Masuk Disposal: TAG Log Global, Penutupan Laporan, Scope Return Group, dan Receive Manually, Bagian 2"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1239
  - TC-FA-TAG-1241
  - TC-FA-TAG-1242
  - TC-FA-TAG-1243
  - TC-FA-TAG-1381
coverage:
  web: automated
---

# Sinkron Masuk Disposal: TAG Log Global, Penutupan Laporan, Scope Return Group, dan Receive Manually, Bagian 2

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Pengamat sesi UI pada TC-FA-TAG-1239, 1241, dan 1381.
- Akun aktor: Manage asset & TAG dengan Update di group Disposal Center [UP_DC] `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_UP_DC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai sebagai Budi S. pada TC-FA-TAG-1242 dan 1243 (ganti akun eksplisit).
- Akun Maya R. (Manage asset & TAG Read, assign HQ Warehouse saja) tidak tertulis di Tabel Pre-setup TC; disediakan tim FE.
- Akun aktor: Asset Admin (pelaku disposal) [AA_DSPO] `assetAdminPelakuDisposal_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_AA_DSPO_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Pelaku disposal; dipakai sebagai pelaku kedua lewat sesi API.
- Akun aktor: Asset Admin (pelaku disposal Dedi K.) [AA_DSPK] `assetAdminPelakuDisposalDediK_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_AA_DSPK_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Pelaku disposal Dedi K.; dipakai sebagai pelaku kedua lewat sesi API pada TC-FA-TAG-1381.
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui, Disposal Group transaksi Disposal Center); aset AST-0902 ('Excavator 20 Ton - 2', Plant B, In Disposal Process) tanpa pemegang dengan Tag RFID `RF-00073` Paired (TC-FA-TAG-1381); Tag To Be Returned lain: [RFID] `RF-00088` ('Excavator 20 Ton - 5', Disposal Center, Dedi K.) dan [NFC] `NF-00092` ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.).
- Kemampuan teknis (disediakan tim FE/BE): menjalankan Execute disposal lewat sesi API dan membaca state backend (status laporan dan status aset) hanya untuk butir Expected TC yang menyebutnya (S-11); baseline kartu Reported dan daftar To Be Returned dibaca di hook `before` (S-12).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset AST-0900 dan AST-0902, Tag, laporan, dan daftar To Be Returned ke keadaan awal lewat fixture backend, serta sesi ke akun default suite.
- State global yang diubah spec ini: status aset, status Tag, laporan, dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1239: disposal selesai menulis TAG Log Global "To be Returned"

1. Pelaku kedua (Asset Admin pelaku disposal) lewat sesi API menyelesaikan langkah Execute disposal aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui, Disposal Group transaksi Disposal Center) dengan Tag RFID RF-00071 Paired hingga disposal selesai
2. Buka Global Settings > TAG
3. Ketik Search `RF-00071`, tekan Enter
4. Buka Popup TAG Log Tag `RF-00071`
5. Verifikasi entri baru bertitle "TAG Marked To be Returned by [PIC]" dengan PIC pelaku disposal
6. Verifikasi entri memuat Asset "Excavator 20 Ton - 2", Asset Code "AST-0900", Reason, dan Return Group "Disposal Center"

### TC-FA-TAG-1241: disposal selesai menutup laporan terbuka dengan status Canceled

7. Tutup Popup TAG Log, lalu siapkan lewat fixture backend aset AST-0900 dengan Tag RF-00071 Paired dan laporan terbuka Damaged (satu-satunya laporan pada aset)
8. Pelaku kedua (Asset Admin pelaku disposal) lewat sesi API menyelesaikan langkah Execute disposal aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui, Disposal Group transaksi Disposal Center) dengan Tag RFID RF-00071 Paired hingga disposal selesai
9. Buka Fixed Asset > TAG tab Paired
10. Verifikasi laporan RF-00071 berstatus Canceled (dibaca lewat kemampuan baca state backend)
11. Verifikasi kartu "Reported" berkurang satu terhadap baseline
12. Verifikasi aset AST-0900 tidak lagi memiliki status "Tag Reported" (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1381: Current Holder memakai pelaku disposal bila aset tidak memiliki pemegang

13. Siapkan lewat fixture backend aset AST-0902 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, tanpa pemegang) dengan Tag RFID RF-00073 Paired dan pulihkan daftar To Be Returned
14. Pelaku kedua (Asset Admin pelaku disposal Dedi K.) lewat sesi API menyelesaikan langkah Execute disposal aset AST-0902 hingga disposal selesai
15. Buka tab To Be Returned
16. Verifikasi kolom Current Holder baris RF-00073 menampilkan "Dedi K." (pelaku disposal) karena aset tidak memiliki pemegang saat disposal

### TC-FA-TAG-1242 dan 1243: Tag hasil disposal terlihat menurut scope Return Group dan aksi Receive Manually

17. Siapkan lewat fixture backend aset AST-0900 dengan Tag RFID RF-00071 Paired dan pulihkan daftar To Be Returned
18. Pelaku kedua (Asset Admin pelaku disposal) lewat sesi API menyelesaikan langkah Execute disposal aset AST-0900 ('Excavator 20 Ton - 2', Plant B, In Disposal Process, Disposal Request disetujui, Disposal Group transaksi Disposal Center) dengan Tag RFID RF-00071 Paired hingga disposal selesai
19. Ganti akun: logout dari akun Total Control
20. Login dengan akun Manage asset & TAG dengan Update di group Disposal Center [UP_DC] (Budi S.) lalu buka Fixed Asset > TAG tab To Be Returned
21. Verifikasi Budi S. melihat baris RF-00071
22. Buka menu aksi baris RF-00071
23. Verifikasi aksi "Receive Manually" tampil pada baris RF-00071 karena Return Group Disposal Center dipegang Update oleh Budi S.
24. Ganti akun: logout dari akun Budi S.
25. Login dengan akun Maya R. lalu buka Fixed Asset > TAG tab To Be Returned
26. Verifikasi tabel To Be Returned Maya R. tampil dengan baris NF-00092 (HQ Warehouse)
27. Verifikasi Maya R. tidak melihat baris RF-00071

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 3, 7, 13, 17, 19, 20, 24 dan 25 (menyiapkan data lewat fixture, mencari Tag di registri lewat Search, R-16; ganti akun eksplisit, S-07).
- TC-FA-TAG-1242 dan 1243 memakai satu kali disposal (AST-0900, Tag RF-00071) karena precondition dan pemicunya sama; Budi S. mengasersi 1242 butir a dan 1243, lalu Maya R. mengasersi 1242 butir b. Urutan TC dikelompokkan per akun (S-10) dan blok akun Total Control mendahului ganti akun.
- Pelaku disposal memakai sesi API karena hanya memicu state dan tidak diasersi di sesinya (R-20).
- Absence TC-FA-TAG-1242 b (Maya R. tidak melihat RF-00071): didahului `Verifikasi` baris NF-00092 pada tabel yang sama sebagai anchor positif (bagian 8b butir 2).
- TC-FA-TAG-1240 tidak ada di spec ini; TC-FA-TAG-1233 sampai 1238 ada di spec 300.
- Temuan untuk QA:
  - TC-FA-TAG-1242 menyebut Budi S. 'Manage asset & TAG Read assign Disposal Center' dan TC-FA-TAG-1243 menyebut Budi S. 'memegang Update di Disposal Center'; spec memakai akun Pre-setup UP_DC yang memegang Update di group Disposal Center untuk keduanya.
  - TC-FA-TAG-1241 Expected a ('laporan RF-00071 berstatus Canceled') tidak punya langkah observasi di UI; spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE).
  - TC-FA-TAG-1241 Expected b ('aset AST-0900 tidak lagi memiliki status Tag Reported') tidak menyebut tempat mengamatinya; spec memakai kemampuan baca state backend.
  - TC-FA-TAG-1241 Post Condition (modul terdampak transactions-disposal dan notification) tidak punya langkah observasi; tidak diasersi.
  - TC-FA-TAG-1239 sampai 1381 langkah TC ke-1 ('Login sbg Asset Admin lalu buka layar Disposal Execute') dan login Total Control adalah dua akun; spec memakai pelaku disposal sebagai pelaku kedua lewat sesi API.
