---
id: TC-AC-PF-E2E-211-validasi-server-template-plan-archived-delete-belum
title: "Defense-in-depth: Validasi Server Template Custom Plan, Edit Plan Archived, Delete Plan Belum Archived atau Pernah Dipakai"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-579
  - TC-AC-PF-580
  - TC-AC-PF-581
  - TC-AC-PF-582
  - TC-AC-PF-583
  - TC-AC-PF-800
coverage:
  web: automated
---

# Defense-in-depth: Validasi Server Template Custom Plan, Edit Plan Archived, Delete Plan Belum Archived atau Pernah Dipakai

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec; request langsung memakai sesi API akun #1.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21; default aktif `Starter` v2, `Growth` v5, `Professional`, `Enterprise`, `SIEM`; default archived `Growth Plus (old)` v3 dengan historical Clients 31) dan Dataset Plan TM (Pre-setup #50, diterapkan lewat fixture BE: custom plan `Paket Terminal Arsip` archived v1 dirujuk empat client berterm terminal selain Deleted; `PT Arsip Deleted` terhapus permanen sehingga Clients bernilai `4`; aksi Delete Hidden di UI untuk plan itu sehingga hanya request langsung yang menjangkaunya).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): jumlah custom plan, Version `Growth Plus (old)`, `Starter`, dan `Paket Terminal Arsip`, jumlah entri Changelog Default (`N_log_default`), dan jumlah entri Changelog Custom (`N_log_custom`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Starter`, `Growth Plus (old)`, `Paket Terminal Arsip`) dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #1, fixture BE untuk membaca state akhir (daftar plan, Version, Clients, dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-579: Template default plan Free untuk Create Custom Plan ditolak server

1. Kirim permintaan buat custom plan FAMS dengan Template `Starter` (Free) dan Plan Name `Paket Template Free {runId}-211` langsung ke server
2. Verifikasi server menolak dengan pesan "The template must be a paid default plan"
3. Verifikasi (dibaca lewat fixture BE) tidak ada plan baru: jumlah custom plan sama dengan baseline
4. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom`

### TC-AC-PF-580: Template yang archived atau milik Product lain untuk Create Custom Plan ditolak server

5. Kirim permintaan buat custom plan FAMS dengan Template `Growth Plus (old)` (archived) dan Plan Name `Paket Template Arsip {runId}-211` langsung ke server
6. Verifikasi permintaan dengan Template archived ditolak server
7. Kirim permintaan buat custom plan FAMS dengan Template `SIEM` (Product lain) dan Plan Name `Paket Template Siem {runId}-211` langsung ke server
8. Verifikasi permintaan dengan Template Product lain ditolak server
9. Verifikasi (dibaca lewat fixture BE) tidak ada plan baru: jumlah custom plan sama dengan baseline
10. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom`

### TC-AC-PF-581: Edit plan berstatus archived ditolak server tanpa mengubah data, versi, dan log

11. Kirim permintaan ubah Group count `Growth Plus (old)` menjadi `25` langsung ke server
12. Verifikasi server menolak permintaan
13. Verifikasi (dibaca lewat fixture BE) data `Growth Plus (old)` tidak berubah: Group count sama dengan baseline
14. Verifikasi (dibaca lewat fixture BE) Version `Growth Plus (old)` tetap `v3`
15. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-582: Delete plan yang belum archived ditolak server

16. Kirim permintaan delete default plan aktif `Starter` langsung ke server
17. Verifikasi server menolak permintaan
18. Verifikasi (dibaca lewat fixture BE) `Starter` tetap Active di sub-tab Active default plan
19. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-583: Delete plan archived yang pernah dipakai subscription ditolak server dan hanya Archive yang diizinkan

20. Kirim permintaan delete `Growth Plus (old)` langsung ke server
21. Verifikasi server menolak permintaan
22. Verifikasi (dibaca lewat fixture BE) `Growth Plus (old)` dan seluruh snapshot versinya tetap ada
23. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-800: Delete langsung plan archived yang masih dirujuk subscription non-Deleted ditolak server meski sebagian term-nya berstatus Deleted

24. Kirim permintaan Delete untuk `Paket Terminal Arsip` langsung ke server
25. Verifikasi permintaan ditolak server tanpa copy modul
26. Verifikasi (dibaca lewat fixture BE) `Paket Terminal Arsip` masih ada di Custom > Archive
27. Verifikasi (dibaca lewat fixture BE) Version `Paket Terminal Arsip` tetap `v1`
28. Verifikasi (dibaca lewat fixture BE) Clients `Paket Terminal Arsip` tetap `4`
29. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Delete untuk `Paket Terminal Arsip`)

## Notes

- K-1: keenam TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC yang mengamati tab, kolom Version, dan ikon Changelog lewat UI dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "tidak ada entri Changelog" diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Plan Name pada request TC-AC-PF-579 dan TC-AC-PF-580 memakai nama bersuffix `{runId}-211` (S-12) karena request tidak boleh membuat plan.
- Temuan untuk QA:
  - TC-AC-PF-579 dan TC-AC-PF-580: Plan Name pada request tidak disebut; spec memakai nama bersuffix.
  - TC-AC-PF-581: nilai Group count pada request tidak disebut; spec memakai `25`.
  - TC-AC-PF-580: Expected tidak menyebut pesan penolakan; hanya penolakan yang diasersi.
  - TC-AC-PF-583: judul menyebut "hanya Archive yang diizinkan", tetapi Expected tidak memuat asersi untuk Archive; tidak ada langkah Archive di spec ini.
