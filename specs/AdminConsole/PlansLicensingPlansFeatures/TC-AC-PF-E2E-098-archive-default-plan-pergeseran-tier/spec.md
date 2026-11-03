---
id: TC-AC-PF-E2E-098-archive-default-plan-pergeseran-tier
title: "Archive Default Plan: Pergeseran Tier saat Archive Plan Free dan Paid Tengah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-241
  - TC-AC-PF-242
coverage:
  web: automated
---

# Archive Default Plan: Pergeseran Tier saat Archive Plan Free dan Paid Tengah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan Y (Pre-setup #37): default FAMS tanpa subscription Starter (Free), Growth, Professional, Enterprise (Paid tier 1, 2, 3). Data Dinamis: default plan `Paid Pengganti {runId}-098` (FAMS, Paid) dibuat di TC-AC-PF-242 dan dibuang oleh pemulihan Dataset Plan Y. Field wajib lain form Create Default Plan diisi nilai valid apa pun yang tidak diasersi (nilainya tidak disebut TC). Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk pemulihan Dataset Plan Y.
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan Y) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: Last Modified plan yang diarsipkan berubah; entri Archive dan Create bertambah di Changelog Default. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-241: Archive default plan Free tidak menggeser plan Paid

1. Buka tab Default sub-tab Active pada Plans List
2. Buka Overlay Row Action `Starter`, lalu klik `Archive`
3. Klik `[Archive]`
4. Verifikasi Toast sukses: "Success, plan has been archived."
5. Verifikasi Urutan Default Active FAMS tetap `Growth`, `Professional`, `Enterprise`
6. Klik sub-tab Archive
7. Verifikasi `Starter` ada di Default > Archive
8. Klik sub-tab Active
9. Klik `+ Default Plan`
10. Pilih Product `FAMS`
11. Verifikasi Radio Pricing Type menawarkan `Free`
12. Verifikasi Radio Pricing Type tidak menawarkan `Paid`
13. Klik segmen Breadcrumb `Plans & Features` pada form Create Default Plan
14. Verifikasi Dialog `Unsaved Changes` tampil
15. Klik `[Leave]`
16. Pulihkan Dataset Plan Y ke keadaan awal lewat Fixture BE

### TC-AC-PF-242: Archive default plan Paid di tengah menggeser Paid bertier lebih tinggi

17. Muat ulang halaman Plans & Features, lalu buka tab Default sub-tab Active
18. Buka Overlay Row Action `Growth`, lalu klik `Archive`
19. Klik `[Archive]`
20. Verifikasi Toast sukses: "Success, plan has been archived."
21. Verifikasi Urutan Default Active FAMS: `Starter`, `Professional`, `Enterprise`
22. Klik sub-tab Archive
23. Verifikasi `Growth` ada di Default > Archive
24. Klik sub-tab Active
25. Klik `+ Default Plan`
26. Pilih Product `FAMS`
27. Pilih Pricing Type `Paid`
28. Verifikasi Helper text "This will be paid tier 3 of 3 (rank 3)."
29. Isi Plan Name `Paid Pengganti {runId}-098`
30. Klik `[Submit]`
31. Klik breadcrumb sub-tab `Active`
32. Verifikasi Urutan Default Active FAMS setelah Create: `Starter`, `Professional`, `Enterprise`, `Paid Pengganti {runId}-098` (tanpa bentrok tier)

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, klik breadcrumb sub-tab `Active` dari Plan Detail yang terbuka sesudah Create (langkah 31), berpindah antara sub-tab Archive dan Active, memulihkan Dataset Plan Y lewat Fixture BE dan memuat ulang halaman antar blok TC.
- Menutup form Create Default Plan di akhir TC-AC-PF-241 memakai klik segmen Breadcrumb `Plans & Features`, `Verifikasi` dialog `Unsaved Changes`, dan `[Leave]` (S-08); `Verifikasi` dialog itu tidak dicatat lagi sebagai butir Notes (S-03).
- Temuan untuk QA: TC-AC-PF-241 tidak menyatakan apakah form Create Default Plan dianggap dirty setelah hanya memilih Product; spec mengasumsikan dialog `Unsaved Changes` tampil (S-08, tanpa langkah bersyarat).
- Temuan untuk QA: TC-AC-PF-242 tidak menyebut isian field wajib selain Plan Name pada Create Default Plan dan nama plan tidak ada di tabel Data Dinamis; spec memakai nama bersuffix dan field wajib bernilai valid yang tidak diasersi.
- Temuan untuk QA: TC-AC-PF-242 tidak menyebut toast sukses Create; spec hanya mengasersi urutan list seperti Expected butir d.
