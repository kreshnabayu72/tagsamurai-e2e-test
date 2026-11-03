---
id: TC-FA-CAID-E2E-045-multi-konteks-race-dengan-mass-update
title: "Multi-Konteks: Registrasi, Transfer, Edit Asset, dan Mutasi Division Saat Mass Update Berjalan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-330
  - TC-FA-CAID-331
coverage:
  web: automated
---

# Multi-Konteks: Registrasi, Transfer, Edit Asset, dan Mutasi Division Saat Mass Update Berjalan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control dan Total Control sesi 2 pada `Company Big` (Pre-setup No 22) untuk TC-FA-CAID-330 dan pada `Company Big Trigger` (Pre-setup No 35) untuk TC-FA-CAID-331. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun dan password disediakan tim FE dengan env var usulan `Spectra.env.FA_BIG_TC_PASSWORD`, `Spectra.env.FA_BIG_TC2_PASSWORD` (`Company Big`), `Spectra.env.FA_BIGTRG_TC_PASSWORD`, dan `Spectra.env.FA_BIGTRG_TC2_PASSWORD` (`Company Big Trigger`). Sesi 1 dan sesi 2 `Company Big` login di hook `before` spec ini pada konteks browser terpisah; ganti akun ke `Company Big Trigger` ditulis sebagai langkah eksplisit dan hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: `Company Big` dengan 10.050 aset Active (Increment 1 sampai 10050; Group `Jakarta Office` Code `JKT`, Category `IT Equipment > Laptop` Code `LAP`, Asset Name `ThinkPad T490` Code `T490`, Purchase Date 15/09/26) dan konfigurasi B1 (No 22). `Company Big Trigger` dengan 10.050 aset Active, konfigurasi B3, aset A1 Active `JKT/LAP/T490/HR/0926/1` dengan tiket Transfer XFR-1 In Transit dari Group `Jakarta Office` ke Group `Warehouse` (Code `WH`), aset Draft D1 `JKT/LAP/T490/0000/0000/10051`, D2 `JKT/LAP/T490/0000/0926/10052`, dan D3 `JKT/LAP/T490/HR/0926/10053` (No 35). Berkas unggah `invoice.pdf` untuk Edit Asset (belum ada di `fixtures/`; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis: sesi API aktor dan seed API untuk `Company Big` dan `Company Big Trigger` (suite.md; seed 10.050 aset dan pengembaliannya disediakan tim FE/BE); kemampuan aksi pada sesi 2 selama Save sesi 1 berjalan (disediakan tim FE; TC berlabel Manual Only karena dua sesi paralel).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: konfigurasi dan Asset ID seluruh aset di kedua Company berubah. Hook `after` memulihkan `Company Big` dan `Company Big Trigger` ke seed awal lewat seed API. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-330: Registrasi aset saat Retroactive Mass Update berjalan

1. Di sesi 2 buka Fixed Asset > Assets > Registration
2. Di sesi 1 pilih Separator `- (Dash)`, lalu klik `[Save]`
3. Di sesi 2, selama Save sesi 1 berjalan, isi Quick Register dengan Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, tanpa Division, Condition `Normal`, lalu klik `[Save as Draft]`
4. Tunggu aksi selesai di sesi 1 dan sesi 2
5. Buka Fixed Asset > Assets > All Assets di sesi 1
6. Verifikasi aset hasil registrasi sesi 2 tersimpan dan memakai konfigurasi baru
7. Verifikasi Asset ID aset baru berformat Dash `JKT-LAP-T490-0000-10051`
8. Verifikasi tidak ada aset yang masih berformat Slash

### TC-FA-CAID-331: Transfer, Edit Asset, atau mutasi Division saat Retroactive Mass Update berjalan

9. Ganti akun: logout sesi 1 dan sesi 2, lalu login Total Control (sesi 1) dan Total Control sesi 2 pada `Company Big Trigger`

#### Pemicu (a) Transfer Group

10. Atur `Company Big Trigger` ke keadaan awal (konfigurasi B3, aset A1 dengan tiket XFR-1 In Transit, aset Draft D1 sampai D3; seed API), lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID di sesi 1
11. Di sesi 1 pilih Separator `- (Dash)`, lalu klik `[Save]`
12. Di sesi 2, selama Save sesi 1 berjalan, buka Fixed Asset > Transactions > Transfer, buka tab Incoming, klik `[Arrival Scan]` pada XFR-1, lakukan verifikasi unit A1, lalu klik `[Confirm Receipt]`
13. Tunggu aksi selesai di sesi 1 dan sesi 2
14. Buka Fixed Asset > Assets > All Assets di sesi 1
15. Verifikasi pemicu Transfer Group di sesi 2 selesai dan memakai konfigurasi serta recipe terbaru
16. Verifikasi Asset ID A1 menjadi `WH-LAP-T490-HR-0926-1`
17. Verifikasi tidak ada aset yang masih berformat Slash

#### Pemicu (b) Edit Asset

18. Atur `Company Big Trigger` ke keadaan awal (seed API), lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID di sesi 1
19. Di sesi 1 pilih Separator `- (Dash)`, lalu klik `[Save]`
20. Di sesi 2, selama Save sesi 1 berjalan, buka Fixed Asset > Assets > Registration, klik `[Complete Detail]` pada aset D1, isi Purchase Date `15/09/26` dan Purchase Price `15000000`, unggah faktur `invoice.pdf`, lalu klik `[Save Details]`
21. Tunggu aksi selesai di sesi 1 dan sesi 2
22. Buka Fixed Asset > Assets > All Assets di sesi 1
23. Verifikasi pemicu Edit Asset di sesi 2 selesai dan memakai konfigurasi serta recipe terbaru
24. Verifikasi Asset ID D1 menjadi `JKT-LAP-T490-0000-0926-10051`
25. Verifikasi tidak ada aset yang masih berformat Slash

#### Pemicu (c) Mutasi Division

26. Atur `Company Big Trigger` ke keadaan awal (seed API), lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID di sesi 1
27. Di sesi 1 pilih Separator `- (Dash)`, lalu klik `[Save]`
28. Di sesi 2, selama Save sesi 1 berjalan, buka Fixed Asset > Assets > Registration, edit Draft aset D2, pilih Division `Human Resources`, lalu simpan
29. Tunggu aksi selesai di sesi 1 dan sesi 2
30. Buka Fixed Asset > Assets > All Assets di sesi 1
31. Verifikasi pemicu mutasi Division di sesi 2 selesai dan memakai konfigurasi serta recipe terbaru
32. Verifikasi Asset ID D2 menjadi `JKT-LAP-T490-HR-0926-10052`
33. Verifikasi tidak ada aset yang masih berformat Slash

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular dan pemicu.
- Spec ini 33 langkah; pemicu (a), (b), dan (c) TC-FA-CAID-331 dijalankan sebagai tiga pengujian terpisah mengikuti TC ("satu pemicu pada tiap pengujian") dengan keadaan awal di-seed ulang pada langkah 10, 18, dan 26.
- Langkah penghubung: langkah 1, 5, 14, 22, dan 30 (membuka halaman), langkah 4, 13, 21, 29 (tunggu aksi selesai karena langkah berikutnya berpindah surface), langkah 9 (ganti akun), langkah 10, 18, dan 26 (seed ulang dan membuka tab Custom Asset ID).
- Langkah 6, 15, 23, dan 31 mengasersi hasil pemicu; "menunggu transaksi mass update commit" pada Expected a tidak teramati langsung di UI dan diasersi lewat hasil Asset ID yang memakai konfigurasi baru (lihat Temuan untuk QA).
- Pembagian TC lintas spec: TC-FA-CAID-324, TC-FA-CAID-326, dan TC-FA-CAID-327 ada di spec 044; TC-FA-CAID-328 dan TC-FA-CAID-329 di spec 048.
- Temuan untuk QA:
  - Pre-setup No 22 dan No 35 hanya menyebut `Company Big` dan `Company Big Trigger` "dengan Total Control dan Total Control sesi 2" tanpa email; ditulis "disediakan tim FE".
  - TC-FA-CAID-330 dan TC-FA-CAID-331 Expected a ("menunggu transaksi mass update commit") tidak punya observasi UI terpisah; diasersi lewat hasil.
  - TC-FA-CAID-331 pemicu (c) menyebut "lalu simpan" tanpa menyebut label tombol; spec menulis "simpan" mengikuti TC.
  - Waktu eksekusi Save 10.050 aset tidak disebut; "tunggu aksi selesai" memakai batas tunggu yang ditentukan tim FE.
  - Post Condition TC-FA-CAID-330 dan TC-FA-CAID-331 tidak diasersi karena TC tidak memberi langkah observasinya.
