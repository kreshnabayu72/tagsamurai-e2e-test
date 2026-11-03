---
id: TC-FA-SU-E2E-337-absence-log-request-ditolak-tier-deactivate-dan-activate-target-total-control-dan
title: "Absence Log Request Ditolak: Tier: Deactivate dan Activate Target Total Control dan Read Only, serta Assign Group Role"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1067
coverage:
  web: automated
---

# Absence Log Request Ditolak: Tier: Deactivate dan Activate Target Total Control dan Read Only, serta Assign Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 7 Group Manager (IT Infrastructure dan Accounts Payable) Oscar Pranata (Pre-setup #9; email disediakan tim FE; `Spectra.env.FA_GM_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23). Target: Lina Marlina (Total Control) dan Citra Lestari (Read Only). Aktor: Sinta Dewi (grup Finance & Accounting) dan Oscar Pranata (grup IT Infrastructure).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum permintaan (baseline, S-12) dan sesudah permintaan; audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena setiap permintaan ditolak server, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1067: Permintaan langsung assign Group Role pada target Total Control dan Read Only

1. Catat jumlah entri log pada Tab Changelog Lina Marlina dan Citra Lestari, Tab System Log aktor, dan Activity Log sebagai baseline
2. Kirim permintaan langsung ke API assign grup Group Role `Manage group` pada Finance & Accounting untuk Lina Marlina memakai klien HTTP dengan token sesi Sinta Dewi
3. Verifikasi anchor: server menolak permintaan dengan status 403
4. Kirim permintaan langsung ke API assign grup Group Role `Manage group` pada Finance & Accounting untuk Citra Lestari memakai klien HTTP dengan token sesi Sinta Dewi
5. Verifikasi anchor: server menolak permintaan dengan status 403
6. Verifikasi tidak ada entri log baru pada Tab Changelog Lina Marlina dan Citra Lestari, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline
7. Ganti akun: login API sebagai Oscar Pranata (Group Manager (IT Infrastructure dan Accounts Payable), `Spectra.env.FA_GM_PASSWORD`) untuk klien HTTP
8. Catat jumlah entri log pada Tab Changelog Lina Marlina dan Citra Lestari, Tab System Log aktor, dan Activity Log sebagai baseline
9. Kirim permintaan langsung ke API assign grup Group Role `Manage group` pada IT Infrastructure untuk Lina Marlina memakai klien HTTP dengan token sesi Oscar Pranata
10. Verifikasi anchor: server menolak permintaan dengan status 403
11. Kirim permintaan langsung ke API assign grup Group Role `Manage group` pada IT Infrastructure untuk Citra Lestari memakai klien HTTP dengan token sesi Oscar Pranata
12. Verifikasi anchor: server menolak permintaan dengan status 403
13. Verifikasi tidak ada entri log baru pada Tab Changelog Lina Marlina dan Citra Lestari, Tab System Log aktor, dan Activity Log: jumlah entri masing-masing sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan P-5 butir a: spec ini memuat TC-FA-SU-1067 untuk asersi absence (kelas g) dengan permintaan langsung ke server sebagai pemicu yang ditolak, user dan baseline sendiri pada tiap TC. Asersi status respons dan state data TC yang sama ada di spec 322. Status 403 pada tiap TC dipakai sebagai anchor bahwa penolakan sudah diproses (bagian 8b butir 2).
- Iterasi kedua (langkah 7 sampai akhir) mengulang langkah 1 sampai 6 untuk Group Manager sesuai Langkah Uji 4 TC, dengan baseline sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 8.
- Ganti akun eksplisit (S-07): langkah 7.
- Temuan untuk QA:
  - Expected TC menyebut "Tab Changelog, Tab System Log, dan Activity Log" tanpa menyebut pemilik tiap surface; spec memakai Tab Changelog target, Tab System Log aktor, dan Activity Log mengikuti rumusan Post Condition TC-FA-SU-1064.
  - Seluruh TC pada spec ini berkolom FE Test `-` atau Expected berupa respons API (K-1); tidak ada langkah UI, sehingga seluruh langkah adalah permintaan langsung dan pembacaan jumlah entri log.
  - Email dan password Sinta Dewi (#6) dan Oscar Pranata (#9) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
  - Klausa log Expected TC-FA-SU-1064 dan 1066 (hanya item eligible menghasilkan entri) berupa asersi jumlah dengan baseline dan diasersi di spec 322, bukan di spec ini.
