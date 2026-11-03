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
- Data Pre-setup yang diubah spec: hierarki dan alokasi grup #12 (Divisi IT beralokasi 100 tanpa subgroup) dan sesi aktif Pre-setup #14 (sesi Budi Santoso, tidak aktif lebih dari 2 jam; akun login Budi Santoso disediakan tim FE). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta pada langkah 12 antar blok TC (pengecualian S-06: alokasi dan sesi Pre-setup tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: kolom Last Updated alokasi Divisi IT berubah, sesi Budi Santoso berakhir, dan entri baru bertambah permanen di Changelog Allocation Quota, Changelog Concurrent User, System Log Rudi Hartono, dan Activity Log Fixed Asset.
- Kemampuan teknis: membaca jumlah entri Changelog Allocation Quota dan Changelog Concurrent User sebelum aksi (baseline, langkah 1 dan 13) disediakan tim FE/BE; asersi jumlah memakai selisih terhadap baseline.
- Jalur menu: System Log lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-367, TC-FA-LIC-368, TC-FA-LIC-369: Remove Allocation Divisi IT tercatat di tiga surface

1. Catat jumlah entri Changelog Allocation Quota (baseline)
2. Buka tab Allocation Quota, klik node `Kantor Pusat`
3. Klik `[Edit]` pada `Divisi IT`, klik `[Clear Field]`, klik `[Save]`
4. Klik ikon Changelog pada toolbar Child Groups Quota
5. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
6. Verifikasi entri baru: Action `Remove Allocation`, Group Name `Divisi IT`, Field `Allocated Quota`, Old Value `100`, New Value `—`, Modified By `Rudi H`
7. Tutup modal dengan `[×]`
8. Buka Global Settings > User > Detail Rudi Hartono > Tab System Log
9. Verifikasi entri System Log hasil aksi, dicari lewat Name `Divisi IT`, Field `Allocated Quota`, Old Value `100`, dan New Value `—`: Action `Remove Allocation`, Object `License`
10. Buka Fixed Asset > Reports & Logs > Activity Log
11. Verifikasi entri Activity Log hasil aksi, dicari lewat Name `Divisi IT`, Field `Allocated Quota`, Old Value `100`, dan New Value `—`: Action `Remove Allocation`, Object `License`, Modified By `Rudi H`

### TC-FA-LIC-373, TC-FA-LIC-374, TC-FA-LIC-375: Force Logout sesi Budi Santoso tercatat di tiga surface

12. Pulihkan Pre-setup #12 dan #14 lewat fixture BE (sesi Budi Santoso aktif)
13. Catat jumlah entri Changelog Concurrent User (baseline)
14. Buka License > Concurrent User, ketik Search `Budi`, tekan Enter
15. Klik `[Force Logout]` pada baris Budi Santoso
16. Klik `[Confirm Logout]` pada dialog `Force Logout User`
17. Tunggu aksi selesai (baris Budi Santoso hilang dari daftar)
18. Buka Global Settings > User > Detail Rudi Hartono > Tab System Log
19. Verifikasi entri System Log hasil aksi, dicari lewat Name `Budi Santoso`, Field `Session Status`, Old Value `Active`, dan New Value `Force Logged Out`: Action `Force Logout`, Object `License`
20. Buka Fixed Asset > Reports & Logs > Activity Log
21. Verifikasi entri Activity Log hasil aksi, dicari lewat Name `Budi Santoso`, Field `Session Status`, Old Value `Active`, dan New Value `Force Logged Out`: Action `Force Logout`, Object `License`, Modified By `Rudi H`
22. Buka License > Concurrent User, klik ikon Changelog pada toolbar
23. Verifikasi modal berjudul `Changelog: Concurrent User`
24. Verifikasi jumlah entri Changelog Concurrent User bertambah tepat satu dari baseline
25. Verifikasi entri baru: Action `Force Logout`, User Name `Budi Santoso`, Field `Session Status`, Old Value `Active`, New Value `Force Logged Out`, Modified By `Rudi H`
26. Tutup modal dengan `[×]`, lalu klik icon panah `(←)` di kiri toolbar Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Pembagian TC: TC-FA-LIC-367, 368, dan 369 memakai aksi yang sama (Remove Allocation `Divisi IT`) dan TC-FA-LIC-373, 374, dan 375 memakai aksi yang sama (Force Logout `Budi Santoso`), sehingga tiap aksi dijalankan sekali dan diamati di tiga surface.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 13 mencatat baseline; langkah 7 dan 26 menutup modal; langkah 12 memulihkan Pre-setup antar blok; langkah 14 menemukan baris target lewat Search `Budi` (R-16); langkah 17 menunggu aksi selesai sebelum berpindah surface (bagian 8b butir 8).
- Entri hasil aksi di System Log dan Activity Log dicari lewat Name, Field, Old Value, dan New Value, bukan posisi teratas (S-12): entri bercap waktu masa depan dari spec lain dapat berada di atas entri baru; Field melengkapi identifikasi entri.
- Temuan untuk QA:
  - TC-FA-LIC-373 langkah 1 ("Force Logout sesi Budi Santoso") tidak merinci dialog; spec memakai `[Force Logout]` dan `[Confirm Logout]` dari TC-FA-LIC-175 dan TC-FA-LIC-615.
  - TC-FA-LIC-367 butir a tidak menyebut jumlah entri; spec menambahkan selisih jumlah terhadap baseline untuk klausa "entri baru" (S-12).
