---
id: TC-FA-SU-E2E-321-defense-in-depth-status-aktif-akun-sendiri-default-user-target-tier-nonaktif-global
title: "Defense-in-depth Status Aktif: Akun Sendiri, Default User, Target Tier, Nonaktif Global Settings, dan Di Luar Scope"
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

# Defense-in-depth Status Aktif: Akun Sendiri, Default User, Target Tier, Nonaktif Global Settings, dan Di Luar Scope

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 7 Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`); langkah 16 Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; email disediakan tim FE; `Spectra.env.FA_MURGR_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), dan Global Settings (#38: Rudi Hartono nonaktif di Global Settings). Target: Lina Marlina (akun sendiri dan Total Control), Ahmad Dahlan (Default User), Citra Lestari (Read Only), Rudi Hartono, Indra Wijaya (di luar scope Finance & Accounting). Semua blok hanya membaca: tidak ada data yang diubah.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE. Pembacaan state pada langkah 16 memakai sesi API Total Control Lina Marlina (`Spectra.env.FA_TC_PASSWORD`).
- Arah toggle pada TC-FA-SU-125 dan 128 ("Activate atau Deactivate") ditulis Deactivate karena kedua target berstatus Active.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-125: Permintaan paksa ubah status aktif akun sendiri

1. Kirim permintaan langsung ke API toggle status akun sendiri (Lina Marlina) memakai klien HTTP dengan token sesi Lina Marlina
2. Verifikasi server menolak permintaan dengan status 403
3. Verifikasi status aktif akun Lina Marlina tetap Active (dibaca lewat API)

### TC-FA-SU-128: Permintaan paksa ubah status pengguna yang nonaktif di Global Settings

4. Kirim permintaan langsung ke API toggle status Rudi Hartono (nonaktif di Global Settings) memakai klien HTTP dengan token sesi Lina Marlina
5. Verifikasi server menolak permintaan dengan status 403
6. Verifikasi status aktif FAMS Rudi Hartono tidak berubah (dibaca lewat API)

### TC-FA-SU-126: Permintaan paksa Deactivate Default User

7. Ganti akun: login API sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
8. Kirim permintaan langsung ke API Deactivate Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Qori Akbar
9. Verifikasi server menolak permintaan dengan status 403
10. Verifikasi status Ahmad Dahlan tetap Active (dibaca lewat API)

### TC-FA-SU-127: Permintaan paksa Deactivate target Total Control atau Read Only

11. Kirim permintaan langsung ke API Deactivate Lina Marlina memakai klien HTTP dengan token sesi Qori Akbar
12. Verifikasi server menolak permintaan dengan status 403
13. Kirim permintaan langsung ke API Deactivate Citra Lestari memakai klien HTTP dengan token sesi Qori Akbar
14. Verifikasi server menolak permintaan dengan status 403
15. Verifikasi status Lina Marlina dan Citra Lestari tidak berubah (dibaca lewat API)

### TC-FA-SU-129: Permintaan paksa Activate atau Deactivate di luar scope aktor ber-scope grup

16. Ganti akun: login API sebagai Sinta Dewi (Manage user & role Group (Update), `Spectra.env.FA_MURGR_UPD_PASSWORD`) untuk klien HTTP
17. Kirim permintaan langsung ke API Deactivate Indra Wijaya (di luar scope Finance & Accounting) memakai klien HTTP dengan token sesi Sinta Dewi
18. Verifikasi server menolak permintaan dengan status 403 untuk Indra Wijaya
19. Verifikasi status Indra Wijaya tetap Active (dibaca lewat API dengan token sesi Total Control Lina Marlina)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-125 sampai 129 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-125 sampai 129 diasersi di spec 336 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Urutan TC sumber diubah (TC-FA-SU-125, 128, 126, 127, 129) supaya ganti akun hanya dua kali; semua blok hanya membaca.
- Klausa tampilan pada Expected b TC-FA-SU-125 sampai 128 (sakelar Disabled dengan tooltip) tidak diasersi karena bagian 8b butir 1 melarang asersi tampilan pada spec permintaan langsung; tampilan itu diuji lewat jalur UI.
- Ganti akun eksplisit (S-07): langkah 7, 16.
- Temuan untuk QA:
  - Expected b TC-FA-SU-125 sampai 128 menggabungkan status respons, state data, tampilan sakelar, dan log dalam satu butir; spec memecahnya menurut surface (S-01).
  - Arah toggle TC-FA-SU-125 dan 128 tidak ditentukan ("Activate atau Deactivate"); spec memakai Deactivate.
  - TC-FA-SU-129 menulis "Periksa status Indra lewat akun Total Control" tanpa langkah login UI; spec membaca lewat sesi API Total Control.
  - Email dan password Qori Akbar (#4) dan Sinta Dewi (#6) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
