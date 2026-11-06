---
id: TC-AC-LA-E2E-019-role-matrix-positif-allocate-per-capability
title: "Role Matrix Positif: Allocate License per Capability dan Peran"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-72
  - TC-AC-LA-80
  - TC-AC-LA-83
  - TC-AC-LA-84
  - TC-AC-LA-85
coverage:
  web: automated
---

# Role Matrix Positif: Allocate License per Capability dan Peran

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read tanpa Update (Pre-setup #5) `createOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Doni Prasetyo`), password `Spectra.env.AC_LA_DIST_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Default User Principal (Pre-setup #2) `defaultUserLic_automated_{namaCompany}@qwertysystem.net` (`Sari Pratama`), password `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD`; Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; Partner satu kantong (Pre-setup #15) `partnerFullLic_automated_{namaCompany}@qwertysystem.net` (`Rian Tarigan`), password `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`; Group Manager dengan Manage allocation (Pre-setup #9) `gmAllocLic_automated_{namaCompany}@qwertysystem.net` (`Hadi Setiawan`), password `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Client | Target | Type dan Quantity | Require Approval | Hasil |
|---|---|---|---|---|---|---|
| `createOnlyLic` (`Doni Prasetyo`) | Distributor Create+Read | `PT Sejahtera` | `SUBS-20260101-A1B2C` | `Concurrent User`, `2` | OFF | `Active`, Allocated By `Doni P` |
| `defaultUserLic` (`Sari Pratama`) | Default User Principal | `PT Sejahtera` | `SUBS-20260101-A1B2C` | `Concurrent User`, `1` | OFF | `Active`, Payment `Free`, Allocated By `Sari P` |
| `totalControlLic` (`Hendra Wijaya`) | Total Control Principal | `PT Sejahtera` | `SUBS-20260101-A1B2C` | `Concurrent User`, `3` | OFF | `Active`, Payment `Free`, Paid From `—`, Cost `—` |
| `partnerFullLic` (`Rian Tarigan`) | Partner satu kantong | `PT Abadi Jaya` | `SUBS-20260110-C1D2E` | `Concurrent User`, `2` | OFF | Allocated By `Rian T`, Payment `Wallet` |
| `gmAllocLic` (`Hadi Setiawan`) | Group Manager + Manage allocation | `Gudang Cimahi Retail` | term FAMS Professional `Active` | `Audit`, `30` | ON | `Active` langsung, Allocated By `Hadi S` |

- Data Pre-setup: #19 PT Sejahtera, #25 PT Abadi Jaya, #32 hierarki group Region Jawa > Cabang Bandung > Gudang Cimahi dengan Client Gudang Cimahi Retail, #33 saldo kantong wallet (Distributor PT Maju Bersama $10,000.00; Partner CV Karya Mandiri $5,000.00; Principal $5,000.00), #34 Product Price, #38 Require Approval ON, #39 Require Approval OFF. Spec membuat alokasi baru (data Dinamis, Completed); record dibersihkan baseline automation/fixture backend di hook `after`.
- State global yang diubah: Require Approval for Allocation diatur OFF (Pre-setup #39) di hook `before` spec ini untuk TC-AC-LA-72, TC-AC-LA-80, TC-AC-LA-84, dan TC-AC-LA-85, dan ON hanya untuk TC-AC-LA-83 lewat fixture backend yang disediakan tim FE/BE (mekanisme tidak tertulis di TC); nilai awal dipulihkan di langkah penghubung akhir dan di hook `after`. Saldo kantong berkurang oleh alokasi Wallet dan dipulihkan fixture backend. Suite berjalan serial.
- Konfigurasi kolom Setup Column yang disimpan spec (kolom Payment, Paid From, dan Cost) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).
- Urutan akun: `createOnlyLic` (hook `before`), `defaultUserLic`, `totalControlLic`, `partnerFullLic`, `gmAllocLic`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps
1. Pastikan kolom Payment, Paid From, dan Cost tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, Paid From, dan Cost, lalu klik `[Save]`

### TC-AC-LA-72: Create+Read tanpa Update mengalokasikan sampai sukses

2. Catat baseline Allocation ID baris di halaman pertama tab Current
3. Klik `[+ Allocation]`, pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `2`
4. Klik `[Submit]`
5. Verifikasi toast sukses: "Success, license has been allocated."
6. Verifikasi baris baru tab Current (Allocation ID tidak ada pada baseline langkah 2) berstatus `Active`
7. Verifikasi Allocated By baris baru: `Doni P`

### TC-AC-LA-80: Default User menjalankan Allocate penuh dengan akses otomatis

8. Ganti akun: Logout lalu login sebagai Default User Principal (`defaultUserLic`), lalu buka Allocation > License Allocation tab Current
9. Tampilkan ulang kolom Payment, Paid From, dan Cost sesudah ganti akun: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, Paid From, dan Cost, lalu klik `[Save]`
10. Catat baseline Allocation ID baris di halaman pertama tab Current
11. Klik `[+ Allocation]`, pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `1`
12. Klik `[Submit]`
13. Verifikasi toast sukses: "Success, license has been allocated."
14. Verifikasi baris baru tab Current (Allocation ID tidak ada pada baseline langkah 10) berstatus `Active`
15. Verifikasi Payment baris baru: `Free`
16. Verifikasi Allocated By baris baru: `Sari P`

### TC-AC-LA-84: Total Control Principal menjalankan Allocate dengan Payment Free

17. Ganti akun: Logout lalu login sebagai Total Control Principal (`totalControlLic`), lalu buka Allocation > License Allocation tab Current
18. Tampilkan ulang kolom Payment, Paid From, dan Cost sesudah ganti akun: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, Paid From, dan Cost, lalu klik `[Save]`
19. Catat baseline Allocation ID baris di halaman pertama tab Current
20. Klik `[+ Allocation]`, lalu pilih Client `PT Sejahtera` dan Target `SUBS-20260101-A1B2C`
21. Verifikasi opsi Type memuat `Concurrent User`
22. Verifikasi opsi Type tidak memuat `Log Source`
23. Verifikasi Section Payment Method tidak dirender pada form
24. Pilih Type `Concurrent User` dan isi Additional Quantity `3`
25. Klik `[Submit]`
26. Verifikasi baris baru tab Current (Allocation ID tidak ada pada baseline langkah 19) berstatus `Active`
27. Verifikasi Payment baris baru: `Free`
28. Verifikasi Paid From baris baru: `—`
29. Verifikasi Cost baris baru: `—`

### TC-AC-LA-85: Partner menjalankan Allocate ke Client yang dipegang

30. Ganti akun: Logout lalu login sebagai Partner satu kantong (`partnerFullLic`), lalu buka Allocation > License Allocation tab Current
31. Tampilkan ulang kolom Payment, Paid From, dan Cost sesudah ganti akun: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, Paid From, dan Cost, lalu klik `[Save]`
32. Catat baseline Allocation ID baris di halaman pertama tab Current
33. Klik `[+ Allocation]`, pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`, dan isi Additional Quantity `2`
34. Verifikasi Section Payment menampilkan Preview Cost
35. Verifikasi Section Payment menampilkan Your pocket balance
36. Klik `[Submit]`
37. Verifikasi baris baru tab Current (Allocation ID tidak ada pada baseline langkah 32) memiliki Allocated By `Rian T`
38. Verifikasi Payment baris baru: `Wallet`

### TC-AC-LA-83: Group Manager dengan Manage allocation bypass approval

39. Atur Require Approval for Allocation menjadi ON pada group Client uji lewat fixture backend
40. Tunggu aksi selesai
41. Ganti akun: Logout lalu login sebagai Group Manager + Manage allocation (`gmAllocLic`), lalu buka Allocation > License Allocation tab Current
42. Catat baseline Allocation ID baris di halaman pertama tab Current
43. Klik `[+ Allocation]`, pilih Client `Gudang Cimahi Retail`, Target term FAMS Professional berstatus Active, Type `Audit`, dan isi Additional Quantity `30`
44. Klik `[Submit]`
45. Verifikasi alokasi baru (Allocation ID tidak ada pada baseline langkah 42) langsung `Completed` berstatus `Active`
46. Verifikasi alokasi baru itu tidak melalui `Waiting for Approval`
47. Verifikasi Allocated By alokasi baru: `Hadi S`
48. Klik row action `Allocation Log` pada alokasi baru
49. Catat jumlah entri Allocation Log alokasi baru sebagai baseline
50. Verifikasi entri `Allocation created by Hadi S` tampil pada Allocation Log alokasi baru (anchor)
51. Verifikasi tidak ada entri `Allocation approved` pada Allocation Log alokasi baru
52. Tutup modal Allocation Log
53. Atur Require Approval for Allocation kembali ke OFF lewat fixture backend

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Setup Column (menampilkan kolom, tanpa `Verifikasi`; langkah 1 untuk akun pertama, langkah 9, 18, dan 31 menampilkan ulang kolom sesudah ganti akun karena preferensi kolom lintas akun tidak dijamin, S-14), langkah `Tunggu aksi selesai` (40, 8b butir 8; Require Approval ditulis lewat fixture backend sebelum ganti akun), langkah mengatur Require Approval lewat fixture backend, langkah 48 (membuka Allocation Log alokasi baru lewat row action), langkah 49 (baseline jumlah entri Allocation Log, S-12), langkah 52 (menutup modal Allocation Log sebelum langkah berikutnya, S-09), dan ganti akun eksplisit (S-07). Langkah `Catat baseline Allocation ID` (S-12) dicatat sebelum tiap `[Submit]`; baris hasil alokasi adalah baris di halaman pertama tab Current yang Allocation ID-nya tidak ada pada baseline, sehingga Submit yang gagal tidak meloloskan baris lama.
- Langkah penghubung (S-03): pembukaan Allocation > License Allocation tab Current di dalam langkah Ganti akun, karena halaman landing akun tidak diandaikan (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil dan data berbeda per role.
- Spec ini di atas 35 langkah. Alasannya: semua blok satu topik (Allocate License oleh role berbeda) dan satu kelas harness (Role Matrix), dan tiap blok akun berdiri sendiri dengan data milik sendiri; kegagalan satu akun tidak membuat blok akun lain kehilangan makna.
- Urutan akun diubah dari urutan TC (72, 80, 83, 84, 85) menjadi 72, 80, 84, 85, 83 supaya Require Approval ON hanya dipasang sekali untuk TC-AC-LA-83 di akhir (S-10).
- Temuan untuk QA:
  - TC-AC-LA-72, TC-AC-LA-80, TC-AC-LA-84, TC-AC-LA-85, dan TC-AC-LA-83 tidak menyebut cara mengatur Require Approval (Pre-setup #38 dan #39); spec memakai fixture backend yang disediakan tim FE/BE.
  - Post Condition TC-AC-LA-72 (`saldo kantong Distributor berkurang sebesar Cost`), TC-AC-LA-84 (`Tidak ada Reserve atau Capture`), dan TC-AC-LA-85 (`Kantong Partner berkurang sebesar Cost`) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Post Condition TC-AC-LA-83 (`Tidak ada entri Allocation approved`) diasersi di langkah 51 dengan baseline langkah 49 dan anchor entri `Allocation created` langkah 50 (klausa log; TC tidak menyebut surface, spec memakai Allocation Log alokasi baru).
  - TC-AC-LA-83 langkah 2 menyebut `Target term FAMS Professional berstatus Active` tanpa label opsi Target; label opsi ditulis sesuai TC.
  - TC-AC-LA-72, TC-AC-LA-80, TC-AC-LA-84, TC-AC-LA-85, dan TC-AC-LA-83 mengasersi hasil pada baris `Allocation baru`; TC tidak menyebut cara menemukan baris, sehingga spec mencatat baseline Allocation ID halaman pertama sebelum tiap `[Submit]` dan memakai baris yang Allocation ID-nya tidak ada pada baseline (S-12).
