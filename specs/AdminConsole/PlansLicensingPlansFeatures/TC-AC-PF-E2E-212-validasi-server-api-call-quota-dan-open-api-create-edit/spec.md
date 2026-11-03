---
id: TC-AC-PF-E2E-212-validasi-server-api-call-quota-dan-open-api-create-edit
title: "Defense-in-depth: Validasi Server API Call Quota dan Open API pada Create dan Edit Plan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-578
  - TC-AC-PF-659
  - TC-AC-PF-755
  - TC-AC-PF-759
  - TC-AC-PF-760
  - TC-AC-PF-761
coverage:
  web: automated
---

# Defense-in-depth: Validasi Server API Call Quota dan Open API pada Create dan Edit Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec; request langsung memakai sesi API akun #1.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21; default `Growth` v5 dengan Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month; custom `Growth Tier` v20) dan Dataset Plan S (Pre-setup #31; default SAMS `Supply Starter` Free v1 dan `Supply Pro` Paid v1, Clients 0, slot Paid tersisa).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): jumlah custom plan, jumlah default plan SAMS, Version `Growth` dan `Growth Tier`, jumlah entri Changelog Default (`N_log_default`), dan jumlah entri Changelog Custom (`N_log_custom`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `Growth Tier`) dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #1, fixture BE untuk membaca state akhir (daftar plan, Version, dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-578: API call quota selain `—` dengan Open API OFF ditolak server pada Create custom plan

1. Kirim permintaan buat custom plan FAMS dengan Template `Growth`, Plan Name `Paket Quota Off {runId}-212`, Open API OFF, dan API call quota `1M/month` langsung ke server
2. Verifikasi permintaan ditolak dengan pesan "API call quota requires Open API to be enabled."
3. Verifikasi (dibaca lewat fixture BE) tidak ada plan baru: jumlah custom plan sama dengan baseline
4. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Create baru)

### TC-AC-PF-659: API call quota selain `—` dengan Open API OFF ditolak server pada Edit custom plan

5. Kirim permintaan ubah `Growth Tier` dengan Open API OFF dan API call quota `1M/month` langsung ke server
6. Verifikasi permintaan ditolak dengan pesan "API call quota requires Open API to be enabled."
7. Verifikasi (dibaca lewat fixture BE) Version `Growth Tier` tetap `v20`
8. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Edit baru)

### TC-AC-PF-755: API call quota selain `—` dengan Open API OFF ditolak server pada Create default plan

9. Kirim permintaan buat default plan SAMS Paid dengan Plan Name `Supply Quota Off {runId}-212`, Open API OFF, dan API call quota `1M/month` langsung ke server
10. Verifikasi permintaan ditolak dengan pesan "API call quota requires Open API to be enabled."
11. Verifikasi (dibaca lewat fixture BE) tidak ada default plan baru: nama dan jumlah default plan SAMS sama dengan baseline
12. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Create baru)

### TC-AC-PF-759: API call quota selain `—` dengan Open API OFF ditolak server pada Edit default plan

13. Kirim permintaan ubah default plan `Growth` dengan Open API OFF dan API call quota `1M/month` langsung ke server
14. Verifikasi permintaan ditolak dengan pesan "API call quota requires Open API to be enabled."
15. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`
16. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Edit baru)

### TC-AC-PF-760: Open API ON dengan API call quota kosong ditolak server pada Create custom plan lewat permintaan langsung

17. Kirim permintaan buat custom plan FAMS dengan Template `Growth`, Plan Name `Paket Quota Kosong {runId}-212`, Open API ON, dan API call quota `—` langsung ke server
18. Verifikasi permintaan ditolak dengan pesan yang sama dengan form: `API call quota must not be empty`
19. Verifikasi (dibaca lewat fixture BE) tidak ada custom plan baru: jumlah custom plan sama dengan baseline
20. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Create baru)

### TC-AC-PF-761: Open API ON dengan API call quota kosong ditolak server pada Edit default plan lewat permintaan langsung

21. Kirim permintaan ubah default plan `Growth` dengan Open API ON dan API call quota `—` langsung ke server
22. Verifikasi permintaan ditolak dengan pesan yang sama dengan form: `API call quota must not be empty`
23. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`
24. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Edit baru)

## Notes

- K-1: keenam TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC yang mengamati tab, kolom Version, daftar plan, dan ikon Changelog lewat UI dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "Changelog tidak memuat entri baru" diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Plan Name pada request TC-AC-PF-578, TC-AC-PF-755, dan TC-AC-PF-760 memakai nama bersuffix `{runId}-212` (S-12) karena request tidak boleh membuat plan.
- Temuan untuk QA:
  - TC-AC-PF-578, TC-AC-PF-755, dan TC-AC-PF-760: Plan Name pada request tidak disebut; spec memakai nama bersuffix.
  - TC-AC-PF-760: Expected menyebut "pesan yang sama dengan form" tanpa menuliskan pesan; spec memakai `API call quota must not be empty` sesuai kutipan di Expected TC.
