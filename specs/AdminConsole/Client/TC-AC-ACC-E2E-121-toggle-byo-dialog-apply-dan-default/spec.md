---
id: TC-AC-ACC-E2E-121-toggle-byo-dialog-apply-dan-default
title: "Toggle Allow Self-Purchased Device Activation: Default Disabled, Dialog Enable, Cancel, Disable Tanpa Dialog, dan Nilai Sama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-246
  - TC-AC-ACC-248
  - TC-AC-ACC-247
  - TC-AC-ACC-251
  - TC-AC-ACC-249
  - TC-AC-ACC-254
coverage:
  web: automated
---

# Toggle Allow Self-Purchased Device Activation: Default Disabled, Dialog Enable, Cancel, Disable Tanpa Dialog, dan Nilai Sama

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun):
  - Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite.
  - Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`, lewat Step ganti akun eksplisit di akhir spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): `PT Sejahtera Abadi {runId}-121` (setara C-01: Active, Partner CV Mitra Sejati, Group Area Jakarta, FAMS, SAMS, SIEM Active, toggle awal Disabled; digeser ke Enabled) dan `PT Uji BYO {runId}-121` (setara C-AST-12: Active, Partner CV Mitra Sejati, Group Area Jakarta, FAMS Active, toggle Disabled; device Jalur B `Handheld BYO Uji` sudah teraktivasi di Global Settings > Hardware tenant replika). Efek: baris Changelog `Edit` Field `Allow Self-Purchased Device Activation` dan Last Updated kedua replika bertambah, hanya pada data milik spec ini. Client C-01 `PT Sejahtera Abadi` dan C-AST-12 `PT Uji BYO` literal tidak disentuh. Client baru milik spec untuk TC-AC-ACC-254 (`PT Default Byo {runId}-121`) dibuat lewat API dan dihapus di hook `after`.
- Kemampuan teknis: klien HTTP/sesi API aktor Active-Full untuk request langsung `set Allow Self-Purchased Device Activation` (TC-AC-ACC-251); sesi API aktor tidak dihitung sebagai sesi web (dinyatakan di `suite.md`); Fixture BE (disediakan tim FE/BE) men-seed kedua replika dan membuat Client baru via API.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-246: Screening toggle Allow Self-Purchased Device Activation default Disabled

1. Ketik Search `PT Sejahtera Abadi {runId}-121`, tekan Enter
2. Klik Company Name `PT Sejahtera Abadi {runId}-121` lalu lihat Section Settings
3. Verifikasi label "Allow Self-Purchased Device Activation" dengan toggle Disabled (default)

### TC-AC-ACC-248: Cancel dialog Enable: toggle tetap Disabled

4. Klik breadcrumb "Client", lalu baca jumlah baris Changelog `Edit` untuk "PT Sejahtera Abadi {runId}-121" Field `Allow Self-Purchased Device Activation` (N0) lewat `[Changelog]` di toolbar List, klik ikon Search, ketik `PT Sejahtera Abadi {runId}-121`, tekan Enter, ubah ukuran halaman modal menjadi 100, lalu tutup modal dan buka kembali Detail `PT Sejahtera Abadi {runId}-121`
5. Geser toggle ke Enabled
6. Klik `[Cancel]` pada dialog
7. Verifikasi dialog tertutup
8. Verifikasi toggle kembali Disabled
9. Verifikasi tidak ada toast
10. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search, ketik `PT Sejahtera Abadi {runId}-121`, tekan Enter, ubah ukuran halaman modal menjadi 100
11. Verifikasi jumlah baris Changelog `Edit` Field `Allow Self-Purchased Device Activation` untuk "PT Sejahtera Abadi {runId}-121" tetap N0 (tidak ada log baru)
12. Tutup modal Changelog dan buka kembali Detail `PT Sejahtera Abadi {runId}-121`

### TC-AC-ACC-247: Enable toggle: dialog konfirmasi D-09 lalu apply

13. Geser toggle ke Enabled
14. Verifikasi dialog Title "Allow Self-Purchased Device Activation" dengan bullet `• PT Sejahtera Abadi {runId}-121`
15. Verifikasi dialog memuat "This client will be able to activate devices that were not shipped through the distribution chain. These devices are not pre-verified. Are you sure you want to enable it?"
16. Verifikasi dialog memuat tombol `[Cancel]` dan `[Enable]`
17. Klik `[Enable]`
18. Verifikasi toast sukses "Success, self-purchased device activation setting has been updated."
19. Verifikasi toggle Enabled

### TC-AC-ACC-251: Nilai sama dikirim: no-op idempoten

20. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search, ketik `PT Sejahtera Abadi {runId}-121`, tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Edit` Field `Allow Self-Purchased Device Activation` (N1), lalu tutup modal
21. Kirim request langsung set "Allow Self-Purchased Device Activation" ke Enabled untuk "PT Sejahtera Abadi {runId}-121" saat nilai sudah Enabled
22. Muat ulang Detail `PT Sejahtera Abadi {runId}-121` dan verifikasi elemen Section Settings tampil
23. Verifikasi toggle tetap Enabled
24. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search, ketik `PT Sejahtera Abadi {runId}-121`, tekan Enter, ubah ukuran halaman modal menjadi 100
25. Verifikasi jumlah baris Action `Edit` Field `Allow Self-Purchased Device Activation` tetap N1 (tidak ada log baru)
26. Tutup modal Changelog dan buka kembali Detail `PT Sejahtera Abadi {runId}-121`

### TC-AC-ACC-249: Disable toggle langsung apply tanpa dialog; device Jalur B yang ada tidak dihapus

27. Klik breadcrumb "Client", ketik Search `PT Uji BYO {runId}-121`, tekan Enter, klik Company Name `PT Uji BYO {runId}-121`
28. Geser toggle ke Enabled lalu klik `[Enable]` pada dialog
29. Geser toggle ke Disabled
30. Verifikasi tidak ada dialog
31. Verifikasi toast sukses "Success, self-purchased device activation setting has been updated."
32. Verifikasi toggle Disabled
33. Buka Global Settings > Hardware tenant `PT Uji BYO {runId}-121`
34. Verifikasi device Jalur B "Handheld BYO Uji" tetap tampil (tidak dihapus)

### Blok Total Control

35. Ganti akun: logout lalu login sebagai Total Control A-01

#### TC-AC-ACC-254: Client baru memiliki toggle Disabled

36. Buka Detail Client baru `PT Default Byo {runId}-121` yang dibuat lewat API
37. Verifikasi toggle "Allow Self-Purchased Device Activation" Disabled

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas enam TC satu topik (toggle BYO Detail) dengan satu akun utama; tiap blok memakai replika atau Client sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Ganti akun ke Total Control di akhir sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras.
- `P-5` (butir b): TC-AC-ACC-251 adalah satu TC objek-uji ringan kelas a (request langsung tanpa harness eksternal) pada permukaan yang sama dengan spec fungsional toggle BYO. `K-1`: Expected TC-AC-ACC-251 berupa state data (nilai toggle dan jumlah baris log) lewat Fixture BE/Detail; respons status request tidak disebut TC dan tidak diasersi.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 4 sampai 12 menyertakan baseline Changelog (S-12) dan membuka kembali Detail karena Changelog dibuka dari List (kembali ke List lewat breadcrumb "Client", S-14, pada langkah 4, 10, 20, 24, dan 27); langkah 35 (ganti akun); pemulihan toggle ke Disabled (Post Condition TC-AC-ACC-247) tidak dijalankan karena target adalah replika milik spec yang dibersihkan hook `after`. Asersi "tidak ada log baru" memakai selisih jumlah baris terhadap baseline sebagai asersi jumlah di spec fungsional (bagian 3 prinsip 13, butir g), bukan kelas g.
- Post Condition TC-AC-ACC-247 butir a (log `Edit` Old `Disabled`, New `Enabled` tercatat) dan TC-AC-ACC-249 butir a tanpa langkah observasi di TC tidak diasersi.
- Temuan untuk QA:
  - TC-AC-ACC-251 tidak menyebut kode status request langsung dan tidak menyebut cara membuat nilai awal Enabled; spec memakai Enable lewat UI sebagai prasyarat dan hanya mengasersi nilai dan jumlah log.
  - TC-AC-ACC-254 Precondition menyebut pengguna berada di Detail "PT Sejahtera Abadi" tetapi langkahnya "Buat Client baru lalu buka Detail" tanpa data Create; spec memakai Client baru yang dibuat lewat API (kemampuan disediakan tim FE).
  - TC-AC-ACC-249 langkah 3 ("Buka Global Settings > Hardware tenant PT Uji BYO") tidak menyebut cara memilih tenant; spec mengikuti teks TC.
