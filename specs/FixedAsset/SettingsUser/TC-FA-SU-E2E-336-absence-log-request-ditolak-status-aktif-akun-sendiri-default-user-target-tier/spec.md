---
id: TC-FA-SU-E2E-336-absence-log-request-ditolak-status-aktif-akun-sendiri-default-user-target-tier
title: "Absence Log Request Ditolak: Status Aktif: Akun Sendiri, Default User, Target Tier, Nonaktif Global Settings, dan Di Luar Scope"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-125
  - TC-FA-SU-126
  - TC-FA-SU-127
  - TC-FA-SU-128
  - TC-FA-SU-129
coverage:
  web: automated
---

# Absence Log Request Ditolak: Status Aktif: Akun Sendiri, Default User, Target Tier, Nonaktif Global Settings, dan Di Luar Scope

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 9 Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`); langkah 20 Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; email disediakan tim FE; `Spectra.env.FA_MURGR_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), dan Global Settings (#38: Rudi Hartono nonaktif di Global Settings). Target: Lina Marlina, Ahmad Dahlan, Citra Lestari, Rudi Hartono, dan Indra Wijaya.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-125: Permintaan paksa ubah status aktif akun sendiri

1. Catat jumlah entri log pada Tab Changelog Lina Marlina, Tab System Log aktor, dan Activity Log sebagai baseline
2. Kirim permintaan langsung ke API toggle status akun sendiri (Lina Marlina) memakai klien HTTP dengan token sesi Lina Marlina
3. Verifikasi anchor: server menolak permintaan dengan status 403
4. Verifikasi tidak ada entri log baru pada Tab Changelog Lina Marlina, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-128: Permintaan paksa ubah status pengguna yang nonaktif di Global Settings

5. Catat jumlah entri log pada Tab Changelog Rudi Hartono, Tab System Log aktor, dan Activity Log sebagai baseline
6. Kirim permintaan langsung ke API toggle status Rudi Hartono (nonaktif di Global Settings) memakai klien HTTP dengan token sesi Lina Marlina
7. Verifikasi anchor: server menolak permintaan dengan status 403
8. Verifikasi tidak ada entri log baru pada Tab Changelog Rudi Hartono, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-126: Permintaan paksa Deactivate Default User

9. Ganti akun: login API sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
10. Catat jumlah entri log pada Tab Changelog Ahmad Dahlan, Tab System Log aktor, dan Activity Log sebagai baseline
11. Kirim permintaan langsung ke API Deactivate Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Qori Akbar
12. Verifikasi anchor: server menolak permintaan dengan status 403
13. Verifikasi tidak ada entri log baru pada Tab Changelog Ahmad Dahlan, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-127: Permintaan paksa Deactivate target Total Control atau Read Only

14. Catat jumlah entri log pada Tab Changelog Lina Marlina dan Citra Lestari, Tab System Log aktor, dan Activity Log sebagai baseline
15. Kirim permintaan langsung ke API Deactivate Lina Marlina memakai klien HTTP dengan token sesi Qori Akbar
16. Verifikasi anchor: server menolak permintaan dengan status 403
17. Kirim permintaan langsung ke API Deactivate Citra Lestari memakai klien HTTP dengan token sesi Qori Akbar
18. Verifikasi anchor: server menolak permintaan dengan status 403
19. Verifikasi tidak ada entri log baru pada Tab Changelog Lina Marlina dan Citra Lestari, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-129: Permintaan paksa Activate atau Deactivate di luar scope aktor ber-scope grup

20. Ganti akun: login API sebagai Sinta Dewi (Manage user & role Group (Update), `Spectra.env.FA_MURGR_UPD_PASSWORD`) untuk klien HTTP
21. Catat jumlah entri log pada Tab Changelog Indra Wijaya, Tab System Log aktor, dan Activity Log sebagai baseline
22. Kirim permintaan langsung ke API Deactivate Indra Wijaya (di luar scope Finance & Accounting) memakai klien HTTP dengan token sesi Sinta Dewi
23. Verifikasi anchor: server menolak permintaan dengan status 403
24. Verifikasi tidak ada entri log baru pada Tab Changelog Indra Wijaya, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-125 sampai 129 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 321. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- Urutan TC sumber diubah (TC-FA-SU-125, 128, 126, 127, 129) supaya ganti akun hanya dua kali.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 5, 10, 14, 21.
- Ganti akun eksplisit (S-07): langkah 9, 20.
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Arah toggle TC-FA-SU-125 dan 128 tidak ditentukan ("Activate atau Deactivate"); spec memakai Deactivate.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
  - Email dan password Qori Akbar (#4) dan Sinta Dewi (#6) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
