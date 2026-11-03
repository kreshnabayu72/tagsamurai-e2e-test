---
id: TC-AC-PF-E2E-096-dialog-archive-plan-screening-dan-cancel-custom-dan-default
title: "Dialog Archive Plan: Screening dan Cancel pada Custom Plan dan Default Plan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-237
  - TC-AC-PF-238
  - TC-AC-PF-239
coverage:
  web: automated
---

# Dialog Archive Plan: Screening dan Cancel pada Custom Plan dan Default Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: custom plan Principal `Paket Tanpa Client` aktif tanpa subscription (Dataset Plan G, Pre-setup #27); Dataset Plan Y (Pre-setup #37): default FAMS tanpa subscription Starter (Free), Growth, Professional, Enterprise (Paid tier 1, 2, 3). Dataset hanya dibaca dan dibatalkan; tidak ada data Dinamis. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Custom dan tab Default. Changelog adalah audit trail permanen sehingga jumlahnya tidak dapat diturunkan dari seeding (bagian 8b butir 10); jumlah dicatat sebelum aksi sebagai baseline dan asersi memakai selisih terhadapnya (S-12).
- State global: suite serial (`parallel: false`). Spec ini memakai data Pre-setup bersama (Dataset Plan G dan Dataset Plan Y) sebagai data uji (nama literal dan, bila ada, target aksi tulis), pengecualian S-06/S-12 butir A-14: seeding idempoten (dilewati bila sudah ada) dan pemulihan semua Dataset yang disentuh ke keadaan awal lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: tidak ada perubahan data karena seluruh aksi dibatalkan; Last Modified dan Changelog tidak berubah. Entri Changelog bersifat permanen dan tidak dapat dihapus lewat UI.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nama data Pre-setup pada langkah mengikuti Tabel Data Uji TC dan dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.

## Test Steps

### TC-AC-PF-237: Screening dialog Archive Plan pada custom plan

1. Buka tab Custom sub-tab Active pada Plans List
2. Buka Overlay Row Action `Paket Tanpa Client`, lalu klik `Archive`
3. Verifikasi Dialog Popup Konfirmasi tampil dengan Title `Archive Plan`; Body bullet • Paket Tanpa Client; teks "This plan will no longer be available for new assignments."; teks "Are you sure you want to archive it?"; tombol `[Cancel]` dan `[Archive]`
4. Klik area gelap di luar dialog
5. Verifikasi Dialog `Archive Plan` tidak tertutup
6. Tekan Esc
7. Verifikasi Dialog `Archive Plan` tertutup seperti `[Cancel]`
8. Verifikasi `Paket Tanpa Client` tetap Active di sub-tab Active

### TC-AC-PF-238: Cancel pada dialog Archive Plan custom plan

9. Catat jumlah entri Changelog tab Custom sebagai baseline
10. Buka Overlay Row Action `Paket Tanpa Client`, lalu klik `Archive`
11. Klik `[Cancel]`
12. Verifikasi Dialog tertutup
13. Verifikasi Tidak ada toast
14. Verifikasi `Paket Tanpa Client` tetap di sub-tab Active
15. Klik ikon Changelog pada toolbar tab Custom
16. Verifikasi Modal Changelog tab Custom tampil dengan entri sebelumnya (anchor)
17. Verifikasi Jumlah entri Changelog tab Custom sama dengan baseline langkah 9 (tidak ada entri baru Archive)
18. Tutup modal Changelog

### TC-AC-PF-239: Cancel pada dialog Archive Plan default plan

19. Buka tab Default sub-tab Active pada Plans List
20. Catat jumlah entri Changelog tab Default sebagai baseline
21. Buka Overlay Row Action `Enterprise`, lalu klik `Archive`
22. Klik `[Cancel]`
23. Verifikasi Dialog tertutup
24. Verifikasi Tidak ada toast
25. Verifikasi `Enterprise` tetap di sub-tab Active
26. Klik ikon Changelog pada toolbar tab Default
27. Verifikasi Modal Changelog tab Default tampil dengan entri sebelumnya (anchor)
28. Verifikasi Jumlah entri Changelog tab Default sama dengan baseline langkah 20 (tidak ada entri baru Archive)
29. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): membuka tab dan sub-tab Plans List sebagai precondition TC, menutup modal Changelog, dan mencatat baseline jumlah entri Changelog sebelum aksi.
- Asersi "tidak ada entri Changelog baru" pada TC-AC-PF-238 dan TC-AC-PF-239 ditulis di spec ini sebagai `Verifikasi` berbaseline (S-05, S-12) dengan anchor modal Changelog yang menampilkan entri sebelumnya; tidak dirujuk ke spec absence karena aksinya (dialog pada plan tertentu) dibangun oleh langkah sebelumnya di spec ini. Butir `P-1` (state berat): konteks dialog dan data plan tidak dapat dilepas dari spec ini tanpa mengulang seluruh persiapan.
- Temuan untuk QA: TC tidak menyatakan cara membaca jumlah entri Changelog untuk asersi "tidak ada entri baru" atau "tepat satu entri". Spec memakai baseline jumlah entri yang dibaca lewat kemampuan baca yang disediakan tim FE/BE (bagian 8b butir 10), tanpa endpoint karangan.
- Temuan untuk QA: TC-AC-PF-237 langkah 3 menggabungkan klik area gelap dan Esc; spec memisahkannya menjadi dua aksi berurutan dengan `Verifikasi` masing-masing (Expected butir b memuat dua klausa).
