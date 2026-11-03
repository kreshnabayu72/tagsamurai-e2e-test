---
id: TC-AC-PF-E2E-209-server-menolak-push-update-dan-client-detail-tanpa-izin
title: "Defense-in-depth: Server Menolak Push Update dan Client Detail Tanpa Izin Group, Filter Pricing Type Custom Diabaikan, dan Payload Script pada Plan Name"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-565
  - TC-AC-PF-566
  - TC-AC-PF-568
  - TC-AC-PF-569
coverage:
  web: automated
---

# Defense-in-depth: Server Menolak Push Update dan Client Detail Tanpa Izin Group, Filter Pricing Type Custom Diabaikan, dan Payload Script pada Plan Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group-Mix Principal `groupMixPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #8; Manage plans & licensing: Read dan Update; Group Role Manage active client: Read Only pada group PT Bumi Sentosa dan Zero Access pada group PT Timur Jaya), password dari `Spectra.env.AC_PF_GM_PASSWORD` (TC-AC-PF-565 dan TC-AC-PF-566). Akun kedua: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (TC-AC-PF-568 lewat sesi API, TC-AC-PF-569 lewat ganti akun UI di langkah 17 sampai 19). Kelas harness: a defense-in-depth (request langsung ke server dan injeksi payload script).
- Login akun #8 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Ganti akun ke #1 ada di langkah 17 sampai 19; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hook `before`): Dataset Plan D (Pre-setup #24: default `Growth` v5 dengan 9 client, termasuk `PT Bumi Sentosa` Active v1 dan `PT Timur Jaya` Active v1 dengan delta upgrade, keduanya eligible), Dataset Plan C (Pre-setup #23: custom plan Principal `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max` aktif; `Arsip Custom Satu`, `Arsip Custom Dua` archived; semuanya Paid), dan Dataset Plan A (Pre-setup #21).
- Data dinamis milik spec (TC-AC-PF-569): custom plan `<script>alert(1)</script> {runId}-209` (Product `FAMS`, Template `Growth`); dibuat oleh spec dan dibersihkan (archive lalu delete) lewat fixture BE di hook `after`.
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): Plan Version `PT Bumi Sentosa` dan `PT Timur Jaya` pada `Growth`, jumlah entri Changelog Default (`N_log_default`), dan jumlah custom plan milik Principal pada Dataset Plan C. Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `Growth Tier`) dan nama client Dataset Plan D dipakai sebagai target request yang ditolak atau sasaran baca; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`) untuk akun #8 dan #1; spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- State global: entri Changelog Custom `Create` untuk plan TC-AC-PF-569 bersifat permanen dan tidak dapat dihapus lewat UI.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #8 dan #1, fixture BE untuk membaca state akhir (Plan Version dan jumlah entri Changelog) dan membersihkan plan.
- Env var: `Spectra.env.AC_PF_GM_PASSWORD` dan `Spectra.env.AC_TC_PASSWORD`; `AC_PF_GM_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-565: Push Update ke client di group tanpa izin ditolak server sebagai akses ditolak (forbidden)

1. Kirim permintaan Push Update untuk `PT Bumi Sentosa` langsung ke server dengan sesi API akun Group-Mix
2. Verifikasi permintaan untuk `PT Bumi Sentosa` ditolak server sebagai akses ditolak (forbidden), bukan tidak ditemukan
3. Kirim permintaan Push Update untuk `PT Timur Jaya` langsung ke server dengan sesi API akun Group-Mix
4. Verifikasi permintaan untuk `PT Timur Jaya` ditolak server sebagai akses ditolak (forbidden), bukan tidak ditemukan
5. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Bumi Sentosa` pada `Growth` tetap `v1`
6. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Timur Jaya` pada `Growth` tetap `v1`
7. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-566: Membuka Client Detail dari Tab Assigned Clients untuk group Zero Access ditolak server

8. Klik teks `Growth` pada kolom Plan Name sehingga Plan Detail `Growth` terbuka
9. Klik Tab Assigned Clients
10. Verifikasi baris client `PT Timur Jaya` tampil di Tab Assigned Clients
11. Kirim permintaan buka Client Detail `PT Timur Jaya` langsung ke server dengan sesi API akun Group-Mix
12. Verifikasi server menolak permintaan sebagai akses ditolak (forbidden)

### TC-AC-PF-568: Filter Pricing Type yang dikirim untuk tab Custom diabaikan server tanpa error

13. Kirim permintaan daftar custom plan langsung ke server dengan sesi API akun Principal Total Control dan filter Pricing Type `Free`
14. Verifikasi server mengabaikan filter Pricing Type (no-op): respons memuat custom plan ber-Pricing Type `Paid`
15. Verifikasi respons tidak berisi error
16. Verifikasi respons mengembalikan seluruh custom plan milik entitas Principal sama dengan jumlah Dataset Plan C

### TC-AC-PF-569: Payload script pada Plan Name dirender sebagai teks di list, Plan Detail, dan Changelog

17. Ganti akun: klik Logout
18. Login sebagai Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` dengan password dari `Spectra.env.AC_TC_PASSWORD`
19. Buka Plans & Licensing > Plans & Features
20. Buka form New Custom Plan
21. Pilih Product `FAMS`, pilih Template `Growth`, dan isi Plan Name `<script>alert(1)</script> {runId}-209`
22. Klik `[Submit]`
23. Klik segmen Breadcrumb `Plans & Features`, lalu klik tab Custom
24. Ketik Search `<script>alert(1)</script> {runId}-209`, tekan Enter
25. Verifikasi kolom Plan Name di list tab Custom menampilkan `<script>alert(1)</script> {runId}-209` sebagai teks apa adanya
26. Verifikasi tidak ada script yang dieksekusi
27. Verifikasi tidak ada dialog alert
28. Klik teks `<script>alert(1)</script> {runId}-209` pada kolom Plan Name sehingga Plan Detail terbuka
29. Verifikasi judul Plan Detail menampilkan `<script>alert(1)</script> {runId}-209` sebagai teks apa adanya
30. Klik segmen Breadcrumb `Plans & Features`, lalu klik tab Custom
31. Klik ikon Changelog pada toolbar tab Custom
32. Verifikasi kolom Plan Name entri Changelog Custom menampilkan `<script>alert(1)</script> {runId}-209` sebagai teks apa adanya
33. Tutup modal Changelog lewat `✕`
34. Klik `(←)` pada kotak Search

## Notes

- K-1: TC-AC-PF-565, TC-AC-PF-566, dan TC-AC-PF-568 adalah kelas a dengan Expected berupa respons API; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC-AC-PF-565 "Dengan sesi Principal Total Control buka Plan Detail `Growth` Tab Assigned Clients ... klik ikon Changelog" dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi pada blok itu.
- Expected "tidak ada entri log" (TC-AC-PF-565) diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Langkah penghubung (S-03): langkah 8 dan 9 membawa sesi akun Group-Mix ke Tab Assigned Clients agar baris client yang disebut Expected TC-AC-PF-566 teramati (TC tidak memberi langkahnya); langkah 17 sampai 19 mengganti akun ke Principal Total Control karena TC-AC-PF-569 membuat plan lewat UI; langkah 23 kembali ke Plans List lewat klik segmen Breadcrumb `Plans & Features` dari Plan Detail yang terbuka sesudah `[Submit]`, lalu langkah 23 dan 24 menemukan baris target (R-16); langkah 30 membawa layar ke list tab Custom; langkah 33 menutup modal dan langkah 34 mengosongkan Search. Urutan blok mengikuti TC dan akun yang butuh UI diletakkan di akhir.
- Plan TC-AC-PF-569 memakai nama bersuffix `{runId}-209` (S-12) sebagai ganti `<script>alert(1)</script>` murni agar tidak bentrok antar-run.
- Temuan untuk QA:
  - TC-AC-PF-566: Expected menyebut "walau baris client tampil di tab", tetapi TC hanya memberi langkah request langsung dan tidak memberi langkah membuka tab sebagai Group-Mix; spec menambah langkah 8 sampai 10.
  - TC-AC-PF-568: Dataset Plan C seluruhnya Paid sehingga "mengabaikan filter Free" teramati dari hasil yang tetap memuat plan Paid; Expected tidak menyebut jumlah plan yang dikembalikan.
  - TC-AC-PF-569: batas panjang Plan Name tidak disebut TC; payload dengan suffix `{runId}-209` memanjang sekitar 43 karakter dan dapat melewati batas Plan Name.
