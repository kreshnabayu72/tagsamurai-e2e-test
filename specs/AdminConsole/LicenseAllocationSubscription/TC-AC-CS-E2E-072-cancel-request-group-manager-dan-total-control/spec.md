---
id: TC-AC-CS-E2E-072-cancel-request-group-manager-dan-total-control
title: "Cancel Request: Group Manager dan Total Control"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-271
  - TC-AC-CS-274
  - TC-AC-CS-555
  - TC-AC-CS-624
  - TC-AC-CS-278
  - TC-AC-CS-536
coverage:
  web: automated
---

# Cancel Request: Group Manager dan Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Group Manager scope Group Jawa Distributor PT Maju Bersama, Dewi Anggraini (Pre-setup #5), `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_GM_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Total Control Distributor PT Maju Bersama, Eko Saputra (Pre-setup #9), `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_DIST_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Total Control Partner CV Karya Mandiri, Lestari Wulandari (Pre-setup #11), `totalControlPartnerSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before` lewat sesi API aktor requester, dihapus di hook `after`; Subscription ID dibaca lewat API seeding dan dirujuk di langkah sebagai nilai terbaca):
  - Client `Percetakan Mega+{runId}-072` (dalam scope group `Jawa` Group Manager) dengan term `{idPercetakan}` FAMS Professional Pending (15/09/26 sampai 14/09/27, Plan Owner PT Maju Bersama (Distributor)) milik requester `Dewi A` (padanan Pre-setup #57).
  - Client `Apotek Sehat Sentosa+{runId}-072` (binaan langsung PT Maju Bersama pada group `Jawa`) dengan term `{idApotek}` SIEM Pending (Start Date `15/09/26`, End Date `14/09/27`, Plan Owner PT Maju Bersama (Distributor)) milik requester `Fajar N` (toggle ON, sudah di-Approve) dengan Reserve $6,000.00 (padanan #90 dan #29).
  - Client `Toko Luar Jawa+{runId}-072` (binaan langsung PT Maju Bersama pada group `Sumatera`, di luar scope group `Jawa` Group Manager `Dewi Anggraini`) dengan term `{idTokoLuar}` FAMS Growth Pending (15/09/26 sampai 14/09/27, Plan Owner PT Maju Bersama (Distributor)) milik requester `Fajar N` (padanan #129).
  - Client `Client Tanpa Subscription+{runId}-072` (binaan langsung PT Maju Bersama pada group `Jawa`, tanpa term maupun trial; padanan #48) yang menerima term Pending dari langkah 30; term itu ikut dihapus bersama Client di hook `after`.
  - Client `Optik Cahaya+{runId}-072` (Plan Owner CV Karya Mandiri (Partner)) dengan term FAMS Growth `{idOptikCanceled}` Canceled tanpa otorisasi yang berlaku (tanggal -/-, dibatalkan Timeout Auto-Cancel, requester `Rina P`; padanan #56) dan term FAMS Growth `{idOptikWFA}` Waiting for Approval (tanggal -/-, milik requester `Rina P`; padanan #55).
- Data Pre-setup yang tidak ditulis spec: akun Total Control Partner `Lestari Wulandari` (#11).
- Data Dinamis: term, alokasi, Reserve, dan entri audit trail turunan Cancel Request ikut dihapus bersama Client seed di hook `after`; satu-satunya state global adalah jam (fixture waktu), dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu (jam server dan jam browser absolut, tanggal acuan `19/08/26`; diatur di hook `before`, dipulihkan di hook `after`) supaya tanggal `15/09/26` dan `14/09/27` konsisten; membaca jumlah notifikasi requester (`Fajar N`, `Dewi A`) dan approver pool; membaca Reserve term dan Reserve tiap alokasi (Wallet).

## Test Steps

### TC-AC-CS-271 dan TC-AC-CS-274: Dialog Cancel Request Group Manager pada term Pending dan pembatalan tanpa notifikasi

1. Ketik Search `Apotek Sehat Sentosa+{runId}-072`, tekan Enter, lalu catat jumlah notifikasi requester `Fajar N` dan approver pool sebagai baseline
2. Klik ikon `⋯` pada baris `{idApotek}` lalu pilih `Cancel Request`
3. Verifikasi Body memuat "This will cancel this request. Are you sure you want to cancel it?"
4. Verifikasi kalimat "You can resubmit it later if needed." tidak ada karena aktor bukan requester original
5. Klik `[Cancel Request]`
6. Verifikasi toast sukses "Success, your request has been canceled."
7. Klik tab `History`
8. Verifikasi term berstatus Canceled
9. Verifikasi Reserve term dan Reserve tiap alokasi (bila ada) dilepas penuh
10. Verifikasi tidak ada notifikasi baru ke requester maupun approver (jumlah sama dengan baseline)

### TC-AC-CS-536: Group Manager tidak dapat Cancel Request term Pending di luar scope group

11. Klik tab `Current`
12. Ganti isi kotak search dengan `Percetakan Mega+{runId}-072`, tekan Enter
13. Verifikasi term `{idPercetakan}` tampil di tab `Current` (pembanding in-scope sebelum empty state)
14. Ganti isi kotak search dengan `Toko Luar Jawa+{runId}-072`, tekan Enter
15. Verifikasi empty state "No results found" menunjukkan term Pending `{idTokoLuar}` tidak tampil bagi Group Manager (di luar scope READ) sehingga Cancel Request tidak dapat diakses lewat UI

### TC-AC-CS-555: Cancel Request term Pending oleh Total Control dan oleh requester

16. Ganti akun: Logout lalu login sebagai Total Control Distributor (`Eko Saputra`)
17. Buka menu Allocation > Client Subscription
18. Ketik Search `Percetakan Mega+{runId}-072`, tekan Enter, lalu catat jumlah notifikasi requester `Dewi A` dan approver pool sebagai baseline
19. Sebagai Total Control (bukan requester), klik ikon `⋯` pada baris `{idPercetakan}` lalu pilih `Cancel Request`
20. Verifikasi dialog memuat "This will cancel this request."
21. Verifikasi dialog tidak memuat kalimat "You can resubmit it later if needed."
22. Klik `[Cancel Request]`
23. Verifikasi toast sukses "Success, your request has been canceled."
24. Klik tab `History`
25. Ganti isi kotak search dengan `{idPercetakan}`, tekan Enter
26. Verifikasi term `{idPercetakan}` berstatus Canceled
27. Verifikasi Reserve term dan Reserve tiap alokasi dilepas penuh
28. Klik tab `Current`
29. Klik `[+ Subscription]`, pilih Client `Client Tanpa Subscription+{runId}-072`, Product `SAMS`, Plan `Growth`, isi Duration `1`, Start Date `15/09/26` lalu klik `[Submit]`
30. Tunggu aksi selesai (modal tertutup)
31. Ganti isi kotak search dengan `Client Tanpa Subscription+{runId}-072`, tekan Enter, lalu klik ikon `⋯` pada term Pending baru dan pilih `Cancel Request`
32. Verifikasi dialog memuat kalimat "You can resubmit it later if needed." karena aktor requester original
33. Klik `[Cancel Request]`
34. Verifikasi toast sukses "Success, your request has been canceled."
35. Klik tab `History`
36. Ganti isi kotak search dengan `Client Tanpa Subscription+{runId}-072`, tekan Enter
37. Verifikasi term Pending baru berstatus Canceled
38. Verifikasi Reserve term dan Reserve tiap alokasi dilepas penuh
39. Verifikasi tidak ada notifikasi baru ke requester maupun approver (jumlah sama dengan baseline)

### TC-AC-CS-624: Baris Canceled dengan otorisasi yang berlaku saat dibatalkan menampilkan tanggal, bukan strip

40. Ganti akun: Logout lalu login sebagai Total Control Principal (`Hendra Wijaya`)
41. Buka menu Allocation > Client Subscription
42. Klik tab `History`
43. Ketik Search `{idApotek}`, tekan Enter
44. Verifikasi baris `{idApotek}` menampilkan Start Date `15/09/26` dan End Date `14/09/27` karena otorisasi term masih berlaku saat dibatalkan
45. Ganti isi kotak search dengan `{idOptikCanceled}`, tekan Enter
46. Verifikasi baris `{idOptikCanceled}` menampilkan "—" pada Start Date dan End Date karena dibatalkan tanpa otorisasi yang berlaku

### TC-AC-CS-278: Cancel Request Hidden bagi aktor bukan requester pada Waiting for Approval

47. Ganti akun: Logout lalu login sebagai Total Control Partner (`Lestari Wulandari`)
48. Buka menu Allocation > Client Subscription
49. Ketik Search `Optik Cahaya+{runId}-072`, tekan Enter, lalu klik ikon `⋯` pada baris `{idOptikWFA}`
50. Verifikasi menu memuat Detail dan Subscription Log
51. Verifikasi menu tidak memuat Cancel Request dan Edit

## Notes

- TC-AC-CS-271 dan TC-AC-CS-274 memakai aksi yang sama (Group Manager membuka dialog Cancel Request pada term Pending `{idApotek}` milik requester lain dalam scope, lalu mengonfirmasi); satu alur memenuhi Expected kedua TC dan keduanya tercatat di `sourceTc`.
- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-536 (Group Manager) dikelompokkan dengan TC-AC-CS-271 dan TC-AC-CS-274 sebelum ganti akun; TC-AC-CS-624 memakai hasil TC-AC-CS-274 (kolom Dependensi) di akun Principal sesudahnya.
- Anchor absence (bagian 8b butir 2): ketiadaan term di luar scope memakai empty state "No results found" setelah pembanding in-scope (term `{idPercetakan}` tampil di tab `Current`) pada surface yang sama; ketiadaan Cancel Request pada menu didahului Verifikasi item Detail dan Subscription Log tampil pada menu yang sama.
- Anchor absence TC-AC-CS-555: ketiadaan kalimat "You can resubmit it later if needed." didahului Verifikasi dialog memuat "This will cancel this request." pada dialog yang sama.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); pindah tab `History` dan `Current` beserta Search verifikasi status Canceled; `Buka menu Allocation > Client Subscription` setelah tiap ganti akun (S-14); `Tunggu aksi selesai` sesudah `[Submit]` pembuatan term sebelum Search; `Klik tab Current` dan Search pembanding sebelum empty state; ganti akun eksplisit (S-07).
- Alasan melewati sekitar 35 langkah (51 langkah): semua blok satu topik (Cancel Request oleh Group Manager dan Total Control) tanpa kelas harness lain dan berdiri sendiri.
- Temuan untuk QA: (1) TC-AC-CS-274 butir c (tidak ada notifikasi ke requester maupun approver) tidak menyebut cara pengamatan; spec memakai kemampuan baca notifikasi yang disediakan tim FE/BE. (2) TC-AC-CS-271 Precondition menyebut "Term Pending milik requester lain dalam scope group" tanpa ID; spec memakai term Apotek Sehat Sentosa seed (padanan Pre-setup #90). (3) TC-AC-CS-536 menyatakan Cancel Request "tidak dapat diakses lewat UI" sebagai akibat term tidak tampil; tidak ada langkah pengamatan terpisah. (4) TC-AC-CS-555 langkah 2 tidak menyebut toast sukses `[Submit]` pembuatan term Pending; spec tidak mengasersinya. (5) TC-AC-CS-278 butir b (menu hanya memuat Detail dan Subscription Log) dan butir a diasersi sebagai satu pemeriksaan menu.
