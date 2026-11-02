---
id: TC-FA-GRP-E2E-279-konflik-dua-admin-edit-bersamaan-last-write-wins-dan-code-auto-generate-bentrok
title: "Konflik Dua Admin: Edit Node yang Sama (Last-Write-Wins) dan Code Auto-Generate Bentrok dengan Retry Otomatis"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-190
  - TC-FA-GRP-334
  - TC-FA-GRP-335
coverage:
  web: automated
---

# Konflik Dua Admin: Edit Node yang Sama (Last-Write-Wins) dan Code Auto-Generate Bentrok dengan Retry Otomatis

## Prerequisites

- Mode: FE+BE (backend nyata; kelas c multi-konteks: dua admin pada client Professional. TC-FA-GRP-190 memakai dua konteks UI karena hasil di kedua konteks diasersi; TC-FA-GRP-334 dan TC-FA-GRP-335 menekan [Submit] bersamaan).
- Akun aktor: Total Control A `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), `Spectra.env.FA_TC_PASSWORD`; Total Control B (user Total Control kedua client yang sama; konteks UI kedua), `Spectra.env.FA_TC_B_PASSWORD`. Kedua nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; email akun B tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Login A di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite; konteks UI B dibuka dan ditutup lewat langkah eksplisit.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8); Warehouse A (Code `WH-A`) dan Head Office (Code `HO`) sebagai dua parent berbeda untuk TC-FA-GRP-334.
- Data Dinamis bersuffix `{runId}-279` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-190: node `LWW Node {runId}-279` (di-seed lewat API di hook `before`, Description awal kosong), Description A `A`, Description B `B`. TC-FA-GRP-334: Name literal `Main Lab` (tanpa suffix karena Code auto-generate diturunkan dari Name; hasil Code `ML` dan `ML2`), dibuat A di bawah Warehouse A dan B di bawah Head Office. TC-FA-GRP-335: Name literal `Retry Lab`, Code kosong.
- Kemampuan teknis: dua konteks browser terpisah (A dan B) yang menekan [Submit] atau [Save] bersamaan; pembacaan jumlah entri Changelog node lewat kemampuan baca Changelog (disediakan tim FE/BE, dicatat sebagai selisih terhadap baseline sebelum aksi); simulasi bentrok ganda Code (kandidat dan suffix berikutnya diambil request lain bersamaan) untuk TC-FA-GRP-335, disediakan tim BE (tidak disebut di TC, PRD, atau LLD).
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-279` dan group literal `Main Lab`, `Retry Lab`, serta group yang Code-nya `ML`, `ML2`, `RL`, `RL2` yang dibuat spec ini (hook `before` juga menghapus sisa literal run sebelumnya); tutup konteks UI B.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-190: Dua aktor mengedit node yang sama (last-write-wins)

1. Catat jumlah entri Changelog `LWW Node {runId}-279` sebagai baseline, lalu buka konteks UI B dan login sebagai Total Control B
2. Konteks A dan B sama-sama membuka Edit `LWW Node {runId}-279`
3. Konteks A mengubah Description menjadi `A`, lalu klik [Save]
4. Verifikasi konteks A menampilkan toast `Success, group has been updated.` tanpa 409
5. Konteks B mengubah Description menjadi `B`, lalu klik [Save]
6. Verifikasi konteks B menampilkan toast `Success, group has been updated.` tanpa 409
7. Buka Popup Detail Group `LWW Node {runId}-279`
8. Verifikasi nilai akhir Description = `B` (seluruh field form B menimpa)
9. Verifikasi Changelog mencatat kedua perubahan: jumlah entri bertambah 2 terhadap baseline
10. Tutup Popup Detail Group dan konteks UI B

### TC-FA-GRP-334: Code auto-generate bersamaan bentrok, retry otomatis sekali

11. Buka konteks UI B dan login sebagai Total Control B
12. Konteks A klik Add Subgroup pada Warehouse A, konteks B klik Add Subgroup pada Head Office, keduanya mengisi Group Name `Main Lab` dengan Code kosong
13. Konteks A dan B menekan [Submit] bersamaan
14. Verifikasi keduanya sukses (tanpa error)
15. Verifikasi salah satu group mendapat Code `ML` dan yang lain mendapat suffix berikutnya `ML2`
16. Tutup konteks UI B

### TC-FA-GRP-335: Retry juga bentrok, inline error dan popup tetap terbuka

17. Klik [+] Group, isi Group Name `Retry Lab` dengan Code kosong
18. Picu bentrok ganda: kandidat Code dan suffix berikutnya diambil request lain bersamaan, lalu klik [Submit]
19. Verifikasi inline error `Code already exists` pada field Code
20. Verifikasi popup tetap terbuka
21. Klik [Submit] ulang
22. Verifikasi aktor dapat submit ulang dan berhasil (toast sukses `Success, group has been created.`)

## Notes

- Mode: FE+BE (backend nyata, kelas c multi-konteks; bagian 3 prinsip 13 butir c). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Pembagian TC lintas spec: TC-FA-GRP-119, 123, 124, dan 974 (konflik batas plan dan platform) ada di spec 043; spec ini memuat konflik Edit dan Code auto-generate pada client Professional.
- TC-FA-GRP-334 dan TC-FA-GRP-190 non-deterministik pada konteks mana yang lebih dulu; asersi dirumuskan tanpa menentukan konteks (TC-FA-GRP-334 "salah satu group").
- TC-FA-GRP-335 memakai satu konteks UI; pemicu bentrok dari request lain disediakan tim BE dan bukan konteks UI kedua.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Catat jumlah entri Changelog `LWW Node {runId}-279` sebagai baseline, ...); langkah 7 (Buka Popup Detail Group `LWW Node {runId}-279`); langkah 10 (Tutup Popup Detail Group dan konteks UI B); langkah 11 (Buka konteks UI B dan login sebagai Total Control B); langkah 16 (Tutup konteks UI B).
- Temuan untuk QA:
  - Email dan password akun Total Control B client Professional tidak tertulis di Pre-setup TC; spec memakai env baru `FA_TC_B_PASSWORD` dan akun yang disediakan tim FE.
  - TC-FA-GRP-190 Expected c "Changelog mencatat kedua perubahan" tidak menyebut cara membaca Changelog; spec memakai Popup Detail Group (kemampuan baca Changelog) dengan selisih jumlah entri terhadap baseline (S-12).
  - TC-FA-GRP-190 menyebut "A & B membuka Edit" tanpa menyebut bahwa Description awal berbeda dari `A` dan `B`; spec men-seed Description awal kosong.
  - TC-FA-GRP-334 tidak menyebut parent B; spec memakai Head Office karena precondition menyebut parent berbeda dari A.
  - TC-FA-GRP-335 tidak menyebut cara memicu bentrok ganda; dicatat sebagai kemampuan "disediakan tim BE".
  - TC-FA-GRP-335 Expected b "aktor dapat Submit ulang dan berhasil" tidak menyebut toast; spec mengasersi toast sukses standar.

