---
id: TC-GS-ROLE-E2E-118-absence-log-cancel-dialog-auto-revert-dan-switch-off-baris-sudah-dihapus
title: "Absence Log: Cancel Dialog Auto-Revert dan Switch OFF atas Baris yang Sudah Dihapus Admin Lain Tidak Menulis Entri Baru"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-328
  - TC-GS-ROLE-339
coverage:
  web: automated
---

# Absence Log: Cancel Dialog Auto-Revert dan Switch OFF atas Baris yang Sudah Dihapus Admin Lain Tidak Menulis Entri Baru

## Prerequisites

- Mode: FE+BE. Kelas harness: absence log (kelas g); pemicu TC-339 adalah pelaku kedua lewat sesi API (kelas c sebagai pemicu, `P-5` butir a) dan pemicu TC-328 adalah aksi UI `[Cancel]`. Suite `parallel: false` karena spec mengubah state user Pre-setup bersama.
- Akun Sesi A (UI): Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Akun Sesi B (pemicu, TC-339): Eko Prasetyo (Total Control kedua, Pre-setup #13, Modified By `Eko P`), email disediakan tim FE, kredensial `Spectra.env.GS_TC2_PASSWORD` (terdaftar). Sesi B memakai sesi API karena hanya memicu perubahan state dan tidak ada asersi di Sesi B; cara memperoleh token disediakan tim FE.
- Akun penerima notifikasi (TC-328): Cakra Mahendra (Pre-setup #20), email dan kredensial disediakan tim FE (Tabel Pre-setup TC tidak memuat email; lihat Temuan untuk QA). Login ke akun ini terjadi pada langkah ganti akun di Test Steps; hook `after` memulihkan sesi ke akun default suite.
- Data Pre-setup #20 (fixture switch Active, bernama literal sesuai TC; Access Global Settings dicentang pada kedua user; nilai identitas mengacu fixture `Fixture.role.*` yang dibuat di tahap script, berkas belum ada): `Nadia Rosalina` (Active; baris `Manage files` Active dengan Read dan Delete tercentang) untuk TC-339 dan `Cakra Mahendra` (Active; Total Control dengan keenam baris Active, Given: di-assign Total Control ulang di hook `before`) untuk TC-328.
- Given (hook `before`): kedua user dipastikan berada di state di atas. Mekanisme menyiapkan access level dan baris role per user disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Baseline (dicatat di hook `before` sesudah Given dan sebelum aksi pemicu pertama, S-12; kemampuan membaca total entri dan jumlah notifikasi disediakan tim FE): total entri Changelog Detail `Manage files` hasil Search `Nadia Rosalina` sebagai `B-NF`; total entri Changelog Detail `Manage TAG` hasil Search `Cakra Mahendra` sebagai `B-CM`; jumlah notifikasi pada Overlay Notifikasi `Cakra Mahendra` sebagai `B-CN`.
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): baris `Manage files` `Nadia Rosalina` dibuat ulang Active dengan Read dan Delete tercentang; `Cakra Mahendra` di-assign Total Control ulang bila access level berubah; sesi dipulihkan ke akun default suite. Efek pada Pre-setup: Modified By dan Last Updated berubah; entri log dan notifikasi bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun UI yang dipakai suite, termasuk akun target; spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-339: Switch Active OFF atas baris yang sudah dihapus admin lain menampilkan toast netral

1. [Sesi A] Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Nadia Rosalina`, tekan Enter
2. [Sesi A] Klik Name `Nadia Rosalina`, buka Tab `Role`
3. [Sesi B] Remove baris `Manage files` milik `Nadia Rosalina` lewat sesi API hingga baris terhapus
4. [Sesi A] Matikan switch `Manage files`
5. [Sesi A] Verifikasi toast netral `This role is no longer available.`
6. [Sesi A] Verifikasi data di-refresh dari server
7. [Sesi A] Verifikasi switch `Manage files` `Nadia Rosalina` OFF dengan seluruh checkbox Disabled
8. [Sesi A] Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage files`, klik `Changelog`
9. [Sesi A] Ketik Search `Nadia Rosalina`, tekan Enter
10. [Sesi A] Verifikasi total entri sama dengan `B-NF` + 1
11. [Sesi A] Verifikasi entry baru Action `Remove` untuk `Nadia Rosalina`, Modified By `Eko P` (entry dari Sesi B)
12. [Sesi A] Verifikasi tidak ada entry log dari aksi Sesi A (satu-satunya entry baru adalah entry Sesi B pada langkah 11)
13. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-328: Cancel dialog auto-revert pada switch OFF mengembalikan switch ke ON

14. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Cakra Mahendra`, tekan Enter
15. Klik Name `Cakra Mahendra`, buka Tab `Role`
16. Matikan switch `Manage TAG`
17. Klik `[Cancel]` pada dialog
18. Verifikasi dialog tertutup
19. Verifikasi tidak ada toast
20. Verifikasi switch `Manage TAG` kembali ON
21. Verifikasi banner Total Control tetap tampil
22. Verifikasi seluruh checkbox baris `Manage TAG` enabled
23. Buka Global Settings > Role & Permission > Tab `Total Control`, ketik Search `Cakra Mahendra`, tekan Enter
24. Verifikasi `Cakra Mahendra` tetap tampil di Tab `Total Control`
25. Buka Tab System, buka Detail `Manage TAG`, klik `Changelog`
26. Verifikasi Changelog Detail `Manage TAG` memuat sedikitnya satu entri
27. Ketik Search `Cakra Mahendra`, tekan Enter
28. Verifikasi total entri sama dengan `B-CM` (tidak ada entry log baru)
29. Tutup modal Changelog
30. Ganti akun: Logout dari akun Ahmad Fauzi, login sebagai `Cakra Mahendra`
31. Buka Overlay Notifikasi
32. Verifikasi Overlay Notifikasi tampil
33. Verifikasi jumlah notifikasi sama dengan `B-CN` (tidak ada notifikasi baru)

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Spec absence (kelas g, bagian 3 prinsip 13g): tiap blok punya pemicu, user, dan baseline sendiri. TC milik spec ini: TC-GS-ROLE-328 dan TC-GS-ROLE-339 (seluruh Expected: tampilan dan state, lalu absence). Pemicu TC-339 adalah pelaku kedua lewat sesi API (`P-5` butir a); pelaku kedua lewat sesi API bukan konteks kedua sehingga tidak memakai butir `P-2` (keputusan 2026-10-30).
- Urutan TC sumber diubah dari 328, 339 menjadi 339 lalu 328 supaya ganti akun ke `Cakra Mahendra` untuk membaca notifikasi (TC-328) terjadi sekali di akhir spec.
- Spec berisi 33 langkah, di bawah ambang sekitar 35; kedua blok berdiri sendiri (user, pemicu, baseline, dan asersi sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Anchor positif absence (bagian 8b butir 2): TC-339 memakai toast netral `This role is no longer available.` (langkah 5) dan entry Remove dari Sesi B pada Changelog yang sama (langkah 11); TC-328 memakai dialog tertutup (langkah 18) bagi absence toast, Changelog Detail `Manage TAG` yang memuat sedikitnya satu entri (langkah 26) bagi absence entry log, dan Overlay Notifikasi yang tampil (langkah 32) bagi absence notifikasi. Absence toast (langkah 19) diletakkan segera sesudah pemicu `[Cancel]` (bagian 8b butir 11). Asersi jumlah dengan baseline mengikuti S-12.
- Search untuk menemukan user atau entri target ditulis sebagai langkah penghubung (R-16): langkah 1, 9, 14, 23, 27. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka Tab `Role`, Tab, Detail, Changelog, dan Overlay Notifikasi (langkah 2, 8, 15, 25, 31), ganti akun (langkah 30), serta menutup modal Changelog (langkah 13 dan 29).
- Temuan untuk QA:
  - Email dan kredensial akun `Cakra Mahendra` tidak ada di Tabel Pre-setup TC; ditulis "disediakan tim FE".
  - TC-GS-ROLE-328 dan TC-GS-ROLE-339 (Expected "tidak ada entry log baru") tidak menyebut surface log; spec memakai Changelog Detail `Manage TAG` (TC-328) dan Changelog Detail `Manage files` (TC-339). TC-GS-ROLE-328 tidak menyebut cara membaca "tidak ada notifikasi ke Cakra Mahendra"; spec memakai Overlay Notifikasi akun itu.
  - TC-GS-ROLE-339 Langkah Uji "Sesi B: buka Detail `Manage files`, Remove baris" menyebut aksi UI; spec memakai sesi API karena Sesi B hanya memicu perubahan state.
  - TC-GS-ROLE-339 bertanda `Manual Only (d)` karena dua sesi paralel; spec tetap memuatnya (hambatan teknis bukan alasan mengeluarkan TC).
  - TC-GS-ROLE-328 Given menyebut Cakra Mahendra di-assign Total Control ulang "bila TC-GS-ROLE-326 sudah dijalankan"; spec menulis Given sendiri di hook `before` dan tidak bergantung urutan spec.
  - Mekanisme menyiapkan access level dan baris role per user (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
