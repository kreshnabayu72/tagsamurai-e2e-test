---
id: TC-AC-PF-E2E-126-efek-lintas-modul-dropdown-plan-subscription-versi
title: "Efek Lintas Modul ke Allocation: Dropdown Plan Subscription, Versi Grandfathering, Renewal, dan Push Update"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-542
  - TC-AC-PF-543
  - TC-AC-PF-544
  - TC-AC-PF-545
  - TC-AC-PF-546
coverage:
  web: automated
---

# Efek Lintas Modul ke Allocation: Dropdown Plan Subscription, Versi Grandfathering, Renewal, dan Push Update

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data Pre-setup (target aksi tulis atau dibaca): Dataset Plan Y (Pre-setup #37): default FAMS `Enterprise` tanpa subscription (TC-AC-PF-542); Dataset Plan A / Dataset Plan D (Pre-setup #21 dan #24): default `Growth` v5 dengan subscription existing `PT Sejahtera Abadi` v5 (TC-AC-PF-544); Dataset Plan P (Pre-setup #28): `Paket Turun` v3 dengan `PT Turun Satu` v1 yang push-nya diblokir (delta downgrade; TC-AC-PF-545) dan `Paket Push` dengan `PT Push Dua` Active v2 eligible (TC-AC-PF-546). General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Aksi mengarsipkan, mengubah versi, dan mengubah term data Pre-setup. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Data Dinamis milik spec (bersuffix per run): default plan `Supply Baru {runId}-126` (Product SAMS, Pricing Type Paid) dan custom plan `Paket Alokasi {runId}-126` (Product FAMS, Template `Growth`), dihapus di hook `after` lewat Fixture BE. Client `PT Baru Mulia` (TC-AC-PF-544) tidak ada di Tabel Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA); subscription barunya dihapus lewat Fixture BE pada langkah 46.
- State global: suite serial (`parallel: false`). Pemulihan semua Dataset yang disentuh ke keadaan awal dijamin Fixture BE (idempoten, disediakan tim FE/BE): dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 20, 35, 46, 54, dan 62). Efek yang tersisa: Last Modified plan yang disentuh dan entri Changelog (permanen) yang dikembalikan lewat Fixture BE (Pre-setup Dinamis #4).
- Kemampuan teknis (disediakan tim FE/BE): akses aktor ke modul Allocation > Client Subscription (`+ Subscription`, Renew dengan `Keep current plan`, List Subscriptions); Fixture BE untuk pemulihan Dataset dan penghapusan subscription buatan spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Dataset aktif per blok (default plan Dataset Plan Y dan Dataset Plan A / D menempati slot default FAMS yang sama dan tidak hidup berdampingan; Fixture BE berpindah dataset antar blok): TC-AC-PF-542 dan TC-AC-PF-543 memakai Dataset Plan Y (langkah 1 memindahkan ke Dataset Plan Y); TC-AC-PF-544 memakai Dataset Plan A dan Dataset Plan D (langkah 36 memindahkan ke keduanya, memuat `Growth` v5 dengan `PT Sejahtera Abadi`); TC-AC-PF-545 dan TC-AC-PF-546 memakai Dataset Plan P (custom plan tidak menempati slot default).
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-542: Plan di-archive tidak ditawarkan di dropdown Plan dan Template

1. Pindah ke Dataset Plan Y lewat Fixture BE
2. Klik tab `Default` sub-tab `Active`
3. Buka Overlay Row Action `Enterprise`, lalu klik `Archive`
4. Klik `[Archive]` pada dialog
5. Tunggu aksi selesai (dialog tertutup)
6. Buka Allocation > Client Subscription, lalu klik `+ Subscription`
7. Buka dropdown Plan
8. Verifikasi Dropdown Plan memuat opsi plan lain, misalnya `Growth` (anchor)
9. Verifikasi Dropdown Plan tidak memuat `Enterprise`
10. Tutup form `+ Subscription` tanpa menyimpan
11. Buka Plans & Licensing > Plans & Features, lalu klik tab `Custom` sub-tab `Active`
12. Klik `+ Custom Plan` pada toolbar
13. Pilih Product `FAMS`
14. Buka dropdown Template
15. Verifikasi Dropdown Template memuat opsi plan lain, misalnya `Growth` (anchor)
16. Verifikasi Dropdown Template tidak memuat `Enterprise`
17. Klik segmen Breadcrumb `Plans & Features` pada form Create Custom Plan
18. Verifikasi Dialog `Unsaved Changes` tampil
19. Klik `[Leave]`
20. Pulihkan Dataset Plan Y ke keadaan awal lewat Fixture BE

### TC-AC-PF-543: Plan baru langsung tersedia di dropdown Plan sesuai entitas pembuat

21. Klik tab `Default` sub-tab `Active`
22. Klik `+ Default Plan` pada toolbar
23. Pilih Product `SAMS`, pilih Pricing Type `Paid`, isi Plan Name `Supply Baru {runId}-126`
24. Klik `[Submit]`
25. Tunggu aksi selesai (Plan Detail `Supply Baru {runId}-126` terbuka)
26. Buka Plans & Licensing > Plans & Features, lalu klik tab `Custom` sub-tab `Active`
27. Klik `+ Custom Plan` pada toolbar
28. Pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Paket Alokasi {runId}-126`
29. Klik `[Submit]`
30. Tunggu aksi selesai (Plan Detail `Paket Alokasi {runId}-126` terbuka)
31. Buka Allocation > Client Subscription, klik `+ Subscription`, lalu buka dropdown Plan
32. Verifikasi Dropdown Plan memuat `Supply Baru {runId}-126` (default plan, platform-wide)
33. Verifikasi Dropdown Plan memuat `Paket Alokasi {runId}-126` (custom plan milik entitas aktor Principal)
34. Tutup form `+ Subscription` tanpa menyimpan
35. Hapus `Supply Baru {runId}-126` dan `Paket Alokasi {runId}-126` lewat Fixture BE

### TC-AC-PF-544: Edit plan tidak diterapkan ke subscription existing

36. Pindah ke Dataset Plan A dan Dataset Plan D lewat Fixture BE
37. Buka Plans & Licensing > Plans & Features, lalu klik tab `Default` sub-tab `Active`
38. Buka Overlay Row Action `Growth`, lalu klik `Edit`
39. Ubah Group count `3` menjadi `25`
40. Klik `[Save]`
41. Tunggu aksi selesai (Plan Detail `Growth` terbuka)
42. Buka Allocation > Client Subscription, lalu cari subscription `PT Sejahtera Abadi`
43. Verifikasi Subscription `PT Sejahtera Abadi` tetap memegang `v5`
44. Tambah subscription baru untuk `PT Baru Mulia` dengan plan `Growth` lewat `+ Subscription`
45. Verifikasi Subscription baru `PT Baru Mulia` memegang `v6`
46. Pulihkan Dataset Plan A dan Dataset Plan D (`Growth` v5) serta hapus subscription `PT Baru Mulia` lewat Fixture BE

### TC-AC-PF-545: Renewal Keep current plan mengunci versi terbaru

47. Buka Allocation > Client Subscription, lalu jalankan Renew pada subscription `PT Turun Satu` dengan `Keep current plan`
48. Buka Plans & Licensing > Plans & Features, klik tab `Custom` sub-tab `Active`, buka Plan Detail `Paket Turun`, lalu klik Tab Assigned Clients
49. Verifikasi Kolom Plan Version `PT Turun Satu` menjadi `v3`
50. Verifikasi Badge `Outdated` pada `PT Turun Satu` hilang
51. Buka Overlay Row Action `PT Turun Satu`
52. Verifikasi Overlay Row Action memuat `Detail` dan tidak memuat `Push Update`
53. Tutup Overlay Row Action
54. Pulihkan Dataset Plan P ke keadaan awal lewat Fixture BE

### TC-AC-PF-546: Push Update mengubah Feature Entitlement subscription

55. Buka Plans & Licensing > Plans & Features, klik tab `Custom` sub-tab `Active`, buka Plan Detail `Paket Push`, lalu klik Tab Assigned Clients
56. Buka Overlay Row Action `PT Push Dua`, lalu klik `Push Update`
57. Klik `[Push Update]` pada dialog
58. Tunggu aksi selesai (dialog tertutup)
59. Buka Allocation > Client Subscription > List Subscriptions, lalu lihat subscription `PT Push Dua`
60. Verifikasi Feature Entitlement subscription `PT Push Dua` menampilkan nilai versi `v3`
61. Verifikasi Open API `Yes` dan API call quota `100K/month` pada Feature Entitlement `PT Push Dua`
62. Pulihkan Dataset Plan P ke keadaan awal lewat Fixture BE

## Notes

- Langkah penghubung (S-03): buka tab, sub-tab, dan modul sebagai precondition TC, "Tunggu aksi selesai" sebelum pindah surface (bagian 8b butir 8), menutup form `+ Subscription` tanpa menyimpan, menutup form dirty lewat klik segmen Breadcrumb `Plans & Features`, `Unsaved Changes`, dan `[Leave]` (S-08; langkah 17 sampai 19), Search subscription `PT Sejahtera Abadi` pada langkah 42 untuk menemukan baris target (R-16), pemindahan Dataset aktif lewat Fixture BE (langkah 1 dan 36), dan pemulihan Dataset lewat Fixture BE.
- Pembagian TC lintas spec: TC-AC-PF-547, TC-AC-PF-548, TC-AC-PF-550, dan TC-AC-PF-551 (efek lintas modul ke FAMS dan Role & Permission) ada di spec 127.
- Asersi pendukung (S-03): langkah 8 dan 15 (`Verifikasi` opsi `Growth` ada) adalah anchor positif bagi asersi tiadanya `Enterprise` pada langkah 9 dan 16 dan bukan Expected TC tersendiri.
- Alasan melewati sekitar 35 langkah (62 langkah): kelima TC lintas modul memakai dua modul (Plans & Features dan Allocation), data Pre-setup berbeda per TC, dan perlu pemulihan Dataset antar blok; S-01 memecah Expected bermajemuk TC-AC-PF-542, TC-AC-PF-543, dan TC-AC-PF-544. Seluruh blok berkelas fungsional dan tidak ada blok baca-log berpola yang dapat dikeluarkan dari hitungan.
- Temuan untuk QA:
  - TC-AC-PF-542 Expected butir a ("subscription existing yang memegangnya tidak terdampak") tidak dapat diasersi: Dataset Plan Y tanpa subscription sehingga tidak ada subscription existing atas `Enterprise`. Klausa itu tidak punya `Verifikasi`; perlu data atau perubahan TC.
  - TC-AC-PF-544 menyebut client `PT Baru Mulia` yang tidak ada di Tabel Pre-setup TC dan tidak menyebut kolom yang diisi di `+ Subscription` selain client dan plan; spec menulis client itu sebagai disediakan tim FE.
  - TC-AC-PF-544 langkah 1 ("ubah Group count") tidak menyebut nilai; spec memakai `3` menjadi `25` (nilai TC-AC-PF-523).
  - TC-AC-PF-543 memakai nama literal `Supply Baru` dan `Paket Alokasi`; spec memberi suffix `{runId}-126` karena plan dibuat spec (S-12).
  - TC-AC-PF-545 Expected butir b ("perubahan terjadi lewat Renewal eksplisit") diasersi sebagai tidak adanya `Push Update` pada Overlay Row Action `PT Turun Satu` (langkah 52).
  - TC-AC-PF-546 tidak menyebut bentuk tampilan "nilai versi `v3`" di Feature Entitlement selain Open API dan API call quota; ditulis sesuai TC.
