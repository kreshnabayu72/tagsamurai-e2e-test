---
id: TC-AC-PF-E2E-111-archive-default-plan-tier-tertinggi-terendah-dan-last-modified-tergeser
title: "Archive Default Plan: Tier Tertinggi, Tier Terendah, dan Last Modified Plan yang Tergeser"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-243
  - TC-AC-PF-244
  - TC-AC-PF-245
coverage:
  web: automated
---

# Archive Default Plan: Tier Tertinggi, Tier Terendah, dan Last Modified Plan yang Tergeser

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan Y (Pre-setup #37): default FAMS tanpa subscription Starter (Free), Growth, Professional, Enterprise (Paid tier 1, 2, 3). Tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44). Jam server dan jam browser sinkron.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Default. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan Y) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: Last Modified plan yang diarsipkan berubah dan entri Archive bertambah di Changelog Default. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-243: Archive default plan Paid pada tier tertinggi

1. Muat ulang halaman Plans & Features, lalu buka tab Default sub-tab Active
2. Buka Overlay Row Action `Enterprise`, lalu klik `Archive`
3. Klik `[Archive]`
4. Verifikasi Urutan Default Active FAMS: `Starter`, `Growth`, `Professional`
5. Klik `+ Default Plan`
6. Pilih Product `FAMS`
7. Pilih Pricing Type `Paid`
8. Verifikasi Helper text "This will be paid tier 3 of 3 (rank 3)."
9. Klik segmen Breadcrumb `Plans & Features` pada form Create Default Plan
10. Verifikasi Dialog `Unsaved Changes` tampil
11. Klik `[Leave]`
12. Pulihkan Dataset Plan Y ke keadaan awal lewat Fixture BE

### TC-AC-PF-244: Archive default plan Paid pada tier terendah menggeser dua plan Paid

13. Muat ulang halaman Plans & Features, lalu buka tab Default sub-tab Active
14. Buka Overlay Row Action `Growth`, lalu klik `Archive`
15. Klik `[Archive]`
16. Buka Overlay Row Action `Professional`, lalu klik `Archive`
17. Klik `[Archive]`
18. Verifikasi Urutan Default Active FAMS: `Starter`, `Enterprise`
19. Klik `+ Default Plan`
20. Pilih Product `FAMS`
21. Pilih Pricing Type `Paid`
22. Verifikasi Helper text "This will be paid tier 2 of 3 (rank 2)."
23. Klik segmen Breadcrumb `Plans & Features` pada form Create Default Plan
24. Verifikasi Dialog `Unsaved Changes` tampil
25. Klik `[Leave]`
26. Pulihkan Dataset Plan Y ke keadaan awal lewat Fixture BE

### TC-AC-PF-245: Pergeseran tier akibat Archive tidak memperbarui Last Modified plan yang tergeser

27. Muat ulang halaman Plans & Features, lalu buka tab Default sub-tab Active
28. Catat Last Modified `Professional` dan `Enterprise` pada list
29. Catat jumlah entri Changelog tab Default sebagai baseline
30. Buka Overlay Row Action `Growth`, lalu klik `Archive`
31. Klik `[Archive]`
32. Verifikasi Last Modified `Professional` dan `Enterprise` sama dengan nilai yang dicatat pada langkah 28
33. Klik ikon Changelog pada toolbar tab Default
34. Verifikasi Modal Changelog tab Default tampil dengan entri sebelumnya (anchor)
35. Verifikasi Jumlah entri Changelog tab Default bertambah tepat satu dari baseline langkah 29 (tidak ada entri untuk `Professional` dan `Enterprise`)
36. Verifikasi Entri terbaru Changelog Default: Action `Archive`, `Growth`, Status `Active` menjadi `Archived`
37. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, memulihkan Dataset Plan Y lewat Fixture BE dan memuat ulang halaman antar blok TC, menutup modal Changelog.
- Menutup form Create Default Plan memakai klik segmen Breadcrumb `Plans & Features`, `Verifikasi` dialog `Unsaved Changes`, dan `[Leave]` (S-08).
- Ketiga blok berkelas fungsional, memulihkan Dataset Plan Y sendiri, dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah sedikit di atas 35 langkah karena tiap Expected punya `Verifikasi` sendiri (S-01) dan pemulihan antar blok.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-243 dan TC-AC-PF-244 tidak menyatakan apakah form Create Default Plan dirty setelah memilih Product dan Pricing Type; spec mengasumsikan dialog `Unsaved Changes` tampil (S-08).
- Temuan untuk QA: TC-AC-PF-245 Post Condition menyebut tidak ada entri log untuk plan yang tergeser; ditulis sebagai `Verifikasi` jumlah entri Changelog bertambah tepat satu dari baseline (Expected butir b TC memuatnya).
