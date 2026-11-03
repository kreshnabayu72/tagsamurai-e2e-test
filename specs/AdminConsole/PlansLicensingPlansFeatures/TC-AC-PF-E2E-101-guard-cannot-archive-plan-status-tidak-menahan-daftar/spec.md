---
id: TC-AC-PF-E2E-101-guard-cannot-archive-plan-status-tidak-menahan-daftar
title: "Guard Cannot Archive Plan: Status yang Tidak Menahan, Daftar Banyak Client, dan Dialog Backdrop"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-250
  - TC-AC-PF-251
  - TC-AC-PF-252
  - TC-AC-PF-706
coverage:
  web: automated
---

# Guard Cannot Archive Plan: Status yang Tidak Menahan, Daftar Banyak Client, dan Dialog Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan G (Pre-setup #27): custom plan Principal `Guard Expired` (client Expired), `Guard Archive` (client Archive), `Guard Purge` (client Purge), `Guard Banyak` (25 client Active `PT Klien 01` sampai `PT Klien 25`), `Guard Campuran` (PT Campur A Active, PT Campur B Waiting for Approval, PT Campur C Pending), `Guard Active` (client `PT Guard Active` Active). Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan G) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: TC-AC-PF-250 mengarsipkan `Guard Expired`, `Guard Archive`, dan `Guard Purge` (Last Modified berubah, tiga entri Archive di Changelog Custom) dan dipulihkan sesudahnya. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

1. Buka tab Custom sub-tab Active pada Plans List

### TC-AC-PF-252: Jumlah client di dialog Cannot Archive Plan dapat lebih besar dari kolom Clients

2. Verifikasi Kolom Clients baris `Guard Campuran` bernilai `1`
3. Buka Overlay Row Action `Guard Campuran`, lalu klik `Archive`
4. Verifikasi Dialog menampilkan "This plan is currently assigned to 3 clients:" dan bullet • PT Campur A, • PT Campur B, • PT Campur C
5. Klik `[OK]`

### TC-AC-PF-251: Dialog Cannot Archive Plan untuk banyak client

6. Buka Overlay Row Action `Guard Banyak`, lalu klik `Archive`
7. Verifikasi Dialog memuat teks "This plan is currently assigned to 25 clients:" dan teks "Reassign or archive those clients first."
8. Gulir daftar client di dalam dialog sampai akhir
9. Verifikasi Daftar bullet • PT Klien 01 sampai • PT Klien 25 berurutan A-Z di container scrollable
10. Verifikasi Tidak ada baris ringkasan sisa jumlah client (daftar tidak dipotong dan tidak diringkas)
11. Klik `[OK]`

### TC-AC-PF-706: Dialog Cannot Archive Plan, klik backdrop diabaikan dan Esc menutup dialog

12. Catat jumlah entri Changelog tab Custom sebagai baseline
13. Buka Overlay Row Action `Guard Active`, lalu klik `Archive`
14. Verifikasi Dialog `Cannot Archive Plan` tampil
15. Klik area gelap di luar dialog
16. Verifikasi Dialog tidak tertutup
17. Tekan Esc
18. Verifikasi Dialog tertutup
19. Verifikasi Tidak ada toast
20. Verifikasi `Guard Active` tetap di sub-tab Active
21. Klik ikon Changelog pada toolbar tab Custom
22. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
23. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 12 (tidak ada entri baru Archive)
24. Tutup modal Changelog

### TC-AC-PF-250: Subscription Expired, Archive, dan Purge tidak menahan Archive plan

25. Buka Overlay Row Action `Guard Expired`, lalu klik `Archive`
26. Klik `[Archive]`
27. Verifikasi Toast sukses: "Success, plan has been archived." untuk `Guard Expired`
28. Verifikasi Dialog `Cannot Archive Plan` tidak muncul untuk `Guard Expired`
29. Buka Overlay Row Action `Guard Archive`, lalu klik `Archive`
30. Klik `[Archive]`
31. Verifikasi Toast sukses: "Success, plan has been archived." untuk `Guard Archive`
32. Verifikasi Dialog `Cannot Archive Plan` tidak muncul untuk `Guard Archive`
33. Buka Overlay Row Action `Guard Purge`, lalu klik `Archive`
34. Klik `[Archive]`
35. Verifikasi Toast sukses: "Success, plan has been archived." untuk `Guard Purge`
36. Verifikasi Dialog `Cannot Archive Plan` tidak muncul untuk `Guard Purge`
37. Klik sub-tab Archive
38. Verifikasi `Guard Expired`, `Guard Archive`, dan `Guard Purge` ada di sub-tab Archive

## Notes

- Urutan blok diubah dari urutan nomor TC: TC-AC-PF-250 ditempatkan terakhir karena mengubah data (Archive tiga plan), sedangkan TC-AC-PF-252, TC-AC-PF-251, dan TC-AC-PF-706 hanya membaca dan membatalkan dialog.
- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, mencatat baseline jumlah entri Changelog Custom sebelum aksi pada TC-AC-PF-706, menutup dialog `Cannot Archive Plan` dengan `[OK]` agar blok berikutnya dapat berjalan, menutup modal Changelog, dan memulihkan Dataset Plan G.
- Asersi "tidak ada entri Changelog baru" pada TC-AC-PF-706 ditulis di spec ini sebagai `Verifikasi` berbaseline (S-05, S-12) dengan anchor modal Changelog yang menampilkan entri sebelumnya; tidak dirujuk ke spec absence karena aksinya (dialog pada plan tertentu) dibangun oleh langkah sebelumnya di spec ini. Butir `P-1` (state berat): konteks dialog dan data plan tidak dapat dilepas dari spec ini tanpa mengulang seluruh persiapan.
- Keempat blok berkelas fungsional dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah melampaui 35 langkah karena tiap Expected punya `Verifikasi` sendiri (S-01).
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-250 Expected butir b (ketiga plan berada di sub-tab Archive) tidak menyebut cara mencari ketiga plan di sub-tab Archive; spec memverifikasinya langsung pada daftar tanpa Search (R-16).
