---
id: TC-AC-PF-E2E-022-aksesibilitas-focus-trap-dialog-archive-delete-dan-cannot-archive-plan
title: "Aksesibilitas: Focus Trap Dialog Archive Plan, Delete Plan, dan Cannot Archive Plan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-794
  - TC-AC-PF-795
coverage:
  web: automated
---

# Aksesibilitas: Focus Trap Dialog Archive Plan, Delete Plan, dan Cannot Archive Plan

## Prerequisites

- Mode: FE+BE (hanya membuka dialog, menekan Tab, dan membatalkan; TC bertanda UI Only, tanpa intercept dan tanpa perubahan data).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan Y (Pre-setup #37: default FAMS tanpa subscription: Starter Free, Growth, Professional, Enterprise Paid), Dataset Plan C (Pre-setup #23: custom archived `Arsip Custom Satu` tidak pernah dipakai), Dataset Plan G (Pre-setup #27: custom `Guard Active` dipakai satu client `PT Guard Active` berstatus Active). Dataset Plan Y menggantikan default plan Dataset Plan A selama spec ini berjalan karena slot Free dan Paid per Product terbatas. Spec hanya membatalkan dialog sehingga data dan Last Updated tidak berubah. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `Arsip Custom Satu`, `Guard Active`) dipakai sebagai target dialog yang selalu dibatalkan; spec tidak mengubahnya.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: pengiriman tombol keyboard Tab dan Shift+Tab serta pembacaan elemen yang sedang fokus, fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-794: Focus trap dialog Archive Plan dan dialog Delete Plan: fokus terkunci di dalam dialog selama terbuka

1. Buka Overlay Row Action `Growth`, klik `Archive` sehingga dialog `Archive Plan` terbuka
2. Tekan Tab berulang kali hingga fokus mencapai kontrol fokus terakhir di dalam dialog, lalu tekan Tab satu kali lagi
3. Verifikasi fokus hanya berpindah di antara kontrol di dalam dialog `Archive Plan` dan tidak pernah berpindah ke halaman Plans List di belakang dialog
4. Verifikasi setelah kontrol fokus terakhir, Tab berikutnya menuju kontrol fokus pertama di dalam dialog `Archive Plan`
5. Tekan Shift+Tab pada kontrol fokus pertama di dalam dialog
6. Verifikasi fokus menuju kontrol fokus terakhir di dalam dialog `Archive Plan`
7. Klik `[Cancel]`
8. Verifikasi dialog `Archive Plan` tertutup
9. Verifikasi `Growth` tetap Active
10. Klik tab Custom, lalu klik sub-tab Archive
11. Buka Overlay Row Action `Arsip Custom Satu`, klik `Delete` sehingga dialog `Delete Plan` terbuka
12. Tekan Tab berulang kali hingga fokus mencapai kontrol fokus terakhir di dalam dialog, lalu tekan Tab satu kali lagi
13. Verifikasi fokus hanya berpindah di antara kontrol di dalam dialog `Delete Plan` dan tidak pernah berpindah ke halaman Plans List di belakang dialog
14. Verifikasi setelah kontrol fokus terakhir, Tab berikutnya menuju kontrol fokus pertama di dalam dialog `Delete Plan`
15. Tekan Shift+Tab pada kontrol fokus pertama di dalam dialog
16. Verifikasi fokus menuju kontrol fokus terakhir di dalam dialog `Delete Plan`
17. Klik `[Cancel]`
18. Verifikasi dialog `Delete Plan` tertutup
19. Verifikasi `Arsip Custom Satu` tetap ada di sub-tab Archive

### TC-AC-PF-795: Focus trap dialog Cannot Archive Plan: fokus tetap di dalam dialog selama terbuka

20. Klik sub-tab Active
21. Buka Overlay Row Action `Guard Active`, klik `Archive` sehingga dialog `Cannot Archive Plan` terbuka
22. Tekan Tab berulang kali, termasuk satu kali setelah fokus mencapai tombol `[OK]`
23. Verifikasi fokus hanya berpindah di antara kontrol di dalam dialog (termasuk tombol `[OK]`) dan tidak pernah berpindah ke halaman Plans List di belakang dialog
24. Tekan Shift+Tab pada kontrol fokus pertama di dalam dialog
25. Verifikasi fokus tetap di dalam dialog
26. Klik `[OK]`
27. Verifikasi dialog `Cannot Archive Plan` tertutup
28. Verifikasi `Guard Active` tetap Active

## Notes

- Langkah penghubung (S-03): klik tab dan sub-tab pada langkah 10 dan 20 mengarahkan layar ke tab yang disyaratkan precondition TC; langkah 11 sampai 19 ditulis eksplisit tanpa "ulangi langkah" (S-04).
- Temuan untuk QA:
  - TC-AC-PF-795: langkah TC hanya "klik `Archive`" lalu menekan Tab pada dialog `Cannot Archive Plan`, sedangkan TC-AC-PF-593 dan Dataset Plan G menunjukkan dialog blok muncul sesudah `[Archive]` pada dialog `Archive Plan`. Spec mengikuti langkah TC (dialog `Cannot Archive Plan` terbuka setelah klik `Archive`); mohon QA menegaskan apakah ada dialog `Archive Plan` terlebih dahulu.
  - TC-AC-PF-794 dan TC-AC-PF-795: Expected mengasersi posisi fokus tetapi tidak menyebut elemen fokus pertama dan terakhir tiap dialog; spec mengasersi seperti kalimat TC tanpa nama kontrol.
