---
id: TC-FA-SU-E2E-332-defense-in-depth-akun-sendiri-sebagai-target-transaction-role-dan-edit-home-group
title: "Defense-in-depth Akun Sendiri sebagai Target: Transaction Role dan Edit Home Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-991
  - TC-FA-SU-992
coverage:
  web: automated
---

# Defense-in-depth Akun Sendiri sebagai Target: Transaction Role dan Edit Home Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage global user & role (Update) Qori Akbar (Pre-setup #4), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURG_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Qori Akbar (akun sendiri).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-991: Akun sendiri sebagai target (assign Transaction Role)

1. Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Qori Akbar (akun sendiri) memakai klien HTTP dengan token sesi Qori Akbar
2. Verifikasi server menolak permintaan dengan status 403
3. Verifikasi Transaction Role Qori Akbar tidak berubah (dibaca lewat API)

### TC-FA-SU-992: Akun sendiri sebagai target (Edit Home Group)

4. Kirim permintaan langsung ke API ubah Home Group Qori Akbar ke IT Infrastructure memakai klien HTTP dengan token sesi Qori Akbar
5. Verifikasi server menolak permintaan dengan status 403
6. Verifikasi Home Group Qori Akbar tidak berubah (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-991 dan 992 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-991 dan 992 diasersi di spec 348 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Temuan untuk QA:
  - Email dan password Qori Akbar (#4) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
  - TC-FA-SU-992 tidak menyebut Home Group awal Qori Akbar; spec mengasersi Home Group tidak berubah dari nilai yang dibaca sebelum permintaan (Pre-setup #43: General Affairs).
  - TC-FA-SU-991 dan 992 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
