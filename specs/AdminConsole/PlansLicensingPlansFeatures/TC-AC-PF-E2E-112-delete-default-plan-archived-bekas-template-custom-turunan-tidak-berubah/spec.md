---
id: TC-AC-PF-E2E-112-delete-default-plan-archived-bekas-template-custom-turunan-tidak-berubah
title: "Delete Default Plan Archived Bekas Template: Custom Plan Turunan Tidak Berubah"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-765
coverage:
  web: automated
---

# Delete Default Plan Archived Bekas Template: Custom Plan Turunan Tidak Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan R (Pre-setup #30): default FAMS Paid archived `Plan Arsip Tengah` tidak pernah dipakai; Dataset Plan TD (Pre-setup #60): custom plan Principal `Paket Turunan Arsip` (FAMS, Paid, v1) turunan Template `Plan Arsip Tengah`, dibuat lewat Fixture BE sebelum plan itu di-archive. Aksi menghapus data. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan R dan Dataset Plan TD) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: `Plan Arsip Tengah` terhapus permanen dan dipulihkan lewat Fixture BE; entri Delete bertambah di Changelog Default dan tidak dapat dihapus. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-765: Delete default plan archived bekas Template

1. Buka tab Custom sub-tab Active pada Plans List
2. Buka Plan Detail `Paket Turunan Arsip`
3. Catat judul dan nilai Tab Overview `Paket Turunan Arsip`
4. Kembali ke Plans List tab Default sub-tab Archive
5. Catat jumlah entri Changelog tab Custom sebagai baseline
6. Buka Overlay Row Action `Plan Arsip Tengah`, lalu klik `Delete`
7. Klik `[Delete]` pada dialog `Delete Plan`
8. Verifikasi Toast sukses: "Success, plan has been permanently deleted."
9. Verifikasi Sub-tab Default > Archive menampilkan plan archived lain (anchor)
10. Verifikasi `Plan Arsip Tengah` tidak ada lagi di Default > Archive
11. Kembali ke Plans List tab Custom sub-tab Active
12. Buka Plan Detail `Paket Turunan Arsip`
13. Verifikasi Judul Plan Detail `Paket Turunan Arsip – v1`
14. Verifikasi `Paket Turunan Arsip` berstatus Active
15. Verifikasi Nilai Tab Overview sama dengan yang dicatat pada langkah 3
16. Kembali ke Plans List tab Custom sub-tab Active
17. Klik ikon Changelog pada toolbar tab Custom
18. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
19. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 5 (tidak ada entri baru untuk `Paket Turunan Arsip`)
20. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, mencatat judul dan nilai Tab Overview sebelum aksi, kembali ke Plans List, dan menutup modal Changelog.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-765 tidak menyatakan nilai Tab Overview yang dicatat; spec membandingkan nilai yang dicatat sebelum dan sesudah aksi.
