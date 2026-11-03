---
id: TC-AC-PF-E2E-097-archive-custom-plan-sukses-header-plan-detail-klik-ganda
title: "Archive Custom Plan: Sukses dari Row Action, Header Plan Detail, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-240
  - TC-AC-PF-253
  - TC-AC-PF-675
coverage:
  web: automated
---

# Archive Custom Plan: Sukses dari Row Action, Header Plan Detail, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: custom plan Principal `Paket Tanpa Client` aktif tanpa subscription (Dataset Plan G, Pre-setup #27). Dipakai tiga kali (satu kali per TC) dan dipulihkan ke Custom > Active lewat Fixture BE di antara blok TC. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44). Jam server dan jam browser sinkron untuk asersi Last Modified.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (`Paket Tanpa Client` (Dataset Plan G)) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: Last Modified `Paket Tanpa Client` dan tiga entri Archive di Changelog Custom bertambah per run. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-240: Archive custom plan tanpa subscription penahan berhasil

1. Buka tab Custom sub-tab Active pada Plans List
2. Buka Overlay Row Action `Paket Tanpa Client`, lalu klik `Archive`
3. Klik `[Archive]`
4. Catat waktu sesudah klik `[Archive]` (acuan Last Modified)
5. Verifikasi Dialog tertutup
6. Verifikasi Toast sukses: "Success, plan has been archived."
7. Verifikasi Sub-tab Active menampilkan plan Custom lain (anchor)
8. Verifikasi `Paket Tanpa Client` tidak ada di sub-tab Active
9. Klik sub-tab Archive
10. Verifikasi `Paket Tanpa Client` ada di sub-tab Archive
11. Verifikasi Last Modified baris `Paket Tanpa Client` sesuai waktu Archive pada langkah 4 (toleransi satu menit; format `dd MMM yy`, 24-hour, UTC)
12. Verifikasi Clients baris `Paket Tanpa Client` tetap `0`
13. Buka Overlay Row Action `Paket Tanpa Client`
14. Verifikasi Overlay Row Action hanya memuat `Detail` dan `Delete`
15. Tutup Overlay Row Action
16. Pulihkan `Paket Tanpa Client` (Custom > Active) ke keadaan awal lewat Fixture BE

### TC-AC-PF-253: Archive dari header Plan Detail custom plan

17. Muat ulang halaman Plans & Features, lalu buka tab Custom sub-tab Active
18. Buka Plan Detail `Paket Tanpa Client`
19. Klik button `Archive` di header
20. Klik `[Archive]` pada dialog
21. Verifikasi Toast sukses: "Success, plan has been archived."
22. Verifikasi Plan Detail menampilkan Status Badge `Archived`
23. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Custom > Archive > Detail`
24. Verifikasi Header Plan Detail memuat ikon Download saja
25. Verifikasi Button `Edit` dan `Archive` Hidden
26. Pulihkan `Paket Tanpa Client` (Custom > Active) ke keadaan awal lewat Fixture BE

### TC-AC-PF-675: Klik ganda cepat pada tombol Archive

27. Muat ulang halaman Plans & Features, lalu buka tab Custom sub-tab Active
28. Catat jumlah entri Changelog tab Custom sebagai baseline
29. Buka Overlay Row Action `Paket Tanpa Client`, lalu klik `Archive`
30. Klik `[Archive]` dua kali dengan cepat
31. Verifikasi Muncul satu toast sukses: "Success, plan has been archived."
32. Verifikasi Tidak ada toast error
33. Klik sub-tab Archive
34. Verifikasi `Paket Tanpa Client` ada di sub-tab Archive
35. Klik ikon Changelog pada toolbar tab Custom
36. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
37. Verifikasi Jumlah entri Changelog tab Custom bertambah tepat satu dari baseline langkah 28 dan entri terbaru berisi Action `Archive` untuk `Paket Tanpa Client`
38. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, menutup overlay dan modal Changelog, memulihkan `Paket Tanpa Client` lewat Fixture BE dan memuat ulang halaman antar blok TC (data berubah oleh blok sebelumnya).
- Semua blok berkelas fungsional, memakai data yang sama dan dipulihkan sebelum blok berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah langkah melampaui 35 langkah karena tiap Expected punya `Verifikasi` sendiri (S-01) dan pemulihan antar blok.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-240 tidak menyebut apakah Last Modified diasersi terhadap waktu aksi; spec memakai waktu yang dicatat sesudah klik `[Archive]` dengan toleransi satu menit (S-12).
