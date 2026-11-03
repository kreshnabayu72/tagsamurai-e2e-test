---
id: TC-AC-PF-E2E-122-isi-entri-changelog-archive-delete-push-update
title: "Isi Entri Changelog: Archive, Delete, dan Push Update"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-525
  - TC-AC-PF-526
  - TC-AC-PF-527
  - TC-AC-PF-528
  - TC-AC-PF-530
coverage:
  web: automated
---

# Isi Entri Changelog: Archive, Delete, dan Push Update

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data Pre-setup (target aksi tulis): `Paket Tanpa Client` (Dataset Plan G, Pre-setup #27; custom plan Principal tanpa subscription), `Enterprise` (Dataset Plan Y, Pre-setup #37; default FAMS tanpa subscription), `Arsip Custom Satu` (Dataset Plan C, Pre-setup #23; custom archived tidak pernah dipakai), `Plan Arsip Lama` (Dataset Plan R, Pre-setup #30; default archived tidak pernah dipakai), dan `Paket Push` v3 dengan `PT Push Dua` Active v2 eligible (Dataset Plan P, Pre-setup #28). General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Aksi mengarsipkan, menghapus, dan mengubah versi client data Pre-setup. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- State global: suite serial (`parallel: false`). Pemulihan semua Dataset yang disentuh ke keadaan awal dijamin Fixture BE (idempoten, disediakan tim FE/BE): dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 9, 18, 27, 36, dan 48). Efek yang tersisa: Last Modified plan yang disentuh dan entri Changelog (permanen) yang dikembalikan lewat Fixture BE (Pre-setup Dinamis #4).
- Baseline: jumlah entri Changelog tab Custom atau tab Default dicatat sebelum aksi tiap TC lewat kemampuan baca (audit trail permanen; S-12, bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Default dan tab Custom; Fixture BE untuk pemulihan Dataset.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-525: Archive custom plan

1. Klik tab `Custom` sub-tab `Active`
2. Catat jumlah entri Changelog tab Custom sebagai baseline
3. Buka Overlay Row Action `Paket Tanpa Client`, lalu klik `Archive`
4. Klik `[Archive]` pada dialog
5. Tunggu aksi selesai (dialog tertutup)
6. Klik ikon Changelog pada toolbar tab Custom
7. Verifikasi Entri baru (jumlah entri bertambah tepat satu dari baseline langkah 2): Action `Archive`, Plan Name `Paket Tanpa Client`, Field `Status`, Old Value `Active`, New Value `Archived`
8. Tutup modal Changelog
9. Pulihkan `Paket Tanpa Client` (Dataset Plan G) ke keadaan awal lewat Fixture BE

### TC-AC-PF-526: Archive default plan

10. Klik tab `Default` sub-tab `Active`
11. Catat jumlah entri Changelog tab Default sebagai baseline
12. Buka Overlay Row Action `Enterprise`, lalu klik `Archive`
13. Klik `[Archive]` pada dialog
14. Tunggu aksi selesai (dialog tertutup)
15. Klik ikon Changelog pada toolbar tab Default
16. Verifikasi Entri baru (jumlah entri bertambah tepat satu dari baseline langkah 11): Action `Archive`, Plan Name `Enterprise`, Field `Status`, Old Value `Active`, New Value `Archived`
17. Tutup modal Changelog
18. Pulihkan Dataset Plan Y ke keadaan awal lewat Fixture BE

### TC-AC-PF-527: Delete custom plan

19. Klik tab `Custom` sub-tab `Archive`
20. Catat jumlah entri Changelog tab Custom sebagai baseline
21. Buka Overlay Row Action `Arsip Custom Satu`, lalu klik `Delete`
22. Klik `[Delete]` pada dialog
23. Tunggu aksi selesai (dialog tertutup)
24. Klik ikon Changelog pada toolbar tab Custom
25. Verifikasi Entri baru (jumlah entri bertambah tepat satu dari baseline langkah 20): Action `Delete`, Plan Name `Arsip Custom Satu`, Field `Plan Name`, Old Value `Arsip Custom Satu`, New Value `—`
26. Tutup modal Changelog
27. Pulihkan `Arsip Custom Satu` (Dataset Plan C) ke keadaan awal lewat Fixture BE

### TC-AC-PF-528: Delete default plan

28. Klik tab `Default` sub-tab `Archive`
29. Catat jumlah entri Changelog tab Default sebagai baseline
30. Buka Overlay Row Action `Plan Arsip Lama`, lalu klik `Delete`
31. Klik `[Delete]` pada dialog
32. Tunggu aksi selesai (dialog tertutup)
33. Klik ikon Changelog pada toolbar tab Default
34. Verifikasi Entri baru (jumlah entri bertambah tepat satu dari baseline langkah 29): Action `Delete`, Plan Name `Plan Arsip Lama`, Field `Plan Name`, Old Value `Plan Arsip Lama`, New Value `—`
35. Tutup modal Changelog
36. Pulihkan `Plan Arsip Lama` (Dataset Plan R) ke keadaan awal lewat Fixture BE

### TC-AC-PF-530: Push Update

37. Klik tab `Custom` sub-tab `Active`
38. Catat jumlah entri Changelog tab Custom sebagai baseline
39. Buka Plan Detail `Paket Push`
40. Klik Tab Assigned Clients
41. Buka Overlay Row Action `PT Push Dua`, lalu klik `Push Update`
42. Klik `[Push Update]` pada dialog
43. Tunggu aksi selesai (dialog tertutup)
44. Kembali ke Plans List tab Custom sub-tab Active
45. Klik ikon Changelog pada toolbar tab Custom
46. Verifikasi Entri baru (jumlah entri bertambah tepat satu dari baseline langkah 38): Action `Push Update`, Plan Name `PT Push Dua`, Field `Plan Version`, Old Value `v2`, New Value `v3`
47. Tutup modal Changelog
48. Pulihkan Dataset Plan P ke keadaan awal lewat Fixture BE

## Notes

- Langkah penghubung (S-03): buka tab dan sub-tab sebagai precondition TC, "Tunggu aksi selesai" sebelum pindah surface (bagian 8b butir 8), kembali ke Plans List, tutup modal Changelog, dan pemulihan Dataset lewat Fixture BE (langkah 9, 18, 27, 36, 48).
- Pembagian TC lintas spec: TC-AC-PF-520 sampai TC-AC-PF-524 ada di spec 121; TC-AC-PF-531 ada di spec 128; TC-AC-PF-529 ada di spec 123.
- Alasan melewati sekitar 35 langkah (48 langkah): kelima TC memakai satu pola (aksi pada plan, lalu baca Changelog), satu kelas harness (fungsional), dan data Pre-setup yang dipulihkan antar blok. Langkah baca-log tiap TC (buka Changelog, `Verifikasi` kolom log, tutup modal, serta kembali ke Plans List pada TC-AC-PF-530: langkah 6 sampai 8, 15 sampai 17, 24 sampai 26, 33 sampai 35, dan 44 sampai 47) mengikuti pola buka surface lalu Verifikasi yang tidak dihitung pada ambang menurut bagian 3 prinsip 13; tanpa blok itu spec ini 32 langkah.
- Temuan untuk QA:
  - Label tombol konfirmasi di TC ditulis "Confirm"; spec memakai label tombol dialog yang berlaku (`[Archive]`, `[Delete]`, `[Push Update]`) sesuai konvensi label tombol (bagian 7).
  - TC-AC-PF-525 sampai TC-AC-PF-530 menyebut entri "baru" tanpa menyatakan cara membedakan dari entri lama; spec memakai selisih jumlah entri terhadap baseline (S-12).
  - Post Condition "Satu entri ..." pada tiap TC diasersi lewat selisih jumlah entri terhadap baseline pada langkah `Verifikasi` yang sama; TC-AC-PF-530 Post Condition "Satu entri Push Update per eksekusi" diasersi dengan cara yang sama.
