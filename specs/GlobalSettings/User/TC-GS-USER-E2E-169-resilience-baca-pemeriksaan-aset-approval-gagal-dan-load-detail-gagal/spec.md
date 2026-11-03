---
id: TC-GS-USER-E2E-169-resilience-baca-pemeriksaan-aset-approval-gagal-dan-load-detail-gagal
title: "Resilience Baca User: Pemeriksaan Aset dan Approval pada Dialog Deactivate Gagal Menampilkan Baris Fallback, dan Load Header serta General Information Detail Gagal dengan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-1112
  - TC-GS-USER-1124
coverage:
  web: automated
---

# Resilience Baca User: Pemeriksaan Aset dan Approval pada Dialog Deactivate Gagal Menampilkan Baris Fallback, dan Load Header serta General Information Detail Gagal dengan Try Again

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness b: fault injection, bagian 3 prinsip 13 dan bagian 6 konvensi). Aksi `[Deactivate]` pada TC-GS-USER-1112 memakai backend nyata dan mengasersi state switch.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tidak dipakai sebagai target aksi dan tidak diubah (S-06).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Activated, Division `Finance`, Access `Fixed Asset`, email `<nama tanpa spasi huruf kecil>+{runId}-169@qwertysystem.net`:
  - `Dewi Lestari {runId}-169`: Active, tanpa aset aktif dan tanpa approval in-flight; target Deactivate pada TC-GS-USER-1112.
  - `Ahmad Fauzi {runId}-169`: Active; target pembukaan Detail pada TC-GS-USER-1124.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE (TC dan PRD tidak menyebut nama endpoint):
  - Respons pemeriksaan aset aktif dan approval pada dialog Deactivate (TC-GS-USER-1112): ditahan melampaui batas waktu klien sehingga pemeriksaan gagal (timeout). Durasi tahanan ditentukan tim FE.
  - Respons detail user (TC-GS-USER-1124): ditahan 3 detik lalu dijawab 5xx (500) tanpa meneruskan request ke backend. Pilihan 3 detik adalah pilihan spec (TC hanya menyebut "lambat lalu gagal").
- Kemampuan teknis: mengamati skeleton pada header dan kartu General Information selama respons ditahan.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): lepas semua intercept, hapus kedua user seed lewat API.

## Test Steps

### Persiapan

1. Ketik Search `Dewi Lestari {runId}-169`, tekan Enter

### TC-GS-USER-1112: Dialog Deactivate, pemeriksaan aset dan approval gagal menampilkan baris fallback dan aksi tetap dapat dilanjutkan

2. Pasang intercept pada respons pemeriksaan aset aktif dan approval: tahan melampaui batas waktu klien (timeout)
3. Klik switch Active baris `Dewi Lestari {runId}-169`
4. Verifikasi dialog `Deactivate User` tetap tampil
5. Verifikasi body dialog memuat `We couldn't check this user's active assets or pending approvals. You can still continue.`
6. Verifikasi baris peringatan aset `Dewi Lestari {runId}-169 is currently holding active assets (Borrowed / Assigned). Asset custody will remain recorded under this user until manually transferred or returned.` dan baris approval `Pending approvals of this user will be reassigned to other approvers.` tidak tampil
7. Verifikasi tombol `[Deactivate]` enabled
8. Lepas intercept respons pemeriksaan aset aktif dan approval
9. Klik `[Deactivate]`
10. Verifikasi toast sukses "Success, user has been deactivated."
11. Verifikasi switch Active baris `Dewi Lestari {runId}-169` OFF

### TC-GS-USER-1124: Header dan General Information, Loading skeleton dan Error load dengan Try Again

12. Ganti isi kotak search dengan `Ahmad Fauzi {runId}-169`, tekan Enter
13. Pasang intercept pada respons detail user: tahan 3 detik lalu jawab 5xx
14. Klik Name `Ahmad Fauzi {runId}-169` di User List
15. Verifikasi skeleton tampil pada Header Detail selama memuat
16. Verifikasi skeleton tampil pada kartu General Information selama memuat
17. Verifikasi setelah gagal Detail menampilkan teks `"Unable to load this data."`
18. Verifikasi setelah gagal Detail menampilkan tombol `[Try Again]`
19. Verifikasi Detail tidak menampilkan empty state
20. Lepas intercept respons detail user sehingga endpoint pulih
21. Klik `[Try Again]`
22. Verifikasi Header Detail menampilkan nama `Ahmad Fauzi {runId}-169`
23. Verifikasi kartu General Information menampilkan data user

## Notes

- Mode: FE+BE (intercept parsial, kelas harness b: fault injection; bagian 6 konvensi). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. Kedua TC berada di kelas harness b (kegagalan baca yang dipaksakan lewat intercept), satu akun, dan user seed masing-masing.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 dan 12 (Search; langkah 12 mengganti isi kotak search yang sudah berisi), 2, 8, 13, dan 20 (memasang dan melepas intercept), 3 (membuka dialog), 9 (`[Deactivate]` dikonfirmasi setelah intercept dilepas), 14 (membuka Detail), dan 21 (`[Try Again]` setelah endpoint pulih).
- Asersi absence (langkah 6 dan 19) berada pada surface yang sudah menampilkan pembandingnya pada langkah sebelumnya (teks fallback pada langkah 5; teks error dan `[Try Again]` pada langkah 17 dan 18).
- Pembagian TC lintas spec: dialog Deactivate dengan pemeriksaan sukses (peringatan aset dan approval) ada di spec 167 dan 047; error load User List, Modal Changelog, dan tab Detail dengan `[Try Again]` ada di spec 007.
- Temuan untuk QA:
  - TC-GS-USER-1112 menulis precondition "Pemeriksaan aset aktif dan approval dibuat gagal (timeout)" tanpa nama endpoint dan durasi timeout; spec memicu lewat `Spectra.intercept()` dan nama endpoint serta durasi ditentukan tim FE.
  - TC-GS-USER-1124 menulis "lambat lalu gagal" tanpa durasi; spec memakai tahan 3 detik. Expected c ("data tampil") tidak merinci data; spec mengasersi nama pada Header dan kartu General Information tampil.
  - TC-GS-USER-1112 dan TC-GS-USER-1124 memakai Dewi Lestari dan Ahmad Fauzi Pre-setup; spec memakai seed bersuffix milik spec (S-06, S-12).
