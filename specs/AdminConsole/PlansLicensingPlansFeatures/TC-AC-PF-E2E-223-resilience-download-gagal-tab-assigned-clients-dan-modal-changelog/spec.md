---
id: TC-AC-PF-E2E-223-resilience-download-gagal-tab-assigned-clients-dan-modal-changelog
title: "Resilience: Download Gagal pada Tab Assigned Clients dan Modal Changelog: Toast Error dengan Nama Berkas"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-450
  - TC-AC-PF-492
  - TC-AC-PF-518
coverage:
  web: automated
---

# Resilience: Download Gagal pada Tab Assigned Clients dan Modal Changelog: Toast Error dengan Nama Berkas

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience (kegagalan ekspor; isi berkas tidak diuji di spec ini).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan D (Pre-setup #24; default `Growth` v5 dengan 9 client), Dataset Log D (Pre-setup #40; Changelog Default 5 entri), dan Dataset Log G (Pre-setup #42; Changelog Global Settings 5 entri). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`) dipakai sebagai plan yang dibuka; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons Download yang dijawab gagal (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC), dilepas segera setelah pemicu (S-09); pembacaan daftar berkas terunduh browser untuk memastikan tidak ada berkas terunduh; sesi API aktor.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-450: Download Tab Assigned Clients gagal: toast error dengan nama berkas tanpa ekstensi

1. Klik teks `Growth` pada kolom Plan Name sehingga Plan Detail `Growth` terbuka
2. Klik Tab Assigned Clients
3. Pasang intercept: respons Download dijawab gagal
4. Klik ikon Download → `Download as CSV`
5. Lepas intercept
6. Verifikasi muncul toast error: "Error, failed to download Assigned-Clients-Growth."
7. Verifikasi toast error tetap tampil setelah 6 detik tanpa di-dismiss
8. Verifikasi tidak ada berkas terunduh
9. Dismiss toast error

### TC-AC-PF-492: Download modal Changelog Default gagal: toast error dengan nama berkas tanpa ekstensi

10. Klik segmen Breadcrumb `Plans & Features`
11. Klik ikon Changelog pada toolbar tab Default
12. Pasang intercept: respons Download dijawab gagal
13. Klik ikon Download → `Download as CSV`
14. Lepas intercept
15. Verifikasi muncul toast error: "Error, failed to download Changelog-Plans-Features-Default."
16. Verifikasi toast error tetap tampil setelah 6 detik tanpa di-dismiss
17. Verifikasi tidak ada berkas terunduh
18. Dismiss toast error
19. Tutup modal Changelog lewat `✕`

### TC-AC-PF-518: Download modal Changelog Global Settings gagal menampilkan toast error dengan nama berkas

20. Klik tab Global Settings
21. Klik ikon Changelog di pojok kanan atas Card
22. Pasang intercept: respons Download dijawab gagal
23. Klik ikon Download → `Download as CSV`
24. Lepas intercept
25. Verifikasi muncul toast error: "Error, failed to download Changelog-Plans-Features-Global-Settings."
26. Dismiss toast error
27. Tutup modal Changelog lewat `✕`

## Notes

- Langkah penghubung (S-03): langkah 9, 18, dan 26 meng-dismiss toast error agar asersi toast berikutnya bukan toast lama (R-12); langkah 10 mengembalikan layar ke list tab Default; langkah 20 mengarahkan layar ke tab Global Settings; langkah 19 dan 27 menutup modal.
- TC-AC-PF-518 hanya memuat asersi toast error; tidak ada asersi toast bertahan atau berkas terunduh pada blok itu.
- Temuan untuk QA:
  - TC-AC-PF-450 dan TC-AC-PF-492: lamanya "tetap tampil sampai di-dismiss" tidak disebut; spec memakai 6 detik (lebih lama dari 4 detik toast sukses pada TC-AC-PF-600) sebagai pilihan spec.
  - TC-AC-PF-518: precondition menempatkan user di Default > Active padahal langkah dimulai dari tab Global Settings; spec mengikuti langkah TC.
