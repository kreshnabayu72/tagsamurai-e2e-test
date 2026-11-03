---
id: TC-FA-FAAM-E2E-016-excess-pelepasan-status-dan-mutasi-katalog
title: "Asset Name Excess: Pelepasan Status, Delete, dan Blok In-Use pada Salinan Client Downgrade"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-237
  - TC-FA-FAAM-272
  - TC-FA-FAAM-273
  - TC-FA-FAAM-686
  - TC-FA-FAAM-729
coverage:
  web: automated
---

# Asset Name Excess: Pelepasan Status, Delete, dan Blok In-Use pada Salinan Client Downgrade

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD` ke client downgrade lain (Pre-setup #20d); halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Berpindah ke client salinan lewat langkah Ganti client eksplisit. Hook `after` mengembalikan sesi ke akun default suite dan client utama. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, `after`, dan seed API per TC dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.downgradeClient`): client downgrade lain (#20d) dengan cap 3, empat Asset Name, dan `Excess Epsilon` (terbaru, excess) ber-Total Asset 2, dipakai TC-FA-FAAM-273 tanpa mengubah data.
- Data Dinamis (salinan client Pre-setup #20 lewat seed API di hook `before`: cap 3, jumlah 4, `Excess Alpha` terlama, `Excess Beta` Total Asset 2, `Excess Delta`, `Excess Gamma` terbaru dan excess; plan sebelum downgrade memiliki cap 4; dibersihkan hook `after`):
  - `Downgrade Client 237 {runId}-016` untuk TC-FA-FAAM-237 (`Excess Delta` dihapus).
  - `Downgrade Client 272 {runId}-016` untuk TC-FA-FAAM-272 (`Excess Gamma` dihapus).
  - `Downgrade Client 686 {runId}-016` untuk TC-FA-FAAM-686 (cap dinaikkan 3 menjadi 4).
  - `Downgrade Client 729 {runId}-016` untuk TC-FA-FAAM-729 (rollback downgrade mengembalikan cap 3 menjadi 4).
- Kemampuan teknis (disediakan tim FE/BE): berpindah client untuk aktor Total Control; seed API untuk menaikkan cap plan client (langkah 6) dan rollback downgrade (langkah 14).
- State global: cap plan client salinan 686 dan 729 diubah oleh langkah 6 dan 14; hook `after` membuang client salinan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-273: Delete pada Asset Name excess ber-aset tetap diblok dialog in-use

1. Klik `⋯` baris `Excess Epsilon` lalu `Delete`
2. Verifikasi dialog `Cannot Delete Asset Name` dengan teks `This asset name is used by 2 assets and cannot be deleted.`
3. Klik `[OK]`

### TC-FA-FAAM-686: Asset Name excess kembali usable saat cap plan naik lewat upgrade

4. Ganti client ke `Downgrade Client 686 {runId}-016` dan buka tab Asset Name
5. Verifikasi baris `Excess Gamma` menampilkan badge `Over Plan Limit` (keadaan awal cap 3)
6. Seed API menaikkan cap plan client menjadi 4 hingga tersimpan
7. Buka tab Asset Name lewat klik menu sidebar `Settings > Asset Master`
8. Klik `⋯` baris `Excess Gamma`
9. Verifikasi baris `Excess Gamma` tampil tanpa badge `Over Plan Limit`
10. Verifikasi menu `⋯` baris `Excess Gamma` memuat `Edit`
11. Tekan Esc untuk menutup menu `⋯`

### TC-FA-FAAM-729: Asset Name excess kembali usable saat rollback downgrade mengembalikan cap plan

12. Ganti client ke `Downgrade Client 729 {runId}-016` dan buka tab Asset Name
13. Verifikasi baris `Excess Gamma` menampilkan badge `Over Plan Limit` (keadaan awal cap 3)
14. Seed API melakukan rollback downgrade (kembali ke plan semula dengan cap 4) hingga tersimpan
15. Buka tab Asset Name lewat klik menu sidebar `Settings > Asset Master`
16. Klik `⋯` baris `Excess Gamma`
17. Verifikasi baris `Excess Gamma` tampil tanpa badge `Over Plan Limit`
18. Verifikasi menu `⋯` baris `Excess Gamma` memuat `Edit`
19. Tekan Esc untuk menutup menu `⋯`

### TC-FA-FAAM-237: Asset Name excess kembali usable setelah jumlah Asset Name turun ke batas cap

20. Ganti client ke `Downgrade Client 237 {runId}-016` dan buka tab Asset Name
21. Verifikasi baris `Excess Gamma` menampilkan badge `Over Plan Limit` (keadaan awal jumlah 4, cap 3)
22. Klik `⋯` baris `Excess Delta` lalu `Delete`
23. Klik `[Delete]` pada dialog konfirmasi
24. Tunggu aksi Delete selesai (dialog tertutup)
25. Klik `⋯` baris `Excess Gamma`
26. Verifikasi baris `Excess Gamma` tampil tanpa badge `Over Plan Limit`
27. Verifikasi menu `⋯` baris `Excess Gamma` memuat `Edit`
28. Tekan Esc untuk menutup menu `⋯`

### TC-FA-FAAM-272: Delete pada Asset Name excess mengikuti guard in-use

29. Ganti client ke `Downgrade Client 272 {runId}-016` dan buka tab Asset Name
30. Klik `⋯` baris `Excess Gamma` lalu `Delete`
31. Verifikasi dialog konfirmasi `Delete Asset Name` tampil
32. Klik `[Delete]`
33. Verifikasi toast `Success, asset name has been deleted.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 273, 686, 729, 237, 272 (dialog blok lebih dahulu, perubahan cap, lalu aksi yang menghapus Asset Name di akhir, S-10). TC-FA-FAAM-645 berada di spec 021.
- Tiap TC memakai client salinannya sendiri, sehingga tidak ada state yang dibawa antar-TC; langkah 4, 12, 20, 29 adalah Ganti client eksplisit.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 4, 12, 20, 29 (Ganti client dan membuka tab), langkah 7 dan 15 (membuka tab sesuai Langkah uji), langkah 11, 19, 28 (menutup menu), langkah 24 (menunggu aksi Delete selesai).
- Langkah 5, 13, 21 adalah `Verifikasi` keadaan awal (badge `Over Plan Limit` tampil) yang tidak ada di Expected TC; ditambahkan sebagai prasyarat asersi "badge hilang" (S-14) dan anchor positif (bagian 8b butir 2). Langkah 9, 17, 26 memakai baris `Excess Gamma` yang tampil sebagai anchor absence badge.
- Pemicu cap plan (langkah 6 dan 14) memakai seed API ("... hingga ... tersimpan", R-20); pelaku kedua yang hanya memicu state tidak memakai `P-2`.
- Temuan untuk QA:
  - TC-237, TC-272, TC-686, TC-729, dan TC-273 tidak menyebut cara berpindah ke client salinan atau akun yang dipakai; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-237 Expected tidak menyebut toast Delete atau pembaruan List setelah `Excess Delta` dihapus; spec menunggu dialog tertutup sebelum membuka menu `Excess Gamma`.
  - TC-686 dan TC-729 Langkah uji "Naikkan cap plan ... lewat seed API" dan "Lakukan rollback downgrade ... lewat seed API" tidak menyebut endpoint atau mekanisme; spec tidak mengarang endpoint.
  - TC-272 Expected menggabungkan dialog konfirmasi dan toast sukses dalam satu butir; spec memecahnya menjadi dua `Verifikasi` (S-01).
