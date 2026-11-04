---
id: TC-FA-COA-E2E-037-popup-used-by-daftar-asset-class-urutan-dan-loading
title: "Popup Used By: Daftar Asset Class, Urutan, dan Loading"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-133
  - TC-FA-COA-134
  - TC-FA-COA-135
  - TC-FA-COA-154
  - TC-FA-COA-155
  - TC-FA-COA-287
coverage:
  web: automated
---

# Popup Used By: Daftar Asset Class, Urutan, dan Loading

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup, seluruhnya hanya dibaca dan tidak berubah (identitas dibaca dari `Fixture.settingsChartOfAccounts.p<N>`: `.code` Account Code dan `.name` Account Name; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin` | Active, Used By 0 | TC-135 |
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Used By 1 (Asset Class `Office Equipment`, 1 Asset Name) | TC-133 |
  | P7 | `4-7002 – Gain and Loss on Disposal` | Used By 2 (Asset Class `Delivery Vehicles` 3 Asset Names dan `Heavy Equipment` 12 Asset Names) | TC-134, TC-287 |
  | P11 | `4-7003 – Gain and Loss on Disposal – Shared` | Used By 1 (Asset Class `Vehicles`, 0 Asset Name, akun dipetakan pada field Gain on Disposal dan Loss on Disposal sekaligus) | TC-155 |
  | P12 | `5-6750 – Depreciation Expense – Fleet` | Used By 1 (Asset Class `Vehicles`, 0 Asset Name) | TC-154 |

- Asset Class pemakai P6, P7, P11, dan P12 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons daftar pemakai Used By (TC-287) di atas backend nyata; endpoint ditetapkan tim FE sesuai PRD/LLD, intercept dilepas pada langkah "Lepas tahanan respons".
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-135: Kolom Used By bernilai 0 tampil sebagai teks biasa dan tidak membuka popup

1. Ketik Search `Fixture.settingsChartOfAccounts.p1.code`, tekan Enter
2. Klik angka `0` di kolom Used By akun P1 (`Fixture.settingsChartOfAccounts.p1.code`)
3. Verifikasi nilai `0` tampil sebagai teks biasa (bukan link)
4. Verifikasi popup Used By tidak terbuka

### TC-FA-COA-133: Popup Used By menampilkan daftar Asset Class dan jumlah Asset Name

5. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p6.code`, tekan Enter
6. Klik angka `1` di kolom Used By akun P6 (`Fixture.settingsChartOfAccounts.p6.code`)
7. Verifikasi popup "Used By" tanpa toolbar dan tanpa tabel
8. Verifikasi teks polos satu baris `Fixture.settingsChartOfAccounts.p6.code – Fixture.settingsChartOfAccounts.p6.name (1)` di bawah judul popup
9. Verifikasi bullet `• Office Equipment — 1 Asset Name`
10. Verifikasi bullet tidak dapat diklik
11. Verifikasi popup hanya memiliki ikon close
12. Klik area backdrop di luar popup
13. Verifikasi klik backdrop tidak menutup popup
14. Klik ikon close popup
15. Verifikasi ikon close menutup popup
16. Klik angka `1` di kolom Used By akun P6 lagi
17. Tekan `Esc`
18. Verifikasi `Esc` menutup popup

### TC-FA-COA-154: Popup Used By menulis `0 Asset Names` untuk Asset Class tanpa Asset Name dan tetap menghitung Asset Class itu

19. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p12.code`, tekan Enter
20. Verifikasi nilai Used By akun P12 adalah `1`
21. Klik angka `1` di kolom Used By akun P12 (`Fixture.settingsChartOfAccounts.p12.code`)
22. Verifikasi popup "Used By" memuat teks polos satu baris `Fixture.settingsChartOfAccounts.p12.code – Fixture.settingsChartOfAccounts.p12.name (1)` di bawah judul
23. Verifikasi popup memuat satu bullet `• Vehicles — 0 Asset Names`
24. Verifikasi jumlah bullet sama dengan nilai Used By walau jumlah Asset Name 0
25. Klik ikon close popup

### TC-FA-COA-155: Used By menghitung satu Asset Class satu kali walau akun dipetakan pada Gain on Disposal dan Loss on Disposal

26. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p11.code`, tekan Enter
27. Verifikasi nilai Used By akun P11 adalah `1`, bukan `2`
28. Klik angka Used By akun P11 (`Fixture.settingsChartOfAccounts.p11.code`)
29. Verifikasi popup "Used By" memuat teks polos satu baris `Fixture.settingsChartOfAccounts.p11.code – Fixture.settingsChartOfAccounts.p11.name (1)` di bawah judul
30. Verifikasi popup memuat satu bullet `• Vehicles — 0 Asset Names`
31. Klik ikon close popup

### TC-FA-COA-134: Popup Used By mengurutkan Asset Class A-Z dan menulis jumlah bentuk jamak

32. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p7.code`, tekan Enter
33. Klik angka `2` di kolom Used By akun P7 (`Fixture.settingsChartOfAccounts.p7.code`)
34. Verifikasi teks polos satu baris `Fixture.settingsChartOfAccounts.p7.code – Fixture.settingsChartOfAccounts.p7.name (2)` di bawah judul popup
35. Verifikasi bullet urut A-Z: `• Delivery Vehicles — 3 Asset Names` lalu `• Heavy Equipment — 12 Asset Names`
36. Verifikasi jumlah bullet sama dengan nilai Used By
37. Verifikasi jumlah bullet sama dengan N pada baris identitas
38. Klik ikon close popup

### TC-FA-COA-287: Popup Used By menampilkan Loading (Shimmer) selama daftar pemakai diambil

39. Tunda respons daftar pemakai (network delay)
40. Klik angka `2` di kolom Used By akun P7 (`Fixture.settingsChartOfAccounts.p7.code`)
41. Verifikasi popup "Used By" menampilkan Loading (Shimmer) selama data belum diterima
42. Lepas tahanan respons
43. Verifikasi shimmer hilang
44. Verifikasi teks polos satu baris `Fixture.settingsChartOfAccounts.p7.code – Fixture.settingsChartOfAccounts.p7.name (2)` di bawah judul popup
45. Verifikasi dua bullet Asset Class tampil

## Notes

- Spec 45 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu topik (popup Used By) pada satu halaman; blok per akun berdiri sendiri dan hanya membaca; langkah Search, buka popup, dan tutup popup berulang per akun karena tabel berhalaman banyak.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; klik ikon close popup (langkah 25, 31, 38) menutup popup sebelum Search berikutnya.
- TC-135 dikerjakan lebih dulu karena hanya mengamati tanpa membuka popup; urutan TC lain mengikuti kompleksitas popup.
- Asersi absence langkah 4 dan 13 memakai asersi sebelumnya pada surface yang sama sebagai anchor (8b.2).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-133 menutup popup lewat ikon close dan `Esc`; Expected TC-134 menyebut "N pada baris identitas" tanpa nilai konkret selain angka Used By, sehingga langkah 37 membandingkan dengan teks pada langkah 34.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `4-7003` adalah data Pre-setup di-seed tim FE/BE dan Account Code dibatasi 15 karakter.
