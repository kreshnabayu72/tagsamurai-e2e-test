---
id: TC-AC-PF-E2E-214-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar
title: "Defense-in-depth: Validasi Server Dependency D-2 dan D-4 serta Nilai Capacity di Luar Daftar Opsi pada Create Custom Plan dan Create Default Plan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-801
  - TC-AC-PF-802
  - TC-AC-PF-803
coverage:
  web: automated
---

# Defense-in-depth: Validasi Server Dependency D-2 dan D-4 serta Nilai Capacity di Luar Daftar Opsi pada Create Custom Plan dan Create Default Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec; request langsung memakai sesi API akun #1.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21; default `Growth` v5 sebagai Template) dan Dataset Plan S (Pre-setup #31; default SAMS `Supply Starter` Free v1 dan `Supply Pro` Paid v1, slot Paid tersisa).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): jumlah custom plan, jumlah default plan SAMS, jumlah entri Changelog Custom (`N_log_custom`), dan jumlah entri Changelog Default (`N_log_default`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Data uji pada request: Plan Name tidak boleh terbentuk sebagai plan; nama memakai suffix `{runId}-214` (S-12).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`) dipakai sebagai Template request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #1, fixture BE untuk membaca state akhir (daftar plan dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-801: Create Custom Plan langsung ke server dengan dependency D-2 atau D-4 dilanggar ditolak tanpa koreksi otomatis

1. Kirim permintaan buat custom plan FAMS dengan Template `Growth`, Plan Name `Paket Dep Langsung {runId}-214`, Group count `1`, Group hierarchy depth `2`, dan License allocation per group OFF langsung ke server
2. Verifikasi permintaan dengan Group hierarchy depth `2` ditolak server tanpa copy modul
3. Kirim permintaan buat custom plan FAMS dengan Template `Growth`, Plan Name `Paket Dep Langsung {runId}-214`, Group count `1`, Group hierarchy depth `1`, dan License allocation per group ON langsung ke server
4. Verifikasi permintaan dengan License allocation per group ON ditolak server tanpa copy modul
5. Verifikasi respons kedua permintaan tidak memuat plan dengan nilai Group hierarchy depth, License allocation per group, atau Group count yang dikoreksi otomatis
6. Verifikasi (dibaca lewat fixture BE) `Paket Dep Langsung {runId}-214` tidak ada di Custom > Active
7. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Create untuk `Paket Dep Langsung {runId}-214`)

### TC-AC-PF-802: Create Custom Plan langsung ke server dengan nilai Capacity di luar daftar opsi ditolak

8. Kirim permintaan buat custom plan FAMS dengan Template `Growth`, Plan Name `Paket Opsi Langsung {runId}-214`, dan Group count `2` langsung ke server
9. Verifikasi permintaan dengan Group count `2` ditolak server tanpa copy modul
10. Kirim permintaan buat custom plan FAMS dengan Template `Growth`, Plan Name `Paket Opsi Langsung {runId}-214`, dan Asset Name cap `100` langsung ke server
11. Verifikasi permintaan dengan Asset Name cap `100` ditolak server tanpa copy modul
12. Verifikasi (dibaca lewat fixture BE) `Paket Opsi Langsung {runId}-214` tidak ada di Custom > Active
13. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Create untuk `Paket Opsi Langsung {runId}-214`)

### TC-AC-PF-803: Create Default Plan langsung ke server dengan dependency D-2 atau D-4 dilanggar ditolak tanpa koreksi otomatis

14. Kirim permintaan buat default plan Product `SAMS`, Pricing Type `Paid`, Plan Name `Supply Dep Langsung {runId}-214`, Group count `1`, dan Group hierarchy depth `2` langsung ke server
15. Verifikasi permintaan dengan Group hierarchy depth `2` ditolak server tanpa copy modul
16. Kirim permintaan buat default plan Product `SAMS`, Pricing Type `Paid`, Plan Name `Supply Dep Langsung {runId}-214`, Group count `1`, dan License allocation per group ON langsung ke server
17. Verifikasi permintaan dengan License allocation per group ON ditolak server tanpa copy modul
18. Verifikasi respons kedua permintaan tidak memuat plan dengan nilai yang dikoreksi otomatis
19. Verifikasi (dibaca lewat fixture BE) `Supply Dep Langsung {runId}-214` tidak ada di Default > Active
20. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Create untuk `Supply Dep Langsung {runId}-214`)

## Notes

- K-1: ketiga TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC "Buka tab ... dan cari ... klik ikon Changelog ... amati entri terbaru" dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "tidak memuat entri Create" diasersi sebagai jumlah entri sama dengan baseline dan nama bersuffix unik (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Plan Name pada request memakai nama bersuffix `{runId}-214` (S-12) sebagai ganti `Paket Dep Langsung`, `Paket Opsi Langsung`, dan `Supply Dep Langsung`.
- Temuan untuk QA:
  - TC-AC-PF-801 dan TC-AC-PF-803: Expected "server tidak mengoreksi nilai ... secara otomatis" tidak punya state yang dapat diamati selain tidak adanya plan hasil request (Expected b); spec mengasersinya dari isi respons dan dari tidak adanya plan.
  - TC-AC-PF-801 sampai TC-AC-PF-803: nilai field lain pada request (selain yang disebut) tidak disebut; spec mengikuti Template `Growth`.
