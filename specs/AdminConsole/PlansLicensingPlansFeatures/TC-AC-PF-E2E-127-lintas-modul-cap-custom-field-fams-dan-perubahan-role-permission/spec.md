---
id: TC-AC-PF-E2E-127-lintas-modul-cap-custom-field-fams-dan-perubahan-role-permission
title: "Lintas Modul: Cap Custom Field FAMS dan Perubahan Role dan Permission Berlaku pada Pemuatan Berikutnya"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-547
  - TC-AC-PF-548
  - TC-AC-PF-550
  - TC-AC-PF-551
coverage:
  web: automated
---

# Lintas Modul: Cap Custom Field FAMS dan Perubahan Role dan Permission Berlaku pada Pemuatan Berikutnya

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (hook `before`; TC-AC-PF-547 dan TC-AC-PF-548): Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`.
- Akun ganti akun eksplisit: Group-Mix Principal `groupMixPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #8; Manage plans & licensing: Read dan Update; Group Role Manage active client: CRUD pada group pemakai plan `Growth` kecuali Read Only pada PT Bumi Sentosa), password dari `Spectra.env.AC_PF_GM_PASSWORD` (langkah 15 dan 16, TC-AC-PF-550); Read Only Principal `readOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`; Pre-setup #2), password dari `Spectra.env.AC_PF_RO_PASSWORD` (langkah 23 dan 24, TC-AC-PF-551). Hook `after` mengembalikan sesi ke akun default suite (S-07).
- Login akun aktor pertama di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Env var: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_PF_GM_PASSWORD`, dan `Spectra.env.AC_PF_RO_PASSWORD`; nama `AC_PF_GM_PASSWORD` dan `AC_PF_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `8` untuk TC-AC-PF-547 dan TC-AC-PF-548 (precondition TC; baseline suite `5` dan `2`); Asset Name `Laptop QA` memiliki 8 custom field di modul FAMS Custom Fields (precondition TC; tidak ada di Tabel Pre-setup TC). Dataset Plan D (Pre-setup #24): default `Growth` v5 dengan sembilan client, termasuk `PT Bumi Sentosa`. Dataset Plan A (Pre-setup #21): custom plan `Growth Tier`. Group Role aktor #8 atas group `PT Bumi Sentosa` berubah dari Read Only menjadi CRUD, dan capability Update diberikan ke aktor #2 setelah login, keduanya lewat Fixture BE yang menyalin perubahan di Settings > Role & Permission (precondition TC).
- State global: suite serial (`parallel: false`). Pemulihan Global FAMS Settings (`5` dan `2`), custom field `Laptop QA`, Group Role aktor #8 (Read Only atas `PT Bumi Sentosa`), dan capability aktor #2 dijamin Fixture BE (idempoten, disediakan tim FE/BE): dijalankan di hook `before` dan `after` serta sebagai langkah penghubung (langkah 14, 22, dan 31). Efek yang tersisa: entri Changelog Global Settings, System Log, dan Activity Log bertambah dan bersifat permanen.
- Kemampuan teknis (disediakan tim FE/BE): akses ke modul FAMS > Settings > Custom Fields untuk client yang dipakai; Fixture BE untuk Global FAMS Settings, custom field `Laptop QA`, Group Role, dan capability; ganti akun lewat Logout lalu login.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite untuk akun #1, #2, dan #8 (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-547: Max custom fields per asset name dibaca FAMS sebagai cap

1. Atur Global FAMS Settings `Max custom fields per asset name` `8` dan Asset Name `Laptop QA` dengan 8 custom field lewat Fixture BE
2. Buka FAMS > Settings > Custom Fields untuk client
3. Coba membuat custom field kesembilan pada `Laptop QA`
4. Verifikasi Pembuatan custom field kesembilan ditolak karena cap 8 tercapai
5. Verifikasi Custom field ke-1 sampai ke-8 tetap ada

### TC-AC-PF-548: Menurunkan cap di bawah jumlah existing tidak menghapus field

6. Buka Plans & Licensing > Plans & Features, lalu klik tab `Global Settings`
7. Ubah `Max custom fields per asset name` dari `8` menjadi `5`
8. Klik `[Save]`
9. Tunggu aksi selesai (toast sukses tampil)
10. Buka FAMS > Settings > Custom Fields untuk `Laptop QA`
11. Verifikasi Kedelapan custom field existing tetap ada dan tidak dihapus
12. Coba membuat custom field baru
13. Verifikasi Pembuatan custom field baru ditolak sampai jumlahnya di bawah 5
14. Pulihkan Global FAMS Settings ke `5` dan `2` serta custom field `Laptop QA` lewat Fixture BE

### TC-AC-PF-550: Perubahan Group Role memengaruhi masking pada pemuatan berikutnya

15. Ganti akun: Logout dari akun Total Control Principal
16. Login sebagai `groupMixPrincipal_automated_{namaCompany}@qwertysystem.net` dengan password dari `Spectra.env.AC_PF_GM_PASSWORD`
17. Ubah Group Role aktor atas group `PT Bumi Sentosa` dari Read Only menjadi CRUD lewat Fixture BE
18. Muat ulang halaman, buka Plan Detail `Growth` pada tab Default sub-tab Active, lalu klik Tab Assigned Clients
19. Buka Overlay Row Action `PT Bumi Sentosa`
20. Verifikasi Overlay Row Action `PT Bumi Sentosa` memuat `Detail` dan `Push Update`
21. Tutup Overlay Row Action
22. Pulihkan Group Role aktor atas group `PT Bumi Sentosa` ke Read Only lewat Fixture BE

### TC-AC-PF-551: Pemberian capability Update setelah login berlaku pada pemuatan berikutnya

23. Ganti akun: Logout dari akun Group-Mix Principal
24. Login sebagai `readOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` dengan password dari `Spectra.env.AC_PF_RO_PASSWORD`
25. Berikan capability Update kepada aktor lewat Fixture BE
26. Muat ulang halaman
27. Klik tab `Custom` sub-tab `Active`
28. Buka Overlay Row Action `Growth Tier`
29. Verifikasi Overlay Row Action `Growth Tier` memuat `Detail` dan `Edit`
30. Tutup Overlay Row Action
31. Cabut capability Update dari aktor lewat Fixture BE

## Notes

- Langkah penghubung (S-03): buka tab dan modul sebagai precondition TC, "Tunggu aksi selesai" sebelum pindah surface (bagian 8b butir 8), tutup Overlay Row Action, serta pemulihan Global FAMS Settings, custom field, Group Role, dan capability lewat Fixture BE (langkah 14, 22, 31). Ganti akun ditulis sebagai langkah eksplisit (S-07; langkah 15, 16, 23, 24); `## Test Steps` per blok akun sah karena langkah tiap blok berbeda.
- Pembagian TC lintas spec: TC-AC-PF-542 sampai TC-AC-PF-546 ada di spec 126.
- Temuan untuk QA:
  - TC-AC-PF-547 dan TC-AC-PF-548 bergantung pada modul FAMS > Settings > Custom Fields dan Asset Name `Laptop QA` (8 custom field) yang tidak ada di Tabel Pre-setup TC; spec menuliskannya sebagai kemampuan "disediakan tim FE/BE" tanpa endpoint karangan.
  - TC-AC-PF-547 Expected tidak menyebut pesan penolakan custom field kesembilan; spec hanya mengasersi penolakan sesuai Expected.
  - TC-AC-PF-548 langkah 3 ("coba membuat custom field baru") tidak menyebut nilai atau nama field; Expected butir b menyebut "sampai jumlahnya di bawah 5" tanpa langkah penghapusan; spec hanya mengasersi penolakan.
  - TC-AC-PF-550 menyatakan Group Role diubah "di Settings > Role & Permission" sebagai precondition tanpa menyebut siapa pelaku perubahan; spec memakai Fixture BE yang disediakan tim FE/BE (S-13). Tabel Pre-setup #8 menyebut aktor Group-Mix tanpa baris Group Role setelah perubahan.
  - TC-AC-PF-551 precondition (a) menyebut capability diberikan "setelah aktor login" tanpa menyebut pelaku; spec memakai Fixture BE yang disediakan tim FE/BE (S-13).
  - Password akun #2 dan #8 memakai nama `AC_PF_RO_PASSWORD` dan `AC_PF_GM_PASSWORD` sesuai `suite.md`; pendaftarannya di `spectra.config.ts` dan `.env.example` berada di luar folder suite.
  - Post Condition "Tidak ada perubahan data" (TC-AC-PF-550, TC-AC-PF-551) tanpa langkah observasi tidak diasersi (S-01).
