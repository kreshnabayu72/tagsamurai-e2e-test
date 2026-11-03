---
id: TC-FA-LIC-E2E-068-retensi-state-sub-tab-riwayat-dan-tab-license-pindah-tab
title: "Retensi State: Sub-tab Riwayat dan Tab License saat Berpindah Tab, serta Reset dari Menu License"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-218
  - TC-FA-LIC-219
  - TC-FA-LIC-221
  - TC-FA-LIC-536
coverage:
  web: automated
---
# Retensi State: Sub-tab Riwayat dan Tab License saat Berpindah Tab, serta Reset dari Menu License

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Data Pre-setup #26 (hanya dibaca): lima sesi cuplikan tabel Concurrent User (Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso), lewat `Fixture.fixedAssetLicense.sesiAktif` (fixture belum ada; disediakan tim FE/BE). Search `Safari` pada Tab `Concurrent User` hanya dipakai untuk mengamati state Search, hasil tabel tidak diasersi.
- State yang diubah dan dipulihkan: Search dan Filter tabel Subscription History, Allocation History, dan Active Sessions (dibersihkan pada langkah 13 dan 38; klik menu `License` pada langkah 27 mereset state halaman).

## Test Steps

### TC-FA-LIC-218: State sub-tab riwayat independen

1. Klik sub-tab `Subscription History`
2. Ketik Search `Active`, tekan Enter
3. Klik sub-tab `Allocation History`
4. Verifikasi Allocation History tampil tanpa Search dan Filter dari sub-tab lain (enam baris: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001)
5. Klik ikon Filter, pada field `Status` centang `Expired`, lalu klik `[Apply]`
6. Klik ikon Filter untuk menutup panel
7. Klik sub-tab `Subscription History`
8. Verifikasi Search `Active` masih aktif dan hasil sama seperti sebelumnya: SUBS-20260101-00001
9. Verifikasi ikon Filter Subscription History tanpa badge titik (tidak ada filter ter-Apply pada sub-tab ini)
10. Klik sub-tab `Allocation History`
11. Verifikasi Filter Status `Expired` tetap pada sub-tab Allocation History: LALC-20250210-00001
12. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`, lalu klik ikon Filter untuk menutup panel
13. Klik sub-tab `Subscription History`, lalu klik `(←)` pada kotak Search

### TC-FA-LIC-219: Pindah antar tab License memulihkan state tabel

14. Klik sub-tab `Allocation History`
15. Ketik Search `Audit`, tekan Enter
16. Klik Tab `Concurrent User`
17. Ketik Search `Safari`, tekan Enter
18. Klik Tab `All License`
19. Verifikasi Tab All License dibuka pada sub-tab `Subscription History`
20. Klik sub-tab `Allocation History`
21. Verifikasi Search `Audit` dipulihkan pada tabel Allocation History
22. Klik Tab `Concurrent User`
23. Verifikasi Tab Concurrent User memulihkan Search `Safari`

### TC-FA-LIC-221: Klik ulang menu License mereset semua state

24. Klik Tab `All License`
25. Klik sub-tab `Allocation History`
26. Ketik Search `Audit`, tekan Enter
27. Klik menu `License` pada sidebar navigasi
28. Verifikasi halaman License terbuka di Tab `All License`
29. Verifikasi sub-tab aktif `Subscription History`
30. Verifikasi tanpa Search, Filter, dan Sort yang aktif

### TC-FA-LIC-536: Pindah Tab License lain lalu kembali

31. Klik sub-tab `Allocation History`
32. Ketik Search `Audit`, tekan Enter
33. Klik Tab `Concurrent User`
34. Klik Tab `All License`
35. Verifikasi sub-tab aktif `Subscription History`, bukan `Allocation History`
36. Klik sub-tab `Allocation History`
37. Verifikasi Search `Audit` pada Allocation History masih aktif
38. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Urutan TC dalam spec: 218, 219, 221, 536 (TC-FA-LIC-221 mereset state halaman sebelum TC-FA-LIC-536 mengandalkan state bersih). TC-FA-LIC-219 memiliki Dependensi TC-FA-LIC-218; langkah TC-FA-LIC-218 yang dibutuhkan (Search di Allocation History) ditulis penuh pada TC-FA-LIC-219 (S-04).
- Spec ini di atas 35 langkah (38 langkah nominal). Alasan: seluruh blok satu topik (retensi state halaman License), satu dataset yang hanya dibaca, dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); setiap `Verifikasi` sesuai satu klausa Expected TC (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): klik sub-tab dan Tab sebagai aksi deterministik (termasuk langkah pertama setiap blok), langkah "Klik ikon Filter untuk menutup panel" dan `[Clear Field]` serta `[Apply]` pada TC-FA-LIC-218 (pemulihan Filter; S-09), langkah 13 dan 38 (mengosongkan Search; S-09).
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-218 `Verifikasi` Allocation History enam baris dan hasil Filter Status `Expired` (LALC-20250210-00001) diturunkan dari Pre-setup #13; `Verifikasi` ikon Filter Subscription History tanpa badge titik (indikator filter aktif) membuktikan "Filter Allocation History tetap pada sub-tab itu".
- Temuan untuk QA:
  - TC-FA-LIC-218 (langkah TC 3) tidak punya Expected hasil tabel setelah Filter Status `Expired`; spec tidak mengasersi hasil itu saat menerapkannya, hanya sesudah kembali ke sub-tab.
  - TC-FA-LIC-219 menulis "Search `Safari`" pada Tab `Concurrent User` tanpa Expected hasil tabel; spec hanya mengasersi pemulihan state Search.
  - TC-FA-LIC-218, 219, 221, dan 536 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
