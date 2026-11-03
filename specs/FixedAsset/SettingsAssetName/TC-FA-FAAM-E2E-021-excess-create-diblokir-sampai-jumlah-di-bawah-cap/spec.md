---
id: TC-FA-FAAM-E2E-021-excess-create-diblokir-sampai-jumlah-di-bawah-cap
title: "Asset Name Excess: Create Baru Diblokir Selama Jumlah Sama dengan atau di Atas Cap, Diterima Setelah Jumlah di Bawah Cap"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-645
coverage:
  web: automated
---

# Asset Name Excess: Create Baru Diblokir Selama Jumlah Sama dengan atau di Atas Cap, Diterima Setelah Jumlah di Bawah Cap

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Berpindah ke client salinan lewat langkah Ganti client eksplisit (langkah 1). Hook `after` mengembalikan sesi ke akun default suite dan client utama. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, `after`, dan seed API per TC dirujuk apa adanya.
- Data Dinamis (salinan client Pre-setup #20 lewat seed API di hook `before`, dibersihkan hook `after`): `Downgrade Client 645 {runId}-021` dengan cap 3, jumlah 4 (`Excess Alpha` terlama, `Excess Beta`, `Excess Delta`, `Excess Gamma` terbaru dan excess; Total Asset `Excess Alpha` dan `Excess Delta` 0); plan sebelum downgrade memiliki cap 4.
- Data Uji Create (suffix `{runId}-021`): Asset Name `Create Min Item {runId}-021`; Category `IT Equipment`; TAG Type `QR`; Brand `Dell`; UoM `Unit` (master data Pre-setup #22 s.d. #24). Asset Name yang dibuat berada di client salinan dan dibuang bersama client oleh hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): berpindah client untuk aktor Total Control.
- State global: tidak ada yang diubah selain client aktif sesi (dipulihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-645: Downgrade: Asset Name excess read-only selama Grace dan Create baru diblokir sampai dalam batas

1. Ganti client ke `Downgrade Client 645 {runId}-021` dan buka tab Asset Name
2. Klik `[+ Asset Name]`
3. Isi field wajib: Asset Name `Create Min Item {runId}-021`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`
4. Klik `[Submit]`
5. Verifikasi dialog kuota `Asset Name Limit Reached` tampil
6. Klik `[OK]` pada dialog kuota
7. Klik `✕` pada Modal Create
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`
10. Klik `⋯` baris `Excess Delta` lalu `Delete`
11. Klik `[Delete]` pada dialog konfirmasi
12. Tunggu aksi Delete selesai (dialog tertutup)
13. Klik `⋯` baris `Excess Alpha` lalu `Delete`
14. Klik `[Delete]` pada dialog konfirmasi
15. Tunggu aksi Delete selesai (dialog tertutup)
16. Klik `[+ Asset Name]`
17. Isi field wajib yang sama: Asset Name `Create Min Item {runId}-021`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`
18. Klik `[Submit]`
19. Verifikasi toast `Success, asset name has been created.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Spec ini memuat TC-FA-FAAM-645 yang berada di topik yang sama dengan spec 016 (kondisi excess pada salinan client downgrade); TC-FA-FAAM-645 hanya muncul di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 (Ganti client dan membuka tab), langkah 6 (menutup dialog kuota sesuai Langkah uji), langkah 7 dan 9 (menutup form dirty dengan `✕` dan `[Leave]`, S-08; `Verifikasi` dialog `Unsaved Changes` pada langkah 8 diwajibkan S-08), langkah 12 dan 15 (menunggu aksi Delete selesai; jumlah Asset Name menjadi 3 lalu 2).
- Dua penghapusan (langkah 10 sampai 15) memakai `Excess Delta` dan `Excess Alpha` (Total Asset 0) dari salinan client sesuai Langkah uji 3; jumlah menjadi 2, di bawah cap 3.
- Tidak ada asersi tambahan di luar Expected a (langkah 5) dan b (langkah 19).
- Temuan untuk QA:
  - TC-645 judul menyebut "Asset Name excess read-only selama Grace" tetapi Langkah uji dan Expected tidak memuat asersi read-only atau Grace; spec hanya mengasersi dialog kuota dan Create yang diterima.
  - TC-645 Langkah 1 menulis "isi field wajib sesuai Data Uji"; Data Uji tidak menyebut nilai TAG Type selain `QR`; spec memakai nilai Data Uji apa adanya.
  - TC-645 Expected a menyebut jumlah 4 "sama dengan atau di atas cap 3" tanpa menyebut teks isi dialog `Asset Name Limit Reached`; spec hanya mengasersi judulnya.
  - TC-645 tidak menyebut cara berpindah ke client salinan; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
