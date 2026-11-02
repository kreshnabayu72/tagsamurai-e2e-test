---
id: TC-AC-SU-E2E-080-user-list-sidebar-group-digabung-search-dan-filter
title: "User List Sidebar Group: Filter Node Beserta Descendant, Digabung dengan Search dan Filter, dan Collapse Persisten"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-283
  - TC-AC-SU-284
  - TC-AC-SU-285
coverage:
  web: automated
---

# User List Sidebar Group: Filter Node Beserta Descendant, Digabung dengan Search dan Filter, dan Collapse Persisten

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Group tree milik spec (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-080`): `Region A {runId}-080` > `Branch 1 {runId}-080` > `Floor 1 {runId}-080`; `Region A {runId}-080` > `Branch 3 {runId}-080`; `Region B {runId}-080`.
- Data Dinamis (nama bersuffix `{runId}-080`): `Jane Smith {runId}-080` (Group Role aktif di `Floor 1 {runId}-080`; Inactive), `Mike Tan {runId}-080` (Group Role aktif di `Branch 3 {runId}-080`; Active), `John Doe {runId}-080` (Group Role aktif di `Region B {runId}-080`), `Rudi Hartono {runId}-080` (hanya Global Role), `Dewi Lestari {runId}-080` dan `Rina Putri {runId}-080` (Total Control), `Dedi Kurnia {runId}-080` (Group Manager `Region A {runId}-080`), `Andi Wijaya {runId}-080` (Read Only). Baris Default User Principal (Pre-setup #1, Total Control permanen) dipakai apa adanya.
- Status Active/Inactive TC-284 ("Jane Smith OFF, Mike Tan ON") dipetakan ke Status user `Jane Smith {runId}-080` Inactive dan `Mike Tan {runId}-080` Active.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### TC-AC-SU-283: Sidebar Group memfilter node beserta seluruh descendant (3 level)

1. Amati Sidebar Group
2. Verifikasi tree group entitas tampil di sisi kanan
3. Verifikasi arrow collapse/expand tampil per node
4. Klik node `Region A {runId}-080`
5. Verifikasi node `Region A {runId}-080` highlighted
6. Verifikasi tabel menampilkan `Jane Smith {runId}-080` (cucu `Floor 1 {runId}-080`), `Mike Tan {runId}-080` (`Branch 3 {runId}-080`), `Dedi Kurnia {runId}-080` (GM), `Dewi Lestari {runId}-080` (TC), `Rina Putri {runId}-080` (TC), `Andi Wijaya {runId}-080` (RO), dan Default User
7. Verifikasi baris `John Doe {runId}-080` dan `Rudi Hartono {runId}-080` tidak tampil
8. Klik node `Floor 1 {runId}-080`
9. Verifikasi node `Floor 1 {runId}-080` highlighted
10. Verifikasi tabel menampilkan `Jane Smith {runId}-080`, `Dedi Kurnia {runId}-080` (GM `Region A {runId}-080`, wewenang mewaris ke `Floor 1 {runId}-080`), Default User, `Dewi Lestari {runId}-080` (TC), `Rina Putri {runId}-080` (TC), dan `Andi Wijaya {runId}-080` (RO)
11. Verifikasi baris `Mike Tan {runId}-080` (`Branch 3 {runId}-080` bukan descendant `Floor 1 {runId}-080`), `John Doe {runId}-080`, dan `Rudi Hartono {runId}-080` tidak tampil
12. Klik node `Floor 1 {runId}-080` lagi
13. Verifikasi node ter-deselect
14. Verifikasi seluruh baris tampil (baris `John Doe {runId}-080`, `Mike Tan {runId}-080`, dan `Rudi Hartono {runId}-080` tampil)

### TC-AC-SU-284: Sidebar Group digabung dengan Filter Panel dan Search

15. Klik node `Region A {runId}-080`
16. Klik icon Filter
17. Pilih Status `Active`, klik `[Apply]`
18. Verifikasi tabel menampilkan irisan Region A dan Active: baris `Mike Tan {runId}-080` tampil
19. Verifikasi baris `Jane Smith {runId}-080` (Inactive) tidak tampil
20. Klik icon Search
21. Ketik Search `mike`, tekan Enter
22. Verifikasi baris `Mike Tan {runId}-080` tampil
23. Verifikasi baris `Dewi Lestari {runId}-080` tidak tampil
24. Klik `(←)` pada kotak Search
25. Klik `[Clear Field]`, klik `[Apply]`
26. Klik node `Region A {runId}-080` agar ter-deselect

### TC-AC-SU-285: Collapse Sidebar Group persisten

27. Klik toggle collapse Sidebar Group
28. Verifikasi sidebar ter-collapse
29. Tekan F5
30. Verifikasi sidebar tetap collapse
31. Klik toggle collapse Sidebar Group agar sidebar terbuka kembali

## Notes

- Langkah penghubung (S-03): menutup Search, `[Clear Field]` lalu `[Apply]`, men-deselect node, dan membuka kembali sidebar di akhir TC memulihkan state (S-09); state collapse tersimpan di browser sehingga pemulihan eksplisit diperlukan.
- TC-283 dan TC-285 mempunyai TC kembar topik di spec lain (TC-26 dan TC-28 di bagian 1 TC); tiap TC tetap di spec masing-masing. TC-283 memakai assignment yang sama dengan TC-26.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-080` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-284 Data Uji menulis "Jane Smith OFF di Floor 1, Mike Tan ON di Branch 3", padahal NC-06 menyatakan Group Role tidak punya switch; spec memetakan OFF/ON ke Status user Inactive/Active supaya irisan `Region A ∩ Active` bermakna.
  - TC-283 Data Uji menyebut Sarah Lee tidak ada (berbeda dengan TC-26); spec mengikuti Data Uji TC-283.
