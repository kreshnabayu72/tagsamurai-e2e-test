---
id: TC-FA-SU-E2E-350-absence-log-request-ditolak-default-user-sebagai-target-transaction-role-dan-edit
title: "Absence Log Request Ditolak: Default User sebagai Target: Transaction Role dan Edit Home Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-997
  - TC-FA-SU-998
coverage:
  web: automated
---

# Absence Log Request Ditolak: Default User sebagai Target: Transaction Role dan Edit Home Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Ahmad Dahlan (Default User, Home Group awal IT Infrastructure, Pre-setup #2).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-997: Default User sebagai target (assign Transaction Role)

1. Catat jumlah entri log pada Tab Changelog Ahmad Dahlan, Tab System Log aktor, dan Activity Log sebagai baseline
2. Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Lina Marlina
3. Verifikasi anchor: server menolak permintaan dengan status 403
4. Verifikasi tidak ada entri log baru pada Tab Changelog Ahmad Dahlan, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-998: Default User sebagai target (Edit Home Group)

5. Catat jumlah entri log pada Tab Changelog Ahmad Dahlan, Tab System Log aktor, dan Activity Log sebagai baseline
6. Kirim permintaan langsung ke API ubah Home Group Ahmad Dahlan dari IT Infrastructure ke Branch Surabaya memakai klien HTTP dengan token sesi Lina Marlina
7. Verifikasi anchor: server menolak permintaan dengan status 403
8. Verifikasi tidak ada entri log baru pada Tab Changelog Ahmad Dahlan, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-997 dan 998 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 334. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 5.
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
