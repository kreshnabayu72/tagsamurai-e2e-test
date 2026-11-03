---
id: TC-FA-SU-E2E-325-defense-in-depth-aktor-read-only-activate-deactivate-dan-global-role
title: "Defense-in-depth Aktor Read Only: Activate, Deactivate, dan Global Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-964
  - TC-FA-SU-965
  - TC-FA-SU-966
  - TC-FA-SU-967
coverage:
  web: automated
---

# Defense-in-depth Aktor Read Only: Activate, Deactivate, dan Global Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Read Only Citra Lestari (Pre-setup #3), `readOnly_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_RO_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Doni Prasetyo (Inactive) dan Gita Permata (Active; Global Role Manage accounting).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-964: Aktor Read Only (Activate)

1. Kirim permintaan langsung ke API Activate Doni Prasetyo memakai klien HTTP dengan token sesi Citra Lestari
2. Verifikasi server menolak permintaan dengan status 403
3. Verifikasi Doni Prasetyo tetap Inactive (dibaca lewat API)

### TC-FA-SU-965: Aktor Read Only (Deactivate)

4. Kirim permintaan langsung ke API Deactivate Gita Permata memakai klien HTTP dengan token sesi Citra Lestari
5. Verifikasi server menolak permintaan dengan status 403
6. Verifikasi Gita Permata tetap Active (dibaca lewat API)

### TC-FA-SU-966: Aktor Read Only (switch Global Role)

7. Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Gita Permata memakai klien HTTP dengan token sesi Citra Lestari
8. Verifikasi server menolak permintaan dengan status 403
9. Verifikasi switch Manage asset ID configuration Gita Permata tetap OFF (dibaca lewat API)

### TC-FA-SU-967: Aktor Read Only (checkbox CRUD Global Role)

10. Kirim permintaan langsung ke API centang Update Manage accounting untuk Gita Permata memakai klien HTTP dengan token sesi Citra Lestari
11. Verifikasi server menolak permintaan dengan status 403
12. Verifikasi nilai Update Manage accounting Gita Permata tidak berubah (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-964 sampai 967 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-964 sampai 967 diasersi di spec 340 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Temuan untuk QA:
  - TC-FA-SU-964 sampai 967 berkolom FE Test `-`; tidak ada langkah UI sehingga seluruh langkah adalah permintaan langsung (K-1).
  - Email Read Only Citra Lestari (#3) mengikuti pola Pre-setup TC; password lewat `Spectra.env.FA_RO_PASSWORD`.
