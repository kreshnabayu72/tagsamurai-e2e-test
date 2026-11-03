---
id: TC-AC-PF-E2E-109-dialog-push-plan-update-screening-tabel-diff-cancel
title: "Dialog Push Plan Update: Screening, Tabel Diff, Cancel, Backdrop, dan Esc"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-275
  - TC-AC-PF-276
  - TC-AC-PF-277
  - TC-AC-PF-705
coverage:
  web: automated
---

# Dialog Push Plan Update: Screening, Tabel Diff, Cancel, Backdrop, dan Esc

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Dataset Plan P: custom plan Principal `Paket Push` v3 (v1 Group count 3, Open API OFF; v2 Group count 25; v3 Open API ON dan API call quota 100K/month) dengan client PT Push Satu Active v1, PT Push Dua Active v2, PT Push Tiga Grace v1, PT Push Empat Expired v1, PT Push Lima Active v3, PT Push Waiting Waiting for Approval v1, PT Push Pending Pending v1, PT Push Arsip Archive v1, PT Push Purge Purge v1. Dataset hanya dibaca dan dibatalkan; tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan P) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: tidak ada perubahan data karena seluruh Push Update dibatalkan; Changelog tidak berubah. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-275: Screening dialog Push Plan Update

1. Buka tab Custom sub-tab Active pada Plans List
2. Buka Plan Detail `Paket Push`
3. Klik Tab Assigned Clients
4. Buka Overlay Row Action `PT Push Dua`, lalu klik `Push Update`
5. Verifikasi Dialog (Dialog Size MD) tampil dengan Title `Push Plan Update`; bullet • PT Push Dua; teks "This client will be updated from v2 to v3."; teks "Are you sure you want to push this update?"
6. Verifikasi Tabel diff berjudul `What's changing` dengan kolom `Field`, `Old Value`, `New Value`
7. Verifikasi Tabel diff memuat baris `Open API` | `No` | `Yes`
8. Verifikasi Tabel diff memuat baris `API call quota` | `—` | `100K/month`
9. Verifikasi Footer dialog memuat `[Cancel]` dan `[Push Update]` (primary)
10. Klik `[Cancel]`

### TC-AC-PF-276: Tabel diff menggabungkan efek net per field untuk client yang tertinggal lebih dari satu versi

11. Buka Overlay Row Action `PT Push Satu`, lalu klik `Push Update`
12. Verifikasi Dialog memuat teks "This client will be updated from v1 to v3."
13. Verifikasi Tabel diff memuat satu baris per field yang berbeda secara net: `Group count` | `3` | `25`; `Open API` | `No` | `Yes`; `API call quota` | `—` | `100K/month` (bukan dua batch terpisah per versi)
14. Klik `[Cancel]`

### TC-AC-PF-277: Cancel pada dialog Push Plan Update

15. Catat jumlah entri Changelog tab Custom sebagai baseline
16. Buka Overlay Row Action `PT Push Dua`, lalu klik `Push Update`
17. Klik `[Cancel]`
18. Verifikasi Dialog tertutup
19. Verifikasi Tidak ada toast
20. Verifikasi Kolom Plan Version `PT Push Dua` tetap `v2` berbadge `Outdated`
21. Kembali ke Plans List tab Custom sub-tab Active
22. Klik ikon Changelog pada toolbar tab Custom
23. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
24. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 15 (tidak ada entri baru Push Update)
25. Tutup modal Changelog

### TC-AC-PF-705: Dialog Push Plan Update, klik backdrop diabaikan dan Esc setara Cancel

26. Catat jumlah entri Changelog tab Custom sebagai baseline
27. Buka Plan Detail `Paket Push`
28. Klik Tab Assigned Clients
29. Buka Overlay Row Action `PT Push Dua`, lalu klik `Push Update`
30. Klik area gelap di luar dialog
31. Verifikasi Dialog tidak tertutup
32. Tekan Esc
33. Verifikasi Dialog tertutup seperti `[Cancel]`
34. Verifikasi Tidak ada toast
35. Verifikasi Kolom Plan Version `PT Push Dua` tetap `v2` berbadge `Outdated`
36. Kembali ke Plans List tab Custom sub-tab Active
37. Klik ikon Changelog pada toolbar tab Custom
38. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
39. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 26 (tidak ada entri baru Push Update)
40. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, menutup dialog dengan `[Cancel]` agar blok berikutnya dapat berjalan, mencatat baseline jumlah entri Changelog Custom sebelum aksi, kembali ke Plans List, dan menutup modal Changelog.
- Asersi "tidak ada entri Changelog baru" pada TC-AC-PF-277 dan TC-AC-PF-705 ditulis di spec ini sebagai `Verifikasi` berbaseline (S-05, S-12) dengan anchor modal Changelog yang menampilkan entri sebelumnya; tidak dirujuk ke spec absence karena aksinya (dialog pada plan tertentu) dibangun oleh langkah sebelumnya di spec ini. Butir `P-1` (state berat): konteks dialog dan data plan tidak dapat dilepas dari spec ini tanpa mengulang seluruh persiapan.
- Keempat blok berkelas fungsional dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah melampaui 35 langkah karena tiap Expected punya `Verifikasi` sendiri (S-01).
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
