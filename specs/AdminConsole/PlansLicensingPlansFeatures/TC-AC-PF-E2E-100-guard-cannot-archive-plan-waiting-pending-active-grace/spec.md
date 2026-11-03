---
id: TC-AC-PF-E2E-100-guard-cannot-archive-plan-waiting-pending-active-grace
title: "Guard Cannot Archive Plan: Subscription Waiting for Approval, Pending, Active, dan Grace"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-246
  - TC-AC-PF-247
  - TC-AC-PF-248
  - TC-AC-PF-249
coverage:
  web: automated
---

# Guard Cannot Archive Plan: Subscription Waiting for Approval, Pending, Active, dan Grace

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan G (Pre-setup #27): custom plan Principal `Guard Waiting` (client `PT Guard Waiting` Waiting for Approval), `Guard Pending` (`PT Guard Pending` Pending), `Guard Active` (`PT Guard Active` Active), `Guard Grace` (`PT Guard Grace` Grace). Dataset hanya dibaca dan dibatalkan; tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan G) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: tidak ada perubahan data karena seluruh Archive ditolak guard; Changelog tidak berubah. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

1. Buka tab Custom sub-tab Active pada Plans List
2. Catat jumlah entri Changelog tab Custom sebagai baseline

### TC-AC-PF-246: Archive custom plan dengan subscription berstatus Waiting for Approval diblokir

3. Buka Overlay Row Action `Guard Waiting`, lalu klik `Archive`
4. Verifikasi Dialog tampil dengan Title `Cannot Archive Plan`; bullet • Guard Waiting; teks "This plan is currently assigned to 1 client:"; bullet • PT Guard Waiting; teks "Reassign or archive that client first."; tombol `[OK]` saja
5. Klik `[OK]`
6. Verifikasi Dialog tertutup
7. Verifikasi `Guard Waiting` tetap di sub-tab Active
8. Klik ikon Changelog pada toolbar tab Custom
9. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
10. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 2 (tidak ada entri baru Archive)
11. Tutup modal Changelog

### TC-AC-PF-247: Archive custom plan dengan subscription berstatus Pending diblokir

12. Buka Overlay Row Action `Guard Pending`, lalu klik `Archive`
13. Verifikasi Dialog tampil dengan Title `Cannot Archive Plan`; bullet • Guard Pending; teks "This plan is currently assigned to 1 client:"; bullet • PT Guard Pending; teks "Reassign or archive that client first."; tombol `[OK]` saja
14. Klik `[OK]`
15. Verifikasi Dialog tertutup
16. Verifikasi `Guard Pending` tetap di sub-tab Active
17. Klik ikon Changelog pada toolbar tab Custom
18. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
19. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 2 (tidak ada entri baru Archive)
20. Tutup modal Changelog

### TC-AC-PF-248: Archive custom plan dengan subscription berstatus Active diblokir

21. Buka Overlay Row Action `Guard Active`, lalu klik `Archive`
22. Verifikasi Dialog tampil dengan Title `Cannot Archive Plan`; bullet • Guard Active; teks "This plan is currently assigned to 1 client:"; bullet • PT Guard Active; teks "Reassign or archive that client first."; tombol `[OK]` saja
23. Klik `[OK]`
24. Verifikasi Dialog tertutup
25. Verifikasi `Guard Active` tetap di sub-tab Active
26. Klik ikon Changelog pada toolbar tab Custom
27. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
28. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 2 (tidak ada entri baru Archive)
29. Tutup modal Changelog

### TC-AC-PF-249: Archive custom plan dengan subscription berstatus Grace diblokir

30. Buka Overlay Row Action `Guard Grace`, lalu klik `Archive`
31. Verifikasi Dialog tampil dengan Title `Cannot Archive Plan`; bullet • Guard Grace; teks "This plan is currently assigned to 1 client:"; bullet • PT Guard Grace; teks "Reassign or archive that client first."; tombol `[OK]` saja
32. Klik `[OK]`
33. Verifikasi Dialog tertutup
34. Verifikasi `Guard Grace` tetap di sub-tab Active
35. Klik ikon Changelog pada toolbar tab Custom
36. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
37. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 2 (tidak ada entri baru Archive)
38. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab sebagai precondition TC, mencatat baseline jumlah entri Changelog Custom sekali sebelum aksi pertama (tidak ada blok yang menambah entri), dan menutup modal Changelog.
- Asersi "tidak ada entri Changelog baru" pada TC-AC-PF-246 sampai TC-AC-PF-249 ditulis di spec ini sebagai `Verifikasi` berbaseline (S-05, S-12) dengan anchor modal Changelog yang menampilkan entri sebelumnya; tidak dirujuk ke spec absence karena aksinya (dialog pada plan tertentu) dibangun oleh langkah sebelumnya di spec ini. Butir `P-1` (state berat): konteks dialog dan data plan tidak dapat dilepas dari spec ini tanpa mengulang seluruh persiapan.
- Keempat blok berkelas fungsional dengan langkah yang sama dan data berbeda; jumlah langkah sedikit di atas 35 langkah karena tiap Expected punya `Verifikasi` sendiri (S-01) dan keempatnya berdiri sendiri.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
