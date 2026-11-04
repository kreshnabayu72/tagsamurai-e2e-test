---
id: TC-FA-LIC-E2E-108-pencatatan-log-remove-allocation-dan-force-logout-di-tiga
title: "Pencatatan Log Remove Allocation dan Force Logout di Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-367
  - TC-FA-LIC-368
  - TC-FA-LIC-369
  - TC-FA-LIC-373
  - TC-FA-LIC-374
  - TC-FA-LIC-375
coverage:
  web: automated
---

# Pencatatan Log Remove Allocation dan Force Logout di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON, General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan alokasi grup #12 (Divisi IT beralokasi 100 tanpa subgroup) dan sesi aktif Pre-setup #14 (sesi Budi Santoso berupa sesi seed tanpa login, tidak aktif lebih dari 2 jam; sesi diakhiri aksi Force Logout di langkah 19 dan dipulihkan fixture BE). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta pada langkah 16 antar blok TC (pengecualian S-06: alokasi dan sesi Pre-setup tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: kolom Last Updated alokasi Divisi IT berubah, sesi Budi Santoso berakhir, dan entri baru bertambah permanen di Changelog Allocation Quota, Changelog Concurrent User, System Log Rudi Hartono, dan Activity Log Fixed Asset.
- Kemampuan teknis: membaca jumlah entri Changelog Allocation Quota, Changelog Concurrent User, System Log Rudi Hartono, dan Activity Log Fixed Asset sebelum aksi (baseline, langkah 1 dan 17) disediakan tim FE/BE; asersi jumlah memakai selisih terhadap baseline dan dibuktikan lebih dulu sebelum isi entri dibaca (S-12).
- Jalur menu: System Log lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-367, TC-FA-LIC-368, TC-FA-LIC-369: Remove Allocation Divisi IT tercatat di tiga surface

1. Catat jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log Fixed Asset (baseline)
2. Buka tab Allocation Quota, klik node `Kantor Pusat`
3. Klik `[Edit]` pada `Divisi IT`, klik `[Clear Field]`, klik `[Save]`
4. Tunggu aksi selesai
5. Klik ikon Changelog pada toolbar Child Groups Quota
6. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
7. Verifikasi entri pada baris teratas (urutan default Date terbaru): Action `Remove Allocation`, Group Name `Divisi IT`, Field `Allocated Quota`, Old Value `100`, New Value `—`, Modified By `Rudi H`
8. Tutup modal dengan `[×]`
9. Buka Global Settings > User, ketik Search `Rudi Hartono`, tekan Enter
10. Klik Name `Rudi Hartono`, buka Tab System Log
11. Verifikasi jumlah entri System Log Rudi Hartono bertambah tepat satu dari baseline
12. Verifikasi entri System Log pada baris teratas: Action `Remove Allocation`, Object `License`, Name `Divisi IT`, Field `Allocated Quota`, Old Value `100`, New Value `—`
13. Buka Fixed Asset > Reports & Logs > Activity Log
14. Verifikasi jumlah entri Activity Log Fixed Asset bertambah tepat satu dari baseline
15. Verifikasi entri Activity Log pada baris teratas: Action `Remove Allocation`, Object `License`, Name `Divisi IT`, Field `Allocated Quota`, Old Value `100`, New Value `—`, Modified By `Rudi H`

### TC-FA-LIC-373, TC-FA-LIC-374, TC-FA-LIC-375: Force Logout sesi Budi Santoso tercatat di tiga surface

16. Pulihkan Pre-setup #12 dan #14 lewat fixture BE (sesi Budi Santoso aktif)
17. Catat jumlah entri Changelog Concurrent User, System Log Rudi Hartono, dan Activity Log Fixed Asset (baseline)
18. Buka License > Concurrent User, ketik Search `Budi`, tekan Enter
19. Klik `[Force Logout]` pada baris Budi Santoso
20. Klik `[Confirm Logout]` pada dialog `Force Logout User`
21. Tunggu aksi selesai
22. Buka Global Settings > User, ketik Search `Rudi Hartono`, tekan Enter
23. Klik Name `Rudi Hartono`, buka Tab System Log
24. Verifikasi jumlah entri System Log Rudi Hartono bertambah tepat satu dari baseline
25. Verifikasi entri System Log pada baris teratas: Action `Force Logout`, Object `License`, Name `Budi Santoso`, Field `Session Status`, Old Value `Active`, New Value `Force Logged Out`
26. Buka Fixed Asset > Reports & Logs > Activity Log
27. Verifikasi jumlah entri Activity Log Fixed Asset bertambah tepat satu dari baseline
28. Verifikasi entri Activity Log pada baris teratas: Action `Force Logout`, Object `License`, Name `Budi Santoso`, Field `Session Status`, Old Value `Active`, New Value `Force Logged Out`, Modified By `Rudi H`
29. Buka License > Concurrent User, klik ikon Changelog pada toolbar
30. Verifikasi modal berjudul `Changelog: Concurrent User`
31. Verifikasi jumlah entri Changelog Concurrent User bertambah tepat satu dari baseline
32. Verifikasi entri pada baris teratas: Action `Force Logout`, User Name `Budi Santoso`, Field `Session Status`, Old Value `Active`, New Value `Force Logged Out`, Modified By `Rudi H`
33. Tutup modal dengan `[×]`, lalu klik icon panah `(←)` di kiri toolbar Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Pembagian TC: TC-FA-LIC-367, 368, dan 369 memakai aksi yang sama (Remove Allocation `Divisi IT`) dan TC-FA-LIC-373, 374, dan 375 memakai aksi yang sama (Force Logout `Budi Santoso`), sehingga tiap aksi dijalankan sekali dan diamati di tiga surface.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 17 mencatat baseline; langkah 8 dan 33 menutup modal; langkah 16 memulihkan Pre-setup antar blok; langkah 9, 10, 22, dan 23 mencari baris `Rudi Hartono` lewat Search sebelum membuka Detail dan langkah 18 menemukan baris target lewat Search `Budi` (R-16, bagian 8b butir 13); langkah 4 dan 21 menunggu aksi `[Save]` atau `[Confirm Logout]` selesai sebelum membuka log atau berpindah surface (bagian 8b butir 8).
- Selisih jumlah entri +1 diverifikasi per surface (langkah 6, 11, 14, 24, 27, dan 31) sebelum isi entri dibaca.
- Cara baca entri hasil aksi (S-12, S-14): selisih jumlah entri = 1 dibuktikan lebih dulu per surface, lalu entri dibaca pada baris teratas urutan default `Date` terbaru. Selisih satu berarti himpunan baris teratas hanya satu baris, sehingga tidak ada urutan antar entri yang diandalkan.
- Temuan untuk QA:
  - TC-FA-LIC-373 langkah 1 ("Force Logout sesi Budi Santoso") tidak merinci dialog; spec memakai `[Force Logout]` dan `[Confirm Logout]` dari TC-FA-LIC-175 dan TC-FA-LIC-615.
