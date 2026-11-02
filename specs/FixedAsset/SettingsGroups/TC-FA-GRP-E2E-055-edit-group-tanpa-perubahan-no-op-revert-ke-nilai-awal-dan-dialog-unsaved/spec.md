---
id: TC-FA-GRP-E2E-055-edit-group-tanpa-perubahan-no-op-revert-ke-nilai-awal-dan-dialog-unsaved
title: "Edit Group: Tanpa Perubahan (No-Op), Ubah Lalu Revert, Kapitalisasi/Spasi Tepi No-Op, dan Dialog Unsaved Tidak Muncul Setelah Revert"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-168
  - TC-FA-GRP-169
  - TC-FA-GRP-170
  - TC-FA-GRP-978
coverage:
  web: automated
---

# Edit Group: Tanpa Perubahan (No-Op), Ubah Lalu Revert, Kapitalisasi/Spasi Tepi No-Op, dan Dialog Unsaved Tidak Muncul Setelah Revert

## Prerequisites

- Mode: FE+BE (backend nyata; asersi tidak adanya pencatatan log memakai baseline jumlah entri, bukan kelas g).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-055` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): node `Edit Target {runId}-055` (level 1, Code `ET`, Description `Edit me`, Function None) di-seed lewat API di hook `before`; tidak diubah oleh spec ini.
- Kemampuan teknis: pembacaan jumlah entri Changelog node, System Log, dan Activity Log serta Modified By dan Last Updated baris target sebelum dan sesudah aksi (disediakan tim FE/BE; selisih terhadap baseline, S-12); jam server dan jam browser sinkron.
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-055` dan group ber-Code literal `ET`.
- State global: tidak ada yang diubah.

## Test Steps

1. Catat jumlah entri Changelog node `Edit Target {runId}-055`, System Log, dan Activity Log, serta Modified By dan Last Updated baris target sebagai baseline, lalu ketik Search `Edit Target {runId}-055`, tekan Enter

### TC-FA-GRP-168: Edit Group tanpa perubahan (No-Op)

2. Buka elipsis (⋯) baris `Edit Target {runId}-055`, klik Edit, lalu klik [Save] tanpa mengubah apa pun
3. Verifikasi popup tertutup
4. Verifikasi toast netral `No changes to save.` (bukan toast sukses)
5. Verifikasi Modified By dan Last Updated baris target tidak berubah terhadap baseline langkah 1
6. Verifikasi tidak ada baris baru di Changelog, System Log, dan Activity Log: jumlah entri sama dengan baseline langkah 1

### TC-FA-GRP-169: Ubah lalu kembalikan ke nilai awal dianggap No-Op

7. Buka elipsis (⋯) baris target, klik Edit, ubah Description lalu ketik ulang nilai semula `Edit me`, lalu klik [Save]
8. Verifikasi toast netral `No changes to save.`
9. Verifikasi tidak ada baris log baru: jumlah entri Changelog, System Log, dan Activity Log sama dengan baseline langkah 1

### TC-FA-GRP-978: Ubah Group Name hanya kapitalisasi atau spasi tepi dianggap No-Op

10. Buka elipsis (⋯) baris target, klik Edit, ubah Group Name menjadi `edit target {runId}-055 ` (huruf kecil dan spasi di akhir), lalu klik [Save]
11. Verifikasi toast netral `No changes to save.` (bukan toast sukses)
12. Verifikasi Group Name tersimpan tetap `Edit Target {runId}-055`
13. Verifikasi Modified By dan Last Updated baris target tidak berubah terhadap baseline langkah 1
14. Verifikasi tidak ada baris baru di Changelog, System Log, dan Activity Log: jumlah entri sama dengan baseline langkah 1

### TC-FA-GRP-170: Dialog Unsaved tidak muncul setelah revert ke nilai tersimpan

15. Buka elipsis (⋯) baris target, klik Edit, ubah Group Name lalu kembalikan persis ke nilai tersimpan, lalu klik (X)
16. Verifikasi popup langsung tertutup
17. Verifikasi dialog `Unsaved changes` tidak muncul
18. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-168, 169, 978 (semua No-Op, node tidak berubah) lalu TC-FA-GRP-170; berbeda dari urutan nomor TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Catat jumlah entri Changelog node `Edit Target {runId}-055`, System Lo...); langkah 18 (Klik `(←)` pada kotak Search).
- Asersi "tidak ada baris log baru" ditulis sebagai `Verifikasi` berbaseline jumlah entri di spec ini (S-12) dengan toast netral sebagai anchor positif respons server; tidak ada rujukan ke spec absence.
- Langkah 1 mencatat baseline dan mencari baris target (R-16).
- Temuan untuk QA:
  - TC-FA-GRP-169 dan TC-FA-GRP-170 tidak menyebut Description dan Group Name awal; spec memakai node milik spec (`Edit me`).
  - TC-FA-GRP-168 Expected c menyebut tiga log sekaligus; spec membacanya lewat kemampuan baca log yang disediakan tim FE/BE.
  - TC-FA-GRP-170 Expected "dirty-check = beda dari nilai tersimpan" adalah penjelasan, tidak diasersi terpisah.

