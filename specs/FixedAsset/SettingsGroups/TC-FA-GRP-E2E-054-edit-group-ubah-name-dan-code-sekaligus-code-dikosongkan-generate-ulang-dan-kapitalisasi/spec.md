---
id: TC-FA-GRP-E2E-054-edit-group-ubah-name-dan-code-sekaligus-code-dikosongkan-generate-ulang-dan-kapitalisasi
title: "Edit Group: Ubah Name dan Code Sekaligus, Code Dikosongkan Di-Generate Ulang, Code Identik Diperlakukan No-Op, dan Nama Sama Beda Kapitalisasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-164
  - TC-FA-GRP-165
  - TC-FA-GRP-166
  - TC-FA-GRP-167
coverage:
  web: automated
---

# Edit Group: Ubah Name dan Code Sekaligus, Code Dikosongkan Di-Generate Ulang, Code Identik Diperlakukan No-Op, dan Nama Sama Beda Kapitalisasi

## Prerequisites

- Mode: FE+BE (backend nyata; Edit Group menulis data, TC-FA-GRP-166 mengasersi tidak adanya pencatatan log berbaseline).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-054` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script):
  - TC-FA-GRP-164: node `Multi Edit Src {runId}-054` (Code `MSRC`, Description `Multi desc`, Function Assignable) diubah menjadi Name `Multi Edit {runId}-054` dan Code `MED`.
  - TC-FA-GRP-165: node literal `Room 302` (Code `R3X`; Name literal karena Code auto-generate `R302` diturunkan dari Name; lihat Temuan untuk QA).
  - TC-FA-GRP-166: Head Office (Code `HO`, Pre-setup) hanya sebagai target no-op: spec tidak mengubah Head Office, Modified By dan Last Updated Head Office tidak berubah (S-06).
  - TC-FA-GRP-167: node `Edit Target {runId}-054` (Code `ET`, Description kosong), diubah menjadi Name `EDIT TARGET {runId}-054` dan Description `Self Check`.
- Kemampuan teknis: pembacaan jumlah entri Changelog Head Office dan node target, System Log, dan Activity Log sebelum dan sesudah aksi (disediakan tim FE/BE; selisih terhadap baseline, S-12); jam server dan jam browser sinkron untuk asersi Last Updated (toleransi satu menit).
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-054`, group literal `Room 302`, dan group ber-Code literal `ET`, `MED`, `MSRC`, `R3X`, `R302` yang dibuat spec ini (hook `before` juga menghapus sisa literal run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Multi Edit Src {runId}-054`, tekan Enter

### TC-FA-GRP-164: Ubah Name dan Code sekaligus

2. Buka elipsis (⋯) baris `Multi Edit Src {runId}-054`, klik Edit, ubah Name menjadi `Multi Edit {runId}-054` dan Code menjadi `MED`, lalu klik [Save]
3. Verifikasi toast sukses `Success, group has been updated.`
4. Ganti isi kotak Search dengan `Multi Edit {runId}-054`, tekan Enter
5. Verifikasi Name `Multi Edit {runId}-054` dan Code `MED` baru tampil pada baris
6. Buka Popup Detail Group baris `Multi Edit {runId}-054`
7. Verifikasi Function Assignable tetap di Popup Detail Group

### TC-FA-GRP-165: Code dikosongkan di-generate ulang dari Name saat ini

8. Verifikasi Description `Multi desc` tetap di Popup Detail Group
9. Tutup Popup Detail Group
10. Ganti isi kotak Search dengan `Room 302`, tekan Enter
11. Buka elipsis (⋯) baris `Room 302`, klik Edit, kosongkan Code, lalu klik [Save]
12. Verifikasi toast sukses `Success, group has been updated.`
13. Verifikasi Code menjadi `R302` (hasil generate dari Name), bukan kosong

### TC-FA-GRP-167: Name sama dengan dirinya sendiri (beda kapitalisasi) tidak duplikat, tercatat bila field lain ikut berubah

14. Catat jumlah entri Changelog node `Edit Target {runId}-054` sebagai baseline, lalu ganti isi kotak Search dengan `Edit Target {runId}-054`, tekan Enter
15. Buka elipsis (⋯) baris `Edit Target {runId}-054`, klik Edit, ubah huruf besar/kecil Name (`EDIT TARGET {runId}-054`) dan ubah Description menjadi `Self Check`, lalu klik [Save]
16. Verifikasi tidak ada error duplikat (exclude diri sendiri)
17. Verifikasi toast sukses `Success, group has been updated.`
18. Verifikasi Group Name tersimpan `EDIT TARGET {runId}-054` pada baris tabel
19. Verifikasi Changelog node bertambah tepat 2 baris Edit terhadap baseline langkah 14: Field Description (`Self Check`) dan Field Group Name (Old Value `Edit Target {runId}-054`, New Value `EDIT TARGET {runId}-054`)

### TC-FA-GRP-166: Code dikosongkan menghasilkan kode identik, tanpa baris log Code

20. Catat jumlah entri Changelog Head Office, System Log, dan Activity Log sebagai baseline, serta Modified By dan Last Updated Head Office (dibaca lewat fixture BE)
21. Buka elipsis (⋯) node Head Office di sidebar, klik Edit, kosongkan Code, lalu klik [Save]
22. Verifikasi toast netral `No changes to save.` (diperlakukan Edit No-Op)
23. Ganti isi kotak Search dengan `Head Office`, tekan Enter
24. Verifikasi Code pada baris tabel Head Office tetap `HO` (kandidat yang hanya bentrok dengan Code node sendiri tidak dihitung bentrok)
25. Verifikasi Modified By dan Last Updated Head Office tidak berubah terhadap baseline langkah 20
26. Verifikasi tidak ada baris baru di Changelog Head Office, System Log, dan Activity Log: jumlah entri sama dengan baseline langkah 20
27. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-164, 165, 167, lalu TC-FA-GRP-166 di akhir (target no-op pada Pre-setup); berbeda dari urutan nomor TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Multi Edit Src {runId}-054`, tekan Enter); langkah 4 (Ganti isi kotak Search dengan `Multi Edit {runId}-054`, tekan Enter; Search `Multi Edit Src {runId}-054` tidak lagi cocok dengan baris yang sudah diganti namanya); langkah 6 (Buka Popup Detail Group baris `Multi Edit {runId}-054`); langkah 9 (Tutup Popup Detail Group); langkah 10 (Ganti isi kotak Search dengan `Room 302`, tekan Enter); langkah 14 (Catat jumlah entri Changelog node `Edit Target {runId}-054` sebagai baseline, lalu ganti isi kotak Search dengan `Edit Target {runId}-054`, tekan Enter); langkah 20 (Catat jumlah entri Changelog Head Office, System Log, dan Activity Log sebagai baseline, serta Modified By dan Last Updated Head Office, dibaca lewat fixture BE); langkah 23 (Ganti isi kotak Search dengan `Head Office`, tekan Enter, sesudah toast netral langkah 22 diasersi; Search `Edit Target {runId}-054` menyaring Head Office keluar dari tabel dan Code `HO` dibaca dari baris tabel). Popup Detail Group dibuka sebelum Description diverifikasi dan ditutup sesudahnya (S-03). Langkah 27 (Klik `(←)` pada kotak Search) menutup Search di akhir spec (S-09).
- Langkah Search (langkah 1 dan Search TC-FA-GRP-165, 167) mencari baris target (R-16).
- Asersi "tanpa baris log" TC-FA-GRP-166 ditulis sebagai `Verifikasi` berbaseline jumlah entri di spec ini (S-12); tidak ada rujukan ke spec absence.
- Temuan untuk QA:
  - TC-FA-GRP-164, 165, 167 Post Condition "Changelog ..." tidak punya langkah observasi di TC kecuali TC-FA-GRP-167 (Expected c memuat baris Changelog); Post Condition lain tidak diasersi di spec ini.
  - TC-FA-GRP-165 mengharuskan Name `Room 302` agar Code `R302`; Code auto-generate diturunkan dari token Name sehingga suffix per run mengubah hasil Code. Nama literal dipakai (pengecualian A-8) dengan pembersihan di hook `before` dan `after`; butuh butir Lampiran A modul Groups (S-12).
  - Nama literal TC-FA-GRP-165 `Room 301` juga dipakai spec 068 (TC-FA-GRP-321); spec ini memakai `Room 302` (Code hasil `R302`, seed Code `R3X`) agar nama literal berbeda antar spec (A-8). Penyimpangan dari Data Uji TC ini perlu persetujuan QA.
  - TC-FA-GRP-166 memakai Head Office Pre-setup sebagai target no-op; tidak ada yang berubah (pengecualian S-06 untuk aksi no-op).
  - TC-FA-GRP-166 Expected b menyebut tiga log sekaligus ("tidak ada baris Changelog/System Log/Activity Log"); spec membacanya lewat kemampuan baca log yang disediakan tim FE/BE.

