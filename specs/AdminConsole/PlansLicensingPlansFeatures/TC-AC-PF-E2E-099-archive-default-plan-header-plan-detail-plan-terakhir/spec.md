---
id: TC-AC-PF-E2E-099-archive-default-plan-header-plan-detail-plan-terakhir
title: "Archive Default Plan: Header Plan Detail, Plan Terakhir, dan Template dengan Custom Plan Turunan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-254
  - TC-AC-PF-730
  - TC-AC-PF-764
coverage:
  web: automated
---

# Archive Default Plan: Header Plan Detail, Plan Terakhir, dan Template dengan Custom Plan Turunan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan Y (Pre-setup #37): default FAMS tanpa subscription Starter (Free), Growth, Professional, Enterprise (Paid tier 1, 2, 3); untuk TC-AC-PF-254 default plan `Professional` diberi satu client Active `PT Guard Professional` lewat Fixture BE (dibuang oleh pemulihan Dataset Plan Y); Dataset Plan TD (Pre-setup #60): custom plan Principal `Paket Turunan Enterprise` (FAMS, Paid, v1) turunan Template `Enterprise`, dibuat lewat Fixture BE sebelum Archive; Dataset Plan LD (Pre-setup #57): tepat satu default plan aktif `Satu Plan` (SIEM, Paid, v1, Clients 0) tanpa default plan lain. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Default dan tab Custom. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan Y, Dataset Plan TD, dan Dataset Plan LD) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: Last Modified plan yang diarsipkan berubah dan entri Archive bertambah di Changelog Default; Dataset Plan LD menggantikan sementara seluruh default plan tenant dan dipulihkan setelah blok terakhir. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-254: Archive dari header Plan Detail default plan memakai dialog dan guard yang sama

1. Buka tab Default sub-tab Active pada Plans List
2. Buka Plan Detail `Enterprise`
3. Klik button `Archive` di header
4. Klik `[Archive]` pada dialog
5. Verifikasi Toast sukses: "Success, plan has been archived."
6. Verifikasi Plan Detail `Enterprise` menampilkan Status Badge `Archived`
7. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Default > Archive > Detail`
8. Kembali ke Plans List tab Default sub-tab Active
9. Buka Plan Detail `Professional`
10. Klik button `Archive` di header
11. Verifikasi Dialog `Cannot Archive Plan` tampil dengan tombol `[OK]`
12. Klik `[OK]`
13. Verifikasi Plan Detail `Professional` menampilkan Status Badge `Active` (plan tetap Active)
14. Pulihkan Dataset Plan Y ke keadaan awal lewat Fixture BE

### TC-AC-PF-764: Archive default plan yang pernah menjadi Template

15. Muat ulang halaman Plans & Features, lalu buka tab Custom sub-tab Active
16. Buka Plan Detail `Paket Turunan Enterprise`
17. Catat judul dan nilai Tab Overview `Paket Turunan Enterprise`
18. Kembali ke Plans List tab Default sub-tab Active
19. Catat jumlah entri Changelog tab Custom sebagai baseline
20. Buka Overlay Row Action `Enterprise`, lalu klik `Archive`
21. Klik `[Archive]` pada dialog `Archive Plan`
22. Verifikasi Toast sukses: "Success, plan has been archived."
23. Verifikasi Dialog `Cannot Archive Plan` tidak muncul
24. Klik sub-tab Archive
25. Verifikasi `Enterprise` ada di Default > Archive
26. Kembali ke Plans List tab Custom sub-tab Active
27. Buka Plan Detail `Paket Turunan Enterprise`
28. Verifikasi Judul Plan Detail `Paket Turunan Enterprise – v1`
29. Verifikasi `Paket Turunan Enterprise` berstatus Active
30. Verifikasi Nilai Tab Overview sama dengan yang dicatat pada langkah 17
31. Kembali ke Plans List tab Custom sub-tab Active
32. Klik ikon Changelog pada toolbar tab Custom
33. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
34. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 19 (tidak ada entri baru untuk `Paket Turunan Enterprise`)
35. Tutup modal Changelog
36. Pulihkan Dataset Plan Y dan Dataset Plan TD ke keadaan awal lewat Fixture BE

### TC-AC-PF-730: Archive default plan terakhir yang tersisa diizinkan

37. Siapkan Dataset Plan LD lewat Fixture BE (tepat satu default plan aktif `Satu Plan`, SIEM Paid, tanpa subscription)
38. Muat ulang halaman Plans & Features, lalu buka tab Default sub-tab Active
39. Catat jumlah entri Changelog tab Default sebagai baseline
40. Buka Overlay Row Action `Satu Plan`, lalu klik `Archive`
41. Klik `[Archive]`
42. Verifikasi Toast sukses: "Success, plan has been archived."
43. Verifikasi Dialog `Cannot Archive Plan` tidak muncul
44. Verifikasi Sub-tab Active menampilkan empty state "No default plans yet"
45. Klik sub-tab Archive
46. Verifikasi `Satu Plan` ada di sub-tab Archive
47. Klik ikon Changelog pada toolbar tab Default
48. Verifikasi Modal Changelog tab Default tampil dengan entri sebelumnya (anchor)
49. Verifikasi Jumlah entri Changelog tab Default bertambah tepat satu dari baseline langkah 39 dan entri terbaru berisi Action `Archive` untuk `Satu Plan`
50. Tutup modal Changelog

## Notes

- Urutan blok diubah dari urutan nomor TC: TC-AC-PF-730 ditempatkan terakhir karena Dataset Plan LD menggantikan seluruh default plan tenant sehingga blok lain tidak dapat dijalankan sesudahnya tanpa pemulihan Dataset Plan Y.
- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, kembali ke Plans List, menyiapkan dan memulihkan dataset lewat Fixture BE dan memuat ulang halaman antar blok TC, menutup modal Changelog.
- Ketiga blok berkelas fungsional dan berdiri sendiri dengan dataset sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah melampaui 35 langkah karena tiap Expected punya `Verifikasi` sendiri (S-01), pencatatan baseline dan nilai Tab Overview, serta pemulihan dataset antar blok.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-254 tidak menyebut teks isi dialog `Cannot Archive Plan` untuk `Professional`; spec hanya mengasersi judul dan tombol `[OK]` yang disebut Expected.
