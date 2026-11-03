---
id: TC-FA-GRP-E2E-067-resilience-form-new-group-new-subgroup-dan-edit-group-gagal-server
title: "Resilience Form: Gagal Server (5xx/Timeout) Mempertahankan Form pada Popup New Group, New Subgroup, dan Edit Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-110
  - TC-FA-GRP-158
  - TC-FA-GRP-216
coverage:
  web: automated
---

# Resilience Form: Gagal Server (5xx/Timeout) Mempertahankan Form pada Popup New Group, New Subgroup, dan Edit Group

## Prerequisites

- Mode: FE+BE (kelas b fault injection; intercept parsial di atas backend nyata: hanya respons simpan group yang dipaksa 500, sisa API memakai backend nyata).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit: respons simpan group (Create Group, Create Subgroup, dan Edit Group) dijawab 500 pada langkah 1, 9, dan 17; dilepas pada langkah 8, 16, dan 25. Nama endpoint tidak disebut di TC dan PRD (ditentukan tim FE di tahap script). Kegagalan timeout tidak dibutuhkan terpisah karena TC memakai 5xx.
- Data Dinamis bersuffix `{runId}-067` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-110: Name `Fail Create {runId}-067`. TC-FA-GRP-158: Name `Fail Sub {runId}-067`. TC-FA-GRP-216: node `Fail Edit {runId}-067` (level 1, Code `ET`, Description `Edit me`, Function None) di-seed lewat API di hook `before`, Description baru `Fail Edit Desc`.
- Kemampuan teknis: pembacaan jumlah group dan Description node target lewat fixture BE (baseline di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD).
- Pemulihan (hook `before` dan `after`): lepas intercept; hapus lewat API node dengan suffix `{runId}-067` dan group ber-Code literal `ET`.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-110: Gagal server mempertahankan form pada Popup New Group

1. Pasang intercept: respons simpan group dijawab 500
2. Klik [+] Group di sidebar
3. Isi Group Name `Fail Create {runId}-067`, lalu klik [Submit]
4. Verifikasi toast error `Error, failed to create group.`
5. Verifikasi popup tetap terbuka dengan input dipertahankan
6. Verifikasi [Submit] kembali enabled untuk retry
7. Klik (X)
8. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil
9. Klik [Leave] (pemulihan form kotor)
10. Lepas intercept respons simpan group

### TC-FA-GRP-158: Gagal server mempertahankan form pada Popup New Subgroup

11. Pasang intercept: respons simpan group dijawab 500
12. Ketik Search `Head Office`, tekan Enter
13. Tunggu toast lama hilang otomatis
14. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
15. Isi Group Name `Fail Sub {runId}-067`, lalu klik [Submit]
16. Verifikasi toast error `Error, failed to create group.`
17. Verifikasi popup tetap terbuka dengan input dipertahankan
18. Verifikasi [Submit] kembali enabled untuk retry
19. Klik (X)
20. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil
21. Klik [Leave] (pemulihan form kotor)
22. Lepas intercept respons simpan group

### TC-FA-GRP-216: Gagal server mempertahankan form pada Popup Edit Group

23. Pasang intercept: respons simpan group dijawab 500
24. Ganti isi kotak Search dengan `Fail Edit {runId}-067`, tekan Enter
25. Buka elipsis (⋯) baris `Fail Edit {runId}-067`, lalu klik Edit
26. Ubah Description menjadi `Fail Edit Desc`, lalu klik [Save]
27. Verifikasi toast error `Error, failed to update group.`
28. Verifikasi popup tetap terbuka dengan input dipertahankan
29. Verifikasi [Save] kembali enabled untuk retry
30. Klik (X)
31. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil
32. Klik [Leave] (pemulihan form kotor)
33. Lepas intercept respons simpan group dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas b fault injection; bagian 3 prinsip 13 butir b). Intercept parsial di atas backend nyata; bukan `Mode: mock` karena TC memakai backend nyata untuk data lain. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Pasang intercept: respons simpan group dijawab 500); langkah 7 (Klik (X)) dan langkah 9 (Klik [Leave], pemulihan form kotor); langkah 10 (Lepas intercept respons simpan group); langkah 11 (Pasang intercept: respons simpan group dijawab 500); langkah 12 (Ketik Search `Head Office`, tekan Enter); langkah 13 (Tunggu toast lama hilang otomatis, supaya toast error langkah 4 tidak lolos sebagai toast langkah 16; R-12); langkah 19 (Klik (X)) dan langkah 21 (Klik [Leave], pemulihan form kotor); langkah 22 (Lepas intercept respons simpan group); langkah 23 (Pasang intercept: respons simpan group dijawab 500); langkah 24 (Ganti isi kotak Search dengan `Fail Edit {runId}-067`, tekan Enter); langkah 30 (Klik (X)) dan langkah 32 (Klik [Leave], pemulihan form kotor); langkah 33 (Lepas intercept respons simpan group dan klik `(←)` pada kotak Search).
- Pencarian baris target (S-03, R-16): langkah 12 (Ketik Search `Head Office`, tekan Enter) menemukan baris Head Office; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Langkah Search mencari baris target (R-16).
- Temuan untuk QA:
  - TC-FA-GRP-110, 158, dan 216 menyebut "5xx/timeout" tetapi Langkah Uji dan Expected hanya memuat 5xx; spec memaksa 500 saja dan tidak menguji timeout.
  - Toast error `Error, failed to create group.` dan `Error, failed to update group.` diasersi persis seperti di TC; TC tidak menyebut apakah popup masih dapat disubmit ulang berhasil setelah intercept dilepas, sehingga tidak diasersi.
  - Ketiga TC tidak menyebut verifikasi bahwa data tidak tersimpan di server; spec mengikuti Expected TC dan tidak menambah asersi.

