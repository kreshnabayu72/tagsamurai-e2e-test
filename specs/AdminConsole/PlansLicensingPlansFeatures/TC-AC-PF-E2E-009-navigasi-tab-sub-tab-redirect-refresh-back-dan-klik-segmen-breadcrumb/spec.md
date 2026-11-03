---
id: TC-AC-PF-E2E-009-navigasi-tab-sub-tab-redirect-refresh-back-dan-klik-segmen-breadcrumb
title: "Navigasi Tab dan Sub-tab: Redirect, Refresh, Back, State Sub-tab, dan Klik Segmen Breadcrumb"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-36
  - TC-AC-PF-37
  - TC-AC-PF-38
  - TC-AC-PF-39
  - TC-AC-PF-612
coverage:
  web: automated
---

# Navigasi Tab dan Sub-tab: Redirect, Refresh, Back, State Sub-tab, dan Klik Segmen Breadcrumb

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21: default `Growth` aktif, `Growth Plus (old)` archived, custom `Growth Tier` dan `Enterprise Reseller`), Dataset Plan R (Pre-setup #30: `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru` archived, Clients 0). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`) dipakai sebagai kata kunci Search; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: kontrol tombol Back browser dan F5; fixture BE (pemulihan Dataset Pre-setup) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-36: Halaman Plans & Features tanpa segmen tab dialihkan ke Default > Active

1. Pindah ke halaman lain di Admin Console lewat sidebar (menu selain Plans & Licensing > Plans & Features)
2. Klik menu Plans & Licensing > Plans & Features di sidebar
3. Verifikasi halaman diarahkan ke Plans & Licensing > Plans & Features > Default > Active
4. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Default > Active`

### TC-AC-PF-37: Pindah tab dan sub-tab mengubah breadcrumb dan mendorong riwayat browser sehingga Back kembali ke tab sebelumnya

5. Klik tab Custom
6. Klik sub-tab Archive
7. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Custom > Archive`
8. Klik tab Global Settings
9. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Global Settings`
10. Klik tombol Back browser satu kali
11. Verifikasi halaman kembali ke Plans & Licensing > Plans & Features > Custom > Archive
12. Klik tombol Back browser satu kali lagi
13. Verifikasi halaman kembali ke Plans & Licensing > Plans & Features > Custom > Active

### TC-AC-PF-38: Refresh halaman pada tab dan sub-tab tertentu memuat tab dan sub-tab yang sama

14. Klik sub-tab Archive
15. Tekan F5
16. Verifikasi halaman tetap Plans & Licensing > Plans & Features > Custom > Archive dengan sub-tab Archive aktif
17. Verifikasi halaman tidak kembali ke Default > Active

### TC-AC-PF-39: Pindah sub-tab lalu kembali memulihkan Search dan Sort sub-tab sebelumnya, state tiap sub-tab tidak dibagi

18. Klik menu Plans & Licensing > Plans & Features di sidebar
19. Ketik Search `Growth`, tekan Enter di sub-tab Active
20. Klik header kolom Version satu kali (ascending)
21. Klik sub-tab Archive
22. Verifikasi kotak Search di sub-tab Archive tertutup
23. Verifikasi tabel sub-tab Archive tidak tersaring (baris `Growth Plus (old)`, `Plan Arsip Baru`, `Plan Arsip Tengah`, dan `Plan Arsip Lama` tampil)
24. Verifikasi tidak ada sort aktif di sub-tab Archive
25. Klik sub-tab Active
26. Verifikasi Search `Growth` masih terpasang di sub-tab Active
27. Verifikasi Sort Version ascending masih aktif di sub-tab Active

### TC-AC-PF-612: Klik segmen breadcrumb pada halaman list: Plans & Licensing statis, Plans & Features, Default, dan Custom membuka tab pada sub-tab default

28. Klik menu Plans & Licensing > Plans & Features di sidebar
29. Klik tab Custom
30. Klik sub-tab Archive
31. Klik segmen `Plans & Licensing` pada breadcrumb
32. Klik segmen terakhir `Archive` pada breadcrumb
33. Verifikasi halaman tetap Plans & Licensing > Plans & Features > Custom > Archive (segmen pertama dan terakhir statis)
34. Klik segmen `Custom` pada breadcrumb
35. Verifikasi halaman Plans & Licensing > Plans & Features > Custom > Active terbuka
36. Klik sub-tab Archive
37. Klik segmen `Plans & Features` pada breadcrumb
38. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active terbuka
39. Klik tab Default
40. Klik sub-tab Archive
41. Klik segmen `Default` pada breadcrumb
42. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active terbuka

## Notes

- Langkah penghubung (S-03): langkah 5, 14, 18, 28, 29, 30, 36, 39, dan 40 mengarahkan layar ke tab, sub-tab, atau list awal yang disyaratkan precondition TC; langkah 1 memenuhi precondition TC-AC-PF-36 ("User berada di halaman lain di Admin Console").
- Pembersihan state (S-09): Search dan Sort yang dipasang langkah 19 dan 20 direset oleh klik menu sidebar pada langkah 28.
- Alasan di atas sekitar 35 langkah (42 langkah): seluruh blok memeriksa satu topik, navigasi tab, sub-tab, dan breadcrumb pada halaman Plans & Features, dengan kelas harness yang sama (fungsional FE+BE) dan dataset yang sama; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Expected dipecah satu `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - TC-AC-PF-36: precondition "halaman lain di Admin Console" tidak menyebut halaman tertentu; spec memakai menu sidebar mana pun selain Plans & Features (langkah 1).
