---
id: TC-AC-PF-E2E-103-delete-plan-archived-sukses-klik-ganda-bekas-template
title: "Delete Plan Archived: Sukses, Nama Dibebaskan, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-258
  - TC-AC-PF-259
  - TC-AC-PF-676
coverage:
  web: automated
---

# Delete Plan Archived: Sukses, Nama Dibebaskan, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: custom plan Principal archived `Arsip Custom Satu` tidak pernah dipakai (Dataset Plan C, Pre-setup #23; dipulihkan lewat Fixture BE di antara blok); Dataset Plan R (Pre-setup #30): default FAMS Paid archived `Plan Arsip Lama` tidak pernah dipakai. Data Dinamis: default plan `Plan Arsip Lama` hasil Create ulang di TC-AC-PF-259 (nama literal sesuai TC) dibuang oleh pemulihan Dataset Plan R. Aksi menghapus data berada di akhir tiap blok. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (`Arsip Custom Satu` (Dataset Plan C) dan Dataset Plan R) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: plan terhapus permanen dipulihkan lewat Fixture BE; entri Delete dan Create bertambah di Changelog dan tidak dapat dihapus. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-258: Delete custom plan archived yang tidak pernah dipakai

1. Buka tab Custom sub-tab Archive pada Plans List
2. Buka Overlay Row Action `Arsip Custom Satu`, lalu klik `Delete`
3. Klik `[Delete]`
4. Verifikasi Toast sukses: "Success, plan has been permanently deleted."
5. Ketik Search `Arsip Custom Satu`, tekan Enter
6. Verifikasi Tabel Archive menampilkan "No results found"
7. Verifikasi `Arsip Custom Satu` tidak ada di sub-tab Archive
8. Klik `(←)` pada kotak Search
9. Pulihkan `Arsip Custom Satu` (Dataset Plan C) ke keadaan awal lewat Fixture BE

### TC-AC-PF-259: Delete default plan archived yang tidak pernah dipakai dan nama dapat dipakai kembali

10. Muat ulang halaman Plans & Features, lalu buka tab Default sub-tab Archive
11. Buka Overlay Row Action `Plan Arsip Lama`, lalu klik `Delete`
12. Klik `[Delete]`
13. Verifikasi Toast sukses: "Success, plan has been permanently deleted."
14. Klik sub-tab Active
15. Klik `+ Default Plan`
16. Pilih Product `FAMS`
17. Pilih Pricing Type yang tersedia
18. Isi Plan Name `Plan Arsip Lama`
19. Klik `[Submit]`
20. Verifikasi Pesan `Plan name already exists` tidak muncul
21. Verifikasi Pembuatan default plan `Plan Arsip Lama` berhasil
22. Pulihkan Dataset Plan R (termasuk menghapus `Plan Arsip Lama` hasil Create) ke keadaan awal lewat Fixture BE

### TC-AC-PF-676: Klik ganda cepat pada tombol Delete

23. Muat ulang halaman Plans & Features, lalu buka tab Custom sub-tab Archive
24. Catat jumlah entri Changelog tab Custom sebagai baseline
25. Buka Overlay Row Action `Arsip Custom Satu`, lalu klik `Delete`
26. Klik `[Delete]` dua kali dengan cepat
27. Verifikasi Muncul satu toast sukses: "Success, plan has been permanently deleted."
28. Verifikasi Tidak ada toast error
29. Verifikasi Sub-tab Archive menampilkan plan archived lain (anchor)
30. Verifikasi `Arsip Custom Satu` tidak ada di sub-tab Archive
31. Klik ikon Changelog pada toolbar tab Custom
32. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
33. Verifikasi Jumlah entri Changelog tab Custom bertambah tepat satu dari baseline langkah 24 dan entri terbaru berisi Action `Delete` untuk `Arsip Custom Satu`
34. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, mencari `Arsip Custom Satu` lewat Search untuk memenuhi Langkah 3 TC-AC-PF-258 dan mengosongkannya dengan `(←)` (R-16), memulihkan dataset lewat Fixture BE dan memuat ulang halaman antar blok TC, dan menutup modal Changelog.
- Blok berkelas fungsional dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah di sekitar batas 35 karena tiap Expected punya `Verifikasi` sendiri (S-01) dan pemulihan antar blok.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-259 langkah 2 tidak menyebut Pricing Type dan field wajib lain Create Default Plan; Dataset Plan R juga tidak menyebut default plan aktif sehingga slot Paid yang tersedia tidak diketahui. Spec memilih Pricing Type yang tersedia dan mengisi field wajib bernilai valid yang tidak diasersi. Indikator keberhasilan Create juga tidak disebut Expected; spec hanya memverifikasi "pembuatan berhasil" seperti tertulis.
- Temuan untuk QA: TC-AC-PF-258 Post Condition (seluruh snapshot versi terhapus) tidak punya langkah observasi di TC sehingga tidak diasersi.
