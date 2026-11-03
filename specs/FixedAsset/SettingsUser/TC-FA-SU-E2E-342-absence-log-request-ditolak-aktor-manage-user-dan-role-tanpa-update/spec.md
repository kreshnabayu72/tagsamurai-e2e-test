---
id: TC-FA-SU-E2E-342-absence-log-request-ditolak-aktor-manage-user-dan-role-tanpa-update
title: "Absence Log Request Ditolak: Aktor Manage user & role Tanpa Update"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-971
  - TC-FA-SU-972
  - TC-FA-SU-973
  - TC-FA-SU-974
  - TC-FA-SU-975
coverage:
  web: automated
---

# Absence Log Request Ditolak: Aktor Manage user & role Tanpa Update

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage global user & role (Read saja) Rina Susanti (Pre-setup #5), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURG_RO_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Gita Permata, Wawan Setiawan, dan Mira Anggraini.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-971: Aktor Manage user & role tanpa Update (Deactivate)

1. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
2. Kirim permintaan langsung ke API Deactivate Gita Permata memakai klien HTTP dengan token sesi Rina Susanti
3. Verifikasi anchor: server menolak permintaan dengan status 403
4. Verifikasi tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-972: Aktor Manage user & role tanpa Update (switch Global Role)

5. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
6. Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Gita Permata memakai klien HTTP dengan token sesi Rina Susanti
7. Verifikasi anchor: server menolak permintaan dengan status 403
8. Verifikasi tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-973: Aktor Manage user & role tanpa Update (simpan Group Role)

9. Catat jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
10. Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Wawan Setiawan memakai klien HTTP dengan token sesi Rina Susanti
11. Verifikasi anchor: server menolak permintaan dengan status 403
12. Verifikasi tidak ada entri log baru pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-974: Aktor Manage user & role tanpa Update (assign Transaction Role)

13. Catat jumlah entri log pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sebagai baseline
14. Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Mira Anggraini memakai klien HTTP dengan token sesi Rina Susanti
15. Verifikasi anchor: server menolak permintaan dengan status 403
16. Verifikasi tidak ada entri log baru pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

### TC-FA-SU-975: Aktor Manage user & role tanpa Update (Edit Home Group)

17. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
18. Kirim permintaan langsung ke API ubah Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Rina Susanti
19. Verifikasi anchor: server menolak permintaan dengan status 403
20. Verifikasi tidak ada entri log baru pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-971 sampai 975 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 327. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 5, 9, 13, 17.
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
  - Email dan password Rina Susanti (#5) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
