---
id: TC-GS-POS-E2E-054-state-tenant-write-lockdown-dan-plan
title: "State Tenant: Client Suspended Menolak Create, Edit, dan Delete Position serta Perilaku Identik Lintas Plan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-268
  - TC-GS-POS-272
  - TC-GS-POS-273
  - TC-GS-POS-274
coverage:
  web: automated
---

# State Tenant: Client Suspended Menolak Create, Edit, dan Delete Position serta Perilaku Identik Lintas Plan

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun aktor (semua Total Control; email akun Client tidak tertulis di tabel Pre-setup TC, lihat Temuan untuk QA; password tidak ditulis di spec atau fixture):
  - Total Control `Client Suspended` (Pre-setup 20), kredensial `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD`. Aktor pertama, login di hook `before`.
  - Total Control Client plan Starter (Pre-setup 23), `Spectra.env.GS_PLANSTARTER_TC_PASSWORD`.
  - Total Control Client plan Growth (Pre-setup 24), `Spectra.env.GS_PLANGROWTH_TC_PASSWORD`.
  - Total Control Client plan Professional (Pre-setup 25), `Spectra.env.GS_PLANPRO_TC_PASSWORD`.
  - Total Control Client plan Enterprise (Pre-setup 26), `Spectra.env.GS_PLANENT_TC_PASSWORD`.
  - Hook `after` mengembalikan sesi ke akun Total Control default suite (`superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Data Pre-setup: Position `Store Manager` milik entitas `Client Suspended` (Pre-setup 20). Penulisan ke entitas ini ditolak (entitas Suspended): `Store Manager` hanya dibaca dan dijadikan target aksi yang ditolak, tidak diubah atau dihapus, sehingga Last Updated-nya tidak berubah (pengecualian S-06); tidak bersuffix.
- Data Dinamis (dibuat dan dihapus oleh langkah spec, bersuffix per run): pada Client Suspended nama yang ditolak disimpan `Retail Supervisor {runId}-054` (TC-GS-POS-272) dan `Store Director {runId}-054` (TC-GS-POS-273), tidak pernah tersimpan; pada tiap Client plan `Plan Tester {runId}-054` (dibuat, lalu diganti nama menjadi `Plan Tester Lead {runId}-054`, lalu dihapus).
- Entitas keempat plan tidak melewati Master Data Count Limit sehingga Create tidak menampilkan dialog `Limit Reached`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` untuk akun aktor spec ini (kelima akun Client) dan hook `after` memulihkannya; lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API `Plan Tester {runId}-054` dan `Plan Tester Lead {runId}-054` pada keempat Client plan bila masih ada; kembalikan sesi ke akun default suite. Tidak ada cleanup pada Client Suspended karena penulisan ditolak.
- Hook `beforeEach`: membuka Global Settings > User > Position pada akun aktor pertama (Client Suspended); langkah buka halaman di `## Test Steps` hanya ada sesudah ganti akun.
- Kemampuan teknis: ganti akun (logout lalu login); dialog `beforeunload` ditangani otomatis saat memuat ulang halaman (langkah 6, 14, dan 21).
- State global: tidak ada yang diubah selain sesi akun (dipulihkan seperti di atas). Status suspended dan plan tiap Client adalah kondisi tetap environment.

## Test Steps

### TC-GS-POS-272: Entitas suspended, Create ditolak

1. Klik `[+ Position]`
2. Ketik `Retail Supervisor {runId}-054` pada field Position Name
3. Klik `[Submit]`
4. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
5. Verifikasi tidak ada redirect (halaman tetap Global Settings > User > Position)
6. Muat ulang halaman Position (dialog `beforeunload` ditangani)
7. Verifikasi tabel masih menampilkan baris `Store Manager`
8. Verifikasi tabel tidak menampilkan baris `Retail Supervisor {runId}-054`

### TC-GS-POS-273: Entitas suspended, Edit ditolak

9. Klik `⋯` pada baris `Store Manager`, pilih `Edit`
10. Ganti isi field Position Name menjadi `Store Director {runId}-054`
11. Klik `[Save]`
12. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
13. Verifikasi tidak ada redirect (halaman tetap Global Settings > User > Position)
14. Muat ulang halaman Position (dialog `beforeunload` ditangani)
15. Verifikasi tabel masih menampilkan baris `Store Manager`
16. Verifikasi tabel tidak menampilkan baris `Store Director {runId}-054`

### TC-GS-POS-274: Entitas suspended, Delete ditolak

17. Klik `⋯` pada baris `Store Manager`, pilih `Delete`
18. Klik `[Delete]` pada Dialog Delete Position
19. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
20. Verifikasi tidak ada redirect (halaman tetap Global Settings > User > Position)
21. Muat ulang halaman Position (dialog `beforeunload` ditangani)
22. Verifikasi tabel masih menampilkan baris `Store Manager`

### TC-GS-POS-268: Tidak ada plan gating, perilaku identik di semua plan (plan Starter)

23. Ganti akun: logout, lalu login sebagai Total Control Client plan Starter
24. Buka Global Settings > User > Position
25. Klik `[+ Position]`
26. Ketik `Plan Tester {runId}-054` pada field Position Name
27. Klik `[Submit]`
28. Verifikasi toast sukses: "Success, position has been created."
29. Ketik `{runId}-054` pada Search tabel lalu tekan Enter
30. Klik `⋯` pada baris `Plan Tester {runId}-054`, pilih `Edit`
31. Ganti isi field Position Name menjadi `Plan Tester Lead {runId}-054`
32. Klik `[Save]`
33. Verifikasi toast sukses: "Success, position has been updated."
34. Klik `⋯` pada baris `Plan Tester Lead {runId}-054`, pilih `Delete`
35. Klik `[Delete]` pada Dialog Delete Position
36. Verifikasi toast sukses: "Success, position has been deleted."
37. Verifikasi tidak ada upsell atau gating selama Create, Edit, dan Delete
38. Verifikasi tidak ada pembatasan selain Master Data Count Limit (tidak ada dialog `Limit Reached` dan tidak ada pesan pembatasan lain)

### TC-GS-POS-268: Tidak ada plan gating, perilaku identik di semua plan (plan Growth)

39. Ganti akun: logout, lalu login sebagai Total Control Client plan Growth
40. Buka Global Settings > User > Position
41. Klik `[+ Position]`
42. Ketik `Plan Tester {runId}-054` pada field Position Name
43. Klik `[Submit]`
44. Verifikasi toast sukses: "Success, position has been created."
45. Ketik `{runId}-054` pada Search tabel lalu tekan Enter
46. Klik `⋯` pada baris `Plan Tester {runId}-054`, pilih `Edit`
47. Ganti isi field Position Name menjadi `Plan Tester Lead {runId}-054`
48. Klik `[Save]`
49. Verifikasi toast sukses: "Success, position has been updated."
50. Klik `⋯` pada baris `Plan Tester Lead {runId}-054`, pilih `Delete`
51. Klik `[Delete]` pada Dialog Delete Position
52. Verifikasi toast sukses: "Success, position has been deleted."
53. Verifikasi tidak ada upsell atau gating selama Create, Edit, dan Delete
54. Verifikasi tidak ada pembatasan selain Master Data Count Limit (tidak ada dialog `Limit Reached` dan tidak ada pesan pembatasan lain)

### TC-GS-POS-268: Tidak ada plan gating, perilaku identik di semua plan (plan Professional)

55. Ganti akun: logout, lalu login sebagai Total Control Client plan Professional
56. Buka Global Settings > User > Position
57. Klik `[+ Position]`
58. Ketik `Plan Tester {runId}-054` pada field Position Name
59. Klik `[Submit]`
60. Verifikasi toast sukses: "Success, position has been created."
61. Ketik `{runId}-054` pada Search tabel lalu tekan Enter
62. Klik `⋯` pada baris `Plan Tester {runId}-054`, pilih `Edit`
63. Ganti isi field Position Name menjadi `Plan Tester Lead {runId}-054`
64. Klik `[Save]`
65. Verifikasi toast sukses: "Success, position has been updated."
66. Klik `⋯` pada baris `Plan Tester Lead {runId}-054`, pilih `Delete`
67. Klik `[Delete]` pada Dialog Delete Position
68. Verifikasi toast sukses: "Success, position has been deleted."
69. Verifikasi tidak ada upsell atau gating selama Create, Edit, dan Delete
70. Verifikasi tidak ada pembatasan selain Master Data Count Limit (tidak ada dialog `Limit Reached` dan tidak ada pesan pembatasan lain)

### TC-GS-POS-268: Tidak ada plan gating, perilaku identik di semua plan (plan Enterprise)

71. Ganti akun: logout, lalu login sebagai Total Control Client plan Enterprise
72. Buka Global Settings > User > Position
73. Klik `[+ Position]`
74. Ketik `Plan Tester {runId}-054` pada field Position Name
75. Klik `[Submit]`
76. Verifikasi toast sukses: "Success, position has been created."
77. Ketik `{runId}-054` pada Search tabel lalu tekan Enter
78. Klik `⋯` pada baris `Plan Tester {runId}-054`, pilih `Edit`
79. Ganti isi field Position Name menjadi `Plan Tester Lead {runId}-054`
80. Klik `[Save]`
81. Verifikasi toast sukses: "Success, position has been updated."
82. Klik `⋯` pada baris `Plan Tester Lead {runId}-054`, pilih `Delete`
83. Klik `[Delete]` pada Dialog Delete Position
84. Verifikasi toast sukses: "Success, position has been deleted."
85. Verifikasi tidak ada upsell atau gating selama Create, Edit, dan Delete
86. Verifikasi tidak ada pembatasan selain Master Data Count Limit (tidak ada dialog `Limit Reached` dan tidak ada pesan pembatasan lain)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Kelas harness: state tenant (write-lockdown Client Suspended dan perilaku lintas plan), bagian 3 prinsip 13h. Spec serial karena berganti akun dan entitas.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-GS-POS-268 dijalankan satu blok per plan (Starter, Growth, Professional, Enterprise) dengan langkah identik.
- Spec memuat 86 langkah (di atas smell sekitar 35 langkah). Alasan: seluruh blok satu kelas harness (state tenant), tiap blok berdiri sendiri pada akun dan entitasnya serta menyiapkan dan menghapus datanya sendiri, dan kegagalan satu blok tidak menghilangkan makna blok lain; 64 langkah berasal dari empat blok plan yang identik.
- Urutan: blok Client Suspended lebih dulu (penulisan ditolak, tidak ada data berubah), blok plan sesudahnya (membuat lalu menghapus datanya sendiri; aksi menghapus data di akhir tiap blok).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 14, dan 21 (memuat ulang halaman sehingga state form atau dialog setelah penolakan tidak berpengaruh dan data dibaca dari server); langkah 23, 39, 55, dan 71 (ganti akun eksplisit); langkah 29, 45, 61, dan 77 (Search `{runId}-054` supaya baris data spec ini mudah ditemukan; Search tidak dikosongkan karena akun diganti sesudahnya).
- Langkah 7 (`Verifikasi` baris `Store Manager` tampil) mendahului langkah 8 (baris `Retail Supervisor {runId}-054` tidak tampil) sebagai anchor pembanding bahwa tabel sudah termuat sesudah muat ulang; urutan ini menyimpang dari urutan butir b TC-GS-POS-272 ("data tidak berubah").
- Langkah 37 dan 38 (dan padanannya) membagi Expected TC-GS-POS-268 butir a ("tanpa upsell/gating/limit berbeda") dan butir b ("satu-satunya batas yang berlaku adalah Master Data Count Limit") menjadi `Verifikasi` tersendiri; butir b hanya teramati sebagai tidak adanya pembatasan lain.
- Temuan untuk QA:
  - TC-GS-POS-272, 273, dan 274 berjudul "suspended/expired", tetapi Precondition hanya `Client Suspended` (Pre-setup 20); tidak ada Pre-setup untuk `Client Expired`. Spec hanya menjalankan Client Suspended; varian Client Expired (`GS_CLIENTEXP_TC_PASSWORD`) membutuhkan keputusan user dan data Position untuk entitas itu.
  - Email akun Total Control Client Suspended dan keempat Client plan tidak tertulis di Pre-setup 20 dan 23 sampai 26; env var `GS_CLIENTSUSP_TC_PASSWORD`, `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, dan `GS_PLANENT_TC_PASSWORD` terdaftar di `spectra.config.ts` dan `.env.example`, sedangkan email akun perlu ditetapkan.
  - TC-GS-POS-272, 273, dan 274 tidak menyebut apakah form atau dialog tetap terbuka setelah toast error; spec memuat ulang halaman sebelum membaca data (langkah 6, 14, 21).
  - TC-GS-POS-268 menulis langkah "Create, Edit, Delete" di tiap entitas tanpa menyebut toast per aksi; spec memakai teks toast standar Position ("Success, position has been created.", "...updated.", "...deleted.").
  - Post Condition TC-GS-POS-272, 273, dan 274 ("Tidak ada entri Changelog") tidak punya langkah observasi di TC; tidak diasersi.
