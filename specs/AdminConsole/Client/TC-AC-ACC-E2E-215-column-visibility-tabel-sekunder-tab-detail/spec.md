---
id: TC-AC-ACC-E2E-215-column-visibility-tabel-sekunder-tab-detail
title: "Column Visibility Tabel Sekunder Tab Subscription, TAG, Hardware, dan Storage"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-818
  - TC-AC-ACC-819
  - TC-AC-ACC-820
  - TC-AC-ACC-822
  - TC-AC-ACC-823
  - TC-AC-ACC-824
coverage:
  web: automated
---

# Column Visibility Tabel Sekunder Tab Subscription, TAG, Hardware, dan Storage

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): C-01 "PT Sejahtera Abadi". Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Preferensi kolom tabel sekunder disimpan di browser; hook suite `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, dinyatakan sekali di `suite.md`). Spec juga memulihkan kolom yang disembunyikan lewat langkah eksplisit di akhir tiap TC.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-818: Column Visibility pada tabel Tab Subscription: License Quota, Fixed Asset Module, Addon Features, Purchase History License

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Klik ⋯ pada header tabel License Quota
5. Verifikasi panel Column Visibility License Quota memuat License Type, Total, Used, Available dengan checkbox tercentang dan item "Setup Column..." di bagian bawah
6. Hapus centang kolom Used
7. Verifikasi kolom Used hilang dari tabel License Quota
8. Klik ⋯ pada header tabel Fixed Asset Module
9. Verifikasi panel Column Visibility Fixed Asset Module memuat Feature, Value, Source
10. Hapus centang kolom Source
11. Verifikasi kolom Source hilang dari tabel Fixed Asset Module
12. Klik ⋯ pada header tabel Addon Features
13. Verifikasi panel Column Visibility Addon Features memuat Feature, Qty
14. Hapus centang kolom Qty
15. Verifikasi kolom Qty hilang dari tabel Addon Features
16. Klik ⋯ pada header tabel Purchase History License
17. Verifikasi panel Column Visibility Purchase History License memuat Subscription, Plan, Item, Purchase Type, Duration, Activation Date, Expired Date, Qty, Source, Action by, Date
18. Hapus centang kolom Qty
19. Verifikasi kolom Qty hilang dari tabel Purchase History License
20. Centang kembali kolom Used (License Quota), Source (Fixed Asset Module), Qty (Addon Features), dan Qty (Purchase History License)

### TC-AC-ACC-819: Column Visibility pada tabel Tab TAG: Quota dan Purchase History TAG

21. Klik Tab `TAG`
22. Klik ⋯ pada header tabel Quota
23. Verifikasi panel Column Visibility Quota memuat Type, Total Quota, Used, Available dan item "Setup Column..." di bagian bawah
24. Hapus centang kolom Used
25. Verifikasi kolom Used hilang dari tabel Quota
26. Klik ⋯ pada header tabel Purchase History TAG
27. Verifikasi panel Column Visibility Purchase History TAG memuat Type, Qty, Source, Action by, Date
28. Hapus centang kolom Source
29. Verifikasi kolom Source hilang dari tabel Purchase History TAG
30. Centang kembali kolom Used (Quota) dan Source (Purchase History TAG)

### TC-AC-ACC-820: Column Visibility pada tabel Tab Hardware: Hardware List, Quota, Purchase History Hardware

31. Klik Tab `Hardware`
32. Klik ⋯ pada header tabel Hardware List
33. Verifikasi panel Column Visibility Hardware List memuat Photo, Category, Type, Brand, Model/Type, SKU, Qty dan item "Setup Column..." di bagian bawah
34. Hapus centang kolom Brand
35. Verifikasi kolom Brand hilang dari tabel Hardware List
36. Klik ⋯ pada header tabel Quota
37. Verifikasi panel Column Visibility Quota memuat Category, Type, Total Quota, Used, Available
38. Hapus centang kolom Type
39. Verifikasi kolom Type hilang dari tabel Quota
40. Klik ⋯ pada header tabel Purchase History Hardware
41. Verifikasi panel Column Visibility Purchase History Hardware memuat Category, Type, Qty, Source, Action by, Date
42. Hapus centang kolom Action by
43. Verifikasi kolom Action by hilang dari tabel Purchase History Hardware
44. Centang kembali kolom Brand (Hardware List), Type (Quota), dan Action by (Purchase History Hardware)

### TC-AC-ACC-822: Column Visibility pada tabel Tab Storage: Quota dan Purchase History Storage

45. Klik Tab `Storage`
46. Klik ⋯ pada header tabel Quota
47. Verifikasi panel Column Visibility Quota memuat Total (GB), Used (GB), Available (GB) dan item "Setup Column..." di bagian bawah
48. Hapus centang kolom Available (GB)
49. Verifikasi kolom Available (GB) hilang dari tabel Quota
50. Klik ⋯ pada header tabel Purchase History Storage
51. Verifikasi panel Column Visibility Purchase History Storage memuat Qty (GB), Source, Action by, Date
52. Hapus centang kolom Source
53. Verifikasi kolom Source hilang dari tabel Purchase History Storage
54. Centang kembali kolom Available (GB) dan Source

### TC-AC-ACC-824: Kolom terakhir yang tersisa pada tabel sekunder tidak dapat di-uncheck

55. Klik ⋯ pada header tabel Quota
56. Hapus centang kolom Used (GB)
57. Hapus centang kolom Available (GB)
58. Verifikasi hanya kolom Total (GB) yang tampil pada tabel Quota
59. Arahkan kursor ke checkbox kolom Total (GB)
60. Verifikasi checkbox Total (GB) tetap tampil namun berstatus disabled
61. Verifikasi tooltip pada checkbox Total (GB): "At least one column must remain visible."
62. Centang kembali kolom Used (GB) dan Available (GB)

### TC-AC-ACC-823: Pengaturan kolom tabel sekunder tersimpan terpisah per tabel dan bertahan setelah muat ulang

63. Klik Tab `TAG`
64. Klik ⋯ pada header tabel Purchase History TAG lalu hapus centang kolom Source
65. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat tabel Purchase History License
66. Verifikasi tabel Purchase History License tetap menampilkan kolom Source
67. Klik Tab `TAG` lalu lihat tabel Purchase History TAG
68. Verifikasi tabel Purchase History TAG tidak menampilkan kolom Source
69. Muat ulang halaman Detail lalu klik Tab `TAG`
70. Lihat tabel Purchase History TAG
71. Verifikasi tabel Purchase History TAG tetap tidak menampilkan kolom Source
72. Centang kembali kolom Source pada Purchase History TAG

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pengaturan kolom pada satu Client, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah "Centang kembali kolom ..." di akhir tiap TC adalah langkah pemulihan (S-09, S-03). TC-824 diletakkan sebelum TC-823 karena TC-823 mengakhiri spec dengan muat ulang halaman (prinsip 6).
- Temuan untuk QA (S-15): TC-818 menyebut item "Setup Column..." di bagian bawah panel; TC-820, TC-822, TC-819 menyebut hal yang sama. Setup Column (modal) tidak diuji di spec ini. Post Condition seluruh TC memulihkan centang; dipenuhi langkah pemulihan eksplisit di spec ini.
