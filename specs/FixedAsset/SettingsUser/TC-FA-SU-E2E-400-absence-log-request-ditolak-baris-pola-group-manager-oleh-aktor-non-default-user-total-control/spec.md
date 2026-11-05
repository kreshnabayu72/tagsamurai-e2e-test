---
id: TC-FA-SU-E2E-400-absence-log-request-ditolak-baris-pola-group-manager-oleh-aktor-non-default-user-total-control
title: "Absence Log Request Ditolak: Baris Pola Group Manager oleh Aktor Non-Default User dan Non-Total Control"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1099
coverage:
  web: automated
---

# Absence Log Request Ditolak: Baris Pola Group Manager oleh Aktor Non-Default User dan Non-Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`; email tidak tertulis di Pre-setup TC (disediakan tim FE). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor berikutnya (ganti akun eksplisit, S-07; sesi API untuk klien HTTP): langkah 7 Manage global user & role (Update) Qori Akbar (Pre-setup #4), `Spectra.env.FA_MURG_UPD_PASSWORD`; email disediakan tim FE.
- Hook suite (`suite.md`): flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), dan Group Manager `FaUserGM` (#48). Target: Putri Anggraeni (Group Manager Finance & Accounting, turunan Accounts Payable; baris pola Group Manager pada kedua node). Nama pengguna dan grup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog Putri Anggraeni, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- State global dan pemulihan: tidak ada data yang diubah karena setiap permintaan ditolak server. Sebagai cadangan, hook `after` memulihkan CRUD baris, status Group Manager, dan baris pola Putri Anggraeni ke Pre-setup #48 lewat seed API (disediakan tim BE/FE). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah entri log pada Tab Changelog Putri Anggraeni, Tab System Log aktor (Sinta Dewi), dan Activity Log (Sinta Dewi) sebagai baseline
2. Kirim permintaan langsung ke API ubah CRUD baris pola Manage files × Accounts Payable milik Putri Anggraeni memakai klien HTTP dengan token Sinta Dewi
3. Verifikasi anchor: server menolak permintaan dengan status 403
4. Kirim permintaan langsung hapus baris Transaction Role pola Transfer × Approver (grup dalam subtree) milik Putri Anggraeni memakai klien HTTP dengan token Sinta Dewi
5. Verifikasi anchor: server menolak permintaan dengan status 403
6. Verifikasi tidak ada entri log baru pada Tab Changelog Putri Anggraeni, Tab System Log aktor (Sinta Dewi), dan Activity Log (Sinta Dewi): jumlah entri masing-masing sama dengan baseline
7. Ganti akun: login API sebagai Qori Akbar (Manage global user & role, `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
8. Catat jumlah entri log pada Tab Changelog Putri Anggraeni, Tab System Log aktor (Qori Akbar), dan Activity Log (Qori Akbar) sebagai baseline
9. Kirim permintaan langsung ke API cabut Accounts Payable dari baris pola Disposal × Asset Admin milik Putri Anggraeni memakai klien HTTP dengan token Qori Akbar
10. Verifikasi anchor: server menolak permintaan dengan status 403
11. Verifikasi tidak ada entri log baru pada Tab Changelog Putri Anggraeni, Tab System Log aktor (Qori Akbar), dan Activity Log (Qori Akbar): jumlah entri masing-masing sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Login pertama TC (Sinta Dewi) dilakukan hook `before`.
- S-05 dan P-5 butir a: spec ini memuat klausa "tidak ada entri log" Expected a TC-FA-SU-1099 (langkah 1 sampai 3 TC) untuk asersi absence (kelas g) dengan permintaan langsung ke server yang ditolak sebagai pemicu, user dan baseline sendiri. Asersi status respons dan state data TC yang sama ada di spec 399. Status 403 pada tiap permintaan dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2). Id TC tetap di `sourceTc` kedua spec.
- Langkah 4 TC (baris Manage user & role diterima) dan langkah 5 TC (konfirmasi Auto-Revert) bukan penolakan 403 sehingga tidak termasuk spec absence ini; keduanya ada di spec 399.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1 dan 8 (baseline).
- Ganti akun eksplisit (S-07): langkah 7. Aktor Sinta Dewi dan Qori Akbar berbeda sehingga surface Tab System Log aktor dan Activity Log dibaca per aktor, dan baseline dicatat ulang sebelum pemicu blok kedua.
- Temuan untuk QA:
  - Kontrak API 403 untuk langkah 1 sampai 3 TC belum diverifikasi (TC menulis "kontrak `settings-user/API/roles.md` perlu diverifikasi"); spec mengasersi kode seperti tertulis di TC (K-1).
  - Expected a TC-FA-SU-1099 menyebut "tidak ada entri log" tanpa menyebut surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064 dan spec 336.
  - Payload "ubah CRUD" tidak ditentukan TC; ditentukan saat tahap script.
  - Seluruh langkah spec adalah permintaan langsung dan pembacaan jumlah entri log; TC-FA-SU-1099 berkolom FE Test `-`.
  - Email dan password Sinta Dewi (#6) dan Qori Akbar (#4) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
