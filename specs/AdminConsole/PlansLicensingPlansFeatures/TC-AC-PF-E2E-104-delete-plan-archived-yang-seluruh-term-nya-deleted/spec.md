---
id: TC-AC-PF-E2E-104-delete-plan-archived-yang-seluruh-term-nya-deleted
title: "Delete Plan Archived yang Seluruh Term-nya Deleted"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-799
coverage:
  web: automated
---

# Delete Plan Archived yang Seluruh Term-nya Deleted

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan DS (Pre-setup #63) disiapkan lewat Fixture BE: custom plan Principal `Paket Semua Deleted` (FAMS, Paid, v1, archived) dan default plan `Plan Semua Deleted` (FAMS, Paid, v1, archived), masing-masing pernah dipakai dua client yang seluruh term-nya `Deleted` (terhapus permanen, tidak terhitung di kolom Clients). Aksi menghapus data. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom dan tab Default. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan DS) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: kedua plan terhapus permanen dan dipulihkan lewat Fixture BE; entri Delete bertambah di Changelog Custom dan Changelog Default. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-799: Plan archived yang seluruh term-nya Deleted: Delete tampil dan berhasil

1. Buka tab Custom sub-tab Archive pada Plans List
2. Verifikasi Kolom Clients baris `Paket Semua Deleted` bernilai `0`
3. Catat jumlah entri Changelog tab Custom sebagai baseline
4. Buka Overlay Row Action `Paket Semua Deleted`
5. Verifikasi Overlay Row Action memuat `Delete`
6. Klik `Delete`
7. Klik `[Delete]` pada dialog `Delete Plan`
8. Verifikasi Toast sukses: "Success, plan has been permanently deleted."
9. Verifikasi `Paket Semua Deleted` tidak ada lagi di Custom > Archive
10. Klik ikon Changelog pada toolbar tab Custom
11. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
12. Verifikasi Jumlah entri Changelog tab Custom bertambah tepat satu dari baseline langkah 3 dan entri terbaru berisi Action `Delete` dan Plan Name `Paket Semua Deleted`
13. Tutup modal Changelog
14. Buka tab Default sub-tab Archive pada Plans List
15. Verifikasi Kolom Clients baris `Plan Semua Deleted` bernilai `0`
16. Catat jumlah entri Changelog tab Default sebagai baseline
17. Buka Overlay Row Action `Plan Semua Deleted`
18. Verifikasi Overlay Row Action memuat `Delete`
19. Klik `Delete`
20. Klik `[Delete]` pada dialog `Delete Plan`
21. Verifikasi Toast sukses: "Success, plan has been permanently deleted."
22. Verifikasi `Plan Semua Deleted` tidak ada lagi di Default > Archive
23. Klik ikon Changelog pada toolbar tab Default
24. Verifikasi Modal Changelog tab Default tampil dengan entri sebelumnya (anchor)
25. Verifikasi Jumlah entri Changelog tab Default bertambah tepat satu dari baseline langkah 16 dan entri terbaru berisi Action `Delete` dan Plan Name `Plan Semua Deleted`
26. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, mencatat baseline jumlah entri Changelog sebelum aksi Delete, dan menutup modal Changelog.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-799 tidak menyebut plan pembanding di Custom > Archive atau Default > Archive untuk anchor asersi hilangnya baris; spec memakai toast sukses dan entri Changelog Delete sebagai bukti terhubung ke pemicu (bagian 8b butir 2).
