---
id: TC-FA-COA-E2E-064-audit-log-edit-account-code-activate-deactivate-dan-delete
title: "Audit Log: Edit Account Code, Activate Deactivate, dan Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-93
  - TC-FA-COA-94
  - TC-FA-COA-95
coverage:
  web: automated
---

# Audit Log: Edit Account Code, Activate Deactivate, dan Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Akun Pre-setup sekali pakai milik spec ini (kunci fixture `Fixture.settingsChartOfAccounts.<kunci>` ditetapkan tim FE; seed ulang sebelum tiap run disediakan tim FE/BE):

  | Akun | Account Code | Account Name | Kondisi | Aksi |
  |---|---|---|---|---|
  | P62 | `5-6104` | Depreciation Expense – Edit Code Log | Active, Used By 0, Last Used in Journal kosong | Account Code diubah menjadi `5-6010` (TC-93) |
  | P64 | `4-7107` | Gain on Disposal – Log Toggle | Inactive, Used By 0, Last Used in Journal kosong | Activate lalu Deactivate (TC-94); status akhir kembali Inactive |
  | P55 | `CAP-8102` | Capitalization Clearing – Single Delete | Active, Used By 0, Last Used in Journal kosong, bukan nilai default company di Settings > Accounting > Preferences | Delete (TC-95) |

  Kode `5-6010` tidak dipakai akun lain pada client uji (perlu dikonfirmasi tim FE). Akun P62 (kini `5-6010`) dan P55 (terhapus) tidak dipulihkan oleh spec; seed ulang disediakan tim FE/BE (S-06).
- Kemampuan teknis: membaca jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS lewat BE sebelum aksi (8b.10, S-12); disediakan tim FE/BE. Baseline dicatat ulang sebelum aksi pemicu tiap TC.
- State yang diubah spec: akun P62 diubah, P64 diubah dua kali, P55 dihapus; audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-93: Edit Account Code tercatat di tiga surface

1. Catat jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS sebagai baseline TC-93
2. Ketik Search `5-6104`, tekan Enter
3. Klik row action `Edit` pada baris akun P62
4. Ubah Account Code menjadi `5-6010`
5. Klik `[Save]`
6. Tunggu aksi selesai (modal Edit Account tertutup)
7. Klik ikon Changelog di toolbar
8. Verifikasi jumlah entri Changelog bertambah satu dari baseline
9. Verifikasi entri teratas: Field Account Code, Old Value `5-6104`, New Value `5-6010`
10. Verifikasi kolom Account Code pada seluruh baris entri dari Save tersebut berisi `5-6010`
11. Tutup modal Changelog dengan ikon ✕
12. Buka System Log pada Detail User aktor
13. Verifikasi jumlah entri System Log bertambah satu dari baseline
14. Verifikasi Name pada entri teratas System Log adalah `5-6010`
15. Buka Activity Log FAMS
16. Verifikasi jumlah entri Activity Log bertambah satu dari baseline
17. Verifikasi Name pada entri teratas Activity Log adalah `5-6010`

### TC-FA-COA-94: Activate dan Deactivate dicatat sebagai Edit atas Status

18. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
19. Catat jumlah entri Changelog, System Log, dan Activity Log sebagai baseline TC-94
20. Ketik Search `4-7107`, tekan Enter
21. Klik switch Status baris akun P64
22. Klik `[Activate]` pada dialog "Activate Account"
23. Tunggu aksi selesai (dialog tertutup dan switch berubah)
24. Klik switch Status baris akun P64
25. Klik `[Deactivate]` pada dialog "Deactivate Account"
26. Tunggu aksi selesai (dialog tertutup dan switch berubah)
27. Klik ikon Changelog di toolbar
28. Verifikasi jumlah entri Changelog bertambah dua dari baseline
29. Verifikasi dua entri teratas (tanpa mengandalkan urutan di antaranya) dengan Action Edit, Field Status, dengan Old Value dan New Value `Inactive` ke `Active` dan `Active` ke `Inactive`
30. Verifikasi Modified By pada kedua entri adalah user aktor
31. Tutup modal Changelog dengan ikon ✕
32. Buka System Log pada Detail User aktor
33. Verifikasi jumlah entri System Log bertambah dua dari baseline
34. Verifikasi dua entri teratas System Log: Object `Chart of Accounts`, Name `4-7107`, Field Status, Old Value dan New Value `Inactive` ke `Active` dan `Active` ke `Inactive`
35. Buka Activity Log FAMS
36. Verifikasi jumlah entri Activity Log bertambah dua dari baseline
37. Verifikasi dua entri teratas Activity Log: Object `Chart of Accounts`, Name `4-7107`, Field Status, Old Value dan New Value yang sama, Modified By = user aktor

### TC-FA-COA-95: Delete tercatat satu baris dan Account Code tetap terbaca (langkah Delete menyalin TC-FA-COA-62)

38. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
39. Catat jumlah entri Changelog, System Log, dan Activity Log sebagai baseline TC-95
40. Ketik Search `CAP-8102`, tekan Enter
41. Klik row action `Delete` pada baris akun P55 sehingga dialog D-07 terbuka
42. Klik `[Delete]`
43. Verifikasi toast "Success, account has been deleted."
44. Verifikasi akun P55 hilang dari tabel
45. Klik ikon Changelog di toolbar
46. Verifikasi jumlah entri Changelog bertambah satu dari baseline
47. Verifikasi entri teratas: Action Delete, Account Code `CAP-8102`, Field Account Code, Old Value `CAP-8102`, New Value `—`
48. Tutup modal Changelog dengan ikon ✕
49. Buka Activity Log FAMS
50. Verifikasi jumlah entri Activity Log bertambah satu dari baseline
51. Verifikasi entri teratas Activity Log menampilkan Object `Chart of Accounts` dan Name `CAP-8102`
52. Buka System Log pada Detail User aktor
53. Verifikasi jumlah entri System Log bertambah satu dari baseline
54. Verifikasi satu baris System Log: Object `Chart of Accounts`, Name `CAP-8102`, Field Account Code, Old Value `CAP-8102`, New Value `—`

## Notes

- Alasan spec di atas sekitar 35 langkah (54 langkah): tiga blok memakai satu halaman dan satu kelas harness (pencatatan log tiga surface); sebagian besar langkah adalah blok baca-log berpola (buka surface, baca selisih, `Verifikasi` kolom) dan Search untuk membuka baris target (8b.12); tiap TC memakai akun dan baseline sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna. Aksi menghapus data berada di blok terakhir (S-10).
- Langkah Delete TC-95 (langkah 40 sampai 44) menyalin langkah TC-FA-COA-62 (S-04): dialog D-07 dibuka dari row action `Delete`, konfirmasi `[Delete]`, toast, dan akun hilang dari tabel.
- Cara baca entri baru (S-14): setelah selisih jumlah dari baseline dibuktikan, entri baru dibaca pada baris teratas urutan default Date Newest First. Pada TC-94 dua entri berada dalam menit yang sama; spec mengasersi himpunan dua entri teratas tanpa urutan di antaranya.
- Langkah penghubung (S-03): langkah 18 dan 38 (navigasi kembali ke modul asal setelah membaca log, S-14), langkah 2, 20, dan 40 (Search untuk menemukan baris target, R-16), langkah 6, 23, dan 26 (menunggu aksi selesai sebelum membuka log), langkah 11, 31, dan 48 (menutup modal).
- Asersi "tidak ada pencatatan/log" tidak ada di spec ini (S-05). Pengecekan isolasi log per aktor tidak dilakukan.
- Temuan untuk QA:
  - TC-93 Post Condition a (label akun di Asset Class, segmen Custom Asset ID, dan Preferences memakai Account Code terbaru; Asset ID yang sudah terbit tidak berubah) tidak memiliki langkah observasi di TC dan tidak diasersi.
  - TC-93 butir b ("seluruh baris L-02 dari Save tersebut") dibaca sebagai baris dari satu Save; karena hanya Account Code yang diubah, selisihnya satu baris (langkah 8 dan 10).
  - TC-94 tidak menyebut toast atau dialog; konfirmasi memakai `[Activate]` dan `[Deactivate]` seperti TC-46 dan TC-50.
  - TC-95 bergantung pada TC-62; langkah Delete disalin ke spec ini (S-04). Akun P62 dan P55 tidak dapat dipulihkan oleh spec.
  - TC-93, TC-94, dan TC-95 tidak menyebut jalur menu menuju System Log pada Detail User aktor dan Activity Log FAMS; spec mengikuti penamaan TC.
