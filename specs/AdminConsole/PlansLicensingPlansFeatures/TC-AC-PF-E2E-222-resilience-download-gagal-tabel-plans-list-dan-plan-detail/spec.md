---
id: TC-AC-PF-E2E-222-resilience-download-gagal-tabel-plans-list-dan-plan-detail
title: "Resilience: Download Gagal pada Tabel Default, Tabel Custom, dan Plan Detail: Toast Error dengan Nama Berkas"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-356
  - TC-AC-PF-407
  - TC-AC-PF-606
coverage:
  web: automated
---

# Resilience: Download Gagal pada Tabel Default, Tabel Custom, dan Plan Detail: Toast Error dengan Nama Berkas

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience (kegagalan ekspor; isi berkas tidak diuji di spec ini).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21; default `Starter` v2 dan plan lain) dan Dataset Plan C (Pre-setup #23; custom plan Principal aktif `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`, semuanya Paid). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Starter`) dipakai sebagai plan yang dibuka; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons Download yang dijawab gagal (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC), dilepas segera setelah pemicu (S-09); pembacaan daftar berkas terunduh browser untuk memastikan tidak ada berkas terunduh; sesi API aktor.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-356: Download tab Default Active gagal: toast error dengan nama berkas tanpa ekstensi

1. Pasang intercept: respons Download dijawab gagal
2. Klik ikon Download → `Download as CSV`
3. Lepas intercept
4. Verifikasi muncul toast error: "Error, failed to download Plans-Features-Default."
5. Verifikasi toast error tetap tampil setelah 6 detik tanpa di-dismiss
6. Verifikasi tidak ada berkas terunduh
7. Dismiss toast error

### TC-AC-PF-407: Download tab Custom Active gagal: toast error dengan nama berkas tanpa ekstensi

8. Klik tab Custom
9. Pasang intercept: respons Download dijawab gagal
10. Klik ikon Download → `Download as CSV`
11. Lepas intercept
12. Verifikasi muncul toast error: "Error, failed to download Plans-Features-Custom."
13. Verifikasi toast error tetap tampil setelah 6 detik tanpa di-dismiss
14. Verifikasi tidak ada berkas terunduh
15. Dismiss toast error

### TC-AC-PF-606: Download Plan Detail gagal: toast error dengan nama berkas tanpa ekstensi

16. Klik tab Default
17. Klik teks `Starter` pada kolom Plan Name sehingga Plan Detail `Starter` terbuka
18. Pasang intercept: respons Download dijawab gagal
19. Klik ikon Download → `Download as CSV`
20. Lepas intercept
21. Verifikasi muncul toast error: "Error, failed to download Plan-Detail-Starter."
22. Verifikasi toast error tetap tampil setelah 6 detik tanpa di-dismiss
23. Verifikasi tidak ada berkas terunduh
24. Dismiss toast error

## Notes

- Langkah penghubung (S-03): langkah 7, 15, dan 24 meng-dismiss toast error agar asersi toast berikutnya bukan toast lama (R-12); langkah 8 dan 16 mengarahkan layar ke tab yang disyaratkan precondition.
- TC-AC-PF-606 menyatakan toast error "yang tetap tampil sampai di-dismiss" dan "tidak ada berkas terunduh" sebagai butir a dan b; keduanya ditulis sebagai `Verifikasi` terpisah (langkah 22 dan 23).
- Temuan untuk QA:
  - TC-AC-PF-356, TC-AC-PF-407, dan TC-AC-PF-606: lamanya "tetap tampil sampai di-dismiss" tidak disebut; spec memakai 6 detik (lebih lama dari 4 detik toast sukses pada TC-AC-PF-600) sebagai pilihan spec.
  - TC-AC-PF-606: precondition menempatkan user di Default > Active tetapi langkah 1 membuka Plan Detail `Starter`; spec mengikuti langkah TC.
