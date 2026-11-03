---
id: TC-FA-SU-E2E-338-absence-log-request-ditolak-transaction-role-dan-group-role-target-tier-di-luar-scope
title: "Absence Log Request Ditolak: Transaction Role dan Group Role: Target Tier, Di Luar Scope, dan Perubahan Baris Terkunci"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-222
  - TC-FA-SU-223
  - TC-FA-SU-272
coverage:
  web: automated
---

# Absence Log Request Ditolak: Transaction Role dan Group Role: Target Tier, Di Luar Scope, dan Perubahan Baris Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 11 Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Wawan Setiawan, Yuda Pratama, Lina Marlina, Citra Lestari, Ahmad Dahlan, dan Qori Akbar.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-222: Perubahan paksa pada baris Group Role terkunci

1. Catat jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
2. Kirim permintaan langsung ke API ubah CRUD baris Branch Surabaya milik Wawan Setiawan (di luar scope Finance & Accounting) memakai klien HTTP dengan token sesi Sinta Dewi
3. Verifikasi anchor: server menolak permintaan dengan status 403
4. Verifikasi tidak ada entri log baru pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-272: Permintaan paksa Assign atau Remove Transaction Role pada grup di luar scope

5. Catat jumlah entri log pada Tab Changelog Yuda Pratama, Tab System Log aktor, dan Activity Log sebagai baseline
6. Kirim permintaan langsung ke API assign Transaction Role pada Logistics Warehouse (di luar scope) untuk Yuda Pratama memakai klien HTTP dengan token sesi Sinta Dewi
7. Verifikasi anchor: server menolak permintaan dengan status 403
8. Kirim permintaan langsung ke API remove baris Transaction Role Yuda Pratama yang memuat grup di luar scope memakai klien HTTP dengan token sesi Sinta Dewi
9. Verifikasi anchor: server menolak permintaan dengan status 403
10. Verifikasi tidak ada entri log baru pada Tab Changelog Yuda Pratama, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-223: Penugasan paksa ke target Total Control, Read Only, Default User, atau akun sendiri

11. Ganti akun: login API sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
12. Catat jumlah entri log pada Tab Changelog Lina Marlina, Citra Lestari, Ahmad Dahlan, dan Qori Akbar, Tab System Log aktor, dan Activity Log sebagai baseline
13. Kirim permintaan langsung ke API assign grup Group Role `Manage files` pada General Affairs untuk Lina Marlina (Total Control) memakai klien HTTP dengan token sesi Qori Akbar
14. Verifikasi anchor: server menolak permintaan dengan status 403
15. Kirim permintaan langsung ke API assign grup Group Role `Manage files` pada General Affairs untuk Citra Lestari (Read Only) memakai klien HTTP dengan token sesi Qori Akbar
16. Verifikasi anchor: server menolak permintaan dengan status 403
17. Kirim permintaan langsung ke API assign grup Group Role `Manage files` pada General Affairs untuk Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Qori Akbar
18. Verifikasi anchor: server menolak permintaan dengan status 403
19. Kirim permintaan langsung ke API assign grup Group Role `Manage files` pada General Affairs untuk Qori Akbar (akun sendiri) memakai klien HTTP dengan token sesi Qori Akbar
20. Verifikasi anchor: server menolak permintaan dengan status 403
21. Verifikasi tidak ada entri log baru pada Tab Changelog keempat target, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-222, 223, dan 272 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 323. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- Urutan TC sumber diubah (TC-FA-SU-222, 272, 223) supaya ganti akun hanya satu kali.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 5, 12.
- Ganti akun eksplisit (S-07): langkah 11.
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
  - TC-FA-SU-223 dan 272 tidak menyebut pengguna target, Group Role, atau baris; spec memakai pilihan yang sama dengan spec 323 (Manage files pada General Affairs; Yuda Pratama).
  - Email dan password Qori Akbar (#4) dan Sinta Dewi (#6) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
