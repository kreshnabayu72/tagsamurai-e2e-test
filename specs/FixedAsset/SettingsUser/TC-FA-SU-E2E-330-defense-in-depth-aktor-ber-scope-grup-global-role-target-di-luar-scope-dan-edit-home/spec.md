---
id: TC-FA-SU-E2E-330-defense-in-depth-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan-edit-home
title: "Defense-in-depth Aktor Ber-scope Grup: Global Role Target, Di Luar Scope, dan Edit Home Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-305
  - TC-FA-SU-982
  - TC-FA-SU-983
  - TC-FA-SU-984
  - TC-FA-SU-985
  - TC-FA-SU-986
coverage:
  web: automated
---

# Defense-in-depth Aktor Ber-scope Grup: Global Role Target, Di Luar Scope, dan Edit Home Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Read Only Citra Lestari (Pre-setup #3), `readOnly_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_RO_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 3 Group Manager (IT Infrastructure dan Accounts Payable) Oscar Pranata (Pre-setup #9; email disediakan tim FE; `Spectra.env.FA_GM_PASSWORD`); langkah 6 Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; email disediakan tim FE; `Spectra.env.FA_MURGR_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Gita Permata (Finance & Accounting, dalam scope Sinta Dewi) dan Indra Wijaya (IT Infrastructure, di luar scope Finance & Accounting).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Ganti akun pada spec ini hanya mengambil token sesi API aktor untuk klien HTTP (sesi UI tetap akun pertama).
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-305: Permintaan langsung Edit Home Group oleh Read Only, Group Manager, atau Manage user & role Group

1. Kirim permintaan langsung ke API Edit Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Citra Lestari
2. Verifikasi server menolak permintaan dengan status 403 untuk aktor Read Only
3. Ganti akun: login API sebagai Oscar Pranata (Group Manager (IT Infrastructure dan Accounts Payable), `Spectra.env.FA_GM_PASSWORD`) untuk klien HTTP
4. Kirim permintaan langsung ke API Edit Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Oscar Pranata
5. Verifikasi server menolak permintaan dengan status 403 untuk aktor Group Manager
6. Ganti akun: login API sebagai Sinta Dewi (Manage user & role Group (Update), `Spectra.env.FA_MURGR_UPD_PASSWORD`) untuk klien HTTP
7. Kirim permintaan langsung ke API Edit Home Group Gita Permata ke IT Infrastructure memakai klien HTTP dengan token sesi Sinta Dewi
8. Verifikasi server menolak permintaan dengan status 403 untuk aktor Manage user & role Group
9. Verifikasi Home Group Gita Permata tidak berubah, tetap Finance & Accounting (dibaca lewat API)

### TC-FA-SU-982: Aktor Manage user & role Group atas Global Role target: permintaan langsung ubah switch Global Role

10. Kirim permintaan langsung ke API nyalakan switch Manage asset ID configuration untuk Gita Permata memakai klien HTTP dengan token sesi Sinta Dewi
11. Verifikasi server menolak permintaan dengan status 403
12. Verifikasi switch Manage asset ID configuration Gita Permata tetap OFF (dibaca lewat API)

### TC-FA-SU-983: Aktor Manage user & role Group atas Global Role target: permintaan langsung ubah checkbox CRUD Global Role

13. Kirim permintaan langsung ke API centang Update Manage accounting untuk Gita Permata memakai klien HTTP dengan token sesi Sinta Dewi
14. Verifikasi server menolak permintaan dengan status 403
15. Verifikasi nilai Update Manage accounting Gita Permata tidak berubah (dibaca lewat API)

### TC-FA-SU-984: Aktor ber-scope grup atas pengguna di luar scope: permintaan langsung Deactivate

16. Kirim permintaan langsung ke API Deactivate Indra Wijaya (di luar scope Finance & Accounting) memakai klien HTTP dengan token sesi Sinta Dewi
17. Verifikasi server menolak permintaan dengan status 403
18. Verifikasi Indra Wijaya tetap Active (dibaca lewat API)

### TC-FA-SU-985: Aktor ber-scope grup atas pengguna di luar scope: permintaan langsung simpan Group Role

19. Kirim permintaan langsung ke API tambah grup General Affairs ke Manage files milik Indra Wijaya (di luar scope) memakai klien HTTP dengan token sesi Sinta Dewi
20. Verifikasi server menolak permintaan dengan status 403
21. Verifikasi penugasan grup Group Role Indra Wijaya tidak berubah (dibaca lewat API)

### TC-FA-SU-986: Aktor ber-scope grup atas pengguna di luar scope: permintaan langsung assign Transaction Role

22. Kirim permintaan langsung ke API assign Transfer × Asset Admin pada Finance & Accounting untuk Indra Wijaya (di luar scope) memakai klien HTTP dengan token sesi Sinta Dewi
23. Verifikasi server menolak permintaan dengan status 403
24. Verifikasi Transaction Role Indra Wijaya tidak berubah (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-305 dan 982 sampai 986 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-305 dan 982 sampai 986 diasersi di spec 345 (TC-FA-SU-982 sampai 986) dan 346 (TC-FA-SU-305) (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Urutan TC sumber diubah: TC-FA-SU-305 dijalankan lebih dulu karena memuat tiga aktor (Read Only, Group Manager, Manage user & role Group), lalu TC-FA-SU-982 sampai 986 dengan aktor terakhir (Sinta Dewi) tanpa ganti akun tambahan.
- Ganti akun eksplisit (S-07): langkah 3, 6.
- Temuan untuk QA:
  - TC-FA-SU-305 tidak menyebut pengguna target dan nilai Home Group baru; spec memakai Gita Permata (Finance & Accounting) dengan nilai baru IT Infrastructure.
  - Post Condition TC-FA-SU-984 menyebut "Gita Permata tetap Active", sedangkan target Expected adalah Indra Wijaya; spec mengikuti Expected (Indra Wijaya tetap Active).
  - Email dan password Sinta Dewi (#6) dan Oscar Pranata (#9) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
  - TC-FA-SU-305 dan 982 sampai 986 berkolom FE Test `-`; seluruh langkah adalah permintaan langsung (K-1).
