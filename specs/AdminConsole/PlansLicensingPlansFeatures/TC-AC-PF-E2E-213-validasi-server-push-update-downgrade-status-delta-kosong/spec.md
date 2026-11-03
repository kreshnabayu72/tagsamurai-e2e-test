---
id: TC-AC-PF-E2E-213-validasi-server-push-update-downgrade-status-delta-kosong
title: "Defense-in-depth: Validasi Server Push Update: Downgrade, Status Non-Eligible, Delta Kosong, Client Expired, dan Term Trial"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-584
  - TC-AC-PF-585
  - TC-AC-PF-586
  - TC-AC-PF-655
  - TC-AC-PF-786
coverage:
  web: automated
---

# Defense-in-depth: Validasi Server Push Update: Downgrade, Status Non-Eligible, Delta Kosong, Client Expired, dan Term Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec; request langsung memakai sesi API akun #1.
- Data Pre-setup (hook `before`): Dataset Plan P (Pre-setup #28): `Paket Turun` v3 dengan `PT Turun Satu` Active v1 (net delta mengandung penurunan); `Paket Push` v3 dengan `PT Push Waiting` (Waiting for Approval v1) dan `PT Push Arsip` (Archive v1); `Paket Revert` v3 dengan `PT Revert Satu` Active v1 (delta net kosong); `Paket Push Exp` dengan `PT Push Exp` (Client Expired dengan term non-Trial Expired v1, diterapkan lewat fixture BE; plan sudah memiliki versi terbaru lebih tinggi dari v1; aksi Push Update Hidden di UI untuk baris ini sehingga hanya request langsung yang menjangkaunya). Dataset Plan TR (Pre-setup #59, diterapkan lewat fixture BE): custom plan `Paket Trial` v2 dengan `PT Trial Aktif` (term Trial Active v1), `PT Trial Habis` (term Trial Expired v1), dan `PT Trial Menunggu` (term Trial Waiting for Approval v1); seluruh delta v1 ke v2 upgrade murni.
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): Plan Version tiap client yang menjadi target dan jumlah entri Changelog Custom (`N_log_custom`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan dan client Pre-setup literal tanpa suffix dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset (termasuk state client Expired dan term Trial) lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #1, fixture BE untuk membaca state akhir (Plan Version client dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-584: Push Update untuk client dengan delta downgrade ditolak server, versi client tidak berubah

1. Kirim permintaan Push Update untuk `PT Turun Satu` langsung ke server
2. Verifikasi server menolak permintaan (upgrade-only)
3. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Turun Satu` tetap `v1`
4. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom`

### TC-AC-PF-585: Push Update untuk subscription berstatus selain Active dan Grace ditolak server

5. Kirim permintaan Push Update untuk `PT Push Waiting` langsung ke server
6. Verifikasi permintaan untuk `PT Push Waiting` ditolak server
7. Kirim permintaan Push Update untuk `PT Push Arsip` langsung ke server
8. Verifikasi permintaan untuk `PT Push Arsip` ditolak server
9. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Push Waiting` tetap `v1`
10. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Push Arsip` tetap `v1`
11. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom`

### TC-AC-PF-586: Push Update untuk client dengan delta net kosong diperlakukan seperti client versi terbaru: tanpa perubahan dan tanpa log

12. Kirim permintaan Push Update untuk `PT Revert Satu` langsung ke server
13. Verifikasi respons server tidak berisi pesan error baru
14. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Revert Satu` tetap `v1`
15. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom`

### TC-AC-PF-655: Push Update langsung ke client yang workspace-nya Expired ditolak server, versi tidak berubah, dan tanpa entri log

16. Kirim permintaan Push Update untuk `PT Push Exp` langsung ke server
17. Verifikasi server menolak permintaan sebagai akses ditolak (forbidden) karena workspace client Expired
18. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Push Exp` tetap `v1`
19. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Push Update untuk `PT Push Exp`)

### TC-AC-PF-786: Push Update langsung ke term Trial berstatus Active, Expired, dan Waiting for Approval ditolak server tanpa copy modul

20. Kirim permintaan Push Update untuk `PT Trial Aktif` langsung ke server
21. Verifikasi permintaan untuk `PT Trial Aktif` ditolak server tanpa copy modul
22. Kirim permintaan Push Update untuk `PT Trial Habis` langsung ke server
23. Verifikasi permintaan untuk `PT Trial Habis` ditolak server tanpa copy modul
24. Kirim permintaan Push Update untuk `PT Trial Menunggu` langsung ke server
25. Verifikasi permintaan untuk `PT Trial Menunggu` ditolak server tanpa copy modul
26. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Trial Aktif` tetap `v1`
27. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Trial Habis` tetap `v1`
28. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Trial Menunggu` tetap `v1`
29. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom` (tidak ada entri Push Update untuk ketiga client)

## Notes

- K-1: kelima TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`. TC-AC-PF-655 dan TC-AC-PF-786 menyentuh state tenant (kelas h) hanya sebagai pemicu yang dibentuk lewat fixture BE (P-2).
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC yang membuka Plan Detail Tab Assigned Clients, mengamati Plan Version, dan klik ikon Changelog dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "tidak ada entri Changelog" diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Temuan untuk QA:
  - TC-AC-PF-586: Expected "Server tidak mengubah apa pun ... tanpa pesan error baru" tidak menyebut kode status respons (sukses no-op atau lainnya); spec hanya mengasersi respons tanpa pesan error.
  - TC-AC-PF-585 dan TC-AC-PF-584: Expected "ditolak" tidak menyebut pesan atau kode; hanya penolakan yang diasersi.
  - TC-AC-PF-655: precondition menyebut plan "sudah memiliki versi terbaru lebih tinggi dari v1" tanpa menyebut nomor versi; spec hanya mengasersi Plan Version client tetap `v1`.
