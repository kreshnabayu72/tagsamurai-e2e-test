---
id: TC-AC-PF-E2E-107-push-update-teks-jumlah-client-outdated-dan-ketiadaan-aksi
title: "Push Update: Teks Jumlah Client Outdated dan Ketiadaan Aksi Massal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-271
  - TC-AC-PF-272
  - TC-AC-PF-282
  - TC-AC-PF-283
coverage:
  web: automated
---

# Push Update: Teks Jumlah Client Outdated dan Ketiadaan Aksi Massal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Dataset Plan P: custom plan Principal `Paket Push` v3 (v1 Group count 3, Open API OFF; v2 Group count 25; v3 Open API ON dan API call quota 100K/month) dengan client PT Push Satu Active v1, PT Push Dua Active v2, PT Push Tiga Grace v1, PT Push Empat Expired v1, PT Push Lima Active v3, PT Push Waiting Waiting for Approval v1, PT Push Pending Pending v1, PT Push Arsip Archive v1, PT Push Purge Purge v1. Custom plan `Satu Outdated` memiliki tepat satu client Outdated; custom plan `Semua Terbaru` memiliki semua client di versi terbaru. Dataset hanya dibaca; tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan P) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: tidak ada perubahan data (seluruh blok hanya membaca). Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-271: Teks jumlah client outdated di toolbar Tab Assigned Clients

1. Buka tab Custom sub-tab Active pada Plans List
2. Buka Plan Detail `Satu Outdated`
3. Klik Tab Assigned Clients
4. Verifikasi Toolbar menampilkan teks "1 client on an outdated version"
5. Kembali ke Plans List tab Custom sub-tab Active
6. Buka Plan Detail `Paket Push`
7. Klik Tab Assigned Clients
8. Verifikasi Toolbar menampilkan teks "8 clients on an outdated version" (PT Push Lima di versi terbaru tidak dihitung)

### TC-AC-PF-272: Teks jumlah client outdated tidak tampil bila tidak ada client Outdated

9. Kembali ke Plans List tab Custom sub-tab Active
10. Buka Plan Detail `Semua Terbaru`
11. Klik Tab Assigned Clients
12. Verifikasi Toolbar memuat Search, Filter, Download
13. Verifikasi Teks jumlah client outdated tidak tampil

### TC-AC-PF-282: Tab Assigned Clients tidak memiliki aksi Push Update massal

14. Kembali ke Plans List tab Custom sub-tab Active
15. Buka Plan Detail `Paket Push`
16. Klik Tab Assigned Clients
17. Verifikasi Toolbar memuat Search, Filter, Download (anchor)
18. Verifikasi Tidak ada tombol `[Push Update to All]`
19. Verifikasi Tidak ada Bulk Action Bar
20. Verifikasi Tidak ada kolom checkbox

### TC-AC-PF-283: Push Update tidak ada pada menu row action Plans List

21. Kembali ke Plans List tab Custom sub-tab Active
22. Buka Overlay Row Action `Paket Push`
23. Verifikasi Overlay Row Action hanya memuat `Detail`, `Edit`, `Archive` (`Push Update` tidak ada)
24. Tutup Overlay Row Action

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, kembali ke Plans List antar blok, dan menutup Overlay Row Action.
- Temuan untuk QA: TC-AC-PF-282 Expected menyebut Push Update hanya tersedia dari row action satu client sebagai kesimpulan; tidak diasersi terpisah (S-03).
- Temuan untuk QA: TC-AC-PF-272 dan TC-AC-PF-282 mengasersi ketiadaan elemen; spec memakai toolbar Search, Filter, Download sebagai anchor positif (bagian 8b butir 2).
