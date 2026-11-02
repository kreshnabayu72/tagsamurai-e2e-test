---
id: TC-FA-GRP-E2E-053-edit-group-screening-popup-prefilled-dan-ubah-name-code-description-saja
title: "Popup Edit Group: Screening Pre-filled Tanpa Baris Under/Stay dan Ubah Name, Code, atau Description Saja"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-160
  - TC-FA-GRP-161
  - TC-FA-GRP-162
  - TC-FA-GRP-163
coverage:
  web: automated
---

# Popup Edit Group: Screening Pre-filled Tanpa Baris Under/Stay dan Ubah Name, Code, atau Description Saja

## Prerequisites

- Mode: FE+BE (backend nyata; Edit Group menulis data dan hasilnya diasersi di tabel, sidebar, dan Detail).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-053` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): node `Edit Target {runId}-053` (level 1, Code `ET`, Description `Edit me`, Function Assignable) di-seed lewat API di hook `before` (Pre-setup tambahan "Edit Target"). Nilai ubah: TC-FA-GRP-161 Name `Edit Target Renamed {runId}-053`; TC-FA-GRP-162 Code `ETR`; TC-FA-GRP-163 Description `Updated notes`.
- Kemampuan teknis: jam server dan jam browser sinkron untuk asersi Last Updated (toleransi satu menit).
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-053` dan group ber-Code literal `ET` dan `ETR` yang dibuat spec ini (hook `before` juga menghapus sisa literal run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target {runId}-053`, tekan Enter

### TC-FA-GRP-160: Screening Popup Edit Group, pre-filled tanpa baris Under dan Stay

2. Buka elipsis (⋯) baris `Edit Target {runId}-053`, lalu klik Edit
3. Verifikasi title `Edit Group` dan icon (X)
4. Verifikasi Group Name, Code, Description, dan Function pre-filled nilai tersimpan (`Edit Target {runId}-053`, `ET`, `Edit me`, Assignable)
5. Verifikasi Function Enabled (tanpa guard histori)
6. Verifikasi tidak ada baris konteks Under
7. Verifikasi tidak ada checkbox `Stay on this form after submitting`
8. Verifikasi footer: [Clear Field] (text) dan [Save] (success)

### TC-FA-GRP-161: Edit Group, ubah Group Name saja

9. Ubah Group Name menjadi `Edit Target Renamed {runId}-053`, lalu klik [Save]
10. Verifikasi popup tertutup
11. Verifikasi toast sukses `Success, group has been updated.`
12. Verifikasi nama baru `Edit Target Renamed {runId}-053` tampil di tabel
13. Verifikasi nama baru tampil di sidebar
14. Klik nama `Edit Target Renamed {runId}-053` untuk membuka Popup Detail Group
15. Verifikasi nama baru tampil di header Popup Detail Group
16. Verifikasi field lain tidak berubah (Code `ET`, Description `Edit me`, Function Assignable)
17. Tutup Popup Detail Group
18. Verifikasi Modified By = aktor (format `[First Name] [Last Initial]`) pada baris `Edit Target Renamed {runId}-053`
19. Verifikasi Last Updated = waktu save (toleransi satu menit)

### TC-FA-GRP-162: Edit Group, ubah Code saja

20. Buka elipsis (⋯) baris `Edit Target Renamed {runId}-053`, klik Edit, ubah Code menjadi `ETR`, lalu klik [Save]
21. Verifikasi popup tertutup
22. Verifikasi toast sukses `Success, group has been updated.`
23. Verifikasi kolom Code menampilkan `ETR`
24. Klik nama group untuk membuka Popup Detail Group
25. Verifikasi header Popup Detail Group menampilkan Code `ETR`
26. Verifikasi field lain tidak berubah (Name `Edit Target Renamed {runId}-053`, Description `Edit me`, Function Assignable)
27. Tutup Popup Detail Group
28. Verifikasi Modified By = aktor (format `[First Name] [Last Initial]`)
29. Verifikasi Last Updated = waktu save (toleransi satu menit)

### TC-FA-GRP-163: Edit Group, ubah Description saja

30. Buka elipsis (⋯) baris `Edit Target Renamed {runId}-053`, klik Edit, ubah Description menjadi `Updated notes`, lalu klik [Save]
31. Verifikasi popup tertutup
32. Verifikasi toast sukses `Success, group has been updated.`
33. Klik nama group untuk membuka Popup Detail Group
34. Verifikasi Description baru `Updated notes` tampil di header Popup Detail Group
35. Verifikasi field lain tidak berubah (Name `Edit Target Renamed {runId}-053`, Code `ETR`, Function Assignable)
36. Tutup Popup Detail Group
37. Verifikasi Modified By = aktor (format `[First Name] [Last Initial]`)
38. Verifikasi Last Updated = waktu save (toleransi satu menit)
39. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Edit Target {runId}-053`, tekan Enter); langkah 14 (Klik nama `Edit Target Renamed {runId}-053` untuk membuka Popup Detail...); langkah 17 (Tutup Popup Detail Group); langkah 24 (Klik nama group untuk membuka Popup Detail Group); langkah 27 (Tutup Popup Detail Group); langkah 33 (Klik nama group untuk membuka Popup Detail Group); langkah 36 (Tutup Popup Detail Group); langkah 39 (Klik `(←)` pada kotak Search).
- Langkah 1 mencari baris target (R-16); node yang di-seed diubah berurutan oleh TC-FA-GRP-161, 162, dan 163 sehingga tiap blok memakai nama dan Code hasil blok sebelumnya (data milik spec ini).
- Alasan spec melewati ~35 langkah (39 langkah): keempat TC satu kelas (fungsional Edit Group), satu dataset (node `Edit Target` milik spec), dan tiap blok berdiri sendiri; langkah banyak karena `Verifikasi` per klausa Expected (S-01) dan langkah penghubung membuka Detail.
- Temuan untuk QA:
  - TC-FA-GRP-161, 162, dan 163 Post Condition "Changelog: tepat 1 baris Edit Field ..." tidak punya langkah observasi di TC; tidak diasersi di spec ini.
  - TC-FA-GRP-161 Expected b dan TC-FA-GRP-162 Expected b menyebut hasil di "header Popup Detail Group" tanpa langkah membuka Detail; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-163 Expected b menyebut Description baru "hanya" tampil di header Popup Detail Group; spec mengasersi tampil di header dan tidak mengasersi ketiadaan di tempat lain (tabel dan sidebar tidak punya kolom Description).
  - TC-FA-GRP-160 menyebut Edit Target "Code ET"; Code `ET` literal dipakai dengan pembersihan di hook `before` dan `after` karena Code auto-generate tidak relevan (S-12).

