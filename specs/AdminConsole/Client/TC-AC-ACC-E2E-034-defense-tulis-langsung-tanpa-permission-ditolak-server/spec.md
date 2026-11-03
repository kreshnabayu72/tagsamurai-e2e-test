---
id: TC-AC-ACC-E2E-034-defense-tulis-langsung-tanpa-permission-ditolak-server
title: "Defense-in-depth: Aksi Tulis Langsung (Create/Edit/Suspend/Delete/Change Partner) tanpa Permission Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-450
  - TC-AC-ACC-621
  - TC-AC-ACC-622
  - TC-AC-ACC-623
  - TC-AC-ACC-624
  - TC-AC-ACC-625
coverage:
  web: automated
---

# Defense-in-depth: Aksi Tulis Langsung (Create/Edit/Suspend/Delete/Change Partner) tanpa Permission Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-02 | Read Only (Principal) | `readOnlyPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_RO_PASSWORD` |
| A-ROL-5 | Active-Delete-Archived-Read (Manage active client: Delete + Read; Manage archived client: Read; exact-match Area Jakarta) | `activeDeleteArchivedReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_DELETE_ARCHIVED_READ_PASSWORD` |
| A-ROL-6 | Archived-Delete-Active-Read (Manage archived client: Delete + Read; Manage active client: Read; exact-match Area Jakarta) | `archivedDeleteActiveReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ARCHIVED_DELETE_ACTIVE_READ_PASSWORD` |
| A-ROL-7 | Active-Update-Archived-Read (Manage active client: Update + Read; Manage archived client: Read; exact-match Area Jakarta) | `activeUpdateArchivedReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_UPDATE_ARCHIVED_READ_PASSWORD` |
| A-ROL-8 | Archived-Update-Active-Read (Manage archived client: Update + Read; Manage active client: Read; exact-match Area Jakarta) | `archivedUpdateActiveReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ARCHIVED_UPDATE_ACTIVE_READ_PASSWORD` |
| A-14 | Partner Total Control (CV Mitra Sejati) | `totalControlPartner_automated_cvMitraSejati@qwertysystem.net` | `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD` |

- Login di hook `before` spec ini (Read Only, A-02); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Target request ditolak memakai Client milik spec (S-06), di-seed lewat Fixture BE di hook `before` dan dihapus di hook `after`: `PT Uji Defense Aktif {runId}-034` (Active, Group `Area Jakarta`, Direct, tanpa riwayat subscription; menggantikan `PT Ubah Mitra 08` pada TC-AC-ACC-622 dan 624 serta target Edit/Suspend/Delete pada TC-AC-ACC-450), `PT Uji Defense Arsip {runId}-034` (Archived, Group `Area Jakarta`; menggantikan `PT Karya Abadi` pada TC-AC-ACC-621 dan 623), dan `PT Uji Defense Partner {runId}-034` (Active, Group `Area Jakarta`, satu-satunya Partner CV Mitra Sejati; menggantikan `PT Ubah Mitra 09` pada TC-AC-ACC-625). Nilai uji: PIC Name `Hendra Pratama`; request Create memakai Company Name `PT Uji Defense Create {runId}-034`; request Change Partner menambah `CV Mitra Lestari`.
- Kemampuan teknis: Sesi API aktor (suite.md): klien HTTP dengan token sesi aktor (login API tiap akun, tanpa mengusir sesi UI; kemampuan disediakan tim BE/FE) untuk request langsung ke server tanpa melalui browser pada TC-AC-ACC-450 dan 621 sampai 625. Kemampuan Fixture BE untuk membaca state Client (nama, PIC Name, status, relasi Partner) sebelum dan sesudah request.
- Asersi tentang data tidak berubah memakai Fixture BE (state data, bagian 8b butir 1) dan layar Detail/List yang sama.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-450: Aksi tulis tanpa permission ditolak server (Create/Update/Delete)

1. Catat state Client `PT Uji Defense Aktif {runId}-034` lewat Fixture BE (nama, PIC Name, status; baseline)
2. Kirim request Create Client dengan Company Name `PT Uji Defense Create {runId}-034` langsung memakai token sesi Read Only
3. Kirim request Edit untuk `PT Uji Defense Aktif {runId}-034` langsung memakai token sesi Read Only
4. Kirim request Suspend untuk `PT Uji Defense Aktif {runId}-034` langsung memakai token sesi Read Only
5. Kirim request Delete untuk `PT Uji Defense Aktif {runId}-034` langsung memakai token sesi Read Only
6. Verifikasi keempat request ditolak server (tidak ada respons sukses 2xx)
7. Verifikasi data tidak berubah: state `PT Uji Defense Aktif {runId}-034` sama dengan baseline dan Client `PT Uji Defense Create {runId}-034` tidak ada
8. Tunggu aksi selesai
9. Logout dari akun Read Only
10. Login sebagai Active-Delete-Archived-Read (A-ROL-5)

### TC-AC-ACC-621: Delete Client Archived oleh pemegang Delete pada Manage active client tanpa Delete pada Manage archived client ditolak

11. Klik sub-tab `Archived`, ketik Search `PT Uji Defense Arsip {runId}-034`, tekan Enter, lalu buka `⋯` baris `PT Uji Defense Arsip {runId}-034`
12. Verifikasi menu `⋯` hanya memuat `Detail`
13. Kirim request HTTP Delete untuk `PT Uji Defense Arsip {runId}-034` langsung ke server memakai token Sesi API aktor yang sama, tanpa melalui browser
14. Verifikasi request ditolak server dengan respons `403 Forbidden`
15. Verifikasi `PT Uji Defense Arsip {runId}-034` tetap tampil di sub-tab `Archived`
16. Tutup menu `⋯`, lalu klik `(←)` pada kotak Search
17. Logout dari akun Active-Delete-Archived-Read
18. Login sebagai Archived-Delete-Active-Read (A-ROL-6)

### TC-AC-ACC-622: Delete Client Active tanpa riwayat oleh pemegang Delete pada Manage archived client tanpa Delete pada Manage active client ditolak

19. Ketik Search `PT Uji Defense Aktif {runId}-034`, tekan Enter, lalu buka `⋯` baris `PT Uji Defense Aktif {runId}-034` di sub-tab `Active`
20. Verifikasi menu `⋯` hanya memuat `Detail`
21. Kirim request HTTP Delete untuk `PT Uji Defense Aktif {runId}-034` langsung ke server memakai token Sesi API aktor yang sama, tanpa melalui browser
22. Verifikasi request ditolak server dengan respons `403 Forbidden`
23. Verifikasi `PT Uji Defense Aktif {runId}-034` tetap tampil di sub-tab `Active`
24. Tutup menu `⋯`, lalu klik `(←)` pada kotak Search
25. Logout dari akun Archived-Delete-Active-Read
26. Login sebagai Active-Update-Archived-Read (A-ROL-7)

### TC-AC-ACC-623: Edit Client Archived oleh pemegang Update pada Manage active client tanpa Update pada Manage archived client ditolak

27. Klik sub-tab `Archived`, ketik Search `PT Uji Defense Arsip {runId}-034`, tekan Enter, lalu buka `⋯` baris `PT Uji Defense Arsip {runId}-034`
28. Verifikasi menu `⋯` hanya memuat `Detail`
29. Kirim request HTTP Edit untuk `PT Uji Defense Arsip {runId}-034` dengan PIC Name `Hendra Pratama` langsung ke server memakai token Sesi API aktor yang sama, tanpa melalui browser
30. Verifikasi request ditolak server dengan respons `403 Forbidden`
31. Buka Detail `PT Uji Defense Arsip {runId}-034`
32. Verifikasi Detail `PT Uji Defense Arsip {runId}-034` tidak menampilkan PIC Name `Hendra Pratama`
33. Kembali ke List dengan tombol Back browser, lalu klik `(←)` pada kotak Search
34. Logout dari akun Active-Update-Archived-Read
35. Login sebagai Archived-Update-Active-Read (A-ROL-8)

### TC-AC-ACC-624: Edit Client Active oleh pemegang Update pada Manage archived client tanpa Update pada Manage active client ditolak

36. Ketik Search `PT Uji Defense Aktif {runId}-034`, tekan Enter, lalu buka `⋯` baris `PT Uji Defense Aktif {runId}-034` di sub-tab `Active`
37. Verifikasi menu `⋯` hanya memuat `Detail`
38. Kirim request HTTP Edit untuk `PT Uji Defense Aktif {runId}-034` dengan PIC Name `Hendra Pratama` langsung ke server memakai token Sesi API aktor yang sama, tanpa melalui browser
39. Verifikasi request ditolak server dengan respons `403 Forbidden`
40. Ketik Search `PT Uji Defense Aktif {runId}-034`, tekan Enter, lalu buka Detail `PT Uji Defense Aktif {runId}-034`
41. Verifikasi Detail `PT Uji Defense Aktif {runId}-034` tidak menampilkan PIC Name `Hendra Pratama`
42. Kembali ke List dengan tombol Back browser, lalu klik `(←)` pada kotak Search
43. Logout dari akun Archived-Update-Active-Read
44. Login sebagai Partner Total Control (CV Mitra Sejati) (A-14)

### TC-AC-ACC-625: Partner mengirim request Change Partner langsung ditolak server

45. Ketik Search `PT Uji Defense Partner {runId}-034`, tekan Enter, lalu buka `⋯` baris `PT Uji Defense Partner {runId}-034`
46. Verifikasi menu `⋯` tidak memuat Change Partner
47. Kirim request HTTP Change Partner untuk `PT Uji Defense Partner {runId}-034` dengan tambahan Partner `CV Mitra Lestari` langsung ke server memakai token Sesi API aktor yang sama, tanpa melalui browser
48. Verifikasi request ditolak server dengan respons `403 Forbidden`
49. Lihat sel Managed By baris `PT Uji Defense Partner {runId}-034`
50. Verifikasi Managed By adalah `CV Mitra Sejati` tanpa `+1 more`
51. Tutup menu `⋯`, lalu klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 8 sampai 10, 16 sampai 18, 24 sampai 26, 33 sampai 35, 42 sampai 44, 51. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- K-1: spec kelas a (defense-in-depth) yang Expected-nya berupa respons API dan state data (TC-AC-ACC-450: request Create/Edit/Suspend/Delete langsung ditolak, data tidak berubah) tetap masuk spec FE+BE walau tumpang tindih dengan `tc-client-backend.md`; asersi TC-AC-ACC-450 hanya status respons dan state data (bagian 8b butir 1), tanpa asersi tampilan.
- TC-AC-ACC-621 sampai 625: request dikirim langsung ke server lewat klien HTTP tanpa browser (Sesi API aktor); asersi hanya respons `403 Forbidden` dan state data/tampilan List atau Detail, tanpa asersi toast (bagian 8b butir 1).
- Penyimpangan data (S-06): TC menyebut Client Pre-setup/A3 (`PT Karya Abadi`, `PT Ubah Mitra 08`, `PT Ubah Mitra 09`) sebagai target; spec memakai Client milik spec bersuffix karena request langsung yang diuji ditolak tetap memakai data milik spec; Group, status, dan relasi Partner Client mengikuti kondisi Client Pre-setup yang dirujuk TC.
- Pembagian TC lintas spec: defense tulis di luar scope (TC-AC-ACC-454, 987) di spec 035; XSS (TC-AC-ACC-452) di spec 036.
- Ukuran spec (51 langkah, melewati sekitar 35 langkah): semua blok satu kelas harness (defense-in-depth kelas a, tanpa harness eksternal), enam role berbeda dengan langkah berbeda sehingga ganti akun eksplisit di tiap akhir blok; tiap blok dimulai dari ganti akun dan Search eksplisit dan tidak bergantung pada hasil blok sebelumnya (request ditolak tidak mengubah data); langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-450: langkah "Kirim request Create, Edit, Suspend, Delete langsung" tidak menyebut target Client, payload Create, maupun status kode yang diharapkan (hanya "Semua ditolak; data tidak berubah"); spec memakai Client milik spec dan mengasersi penolakan tanpa kode tertentu.
