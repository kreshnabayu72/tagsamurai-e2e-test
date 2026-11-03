---
id: TC-AC-PF-E2E-023-aksesibilitas-focus-trap-dialog-push-plan-update-dan-unsaved-changes
title: "Aksesibilitas: Focus Trap Dialog Push Plan Update dan Unsaved Changes"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-796
  - TC-AC-PF-797
coverage:
  web: automated
---

# Aksesibilitas: Focus Trap Dialog Push Plan Update dan Unsaved Changes

## Prerequisites

- Mode: FE+BE (hanya membuka dialog, menekan Tab, dan membatalkan; TC bertanda UI Only, tanpa intercept dan tanpa perubahan data).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan P (Pre-setup #28), bagian yang dipakai: custom plan Principal `Paket Push` v3 dengan `PT Push Dua` Active v2 (eligible Push Update); Dataset Plan A (Pre-setup #21) termasuk default plan `Growth` sebagai Template. Spec hanya membatalkan dialog sehingga versi client dan Last Updated tidak berubah. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Paket Push`, `Growth`) dan client `PT Push Dua` dipakai sebagai target dialog yang selalu dibatalkan; spec tidak mengubahnya.
- Data Dinamis: Plan Name `Paket Fokus {runId}-023` hanya diketik di form dan tidak pernah disimpan.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: pengiriman tombol keyboard Tab, Shift+Tab, dan Esc serta pembacaan elemen yang sedang fokus, fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-796: Focus trap dialog Push Plan Update: fokus terkunci di dalam dialog selama terbuka

1. Klik tab Custom, lalu klik teks `Paket Push` pada kolom Plan Name untuk membuka Plan Detail `Paket Push`
2. Klik Tab Assigned Clients
3. Buka Overlay Row Action `PT Push Dua`, klik `Push Update` sehingga dialog `Push Plan Update` terbuka
4. Tekan Tab berulang kali hingga fokus mencapai kontrol fokus terakhir di dalam dialog, lalu tekan Tab satu kali lagi
5. Verifikasi fokus hanya berpindah di antara kontrol di dalam dialog dan tidak pernah berpindah ke halaman Plan Detail di belakang dialog
6. Verifikasi setelah kontrol fokus terakhir, Tab berikutnya menuju kontrol fokus pertama di dalam dialog
7. Tekan Shift+Tab pada kontrol fokus pertama di dalam dialog
8. Verifikasi fokus menuju kontrol fokus terakhir di dalam dialog
9. Klik `[Cancel]`
10. Verifikasi dialog `Push Plan Update` tertutup
11. Verifikasi versi `PT Push Dua` tetap `v2`

### TC-AC-PF-797: Focus trap dialog Unsaved Changes: fokus terkunci di dalam dialog selama terbuka

12. Klik menu Plans & Licensing > Plans & Features di sidebar, klik tab Custom, lalu klik `+ Custom Plan`
13. Pilih Product `FAMS` dan Template `Growth`, isi Plan Name `Paket Fokus {runId}-023`
14. Tekan Esc sehingga dialog `Unsaved Changes` muncul
15. Verifikasi dialog `Unsaved Changes` tampil
16. Tekan Tab berulang kali hingga fokus mencapai kontrol fokus terakhir di dalam dialog, lalu tekan Tab satu kali lagi
17. Verifikasi fokus hanya berpindah di antara kontrol di dalam dialog dan tidak pernah berpindah ke form di belakang dialog
18. Verifikasi setelah kontrol fokus terakhir, Tab berikutnya menuju kontrol fokus pertama di dalam dialog
19. Tekan Shift+Tab pada kontrol fokus pertama di dalam dialog
20. Verifikasi fokus menuju kontrol fokus terakhir di dalam dialog
21. Klik `[Cancel]`
22. Verifikasi dialog `Unsaved Changes` tertutup
23. Verifikasi user tetap di form dengan input dipertahankan
24. Klik segmen Breadcrumb `Plans & Features`
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): klik tab Custom dan klik menu sidebar pada langkah 1 dan 12 mengarahkan layar ke tab yang disyaratkan precondition TC; langkah 24 sampai 26 menutup form dirty (S-08, S-09).
- Temuan untuk QA:
  - TC-AC-PF-796: TC tidak menyebut kontrol fokus pertama dan terakhir dialog `Push Plan Update` dan tidak menyebut apakah `PT Push Dua` v2 yang ditampilkan dialog sudah eligible; spec mengikuti kalimat TC.
  - TC-AC-PF-797: Expected c "user tetap di form dengan input dipertahankan" tidak menyebut field mana yang diasersi; spec mengasersi seluruh input (Product, Template, Plan Name) tetap terisi.
