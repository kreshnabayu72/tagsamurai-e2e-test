---
id: TC-FA-SU-E2E-333-defense-in-depth-default-user-sebagai-target-deactivate-global-role-dan-group-role
title: "Defense-in-depth Default User sebagai Target: Deactivate, Global Role, dan Group Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-993
  - TC-FA-SU-994
  - TC-FA-SU-995
  - TC-FA-SU-996
coverage:
  web: automated
---

# Defense-in-depth Default User sebagai Target: Deactivate, Global Role, dan Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Ahmad Dahlan (Default User, Pre-setup #2).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-993: Default User sebagai target (Deactivate)

1. Kirim permintaan langsung ke API Deactivate Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Lina Marlina
2. Verifikasi server menolak permintaan dengan status 403
3. Verifikasi Ahmad Dahlan tetap Active (dibaca lewat API)

### TC-FA-SU-994: Default User sebagai target (switch Global Role)

4. Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Lina Marlina
5. Verifikasi server menolak permintaan dengan status 403
6. Verifikasi switch Manage asset ID configuration Ahmad Dahlan tidak berubah (dibaca lewat API)

### TC-FA-SU-995: Default User sebagai target (checkbox CRUD Global Role)

7. Kirim permintaan langsung ke API centang Update Manage accounting untuk Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Lina Marlina
8. Verifikasi server menolak permintaan dengan status 403
9. Verifikasi nilai Update Manage accounting Ahmad Dahlan tidak berubah (dibaca lewat API)

### TC-FA-SU-996: Default User sebagai target (simpan Group Role)

10. Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Lina Marlina
11. Verifikasi server menolak permintaan dengan status 403
12. Verifikasi penugasan grup Group Role Ahmad Dahlan tidak berubah (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-993 sampai 996 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-993 sampai 996 diasersi di spec 349 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Temuan untuk QA:
  - Post Condition TC-FA-SU-993 menyebut "Gita Permata tetap Active", sedangkan target Expected adalah Ahmad Dahlan; spec mengikuti Expected (Ahmad Dahlan tetap Active).
  - TC-FA-SU-993 sampai 996 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
