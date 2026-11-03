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
10. Catat waktu sesudah [Save]
11. Verifikasi popup tertutup
12. Verifikasi toast sukses `Success, group has been updated.`
13. Ganti isi kotak Search dengan `Edit Target Renamed {runId}-053`, tekan Enter
14. Verifikasi nama baru `Edit Target Renamed {runId}-053` tampil di tabel
15. Verifikasi nama baru tampil di sidebar
16. Klik nama `Edit Target Renamed {runId}-053` untuk membuka Popup Detail Group
17. Verifikasi nama baru tampil di header Popup Detail Group
18. Verifikasi field lain tidak berubah (Code `ET`, Description `Edit me`, Function Assignable)
19. Tutup Popup Detail Group
20. Verifikasi Modified By = aktor (format `[First Name] [Last Initial]`) pada baris `Edit Target Renamed {runId}-053`
21. Verifikasi Last Updated = waktu save yang dicatat pada langkah 10 (toleransi satu menit)

### TC-FA-GRP-162: Edit Group, ubah Code saja

22. Buka elipsis (⋯) baris `Edit Target Renamed {runId}-053`, klik Edit, ubah Code menjadi `ETR`, lalu klik [Save]
23. Catat waktu sesudah [Save]
24. Verifikasi popup tertutup
25. Verifikasi toast sukses `Success, group has been updated.`
26. Verifikasi kolom Code menampilkan `ETR`
27. Klik nama group untuk membuka Popup Detail Group
28. Verifikasi header Popup Detail Group menampilkan Code `ETR`
29. Verifikasi field lain tidak berubah (Name `Edit Target Renamed {runId}-053`, Description `Edit me`, Function Assignable)
30. Tutup Popup Detail Group
31. Verifikasi Modified By = aktor (format `[First Name] [Last Initial]`)
32. Verifikasi Last Updated = waktu save yang dicatat pada langkah 23 (toleransi satu menit)

### TC-FA-GRP-163: Edit Group, ubah Description saja

33. Buka elipsis (⋯) baris `Edit Target Renamed {runId}-053`, klik Edit, ubah Description menjadi `Updated notes`, lalu klik [Save]
34. Catat waktu sesudah [Save]
35. Verifikasi popup tertutup
36. Verifikasi toast sukses `Success, group has been updated.`
37. Klik nama group untuk membuka Popup Detail Group
38. Verifikasi Description baru `Updated notes` tampil di header Popup Detail Group
39. Verifikasi field lain tidak berubah (Name `Edit Target Renamed {runId}-053`, Code `ETR`, Function Assignable)
40. Tutup Popup Detail Group
41. Verifikasi Modified By = aktor (format `[First Name] [Last Initial]`)
42. Verifikasi Last Updated = waktu save yang dicatat pada langkah 34 (toleransi satu menit)
43. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Edit Target {runId}-053`, tekan Enter); langkah 16 (Klik nama `Edit Target Renamed {runId}-053` untuk membuka Popup Detail Group); langkah 19 (Tutup Popup Detail Group); langkah 27 (Klik nama group untuk membuka Popup Detail Group); langkah 30 (Tutup Popup Detail Group); langkah 37 (Klik nama group untuk membuka Popup Detail Group); langkah 40 (Tutup Popup Detail Group); langkah 43 (Klik `(←)` pada kotak Search). Langkah 13 (Ganti isi kotak Search dengan `Edit Target Renamed {runId}-053`, tekan Enter; Search `Edit Target {runId}-053` tidak lagi cocok dengan baris yang sudah diganti namanya) dan langkah 10, 23, 34 (Catat waktu sesudah [Save], pembanding Last Updated TC-FA-GRP-161, 162, 163; S-12).
- Langkah 1 mencari baris target (R-16); node yang di-seed diubah berurutan oleh TC-FA-GRP-161, 162, dan 163 sehingga tiap blok memakai nama dan Code hasil blok sebelumnya (data milik spec ini).
- Alasan spec melewati ~35 langkah (43 langkah): keempat TC satu kelas (fungsional Edit Group), satu dataset (node `Edit Target` milik spec), dan tiap blok berdiri sendiri; langkah banyak karena `Verifikasi` per klausa Expected (S-01) dan langkah penghubung membuka Detail.
- Temuan untuk QA:
  - TC-FA-GRP-161, 162, dan 163 Post Condition "Changelog: tepat 1 baris Edit Field ..." tidak punya langkah observasi di TC; tidak diasersi di spec ini.
  - TC-FA-GRP-161 Expected b dan TC-FA-GRP-162 Expected b menyebut hasil di "header Popup Detail Group" tanpa langkah membuka Detail; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-163 Expected b menyebut Description baru "hanya" tampil di header Popup Detail Group; spec mengasersi tampil di header dan tidak mengasersi ketiadaan di tempat lain (tabel dan sidebar tidak punya kolom Description).
  - TC-FA-GRP-160 menyebut Edit Target "Code ET"; Code `ET` literal dipakai dengan pembersihan di hook `before` dan `after` karena Code auto-generate tidak relevan (S-12).

