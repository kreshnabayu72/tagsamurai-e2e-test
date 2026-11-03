---
id: TC-AC-LA-E2E-124-log-edit-tiga-surface
title: "Log Edit di Tiga Surface: Type dan Quantity, Pending ke Waiting for Approval, dan Pending ke Active"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-388
  - TC-AC-LA-389
  - TC-AC-LA-390
coverage:
  web: automated
---

# Log Edit di Tiga Surface: Type dan Quantity, Pending ke Waiting for Approval, dan Pending ke Active

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update (requester) | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), Toko Serba Ada (Pre-setup #21; term Active `SUBS-20250201-J7K8L`, term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Require Approval for Allocation ON (Pre-setup #38) untuk blok TC-AC-LA-388 dan TC-AC-LA-389, OFF (Pre-setup #39) untuk blok TC-AC-LA-390.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41 dan #46 bersama):
  - `{idEdit}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost $150.00 di-Reserve (bentuk Pre-setup #41);
  - `{idPendSend}` dan `{idPendTarget}`: dua alokasi `Completed` berstatus lisensi `Pending`, Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini, Cost $3,650.00 di-Reserve (bentuk Pre-setup #46).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; fixture backend untuk menyetel Require Approval for Allocation ON atau OFF dan memulihkannya.
- State global: toggle Require Approval for Allocation diubah ke OFF sebelum blok TC-AC-LA-390 dan dipulihkan di hook `after`; saldo kantong #33 dipulihkan oleh pembersihan record seed.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Edit Type dan Quantity: satu baris per atribut yang berubah (TC-AC-LA-388)

1. Ketik Search `{idEdit}`, tekan Enter
2. Klik row action `Edit` pada baris `{idEdit}`
3. Ubah Type dari `Concurrent User` menjadi `Asset License`
4. Ubah Additional Quantity dari `5` menjadi `8`
5. Klik `[Save]`
6. Tunggu aksi selesai
7. Klik ikon `Changelog` pada List
8. Ketik Search `{idEdit}`, tekan Enter
9. Verifikasi Changelog memuat satu baris Action `Edit` dengan Field `Type`, Old `Concurrent User`, New `Asset License`, dan satu baris Action `Edit` dengan Field `Additional Quantity`, Old `5`, New `8`
10. Verifikasi Changelog untuk `{idEdit}` hanya memuat dua baris `Edit` tersebut, tanpa baris untuk atribut yang tidak berubah termasuk Field `Target`
11. Tutup modal Changelog
12. Buka Detail User `Dewi Anggraini` > tab System Log
13. Ketik Search `{idEdit}`, tekan Enter
14. Verifikasi System Log aktor memuat baris `Edit` yang sama per atribut (Field `Type` Old `Concurrent User` New `Asset License`; Field `Additional Quantity` Old `5` New `8`)
15. Verifikasi System Log untuk `{idEdit}` hanya memuat dua baris `Edit` tersebut, tanpa Field `Target`
16. Buka Activity Log Admin Console
17. Ketik Search `{idEdit}`, tekan Enter
18. Verifikasi Activity Log memuat baris `Edit` yang sama per atribut dengan Modified By `Dewi A`
19. Verifikasi Activity Log untuk `{idEdit}` hanya memuat dua baris `Edit` tersebut, tanpa Field `Target`
20. Buka Allocation > License Allocation (tab Current)

### Edit Pending kembali ke Waiting for Approval: baris Status (TC-AC-LA-389)

21. Ketik Search `{idPendSend}`, tekan Enter
22. Klik row action `Edit` pada baris Pending `{idPendSend}`
23. Ubah Additional Quantity menjadi `20`
24. Klik `[Save]`
25. Klik `[Send]` pada D-04
26. Tunggu aksi selesai
27. Klik ikon `Changelog` pada List
28. Ketik Search `{idPendSend}`, tekan Enter
29. Verifikasi Changelog memuat baris Action `Edit`, Field `Status`, Old `Pending`, New `Waiting for Approval`
30. Verifikasi Changelog memuat baris perubahan Quantity (Field `Additional Quantity`, Old `10`, New `20`)
31. Tutup modal Changelog
32. Buka Detail User `Dewi Anggraini` > tab System Log
33. Ketik Search `{idPendSend}`, tekan Enter
34. Verifikasi System Log aktor memuat baris `Edit` Status `Pending` ke `Waiting for Approval`
35. Verifikasi System Log memuat baris perubahan Quantity
36. Buka Activity Log Admin Console
37. Ketik Search `{idPendSend}`, tekan Enter
38. Verifikasi Activity Log memuat baris `Edit` Status `Pending` ke `Waiting for Approval`
39. Verifikasi Activity Log memuat baris perubahan Quantity
40. Buka Allocation > License Allocation (tab Current)

### Edit Pending langsung Active: baris Status dan Target (TC-AC-LA-390)

41. Setel Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend
42. Ketik Search `{idPendTarget}`, tekan Enter
43. Klik row action `Edit` pada baris Pending `{idPendTarget}`
44. Ganti Target ke term Active `SUBS-20250201-J7K8L`
45. Klik `[Save]`
46. Tunggu aksi selesai
47. Klik ikon `Changelog` pada List
48. Ketik Search `{idPendTarget}`, tekan Enter
49. Verifikasi Changelog memuat baris Action `Edit`, Field `Status`, Old `Pending`, New `Active`
50. Verifikasi Changelog memuat satu baris `Edit` Field `Target` dengan Old Value `SUBS-20260819-00001` dan New Value `SUBS-20250201-J7K8L`
51. Tutup modal Changelog
52. Buka Detail User `Dewi Anggraini` > tab System Log
53. Ketik Search `{idPendTarget}`, tekan Enter
54. Verifikasi System Log aktor memuat baris `Edit` Status `Pending` ke `Active`
55. Verifikasi System Log memuat satu baris `Edit` Field `Target` dengan Old Value `SUBS-20260819-00001` dan New Value `SUBS-20250201-J7K8L`
56. Buka Activity Log Admin Console
57. Ketik Search `{idPendTarget}`, tekan Enter
58. Verifikasi Activity Log memuat baris `Edit` Status `Pending` ke `Active`
59. Verifikasi Activity Log memuat satu baris `Edit` Field `Target` dengan Old Value `SUBS-20260819-00001` dan New Value `SUBS-20250201-J7K8L`

## Notes

- Alasan di atas sekitar 35 langkah: ketiga blok satu topik (pencatatan Edit oleh Dewi Anggraini pada tiga surface), satu kelas harness fungsional, dan masing-masing memakai record seed sendiri sehingga berdiri sendiri. Sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung pada ambang smell; langkah aksi Edit hanya 15.
- Langkah penghubung (S-03, R-16): langkah 6, 26 dan 46 (menunggu aksi selesai karena langkah berikutnya berpindah surface, 8b butir 8), langkah 1, 8, 13, 17, 21, 28, 33, 37, 42, 48, 53, dan 57 (Search baris atau entri berdasarkan Allocation ID), langkah 11 dan 31 dan 51 (menutup modal Changelog), langkah 20 dan 40 (kembali ke List), langkah 41 (menyetel toggle).
- Urutan blok mengikuti kebutuhan toggle (ON untuk TC-AC-LA-388 dan TC-AC-LA-389, OFF untuk TC-AC-LA-390) dan sama dengan urutan sourceTc. TC-AC-LA-391, 399, dan 392 (Cancel dan Resubmit) ada di spec 137.
- TC-AC-LA-388 butir d ("tidak ada baris untuk atribut yang tidak berubah, termasuk Field `Target`") ditulis sebagai asersi jumlah dengan anchor baris `Type` dan `Additional Quantity` pada surface yang sama (langkah 10, 15, dan 19); ini bukan kelas g.
- Temuan untuk QA:
  - TC-AC-LA-388, 389, dan 390 tidak menyebut cara menemukan entri di Changelog, System Log, dan Activity Log; spec memakai Search dengan Allocation ID unik.
  - TC-AC-LA-389 butir c ("Baris perubahan Quantity ikut tercatat") tidak menyebut surface maupun nilai Old dan New; spec memakai ketiga surface dan nilai dari seed (Old `10`, New `20`).
  - TC-AC-LA-389 menyebut `[Send]` pada D-04 tanpa menjelaskan dialog D-04; spec mengikuti penulisan TC.
  - TC-AC-LA-388 tidak menyebut nilai toggle Require Approval; spec memakai ON karena record sumber berstatus `Waiting for Approval` (Pre-setup #38).
  - TC-AC-LA-390 mensyaratkan Toko Serba Ada (Pre-setup #21) di Precondition sebagai Client record Pending; Target semula `SUBS-20260819-00001` diturunkan dari Expected TC dan Pre-setup #46.
