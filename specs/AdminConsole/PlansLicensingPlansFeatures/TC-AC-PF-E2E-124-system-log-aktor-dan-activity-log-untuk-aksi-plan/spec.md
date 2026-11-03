---
id: TC-AC-PF-E2E-124-system-log-aktor-dan-activity-log-untuk-aksi-plan
title: "System Log Aktor dan Activity Log untuk Aksi Plan dan Global Settings serta Konsistensi Tiga Surface"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-532
  - TC-AC-PF-533
  - TC-AC-PF-534
  - TC-AC-PF-535
  - TC-AC-PF-536
  - TC-AC-PF-537
coverage:
  web: automated
---

# System Log Aktor dan Activity Log untuk Aksi Plan dan Global Settings serta Konsistensi Tiga Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data Pre-setup: Dataset Plan A / Dataset Plan C (Pre-setup #21 dan #23): custom plan `Growth Tier` v20 (Group count `25`; target aksi tulis TC-AC-PF-537); Dataset Plan P (Pre-setup #28): `Paket Push` v3 dengan `PT Push Dua` Active v2 eligible (target Push Update TC-AC-PF-533 dan TC-AC-PF-536); Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini). General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Data Dinamis milik spec (bersuffix per run): custom plan `Paket Log Create {runId}-124` (TC-AC-PF-532), `Paket Log Aksi {runId}-124` (TC-AC-PF-533; dipakai Create, Edit, Archive, dan Delete), dan `Paket Log Aktivitas {runId}-124` (TC-AC-PF-535). Plan buatan spec dibersihkan di hook `after` lewat Fixture BE.
- Pemicu precondition TC ("aktor baru menjalankan aksi") dijalankan lewat sesi API aktor yang sama dengan sesi UI; sesi API tidak dihitung sebagai sesi web (lihat `suite.md`).
- State global: suite serial (`parallel: false`). Pemulihan `Growth Tier` v20, Dataset Plan P, dan Global FAMS Settings (`5` dan `2`) dijamin Fixture BE (idempoten, disediakan tim FE/BE): dijalankan di hook `before` dan `after` serta sebagai langkah penghubung (langkah 13, 17, 33, dan 48). Efek yang tersisa: entri Changelog, System Log, dan Activity Log bertambah dan bersifat permanen (tidak dapat dihapus lewat UI); entri Changelog dikembalikan lewat Fixture BE (Pre-setup Dinamis #4).
- Baseline: jumlah entri Changelog tab Custom, System Log aktor, dan Activity Log dicatat pada langkah 35 lewat kemampuan baca; baseline entri Activity Log untuk TC-AC-PF-536 (Push Update `PT Push Dua` dan Edit `Max custom fields per asset name`) dicatat pada langkah 26 sebelum pemicu langkah 27 (audit trail permanen; asersi memakai selisih terhadap baseline, bukan entri lama; S-12, bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor untuk memicu aksi plan dan Save Global FAMS Settings; kemampuan baca jumlah entri Changelog Custom, System Log aktor, dan Activity Log; Fixture BE untuk pemulihan Dataset.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-532: System Log aktor untuk Create plan

1. Buat custom plan `Paket Log Create {runId}-124` (Product FAMS, Template `Growth`) lewat sesi API aktor hingga entri System Log tersimpan
2. Buka menu Global Settings > User
3. Ketik Search `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net`, tekan Enter
4. Buka Detail User `Andi Wijaya`, lalu klik Tab System Log
5. Verifikasi Entri teratas: Action `Create`, Object `Plans & Features`, Name `Paket Log Create {runId}-124`, Field `Plan Name`, Old Value `—`, New Value `Paket Log Create {runId}-124`
6. Verifikasi Tabel System Log tidak memiliki kolom Modified By

### TC-AC-PF-533: System Log aktor untuk Edit, Archive, Delete, dan Push Update

7. Buat `Paket Log Aksi {runId}-124`, ubah Group count `3` menjadi `25`, Archive, lalu Delete, kemudian Push Update `PT Push Dua` pada `Paket Push` (Dataset Plan P), semuanya lewat sesi API aktor hingga entri System Log tersimpan
8. Muat ulang halaman, lalu klik Tab System Log
9. Verifikasi Entri teratas Push Update (aksi terakhir pada langkah 7): Object `Plans & Features`, Name `PT Push Dua` (nama Client, bukan nama plan), Field `Plan Version`
10. Verifikasi Entri Delete: Object `Plans & Features`, Name `Paket Log Aksi {runId}-124`, Field `Plan Name`, Old Value `Paket Log Aksi {runId}-124`, New Value `—`
11. Verifikasi Entri Archive: Object `Plans & Features`, Name `Paket Log Aksi {runId}-124`, Field `Status`, Old Value `Active`, New Value `Archived`
12. Verifikasi Entri Edit: Object `Plans & Features`, Name `Paket Log Aksi {runId}-124`, Field `Group count`
13. Pulihkan Dataset Plan P ke keadaan awal lewat Fixture BE

### TC-AC-PF-534: System Log aktor untuk Save Global FAMS Settings

14. Simpan Global FAMS Settings `Max custom fields per asset name` dari `5` menjadi `8` lewat sesi API aktor hingga entri System Log tersimpan
15. Muat ulang halaman, lalu klik Tab System Log
16. Verifikasi Entri teratas: Action `Edit`, Object `Global FAMS Settings`, Name `—`, Field `Max custom fields per asset name`, Old Value `5`, New Value `8`
17. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE

### TC-AC-PF-535: Activity Log Admin Console untuk aksi plan

18. Buat `Paket Log Aktivitas {runId}-124`, ubah Group count `3` menjadi `25`, Archive, lalu Delete, semuanya lewat sesi API aktor hingga entri Activity Log tersimpan
19. Buka Admin Console > Activity Log
20. Filter Object `Plans & Features`
21. Verifikasi Entri Delete: Object `Plans & Features`, Name `Paket Log Aktivitas {runId}-124`, Action `Delete`, Field `Plan Name`, Old Value `Paket Log Aktivitas {runId}-124`, New Value `—`, Modified By `Andi W`
22. Verifikasi Entri Archive: Object `Plans & Features`, Name `Paket Log Aktivitas {runId}-124`, Action `Archive`, Field `Status`, Old Value `Active`, New Value `Archived`, Modified By `Andi W`
23. Verifikasi Entri Edit: Object `Plans & Features`, Name `Paket Log Aktivitas {runId}-124`, Action `Edit`, Field `Group count`, Old Value `3`, New Value `25`, Modified By `Andi W`
24. Verifikasi Entri Create: Object `Plans & Features`, Name `Paket Log Aktivitas {runId}-124`, Action `Create`, Field `Plan Name`, Old Value `—`, New Value `Paket Log Aktivitas {runId}-124`, Modified By `Andi W`

### TC-AC-PF-536: Activity Log untuk Push Update dan Global Settings

25. Pulihkan Dataset Plan P ke keadaan awal lewat Fixture BE
26. Catat jumlah entri Activity Log dengan Action `Push Update` untuk Name `PT Push Dua` dan jumlah entri Activity Log dengan Action `Edit` untuk Field `Max custom fields per asset name` sebagai baseline (kemampuan baca)
27. Push Update `PT Push Dua` pada `Paket Push`, lalu simpan Global FAMS Settings `Max custom fields per asset name` dari `5` menjadi `8`, semuanya lewat sesi API aktor hingga entri Activity Log tersimpan
28. Muat ulang halaman Activity Log
29. Verifikasi Jumlah entri Activity Log Action `Push Update` untuk Name `PT Push Dua` bertambah tepat satu dari baseline langkah 26
30. Verifikasi Entri Push Update: Object `Plans & Features`, Name `PT Push Dua`, Action `Push Update`, Field `Plan Version`, Old Value `v2`, New Value `v3`
31. Verifikasi Jumlah entri Activity Log Action `Edit` untuk Field `Max custom fields per asset name` bertambah tepat satu dari baseline langkah 26
32. Verifikasi Entri Global Settings: Object `Global FAMS Settings`, Name `—`, Action `Edit`, Field `Max custom fields per asset name`
33. Pulihkan Dataset Plan P dan Global FAMS Settings (`5` dan `2`) lewat Fixture BE

### TC-AC-PF-537: Satu aksi menghasilkan satu record konsisten di tiga surface

34. Buka menu Plans & Licensing > Plans & Features, lalu klik tab `Custom` sub-tab `Active`
35. Catat jumlah entri Changelog tab Custom, System Log aktor, dan Activity Log sebagai baseline
36. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
37. Ubah Group count `25` menjadi `3`
38. Klik `[Save]`
39. Tunggu aksi selesai (Plan Detail `Growth Tier` terbuka)
40. Kembali ke Plans List tab Custom sub-tab Active
41. Klik ikon Changelog pada toolbar tab Custom
42. Verifikasi Entri baru di Changelog tab Custom: Field `Group count`, Old Value `25`, New Value `3`, dan jumlah entri bertambah tepat satu dari baseline langkah 35
43. Tutup modal Changelog
44. Buka menu Global Settings > User, cari `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net`, buka Detail User `Andi Wijaya`, lalu klik Tab System Log
45. Verifikasi Entri baru di System Log aktor: Field `Group count`, Old Value `25`, New Value `3`, dan jumlah entri bertambah tepat satu dari baseline langkah 35
46. Buka Admin Console > Activity Log
47. Verifikasi Entri baru di Activity Log: Field `Group count`, Old Value `25`, New Value `3`, dan jumlah entri bertambah tepat satu dari baseline langkah 35
48. Pulihkan Dataset Pre-setup (`Growth Tier` v20) lewat Fixture BE

## Notes

- Langkah penghubung (S-03): navigasi menu dan Search untuk menemukan user target (R-16; langkah 2, 3, 44), muat ulang halaman supaya entri baru terbaca, filter Object `Plans & Features` pada Activity Log, "Tunggu aksi selesai" sebelum pindah surface (bagian 8b butir 8), kembali ke Plans List, tutup modal Changelog, pemulihan Dataset lewat Fixture BE, dan pencatatan baseline (langkah 26 dan 35). Pemicu precondition TC lewat sesi API aktor ditulis "... hingga ... tersimpan" (R-20).
- Entri yang diamati adalah entri terbaru hasil pemicu di langkah sebelumnya; urutan pemicu pada langkah 7 (Archive, Delete, lalu Push Update) membuat empat entri teratas System Log aktor berurutan Push Update, Delete, Archive, Edit (S-14).
- Pembagian TC lintas spec: TC-AC-PF-538 (tidak ada entri log untuk aksi ditolak) ada di spec 125.
- Alasan melewati sekitar 35 langkah (48 langkah): keenam TC membaca surface log yang sama (System Log aktor dan Activity Log) untuk aksi plan dan Global Settings, dalam satu kelas harness (fungsional). Langkah baca-log (buka surface, filter atau Search, `Verifikasi` kolom log: langkah 2 sampai 6, 8 sampai 12, 15 sampai 16, 19 sampai 24, 28 sampai 32, 41 sampai 47) mengikuti pola yang tidak dihitung pada ambang menurut bagian 3 prinsip 13; tanpa blok itu spec ini 18 langkah.
- Temuan untuk QA:
  - TC-AC-PF-533 precondition meminta Edit, Archive, Delete, dan Push Update pada Dataset Plan P, tetapi plan di Dataset Plan P semuanya memiliki client sehingga Archive dan Delete diblokir guard. Spec memakai plan milik spec `Paket Log Aksi {runId}-124` untuk Edit, Archive, dan Delete, dan Dataset Plan P hanya untuk Push Update (S-06).
  - TC-AC-PF-532 sampai TC-AC-PF-536 tidak menyatakan cara aksi pemicu dijalankan (UI atau API); spec memakai sesi API aktor (precondition, bukan objek uji) dan mengasersi hasilnya di UI.
  - TC-AC-PF-535 tidak menyebut Old Value dan New Value tiap aksi secara rinci (hanya "sesuai tabel 8.3"); spec memakai nilai dari TC-AC-PF-520, TC-AC-PF-522, dan TC-AC-PF-525.
  - TC-AC-PF-534 tidak menyebut Name entri Global FAMS Settings selain `—`; ditulis sesuai TC.
  - Post Condition "Entri System Log sisi aktor" dan "Entri Activity Log" pada TC-AC-PF-532 sampai TC-AC-PF-536 tanpa langkah observasi tambahan tidak diasersi di luar Expected (S-01).
