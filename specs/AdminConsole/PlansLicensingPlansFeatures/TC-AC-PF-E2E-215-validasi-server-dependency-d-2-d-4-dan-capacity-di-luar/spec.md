---
id: TC-AC-PF-E2E-215-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar
title: "Defense-in-depth: Validasi Server Dependency D-2 dan D-4 serta Nilai Capacity di Luar Daftar Opsi pada Create Default Plan dan Edit Plan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-804
  - TC-AC-PF-805
  - TC-AC-PF-806
coverage:
  web: automated
---

# Defense-in-depth: Validasi Server Dependency D-2 dan D-4 serta Nilai Capacity di Luar Daftar Opsi pada Create Default Plan dan Edit Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec; request langsung memakai sesi API akun #1.
- Data Pre-setup (hook `before`): Dataset Plan S (Pre-setup #31; default SAMS `Supply Starter` Free v1 dan `Supply Pro` Paid v1, slot Paid tersisa) dan Dataset Plan A (Pre-setup #21; default `Growth` v5 dengan Group count 3, Group hierarchy depth 2, License allocation per group ON; custom `Growth Tier` v20).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): jumlah default plan SAMS, Version `Growth` dan `Growth Tier`, jumlah entri Changelog Default (`N_log_default`), dan jumlah entri Changelog Custom (`N_log_custom`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Data uji pada request: Plan Name pada request Create tidak boleh terbentuk sebagai plan; nama memakai suffix `{runId}-215` (S-12).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `Growth Tier`) dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #1, fixture BE untuk membaca state akhir (daftar plan, Version, dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-804: Create Default Plan langsung ke server dengan nilai Capacity di luar daftar opsi ditolak

1. Kirim permintaan buat default plan Product `SAMS`, Pricing Type `Paid`, Plan Name `Supply Opsi Langsung {runId}-215`, Group count `3`, dan Group hierarchy depth `3` langsung ke server
2. Verifikasi permintaan dengan Group count `3` dan Group hierarchy depth `3` ditolak server tanpa copy modul
3. Kirim permintaan buat default plan Product `SAMS`, Pricing Type `Paid`, Plan Name `Supply Opsi Langsung {runId}-215`, dan Category count `7` langsung ke server
4. Verifikasi permintaan dengan Category count `7` ditolak server tanpa copy modul
5. Verifikasi (dibaca lewat fixture BE) `Supply Opsi Langsung {runId}-215` tidak ada di Default > Active
6. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Create untuk `Supply Opsi Langsung {runId}-215`)

### TC-AC-PF-805: Edit Default Plan dan Edit Custom Plan langsung ke server dengan dependency D-2 atau D-4 dilanggar ditolak tanpa koreksi otomatis

7. Kirim permintaan ubah default plan `Growth` dengan Group count `1`, Group hierarchy depth `2`, dan License allocation per group OFF langsung ke server
8. Verifikasi permintaan ubah `Growth` dengan Group hierarchy depth `2` ditolak server tanpa copy modul
9. Kirim permintaan ubah default plan `Growth` dengan Group count `1`, Group hierarchy depth `1`, dan License allocation per group ON langsung ke server
10. Verifikasi permintaan ubah `Growth` dengan License allocation per group ON ditolak server tanpa copy modul
11. Kirim permintaan ubah custom plan `Growth Tier` dengan Group count `1`, Group hierarchy depth `2`, dan License allocation per group OFF langsung ke server
12. Verifikasi permintaan ubah `Growth Tier` dengan Group hierarchy depth `2` ditolak server tanpa copy modul
13. Kirim permintaan ubah custom plan `Growth Tier` dengan Group count `1`, Group hierarchy depth `1`, dan License allocation per group ON langsung ke server
14. Verifikasi permintaan ubah `Growth Tier` dengan License allocation per group ON ditolak server tanpa copy modul
15. Verifikasi server tidak mengoreksi nilai secara otomatis: respons keempat permintaan tidak memuat plan dengan nilai yang dikoreksi
16. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`
17. Verifikasi (dibaca lewat fixture BE) Version `Growth Tier` tetap `v20`
18. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Edit baru untuk `Growth`)
19. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Edit baru untuk `Growth Tier`)

### TC-AC-PF-806: Edit Default Plan dan Edit Custom Plan langsung ke server dengan nilai Capacity di luar daftar opsi ditolak

20. Kirim permintaan ubah default plan `Growth` dengan Group count `2` langsung ke server
21. Verifikasi permintaan ubah `Growth` dengan Group count `2` ditolak server tanpa copy modul
22. Kirim permintaan ubah custom plan `Growth Tier` dengan Asset Name cap `100` langsung ke server
23. Verifikasi permintaan ubah `Growth Tier` dengan Asset Name cap `100` ditolak server tanpa copy modul
24. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`
25. Verifikasi (dibaca lewat fixture BE) Version `Growth Tier` tetap `v20`
26. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Edit baru untuk `Growth`)
27. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Edit baru untuk `Growth Tier`)

## Notes

- K-1: ketiga TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC yang membuka tab Default dan Custom, mengamati kolom Version, dan klik ikon Changelog dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "tidak memuat entri Create atau Edit baru" diasersi sebagai jumlah entri sama dengan baseline dan nama bersuffix unik (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Plan Name pada request Create memakai nama bersuffix `{runId}-215` (S-12) sebagai ganti `Supply Opsi Langsung`.
- Temuan untuk QA:
  - TC-AC-PF-805: Expected a "server tidak mengoreksi nilai secara otomatis" hanya teramati dari isi respons dan Version yang tidak naik; tidak ada nilai plan lain yang disebut untuk dibandingkan.
  - TC-AC-PF-804: nilai field lain pada request (selain yang disebut) tidak disebut.
