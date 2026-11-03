---
id: TC-AC-LA-E2E-137-log-cancel-dan-resubmit-tiga-surface
title: "Log Cancel dan Resubmit di Tiga Surface: Cancel Waiting for Approval, Resubmit sebagai Create Baru, dan Cancel Pending oleh Total Control"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-391
  - TC-AC-LA-399
  - TC-AC-LA-392
coverage:
  web: automated
---

# Log Cancel dan Resubmit di Tiga Surface: Cancel Waiting for Approval, Resubmit sebagai Create Baru, dan Cancel Pending oleh Total Control

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Ganti akun ke Fajar Nugroho dilakukan eksplisit pada blok TC-AC-LA-392; hook `after` mengembalikan sesi ke akun default suite. Flag Guided Tooltip diatur hook `before` suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update (requester) | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (pelaku pembatalan) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Require Approval for Allocation ON (Pre-setup #38).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41, #46, dan #48 bersama):
  - `{idWfa}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost $150.00 di-Reserve (bentuk Pre-setup #41);
  - `{idCanceled}`: alokasi `Canceled` manual Concurrent User +5 PT Sejahtera, requester Dewi Anggraini (bentuk Pre-setup #48);
  - `{idPend}`: alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini, Cost $3,650.00 di-Reserve (bentuk Pre-setup #46);
  - `{idResub}`: Allocation ID hasil Resubmit pada langkah di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; kemampuan membaca jumlah entri log per Allocation ID.
- State global: tidak ada yang diubah selain saldo kantong #33 akibat Resubmit dan Cancel; saldo dipulihkan oleh pembersihan record di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Log Cancel dari Waiting for Approval (TC-AC-LA-391)

1. Ketik Search `{idWfa}`, tekan Enter
2. Klik row action `Cancel Allocation` pada baris `{idWfa}` milik sendiri
3. Klik `[Cancel Request]`
4. Tunggu aksi selesai
5. Klik ikon `Changelog` pada List
6. Ketik Search `{idWfa}`, tekan Enter
7. Verifikasi Changelog memuat entri Action `Cancel`, Field `Status`, Old `Waiting for Approval`, New `Canceled`
8. Tutup modal Changelog
9. Buka Detail User `Dewi Anggraini` > tab System Log
10. Ketik Search `{idWfa}`, tekan Enter
11. Verifikasi System Log aktor memuat entri Action `Cancel`, Status `Waiting for Approval` ke `Canceled`
12. Buka Activity Log Admin Console
13. Ketik Search `{idWfa}`, tekan Enter
14. Verifikasi Activity Log memuat entri Action `Cancel`, Status `Waiting for Approval` ke `Canceled`, Modified By `Dewi A`
15. Buka Allocation > License Allocation (tab Current)
16. Catat baseline Allocation ID baris di halaman pertama tab Current

### Log Resubmit dicatat sebagai Create baru (TC-AC-LA-399)

17. Klik tab `History`
18. Ketik Search `{idCanceled}`, tekan Enter
19. Klik row action `Resubmit` pada baris `{idCanceled}`
20. Klik `[Submit]`
21. Klik `(←)` pada kotak Search, lalu klik tab `Current`
22. Catat Allocation ID record baru sebagai `{idResub}` (tidak ada pada baseline langkah 16)
23. Klik ikon `Changelog` pada List
24. Ketik Search `{idResub}`, tekan Enter
25. Verifikasi Changelog memuat entri Action `Create` dengan Allocation ID `{idResub}` (berbeda dari `{idCanceled}`) dan Field `Allocation Details`
26. Verifikasi Changelog untuk `{idResub}` dan `{idCanceled}` tidak memuat baris Action `Resubmit`
27. Tutup modal Changelog
28. Buka Detail User `Dewi Anggraini` > tab System Log
29. Ketik Search `{idResub}`, tekan Enter
30. Verifikasi System Log aktor memuat entri Action `Create` dengan Name `{idResub}` dan Field `Allocation Details`
31. Verifikasi System Log aktor untuk `{idResub}` dan `{idCanceled}` tidak memuat baris Action `Resubmit`
32. Buka Activity Log Admin Console
33. Ketik Search `{idResub}`, tekan Enter
34. Verifikasi Activity Log memuat entri Action `Create` dengan Name `{idResub}` dan Field `Allocation Details`
35. Verifikasi Activity Log untuk `{idResub}` dan `{idCanceled}` tidak memuat baris Action `Resubmit`

### Log Cancel dari Pending oleh pelaku pembatalan (TC-AC-LA-392)

36. Ganti akun: Logout dari Dewi Anggraini
37. Login sebagai Fajar Nugroho (`totalControlDistLic`, password `Spectra.env.AC_LA_TC_DIST_PASSWORD`)
38. Buka Allocation > License Allocation (tab Current)
39. Ketik Search `{idPend}`, tekan Enter
40. Klik row action `Cancel Allocation` pada baris Pending `{idPend}` milik `Dewi A`
41. Klik `[Cancel Request]`
42. Tunggu aksi selesai
43. Klik ikon `Changelog` pada List
44. Ketik Search `{idPend}`, tekan Enter
45. Verifikasi Changelog memuat entri Action `Cancel`, Status `Pending` ke `Canceled`
46. Tutup modal Changelog
47. Buka Detail User `Fajar Nugroho` > tab System Log
48. Ketik Search `{idPend}`, tekan Enter
49. Verifikasi System Log `Fajar Nugroho` (aktor pembatalan) memuat entri Action `Cancel`, Status `Pending` ke `Canceled`
50. Buka Activity Log Admin Console
51. Ketik Search `{idPend}`, tekan Enter
52. Verifikasi Activity Log memuat entri Action `Cancel`, Status `Pending` ke `Canceled`, Modified By `Fajar N`

## Notes

- P-1: langkah 26, 31, dan 35 adalah asersi absence baris Action `Resubmit` untuk TC-AC-LA-399 butir b; spec absence tidak memuat TC ini sehingga asersi ditulis di sini dengan anchor positif (entri `Create` pada langkah 25, 30, dan 34 di surface yang sama) dan data milik spec. Alasan: record `Canceled` dengan Reserve wallet dan hasil Resubmit adalah state berat yang dibangun langkah sebelumnya pada blok ini (S-05).
- Alasan di atas sekitar 35 langkah (52 langkah): ketiga blok satu topik (pencatatan Cancel dan Resubmit pada tiga surface), satu kelas harness fungsional, dan masing-masing memakai record seed sendiri sehingga berdiri sendiri. Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung pada ambang smell; langkah aksi sekitar 15 termasuk ganti akun.
- Langkah penghubung (S-03, R-16): langkah 4 dan 42 (menunggu aksi selesai karena langkah berikutnya berpindah surface, 8b butir 8), langkah 1, 6, 10, 13, 18, 24, 29, 33, 39, 44, 48, dan 51 (Search baris atau entri berdasarkan Allocation ID), langkah 8, 27, dan 46 (menutup modal Changelog), langkah 15 dan 38 (kembali ke List), langkah 16 (baseline Allocation ID baris di halaman pertama tab Current sebelum `[Submit]` Resubmit, S-12, pola spec 042), langkah 17 (pindah tab History), langkah 21 (mengosongkan Search `{idCanceled}` lewat klik `(←)` pada kotak Search, lalu pindah ke tab Current karena record baru hanya tampil di tab Current dan Search tidak dibawa antar tab; pencatatan ID pada langkah 22 sebanding dengan baseline langkah 16), langkah 36 sampai 38 (ganti akun).
- Pembagian TC lintas spec: TC-AC-LA-388, 389, dan 390 (Edit) ada di spec 124.
- Temuan untuk QA:
  - TC-AC-LA-391, 399, dan 392 tidak menyebut cara menemukan entri di Changelog, System Log, dan Activity Log; spec memakai Search dengan Allocation ID unik.
  - TC-AC-LA-399 butir a tidak menyebut nilai Old, New, atau isi Allocation Details record baru; spec hanya mengasersi Action, Allocation ID baru, dan Field.
  - TC-AC-LA-399 butir b ("tidak ada baris Action `Resubmit` terpisah") tidak menyebut surface; spec memakai ketiga surface.
  - TC-AC-LA-392 menyebut "Cancel record Pending milik `Dewi A` sebagai Total Control" tanpa menyebut toggle Require Approval; spec memakai ON sesuai suite (Pre-setup #38) dan tidak mengubahnya.
  - TC-AC-LA-392 hanya mencantumkan akun #10 di ACC, sedangkan record Pending berasal dari requester `Dewi A`; spec memakai Dewi Anggraini (Pre-setup #4) sebagai pemilik seed sesuai Pre-setup #46.
