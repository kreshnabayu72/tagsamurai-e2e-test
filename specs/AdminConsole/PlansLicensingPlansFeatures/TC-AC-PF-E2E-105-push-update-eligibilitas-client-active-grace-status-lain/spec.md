---
id: TC-AC-PF-E2E-105-push-update-eligibilitas-client-active-grace-status-lain
title: "Push Update: Eligibilitas Client Berdasarkan Status Subscription dan Versi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-264
  - TC-AC-PF-265
  - TC-AC-PF-266
  - TC-AC-PF-267
coverage:
  web: automated
---

# Push Update: Eligibilitas Client Berdasarkan Status Subscription dan Versi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Dataset Plan P: custom plan Principal `Paket Push` v3 (v1 Group count 3, Open API OFF; v2 Group count 25; v3 Open API ON dan API call quota 100K/month) dengan client PT Push Satu Active v1, PT Push Dua Active v2, PT Push Tiga Grace v1, PT Push Empat Expired v1, PT Push Lima Active v3, PT Push Waiting Waiting for Approval v1, PT Push Pending Pending v1, PT Push Arsip Archive v1, PT Push Purge Purge v1. Tabel client non-eligible TC-AC-PF-266: `PT Push Empat` (Expired v1), `PT Push Waiting` (Waiting for Approval v1), `PT Push Pending` (Pending v1), `PT Push Arsip` (Archive v1), `PT Push Purge` (Purge v1). Dataset hanya dibaca; tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Aktor memegang Group Role Manage active client CRUD pada group semua client (Pre-setup #1).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan P) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: tidak ada perubahan data (seluruh blok hanya membaca). Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-264: Client Active Outdated dengan delta upgrade murni menampilkan Push Update

1. Buka tab Custom sub-tab Active pada Plans List
2. Buka Plan Detail `Paket Push`
3. Klik Tab Assigned Clients
4. Verifikasi Kolom Plan Version `PT Push Satu` dan `PT Push Dua` menampilkan versi lama (`v1` dan `v2`) dengan badge `Outdated`
5. Buka Overlay Row Action `PT Push Satu`
6. Verifikasi Overlay Row Action memuat `Detail` dan `Push Update` (ikon `ArrowUpCircleLine`, severity dark)
7. Tutup Overlay Row Action
8. Buka Overlay Row Action `PT Push Dua`
9. Verifikasi Overlay Row Action memuat `Detail` dan `Push Update` (ikon `ArrowUpCircleLine`, severity dark)
10. Tutup Overlay Row Action

### TC-AC-PF-265: Client Grace Outdated dengan delta upgrade tetap eligible Push Update

11. Buka Overlay Row Action `PT Push Tiga`
12. Verifikasi Overlay Row Action memuat `Detail` dan `Push Update`
13. Verifikasi Badge Subscription Status `Grace` dan Plan Version `v1` dengan badge `Outdated` pada baris `PT Push Tiga`
14. Tutup Overlay Row Action

### TC-AC-PF-266: Client Expired, Waiting for Approval, Pending, Archive, dan Purge tidak eligible

15. Buka Overlay Row Action `PT Push Empat`
16. Verifikasi Overlay Row Action `PT Push Empat` hanya memuat `Detail` (`Push Update` tidak ada walau versi lebih lama dan delta upgrade)
17. Tutup Overlay Row Action
18. Buka Overlay Row Action `PT Push Waiting`
19. Verifikasi Overlay Row Action `PT Push Waiting` hanya memuat `Detail` (`Push Update` tidak ada walau versi lebih lama dan delta upgrade)
20. Tutup Overlay Row Action
21. Buka Overlay Row Action `PT Push Pending`
22. Verifikasi Overlay Row Action `PT Push Pending` hanya memuat `Detail` (`Push Update` tidak ada walau versi lebih lama dan delta upgrade)
23. Tutup Overlay Row Action
24. Buka Overlay Row Action `PT Push Arsip`
25. Verifikasi Overlay Row Action `PT Push Arsip` hanya memuat `Detail` (`Push Update` tidak ada walau versi lebih lama dan delta upgrade)
26. Tutup Overlay Row Action
27. Buka Overlay Row Action `PT Push Purge`
28. Verifikasi Overlay Row Action `PT Push Purge` hanya memuat `Detail` (`Push Update` tidak ada walau versi lebih lama dan delta upgrade)
29. Tutup Overlay Row Action
30. Arahkan kursor ke baris `PT Push Empat`
31. Verifikasi Tidak ada tooltip penjelas pada baris `PT Push Empat`

### TC-AC-PF-267: Client di versi terbaru tidak berbadge Outdated dan tidak memiliki Push Update

32. Verifikasi Baris `PT Push Lima` menampilkan Plan Version `v3` tanpa badge `Outdated`
33. Buka Overlay Row Action `PT Push Lima`
34. Verifikasi Overlay Row Action hanya memuat `Detail`
35. Tutup Overlay Row Action

## Notes

- Plan Detail `Paket Push` dan Tab Assigned Clients dibuka satu kali dan dipakai berulang oleh keempat blok (halaman yang sama dipakai berulang, bagian 3 prinsip 13); setiap blok menutup Overlay Row Action sebelum blok berikutnya.
- Blok TC-AC-PF-266 membuka overlay lima client satu per satu (langkah berulang per baris data); tiap iterasi memuat satu `Verifikasi` per klausa.
- Langkah "Arahkan kursor ke baris `PT Push Empat`" pada TC-AC-PF-266 adalah langkah penghubung agar asersi absence tooltip bermakna (bagian 8b butir 5).
- Keempat blok berkelas fungsional dan hanya membaca; jumlah langkah di sekitar batas 35 karena tiap Expected punya `Verifikasi` sendiri (S-01).
- Temuan untuk QA: TC-AC-PF-266 Expected butir b (tidak ada tooltip penjelas pada baris tersebut) tidak menyebut baris mana yang diamati; spec mengamati baris `PT Push Empat`.
