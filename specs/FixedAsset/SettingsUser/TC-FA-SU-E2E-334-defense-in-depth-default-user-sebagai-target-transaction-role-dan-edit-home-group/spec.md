---
id: TC-FA-SU-E2E-334-defense-in-depth-default-user-sebagai-target-transaction-role-dan-edit-home-group
title: "Defense-in-depth Default User sebagai Target: Transaction Role dan Edit Home Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-997
  - TC-FA-SU-998
coverage:
  web: automated
---

# Defense-in-depth Default User sebagai Target: Transaction Role dan Edit Home Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Ahmad Dahlan (Default User, Home Group awal IT Infrastructure, Pre-setup #2).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-997: Default User sebagai target (assign Transaction Role)

1. Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Lina Marlina
2. Verifikasi server menolak permintaan dengan status 403
3. Verifikasi Transaction Role Ahmad Dahlan tidak berubah (dibaca lewat API)

### TC-FA-SU-998: Default User sebagai target (Edit Home Group)

4. Kirim permintaan langsung ke API ubah Home Group Ahmad Dahlan dari IT Infrastructure ke Branch Surabaya memakai klien HTTP dengan token sesi Lina Marlina
5. Verifikasi server menolak permintaan dengan status 403 (bukan 200 dan bukan no-op: nilai baru Branch Surabaya berbeda dari nilai awal sehingga penolakan dapat dibedakan dari tidak ada perubahan)
6. Verifikasi Home Group Ahmad Dahlan tetap IT Infrastructure (bukan Branch Surabaya) (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-997 dan 998 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-997 dan 998 diasersi di spec 350 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Temuan untuk QA:
  - TC-FA-SU-997 dan 998 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
