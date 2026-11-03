---
id: TC-FA-SU-E2E-331-defense-in-depth-akun-sendiri-sebagai-target-deactivate-global-role-dan-group-role
title: "Defense-in-depth Akun Sendiri sebagai Target: Deactivate, Global Role, dan Group Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-987
  - TC-FA-SU-988
  - TC-FA-SU-989
  - TC-FA-SU-990
coverage:
  web: automated
---

# Defense-in-depth Akun Sendiri sebagai Target: Deactivate, Global Role, dan Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage global user & role (Update) Qori Akbar (Pre-setup #4), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURG_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Qori Akbar (akun sendiri).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-987: Akun sendiri sebagai target (Deactivate)

1. Kirim permintaan langsung ke API Deactivate Qori Akbar (akun sendiri) memakai klien HTTP dengan token sesi Qori Akbar
2. Verifikasi server menolak permintaan dengan status 403
3. Verifikasi Qori Akbar tetap Active (dibaca lewat API)

### TC-FA-SU-988: Akun sendiri sebagai target (switch Global Role)

4. Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Qori Akbar (akun sendiri) memakai klien HTTP dengan token sesi Qori Akbar
5. Verifikasi server menolak permintaan dengan status 403
6. Verifikasi switch Manage asset ID configuration Qori Akbar tidak berubah (dibaca lewat API)

### TC-FA-SU-989: Akun sendiri sebagai target (checkbox CRUD Global Role)

7. Kirim permintaan langsung ke API centang Update Manage accounting untuk Qori Akbar (akun sendiri) memakai klien HTTP dengan token sesi Qori Akbar
8. Verifikasi server menolak permintaan dengan status 403
9. Verifikasi nilai Update Manage accounting Qori Akbar tidak berubah (dibaca lewat API)

### TC-FA-SU-990: Akun sendiri sebagai target (simpan Group Role)

10. Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Qori Akbar (akun sendiri) memakai klien HTTP dengan token sesi Qori Akbar
11. Verifikasi server menolak permintaan dengan status 403
12. Verifikasi penugasan grup Group Role Qori Akbar tidak berubah (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-987 sampai 990 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-987 sampai 990 diasersi di spec 347 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Temuan untuk QA:
  - Post Condition TC-FA-SU-987 menyebut "Gita Permata tetap Active", sedangkan target Expected adalah Qori Akbar; spec mengikuti Expected (Qori Akbar tetap Active).
  - Email dan password Qori Akbar (#4) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
  - TC-FA-SU-987 sampai 990 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
