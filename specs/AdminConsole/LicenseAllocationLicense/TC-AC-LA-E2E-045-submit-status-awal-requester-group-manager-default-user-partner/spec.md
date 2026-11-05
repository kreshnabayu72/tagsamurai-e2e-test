---
id: TC-AC-LA-E2E-045-submit-status-awal-requester-group-manager-default-user-partner
title: "Submit Allocate: Status Awal Requester Group Manager, Default User, Partner, dan Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-163
  - TC-AC-LA-164
  - TC-AC-LA-530
  - TC-AC-LA-173
coverage:
  web: automated
---

# Submit Allocate: Status Awal Requester Group Manager, Default User, Partner, dan Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager dengan Manage allocation `gmAllocLic_automated_{namaCompany}@qwertysystem.net` (`Hadi Setiawan`, Pre-setup #9), password `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Default User Principal `defaultUserLic_automated_{namaCompany}@qwertysystem.net` (`Sari Pratama`, Pre-setup #2), password `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD`; Partner satu kantong `partnerFullLic_automated_{namaCompany}@qwertysystem.net` (`Rian Tarigan`, Pre-setup #15), password `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`; Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`; di luar scope group Group Manager `Hadi Setiawan` namun dalam irisan scope Manage allocation), PT Abadi Jaya (#25, `SUBS-20260110-C1D2E`), kantong wallet (#33), Product Price (#34), kantong Partner CV Karya Mandiri (#33).
- Toggle Require Approval for Allocation: ON (#38) untuk TC-AC-LA-163, 164, dan 530 (diatur di hook `before`), OFF (#39) untuk TC-AC-LA-173 (diatur lewat langkah 40); diatur fixture backend (disediakan tim FE/BE) dan dipulihkan ke keadaan awal di hook `after`.
- Jam: tanggal acuan server uji 22 Dec 2026 (fixture waktu, nilai absolut, disediakan tim FE/BE) untuk TC-AC-LA-530; jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: empat alokasi Concurrent User ke PT Sejahtera (+2 oleh Hadi S dan +2 oleh Sari P, Waiting for Approval; +4 oleh Hendra W, Completed Active Free) dan ke PT Abadi Jaya (+2 oleh Rian T, Waiting for Approval, Reserve $20.00). Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong, Reserve, dan ledger kuota dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dan saldo kantong dicatat sebelum tiap `[Submit]`.
- Kemampuan teknis: membaca saldo kantong Partner (disediakan tim FE/BE); membuka Activity Log dan mencari entri berdasarkan Allocation ID; menampilkan kolom Payment lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-163: Requester Group Manager di luar scope Client sendiri dengan toggle ON

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `2`
4. Klik `[Submit]`
5. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 1) berstatus `Waiting for Approval` (bukan bypass)

### TC-AC-LA-164: Aktor Principal dengan toggle ON tetap Waiting for Approval tanpa Reserve

6. Ganti akun: logout `Hadi S`, login sebagai `Sari Pratama` dengan `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD`, buka Allocation > License Allocation tab Current
7. Pastikan kolom Payment tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, lalu klik `[Save]`
8. Catat baseline Allocation ID baris di halaman pertama tab Current
9. Klik `[+ Allocation]`
10. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `2`, lalu catat Current Quota
11. Klik `[Submit]`
12. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 8) berstatus `Waiting for Approval`
13. Verifikasi Payment `Free` tanpa Reserve
14. Klik `[+ Allocation]`
15. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`
16. Verifikasi Current Quota term tidak berubah dari nilai langkah 10
17. Klik `[×]` pada header
18. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
19. Klik `[Leave]`

### TC-AC-LA-530: Partner dengan toggle ON menghasilkan Waiting for Approval dengan Reserve pada kantong Partner

20. Ganti akun: logout `Sari P`, login sebagai `Rian Tarigan` dengan `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`, buka Allocation > License Allocation tab Current
21. Pastikan kolom Payment tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, lalu klik `[Save]`
22. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo Available, Reserved, Balance kantong Partner
23. Klik `[+ Allocation]`
24. Pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`, isi Additional Quantity `2`, lalu catat Current Quota
25. Klik `[Submit]`
26. Verifikasi toast sukses "Success, license has been allocated."
27. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 22): status `Waiting for Approval`
28. Verifikasi severity status baris baru: warning
29. Verifikasi Allocated By baris baru: `Rian T`
30. Verifikasi Payment baris baru: `Wallet`
31. Verifikasi Reserved kantong Partner naik `$20.00`
32. Verifikasi Available kantong Partner turun `$20.00`
33. Verifikasi Balance kantong Partner tidak berubah
34. Klik `[+ Allocation]`
35. Pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`
36. Verifikasi Current Quota term tidak berubah dari nilai langkah 24
37. Klik `[×]` pada header
38. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
39. Klik `[Leave]`

### TC-AC-LA-173: Principal tidak memiliki wallet, tanpa Reserve atau Capture dan Payment Free

40. Atur toggle Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend hingga tersimpan
41. Ganti akun: logout `Rian T`, login sebagai `Hendra Wijaya` dengan `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`, buka Allocation > License Allocation tab Current
42. Pastikan kolom Payment tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, lalu klik `[Save]`
43. Catat baseline Allocation ID baris di halaman pertama tab Current
44. Klik `[+ Allocation]`
45. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `4`
46. Klik `[Submit]`
47. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 43) berstatus `Active`
48. Verifikasi Payment baris baru: `Free`
49. Buka Activity Log dan cari entri alokasi baru berdasarkan Allocation ID
50. Verifikasi entri alokasi baru tampil pada Activity Log (ditemukan lewat Allocation ID)
51. Verifikasi baris Activity Log memakai teks New Value tanpa `Paid via wallet`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 6 kali, kejadian menutup 6 (modal tertutup oleh Submit di langkah 4, 11, 25, dan 46; dialog Leave di langkah 17 sampai 19 dan 37 sampai 39).
- Spec 51 langkah, di atas smell 35 langkah, dengan empat blok satu topik (status awal hasil Submit per jenis requester) yang berdiri sendiri: tiap blok memakai akun dan alokasi sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Empat akun berbeda menuntut tiga langkah ganti akun eksplisit (S-07).
- Penyimpangan urutan (S-10): TC-AC-LA-173 (toggle OFF) dijalankan paling akhir supaya toggle hanya dialihkan sekali (langkah 40).
- Langkah penghubung (S-03): langkah 7, 21, dan 42 (menampilkan kolom Payment lewat Setup Column, tanpa `Verifikasi`; kolom Payment tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii; diulang setelah tiap ganti akun karena tampilan kolom tidak diandaikan terbawa), langkah 1, 8, 22, dan 43 (baseline), langkah 14 sampai 19 dan 34 sampai 39 (membuka form ulang untuk mengamati Current Quota lalu menutup form dirty, S-08), langkah 40 (mengatur toggle), langkah 49 (membuka Activity Log).
- Temuan untuk QA:
  - TC-AC-LA-163 Precondition ("Client PT Sejahtera di luar scope group Group Manager ini namun masih dalam irisan scope Manage allocation") tidak menyebut cara membuktikan atau menyiapkan irisan scope itu; kondisi diasumsikan tersedia pada akun Pre-setup #9 (Hadi Setiawan).
  - TC-AC-LA-164 Expected b ("kuota term tidak berubah") dan TC-AC-LA-530 Expected d ("Current Quota term tidak berubah") menyebut Current Quota tanpa lokasi pengamatan; spec mengamati Current Quota di form Allocate berikutnya.
  - TC-AC-LA-173 Expected a ("tidak ada mutasi wallet") tidak dapat diamati karena Principal tidak memiliki wallet; yang diasersi adalah Payment `Free` dan teks Activity Log tanpa `Paid via wallet` (Expected b). Sub-asersi mutasi wallet dicatat tanpa langkah.
  - TC-AC-LA-173 Expected b tidak menyebut teks New Value persis; spec hanya mengasersi bahwa `Paid via wallet` tidak ada pada baris Activity Log yang ditemukan lewat Allocation ID (anchor positif: langkah 50).
  - Pre-setup #15 (Rian Tarigan) pada TC-AC-LA-530 memakai kantong dari Pre-setup #33 sedangkan #35 memberi kantong yang sama saldo $20.00 (TC-AC-LA-144); lihat Temuan spec 028 dan 032.
