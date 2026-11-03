---
id: TC-FA-LIC-E2E-107-pencatatan-log-edit-allocation-di-changelog-system-log
title: "Pencatatan Log Edit Allocation di Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-364
  - TC-FA-LIC-365
  - TC-FA-LIC-366
  - TC-FA-LIC-370
  - TC-FA-LIC-371
  - TC-FA-LIC-372
coverage:
  web: automated
---

# Pencatatan Log Edit Allocation di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON, General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, jam dan format tanggal): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan alokasi grup #12 (Divisi Logistik 500, Divisi Keuangan belum beralokasi, Cabang Surabaya 800). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta pada langkah 16, 25, dan 30 antar blok TC (pengecualian S-06: alokasi grup Pre-setup bernama literal tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: kolom Last Updated alokasi yang diedit berubah, dan entri baru bertambah permanen di Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log Fixed Asset (audit trail).
- Kemampuan teknis: membaca jumlah entri Changelog Allocation Quota sebelum aksi (baseline, langkah 1) disediakan tim FE/BE; asersi jumlah memakai selisih terhadap baseline. Waktu aksi dicatat sesudah `[Save]`, Date entri dibandingkan dengan toleransi satu menit, jam server dan jam browser sinkron.
- Jalur menu: System Log lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-364, TC-FA-LIC-365, TC-FA-LIC-366: Edit Divisi Logistik 500 menjadi 600 tercatat di tiga surface

1. Catat jumlah entri Changelog Allocation Quota (baseline)
2. Buka tab Allocation Quota, klik node `Kantor Pusat`
3. Klik `[Edit]` pada `Divisi Logistik`, isi `600`, klik `[Save]`
4. Catat waktu aksi sesudah `[Save]`
5. Klik ikon Changelog pada toolbar Child Groups Quota
6. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
7. Verifikasi Date entri hasil aksi, dicari lewat Group Name `Divisi Logistik`, Field `Allocated Quota`, Old Value `500`, dan New Value `600`, sesuai waktu aksi (toleransi satu menit, format General Settings)
8. Verifikasi entri hasil aksi, dicari lewat Group Name `Divisi Logistik`, Field `Allocated Quota`, Old Value `500`, dan New Value `600`: Action `Edit`, Modified By `Rudi H`
9. Verifikasi Action dan nilai ditulis plain text (bukan badge)
10. Tutup modal dengan `[×]`
11. Buka Global Settings > User > Detail Rudi Hartono > Tab System Log
12. Verifikasi entri System Log hasil aksi, dicari lewat Name `Divisi Logistik`, Field `Allocated Quota`, Old Value `500`, dan New Value `600`: Action `Edit`, Object `License`
13. Verifikasi System Log tanpa kolom Modified By
14. Buka Fixed Asset > Reports & Logs > Activity Log
15. Verifikasi entri Activity Log hasil aksi, dicari lewat Name `Divisi Logistik`, Field `Allocated Quota`, Old Value `500`, dan New Value `600`: Action `Edit`, Object `License`, Modified By `Rudi H`

### TC-FA-LIC-370: Alokasi pertama dicatat Action Edit dengan Old Value strip di tiga surface

16. Pulihkan Pre-setup #12 lewat fixture BE (Divisi Keuangan belum beralokasi)
17. Buka License > Allocation Quota, klik node `Kantor Pusat`
18. Klik `[Edit]` pada `Divisi Keuangan`, isi `50`, klik `[Save]`
19. Klik ikon Changelog pada toolbar Child Groups Quota
20. Verifikasi Changelog: Action `Edit`, Group Name `Divisi Keuangan`, Field `Allocated Quota`, Old Value `—`, New Value `50`, Modified By `Rudi H`
21. Tutup modal dengan `[×]`, lalu buka Global Settings > User > Detail Rudi Hartono > Tab System Log
22. Verifikasi System Log: Action `Edit`, Object `License`, Name `Divisi Keuangan`, Old Value `—`, New Value `50`
23. Buka Fixed Asset > Reports & Logs > Activity Log
24. Verifikasi Activity Log: Action `Edit`, Object `License`, Name `Divisi Keuangan`, Old Value `—`, New Value `50`, Modified By `Rudi H`

### TC-FA-LIC-371: Edit ke nilai 0 dicatat sebagai angka 0 (bukan Remove Allocation)

25. Pulihkan Pre-setup #12 lewat fixture BE (Divisi Keuangan belum beralokasi)
26. Buka License > Allocation Quota, klik node `Kantor Pusat`
27. Klik `[Edit]` pada `Divisi Keuangan`, isi `0`, klik `[Save]`
28. Klik ikon Changelog pada toolbar Section 2
29. Verifikasi entri hasil aksi, dicari lewat Group Name `Divisi Keuangan`, Field `Allocated Quota`, Old Value `—`, dan New Value `0`: Action `Edit`

### TC-FA-LIC-372: Edit alokasi grup level 1 dicatat dengan Group Name grup level 1

30. Tutup modal dengan `[×]`, lalu pulihkan Pre-setup #12 lewat fixture BE
31. Klik node `All Groups`, klik `[Edit]` pada `Cabang Surabaya`, isi `850` (dari 800), klik `[Save]`
32. Klik ikon Changelog pada toolbar Section 2
33. Verifikasi entri hasil aksi, dicari lewat Group Name `Cabang Surabaya`, Field `Allocated Quota`, Old Value `800`, dan New Value `850`: Action `Edit`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Pembagian TC: TC-FA-LIC-364, 365, dan 366 memakai aksi yang sama (Edit `Divisi Logistik` 500 menjadi 600) sehingga dijalankan sekali dan diamati di tiga surface (Changelog langkah 5 sampai 10, System Log langkah 11 sampai 13, Activity Log langkah 14 dan 15).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 4 mencatat baseline dan waktu aksi; langkah 10, 21, dan 30 menutup modal atau berpindah surface; langkah 16, 25, dan 30 memulihkan Pre-setup #12 antar blok (S-09).
- Entri hasil aksi dicari lewat Group Name atau Name, Field, Old Value, dan New Value, bukan posisi teratas (S-12): entri bercap waktu masa depan dari spec lain yang menggeser jam server dapat berada di atas entri baru, dan jumlah entri tetap memakai selisih terhadap baseline. Field `Allocated Quota` pada langkah 29 dan 33 melengkapi identifikasi entri; TC-FA-LIC-371 dan TC-FA-LIC-372 tidak menyebutnya.
- Temuan untuk QA:
  - TC-FA-LIC-365 butir a menyebut "tanpa kolom Modified By" di System Log tanpa langkah pengamatan lain; spec mengasersi header kolom System Log (langkah 13).
  - TC-FA-LIC-371 langkah 1 tidak menyebut navigasi ke node `Kantor Pusat`; spec memakai langkah yang sama dengan TC-FA-LIC-370.
