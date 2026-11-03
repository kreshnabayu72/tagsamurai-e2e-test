---
id: TC-GS-NLU-E2E-120-state-tenant-plan-tier-dan-subscription-fams
title: "State tenant: plan tier dan subscription FAMS"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-454
  - TC-GS-NLU-464
coverage:
  web: automated
---

# State tenant: plan tier dan subscription FAMS

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; plan dan subscription Client adalah Pre-setup No. 15 dan tidak diubah spec ini. Tidak ada respons yang di-mock atau di-intercept.
- Role yang diuji (Total Control pada Client uji; password hanya lewat `Spectra.env`):

| Client | Plan | Akun | Env var password |
|---|---|---|---|
| PT Starter Mandiri | Starter | Total Control Client PT Starter Mandiri; email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.GS_PLANSTARTER_TC_PASSWORD` |
| PT Maju Bersama | Growth | Total Control Client PT Maju Bersama; email tidak tertulis di Pre-setup TC | `Spectra.env.GS_PLANGROWTH_TC_PASSWORD` |
| PT Profesional Jaya | Professional | Total Control Client PT Profesional Jaya; email tidak tertulis di Pre-setup TC | `Spectra.env.GS_PLANPRO_TC_PASSWORD` |
| PT Enterprise Raya | Enterprise | Total Control Client PT Enterprise Raya; email tidak tertulis di Pre-setup TC | `Spectra.env.GS_PLANENT_TC_PASSWORD` |
| PT Tanpa FAMS | subscription FAMS tidak aktif | Total Control Client PT Tanpa FAMS; email tidak tertulis di Pre-setup TC | `Spectra.env.GS_NOFAMS_TC_PASSWORD` |

- Environment variable: `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, `GS_PLANENT_TC_PASSWORD`, `GS_NOFAMS_TC_PASSWORD`.
- Login akun aktor pertama (Total Control PT Starter Mandiri) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup yang diasumsikan tersedia di tiap Client plan (hanya dibaca): Login User `Ahmad Fauzi` dan Division `Operations` (lihat Temuan untuk QA).
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE):
  - TC-GS-NLU-454: Non-Login User baru dibuat lewat UI di tiap Client plan: First Name `Plan`, Last Name `<Plan> {runId}-120` (`Starter`, `Growth`, `Professional`, `Enterprise`), Division `Operations`, Email `plan<plan>+{runId}-120@qwertysystem.net`, Represented By `Ahmad Fauzi`. Dihapus hook `after` lewat API.
  - TC-GS-NLU-464: Non-Login User `Detail Tanpa FAMS {runId}-120` di Client PT Tanpa FAMS.
- Ambang yang dibandingkan antar Client (TC-GS-NLU-454): daftar field popup Create First Name, Last Name, Position, Division, Employee ID, Email, Represented By.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-120` di semua Client uji tanpa mengasumsikan seeding berhasil penuh. State Client tidak diubah spec ini.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-454: Create Non-Login User identik di semua tier plan tanpa gating

1. Klik `[+ Non-Login User]` (Client PT Starter Mandiri, Plan Starter)
2. Verifikasi popup Create tidak menampilkan pesan gating, upsell, atau limit plan
3. Verifikasi popup Create memuat field First Name, Last Name, Position, Division, Employee ID, Email, dan Represented By
4. Isi First Name `Plan`, Last Name `Starter {runId}-120`, Division `Operations`, Email `planstarter+{runId}-120@qwertysystem.net`, lalu pilih Represented By `Ahmad Fauzi` lewat popup Select User
5. Klik `[Submit]`
6. Verifikasi Toast sukses `Success, non-login user has been created.`
7. Untuk setiap baris tabel Client plan berikut (Growth, Professional, Enterprise) lakukan langkah 8 sampai 14 dengan Last Name `<Plan> {runId}-120` dan env var password sesuai tabel Role yang diuji
8. Ganti akun: logout, lalu login sebagai Total Control Client baris tersebut; buka sub-tab Non-Login User lewat Global Settings > User > User List
9. Klik `[+ Non-Login User]`
10. Verifikasi popup Create tidak menampilkan pesan gating, upsell, atau limit plan
11. Verifikasi popup Create memuat field yang sama seperti Client PT Starter Mandiri (First Name, Last Name, Position, Division, Employee ID, Email, Represented By)
12. Isi First Name `Plan`, Last Name `<Plan> {runId}-120`, Division `Operations`, Email `plan<plan>+{runId}-120@qwertysystem.net`, lalu pilih Represented By `Ahmad Fauzi` lewat popup Select User
13. Klik `[Submit]`
14. Verifikasi Toast sukses `Success, non-login user has been created.`

### TC-GS-NLU-464: Detail Non-Login User pada Client tanpa subscription FAMS aktif tidak merender Tab Responsibilities

15. Ganti akun: logout, lalu login sebagai Total Control PT Tanpa FAMS (`Spectra.env.GS_NOFAMS_TC_PASSWORD`)
16. Buka sub-tab Non-Login User, ketik Search `Detail Tanpa FAMS {runId}-120`, tekan Enter, klik Name baris tersebut untuk membuka Detail
17. Verifikasi hanya tab `Changelog` yang tampil pada daftar tab Detail
18. Verifikasi tab `Responsibilities` beserta sub-tab `Borrowed Assets` dan `Assigned Assets` tidak dirender

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 16 (membuka sub-tab dan Search record yang dicari), langkah 8 dan 15 (ganti akun eksplisit, S-07).
- Langkah berulang (bagian 8b butir 7): langkah 8 sampai 14 diulang untuk Client Growth, Professional, dan Enterprise; parameter tiap iterasi (Last Name, Email, env var password) ada di tabel `## Prerequisites`, tanpa langkah bersyarat, `Verifikasi` tetap satu per klausa. Ekspansi: 6 langkah Starter + 3 iterasi × 7 langkah + 1 langkah pengulangan + 4 langkah TC-GS-NLU-464 = 18 langkah nominal sebelum ekspansi; dengan ekspansi sekitar 32 langkah.
- TC-GS-NLU-454 mengasersi bahwa perilaku popup identik antar-tier dengan membandingkan setiap Client dengan Client PT Starter Mandiri pada klausa yang sama.
- Temuan untuk QA:
  - TC-GS-NLU-454 dan 464 menyebut Client plan Starter, Growth, Professional, Enterprise dan PT Tanpa FAMS tanpa email akun; nama env password `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, `GS_PLANENT_TC_PASSWORD`, dan `GS_NOFAMS_TC_PASSWORD` sudah terdaftar untuk "Total Control Client plan ..." dan "Client tanpa subscription Fixed Asset" di suite lain dan dipakai ulang; kecocokan akun dengan PT Starter Mandiri, PT Maju Bersama, PT Profesional Jaya, PT Enterprise Raya, dan PT Tanpa FAMS perlu dikonfirmasi tim FE. Akun PT Maju Bersama (Growth) mungkin sama dengan akun default suite (`GS_TC_PASSWORD`).
  - TC-GS-NLU-454 tidak menyebut field wajib per Client, keberadaan Login User `Ahmad Fauzi` dan Division `Operations` di tiap Client plan, serta contoh validasi yang dibandingkan; spec mengasumsikan keduanya tersedia sebagai Pre-setup tiap Client dan hanya membandingkan popup serta hasil Submit.
  - TC-GS-NLU-454 Expected klausa "satu-satunya batas adalah Master Data Count Limit gabungan" tidak punya `Verifikasi` di spec ini: klausa itu tidak teramati tanpa mencapai Master Data Count Limit pada tiap tier, sedangkan spec tidak mengubah state Client. Mohon pemilik TC menetapkan apakah klausa dipindah ke TC limit per tier atau dihapus.
  - TC-GS-NLU-464 menyebut `Detail Tanpa FAMS` sebagai Pre-setup; spec memakai record milik spec bernama `Detail Tanpa FAMS {runId}-120`.
