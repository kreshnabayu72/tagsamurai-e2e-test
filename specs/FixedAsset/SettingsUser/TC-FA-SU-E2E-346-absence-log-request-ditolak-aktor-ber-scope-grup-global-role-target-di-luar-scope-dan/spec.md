---
id: TC-FA-SU-E2E-346-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan
title: "Absence Log Request Ditolak: Aktor Ber-scope Grup: Global Role Target, Di Luar Scope, dan Edit Home Group (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-305
coverage:
  web: automated
---

# Absence Log Request Ditolak: Aktor Ber-scope Grup: Global Role Target, Di Luar Scope, dan Edit Home Group (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Read Only Citra Lestari (Pre-setup #3), `readOnly_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_RO_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 4 Group Manager (IT Infrastructure dan Accounts Payable) Oscar Pranata (Pre-setup #9; email disediakan tim FE; `Spectra.env.FA_GM_PASSWORD`); langkah 7 Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; email disediakan tim FE; `Spectra.env.FA_MURGR_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23). Target: Gita Permata (Finance & Accounting).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-305: Permintaan langsung Edit Home Group oleh Read Only, Group Manager, atau Manage user & role Group

1. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
2. Kirim permintaan langsung ke API Edit Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Citra Lestari
3. Verifikasi anchor: server menolak permintaan dengan status 403 untuk aktor Read Only
4. Ganti akun: login API sebagai Oscar Pranata (Group Manager (IT Infrastructure dan Accounts Payable), `Spectra.env.FA_GM_PASSWORD`) untuk klien HTTP
5. Kirim permintaan langsung ke API Edit Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Oscar Pranata
6. Verifikasi anchor: server menolak permintaan dengan status 403 untuk aktor Group Manager
7. Ganti akun: login API sebagai Sinta Dewi (Manage user & role Group (Update), `Spectra.env.FA_MURGR_UPD_PASSWORD`) untuk klien HTTP
8. Kirim permintaan langsung ke API Edit Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Sinta Dewi
9. Verifikasi anchor: server menolak permintaan dengan status 403 untuk aktor Manage user & role Group
10. Verifikasi tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log ketiga aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-305 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 330. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1.
- Ganti akun eksplisit (S-07): langkah 4, 7.
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
  - TC-FA-SU-305 tidak menyebut pengguna target dan nilai Home Group baru; spec memakai Gita Permata dengan nilai baru IT Infrastructure (sama dengan spec 330).
  - Email dan password Sinta Dewi (#6) dan Oscar Pranata (#9) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
