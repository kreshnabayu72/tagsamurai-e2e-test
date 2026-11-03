---
id: TC-FA-SU-E2E-327-defense-in-depth-aktor-manage-user-dan-role-tanpa-update
title: "Defense-in-depth Aktor Manage user & role Tanpa Update"
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

# Defense-in-depth Aktor Manage user & role Tanpa Update

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage global user & role (Read saja) Rina Susanti (Pre-setup #5), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURG_RO_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Gita Permata, Wawan Setiawan, dan Mira Anggraini.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-971: Aktor Manage user & role tanpa Update (Deactivate)

1. Kirim permintaan langsung ke API Deactivate Gita Permata memakai klien HTTP dengan token sesi Rina Susanti
2. Verifikasi server menolak permintaan dengan status 403
3. Verifikasi Gita Permata tetap Active (dibaca lewat API)

### TC-FA-SU-972: Aktor Manage user & role tanpa Update (switch Global Role)

4. Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Gita Permata memakai klien HTTP dengan token sesi Rina Susanti
5. Verifikasi server menolak permintaan dengan status 403
6. Verifikasi switch Manage asset ID configuration Gita Permata tetap OFF (dibaca lewat API)

### TC-FA-SU-973: Aktor Manage user & role tanpa Update (simpan Group Role)

7. Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Wawan Setiawan memakai klien HTTP dengan token sesi Rina Susanti
8. Verifikasi server menolak permintaan dengan status 403
9. Verifikasi penugasan grup Group Role Wawan Setiawan tidak berubah (dibaca lewat API)

### TC-FA-SU-974: Aktor Manage user & role tanpa Update (assign Transaction Role)

10. Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Mira Anggraini memakai klien HTTP dengan token sesi Rina Susanti
11. Verifikasi server menolak permintaan dengan status 403
12. Verifikasi Transaction Role Mira Anggraini tidak berubah (dibaca lewat API)

### TC-FA-SU-975: Aktor Manage user & role tanpa Update (Edit Home Group)

13. Kirim permintaan langsung ke API ubah Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Rina Susanti
14. Verifikasi server menolak permintaan dengan status 403
15. Verifikasi Home Group Gita Permata tetap Finance & Accounting (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-971 sampai 975 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-971 sampai 975 diasersi di spec 342 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Temuan untuk QA:
  - Email dan password Rina Susanti (#5) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
  - TC-FA-SU-971 sampai 975 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
