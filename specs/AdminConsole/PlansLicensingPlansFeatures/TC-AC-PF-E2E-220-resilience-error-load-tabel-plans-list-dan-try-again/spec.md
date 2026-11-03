---
id: TC-AC-PF-E2E-220-resilience-error-load-tabel-plans-list-dan-try-again
title: "Resilience: Error Load Tabel Plans List pada Empat Sub-tab dan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-18
  - TC-AC-PF-681
  - TC-AC-PF-682
  - TC-AC-PF-683
coverage:
  web: automated
---

# Resilience: Error Load Tabel Plans List pada Empat Sub-tab dan Try Again

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21; default aktif `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`; default archived `Growth Plus (old)`; custom archived `Enterprise Reseller`) dan Dataset Plan C (Pre-setup #23; custom plan Principal aktif `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix dipakai sebagai baris yang diasersi; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons daftar plan yang dijawab server error (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC), dilepas segera setelah pemicu (S-09); sesi API aktor.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-18: Error load tabel Plans List tampil sebagai error state dan Try Again memuat ulang data

1. Pasang intercept: respons daftar plan dijawab server error
2. Tekan F5 sehingga daftar plan gagal dimuat
3. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
4. Verifikasi area tabel bukan empty state
5. Lepas intercept
6. Klik `[Try Again]`
7. Verifikasi baris Dataset Plan A tampil (`Starter`, `Growth`)

### TC-AC-PF-681: Error load tabel Plans List tab Custom sub-tab Active tampil sebagai error state dan Try Again memuat ulang data

8. Pasang intercept: respons daftar plan dijawab server error
9. Klik tab Custom
10. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
11. Verifikasi area tabel bukan empty state
12. Lepas intercept
13. Klik `[Try Again]`
14. Verifikasi baris plan tampil (`alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`)

### TC-AC-PF-682: Error load tabel Plans List tab Default sub-tab Archive tampil sebagai error state dan Try Again memuat ulang data

15. Klik tab Default
16. Pasang intercept: respons daftar plan dijawab server error
17. Klik sub-tab Archive
18. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
19. Verifikasi area tabel bukan empty state
20. Lepas intercept
21. Klik `[Try Again]`
22. Verifikasi baris plan tampil (`Growth Plus (old)`)

### TC-AC-PF-683: Error load tabel Plans List tab Custom sub-tab Archive tampil sebagai error state dan Try Again memuat ulang data

23. Klik tab Custom
24. Klik sub-tab Active
25. Pasang intercept: respons daftar plan dijawab server error
26. Klik sub-tab Archive
27. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
28. Verifikasi area tabel bukan empty state
29. Lepas intercept
30. Klik `[Try Again]`
31. Verifikasi baris plan tampil (`Enterprise Reseller`)

## Notes

- Langkah penghubung (S-03): langkah 15 mengembalikan layar ke tab Default sesuai precondition TC-AC-PF-682; langkah 23 dan 24 mengarahkan layar ke tab Custom sub-tab Active sesuai precondition TC-AC-PF-683.
- TC-AC-PF-18 tidak menyebut tab dan sub-tab yang dimuat ulang; spec memakai Default > Active sesuai precondition.
- Asersi "bukan empty state" (langkah 4, 11, 19, 28) memakai tampilnya `Unable to load this data.` pada area tabel yang sama sebagai anchor positif (langkah 3, 10, 18, 27).
- Temuan untuk QA:
  - TC-AC-PF-681 dan TC-AC-PF-682: titik awal precondition (Default > Active) tidak sama dengan tab yang dimuat gagal (Custom, sub-tab Archive); spec mengikuti langkah TC.
  - TC-AC-PF-18, TC-AC-PF-681, TC-AC-PF-682, dan TC-AC-PF-683: Expected setelah Try Again hanya menyebut "baris tampil"; spec mengasersi nama baris yang disebut Dataset pada precondition.
