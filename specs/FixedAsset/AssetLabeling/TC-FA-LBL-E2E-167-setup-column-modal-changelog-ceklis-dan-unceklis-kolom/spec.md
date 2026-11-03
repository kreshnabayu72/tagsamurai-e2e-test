---
id: TC-FA-LBL-E2E-167-setup-column-modal-changelog-ceklis-dan-unceklis-kolom
title: "Setup Column Modal Changelog: Ceklis dan Unceklis Kolom Hideable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-314
coverage:
  web: automated
---

# Setup Column Modal Changelog: Ceklis dan Unceklis Kolom Hideable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): tujuh kolom Modal Changelog pada konfigurasi default.
- Tabel "Kolom Changelog" (parameter langkah berulang): `Date`, `Action`, `Label Name`, `Field`, `Old Value`, `New Value`.
- State global yang diubah: konfigurasi kolom Setup Column Modal Changelog (disimpan lewat `[Save]`). Dipulihkan dengan menyimpan ketujuh kolom pada langkah terakhir dan oleh hook `after` suite (hapus preferensi kolom di browser; kemampuan disediakan tim FE). Spec tidak membuat atau mengubah data backend.
- Kemampuan teknis: muat ulang halaman dengan F5 (`beforeunload` tidak dipicu karena tidak ada form dirty).

## Test Steps

### TC-FA-LBL-314: Setup Column Changelog: ceklis dan unceklis kelas Hideable

1. Klik icon Changelog di Table Tools
2. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`
3. Untuk setiap kolom pada tabel "Kolom Changelog" (langkah 4 sampai 5)
4. Hapus centang kolom tersebut pada daftar Setup Column
5. Verifikasi kolom tersebut langsung hilang dari Live Preview
6. Verifikasi hanya `Modified By` tersisa di Live Preview
7. Untuk setiap kolom pada tabel "Kolom Changelog" (langkah 8 sampai 9)
8. Centang kembali kolom tersebut pada daftar Setup Column
9. Verifikasi kolom tersebut muncul kembali di Live Preview pada posisi semula
10. Hapus centang `Modified By`, klik `[Save]`
11. Tutup Modal Changelog dengan `[✕]`, lalu klik icon Changelog di Table Tools
12. Verifikasi `Modified By` tidak tampil di modal
13. Verifikasi keenam kolom lain tampil di modal
14. Tekan F5 lalu klik icon Changelog di Table Tools
15. Verifikasi `Modified By` tetap tersembunyi setelah reload
16. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`, centang `Modified By`, klik `[Save]`
17. Verifikasi ketujuh kolom tampil
18. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah berulang (bagian 8b butir 7): enam kolom dengan parameter di tabel "Kolom Changelog" pada Prerequisites, tanpa langkah bersyarat. Langkah yang diulang: hapus centang beserta `Verifikasi` hilang dari Live Preview (langkah 4 sampai 5), dan centang kembali beserta `Verifikasi` muncul kembali (langkah 8 sampai 9). Ambang langkah dihitung dengan ekspansi (enam kali dua langkah pada tiap putaran), sehingga spec berisi sekitar 36 langkah. Alasan melewati sekitar 35 langkah: spec berisi satu TC (satu TC satu spec) dengan satu kelas harness dan satu dataset, jadi tidak dapat dipecah.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup lalu membuka Modal Changelog, F5 lalu membuka modal, dan menutup modal di akhir spec. `[Save]` pada Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (bagian 8b butir 8).
- Pembagian TC lintas spec: TC-FA-LBL-312 dan TC-FA-LBL-313 ada di spec 083, TC-FA-LBL-315 dan TC-FA-LBL-316 ada di spec 084.
- Temuan untuk QA:
  - TC-FA-LBL-314 menyatakan kolom hilang "langsung" dari Live Preview; spec mengasersi tiap kolom satu per satu sesuai langkah TC.
  - Pada langkah terakhir TC-FA-LBL-314 `[Save]` menutup popup; TC tidak menyatakan apakah modal ikut menutup, sehingga asersi ketujuh kolom dibaca dari tabel modal yang tetap terbuka.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
