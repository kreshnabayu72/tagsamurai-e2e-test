---
id: TC-AC-PF-E2E-110-confirm-push-update-sukses-plan-free-diff-preset-klik-ganda
title: "Confirm Push Update: Sukses, Plan Free, Tabel Diff API Call Quota, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-278
  - TC-AC-PF-279
  - TC-AC-PF-650
  - TC-AC-PF-677
coverage:
  web: automated
---

# Confirm Push Update: Sukses, Plan Free, Tabel Diff API Call Quota, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Dataset Plan P: custom plan Principal `Paket Push` v3 (v1 Group count 3, Open API OFF; v2 Group count 25; v3 Open API ON dan API call quota 100K/month) dengan client PT Push Satu Active v1, PT Push Dua Active v2, PT Push Tiga Grace v1, PT Push Empat Expired v1, PT Push Lima Active v3, PT Push Waiting Waiting for Approval v1, PT Push Pending Pending v1, PT Push Arsip Archive v1, PT Push Purge Purge v1. Default `Starter` v3 dengan client `PT Free Satu` Active v2 dan delta upgrade (Dataset Plan P). Dataset Plan CP (Pre-setup #53): custom plan Principal `Paket Kuota Push` v2 (FAMS, Paid, Open API ON; v1 API call quota 100000 lewat Custom; v2 API call quota 150000) dengan client `PT Kuota Satu` Active v1. Tiap blok memulihkan versi client ke keadaan awal lewat Fixture BE. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44). Jam server dan jam browser sinkron.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan P dan Dataset Plan CP) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: versi client yang di-Push Update dipulihkan lewat Fixture BE; entri Push Update bertambah di Changelog Custom/Default dan tidak dapat dihapus. Last Modified `Paket Push` tidak berubah oleh Push Update (TC-AC-PF-278 butir f). Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-278: Confirm Push Update ke client eligible

1. Buka tab Custom sub-tab Active pada Plans List
2. Catat Last Modified baris `Paket Push` pada Plans List
3. Buka Plan Detail `Paket Push`
4. Klik Tab Assigned Clients
5. Catat teks jumlah client outdated pada toolbar
6. Buka Overlay Row Action `PT Push Dua`, lalu klik `Push Update`
7. Klik `[Push Update]`
8. Verifikasi Muncul toast sukses: "Success, plan update has been pushed."
9. Verifikasi Kolom Plan Version `PT Push Dua` menjadi `v3` tanpa badge `Outdated`
10. Verifikasi Teks jumlah client outdated berkurang satu dari nilai pada langkah 5
11. Buka Overlay Row Action `PT Push Dua`
12. Verifikasi Overlay Row Action `PT Push Dua` hanya memuat `Detail`
13. Tutup Overlay Row Action
14. Verifikasi Kolom Plan Version `PT Push Satu` tetap `v1`
15. Kembali ke Plans List tab Custom sub-tab Active
16. Verifikasi Last Modified baris `Paket Push` sama dengan nilai pada langkah 2 (Push Update tidak memperbarui Last Modified)
17. Pulihkan Dataset Plan P ke keadaan awal lewat Fixture BE

### TC-AC-PF-279: Push Update default plan Free berhasil

18. Buka tab Default sub-tab Active pada Plans List
19. Buka Plan Detail `Starter`
20. Klik Tab Assigned Clients
21. Buka Overlay Row Action `PT Free Satu`, lalu klik `Push Update`
22. Klik `[Push Update]`
23. Verifikasi Toast sukses: "Success, plan update has been pushed."
24. Verifikasi Kolom Plan Version `PT Free Satu` menjadi `v3`
25. Pulihkan Dataset Plan P ke keadaan awal lewat Fixture BE

### TC-AC-PF-650: Tabel diff Push Plan Update menampilkan API call quota bernilai sama dengan preset

26. Siapkan Dataset Plan CP lewat Fixture BE (seeding idempoten)
27. Buka tab Custom sub-tab Active pada Plans List
28. Buka Plan Detail `Paket Kuota Push`
29. Klik Tab Assigned Clients
30. Buka Overlay Row Action `PT Kuota Satu`, lalu klik `Push Update`
31. Verifikasi Dialog memuat teks "This client will be updated from v1 to v2."
32. Verifikasi Tabel diff memuat satu baris `API call quota` | `100K/month` | `150,000/month` (nilai lama 100000 tampil sebagai preset, bukan `100,000/month`)
33. Klik `[Push Update]`
34. Verifikasi Muncul toast sukses: "Success, plan update has been pushed."
35. Verifikasi Kolom Plan Version `PT Kuota Satu` menjadi `v2`
36. Pulihkan Dataset Plan CP (`PT Kuota Satu` kembali ke v1) ke keadaan awal lewat Fixture BE

### TC-AC-PF-677: Klik ganda cepat pada tombol Push Update

37. Muat ulang halaman Plans & Features, lalu buka tab Custom sub-tab Active
38. Catat jumlah entri Changelog tab Custom sebagai baseline
39. Buka Plan Detail `Paket Push`
40. Klik Tab Assigned Clients
41. Buka Overlay Row Action `PT Push Dua`, lalu klik `Push Update`
42. Klik `[Push Update]` dua kali dengan cepat
43. Verifikasi Muncul satu toast sukses: "Success, plan update has been pushed."
44. Verifikasi Tidak ada toast error
45. Verifikasi Kolom Plan Version `PT Push Dua` menjadi `v3`
46. Kembali ke Plans List tab Custom sub-tab Active
47. Klik ikon Changelog pada toolbar tab Custom
48. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
49. Verifikasi Jumlah entri Changelog tab Custom bertambah tepat satu dari baseline langkah 38 dan entri terbaru berisi Action `Push Update` untuk `Paket Push`
50. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, mencatat Last Modified, teks jumlah client outdated, dan baseline Changelog sebelum aksi, memulihkan dataset lewat Fixture BE dan memuat ulang halaman antar blok TC, menutup modal Changelog.
- Aksi mengubah versi client berada di akhir tiap blok TC; urutan blok mengikuti nomor TC kecuali TC-AC-PF-677 yang sengaja terakhir karena memakai ulang `PT Push Dua` yang dipulihkan.
- Semua blok berkelas fungsional (Push Update) dan berdiri sendiri dengan pemulihan data sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah melampaui 35 langkah karena tiap Expected punya `Verifikasi` sendiri (S-01) dan pemulihan antar blok.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-278 Post Condition butir b (satu entri Changelog Action `Push Update`) tidak punya langkah observasi di TC dan tidak diasersi pada TC itu; entri Push Update hanya diasersi pada TC-AC-PF-677 (S-01).
- Temuan untuk QA: TC-AC-PF-279 dan TC-AC-PF-650 tidak menyebut nilai awal `Verifikasi` jumlah client outdated; tidak diasersi.
