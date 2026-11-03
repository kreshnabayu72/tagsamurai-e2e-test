---
id: TC-FA-CAID-E2E-014-plan-starter-guard-pembaruan-otomatis
title: "Plan Starter: Guard Pembaruan Otomatis Asset ID Saat Transfer, Edit Asset, dan Mutasi Division"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-335
coverage:
  web: automated
---

# Plan Starter: Guard Pembaruan Otomatis Asset ID Saat Transfer, Edit Asset, dan Mutasi Division

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini. Spec tidak berawal di tab Custom Asset ID: langkah 1 membuka Fixed Asset > Transactions > Transfer; halaman yang dibuka hook `beforeEach` suite tidak dipakai langkah.
- Akun aktor: Total Control `Company Starter` (Pre-setup No 13). Email akun disediakan tim FE/BE (Pre-setup No 13 TC), password `Spectra.env.FA_STARTER_TC_PASSWORD`. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite.
- Data Pre-setup No 13 varian TC guard pembaruan otomatis (di-seed hook `before` spec ini): `Company Starter` plan Starter dengan konfigurasi B3 (Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Division Code, Purchase Date, Asset Increment) dan Master Switch ON; aset S2 Draft `JKT/LAP/T490/0000/0000/2` (Purchase Date dan Division kosong); aset S3 Active `JKT/LAP/T490/HR/0926/3` dengan tiket Transfer XFR-S In Transit ke Group `Warehouse`; Group `Jakarta Office` (Code `JKT`), Division `Human Resources` (Code `HR`). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data langkah: Purchase Date `15/09/26`, Purchase Price `15000000`, berkas faktur `invoice.pdf` (berkas belum ada di `fixtures/`; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis: seed varian guard Company Starter dan reset ke Pre-setup di hook `before` dan `after` spec ini (disediakan tim FE/BE, mekanisme tidak tertulis di TC, PRD, atau LLD); pengunggahan berkas pada Complete Detail.
- State global: aset S2 dan S3 serta tiket XFR-S berubah oleh spec; dipulihkan oleh seed reset Company Starter di hook `after` spec ini walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-335: Transfer, Edit Asset, dan mutasi Division pada plan Starter dengan Master Switch ON dilewati tanpa mutasi Asset ID

1. Buka Fixed Asset > Transactions > Transfer
2. Buka tab `Incoming`
3. Klik `[Arrival Scan]` pada tiket XFR-S
4. Konfirmasikan unit S3 pada Arrival Scan
5. Klik `[Confirm Receipt]`
6. Tunggu aksi selesai: `[Confirm Receipt]` selesai diproses
7. Buka Fixed Asset > Assets > Registration
8. Klik `[Complete Detail]` pada aset S2
9. Isi Purchase Date `15/09/26` dan Purchase Price `15000000`
10. Unggah faktur `invoice.pdf`
11. Klik `[Save Details]`
12. Tunggu aksi selesai: tombol `[Save Details]` selesai diproses
13. Edit Draft S2: pilih Division `Human Resources`, lalu simpan
14. Tunggu aksi selesai: penyimpanan Edit Draft S2 selesai
15. Buka Fixed Asset > Assets > All Assets, lalu buka Detail aset S3
16. Verifikasi Transfer selesai: Group aset S3 menjadi `Warehouse`
17. Verifikasi header Detail aset S3 menampilkan Asset ID tetap `JKT/LAP/T490/HR/0926/3`
18. Verifikasi tidak ada banner info pada Detail aset S3
19. Klik tab `Histori Aset`
20. Verifikasi tabel Histori Aset S3 termuat dengan kolom `Old Asset ID`, `New Asset ID`, `Reason`, `Changed At`, dan `Changed By`
21. Verifikasi tidak ada entri riwayat Asset ID pada aset S3
22. Buka Detail aset S2 dari Fixed Asset > Assets > All Assets
23. Verifikasi Purchase Date aset S2 tersimpan `15/09/26`
24. Verifikasi Division aset S2 tersimpan `Human Resources`
25. Verifikasi header Detail aset S2 menampilkan Asset ID tetap `JKT/LAP/T490/0000/0000/2`
26. Verifikasi tidak ada banner info pada Detail aset S2
27. Klik tab `Histori Aset`
28. Verifikasi tabel Histori Aset S2 termuat dengan kolom `Old Asset ID`, `New Asset ID`, `Reason`, `Changed At`, dan `Changed By`
29. Verifikasi tidak ada entri riwayat Asset ID pada aset S2

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 2, 7, 15, 22 (membuka halaman), langkah 3 sampai 5, 8 sampai 11, 13 (aksi TC), langkah 6, 12, 14 ("Tunggu aksi selesai" karena langkah berikutnya berpindah surface), dan langkah 19 dan 27 (membuka tab `Histori Aset`).
- Pecahan Expected: a menjadi langkah 16, 23, dan 24; b menjadi langkah 17 dan 25; c menjadi langkah 18, 20 sampai 21, 26, dan 28 sampai 29. Asersi absence "tidak ada entri riwayat" (langkah 21 dan 29) didahului anchor positif header Detail aset yang menampilkan Asset ID (langkah 17 dan 25, klausa anchor yang disebut Expected c) dan tabel Histori Aset termuat dengan kolom tampil (langkah 20 dan 28, pengamatan "tab `Histori Aset` terbuka"), dan "tidak ada banner" (langkah 18 dan 26) didahului header Detail aset yang sama (langkah 17 dan 25). Asersi ini mengamati tabel riwayat dan banner Detail aset (state), bukan Changelog, System Log, atau Activity Log, sehingga bukan kelas absence log.
- Spec berdiri sendiri pada seed varian guard Company Starter; tidak bergantung pada spec plan tier lain.
- Temuan untuk QA:
  - Langkah TC "verifikasi unit S3" pada Arrival Scan tidak memberi mekanisme (pindai, pilih, atau centang) dan tidak ada Expected terkait; spec menulisnya sebagai aksi "Konfirmasikan unit S3" tanpa menebak mekanismenya.
  - TC tidak menyebut lokasi aksi "Edit Draft S2"; spec mengikuti urutan TC dan memulainya dari halaman Registration yang sama dengan Complete Detail.
  - Berkas `invoice.pdf` tidak ada di `fixtures/` (hanya `sampleDocument.pdf` dan `sampleImage.png`).
  - Post Condition TC-FA-CAID-335 kosong; tidak ada yang diasersi.
