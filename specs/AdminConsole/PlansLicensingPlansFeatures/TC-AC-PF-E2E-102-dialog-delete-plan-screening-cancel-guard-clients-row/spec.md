---
id: TC-AC-PF-E2E-102-dialog-delete-plan-screening-cancel-guard-clients-row
title: "Dialog Delete Plan: Screening, Cancel, Guard Plan yang Pernah Dipakai, dan Row Action Plan Active"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-256
  - TC-AC-PF-257
  - TC-AC-PF-260
  - TC-AC-PF-261
  - TC-AC-PF-263
  - TC-AC-PF-607
coverage:
  web: automated
---

# Dialog Delete Plan: Screening, Cancel, Guard Plan yang Pernah Dipakai, dan Row Action Plan Active

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: custom plan Principal archived `Arsip Custom Satu` tidak pernah dipakai (Dataset Plan C, Pre-setup #23); Dataset Plan A (Pre-setup #21): default archived `Growth Plus (old)` (historical Clients 31), default aktif `Starter`, custom aktif `Growth Tier`; Dataset Plan G (Pre-setup #27): `Guard Expired` hanya memiliki satu client Expired dan sudah di-archive (disiapkan lewat Fixture BE); Dataset Plan R (Pre-setup #30): default FAMS Paid archived `Plan Arsip Lama` tidak pernah dipakai. Dataset hanya dibaca dan dibatalkan; tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Default. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan A, Dataset Plan C, Dataset Plan G, dan Dataset Plan R) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: tidak ada perubahan data karena seluruh Delete dibatalkan; Changelog tidak berubah. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-256: Screening dialog Delete Plan pada custom plan archived

1. Buka tab Custom sub-tab Archive pada Plans List
2. Buka Overlay Row Action `Arsip Custom Satu`, lalu klik `Delete`
3. Verifikasi Dialog tampil dengan Title `Delete Plan`; Body bullet • Arsip Custom Satu; teks "This action is permanent and cannot be undone. The plan will be removed; its change history stays in the log."; teks "Are you sure you want to delete it?"; tombol `[Cancel]` dan `[Delete]` (danger)
4. Klik area gelap di luar dialog
5. Verifikasi Dialog `Delete Plan` tidak tertutup
6. Klik `[Cancel]`

### TC-AC-PF-257: Cancel pada dialog Delete Plan menutup dialog

7. Buka Overlay Row Action `Arsip Custom Satu`, lalu klik `Delete`
8. Klik `[Cancel]`
9. Verifikasi Dialog tertutup
10. Verifikasi Tidak ada toast
11. Verifikasi `Arsip Custom Satu` tetap di sub-tab Archive

### TC-AC-PF-260: Plan archived yang pernah dipakai tidak menawarkan Delete

12. Buka tab Default sub-tab Archive pada Plans List
13. Buka Overlay Row Action `Growth Plus (old)`
14. Verifikasi Overlay Row Action hanya memuat `Detail`
15. Tutup Overlay Row Action
16. Buka Plan Detail `Growth Plus (old)`
17. Verifikasi Header Plan Detail tidak memuat aksi Delete, Edit, maupun Archive

### TC-AC-PF-261: Plan dengan client Expired tetap tidak bisa di-Delete setelah di-Archive

18. Buka tab Custom sub-tab Archive pada Plans List
19. Verifikasi Kolom Clients baris `Guard Expired` di sub-tab Archive bernilai `1` (historical count)
20. Buka Overlay Row Action `Guard Expired`
21. Verifikasi Overlay Row Action hanya memuat `Detail`
22. Tutup Overlay Row Action

### TC-AC-PF-263: Row action Delete tidak tersedia pada plan Active di kedua tab

23. Buka tab Default sub-tab Active pada Plans List
24. Buka Overlay Row Action `Starter`
25. Verifikasi Overlay Row Action `Starter` tidak memuat `Delete`
26. Tutup Overlay Row Action
27. Buka tab Custom sub-tab Active pada Plans List
28. Buka Overlay Row Action `Growth Tier`
29. Verifikasi Overlay Row Action `Growth Tier` tidak memuat `Delete`
30. Tutup Overlay Row Action

### TC-AC-PF-607: Cancel pada dialog Delete Plan default plan

31. Buka tab Default sub-tab Archive pada Plans List
32. Catat jumlah entri Changelog tab Default sebagai baseline
33. Buka Overlay Row Action `Plan Arsip Lama`, lalu klik `Delete`
34. Verifikasi Dialog tampil dengan Title `Delete Plan`; Body bullet • Plan Arsip Lama; teks "This action is permanent and cannot be undone. The plan will be removed; its change history stays in the log."; teks "Are you sure you want to delete it?"; tombol `[Cancel]` dan `[Delete]` (danger)
35. Klik `[Cancel]`
36. Verifikasi Dialog tertutup
37. Verifikasi Tidak ada toast
38. Verifikasi `Plan Arsip Lama` tetap di Default > Archive
39. Klik ikon Changelog pada toolbar tab Default
40. Verifikasi Modal Changelog tab Default tampil dengan entri sebelumnya (anchor)
41. Verifikasi Jumlah entri Changelog tab Default sama dengan baseline langkah 32 (tidak ada entri baru Delete)
42. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, menutup overlay Row Action dan dialog dengan `[Cancel]` agar blok berikutnya dapat berjalan, mencatat baseline jumlah entri Changelog Default sebelum aksi pada TC-AC-PF-607, dan menutup modal Changelog.
- Asersi "tidak ada entri Changelog baru" pada TC-AC-PF-607 ditulis di spec ini sebagai `Verifikasi` berbaseline (S-05, S-12) dengan anchor modal Changelog yang menampilkan entri sebelumnya; tidak dirujuk ke spec absence karena aksinya (dialog pada plan tertentu) dibangun oleh langkah sebelumnya di spec ini. Butir `P-1` (state berat): konteks dialog dan data plan tidak dapat dilepas dari spec ini tanpa mengulang seluruh persiapan.
- Keenam blok berkelas fungsional dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah melampaui 35 langkah karena tiap Expected punya `Verifikasi` sendiri (S-01) dan tiap blok membuka tab atau sub-tab sesuai precondition TC.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-260 langkah 2 tidak menyebut cara membuka Plan Detail; spec memakai klik Plan Name pada baris `Growth Plus (old)`.
