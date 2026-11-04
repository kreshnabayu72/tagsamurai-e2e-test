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
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, jam dan format tanggal): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan alokasi grup #12 (Divisi Logistik 500, Divisi Keuangan belum beralokasi, Cabang Surabaya 800). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta pada langkah 21, 39, dan 47 antar blok TC (pengecualian S-06: alokasi grup Pre-setup bernama literal tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: kolom Last Updated alokasi yang diedit berubah, dan entri baru bertambah permanen di Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log Fixed Asset (audit trail).
- Kemampuan teknis: membaca jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log Fixed Asset sebelum dan sesudah aksi disediakan tim FE/BE (dinyatakan di `suite.md`). Baseline dicatat sebelum aksi pemicu tiap TC (langkah 1 sampai 3, 22 sampai 24, 40, dan 48) hanya untuk surface yang diamati TC itu, dan asersi jumlah memakai selisih terhadap baseline (S-12). Waktu aksi dicatat sesudah `[Save]`, Date entri dibandingkan dengan toleransi satu menit, jam server dan jam browser sinkron.
- Jalur menu: System Log lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-364, TC-FA-LIC-365, TC-FA-LIC-366: Edit Divisi Logistik 500 menjadi 600 tercatat di tiga surface

1. Catat jumlah entri Changelog Allocation Quota (baseline)
2. Catat jumlah entri System Log Rudi Hartono (baseline)
3. Catat jumlah entri Activity Log Fixed Asset (baseline)
4. Buka tab Allocation Quota, klik node `Kantor Pusat`
5. Klik `[Edit]` pada `Divisi Logistik`, isi `600`, klik `[Save]`
6. Tunggu aksi selesai
7. Catat waktu aksi sesudah `[Save]`
8. Klik ikon Changelog pada toolbar Child Groups Quota
9. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
10. Verifikasi Date entri pada baris teratas (urutan default Date terbaru) sesuai waktu aksi (toleransi satu menit, format General Settings)
11. Verifikasi entri pada baris teratas: Action `Edit`, Group Name `Divisi Logistik`, Field `Allocated Quota`, Old Value `500`, New Value `600`, Modified By `Rudi H`
12. Verifikasi Action dan nilai ditulis plain text (bukan badge)
13. Tutup modal dengan `[×]`
14. Buka Global Settings > User, ketik Search `Rudi Hartono`, tekan Enter
15. Klik Name `Rudi Hartono`, buka Tab System Log
16. Verifikasi jumlah entri System Log bertambah tepat satu dari baseline
17. Verifikasi entri System Log pada baris teratas: Action `Edit`, Object `License`, Name `Divisi Logistik`, Field `Allocated Quota`, Old Value `500`, New Value `600`, tanpa kolom Modified By
18. Buka Fixed Asset > Reports & Logs > Activity Log
19. Verifikasi jumlah entri Activity Log bertambah tepat satu dari baseline
20. Verifikasi entri Activity Log pada baris teratas: Action `Edit`, Object `License`, Name `Divisi Logistik`, Field `Allocated Quota`, Old Value `500`, New Value `600`, Modified By `Rudi H`

### TC-FA-LIC-370: Alokasi pertama dicatat Action Edit dengan Old Value strip di tiga surface

21. Pulihkan Pre-setup #12 lewat fixture BE
22. Catat jumlah entri Changelog Allocation Quota (baseline)
23. Catat jumlah entri System Log Rudi Hartono (baseline)
24. Catat jumlah entri Activity Log Fixed Asset (baseline)
25. Buka License > Allocation Quota, klik node `Kantor Pusat`
26. Klik `[Edit]` pada `Divisi Keuangan`, isi `50`, klik `[Save]`
27. Tunggu aksi selesai
28. Klik ikon Changelog pada toolbar Child Groups Quota
29. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
30. Verifikasi Changelog pada baris teratas: Action `Edit`, Group Name `Divisi Keuangan`, Field `Allocated Quota`, Old Value `—`, New Value `50`, Modified By `Rudi H`
31. Tutup modal dengan `[×]`
32. Buka Global Settings > User, ketik Search `Rudi Hartono`, tekan Enter
33. Klik Name `Rudi Hartono`, buka Tab System Log
34. Verifikasi jumlah entri System Log bertambah tepat satu dari baseline
35. Verifikasi System Log pada baris teratas: Action `Edit`, Object `License`, Name `Divisi Keuangan`, Old Value `—`, New Value `50`
36. Buka Fixed Asset > Reports & Logs > Activity Log
37. Verifikasi jumlah entri Activity Log bertambah tepat satu dari baseline
38. Verifikasi Activity Log pada baris teratas: Action `Edit`, Object `License`, Name `Divisi Keuangan`, Old Value `—`, New Value `50`, Modified By `Rudi H`

### TC-FA-LIC-371: Edit ke nilai 0 dicatat sebagai angka 0 (bukan Remove Allocation)

39. Pulihkan Pre-setup #12 lewat fixture BE
40. Catat jumlah entri Changelog Allocation Quota (baseline)
41. Buka License > Allocation Quota, klik node `Kantor Pusat`
42. Klik `[Edit]` pada `Divisi Keuangan`, isi `0`, klik `[Save]`
43. Tunggu aksi selesai
44. Klik ikon Changelog pada toolbar Section 2
45. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
46. Verifikasi entri Changelog pada baris teratas: Group Name `Divisi Keuangan`, Field `Allocated Quota`, Old Value `—`, New Value `0`, Action `Edit`

### TC-FA-LIC-372: Edit alokasi grup level 1 dicatat dengan Group Name grup level 1

47. Tutup modal dengan `[×]`, lalu pulihkan Pre-setup #12 lewat fixture BE
48. Catat jumlah entri Changelog Allocation Quota (baseline)
49. Klik node `All Groups`, klik `[Edit]` pada `Cabang Surabaya`, isi `850`, klik `[Save]`
50. Tunggu aksi selesai
51. Klik ikon Changelog pada toolbar Section 2
52. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
53. Verifikasi entri Changelog pada baris teratas: Group Name `Cabang Surabaya`, Field `Allocated Quota`, Old Value `800`, New Value `850`, Action `Edit`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Pembagian TC: TC-FA-LIC-364, 365, dan 366 memakai aksi yang sama (Edit `Divisi Logistik` 500 menjadi 600) sehingga dijalankan sekali dan diamati di tiga surface (Changelog langkah 8 sampai 12, System Log langkah 14 sampai 17, Activity Log langkah 18 sampai 20).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 sampai 3, 22 sampai 24, 40, dan 48 mencatat baseline jumlah entri; langkah 7 mencatat waktu aksi; langkah 6, 27, 43, dan 50 menunggu aksi `[Save]` selesai sebelum berpindah surface (bagian 8b butir 8); langkah 13, 31, dan 47 menutup modal atau berpindah surface; langkah 21, 39, dan 47 memulihkan Pre-setup #12 antar blok (S-09); langkah 14, 15, 32, dan 33 mencari baris `Rudi Hartono` lewat Search sebelum membuka Detail (R-16, bagian 8b butir 13), Search tidak dibersihkan karena spec tidak kembali ke daftar User.
- Cara baca entri hasil aksi (S-12, S-14): baseline dicatat ulang sebelum aksi tiap TC pada tiap surface yang diamati TC itu (TC-FA-LIC-371 dan 372 hanya mengamati Changelog, sehingga surface lain tidak dicatat); sesudah aksi, selisih jumlah entri = 1 dibuktikan lebih dulu, lalu entri dibaca pada baris teratas urutan default `Date` terbaru. Selisih satu berarti himpunan baris teratas hanya satu baris, sehingga tidak ada urutan antar entri yang diandalkan. Nilai yang sama tiap run (`Divisi Logistik` 500 ke 600) bukan satu-satunya bukti entri baru. Field `Allocated Quota` pada langkah 46 dan 53 melengkapi identifikasi entri; TC-FA-LIC-371 dan TC-FA-LIC-372 tidak menyebutnya.
- Verifikasi selisih jumlah entri pada TC-FA-LIC-370, 371, dan 372 (langkah 29, 34, 37, 45, dan 52) tidak ada di Expected TC; ditambahkan karena S-12 memperlakukan asersi "memuat entri" atas audit trail sebagai asersi entri baru.
- Spec ini 53 langkah. Alasan di atas sekitar 35 langkah: seluruh blok adalah pencatatan log Edit Allocation pada tiga surface log yang sama dengan dataset Pre-setup #12 yang sama, tiap blok berdiri sendiri (dipulihkan fixture BE di awal), dan S-12 menuntut baseline dan Verifikasi selisih per TC per surface sehingga langkah baseline dan selisih tidak dapat digabung.
- Temuan untuk QA:
  - TC-FA-LIC-371 langkah 1 tidak menyebut navigasi ke node `Kantor Pusat`; spec memakai langkah yang sama dengan TC-FA-LIC-370.
